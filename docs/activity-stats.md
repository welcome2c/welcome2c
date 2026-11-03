# GitHub 활동 통계 관리

계정 주인의 GitHub CLI 인증으로 소유 저장소와 작성 커밋, 생성 PR을 조회합니다.
공개 파일에는 합계·주별 건수·언어별 바이트만 저장하며 비공개 저장소 이름, 커밋 ID, 이메일과 토큰을 저장하지 않습니다.

```sh
python3 scripts/update_profile_stats.py
```

Python 표준 라이브러리와 인증된 `gh`가 필요합니다.
추가 Python 패키지나 외부 통계 이미지 서버는 사용하지 않습니다.
통계는 README에 표시된 집계 시점의 스냅샷입니다.
README에서는 커밋·PR·저장소 수와 집계일을 짧은 본문으로 표시합니다.

## 매일 자동 갱신

`.github/workflows/profile-activity.yml`은 한국 시간 매일 오전 08:17에 실행합니다.
GitHub 사정에 따라 실행이 늦어질 수 있으며, 다른 저장소의 커밋 직후에 실행되는 방식은 아닙니다.
Actions의 **Refresh profile activity → Run workflow**로도 실행할 수 있습니다.

비공개 저장소 집계를 활성화하려면 계정 주인이 전용 읽기 토큰을 한 번 등록해야 합니다.
등록 전에는 실행이 명확히 실패하며, 공개 저장소 수치만으로 기존 통계를 덮어쓰지 않습니다.

1. [Fine-grained personal access token 생성](https://github.com/settings/personal-access-tokens/new)에서 Resource owner를 `welcome2c`로 선택합니다.
2. Repository access를 **All repositories**로 선택하고, Repository permissions에서 **Contents: Read-only**, **Pull requests: Read-only**를 설정합니다. Metadata 읽기는 기본으로 포함됩니다.
3. [프로필 저장소 Secret 등록](https://github.com/welcome2c/welcome2c/settings/secrets/actions/new)에서 이름을 `PROFILE_STATS_TOKEN`으로 지정하고 토큰을 직접 등록합니다.

이 토큰은 집계 단계의 읽기에만 사용합니다.
프로필 저장소에 결과를 쓰는 단계는 해당 저장소에 한정된 기본 `GITHUB_TOKEN`을 사용합니다.
자동 커밋의 작성자는 GitHub Actions 봇이므로 본인의 작성 커밋 수에 포함되지 않습니다.
토큰이 만료되면 같은 Secret을 갱신해야 합니다.

- `assets/activity/summary.json`: 공개 가능한 집계만 포함한 스냅샷
- `scripts/update_profile_stats.py`: API 조회·중복 제거·집계 및 README 통계 갱신
- `scripts/render_profile_stats.py`: 필요할 때 별도로 실행하는 SVG 생성기. 생성 이미지는 현재 README에서 사용하지 않습니다.

커밋은 최근 365일 동안 계정과 연결된 작성자가 소유 저장소의 기본 브랜치에 남긴 고유 커밋을 집계합니다.
이메일이 계정과 연결되지 않은 커밋이나 병합 전 작업 브랜치의 커밋은 포함되지 않습니다.
PR은 같은 기간 해당 계정이 접근 가능한 저장소에 생성한 PR을 GitHub 검색으로 집계합니다.
스냅샷에는 주별 건수와 언어 비중도 보관합니다.
언어 비중은 현재 저장소 코드 바이트 기준으로, 커밋 비중이나 숙련도를 뜻하지 않습니다.

집계 정의는 GitHub 기본 기여 달력과 다를 수 있습니다.
원본 기여 달력의 표시 수치를 전체 저장소 커밋 수로 대체하거나 혼합하지 않습니다.
