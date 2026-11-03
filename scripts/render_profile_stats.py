"""Render the aggregate activity snapshot as accessible light/dark SVGs."""

from datetime import datetime
from html import escape
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "activity"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Apple SD Gothic Neo', sans-serif"
PALETTES = {
    "dark": {"bg": "#151b26", "text": "#eef2f8", "muted": "#b3bfd0", "line": "#344157", "accent": "#a97bff"},
    "light": {"bg": "#f6f8fc", "text": "#1d2737", "muted": "#516076", "line": "#cbd4e2", "accent": "#7040c5"},
}


def text(x, y, value, size, fill, weight=400, anchor="start"):
    return (f'<text x="{x:g}" y="{y:g}" fill="{fill}" font-family="{escape(FONT)}" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(str(value))}</text>')


def line(x1, y1, x2, y2, color, width=1):
    return f'<path d="M{x1:g} {y1:g}H{x2:g}" fill="none" stroke="{color}" stroke-width="{width}"/>'


def luminance(color):
    channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + .055) / 1.055) ** 2.4 for v in channels]
    return sum(a * b for a, b in zip(linear, (.2126, .7152, .0722)))


def contrast(a, b):
    high, low = sorted([luminance(a), luminance(b)], reverse=True)
    return (high + .05) / (low + .05)


def mark_color(color, background):
    if contrast(color, background) >= 3:
        return color
    rgb = [int(color[i:i + 2], 16) for i in (1, 3, 5)]
    for factor in (.9, .8, .7, .6, .5):
        candidate = "#" + "".join(f"{round(v * factor):02x}" for v in rgb)
        if contrast(candidate, background) >= 3:
            return candidate
    return color


def render(snapshot, theme, mobile):
    p = PALETTES[theme]
    assert contrast(p["text"], p["bg"]) >= 4.5
    assert contrast(p["muted"], p["bg"]) >= 4.5
    width, height = (640, 444) if mobile else (760, 260)
    padding = 24
    labels = ["작성 커밋", "생성 PR", "소유 저장소"]
    values = [snapshot["commits"], snapshot["pull_requests"], snapshot["owned_repositories"]]
    period_label = "전체 기간" if snapshot["period"].get("type") == "all_time" else "최근 1년"
    hints = [period_label, period_label, "포크 제외"]
    date = datetime.fromisoformat(snapshot["generated_at"]).astimezone(ZoneInfo("Asia/Seoul")).strftime("%Y.%m.%d")
    visible_languages = 3 if mobile else 4
    top = snapshot["languages"][:visible_languages]
    other = sum(item["bytes"] for item in snapshot["languages"][visible_languages:])
    languages = list(top) + ([{"name": "Other", "bytes": other, "color": "#8795a8"}] if other else [])
    total_bytes = sum(item["bytes"] for item in languages)
    weeks = snapshot["weeks"][:-1][-12:]
    descriptions = "; ".join(labels[i] + " " + str(values[i]) for i in range(3))
    description = (f'{date} 집계. {period_label} GitHub 활동. {descriptions}. '
                   '공개·비공개 소유 저장소를 합산하고 포크와 회사 GitLab은 제외합니다. '
                   '계정에 연결된 작성 커밋을 기본 브랜치에서 중복 제거합니다. '
                   '그래프는 완료된 최근 12주의 커밋이며 언어 비중은 코드 바이트 기준입니다.')
    body = [f'<rect width="{width}" height="{height}" rx="14" fill="{p["bg"]}"/>']
    cell = (width - 2 * padding) / 3
    for index, (label, value, hint) in enumerate(zip(labels, values, hints)):
        x = padding + index * cell
        body.append(text(x, 32 if mobile else 26, label, 24 if mobile else 14, p["muted"], 500))
        body.append(text(x - 1, 80 if mobile else 60, f"{value:,}", 44 if mobile else 32, p["text"], 600))
        body.append(text(x, 112 if mobile else 81, hint, 22 if mobile else 12, p["muted"]))
    divider = 132 if mobile else 96
    body.append(line(padding, divider, width - padding, divider, p["line"]))
    heading_y = 169 if mobile else 121
    body.append(text(padding, heading_y, "주별 커밋", 26 if mobile else 15, p["text"], 600))
    chart_right = width - padding if mobile else 433
    body.append(text(chart_right, heading_y, "완료된 최근 12주", 22 if mobile else 12, p["muted"], anchor="end"))
    left, right = (58, chart_right - 4) if mobile else (42, chart_right)
    top_y, bottom = (198, 264) if mobile else (144, 206)
    maximum = max([week["count"] for week in weeks] + [1])
    step = max(1, math.ceil(maximum / 4 / 5) * 5)
    ceiling = max(step, math.ceil(maximum / step) * step)
    ticks = sorted(set([0, ceiling // 2, ceiling]))
    for value in ticks:
        y = bottom - value / ceiling * (bottom - top_y)
        body.append(line(left, y, right, y, p["line"]))
        body.append(text(left - 10, y + (7 if mobile else 4), value, 22 if mobile else 12, p["muted"], anchor="end"))
    points = []
    for index, week in enumerate(weeks):
        x = left + index / max(1, len(weeks) - 1) * (right - left)
        y = bottom - week["count"] / ceiling * (bottom - top_y)
        points.append((x, y))
    path = "M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in points)
    area = path + f"L{right:g} {bottom:g}L{left:g} {bottom:g}Z"
    body.append(f'<path d="{area}" fill="{p["accent"]}" fill-opacity=".12"/>')
    body.append(f'<path d="{path}" fill="none" stroke="{p["accent"]}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
    for (x, y), week in zip(points, weeks):
        body.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.5" fill="{p["accent"]}"><title>{week["date"]} 주: {week["count"]}커밋</title></circle>')
    for index in (0, len(weeks) // 2, len(weeks) - 1):
        x = points[index][0]
        label = weeks[index]["date"][5:].replace("-", ".")
        anchor = "start" if index == 0 else "end" if index == len(weeks) - 1 else "middle"
        body.append(text(x, bottom + (28 if mobile else 20), label, 22 if mobile else 12, p["muted"], anchor=anchor))
    lang_left = padding if mobile else 473
    lang_y = 330 if mobile else 121
    body.append(text(lang_left, lang_y, "언어 비중", 24 if mobile else 15, p["text"], 600))
    if mobile:
        body.append(text(width - padding, lang_y, "코드 바이트 기준", 20, p["muted"], anchor="end"))
    bar_y = 345 if mobile else 136
    bar_width = width - padding - lang_left
    cursor = lang_left
    for item in languages:
        segment = item["bytes"] / total_bytes * bar_width if total_bytes else 0
        color = mark_color(item["color"], p["bg"])
        body.append(f'<rect x="{cursor:.2f}" y="{bar_y}" width="{segment:.2f}" height="{10 if mobile else 8}" fill="{color}"/>')
        cursor += segment
    for index, item in enumerate(languages):
        x = lang_left + (index % 2) * (300 if mobile else 138)
        y = (380 if mobile else 172) + (index // 2) * (28 if mobile else 25)
        color = mark_color(item["color"], p["bg"])
        percent = item["bytes"] / total_bytes * 100 if total_bytes else 0
        body.append(f'<circle cx="{x + 3}" cy="{y - (7 if mobile else 4)}" r="{4 if mobile else 3}" fill="{color}"/>')
        body.append(text(x + (16 if mobile else 12), y, f'{item["name"]} {percent:.1f}%', 22 if mobile else 12, p["text"]))
    if mobile:
        body.append(text(padding, height - 11, f"{date} · 공개·비공개 합산 · GitLab 제외", 20, p["muted"]))
    else:
        body.append(text(padding, height - 12, f"{date} 집계 · 공개·비공개 합산", 12, p["muted"]))
        body.append(text(width - padding, height - 12, "코드 바이트 기준 · 회사 GitLab 제외", 12, p["muted"], anchor="end"))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">'
           f'<title id="title">DevHoony의 GitHub 활동</title>'
           f'<desc id="description">{escape(description)}</desc>' + "\n".join(body) + "</svg>\n")
    name = f"dashboard-{'mobile-' if mobile else ''}{theme}.svg"
    (OUTPUT / name).write_text(svg)


def render_all(snapshot=None):
    snapshot = snapshot or json.loads((OUTPUT / "summary.json").read_text())
    for theme in PALETTES:
        for mobile in (False, True):
            render(snapshot, theme, mobile)


if __name__ == "__main__":
    render_all()
    print("Rendered 4 activity SVGs: desktop/mobile, light/dark.")
