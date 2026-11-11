"""Draw the logo honeycombs used on book covers, and the Web course's logo row for slides.

    python3 assets/logos/build_logo_sets.py

A honeycomb is seven hexagons: the course's own mark (or HTML5 for Web) in the middle, and six logos around it, so a
book about, say, data and networking shows at once that it is for mobile apps. Which logos each course gets is
LOGO_SETS in tools/course_themes.py. Every logo is unchanged; only the hexagon behind it is added. Licenses and
credit lines: assets/logos/README.md.

Output: assets/logos/honeycomb/<course>.svg, and assets/logos/web/web-logos-{light,dark}-bg.svg (one row, for slides).
"""
import math
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from course_themes import LOGO_FILES, LOGO_SETS  # noqa: E402

NOTE = "<!-- Made by assets/logos/build_logo_sets.py from unchanged logos; see assets/logos/README.md for each license. -->"


def nested(path, x, y, size, prefix, white_text=False):
    """The logo file as a nested <svg> at (x, y), size by size, with its ids and class names made unique."""
    text = re.sub(r"<\?xml[^>]*>|<!--.*?-->|<!DOCTYPE[^>]*>", "", (ROOT / path).read_text(), flags=re.S)

    def fix(m):
        attrs = m.group(1)
        if "viewBox" not in attrs:  # for example the React and Android logos: give them a viewBox so they scale
            w = re.search(r'\swidth="([\d.]+)', attrs).group(1)
            h = re.search(r'\sheight="([\d.]+)', attrs).group(1)
            attrs += f' viewBox="0 0 {w} {h}"'
        attrs = re.sub(r'\s(width|height|x|y|id)="[^"]*"', "", attrs)
        if white_text:  # the HTML5 wordmark has no fill of its own, so it takes this one
            attrs += ' fill="#FFFFFF"'
        return f'<svg{attrs} x="{x:.1f}" y="{y:.1f}" width="{size:.1f}" height="{size:.1f}">'

    text = re.sub(r"<svg\b([^>]*)>", fix, text, count=1)
    if "/icons/courses/" in path:  # a course mark: drop its small corner square, which the hexagon would cut in half
        text = re.sub(r'<rect x="196"[^>]*/>', "", text)
    # In one file, ids and CSS classes are shared by every logo: give each logo's its own prefix.
    text = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{prefix}{m.group(1)}"', text)
    text = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{prefix}{m.group(1)})", text)
    text = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{prefix}{m.group(1)}"', text)
    classes = set(c for value in re.findall(r'class="([^"]+)"', text) for c in value.split())
    text = re.sub(r'class="([^"]+)"', lambda m: 'class="' + " ".join(prefix + c for c in m.group(1).split()) + '"', text)
    for c in sorted(classes, key=len, reverse=True):
        text = re.sub(rf"\.{re.escape(c)}(?![\w-])", f".{prefix}{c}", text)
    return text


def hexagon(cx, cy, r):
    """Points of a hexagon with a point at the top."""
    return " ".join(f"{cx + r * math.cos(math.radians(a)):.1f},{cy + r * math.sin(math.radians(a)):.1f}"
                    for a in range(-90, 270, 60))


def tile(name):
    """(file, hexagon color, logo size as a share of the hexagon's radius) for a logo name or a course mark."""
    if name in LOGO_FILES:
        return LOGO_FILES[name]
    path = f"assets/icons/courses/{name}.svg"  # a course mark: a square in the course color, so the hexagon matches it
    color = re.search(r'<rect[^>]*fill="(#[0-9A-Fa-f]{6})"', (ROOT / path).read_text()).group(1)
    return path, color, 1.8  # drawn larger than the hexagon: the symbol fills it, and the square's edges are cut off


def honeycomb(center, around):
    r, gap = 200, 16
    w = math.sqrt(3) * r
    step_x, step_y = w + gap, 1.5 * r + gap * math.sqrt(3) / 2
    spots = [(0, 0), (-step_x / 2, -step_y), (step_x / 2, -step_y), (step_x, 0), (step_x / 2, step_y), (-step_x / 2, step_y), (-step_x, 0)]
    half_w, half_h = step_x + w / 2, step_y + r
    body = ""
    for i, (name, (cx, cy)) in enumerate(zip([center] + around, spots)):
        path, color, share = tile(name)
        size = share * r
        body += (f'<clipPath id="tile{i}"><polygon points="{hexagon(cx, cy, r)}"/></clipPath>'
                 f'<polygon points="{hexagon(cx, cy, r)}" fill="{color}"/>'
                 f'<g clip-path="url(#tile{i})">{nested(path, cx - size / 2, cy - size / 2, size, f"t{i}_")}</g>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-half_w:.1f} {-half_h:.1f} {2 * half_w:.1f} {2 * half_h:.1f}">'
            f"{NOTE}{body}</svg>")


def row(names, white_text):
    t, g = 240, 32
    body = "".join(nested(LOGO_FILES[n][0], i * (t + g), 0, t, f"r{i}_", white_text and n == "html5") for i, n in enumerate(names))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {len(names) * t + (len(names) - 1) * g} {t}">{NOTE}{body}</svg>'


if __name__ == "__main__":
    out = ROOT / "assets/logos/honeycomb"
    out.mkdir(exist_ok=True)
    for course, (center, around) in LOGO_SETS.items():
        assert len(around) == 6, course
        (out / f"{course}.svg").write_text(honeycomb(center, around))
        print("wrote", (out / f"{course}.svg").relative_to(ROOT))
    names = ["html5", "css", "javascript", "typescript", "react"]
    (ROOT / "assets/logos/web/web-logos-light-bg.svg").write_text(row(names, False))
    (ROOT / "assets/logos/web/web-logos-dark-bg.svg").write_text(row(names, True))
    print("wrote assets/logos/web/web-logos-light-bg.svg and web-logos-dark-bg.svg")
