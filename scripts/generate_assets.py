"""Regenerate the profile's self-contained SVG artwork. Python stdlib only."""

from base64 import b64encode
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, monospace"


def svg(width, height, title, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">\n'
        f'<title>{escape(title)}</title>\n{body}\n</svg>\n'
    )


def text(x, y, value, size, color, weight=400, mono=False, spacing=0):
    font = MONO if mono else FONT
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-family="{escape(font)}" '
        f'font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}">'
        f'{escape(value)}</text>'
    )


def hero(theme, mobile=False):
    width, height = (720, 390) if mobile else (1200, 340)
    bg = "#142133" if theme == "light" else "#192b43"
    muted, foreground, accent = "#c1ccdc", "#f4f7fc", "#f5ad75"
    x = 44 if mobile else 60
    body = f'<rect width="{width}" height="{height}" rx="18" fill="{bg}"/>'
    if mobile:
        body += '<g opacity=".23" transform="translate(535 95) rotate(-14)"><rect width="145" height="160" rx="30" fill="none" stroke="#8191a7" stroke-width="2"/><rect x="105" y="-8" width="45" height="45" rx="13" fill="#f5ad75"/></g>'
        body += text(x, 61, "TAP STUDIO / DEVHOONY", 28, muted, 500, True, 1)
        body += text(x, 148, "Ideas into", 68, foreground, 600, spacing=-2)
        body += text(x, 224, "everyday apps.", 68, accent, 600, spacing=-2)
        body += text(x, 300, "Android Engineer", 28, muted)
        body += text(x, 342, "Donghoon Kim", 28, muted)
    else:
        body += '<g transform="translate(977 90) rotate(-14)"><rect width="150" height="170" rx="33" fill="none" stroke="#52637c" stroke-width="2"/><rect x="23" y="25" width="104" height="120" rx="23" fill="none" stroke="#52637c" stroke-width="2"/><rect x="111" y="-6" width="49" height="49" rx="14" fill="#f5ad75"/><rect x="39" y="129" width="49" height="49" rx="14" fill="#30445f"/></g>'
        body += '<circle cx="65" cy="58" r="5" fill="#f5ad75"/>'
        body += text(85, 65, "TAP STUDIO / DEVHOONY", 19, muted, 500, True, 2)
        body += text(x, 151, "Ideas into", 70, foreground, 600, spacing=-2)
        body += text(x, 231, "everyday apps.", 70, accent, 600, spacing=-2)
        body += text(x, 288, "Android Engineer · Donghoon Kim", 24, muted)
    name = "hero-mobile" if mobile else "hero"
    (ASSETS / f"{name}-{theme}.svg").write_text(
        svg(width, height, "Tap Studio · DevHoony — Ideas into everyday apps.", body)
    )


PRODUCTS = [
    ("weathercast", "WeatherCast", "WEATHER & LIFESTYLE", "#e2eef7", "#20384c", "#243f56", "#e1f0fc", "weathercast-icon.jpg"),
    ("pixel-walker", "Pixel Walker RPG", "STEPS INTO ADVENTURE", "#e4ecdd", "#293c30", "#314b35", "#e2efd9", "pixel-walker-icon.jpg"),
    ("gemiboard", "GemiBoard", "TYPE. REFINE. SEND.", "#eae5f3", "#353046", "#493a62", "#eee6fb", "gemiboard-icon.png"),
    ("pop-quiz-daily", "Pop Quiz Daily", "A LITTLE SMARTER, DAILY.", "#f5e7d9", "#46372e", "#684936", "#faeadc", "pop-quiz-daily-icon.jpg"),
]


def product(data, theme):
    slug, name, caption, light, dark, light_fg, dark_fg, icon = data
    bg, fg = (light, light_fg) if theme == "light" else (dark, dark_fg)
    content = (ASSETS / "apps" / icon).read_bytes()
    mime = "image/png" if icon.endswith("png") else "image/jpeg"
    encoded = b64encode(content).decode()
    body = f'<rect width="720" height="280" rx="16" fill="{bg}"/>'
    body += '<defs><clipPath id="app-icon"><rect x="48" y="38" width="104" height="104" rx="23"/></clipPath></defs>'
    body += f'<image x="48" y="38" width="104" height="104" clip-path="url(#app-icon)" href="data:{mime};base64,{encoded}"/>'
    body += text(48, 192, caption, 19, fg, 500, True, 1.1)
    body += text(46, 246, name, 47, fg, 600, spacing=-1)
    body += f'<path d="M604 75h45m-13-13 13 13-13 13" fill="none" stroke="{fg}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity=".55"/>'
    (ASSETS / f"{slug}-{theme}.svg").write_text(svg(720, 280, name + " · " + caption, body))


if __name__ == "__main__":
    ASSETS.mkdir(exist_ok=True)
    for theme in ("light", "dark"):
        hero(theme)
        hero(theme, mobile=True)
        for data in PRODUCTS:
            product(data, theme)
    print("Generated 12 profile SVG assets.")
