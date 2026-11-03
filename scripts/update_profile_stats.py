"""Collect owner activity with gh; publish aggregate statistics, never private repo names.

Run: python3 scripts/update_profile_stats.py
Requires an authenticated GitHub CLI with read access to the owner's repositories.
"""

from collections import Counter
from datetime import datetime, timedelta, timezone
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
OWNER = "welcome2c"
OUTPUT = ROOT / "assets" / "activity"


def graphql(gh, query, **variables):
    result = subprocess.run(
        [gh, "api", "graphql", "--input", "-"],
        input=json.dumps({"query": query, "variables": variables}),
        text=True, capture_output=True, check=False,
    )
    if result.returncode:
        raise RuntimeError("GitHub query failed; statistics were not updated.")
    response = json.loads(result.stdout)
    if response.get("errors"):
        raise RuntimeError("GitHub returned incomplete data; statistics were not updated.")
    return response["data"]


def collect(gh):
    end = datetime.now(timezone.utc).replace(microsecond=0)
    start = end - timedelta(days=365)
    first = graphql(gh, '''query($login:String!,$q:String!){
      viewer{login} user(login:$login){id}
      search(type:ISSUE,query:$q,first:1){issueCount}
    }''', login=OWNER, q="author:" + OWNER + " is:pr created:" +
                    start.strftime("%Y-%m-%dT%H:%M:%SZ") + ".." +
                    end.strftime("%Y-%m-%dT%H:%M:%SZ"))
    if first["viewer"]["login"].lower() != OWNER:
        raise RuntimeError("Use the profile owner's gh account to collect complete statistics.")
    author = first["user"]["id"]
    query = '''query($login:String!,$author:ID!,$from:GitTimestamp!,$to:GitTimestamp!,$after:String){
      user(login:$login){repositories(first:100,after:$after,ownerAffiliations:OWNER,isFork:false){
        pageInfo{hasNextPage endCursor}
        nodes{nameWithOwner isPrivate stargazerCount
          languages(first:100,orderBy:{field:SIZE,direction:DESC}){edges{size node{name color}}}
          defaultBranchRef{name target{... on Commit{
            history(first:100,author:{id:$author},since:$from,until:$to){
              totalCount pageInfo{hasNextPage endCursor} nodes{oid committedDate}
            }
          }}}
        }
      }}
    }'''
    commits = {}
    languages = Counter()
    colors = {}
    repository_count = public_count = stars = 0
    after = None
    while True:
        data = graphql(gh, query, login=OWNER, author=author,
                       **{"from": start.isoformat(), "to": end.isoformat(), "after": after})
        connection = data["user"]["repositories"]
        for repo in connection["nodes"]:
            repository_count += 1
            public_count += not repo["isPrivate"]
            if not repo["isPrivate"]:
                stars += repo["stargazerCount"]
            if repo["nameWithOwner"].lower() != OWNER + "/" + OWNER:
                for edge in repo["languages"]["edges"]:
                    name = edge["node"]["name"]
                    languages[name] += edge["size"]
                    colors[name] = edge["node"]["color"] or "#8795a8"
            branch = repo["defaultBranchRef"]
            if not branch:
                continue
            history = branch["target"]["history"]
            while True:
                for commit in history["nodes"]:
                    commits[commit["oid"]] = commit["committedDate"]
                if not history["pageInfo"]["hasNextPage"]:
                    break
                name = repo["nameWithOwner"].split("/", 1)[1]
                history = graphql(gh, '''query($owner:String!,$name:String!,$branch:String!,$author:ID!,
                    $from:GitTimestamp!,$to:GitTimestamp!,$after:String!){
                  repository(owner:$owner,name:$name){ref(qualifiedName:$branch){target{... on Commit{
                    history(first:100,after:$after,author:{id:$author},since:$from,until:$to){
                      pageInfo{hasNextPage endCursor} nodes{oid committedDate}
                    }
                  }}}}
                }''', owner=OWNER, name=name, branch="refs/heads/" + branch["name"],
                    author=author, **{"from": start.isoformat(), "to": end.isoformat(),
                    "after": history["pageInfo"]["endCursor"]})["repository"]["ref"]["target"]["history"]
        if not connection["pageInfo"]["hasNextPage"]:
            break
        after = connection["pageInfo"]["endCursor"]
    days = Counter(value[:10] for value in commits.values())
    first_monday = start.date() - timedelta(days=start.weekday())
    last_monday = end.date() - timedelta(days=end.weekday())
    weeks = []
    cursor = first_monday
    while cursor <= last_monday:
        count = sum(days[(cursor + timedelta(days=i)).isoformat()] for i in range(7))
        weeks.append({"date": cursor.isoformat(), "count": count})
        cursor += timedelta(days=7)
    assert sum(week["count"] for week in weeks) == len(commits)
    return {
        "schema_version": 1, "login": OWNER, "generated_at": end.isoformat(),
        "period": {"from": start.isoformat(), "to": end.isoformat()},
        "scope": {
            "commits": "Unique commits authored by the account in owned non-fork default branches; public and private.",
            "pull_requests": "Pull requests created by the account across accessible repositories in the same period.",
            "languages": "Owned non-fork repository code bytes, excluding the profile repository; public and private.",
            "company_gitlab_included": False,
        },
        "commits": len(commits), "pull_requests": first["search"]["issueCount"],
        "commit_days": len(days), "owned_repositories": repository_count,
        "public_repositories": public_count, "public_stars": stars, "weeks": weeks,
        "languages": [{"name": name, "bytes": size, "color": colors[name]}
                      for name, size in languages.most_common()],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-only", action="store_true")
    args = parser.parse_args()
    gh = shutil.which("gh") or str(Path.home() / ".local/bin/gh")
    snapshot = collect(gh)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    if not args.snapshot_only:
        readme = ROOT / "README.md"
        date = datetime.fromisoformat(snapshot["generated_at"]).astimezone(ZoneInfo("Asia/Seoul")).strftime("%Y.%m.%d")
        activity = (f'<!-- activity-stats:start -->\n'
                    f'**GitHub 활동** · 최근 1년 작성 커밋 **{snapshot["commits"]:,}** · '
                    f'생성 PR **{snapshot["pull_requests"]:,}** · '
                    f'소유 저장소 **{snapshot["owned_repositories"]:,}**' + '\\\n' +
                    f'<sub>{date} 집계 · 공개·비공개 합산 · 회사 GitLab 제외</sub>\n'
                    '<!-- activity-stats:end -->')
        pattern = r'<!-- activity-stats:start -->.*?<!-- activity-stats:end -->'
        content, replacements = re.subn(pattern, lambda m: activity, readme.read_text(), count=1, flags=re.S)
        if replacements != 1:
            raise RuntimeError("Activity markers missing; statistics were not updated.")
        readme.write_text(content)
    (OUTPUT / "summary.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: snapshot[key] for key in
          ["login", "generated_at", "commits", "pull_requests", "commit_days", "owned_repositories"]},
          ensure_ascii=False))
