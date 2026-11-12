"""The look of each newer course: colors, fonts, logos, cover, and title-slide details.

build_lessons.py adds these to its COURSES. Every course has its own look, so no two courses share a palette,
a pair of fonts, or a cover pattern. Each course's planning/slide-design.md describes its look in words.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATIC_WEIGHTS = {"Regular": "400", "Italic": "400", "Bold": "700", "BoldItalic": "700"}


def faces(*families):
    """@font-face entries for (family name, folder in assets/fonts) pairs. Variable fonts cover every weight;
    for static fonts, only regular, italic, bold, and bold italic are loaded."""
    out = []
    for name, folder in families:
        for f in sorted((ROOT / "assets/fonts" / folder).glob("*.ttf")):
            italic = "Italic" in f.stem
            style = "font-style:italic;" if italic else "font-style:normal;"
            if "[" in f.stem:
                weight = "100 900"
            else:
                suffix = f.stem.split("-")[-1]
                if suffix not in STATIC_WEIGHTS:
                    continue
                weight = STATIC_WEIGHTS[suffix]
            out.append((name, str(f.relative_to(ROOT)), weight, "truetype", style))
    return out


def theme(primary, surface, border, text, muted, dark, code, note_tint, note_text):
    """The color groups that build_lessons.py reads. dark is the title slides: background, surface, border, text, muted, primary."""
    bg, dsurface, dborder, dtext, dmuted, dprimary = dark
    return {
        "light": {"text": text, "text-muted": muted, "surface": surface, "border": border, "primary": primary},
        "dark": {"background": bg, "surface": dsurface, "border": dborder, "text": dtext, "text-muted": dmuted, "primary": dprimary},
        "code": code,
        "callout": {"note": {"accent": primary, "tint": note_tint, "text": note_text, "label": "Note"}},
    }


def texts(title, km_second, points_en, points_km, badge_en="A Practical Guide", badge_km="រៀន និងអនុវត្តជាក់ស្ដែង", second="Programming"):
    return {
        "en": {"title": title, "second": second, "badge": badge_en, "toc": "Contents", "inside": "In this section", "points": points_en},
        "km": {"title": title, "second": second, "badge": badge_km, "toc": "មាតិកា", "inside": "ក្នុងផ្នែកនេះ", "points": points_km},
    }


# ------------------------------------------------------------------ cover patterns
# Each returns HTML for a 2480 x 3508 px page (A4 at 300 dpi). mm is pixels per millimetre.
# The top of the page (title) and the clear area on the right (marks) stay empty.

def flutter_motif(w, h, mm):
    """Nested, offset frames: a widget tree seen from above. Indigo and sky blue."""
    out = ""
    for i in range(8):
        size = (40 + i * 15) * mm
        x, y = w - size - 6 * mm + i * 3 * mm, h - size - 8 * mm + i * 4 * mm
        color = "#4FC3F7" if i % 3 == 0 else "#6C63FF"
        alpha = 0.55 - i * 0.045
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{size}px;height:{size}px;'
                f'border:{1.4 * mm}px solid {color};opacity:{alpha:.2f}"></div>')
    for i in range(5):
        out += (f'<div style="position:absolute;left:{20 * mm}px;top:{(206 + i * 13) * mm}px;width:{(26 + i * 11) * mm}px;'
                f'height:{6 * mm}px;background:{"#4FC3F7" if i == 2 else "#2A2470"}"></div>')
    return out


def ios_motif(w, h, mm):
    """A loose grid of screen outlines, some filled with plum and gold: apps on a home screen. Warm sand page."""
    out = ""
    for row in range(3):
        for col in range(5):
            x, y = (14 + col * 40) * mm, (178 + row * 31) * mm
            if col >= 3 and row == 0:
                continue  # the clear area for the Swift logo
            fill = {(1, 1): "#5A2D6E", (3, 2): "#C99A2E", (0, 2): "#C99A2E", (4, 2): "#5A2D6E"}.get((row, col), "transparent")
            out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{26 * mm}px;height:{26 * mm}px;'
                    f'border:{0.9 * mm}px solid #5A2D6E;opacity:{0.85 if fill != "transparent" else 0.28};background:{fill}"></div>')
    return out


def kotlin_motif(w, h, mm):
    """Diagonal bands in magenta and orange, rising from the lower left: Kotlin's angles. Near-black page."""
    out = ""
    colors = ["#B4237A", "#FF8A3D", "#7A1E5C", "#E5487F", "#3A1630"]
    for i, color in enumerate(colors):
        left = (-40 + i * 30) * mm
        out += (f'<div style="position:absolute;left:{left}px;top:{(300 + i * 4) * mm}px;width:{130 * mm}px;height:{16 * mm}px;'
                f'background:{color};transform:rotate(-38deg);transform-origin:left top;opacity:.9"></div>')
    return out


def android_motif(w, h, mm):
    """A grid of dots, some grown into large green circles: Material's round shapes. Pale green page."""
    out = ""
    for row in range(6):
        for col in range(9):
            x, y = (20 + col * 20) * mm, (180 + row * 15) * mm
            big = (row, col) in {(1, 2), (3, 5), (4, 1), (2, 7)}
            size = (11 if big else 3) * mm
            color = "#1E8A4C" if (row + col) % 3 else "#3DDC84"
            out += (f'<div style="position:absolute;left:{x - size / 2}px;top:{y - size / 2}px;width:{size}px;height:{size}px;'
                    f'border-radius:50%;background:{color};opacity:{0.95 if big else 0.45}"></div>')
    return out


def javascript_motif(w, h, mm):
    """Huge braces, brackets, and a semicolon in yellow and grey on black: the punctuation of JavaScript."""
    font = (ROOT / "assets/fonts/space-mono/SpaceMono-Bold.ttf").as_uri()
    marks = [("{", 12, 196, 112, "#F7DF1E", 1), ("}", 92, 196, 112, "#F7DF1E", .9), ("( )", 38, 222, 40, "#5C5A4A", 1),
             (";", 150, 178, 80, "#F7DF1E", .5)]
    return f"<style>@font-face{{font-family:SM;src:url({font})}}</style>" + "".join(
        f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;font:700 {size * mm}px/1 SM, monospace;'
        f'color:{color};opacity:{alpha}">{text}</div>' for text, x, y, size, color, alpha in marks)


def react_native_motif(w, h, mm):
    """Lanes like a transit map: parallel lines with stops, where messages travel between the JavaScript side and
    the native side. Cyan and teal on dark slate."""
    out = ""
    lanes = [(20, 0.9, "#61DAFB", [40, 96, 150]), (34, 0.5, "#2B8AA8", [24, 70, 128, 176]), (48, 0.9, "#61DAFB", [58, 112]),
             (62, 0.35, "#AAB4BE", [30, 90, 160]), (76, 0.6, "#2B8AA8", [46, 136])]
    for i, (y, alpha, color, stops) in enumerate(lanes):
        top = (184 + y) * mm
        out += f'<div style="position:absolute;left:0;top:{top}px;width:{w}px;height:{1.4 * mm}px;background:{color};opacity:{alpha}"></div>'
        for x in stops:
            out += (f'<div style="position:absolute;left:{(x - 3) * mm}px;top:{top - 2.3 * mm}px;width:{6 * mm}px;height:{6 * mm}px;'
                    f'border-radius:50%;background:#1B1E24;border:{1.4 * mm}px solid {color};opacity:{max(alpha, .6)}"></div>')
    return out


def cicd_motif(w, h, mm):
    """A pipeline: rows of square stages joined by lines, most of them passed (lime), one still running. Slate page."""
    out = ""
    for row in range(3):
        y = (196 + row * 26) * mm
        out += f'<div style="position:absolute;left:{14 * mm}px;top:{y + 7 * mm}px;width:{182 * mm}px;height:{1.2 * mm}px;background:#4E6A82"></div>'
        for col in range(6):
            x = (14 + col * 34) * mm
            done = col < 5 - row
            out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{15 * mm}px;height:{15 * mm}px;'
                    f'background:{"#9BE15D" if done else "#18222C"};border:{1.2 * mm}px solid {"#9BE15D" if done else "#7C93A8"}"></div>')
    return out


def testing_motif(w, h, mm):
    """A grid of test results: rows of green ticks, with one red cross, like a test report. Pale lavender page."""
    cells = ""
    for row in range(4):
        for col in range(8):
            x, y = 14 + col * 23, 186 + row * 22
            failed = (row, col) == (2, 5)
            mark = ('<path d="M5 5 L15 15 M15 5 L5 15" stroke="#C2332F" stroke-width="3" fill="none"/>' if failed else
                    '<path d="M4 10.5 L8.5 15 L16 6" stroke="#2FB36B" stroke-width="3" fill="none" stroke-linecap="square"/>')
            cells += (f'<svg style="position:absolute;left:{x * mm}px;top:{y * mm}px" width="{16 * mm}" height="{16 * mm}" viewBox="0 0 20 20">'
                      f'<rect x="1" y="1" width="18" height="18" fill="#FFFFFF" stroke="{"#C2332F" if failed else "#CBBDE6"}" stroke-width="1"/>{mark}</svg>')
    return cells


def architecture_motif(w, h, mm):
    """A blueprint: a fine grid, with a layered drawing of boxes and connecting lines in white and azure. Navy page."""
    grid = (f'<div style="position:absolute;left:0;top:{170 * mm}px;width:{w}px;height:{h - 170 * mm}px;'
            f'background-image:linear-gradient(#2A5D8A 1px,transparent 1px),linear-gradient(90deg,#2A5D8A 1px,transparent 1px);'
            f'background-size:{8 * mm}px {8 * mm}px;opacity:.55"></div>')
    boxes = [(20, 184, 52, 16, "#FFFFFF"), (84, 184, 52, 16, "#FFFFFF"), (148, 184, 44, 16, "#FFFFFF"),
             (20, 216, 116, 16, "#7FB8EA"), (148, 216, 44, 16, "#7FB8EA"), (20, 248, 172, 14, "#3D8FD6")]
    out = grid
    for x, y, bw, bh, color in boxes:
        out += (f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;width:{bw * mm}px;height:{bh * mm}px;'
                f'border:{0.8 * mm}px solid {color};background:#0D2A44"></div>')
    for x in (46, 110, 170):
        out += f'<div style="position:absolute;left:{x * mm}px;top:{200 * mm}px;width:{0.8 * mm}px;height:{16 * mm}px;background:#7FB8EA"></div>'
    for x in (78, 170):
        out += f'<div style="position:absolute;left:{x * mm}px;top:{232 * mm}px;width:{0.8 * mm}px;height:{16 * mm}px;background:#3D8FD6"></div>'
    return out


def blueprint_motif(w, h, mm):
    """A blueprint: a faint amber grid over a deep-navy page, with one bright drawn square and corner ticks,
    like an architect's plan. Security Fundamentals is the foundation the whole program is built on."""
    out = ""
    # faint grid lines across the lower part of the page
    step = 16 * mm
    x = 0
    while x <= w:
        out += (f'<div style="position:absolute;left:{x}px;top:{150 * mm}px;width:1px;height:{150 * mm}px;'
                f'background:#F2A541;opacity:.10"></div>')
        x += step
    y = 150 * mm
    while y <= h:
        out += (f'<div style="position:absolute;left:0;top:{y}px;width:{w}px;height:1px;'
                f'background:#F2A541;opacity:.10"></div>')
        y += step
    # one bright drawn square, centred low, with corner ticks
    cx, cy, s = 150 * mm, 232 * mm, 80 * mm
    lft, top = cx - s / 2, cy - s / 2
    out += (f'<div style="position:absolute;left:{lft}px;top:{top}px;width:{s}px;height:{s}px;'
            f'border:{1.4 * mm}px solid #F2A541;opacity:.9"></div>')
    inner = 44 * mm
    out += (f'<div style="position:absolute;left:{cx - inner / 2}px;top:{cy - inner / 2}px;width:{inner}px;height:{inner}px;'
            f'border:{1 * mm}px solid #6FA8DC;opacity:.85"></div>')
    for dx, dy in ((lft, top), (lft + s, top), (lft, top + s), (lft + s, top + s)):
        out += (f'<div style="position:absolute;left:{dx - 3 * mm}px;top:{dy - 3 * mm}px;width:{6 * mm}px;height:{6 * mm}px;'
                f'background:#F2A541"></div>')
    return out


def circuit_motif(w, h, mm):
    """Circuit-board traces: teal lines with square pads and vias, fanning out across the lower page.
    How Computers Work opens up the machine and looks inside."""
    out = ""
    teal, dim = "#2DD4BF", "#1C4C47"
    # a few horizontal/vertical traces with right-angle turns and pads at the ends
    # Kept in the lower-right quadrant (x >= 96), clear of the bottom-left author line.
    traces = [
        [(104, 300), (104, 232), (150, 232), (150, 272)],
        [(150, 272), (196, 272)],
        [(150, 232), (196, 232), (196, 300)],
        [(124, 300), (124, 252), (150, 252)],
        [(104, 286), (176, 286)],
    ]
    for pts in traces:
        for i in range(len(pts) - 1):
            x1, y1 = pts[i]; x2, y2 = pts[i + 1]
            left, top = min(x1, x2), min(y1, y2)
            wpx = max(abs(x2 - x1), 0.8) * mm
            hpx = max(abs(y2 - y1), 0.8) * mm
            out += (f'<div style="position:absolute;left:{left * mm}px;top:{top * mm}px;width:{wpx}px;height:{hpx}px;'
                    f'background:{teal};opacity:.55"></div>')
    # square pads at trace ends and junctions
    pads = [(104, 300), (150, 272), (196, 272), (196, 300), (150, 252), (124, 300), (150, 232)]
    for x, y in pads:
        s = 5 * mm
        out += (f'<div style="position:absolute;left:{x * mm - s / 2}px;top:{y * mm - s / 2}px;width:{s}px;height:{s}px;'
                f'background:{teal}"></div>')
    # faint grid of dim vias behind it, right side only
    for gx in range(0, 6):
        for gy in range(0, 5):
            out += (f'<div style="position:absolute;left:{(100 + gx * 20) * mm}px;top:{(236 + gy * 15) * mm}px;'
                    f'width:{2 * mm}px;height:{2 * mm}px;background:{dim};opacity:.5"></div>')
    return out


def security_motif(w, h, mm):
    """Nested squares, like the doors of a vault, in dark red tones, with one bright crimson ring. Near-black page."""
    out = ""
    cx, cy = 150 * mm, 232 * mm
    for i in range(7):
        size = (14 + i * 15) * mm
        color = "#D7264E" if i == 2 else "#5A1424"
        out += (f'<div style="position:absolute;left:{cx - size / 2}px;top:{cy - size / 2}px;width:{size}px;height:{size}px;'
                f'border:{1.6 * mm}px solid {color};opacity:{0.95 if i == 2 else 0.8 - i * 0.07}"></div>')
    out += f'<div style="position:absolute;left:{cx - 3 * mm}px;top:{cy - 3 * mm}px;width:{6 * mm}px;height:{6 * mm}px;background:#D7264E"></div>'
    return out


def observability_motif(w, h, mm):
    """Three charts stacked like a dashboard: a steady line, a bar chart, and a line with one spike. Dark green page."""
    def line(points, top, color, width):
        pts = " ".join(f"{x * 2.4},{y}" for x, y in points)
        return (f'<svg style="position:absolute;left:{18 * mm}px;top:{top * mm}px" width="{176 * mm}" height="{30 * mm}" viewBox="0 0 176 30">'
                f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="miter"/></svg>')
    calm = [(i * 6, 18 + (3 if i % 3 == 0 else -2 if i % 3 == 1 else 0)) for i in range(13)]
    spike = [(i * 6, 22 - (16 if i == 8 else 2 if i % 2 else 0)) for i in range(13)]
    bars = "".join(f'<div style="position:absolute;left:{(18 + i * 11) * mm}px;top:{(236 - hgt) * mm}px;width:{7 * mm}px;height:{hgt * mm}px;'
                   f'background:{"#A3D139" if i == 9 else "#3E5A2A"}"></div>' for i, hgt in enumerate([8, 11, 9, 13, 10, 12, 9, 14, 11, 20, 10, 12, 9, 11, 10, 8]))
    return line(calm, 172, "#6F8F3A", 1.2) + bars + line(spike, 240, "#A3D139", 1.4)


def performance_motif(w, h, mm):
    """A flame graph: stacked bars, wide at the bottom and narrower above, in warm orange and amber. Dark brown page."""
    rows = [[(14, 182)], [(14, 104), (122, 74)], [(14, 60), (78, 38), (122, 50)], [(20, 40), (84, 20), (128, 30)],
            [(26, 22), (134, 12)]]
    colors = ["#7A2E0A", "#B4400F", "#D9480F", "#F07A2A", "#FFC078"]
    out = ""
    for level, bars in enumerate(rows):
        y = 248 - level * 15
        for x, width in bars:
            out += (f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;width:{width * mm}px;height:{13 * mm}px;'
                    f'background:{colors[level]}"></div>')
    return out


def release_motif(w, h, mm):
    """Version tags laid out like luggage labels, and one red stamp: RELEASED. Cream page, navy ink."""
    font = (ROOT / "assets/fonts/courier-prime/CourierPrime-Bold.ttf").as_uri()
    tags = [("v1.3.2", 18, 190, -4), ("v1.4.0", 70, 182, 3), ("v1.4.1", 124, 196, -2), ("v1.5.0", 40, 226, 2)]
    out = f"<style>@font-face{{font-family:CP;src:url({font})}}</style>"
    for text, x, y, angle in tags:
        out += (f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;width:{46 * mm}px;height:{18 * mm}px;'
                f'border:{0.8 * mm}px solid #1C2B4A;background:#FFFFFF;transform:rotate({angle}deg);display:flex;align-items:center;'
                f'justify-content:center;font:700 {7 * mm}px CP, monospace;color:#1C2B4A">{text}</div>')
    out += (f'<div style="position:absolute;left:{104 * mm}px;top:{234 * mm}px;padding:{2 * mm}px {5 * mm}px;border:{1.4 * mm}px solid #C8102E;'
            f'transform:rotate(-12deg);font:700 {9 * mm}px CP, monospace;color:#C8102E;letter-spacing:{0.6 * mm}px">RELEASED</div>')
    return out


def networking_motif(w, h, mm):
    """A small network: round nodes joined by lines, one route lit in coral from a phone to a server. Navy page."""
    nodes = {"a": (24, 200), "b": (66, 186), "c": (108, 210), "d": (150, 190), "e": (186, 214), "f": (44, 240), "g": (96, 252),
             "h": (140, 238), "i": (178, 256)}
    links = [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("a", "f"), ("f", "g"), ("g", "h"), ("h", "i"), ("b", "g"), ("c", "h"), ("d", "h"), ("e", "i")]
    lit = {("a", "b"), ("b", "c"), ("c", "h"), ("h", "i")}
    svg = f'<svg style="position:absolute;left:0;top:0" width="{w}" height="{h}" viewBox="0 0 210 297">'
    for x, y in links:
        on = (x, y) in lit
        (x1, y1), (x2, y2) = nodes[x], nodes[y]
        svg += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{"#FF7A59" if on else "#33415C"}" stroke-width="{1.6 if on else 1}"/>'
    for name, (x, y) in nodes.items():
        on = name in ("a", "i")
        svg += f'<circle cx="{x}" cy="{y}" r="{4.5 if on else 3}" fill="{"#FF7A59" if on else "#101828"}" stroke="{"#FF7A59" if on else "#5B6B8A"}" stroke-width="1"/>'
    return svg + "</svg>"


def accessibility_motif(w, h, mm):
    """Large dots in cells of six, like braille, in blue, with one cell in yellow. White page, strong contrast."""
    out = ""
    for cell in range(6):
        cx = 22 + cell * 30
        for row in range(3):
            for col in range(2):
                if (cell * 7 + row * 3 + col * 5) % 4 == 0:
                    continue
                x, y = cx + col * 11, 196 + row * 14
                color = "#FFD500" if cell == 3 else "#1A4FD6"
                out += (f'<div style="position:absolute;left:{(x - 4) * mm}px;top:{(y - 4) * mm}px;width:{8 * mm}px;height:{8 * mm}px;'
                        f'border-radius:50%;background:{color}"></div>')
    out += f'<div style="position:absolute;left:{18 * mm}px;top:{248 * mm}px;width:{174 * mm}px;height:{3 * mm}px;background:#111111"></div>'
    return out


def workflow_motif(w, h, mm):
    """A branch graph: a main line of commits, with two branches that leave and merge back. Violet and gold."""
    svg = f'<svg style="position:absolute;left:0;top:0" width="{w}" height="{h}" viewBox="0 0 210 297">'
    svg += '<line x1="16" y1="250" x2="196" y2="250" stroke="#8B7BE0" stroke-width="2"/>'
    svg += '<path d="M40 250 C 52 222, 64 222, 76 222 L 104 222 C 116 222, 124 250, 132 250" fill="none" stroke="#F0B429" stroke-width="2"/>'
    svg += '<path d="M110 250 C 120 200, 130 196, 140 196 L 164 196 C 174 196, 180 250, 188 250" fill="none" stroke="#C9BDFF" stroke-width="2"/>'
    for x in (16, 40, 70, 110, 132, 160, 188):
        svg += f'<circle cx="{x}" cy="250" r="4.5" fill="#1A1726" stroke="#8B7BE0" stroke-width="2"/>'
    for x in (76, 92, 104):
        svg += f'<circle cx="{x}" cy="222" r="4" fill="#F0B429"/>'
    for x in (140, 152, 164):
        svg += f'<circle cx="{x}" cy="196" r="4" fill="#C9BDFF"/>'
    return svg + "</svg>"


# ------------------------------------------------------------------ courses

def typescript_motif(w, h, mm):
    """A blueprint: a fine grid in the lower half, with type annotations drawn on it. Navy and TypeScript blue."""
    font = (ROOT / "assets/fonts/spline-sans-mono/SplineSansMono[wght].ttf").as_uri()
    out = f"<style>@font-face{{font-family:SSM;src:url({font})}}</style>"
    for i in range(0, 25):
        x = i * 9 * mm
        out += f'<div style="position:absolute;left:{x}px;top:{165 * mm}px;width:1px;height:{140 * mm}px;background:#25395A"></div>'
    for j in range(0, 16):
        y = (165 + j * 9) * mm
        out += f'<div style="position:absolute;left:0;top:{y}px;width:{w}px;height:1px;background:#25395A"></div>'
    marks = [(": number", 14, 186, 30, "#5AA0F2", .95), ("<T>", 104, 206, 64, "#3178C6", .85),
             ("string | null", 18, 236, 22, "#A8B7CC", .7), ("?.", 140, 252, 44, "#5AA0F2", .45), ("readonly", 20, 266, 18, "#5AA0F2", .5)]
    out += "".join(f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;font:600 {s * mm}px/1 SSM, monospace;'
                   f'color:{c};opacity:{a};white-space:nowrap">{text}</div>' for text, x, y, s, c, a in marks)
    return out


def web_motif(w, h, mm):
    """Browser windows, stacked and offset, with a large tag sign. Aubergine, raspberry, and mint."""
    font = (ROOT / "assets/fonts/geist-mono/GeistMono[wght].ttf").as_uri()
    out = f"<style>@font-face{{font-family:GM;src:url({font})}}</style>"
    windows = [(14, 176, 118, 72, "#FF6B9A", .95), (44, 196, 118, 72, "#7DE2D1", .75), (74, 216, 118, 72, "#B9ADC4", .5)]
    for x, y, ww, hh, color, alpha in windows:
        box = (f'position:absolute;left:{x * mm}px;top:{y * mm}px;width:{ww * mm}px;height:{hh * mm}px;'
               f'border:{1.6 * mm}px solid {color};opacity:{alpha};background:#1C1426')
        dots = "".join(f'<div style="position:absolute;left:{(4 + i * 6) * mm}px;top:{3.2 * mm}px;width:{3 * mm}px;height:{3 * mm}px;'
                       f'border-radius:50%;background:{color}"></div>' for i in range(3))
        bars = "".join(f'<div style="position:absolute;left:{6 * mm}px;top:{(18 + i * 9) * mm}px;width:{(ww - 12 - i * 18) * mm}px;'
                       f'height:{2.4 * mm}px;background:{color};opacity:.55"></div>' for i in range(4))
        out += (f'<div style="{box}"><div style="position:absolute;left:0;right:0;top:0;height:{9.5 * mm}px;'
                f'border-bottom:{1.2 * mm}px solid {color}"></div>{dots}{bars}</div>')
    out += (f'<div style="position:absolute;left:{148 * mm}px;top:{262 * mm}px;font:700 {34 * mm}px/1 GM, monospace;'
            f'color:#FF6B9A;opacity:.35">&lt;/&gt;</div>')
    return out


def rust_motif(w, h, mm):
    """Riveted iron plates in the lower half, rust at their edges, with ownership marks stamped on them."""
    font = (ROOT / "assets/fonts/reddit-mono/RedditMono[wght].ttf").as_uri()
    out = f"<style>@font-face{{font-family:RM;src:url({font})}}</style>"
    plates = [(10, 172, 96, 58, "#3B2C25", "#E2622F"), (98, 196, 102, 64, "#33261F", "#F0743E"), (10, 240, 82, 54, "#2C211C", "#B8471C")]
    for x, y, pw, ph, fill, edge in plates:
        out += (f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;width:{pw * mm}px;height:{ph * mm}px;background:{fill};'
                f'border:{1.4 * mm}px solid {edge};box-shadow:0 0 0 {0.8 * mm}px #1B1512"></div>')
        for rx, ry in ((4, 4), (pw - 8, 4), (4, ph - 8), (pw - 8, ph - 8)):
            out += (f'<div style="position:absolute;left:{(x + rx) * mm}px;top:{(y + ry) * mm}px;width:{3.4 * mm}px;height:{3.4 * mm}px;'
                    f'border-radius:50%;background:#8C7B70"></div>')
    marks = [("&amp;mut", 22, 192, 26, "#F0743E", .95), ("Ok(())", 112, 219, 22, "#F7F0EB", .8),
             ("&#39;a", 36, 255, 30, "#F0743E", .7), ("move", 128, 272, 18, "#BBA99E", .6)]
    out += "".join(f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;font:700 {s * mm}px/1 RM, monospace;'
                   f'color:{c};opacity:{a};white-space:nowrap">{text}</div>' for text, x, y, s, c, a in marks)
    return out


def java_motif(w, h, mm):
    """Layered JVM bytecode/class frames and warm coffee accents in rich navy and crimson/amber."""
    font = (ROOT / "assets/fonts/cascadia-code/CascadiaCode[wght].ttf").as_uri()
    out = f"<style>@font-face{{font-family:CC;src:url({font})}}</style>"
    blocks = [
        (16, 178, 108, 48, "#1A2536", "#EA2D2E", 0.95),
        (56, 214, 114, 48, "#141E2E", "#0074BD", 0.85),
        (24, 252, 126, 46, "#0F1724", "#E76F51", 0.75),
    ]
    for x, y, bw, bh, fill, border, alpha in blocks:
        out += (f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;width:{bw * mm}px;height:{bh * mm}px;'
                f'background:{fill};border:{1.4 * mm}px solid {border};opacity:{alpha};'
                f'box-shadow:0 0 {12 * mm}px rgba(0,0,0,0.4)"></div>')
    marks = [
        ("public class", 26, 194, 18, "#FF6B6B", 0.9),
        ("record Order()", 68, 230, 18, "#56CCF2", 0.85),
        ("JVM::Bytecode", 34, 268, 16, "#FFD166", 0.75),
    ]
    out += "".join(f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;font:700 {s * mm}px/1 CC, monospace;'
                   f'color:{c};opacity:{a};white-space:nowrap">{text}</div>' for text, x, y, s, c, a in marks)
    return out


def spring_motif(w, h, mm):
    """Hexagonal microservice nodes, clean API badges, and Spring leaf green accents."""
    font = (ROOT / "assets/fonts/intel-one-mono/IntelOneMono[wght].ttf").as_uri()
    out = f"<style>@font-face{{font-family:IOM;src:url({font})}}</style>"
    nodes = [
        (18, 176, 112, 54, "#14281B", "#6DB33F", 0.95),
        (64, 212, 118, 52, "#0F2015", "#85EA2D", 0.85),
        (28, 254, 124, 48, "#0A170F", "#529922", 0.75),
    ]
    for x, y, nw, nh, fill, border, alpha in nodes:
        out += (f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;width:{nw * mm}px;height:{nh * mm}px;'
                f'background:{fill};border:{1.4 * mm}px solid {border};opacity:{alpha};'
                f'box-shadow:0 0 {12 * mm}px rgba(109,179,63,0.15)"></div>')
    marks = [
        ("@SpringBootApplication", 26, 194, 13, "#85EA2D", 0.9),
        ("GET /api/orders", 74, 230, 16, "#EBF7EE", 0.85),
        ("@RestController", 36, 270, 16, "#6DB33F", 0.75),
    ]
    out += "".join(f'<div style="position:absolute;left:{x * mm}px;top:{y * mm}px;font:700 {s * mm}px/1 IOM, monospace;'
                   f'color:{c};opacity:{a};white-space:nowrap">{text}</div>' for text, x, y, s, c, a in marks)
    return out


COURSES = {
    "flutter": {
        "folder": "02-flutter", "code": "dart", "name": "Flutter", "slug": "flutter-app-development",
        "logo_dark": "assets/logos/flutter/flutter-logo-dark-bg.svg", "logo_light": "assets/logos/flutter/flutter-logo-light-bg.svg",
        "icon": "assets/logos/flutter/flutter-icon.svg",
        "credit": "Flutter, Dart, and the related logos are trademarks of Google LLC. We are not endorsed by or affiliated with Google LLC.",
        "cover": {"style": "motif", "bg": "#15123A", "ink": "#FFFFFF", "second": "#4FC3F7", "accent": "#6C63FF",
                  "art": "assets/covers/patterns/flutter-cover-background.png", "motif": flutter_motif},
        # Its own look: deep indigo and sky blue, with nested frames (the widget tree) as the visual idea.
        "theme": theme(
            primary="#4B3FCF", surface="#F4F3FD", border="#DCD9F5", text="#1A1830", muted="#5D5A78",
            dark=("#15123A", "#221E52", "#332E6E", "#F5F4FF", "#B9B5E0", "#4FC3F7"),
            code={"background": "#1B1840", "border": "#2E2A63", "highlight-line": "#262257", "text": "#ECEBFF",
                  "comment": "#8E8AB8", "keyword": "#C3A6FF", "string": "#9EE6A0", "number": "#FFC86B",
                  "type": "#6FD6FF", "function": "#FF9EC7", "punctuation": "#CFCDF0", "output": "#B6E8FF"},
            note_tint="#F2F0FE", note_text="#33299E"),
        "fonts": ("Figtree", "Fira Code"),
        "font_faces": faces(("Figtree", "figtree"), ("Fira Code", "fira-code")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 150px; height: 10px; margin-top: 22px;
  background: linear-gradient(90deg, #6C63FF 0 50%, #4FC3F7 50% 100%); }
section.dark::before { content: ""; position: absolute; right: 70px; bottom: 70px; width: 150px; height: 150px;
  border: 6px solid #6C63FF; box-shadow: 24px 24px 0 -6px #15123A, 24px 24px 0 0 #4FC3F7; opacity: .7; }
section.recap { background: #F4F3FD; border-left: 14px solid #4B3FCF; }
pre.output { border-left-color: #4FC3F7; }
.footer span:first-child::before { content: ""; display: inline-block; width: 10px; height: 10px; border: 2px solid #4B3FCF; margin-right: 10px; }
""",
        "book_css": """
pre.output { border-left-color: #4FC3F7; }
@page { @top-left { border-bottom-color: #4B3FCF; } @top-right { border-bottom-color: #4B3FCF; } }
""",
        "text": texts("Flutter App Development", "ការអភិវឌ្ឍន៍ App",
                      ["Build real apps from one codebase", "Learn widgets, layout, and state, step by step", "Make the Mina Coffee app"],
                      ["បង្កើត app ពិតៗពីកូដតែមួយ", "រៀន widget, layout និង state ម្ដងមួយជំហាន", "បង្កើត app Mina Coffee"],
                      second="App Development"),
    },
    "ios": {
        "folder": "04-ios-development", "code": "swift", "name": "iOS", "slug": "ios-development-with-swiftui",
        # Title slides are light here, so they use the Swift logo for light backgrounds. Never the Apple logo,
        # the Xcode icon, or the SwiftUI icon.
        "logo_dark": "assets/logos/swift/swift-logo-light-bg.svg", "logo_light": "assets/logos/swift/swift-logo-light-bg.svg",
        "icon": "assets/logos/swift/swift-icon.svg",
        "credit": ("Apple, iPhone, iPad, Mac, macOS, iPadOS, watchOS, tvOS, visionOS, Apple Watch, Apple TV, Apple Vision Pro, App Store, Xcode, Swift, SwiftUI, and the Swift logo are trademarks of Apple Inc., registered in the "
                   "U.S. and other countries. IOS is a trademark or registered trademark of Cisco in the U.S. and other countries and is used under license. We are not endorsed by or affiliated with Apple Inc."),
        "cover": {"style": "motif", "bg": "#F6F1EA", "ink": "#2A1533", "second": "#5A2D6E", "accent": "#5A2D6E",
                  "art": "assets/covers/patterns/ios-cover-background.png", "motif": ios_motif, "size": "120pt"},
        # Its own look: warm sand and plum, with gold, and light title slides. See 04-ios-development/planning/slide-design.md.
        "theme": theme(
            primary="#6B3483", surface="#FAF6F0", border="#E7DCCB", text="#24152B", muted="#6A5B6E",
            dark=("#F6F1EA", "#EDE3D3", "#DCCDB6", "#2A1533", "#6A5B6E", "#6B3483"),
            code={"background": "#2A1B30", "border": "#3E2A47", "highlight-line": "#35233D", "text": "#F3ECF5",
                  "comment": "#9C8BA3", "keyword": "#F28DC1", "string": "#F2C46B", "number": "#B9E28C",
                  "type": "#9CC8FF", "function": "#E8B3FF", "punctuation": "#D9CFDD", "output": "#F2DDA6"},
            note_tint="#F8F1FB", note_text="#4A2159"),
        "fonts": ("Manrope", "DM Mono"),
        "font_faces": faces(("Manrope", "manrope"), ("DM Mono", "dm-mono")),
        "slide_css": """
section.dark { border-bottom: 18px solid #5A2D6E; }
section.dark h1 { color: #2A1533; }
section.dark h1::after { content: ""; display: block; width: 90px; height: 90px; margin: -100px 0 0 auto; background: #C99A2E; opacity: .9; }
section.dark h2 { color: #6B3483; }
section.dark .footer { color: #6A5B6E; }
section.recap { background: #FAF6F0; }
section.recap::after { content: ""; position: absolute; right: 60px; top: 56px; width: 44px; height: 44px; background: #C99A2E; }
pre.output { border-left-color: #C99A2E; }
.footer span:first-child::before { content: ""; display: inline-block; width: 10px; height: 14px; border: 2px solid #6B3483; margin-right: 10px; vertical-align: -2px; }
""",
        "book_css": """
pre.output { border-left-color: #C99A2E; }
@page { @top-left { border-bottom-color: #6B3483; } @top-right { border-bottom-color: #6B3483; } }
""",
        "text": texts("iOS Development with SwiftUI", "ជាមួយ SwiftUI",
                      ["Build iPhone apps with SwiftUI", "Learn views, state, and data, step by step", "Make the Mina Coffee members' app"],
                      ["បង្កើត app iPhone ជាមួយ SwiftUI", "រៀន view, state និងទិន្នន័យ ម្ដងមួយជំហាន", "បង្កើត app សមាជិក Mina Coffee"],
                      second="with SwiftUI"),
    },
    "kotlin": {
        "folder": "05-kotlin", "code": "kotlin", "name": "Kotlin", "slug": "kotlin-programming",
        # The full Kotlin logo is not allowed, and the Kotlin icon only next to other language icons, so the title slides
        # and cover use Kodee, the Kotlin mascot (CC BY 4.0). See assets/logos/README.md.
        "logo_dark": "assets/mascots/kodee/kodee-waving.svg", "logo_light": "assets/mascots/kodee/kodee-waving.svg",
        "icon": "assets/mascots/kodee/kodee-greeting.svg",
        "credit": ("Kotlin is a trademark of the Kotlin Foundation. IntelliJ IDEA is a trademark of JetBrains s.r.o. We are not "
                   "endorsed by or affiliated with the Kotlin Foundation or JetBrains. Kodee by JetBrains s.r.o. is licensed under CC BY 4.0."),
        # The same layout as the Dart and Swift covers, in Kotlin's colors: a pale pink page, magenta and orange, and
        # Preah Vihear temple at the bottom, toned magenta (cover_art()). Square corners, like the Kotlin style.
        "cover": {"page": ("#FFF8FB", "#FCEDF4", "#F8DDEA"), "text": "#2A0F22", "accent": "#B4237A",
                  "tint": ("#F7C6DC", "#2A0F22"), "glow": "rgba(110,20,70,.20)", "square": True,
                  "photo": "assets/photos/preah-vihear-mcfa.jpg", "photo_pos": "62% 40%",
                  "fade": "transparent 0%,rgba(0,0,0,.12) 18%,rgba(0,0,0,.45) 36%,rgba(0,0,0,.85) 52%,#000 62%",
                  "art": "assets/covers/art/05-kotlin-cover-art.png",
                  # From the Ministry of Culture and Fine Arts; written permission still to be obtained (see assets/photos/README.md).
                  # The licensed alternative: "assets/photos/preah-vihear-psamathem.jpg", with its CC BY-SA 4.0 credit from that README.
                  "photo_credit": ("Cover photo: Preah Vihear temple, courtesy of the Ministry of Culture and Fine Arts of Cambodia "
                                   "(mcfa.gov.kh). Cropped and toned magenta.")},
        # Its own look: near-black, magenta, and orange, with diagonal bands. See 05-kotlin/planning/slide-design.md.
        "theme": theme(
            primary="#A61E6E", surface="#FCF3F7", border="#F0D6E3", text="#1E1219", muted="#6B5462",
            dark=("#160B14", "#24121F", "#3A1D31", "#FFF5FA", "#D5B5C6", "#FF8A3D"),
            code={"background": "#1E1219", "border": "#3A1D31", "highlight-line": "#2A1824", "text": "#F7EDF2",
                  "comment": "#9A8290", "keyword": "#FF7AB6", "string": "#FFB36B", "number": "#9BE3C4",
                  "type": "#C9A2FF", "function": "#7FD3FF", "punctuation": "#E3D3DB", "output": "#FFD3B0"},
            note_tint="#FCF1F6", note_text="#7A1450"),
        "fonts": ("Plus Jakarta Sans", "Red Hat Mono"),
        "font_faces": faces(("Plus Jakarta Sans", "plus-jakarta-sans"), ("Red Hat Mono", "red-hat-mono")),
        "slide_css": """
section.dark { background: linear-gradient(135deg, #160B14 0 72%, #24121F 72% 100%); }
section.dark h1::after { content: ""; display: block; width: 160px; height: 10px; margin-top: 22px;
  background: linear-gradient(90deg, #B4237A, #FF8A3D); transform: skewX(-30deg); transform-origin: left; }
section.dark .logo { height: 96px; }
section.recap { background: #FCF3F7; border-top: 10px solid #FF8A3D; }
pre.output { border-left-color: #FF8A3D; }
.footer span:first-child::before { content: ""; display: inline-block; width: 14px; height: 8px; background: #B4237A; margin-right: 10px; transform: skewX(-30deg); }
""",
        "book_css": """
pre.output { border-left-color: #FF8A3D; }
@page { @top-left { border-bottom-color: #A61E6E; } @top-right { border-bottom-color: #A61E6E; } }
""",
        "text": texts("Kotlin Programming", "ការសរសេរកម្មវិធី",
                      ["Learn the Kotlin language, step by step", "Write real programs for a coffee shop", "Get ready for Android apps"],
                      ["រៀនភាសា Kotlin ម្ដងមួយជំហាន", "សរសេរកម្មវិធីពិតសម្រាប់ហាងកាហ្វេ", "ត្រៀមខ្លួនសម្រាប់ app Android"]),
    },
    "android": {
        "folder": "06-android-development", "code": "kotlin", "name": "Android", "slug": "android-development-with-compose",
        # Only the robot head: the Android wordmark and its typeface are not allowed. Title slides are light.
        "logo_dark": "assets/logos/android/android-robot-head.svg", "logo_light": "assets/logos/android/android-robot-head.svg",
        "icon": "assets/logos/android/android-robot-head.svg",
        "credit": ("The Android robot is reproduced or modified from work created and shared by Google and used according to terms "
                   "described in the Creative Commons 3.0 Attribution License. Android, Android Studio, Jetpack Compose, and Google Play "
                   "are trademarks of Google LLC. We are not endorsed by or affiliated with Google LLC."),
        "cover": {"style": "motif", "bg": "#EEF5EA", "ink": "#0F2E1C", "second": "#1E8A4C", "accent": "#1E8A4C",
                  "art": "assets/covers/patterns/android-cover-background.png", "motif": android_motif, "size": "112pt", "author_side": "right"},
        # Its own look: pale green and deep green, with round shapes, and light title slides.
        "theme": theme(
            primary="#1B7A44", surface="#F3F8F0", border="#D5E6CF", text="#13241A", muted="#4F6356",
            dark=("#EEF5EA", "#E1EEDA", "#C9DFC0", "#0F2E1C", "#4F6356", "#1B7A44"),
            code={"background": "#14241B", "border": "#24402F", "highlight-line": "#1C3125", "text": "#E9F5EC",
                  "comment": "#86A090", "keyword": "#7CE3A6", "string": "#F4D58D", "number": "#F2A877",
                  "type": "#8FD3FF", "function": "#C6F28B", "punctuation": "#CFE3D5", "output": "#BDF0D0"},
            note_tint="#EFF8EC", note_text="#145C33"),
        "fonts": ("Roboto", "Roboto Mono"),
        "font_faces": faces(("Roboto", "roboto"), ("Roboto Mono", "roboto-mono")),
        "slide_css": """
section.dark h1 { color: #0F2E1C; }
section.dark h1::after { content: ""; display: block; width: 26px; height: 26px; border-radius: 50%; background: #3DDC84;
  box-shadow: 40px 0 0 #1B7A44, 80px 0 0 #C9DFC0; margin-top: 22px; }
section.dark h2 { color: #1B7A44; }
section.dark::before { content: ""; position: absolute; right: -90px; bottom: -90px; width: 300px; height: 300px; border-radius: 50%;
  background: #3DDC84; opacity: .35; }
section.recap { background: #F3F8F0; border-top: 10px solid #3DDC84; }
pre.output { border-left-color: #3DDC84; }
.footer span:first-child::before { content: ""; display: inline-block; width: 10px; height: 10px; border-radius: 50%; background: #3DDC84; margin-right: 10px; }
""",
        "book_css": """
pre.output { border-left-color: #3DDC84; }
@page { @top-left { border-bottom-color: #1B7A44; } @top-right { border-bottom-color: #1B7A44; } }
""",
        "text": texts("Android Development with Jetpack Compose", "ជាមួយ Jetpack Compose",
                      ["Build Android apps with Jetpack Compose", "Learn screens, state, and data, step by step", "Make the Mina Coffee counter app"],
                      ["បង្កើត app Android ជាមួយ Jetpack Compose", "រៀន screen, state និងទិន្នន័យ ម្ដងមួយជំហាន", "បង្កើត app បញ្ជរ Mina Coffee"],
                      second="with Jetpack Compose"),
    },
    "javascript": {
        "folder": "07-java-script", "code": "javascript", "name": "JavaScript", "slug": "javascript-programming",
        # JavaScript has no official logo. This is the community logo from JSConf, under the MIT license.
        "logo_dark": "assets/logos/javascript/javascript-icon.svg", "logo_light": "assets/logos/javascript/javascript-icon.svg",
        "icon": "assets/logos/javascript/javascript-icon.svg",
        "credit": ("JavaScript is a trademark of Oracle Corporation in the United States. Node.js is a trademark of the OpenJS Foundation. "
                   "The JavaScript logo is the community logo released by JSConf under the MIT license. We are not endorsed by or affiliated with any of them."),
        # The same layout as the Dart, Swift, and Kotlin covers: a pale yellow page, and Sbek Thom, the Khmer shadow theatre (UNESCO), toned yellow.
        "cover": {"page": ("#FFFDF3", "#FFF7D2", "#FCEFAE"), "text": "#1C1800", "accent": "#9C7A00",
                  "tint": ("#F8E27C", "#1C1800"), "glow": "rgba(60,48,0,.22)", "square": True,
                  "photo": "assets/photos/sbek-thom-mcfa.jpg", "photo_pos": "50% 38%",
                  "fade": "transparent 0%,rgba(0,0,0,.12) 18%,rgba(0,0,0,.45) 36%,rgba(0,0,0,.85) 52%,#000 62%",
                  "art": "assets/covers/art/07-java-script-cover-art.png",
                  # From the Ministry of Culture and Fine Arts; written permission still to be obtained (see assets/photos/README.md).
                  "photo_credit": ("Cover photo: Sbek Thom, Khmer shadow theatre, courtesy of the Ministry of Culture and Fine Arts of Cambodia (mcfa.gov.kh). Cropped and toned yellow.")},
        # Its own look: black and signal yellow, with big punctuation. See 07-java-script/planning/slide-design.md.
        "theme": theme(
            primary="#8C6D00", surface="#FFFBE0", border="#EFE4A6", text="#141414", muted="#5A5748",
            dark=("#111111", "#1E1E1C", "#33322C", "#FAFAF5", "#BDBBA8", "#F7DF1E"),
            code={"background": "#151515", "border": "#2E2E2A", "highlight-line": "#202020", "text": "#F2F2EA",
                  "comment": "#8D8B7C", "keyword": "#F7DF1E", "string": "#9FE59A", "number": "#FFB86B",
                  "type": "#8FD0FF", "function": "#F0A6FF", "punctuation": "#D6D4C6", "output": "#F7EFA8"},
            note_tint="#FFFAD6", note_text="#5C4800"),
        "fonts": ("Space Grotesk", "Space Mono"),
        "font_faces": faces(("Space Grotesk", "space-grotesk"), ("Space Mono", "space-mono")),
        "slide_css": """
section.dark h1::after { content: ";"; display: block; font: 700 64px/1 'Space Mono', monospace; color: #F7DF1E; margin-top: 6px; }
section.dark::before { content: "{ }"; position: absolute; right: 60px; bottom: 40px; font: 700 150px/1 'Space Mono', monospace;
  color: #F7DF1E; opacity: .16; }
section.recap { background: #FFFBE0; border-left: 14px solid #111111; }
pre.output { border-left-color: #F7DF1E; }
.footer span:first-child::before { content: "{}"; font-family: 'Space Mono', monospace; font-weight: 700; color: #8C6D00; margin-right: 8px; }
section.dark .footer span:first-child::before { color: #F7DF1E; }
""",
        "book_css": """
pre.output { border-left-color: #F7DF1E; }
@page { @top-left { border-bottom-color: #111111; } @top-right { border-bottom-color: #111111; } }
""",
        "text": texts("JavaScript Programming", "ការសរសេរកម្មវិធី",
                      ["Learn JavaScript from the first line", "Build pages and programs for a coffee shop", "Get ready for React Native and Node.js"],
                      ["រៀន JavaScript ពីបន្ទាត់ទីមួយ", "បង្កើតទំព័រ និងកម្មវិធីសម្រាប់ហាងកាហ្វេ", "ត្រៀមខ្លួនសម្រាប់ React Native និង Node.js"]),
    },
    "react-native": {
        "folder": "10-react-native", "code": "tsx", "name": "React Native", "slug": "react-native-app-development",
        "logo_dark": "assets/logos/react-native/react-native-icon.svg", "logo_light": "assets/logos/react-native/react-native-icon.svg",
        "icon": "assets/logos/react-native/react-native-icon.svg",
        "credit": "React Native and the React logo are trademarks of Meta Platforms, Inc. We are not endorsed by or affiliated with Meta.",
        "cover": {"style": "motif", "bg": "#1B1E24", "ink": "#FFFFFF", "second": "#61DAFB", "accent": "#2B8AA8",
                  "art": "assets/covers/patterns/react-native-cover-background.png", "motif": react_native_motif, "size": "74pt", "author_side": "right"},
        # Its own look: dark slate and cyan, with lanes. See 10-react-native/planning/slide-design.md.
        "theme": theme(
            primary="#0E6E8C", surface="#EEF8FB", border="#CDE6EE", text="#15191F", muted="#525C66",
            dark=("#1B1E24", "#252A32", "#353C46", "#F2F6F8", "#AAB4BE", "#61DAFB"),
            code={"background": "#1B1E24", "border": "#353C46", "highlight-line": "#252A32", "text": "#ECF1F4",
                  "comment": "#8792A0", "keyword": "#C792EA", "string": "#C3E88D", "number": "#F78C6C",
                  "type": "#61DAFB", "function": "#82AAFF", "punctuation": "#BFC7D1", "output": "#B5EAF7"},
            note_tint="#EBF7FB", note_text="#0B5068"),
        "fonts": ("Outfit", "Chivo Mono"),
        "font_faces": faces(("Outfit", "outfit"), ("Chivo Mono", "chivo-mono")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 140px; height: 4px; background: #61DAFB; margin-top: 24px;
  box-shadow: 0 10px 0 #2B8AA8, 0 20px 0 #353C46; }
section.dark::before { content: ""; position: absolute; right: 0; bottom: 130px; width: 420px; height: 4px; background: #61DAFB; opacity: .4;
  box-shadow: -60px 34px 0 #2B8AA8, 0 68px 0 #353C46; }
section.recap { background: #EEF8FB; border-bottom: 10px solid #61DAFB; }
pre.output { border-left-color: #61DAFB; }
.footer span:first-child::before { content: ""; display: inline-block; width: 16px; height: 2px; background: #0E6E8C; margin-right: 10px; vertical-align: middle; }
""",
        "book_css": """
pre.output { border-left-color: #61DAFB; }
@page { @top-left { border-bottom-color: #0E6E8C; } @top-right { border-bottom-color: #0E6E8C; } }
""",
        "text": texts("React Native App Development", "ការអភិវឌ្ឍន៍ App",
                      ["Build Android and iOS apps with React", "Learn components, state, and data, step by step", "Make the Mina Coffee delivery app"],
                      ["បង្កើត app Android និង iOS ជាមួយ React", "រៀន component, state និងទិន្នន័យ ម្ដងមួយជំហាន", "បង្កើត app ដឹកជញ្ជូន Mina Coffee"],
                      second="App Development"),
    },
    "ci-cd": {
        "folder": "11-ci-cd", "code": "yaml", "name": "CI/CD", "slug": "ci-cd-for-mobile-apps",
        # No brand logo: a course mark made from a Material Symbols icon (Apache 2.0), see assets/build_course_icons.py.
        "logo_dark": "assets/icons/courses/ci-cd.svg", "logo_light": "assets/icons/courses/ci-cd.svg", "icon": "assets/icons/courses/ci-cd.svg",
        "credit": ("GitHub and GitHub Actions are trademarks of GitHub, Inc. Dart and Flutter are trademarks of Google LLC. "
                   "Course mark icon from Material Symbols by Google, Apache License 2.0. We are not endorsed by or affiliated with any of them."),
        "cover": {"style": "motif", "bg": "#18222C", "ink": "#FFFFFF", "second": "#9BE15D", "accent": "#3E5C76",
                  "art": "assets/covers/patterns/ci-cd-cover-background.png", "motif": cicd_motif, "size": "120pt", "author_side": "right"},
        # Its own look: slate and lime, with pipeline stages. See 11-ci-cd/planning/slide-design.md.
        "theme": theme(
            primary="#2F5573", surface="#F1F5F8", border="#D3DEE7", text="#16212B", muted="#536373",
            dark=("#18222C", "#22303D", "#33475A", "#F3F7FA", "#AFC0CF", "#9BE15D"),
            code={"background": "#18222C", "border": "#33475A", "highlight-line": "#22303D", "text": "#E9F0F5",
                  "comment": "#8396A8", "keyword": "#9BE15D", "string": "#F7C873", "number": "#F59E7A",
                  "type": "#7CC4F5", "function": "#C9A6F7", "punctuation": "#C3D0DB", "output": "#CFF3AE"},
            note_tint="#EEF4F8", note_text="#1F3D55"),
        "fonts": ("Archivo", "Ubuntu Mono"),
        "font_faces": faces(("Archivo", "archivo"), ("Ubuntu Mono", "ubuntu-mono")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 180px; height: 18px; margin-top: 22px;
  background: linear-gradient(90deg, #9BE15D 0 18px, transparent 18px 40px, #9BE15D 40px 58px, transparent 58px 80px, #9BE15D 80px 98px,
  transparent 98px 120px, #7C93A8 120px 138px, transparent 138px); }
section.dark .logo { height: 72px; }
section.recap { background: #F1F5F8; border-left: 14px solid #9BE15D; }
pre.output { border-left-color: #9BE15D; }
.footer span:first-child::before { content: ""; display: inline-block; width: 10px; height: 10px; background: #9BE15D; margin-right: 10px; }
""",
        "book_css": """
pre.output { border-left-color: #9BE15D; }
@page { @top-left { border-bottom-color: #2F5573; } @top-right { border-bottom-color: #2F5573; } }
""",
        "text": texts("CI/CD for Mobile Apps", "សម្រាប់ App ទូរស័ព្ទ",
                      ["Build, test, and ship on every change", "Pipelines for Android, iOS, Flutter, and React Native", "Release to the stores with confidence"],
                      ["Build, test និង ship រាល់ពេលកែប្រែ", "Pipeline សម្រាប់ Android, iOS, Flutter និង React Native", "Release ទៅ store ដោយទំនុកចិត្ត"],
                      second="for Mobile Apps"),
    },
    "automated-testing": {
        "folder": "12-automated-testing", "code": "dart", "name": "Automated Testing", "slug": "automated-testing-for-mobile-apps",
        "logo_dark": "assets/icons/courses/automated-testing.svg", "logo_light": "assets/icons/courses/automated-testing.svg",
        "icon": "assets/icons/courses/automated-testing.svg",
        "credit": ("Dart and Flutter are trademarks of Google LLC. Course mark icon from Material Symbols by Google, Apache License 2.0. "
                   "We are not endorsed by or affiliated with Google LLC."),
        "cover": {"style": "motif", "bg": "#F3F0FA", "ink": "#241640", "second": "#6B3FA0", "accent": "#6B3FA0",
                  "art": "assets/covers/patterns/automated-testing-cover-background.png", "motif": testing_motif, "size": "78pt", "author_side": "right"},
        # Its own look: pale lavender, purple, and green ticks, with light title slides.
        "theme": theme(
            primary="#5E3594", surface="#F7F4FC", border="#E1D8F0", text="#1E1430", muted="#5E5470",
            dark=("#F3F0FA", "#E9E3F5", "#D6CCEB", "#241640", "#5E5470", "#5E3594"),
            code={"background": "#211833", "border": "#3A2D55", "highlight-line": "#2B2042", "text": "#F1ECF9",
                  "comment": "#978CAB", "keyword": "#C9A7FF", "string": "#8FE3B0", "number": "#FFC58A",
                  "type": "#8ECDFF", "function": "#FF9FCB", "punctuation": "#D7CEE6", "output": "#C9F2D6"},
            note_tint="#F5F0FC", note_text="#45246F"),
        "fonts": ("Lexend", "Inconsolata"),
        "font_faces": faces(("Lexend", "lexend"), ("Inconsolata", "inconsolata")),
        "slide_css": """
section.dark h1 { color: #241640; }
section.dark h1::after { content: "+5: All tests passed!"; display: block; margin-top: 18px; font: 600 26px/1 'Inconsolata', monospace; color: #2FB36B; }
section.dark h2 { color: #5E3594; }
section.recap { background: #F7F4FC; border-top: 10px solid #2FB36B; }
pre.output { border-left-color: #2FB36B; }
.footer span:first-child::before { content: ""; display: inline-block; width: 6px; height: 11px; border: solid #2FB36B; border-width: 0 3px 3px 0;
  transform: rotate(45deg); margin: 0 12px 2px 2px; }
""",
        "book_css": """
pre.output { border-left-color: #2FB36B; }
@page { @top-left { border-bottom-color: #5E3594; } @top-right { border-bottom-color: #5E3594; } }
""",
        "text": texts("Automated Testing for Mobile Apps", "សម្រាប់ App ទូរស័ព្ទ",
                      ["Write tests that catch bugs before users do", "Unit, UI, and end-to-end tests on every platform", "Build a testing habit for your team"],
                      ["សរសេរ test ដែលចាប់ bug មុនអ្នកប្រើ", "Unit, UI និង end-to-end test លើគ្រប់ platform", "បង្កើតទម្លាប់ testing សម្រាប់ក្រុម"],
                      second="for Mobile Apps"),
    },
    "mobile-architecture": {
        "folder": "13-mobile-architecture", "code": "dart", "name": "Mobile App", "slug": "mobile-app-architecture",
        "logo_dark": "assets/icons/courses/mobile-architecture.svg", "logo_light": "assets/icons/courses/mobile-architecture.svg",
        "icon": "assets/icons/courses/mobile-architecture.svg",
        "credit": ("Dart and Flutter are trademarks of Google LLC. Course mark icon from Material Symbols by Google, Apache License 2.0. "
                   "We are not endorsed by or affiliated with Google LLC."),
        "cover": {"style": "motif", "bg": "#0D2A44", "ink": "#FFFFFF", "second": "#7FB8EA", "accent": "#3D8FD6",
                  "art": "assets/covers/patterns/mobile-architecture-cover-background.png", "motif": architecture_motif, "size": "72pt", "author_side": "right"},
        # Its own look: a blueprint, navy and azure, with a grid. See 13-mobile-architecture/planning/slide-design.md.
        "theme": theme(
            primary="#1F5F9E", surface="#F0F5FB", border="#D3E1F0", text="#0F1E2E", muted="#4D6075",
            dark=("#0D2A44", "#143657", "#22496E", "#F2F7FC", "#A9C3DD", "#7FB8EA"),
            code={"background": "#0F2236", "border": "#22496E", "highlight-line": "#163050", "text": "#E8F1FA",
                  "comment": "#7F98B3", "keyword": "#7FB8EA", "string": "#F2D28C", "number": "#F5A97F",
                  "type": "#9BE7D8", "function": "#D6B4FF", "punctuation": "#C2D4E6", "output": "#BFE0FF"},
            note_tint="#EEF5FC", note_text="#164675"),
        "fonts": ("Noto Sans", "Noto Sans Mono"),
        "font_faces": faces(("Noto Sans", "noto-sans"), ("Noto Sans Mono", "noto-sans-mono")),
        "slide_css": """
section.dark { background-color: #0D2A44; background-image: linear-gradient(#173B5E 1px, transparent 1px),
  linear-gradient(90deg, #173B5E 1px, transparent 1px); background-size: 40px 40px; }
section.dark h1::after { content: ""; display: block; width: 160px; height: 0; border-top: 3px dashed #7FB8EA; margin-top: 24px; }
section.recap { background: #F0F5FB; border: 3px solid #1F5F9E; }
pre.output { border-left-color: #3D8FD6; }
.footer span:first-child::before { content: ""; display: inline-block; width: 12px; height: 8px; border: 2px solid #1F5F9E; margin-right: 10px; }
""",
        "book_css": """
pre.output { border-left-color: #3D8FD6; }
@page { @top-left { border-bottom-color: #1F5F9E; } @top-right { border-bottom-color: #1F5F9E; } }
""",
        "text": texts("Mobile App Architecture", "ស្ថាបត្យកម្ម App ទូរស័ព្ទ",
                      ["Design apps that stay easy to change", "Layers, state, data, and modules, step by step", "Patterns for every platform"],
                      ["រចនា app ដែលងាយកែប្រែជានិច្ច", "Layer, state, ទិន្នន័យ និង module ម្ដងមួយជំហាន", "Pattern សម្រាប់គ្រប់ platform"],
                      second="Architecture"),
    },
    "mobile-security": {
        "folder": "14-mobile-security", "code": "dart", "name": "Mobile App", "slug": "mobile-app-security",
        "logo_dark": "assets/icons/courses/mobile-security.svg", "logo_light": "assets/icons/courses/mobile-security.svg",
        "icon": "assets/icons/courses/mobile-security.svg",
        "credit": ("OWASP is a trademark of the OWASP Foundation. Dart is a trademark of Google LLC. Course mark icon from Material Symbols "
                   "by Google, Apache License 2.0. We are not endorsed by or affiliated with either of them."),
        "cover": {"style": "motif", "bg": "#12090C", "ink": "#FFFFFF", "second": "#FF5A7A", "accent": "#B3123A",
                  "art": "assets/covers/patterns/mobile-security-cover-background.png", "motif": security_motif, "size": "96pt", "author_side": "left"},
        # Its own look: near-black and crimson, with a vault of nested squares. See 14-mobile-security/planning/slide-design.md.
        "theme": theme(
            primary="#A3123A", surface="#FCF2F4", border="#F0D2D9", text="#1D0E12", muted="#64505A",
            dark=("#12090C", "#1F1015", "#3A1A23", "#FBF2F4", "#C9AAB2", "#FF5A7A"),
            code={"background": "#170C10", "border": "#3A1A23", "highlight-line": "#22121A", "text": "#F6ECEF",
                  "comment": "#9A8189", "keyword": "#FF7A95", "string": "#F2CF84", "number": "#8FD8C4",
                  "type": "#A9C8FF", "function": "#E7B2FF", "punctuation": "#DCC9CF", "output": "#FFD0DA"},
            note_tint="#FCF0F3", note_text="#7A0E2B"),
        "fonts": ("Barlow", "Overpass Mono"),
        "font_faces": faces(("Barlow", "barlow"), ("Overpass Mono", "overpass-mono")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 40px; height: 40px; margin-top: 22px; border: 5px solid #D7264E;
  box-shadow: 0 0 0 9px #12090C, 0 0 0 14px #5A1424; }
section.recap { background: #FCF2F4; border-top: 10px solid #A3123A; }
pre.output { border-left-color: #D7264E; }
.footer span:first-child::before { content: ""; display: inline-block; width: 8px; height: 8px; border: 2px solid #A3123A; outline: 2px solid #F0D2D9;
  outline-offset: 2px; margin-right: 12px; }
""",
        "book_css": """
pre.output { border-left-color: #D7264E; }
@page { @top-left { border-bottom-color: #A3123A; } @top-right { border-bottom-color: #A3123A; } }
""",
        "text": texts("Mobile App Security", "សុវត្ថិភាព App ទូរស័ព្ទ",
                      ["Think like an attacker, build like a defender", "Secrets, sign-in, storage, and networks", "Protect users and their data"],
                      ["គិតដូចអ្នកវាយប្រហារ បង្កើតដូចអ្នកការពារ", "Secret, sign-in, storage និង network", "ការពារអ្នកប្រើ និងទិន្នន័យរបស់ពួកគេ"],
                      second="Security"),
    },
    "observability": {
        "folder": "15-observability-monitoring", "code": "dart", "name": "Observability", "slug": "observability-and-monitoring",
        "logo_dark": "assets/icons/courses/observability.svg", "logo_light": "assets/icons/courses/observability.svg",
        "icon": "assets/icons/courses/observability.svg",
        "credit": ("Dart is a trademark of Google LLC. OpenTelemetry is a trademark of The Linux Foundation. Course mark icon from Material "
                   "Symbols by Google, Apache License 2.0. We are not endorsed by or affiliated with either of them."),
        "cover": {"style": "motif", "bg": "#0E1512", "ink": "#FFFFFF", "second": "#A3D139", "accent": "#4F6B00",
                  "art": "assets/covers/patterns/observability-cover-background.png", "motif": observability_motif, "size": "68pt", "author_side": "right"},
        # Its own look: a dark dashboard, with chartreuse signals. See 15-observability-monitoring/planning/slide-design.md.
        "theme": theme(
            primary="#4F6B00", surface="#F5F8EC", border="#DDE7C4", text="#141A10", muted="#55604A",
            dark=("#0E1512", "#17201B", "#28352D", "#F1F6EC", "#AEBBA6", "#A3D139"),
            code={"background": "#111A15", "border": "#28352D", "highlight-line": "#18231C", "text": "#E9F2E6",
                  "comment": "#83947F", "keyword": "#A3D139", "string": "#F2C97E", "number": "#7FD6E8",
                  "type": "#C9B6FF", "function": "#FFAB91", "punctuation": "#C7D3C2", "output": "#DDF2B0"},
            note_tint="#F3F8E6", note_text="#3B5000"),
        "fonts": ("Work Sans", "Martian Mono"),
        "font_faces": faces(("Work Sans", "work-sans"), ("Martian Mono", "martian-mono")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 200px; height: 30px; margin-top: 18px;
  background: linear-gradient(135deg, transparent 46%, #A3D139 47% 53%, transparent 54%) 0 0/40px 30px repeat-x; }
section.recap { background: #F5F8EC; border-left: 14px solid #A3D139; }
pre.output { border-left-color: #A3D139; }
.footer span:first-child::before { content: ""; display: inline-block; width: 4px; height: 12px; background: #4F6B00;
  box-shadow: 6px 4px 0 #A3D139, 12px -2px 0 #4F6B00; margin-right: 22px; vertical-align: -1px; }
""",
        "book_css": """
pre.output { border-left-color: #A3D139; }
@page { @top-left { border-bottom-color: #4F6B00; } @top-right { border-bottom-color: #4F6B00; } }
""",
        "text": texts("Observability and Monitoring", "និង Monitoring",
                      ["See what your app does on real phones", "Logs, crashes, metrics, and traces", "Find problems before users report them"],
                      ["មើលឃើញអ្វីដែល app ធ្វើលើទូរស័ព្ទពិត", "Log, crash, metric និង trace", "រកបញ្ហាឃើញមុនអ្នកប្រើរាយការណ៍"],
                      second="and Monitoring"),
    },
    "performance": {
        "folder": "16-performance-profiling", "code": "dart", "name": "Mobile", "slug": "mobile-app-performance",
        "logo_dark": "assets/icons/courses/performance.svg", "logo_light": "assets/icons/courses/performance.svg",
        "icon": "assets/icons/courses/performance.svg",
        "credit": ("Dart and Flutter are trademarks of Google LLC. Course mark icon from Material Symbols by Google, Apache License 2.0. "
                   "We are not endorsed by or affiliated with Google LLC."),
        "cover": {"style": "motif", "bg": "#160C05", "ink": "#FFFFFF", "second": "#FFA94D", "accent": "#D9480F",
                  "art": "assets/covers/patterns/performance-cover-background.png", "motif": performance_motif, "size": "84pt", "author_side": "right"},
        # Its own look: dark brown and hot orange, with a flame graph. See 16-performance-profiling/planning/slide-design.md.
        "theme": theme(
            primary="#C2410C", surface="#FFF5EE", border="#F5DCC9", text="#1F130B", muted="#66554A",
            dark=("#160C05", "#24150B", "#3D2414", "#FFF6EF", "#D6BBA6", "#FFA94D"),
            code={"background": "#1A0F08", "border": "#3D2414", "highlight-line": "#251710", "text": "#FBEFE6",
                  "comment": "#A08A7A", "keyword": "#FF9A57", "string": "#E3E08A", "number": "#7FD8C9",
                  "type": "#9CC3FF", "function": "#F7B2D9", "punctuation": "#E3D2C5", "output": "#FFD8B5"},
            note_tint="#FFF3EA", note_text="#8A2E06"),
        "fonts": ("Sora", "Azeret Mono"),
        "font_faces": faces(("Sora", "sora"), ("Azeret Mono", "azeret-mono")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 180px; height: 10px; margin-top: 22px; background: #7A2E0A;
  box-shadow: 20px -12px 0 -2px #D9480F, 40px -24px 0 -4px #FFC078; }
section.recap { background: #FFF5EE; border-bottom: 10px solid #D9480F; }
pre.output { border-left-color: #D9480F; }
.footer span:first-child::before { content: ""; display: inline-block; width: 14px; height: 4px; background: #7A2E0A;
  box-shadow: 2px -5px 0 #D9480F; margin-right: 10px; vertical-align: 1px; }
""",
        "book_css": """
pre.output { border-left-color: #D9480F; }
@page { @top-left { border-bottom-color: #C2410C; } @top-right { border-bottom-color: #C2410C; } }
""",
        "text": texts("Mobile App Performance", "សមត្ថភាព App ទូរស័ព្ទ",
                      ["Make apps start fast and scroll smoothly", "Measure with profilers, not guesses", "Fast on every phone, not only yours"],
                      ["ធ្វើឱ្យ app ចាប់ផ្ដើមលឿន និង scroll រលូន", "វាស់ដោយ profiler មិនមែនដោយការទាយ", "លឿនលើគ្រប់ទូរស័ព្ទ មិនត្រឹមតែរបស់អ្នក"],
                      second="App Performance"),
    },
    "release-engineering": {
        "folder": "17-release-engineering", "code": "dart", "name": "Release", "slug": "release-engineering-for-mobile-apps",
        "logo_dark": "assets/icons/courses/release-engineering.svg", "logo_light": "assets/icons/courses/release-engineering.svg",
        "icon": "assets/icons/courses/release-engineering.svg",
        "credit": ("Google Play and Android are trademarks of Google LLC. App Store, TestFlight, and iOS are trademarks of Apple Inc. Course mark icon "
                   "from Material Symbols by Google, Apache License 2.0. We are not endorsed by or affiliated with either of them."),
        "cover": {"style": "motif", "bg": "#FBF7EE", "ink": "#1C2B4A", "second": "#C8102E", "accent": "#1C2B4A",
                  "art": "assets/covers/patterns/release-engineering-cover-background.png", "motif": release_motif, "size": "104pt", "author_side": "right"},
        # Its own look: cream paper, navy ink, and a red stamp, with light title slides. See 17-release-engineering/planning/slide-design.md.
        "theme": theme(
            primary="#1C3F73", surface="#FBF7EE", border="#E8DFCB", text="#16202F", muted="#5B6170",
            dark=("#FBF7EE", "#F1EADB", "#E0D4BC", "#1C2B4A", "#5B6170", "#C8102E"),
            code={"background": "#1C2B4A", "border": "#2E4168", "highlight-line": "#24365A", "text": "#F1F4FA",
                  "comment": "#93A0B8", "keyword": "#FFB3BF", "string": "#F2D79A", "number": "#9FE0C4",
                  "type": "#A9C8FF", "function": "#FFD0A0", "punctuation": "#CBD3E3", "output": "#F6E7C8"},
            note_tint="#F6F1E4", note_text="#1C2B4A"),
        "fonts": ("Libre Franklin", "Courier Prime"),
        "font_faces": faces(("Libre Franklin", "libre-franklin"), ("Courier Prime", "courier-prime")),
        "slide_css": """
section.dark h1 { color: #1C2B4A; }
section.dark h1::after { content: "RELEASED"; display: table; margin: 18px 0 0; padding: 4px 14px; border: 4px solid #C8102E; color: #C8102E;
  font: 700 22px/1.2 'Courier Prime', monospace; letter-spacing: 3px; transform: rotate(-4deg); }
section.dark h2 { color: #C8102E; }
section.recap { background: #FBF7EE; border-top: 6px double #1C2B4A; }
pre.output { border-left-color: #C8102E; }
.footer span:first-child::before { content: "v"; font-family: 'Courier Prime', monospace; font-weight: 700; color: #C8102E; margin-right: 8px; }
""",
        "book_css": """
pre.output { border-left-color: #C8102E; }
@page { @top-left { border-bottom-color: #1C3F73; } @top-right { border-bottom-color: #1C3F73; } }
""",
        "text": texts("Release Engineering for Mobile Apps", "សម្រាប់ App ទូរស័ព្ទ",
                      ["Ship updates to both stores safely", "Versions, rollouts, flags, and hotfixes", "Release with a plan, not with hope"],
                      ["បញ្ចេញ update ទៅ store ទាំងពីរដោយសុវត្ថិភាព", "Version, rollout, flag និង hotfix", "Release ដោយមានផែនការ មិនមែនដោយសង្ឃឹម"],
                      second="Engineering"),
    },
    "data-networking": {
        "folder": "18-data-networking", "code": "dart", "name": "Data and", "slug": "data-and-networking",
        "logo_dark": "assets/icons/courses/data-networking.svg", "logo_light": "assets/icons/courses/data-networking.svg",
        "icon": "assets/icons/courses/data-networking.svg",
        "credit": ("Dart is a trademark of Google LLC. Course mark icon from Material Symbols by Google, Apache License 2.0. "
                   "We are not endorsed by or affiliated with Google LLC."),
        "cover": {"style": "motif", "bg": "#101828", "ink": "#FFFFFF", "second": "#FF7A59", "accent": "#D2462A",
                  "art": "assets/covers/patterns/data-networking-cover-background.png", "motif": networking_motif, "size": "92pt", "author_side": "left"},
        # Its own look: navy and coral, with a network of nodes. See 18-data-networking/planning/slide-design.md.
        "theme": theme(
            primary="#C03A1F", surface="#FFF4F0", border="#F4D7CE", text="#141B2B", muted="#566078",
            dark=("#101828", "#1A2438", "#2B3854", "#F3F5FA", "#AAB4C8", "#FF7A59"),
            code={"background": "#111A2C", "border": "#2B3854", "highlight-line": "#18233A", "text": "#EAF0FA",
                  "comment": "#8592AD", "keyword": "#FF9478", "string": "#A9E5A0", "number": "#F9D27A",
                  "type": "#86C8FF", "function": "#D3B4FF", "punctuation": "#C6CFDF", "output": "#FFD1C4"},
            note_tint="#FFF2EE", note_text="#8C2A15"),
        "fonts": ("Nunito Sans", "Anonymous Pro"),
        "font_faces": faces(("Nunito Sans", "nunito-sans"), ("Anonymous Pro", "anonymous-pro")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 180px; height: 14px; margin-top: 22px;
  background: radial-gradient(circle, #FF7A59 0 6px, transparent 7px) 0 50%/60px 14px repeat-x,
  linear-gradient(#FF7A59, #FF7A59) 0 50%/100% 2px no-repeat; }
section.recap { background: #FFF4F0; border-left: 14px solid #FF7A59; }
pre.output { border-left-color: #FF7A59; }
.footer span:first-child::before { content: ""; display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #FF7A59;
  box-shadow: 12px 0 0 #C03A1F; margin-right: 20px; }
""",
        "book_css": """
pre.output { border-left-color: #FF7A59; }
@page { @top-left { border-bottom-color: #C03A1F; } @top-right { border-bottom-color: #C03A1F; } }
""",
        "text": texts("Data and Networking for Mobile Apps", "និង Networking",
                      ["Load, save, and sync data reliably", "HTTP, JSON, caching, and local databases", "Apps that keep working offline"],
                      ["ទាញ រក្សាទុក និង sync ទិន្នន័យដោយទុកចិត្តបាន", "HTTP, JSON, caching និង database ក្នុងឧបករណ៍", "App ដែលនៅតែដំណើរការពេល offline"],
                      second="Networking"),
    },
    "accessibility-localization": {
        "folder": "19-accessibility-localization", "code": "dart", "name": "Accessibility", "slug": "accessibility-and-localization",
        "logo_dark": "assets/icons/courses/accessibility-localization.svg", "logo_light": "assets/icons/courses/accessibility-localization.svg",
        "icon": "assets/icons/courses/accessibility-localization.svg",
        "credit": ("Dart is a trademark of Google LLC. Course mark icon from Material Symbols by Google, Apache License 2.0. Atkinson Hyperlegible "
                   "fonts by the Braille Institute of America, SIL Open Font License. We are not endorsed by or affiliated with either of them."),
        "cover": {"style": "motif", "bg": "#FFFFFF", "ink": "#111111", "second": "#1A4FD6", "accent": "#1A4FD6",
                  "art": "assets/covers/patterns/accessibility-localization-cover-background.png", "motif": accessibility_motif, "size": "74pt", "author_side": "right"},
        # Its own look: the highest contrast of all the courses, white, black, blue, and yellow, with light title slides.
        "theme": theme(
            primary="#1A4FD6", surface="#F4F7FF", border="#C9D6F5", text="#111111", muted="#3D4350",
            dark=("#FFFFFF", "#F1F4FB", "#C9D6F5", "#111111", "#3D4350", "#1A4FD6"),
            code={"background": "#111111", "border": "#333333", "highlight-line": "#1E1E1E", "text": "#FFFFFF",
                  "comment": "#B8B8B8", "keyword": "#FFD500", "string": "#9FE3A6", "number": "#8EC5FF",
                  "type": "#FFB38A", "function": "#E6B8FF", "punctuation": "#E0E0E0", "output": "#FFF1A8"},
            note_tint="#EEF3FF", note_text="#0E3299"),
        "fonts": ("Atkinson Hyperlegible Next", "Atkinson Hyperlegible Mono"),
        "font_faces": faces(("Atkinson Hyperlegible Next", "atkinson-hyperlegible-next"), ("Atkinson Hyperlegible Mono", "atkinson-hyperlegible-mono")),
        "slide_css": """
section.dark { border-left: 24px solid #FFD500; }
section.dark h1 { color: #111111; }
section.dark h1::after { content: ""; display: block; width: 140px; height: 12px; background: #1A4FD6; margin-top: 22px; }
section.dark h2 { color: #1A4FD6; }
section.recap { background: #F4F7FF; border-top: 12px solid #FFD500; }
pre.output { border-left-color: #FFD500; }
.footer span:first-child::before { content: ""; display: inline-block; width: 12px; height: 12px; border-radius: 50%; background: #1A4FD6;
  box-shadow: 16px 0 0 #FFD500; margin-right: 26px; vertical-align: -1px; }
""",
        "book_css": """
pre.output { border-left-color: #FFD500; }
@page { @top-left { border-bottom-color: #1A4FD6; } @top-right { border-bottom-color: #1A4FD6; } }
""",
        "text": texts("Accessibility and Localization", "និង Localization",
                      ["Apps that everyone can use", "Contrast, large text, screen readers, and touch", "Khmer, English, and every language"],
                      ["App ដែលគ្រប់គ្នាអាចប្រើបាន", "Contrast, អក្សរធំ, screen reader និង touch", "ខ្មែរ អង់គ្លេស និងគ្រប់ភាសា"],
                      second="and Localization"),
    },
    "developer-workflow": {
        "folder": "20-developer-workflow", "code": "dart", "name": "Developer", "slug": "developer-workflow",
        "logo_dark": "assets/icons/courses/developer-workflow.svg", "logo_light": "assets/icons/courses/developer-workflow.svg",
        "icon": "assets/icons/courses/developer-workflow.svg",
        "credit": ("Git is a trademark of Software Freedom Conservancy. GitHub is a trademark of GitHub, Inc. Course mark icon from Material "
                   "Symbols by Google, Apache License 2.0. We are not endorsed by or affiliated with any of them."),
        "cover": {"style": "motif", "bg": "#1A1726", "ink": "#FFFFFF", "second": "#F0B429", "accent": "#5B3FC4", "badge_ink": "#FFFFFF",
                  "art": "assets/covers/patterns/developer-workflow-cover-background.png", "motif": workflow_motif, "size": "96pt", "author_side": "left"},
        # Its own look: deep violet and gold, with a branch graph. See 20-developer-workflow/planning/slide-design.md.
        "theme": theme(
            primary="#5B3FC4", surface="#F6F3FF", border="#DDD5F7", text="#1A1726", muted="#5C5670",
            dark=("#1A1726", "#25213A", "#3A3456", "#F6F4FF", "#B9B2D6", "#F0B429"),
            code={"background": "#1A1726", "border": "#3A3456", "highlight-line": "#231F33", "text": "#EFEBFF",
                  "comment": "#9089AE", "keyword": "#C9BDFF", "string": "#F0C76A", "number": "#8FE0C8",
                  "type": "#8FC4FF", "function": "#FFA8C8", "punctuation": "#D3CCEA", "output": "#E9E0FF"},
            note_tint="#F4F0FF", note_text="#3E2A91"),
        "fonts": ("Karla", "Fragment Mono"),
        "font_faces": faces(("Karla", "karla"), ("Fragment Mono", "fragment-mono")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 180px; height: 26px; margin-top: 18px;
  background: radial-gradient(circle, #F0B429 0 6px, transparent 7px) 0 0/45px 26px repeat-x,
  linear-gradient(#8B7BE0, #8B7BE0) 0 50%/100% 3px no-repeat; }
section.recap { background: #F6F3FF; border-left: 14px solid #F0B429; }
pre.output { border-left-color: #F0B429; }
.footer span:first-child::before { content: ""; display: inline-block; width: 8px; height: 8px; border-radius: 50%; border: 2px solid #5B3FC4;
  margin-right: 10px; }
""",
        "book_css": """
pre.output { border-left-color: #F0B429; }
@page { @top-left { border-bottom-color: #5B3FC4; } @top-right { border-bottom-color: #5B3FC4; } }
""",
        "text": texts("Developer Workflow for Mobile Teams", "សម្រាប់ក្រុម Mobile",
                      ["Git, branches, and pull requests", "Code review, tools, and documentation", "Work well with a team"],
                      ["Git, branch និង pull request", "Code review, ឧបករណ៍ និងឯកសារ", "ធ្វើការល្អជាមួយក្រុម"],
                      second="Workflow"),
    },
    "typescript": {
        "folder": "08-typescript", "code": "typescript", "name": "TypeScript", "slug": "typescript-programming",
        # The official TypeScript mark from typescriptlang.org/branding, unchanged. See assets/logos/README.md.
        "logo_dark": "assets/logos/typescript/typescript-icon.svg", "logo_light": "assets/logos/typescript/typescript-icon.svg",
        "icon": "assets/logos/typescript/typescript-icon.svg",
        "credit": ("TypeScript and the TypeScript logo are trademarks of Microsoft Corporation. Node.js is a trademark of the "
                   "OpenJS Foundation. We are not endorsed by or affiliated with Microsoft or the OpenJS Foundation."),
        # The same layout as the Dart, Swift, and Kotlin covers: a pale blue page, and Koh Ker temple (UNESCO), toned TypeScript blue.
        "cover": {"page": ("#F6FAFF", "#E7F0FB", "#D5E4F7"), "text": "#0D1B2E", "accent": "#3178C6",
                  "tint": ("#B7D2F2", "#0D1B2E"), "glow": "rgba(13,27,46,.22)", "square": True,
                  "photo": "assets/photos/koh-ker-mcfa.jpg", "photo_pos": "50% 0%",
                  # A short fade and the top of the photo, so the top of the pyramid stays visible (the bottom is cropped).
                  "fade": "transparent 0%,rgba(0,0,0,.5) 4%,rgba(0,0,0,.9) 10%,#000 14%",
                  "art": "assets/covers/art/08-typescript-cover-art.png",
                  # From the Ministry of Culture and Fine Arts; written permission still to be obtained (see assets/photos/README.md).
                  "photo_credit": ("Cover photo: Prasat Thom at Koh Ker, courtesy of the Ministry of Culture and Fine Arts of Cambodia (mcfa.gov.kh). Cropped and toned blue.")},
        # Its own look: a navy blueprint with TypeScript blue, and type annotations. See 08-typescript/planning/slide-design.md.
        "theme": theme(
            primary="#235A97", surface="#EEF4FB", border="#CFDDF0", text="#111A26", muted="#4F5D70",
            dark=("#0D1B2E", "#16273F", "#25395A", "#F2F6FB", "#A8B7CC", "#5AA0F2"),
            code={"background": "#0F1D30", "border": "#25395A", "highlight-line": "#16273F", "text": "#E8EFF8",
                  "comment": "#7F92AB", "keyword": "#7FB8FF", "string": "#F5C77E", "number": "#F59AA3",
                  "type": "#6EE0C4", "function": "#D7B6FF", "punctuation": "#BAC8DA", "output": "#BFD9FF"},
            note_tint="#EDF4FC", note_text="#173E69"),
        "fonts": ("Instrument Sans", "Spline Sans Mono"),
        "font_faces": faces(("Instrument Sans", "instrument-sans"), ("Spline Sans Mono", "spline-sans-mono")),
        "slide_css": """
section.dark h1::after { content: ": Type"; display: block; font: 600 40px/1 'Spline Sans Mono', monospace; color: #5AA0F2; margin-top: 18px; }
section.dark::before { content: "<T>"; position: absolute; right: 60px; bottom: 40px; font: 600 140px/1 'Spline Sans Mono', monospace;
  color: #3178C6; opacity: .22; }
section.recap { background: #EEF4FB; border-left: 14px solid #3178C6; }
pre.output { border-left-color: #3178C6; }
.footer span:first-child::before { content: ":"; font-family: 'Spline Sans Mono', monospace; font-weight: 700; color: #235A97; margin-right: 8px; }
section.dark .footer span:first-child::before { color: #5AA0F2; }
""",
        "book_css": """
pre.output { border-left-color: #3178C6; }
@page { @top-left { border-bottom-color: #235A97; } @top-right { border-bottom-color: #235A97; } }
""",
        "text": texts("TypeScript Programming", "ការសរសេរកម្មវិធី",
                      ["Add types to the JavaScript you know", "Catch mistakes before the code runs", "Use one set of types for the web, apps, and servers"],
                      ["បន្ថែម type ទៅ JavaScript ដែលអ្នកស្គាល់", "រកកំហុសមុនពេលកូដ run", "ប្រើ type តែមួយសម្រាប់ web, app និង server"]),
    },
    "web": {
        "folder": "09-web-development", "code": "html", "name": "Web", "slug": "web-development",
        # HTML5, CSS, JavaScript, TypeScript, React, Git, and Firebase logos (assets/logos/build_logo_sets.py); licenses in assets/logos/README.md.
        "logo_dark": "assets/logos/web/web-logos-dark-bg.svg", "logo_light": "assets/logos/web/web-logos-light-bg.svg",
        "icon": "assets/logos/honeycomb/web.svg",  # the cover honeycomb (LOGO_SETS below)
        "credit": ("HTML5 logo by W3C, licensed under CC BY 3.0. CSS logo by the CSS-Next Community Group, CC0. "
                   "The JavaScript logo is the community logo released by JSConf under the MIT license. "
                   "TypeScript and the TypeScript logo are trademarks of Microsoft Corporation. React and the React logo are "
                   "trademarks of Meta Platforms, Inc. Firebase and the Firebase logo are trademarks of Google LLC. "
                   "Git Logo by Jason Long is licensed under the Creative Commons Attribution 3.0 Unported License. "
                   "We are not endorsed by or affiliated with any of them."),
        # The same layout as the Dart, Swift, and Kotlin covers: a pale pink page, and Sambor Prei Kuk temple (UNESCO), toned raspberry.
        "cover": {"page": ("#FFF7FA", "#FCEAF1", "#F8D8E4"), "text": "#1C1426", "accent": "#B0204F",
                  "tint": ("#F7C0D3", "#1C1426"), "glow": "rgba(60,15,35,.22)", "square": True,
                  "photo": "assets/photos/sambor-prei-kuk-mcfa.jpg", "photo_pos": "50% 50%", "icon_width": 72,
                  "fade": "transparent 0%,rgba(0,0,0,.12) 18%,rgba(0,0,0,.45) 36%,rgba(0,0,0,.85) 52%,#000 62%",
                  "art": "assets/covers/art/09-web-development-cover-art.png",
                  # From the Ministry of Culture and Fine Arts; written permission still to be obtained (see assets/photos/README.md).
                  "photo_credit": ("Cover photo: a temple at Sambor Prei Kuk, courtesy of the Ministry of Culture and Fine Arts of Cambodia (mcfa.gov.kh). Cropped and toned raspberry.")},
        # Its own look: aubergine, raspberry, and mint, with browser windows. See 09-web-development/planning/slide-design.md.
        "theme": theme(
            primary="#B0204F", surface="#FBF0F4", border="#EED3DD", text="#1C1426", muted="#5E5366",
            dark=("#1C1426", "#271D33", "#3A2D49", "#F8F3FA", "#B9ADC4", "#FF6B9A"),
            code={"background": "#1C1426", "border": "#3A2D49", "highlight-line": "#271D33", "text": "#F3EEF6",
                  "comment": "#9A8DA8", "keyword": "#FF7FA8", "string": "#9BE8D8", "number": "#FFC27A",
                  "type": "#B8A4FF", "function": "#FFE08A", "punctuation": "#CFC5D9", "output": "#B9F2E6"},
            note_tint="#FCEFF4", note_text="#7A1236"),
        "fonts": ("Geist", "Geist Mono"),
        "font_faces": faces(("Geist", "geist"), ("Geist Mono", "geist-mono")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 190px; height: 26px; margin-top: 22px; border: 3px solid #FF6B9A;
  background: radial-gradient(circle at 14px 12px, #FF6B9A 4px, transparent 5px), radial-gradient(circle at 30px 12px, #7DE2D1 4px, transparent 5px); }
section.dark::before { content: "</>"; position: absolute; right: 60px; bottom: 40px; font: 700 130px/1 'Geist Mono', monospace;
  color: #FF6B9A; opacity: .2; }
section.recap { background: #FBF0F4; border-top: 10px solid #FF6B9A; }
pre.output { border-left-color: #7DE2D1; }
pre.shell { border-left: 6px solid #FF6B9A; }
.footer span:first-child::before { content: "</>"; font-family: 'Geist Mono', monospace; font-weight: 700; color: #B0204F; margin-right: 8px; }
section.dark .footer span:first-child::before { color: #FF6B9A; }
""",
        "book_css": """
pre.output { border-left-color: #7DE2D1; }
pre.shell { border-left: 1.2mm solid #FF6B9A; }
@page { @top-left { border-bottom-color: #B0204F; } @top-right { border-bottom-color: #B0204F; } }
""",
        "text": texts("Web Development", "Development",
                      ["Learn how the internet and the web work", "Build fast, accessible websites with HTML and CSS", "Connect the web to your mobile apps"],
                      ["រៀនពីរបៀបដែល internet និង web ដំណើរការ", "បង្កើតគេហទំព័រលឿន និងងាយប្រើ ជាមួយ HTML និង CSS", "ភ្ជាប់ web ទៅ app ទូរស័ព្ទរបស់អ្នក"],
                      second="Development"),
    },
    "rust": {
        "folder": "22-rust", "code": "rust", "name": "Rust", "slug": "rust-programming",
        # The official Rust logo from rust-lang/rust-artwork, unchanged (CC BY 4.0, a Rust Foundation trademark).
        # See assets/logos/README.md.
        "logo_dark": "assets/logos/rust/rust-icon-dark-bg.svg", "logo_light": "assets/logos/rust/rust-icon.svg",
        "icon": "assets/logos/rust/rust-icon.svg",
        "credit": ("Rust and Cargo, and the Rust logo, are trademarks of the Rust Foundation. The Rust logo is from "
                   "rust-lang/rust-artwork, CC BY 4.0. We are not endorsed by or affiliated with the Rust Foundation or the Rust project."),
        "cover": {"style": "motif", "bg": "#1B1512", "ink": "#FFFFFF", "second": "#F0743E", "accent": "#E2622F", "badge_ink": "#1B1512",
                  "art": "assets/covers/patterns/rust-cover-background.png", "motif": rust_motif, "size": "120pt", "author_side": "right"},
        # Its own look: the forge. Dark iron, rust orange, and riveted plates. See 22-rust/planning/slide-design.md.
        "theme": theme(
            primary="#A9380F", surface="#FBF2EC", border="#F0D8C9", text="#1E1714", muted="#61534B",
            dark=("#1B1512", "#261D19", "#3B2C25", "#F7F0EB", "#BBA99E", "#F0743E"),
            code={"background": "#1D1714", "border": "#3B2C25", "highlight-line": "#2A211C", "text": "#F2EAE4",
                  "comment": "#9A8A80", "keyword": "#FF9A6B", "string": "#B5E08A", "number": "#FFD27A",
                  "type": "#7FD4E6", "function": "#F6C177", "punctuation": "#D3C5BC", "output": "#FFD9C2"},
            note_tint="#FCF1EA", note_text="#7A2A0C"),
        "fonts": ("Bricolage Grotesque", "Reddit Mono"),
        "font_faces": faces(("Bricolage Grotesque", "bricolage-grotesque"), ("Reddit Mono", "reddit-mono")),
        "slide_css": """
section.dark h1::after { content: "Ok(())"; display: block; font: 700 40px/1 'Reddit Mono', monospace; color: #F0743E; margin-top: 18px; }
section.dark::before { content: "&"; position: absolute; right: 70px; bottom: 30px; font: 700 170px/1 'Reddit Mono', monospace;
  color: #E2622F; opacity: .22; }
section.recap { background: #FBF2EC; border-left: 14px solid #E2622F; }
pre.output { border-left-color: #E2622F; }
.footer span:first-child::before { content: "&"; font-family: 'Reddit Mono', monospace; font-weight: 700; color: #A9380F; margin-right: 8px; }
section.dark .footer span:first-child::before { color: #F0743E; }
""",
        "book_css": """
pre.output { border-left-color: #E2622F; }
@page { @top-left { border-bottom-color: #A9380F; } @top-right { border-bottom-color: #A9380F; } }
""",
        "text": texts("Rust Programming", "ការសរសេរកម្មវិធី",
                      ["Write fast code that is safe with memory", "Learn ownership and borrowing, step by step", "Share one Rust core with Android, iOS, and the web"],
                      ["សរសេរកូដលឿន និងមានសុវត្ថិភាពជាមួយ memory", "រៀន ownership និង borrowing ម្ដងមួយជំហាន", "ចែករំលែក Rust core តែមួយ ជាមួយ Android, iOS និង web"]),
    },
    "security-fundamentals": {
        "folder": "01-security-fundamentals", "code": "text", "name": "Security Fundamentals", "slug": "security-fundamentals",
        "logo_dark": "assets/icons/courses/security-fundamentals.svg", "logo_light": "assets/icons/courses/security-fundamentals.svg",
        "icon": "assets/icons/courses/security-fundamentals.svg",
        "credit": ("Course mark icon from Material Symbols by Google, Apache License 2.0. NIST, CIS, ISO, OWASP, and MITRE ATT&CK "
                   "are the trademarks of their respective owners, used here only to refer to their published work."),
        "cover": {"style": "motif", "bg": "#0A1E42", "ink": "#FFFFFF", "second": "#6FA8DC", "accent": "#F2A541",
                  "art": "assets/covers/patterns/security-fundamentals-cover-background.png",
                  "motif": blueprint_motif, "size": "72pt", "author_side": "left"},
        # Its own look: deep navy and amber "blueprint". See 01-security-fundamentals/planning/slide-design.md.
        "theme": theme(
            primary="#0E2A5A", surface="#F6F8FB", border="#D7E0EC", text="#14213D", muted="#51607A",
            dark=("#0A1E42", "#122A52", "#28406B", "#F2F5FA", "#A8BAD4", "#F2A541"),
            code={"background": "#0F1E38", "border": "#26406B", "highlight-line": "#17294A", "text": "#EAF1FB",
                  "comment": "#8193AE", "keyword": "#7FB2F0", "string": "#F2C98A", "number": "#9FE0C8",
                  "type": "#A9C8FF", "function": "#F2A541", "punctuation": "#CBD7E6", "output": "#BFE3C9"},
            note_tint="#EEF3FB", note_text="#0E2A5A"),
        "fonts": ("Inter", "JetBrains Mono"),
        "font_faces": faces(("Inter", "inter"), ("JetBrains Mono", "jetbrains-mono")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 52px; height: 52px; margin-top: 22px; border: 4px solid #F2A541; }
section.recap { background: #FBF4E6; border-top: 10px solid #F2A541; }
pre.output { border-left-color: #F2A541; }
.footer span:first-child::before { content: ""; display: inline-block; width: 8px; height: 8px; border: 2px solid #0E2A5A;
  outline: 2px solid #D7E0EC; outline-offset: 2px; margin-right: 12px; }
section.dark .footer span:first-child::before { border-color: #F2A541; outline-color: #28406B; }
""",
        "book_css": """
pre.output { border-left-color: #F2A541; }
@page { @top-left { border-bottom-color: #0E2A5A; } @top-right { border-bottom-color: #0E2A5A; } }
""",
        "text": texts("Security Fundamentals", "មូលដ្ឋានគ្រឹះសន្តិសុខ",
                      ["Understand what cybersecurity is, from the ground up", "Learn how attacks work, and how to defend",
                       "Build the base for every later security course"],
                      ["យល់ដឹងពី cybersecurity ចាប់ពីមូលដ្ឋាន", "រៀនពីរបៀបនៃការវាយប្រហារ និងការការពារ",
                       "បង្កើតមូលដ្ឋានសម្រាប់គ្រប់ course សន្តិសុខបន្ទាប់"],
                      badge_en="A Practical Guide", second=""),
    },
    "computer-fundamentals": {
        "folder": "02-computer-fundamentals", "code": "c", "name": "How Computers Work", "slug": "how-computers-work",
        "logo_dark": "assets/icons/courses/computer-fundamentals.svg", "logo_light": "assets/icons/courses/computer-fundamentals.svg",
        "icon": "assets/icons/courses/computer-fundamentals.svg",
        "credit": "Course mark icon from Material Symbols by Google, Apache License 2.0.",
        "cover": {"style": "motif", "bg": "#0C1716", "ink": "#FFFFFF", "second": "#5EEAD4", "accent": "#2DD4BF",
                  "art": "assets/covers/patterns/computer-fundamentals-cover-background.png",
                  "motif": circuit_motif, "size": "64pt", "author_side": "left"},
        # Its own look: charcoal and teal "circuit". See 02-computer-fundamentals/planning/slide-design.md.
        "theme": theme(
            primary="#0C7A6E", surface="#F4F8F7", border="#D4E4E1", text="#122420", muted="#4E635E",
            dark=("#0C1716", "#13211F", "#224A44", "#EFF6F4", "#A6C3BD", "#2DD4BF"),
            code={"background": "#0D1A18", "border": "#224A44", "highlight-line": "#14251F", "text": "#E8F3F0",
                  "comment": "#6F8C86", "keyword": "#5EEAD4", "string": "#F2C98A", "number": "#9FE0C8",
                  "type": "#8BD5FF", "function": "#F6A96B", "punctuation": "#C7D8D4", "output": "#BFE8DC"},
            note_tint="#EBF5F3", note_text="#0C5248"),
        "fonts": ("Space Grotesk", "Space Mono"),
        "font_faces": faces(("Space Grotesk", "space-grotesk"), ("Space Mono", "space-mono")),
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 90px; height: 6px; background: #2DD4BF; margin-top: 22px; }
section.recap { background: #E8F6F3; border-top: 10px solid #2DD4BF; }
pre.output { border-left-color: #2DD4BF; }
.footer span:first-child::before { content: "01"; font-family: 'Space Mono', monospace; font-weight: 700; color: #0C7A6E; margin-right: 10px; }
section.dark .footer span:first-child::before { color: #2DD4BF; }
""",
        "book_css": """
pre.output { border-left-color: #2DD4BF; }
@page { @top-left { border-bottom-color: #0C7A6E; } @top-right { border-bottom-color: #0C7A6E; } }
""",
        "text": texts("How Computers Work", "របៀបដែលកុំព្យូទ័រដំណើរការ",
                      ["See inside the machine, from bits to the boot", "Understand memory, files, programs, and the OS",
                       "Build the base for reversing, forensics, and exploitation"],
                      ["មើលខាងក្នុងម៉ាស៊ីន ចាប់ពី bit ដល់ការ boot", "យល់ពី memory, file, program និង OS",
                       "បង្កើតមូលដ្ឋានសម្រាប់ reversing, forensics និង exploitation"],
                      badge_en="A Practical Guide", second=""),
    },
    "java": {
        "folder": "23-java", "code": "java", "name": "Java", "slug": "java-programming",
        "logo_dark": "assets/logos/java/java-logo-dark-bg.svg", "logo_light": "assets/logos/java/java-logo-light-bg.svg",
        "icon": "assets/logos/java/java-icon.svg",
        "credit": "Java, JVM, and the Java logo are trademarks or registered trademarks of Oracle and/or its affiliates. We are not endorsed by or affiliated with Oracle.",
        "cover": {"style": "motif", "bg": "#121A28", "ink": "#FFFFFF", "second": "#EA2D2E", "accent": "#0074BD", "badge_ink": "#FFFFFF",
                  "motif": java_motif, "size": "120pt", "author_side": "right"},
        "theme": theme(
            primary="#C82324", surface="#F8FAFC", border="#D7E0EA", text="#16202E", muted="#526071",
            dark=("#121A28", "#1A2536", "#283850", "#F0F4F9", "#A2B4C7", "#EA2D2E"),
            code={"background": "#141E2D", "border": "#24354D", "highlight-line": "#1E2B3E", "text": "#E9EFF6",
                  "comment": "#7D8E9E", "keyword": "#FF6B6B", "string": "#97D8A8", "number": "#FFD166",
                  "type": "#56CCF2", "function": "#FF8C70", "punctuation": "#CAD5E2", "output": "#C2E8FF"},
            note_tint="#FFF5F5", note_text="#8A1818"),
        "fonts": ("Rubik", "Cascadia Code"),
        "font_faces": faces(("Rubik", "rubik"), ("Cascadia Code", "cascadia-code")),
        "slide_css": """
section.dark h1::after { content: "public class Main"; display: block; font: 700 36px/1 'Cascadia Code', monospace; color: #EA2D2E; margin-top: 18px; }
section.dark::before { content: "JVM"; position: absolute; right: 70px; bottom: 30px; font: 700 160px/1 'Cascadia Code', monospace;
  color: #0074BD; opacity: .18; }
section.recap { background: #F8FAFC; border-left: 14px solid #EA2D2E; }
pre.output { border-left-color: #EA2D2E; }
.footer span:first-child::before { content: "java"; font-family: 'Cascadia Code', monospace; font-weight: 700; color: #C82324; margin-right: 8px; }
section.dark .footer span:first-child::before { color: #EA2D2E; }
""",
        "book_css": """
pre.output { border-left-color: #EA2D2E; }
@page { @top-left { border-bottom-color: #C82324; } @top-right { border-bottom-color: #C82324; } }
""",
        "text": texts("Java Programming", "ការសរសេរកម្មវិធី",
                      ["Master modern Java from JVM fundamentals to Project Loom", "Build robust object-oriented services for back office systems", "Prepare for enterprise architecture and Spring Boot"],
                      ["រៀនភាសា Java ទំនើប ពីមូលដ្ឋានគ្រឹះ JVM ដល់ Project Loom", "បង្កើត service គ្រប់គ្រងទិន្នន័យតាមបែប OOP យ៉ាងរឹងមាំ", "ត្រៀមខ្លួនសម្រាប់ស្ថាបត្យកម្ម enterprise និង Spring Boot"]),
    },
    "spring-boot": {
        "folder": "24-spring-boot", "code": "java", "name": "Spring Boot", "slug": "spring-boot-development",
        "logo_dark": "assets/logos/spring-boot/spring-boot-logo-dark-bg.svg", "logo_light": "assets/logos/spring-boot/spring-boot-logo-light-bg.svg",
        "icon": "assets/logos/spring-boot/spring-boot-icon.svg",
        "credit": "Spring and Spring Boot are trademarks of Broadcom Inc. and/or its subsidiaries in the United States and other countries. We are not endorsed by or affiliated with Broadcom.",
        "cover": {"style": "motif", "bg": "#0D2116", "ink": "#FFFFFF", "second": "#6DB33F", "accent": "#85EA2D", "badge_ink": "#0D2116",
                  "motif": spring_motif, "size": "120pt", "author_side": "right"},
        "theme": theme(
            primary="#257833", surface="#F5FBF6", border="#CEE6D4", text="#13261A", muted="#486552",
            dark=("#0D2116", "#153020", "#1F452E", "#EEF9F1", "#9BC3A6", "#6DB33F"),
            code={"background": "#102317", "border": "#1E3F2A", "highlight-line": "#183322", "text": "#EAF7EE",
                  "comment": "#789C83", "keyword": "#6DB33F", "string": "#9EE6B8", "number": "#FFD3B6",
                  "type": "#56CCF2", "function": "#85EA2D", "punctuation": "#CFE5D6", "output": "#C8F7DC"},
            note_tint="#F0FAF3", note_text="#175424"),
        "fonts": ("Urbanist", "Intel One Mono"),
        "font_faces": faces(("Urbanist", "urbanist"), ("Intel One Mono", "intel-one-mono")),
        "slide_css": """
section.dark h1::after { content: "@SpringBootApplication"; display: block; font: 700 36px/1 'Intel One Mono', monospace; color: #6DB33F; margin-top: 18px; }
section.dark::before { content: "REST"; position: absolute; right: 70px; bottom: 30px; font: 700 160px/1 'Intel One Mono', monospace;
  color: #85EA2D; opacity: .15; }
section.recap { background: #F5FBF6; border-left: 14px solid #6DB33F; }
pre.output { border-left-color: #6DB33F; }
.footer span:first-child::before { content: "spring"; font-family: 'Intel One Mono', monospace; font-weight: 700; color: #257833; margin-right: 8px; }
section.dark .footer span:first-child::before { color: #6DB33F; }
""",
        "book_css": """
pre.output { border-left-color: #6DB33F; }
@page { @top-left { border-bottom-color: #257833; } @top-right { border-bottom-color: #257833; } }
""",
        "text": texts("Spring Boot Development", "ការអភិវឌ្ឍ",
                      ["Build fast REST APIs for mobile and web apps", "Master Spring Data JPA, Security, and JWT tokens", "Deploy containerized cloud-ready microservices"],
                      ["បង្កើត REST API លឿនសម្រាប់ app ទូរស័ព្ទ និង web", "ស្ទាត់ជំនាញ Spring Data JPA, Security និង JWT tokens", "ដាក់ឱ្យដំណើរការ microservice តាម container លើ cloud"],
                      second="Backend Development"),
    },
}



def _light(color):
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b > 140


# Courses with light title slides: terminal output (```console and ```sh blocks) normally uses the title slides'
# surface color, which would be light here. Give those blocks the dark code-panel color instead, so they stay readable.
for _course in COURSES.values():
    _theme = _course.get("theme", {})
    if _light(_theme.get("dark", {}).get("background", "#000000")):
        _fix = f"\npre.shell {{ background: {_theme['code']['background']}; }}\n"
        _course["slide_css"] = _course.get("slide_css", "") + _fix
        _course["book_css"] = _course.get("book_css", "") + _fix


# ------------------------------------------------------------------ book covers: Cambodia's heritage
# Every full book has the same cover layout (the Dart one): a pale page in the course's color, and a toned photo at the
# bottom. The photos show Cambodia's twelve UNESCO heritage items (from mcfa.gov.kh/unesco-world-heritage/) and, for
# the other books, Cambodian landmarks. A caption names the place, and for UNESCO items the date it was inscribed.
# Credits and licenses: assets/photos/README.md. Covers are made with `build_lessons.py <course> --cover`.

KM_MONTHS = ["មករា", "កុម្ភៈ", "មីនា", "មេសា", "ឧសភា", "មិថុនា", "កក្កដា", "សីហា", "កញ្ញា", "តុលា", "វិច្ឆិកា", "ធ្នូ"]
EN_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
KM_DIGITS = str.maketrans("0123456789", "០១២៣៤៥៦៧៨៩")


def heritage(en, km, date, intangible=False):
    """Caption for a UNESCO item: its name, and when it was inscribed. date is (day, month, year)."""
    day, month, year = date
    en_kind = "UNESCO Intangible Cultural Heritage" if intangible else "UNESCO World Heritage"
    km_kind = "បេតិកភណ្ឌវប្បធម៌អរូបី UNESCO" if intangible else "បេតិកភណ្ឌពិភពលោក UNESCO"
    return {"en": (en, f"{en_kind} · inscribed {day} {EN_MONTHS[month - 1]} {year}"),
            "km": (km, f"{km_kind} · ចុះបញ្ជី {str(day).translate(KM_DIGITS)} {KM_MONTHS[month - 1]} {str(year).translate(KM_DIGITS)}")}


def place(en, km, where_en, where_km):
    """Caption for a landmark: its name and where it is."""
    return {"en": (en, where_en), "km": (km, where_km)}


def _mix(color, white_share):
    """The color mixed with white; white_share 0.9 is a very pale tint."""
    rgb = [int(color[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(c + (255 - c) * white_share):02X}" for c in rgb)


def photo_cover(course, photo, credit, caption, position="50% 40%", fade=None):
    """The cover settings for a course, from its theme colors."""
    light = course["theme"]["light"]
    accent, text = light["primary"], light["text"]
    rgb = ",".join(str(int(text[i:i + 2], 16)) for i in (1, 3, 5))
    return {"page": (_mix(accent, .97), _mix(accent, .91), _mix(accent, .84)), "text": text, "accent": accent,
            "tint": (_mix(accent, .74), text), "glow": f"rgba({rgb},.22)", "square": True,
            "photo": f"assets/photos/{photo}", "photo_pos": position,
            "fade": fade or "transparent 0%,rgba(0,0,0,.12) 18%,rgba(0,0,0,.45) 36%,rgba(0,0,0,.85) 52%,#000 62%",
            "art": f'assets/covers/art/{course["folder"]}-cover-art.png', "photo_credit": credit, "caption": caption}


MCFA = "courtesy of the Ministry of Culture and Fine Arts of Cambodia (mcfa.gov.kh). Cropped and toned."
ANGKOR = (14, 12, 1992)

# course: (photo, credit, caption, position)
PHOTO_COVERS = {
    "flutter": ("royal-ballet-mcfa.jpg", f"Cover photo: the Royal Ballet of Cambodia, {MCFA}",
                heritage("Royal Ballet of Cambodia", "របាំព្រះរាជទ្រព្យ", (7, 11, 2003), True), "50% 20%"),
    "ios": ("chapei-dang-veng-mcfa.jpg", f"Cover photo: Chapei Dang Veng, {MCFA}",
            heritage("Chapei Dang Veng", "ចាប៉ីដងវែង", (30, 11, 2016), True), "50% 35%"),
    "android": ("bokator-mcfa.jpg", f"Cover photo: Kun Lbokator at the Bayon, {MCFA}",
                heritage("Kun Lbokator", "គុនល្បុក្កតោ", (29, 11, 2022), True), "50% 35%"),
    "react-native": ("lkhon-khol-mcfa.jpg", f"Cover photo: Lkhon Khol Wat Svay Andet, {MCFA}",
                     heritage("Lkhon Khol Wat Svay Andet", "ល្ខោនខោលវត្តស្វាយអណ្ដែត", (28, 11, 2018), True), "50% 60%"),
    "ci-cd": ("tugging-mcfa.jpg", f"Cover photo: tugging rituals and games, {MCFA}",
              heritage("Tugging rituals and games", "ល្បែងទាញព្រ័ត្រ", (2, 12, 2015), True), "50% 45%"),
    "automated-testing": ("krama-mcfa.jpg", f"Cover photo: weaving the Khmer krama, {MCFA}",
                          heritage("The Khmer Krama", "ក្រមាខ្មែរ", (4, 12, 2024), True), "50% 100%"),
    "mobile-architecture": ("royal-palace-commons.jpg",
                            "Cover photo: “2016 Phnom Penh, Pałac Królewski, Hala Tronowa (04)” by Marcin Konsek, CC BY-SA 4.0, via Wikimedia Commons. Cropped and toned.",
                            place("Throne Hall, Royal Palace", "ព្រះទីនាំងទេវាវិនិច្ឆ័យ ព្រះបរមរាជវាំង", "Phnom Penh", "រាជធានីភ្នំពេញ"), "50% 45%"),
    "mobile-security": ("banteay-srei-commons.jpg",
                        "Cover photo: “Banteay Srei Temple” by Mig Gilbert, CC BY-SA 2.0, via Wikimedia Commons. Cropped and toned.",
                        heritage("Banteay Srei, Angkor", "ប្រាសាទបន្ទាយស្រី អង្គរ", ANGKOR), "50% 55%"),
    "observability": ("wat-phnom-commons.jpg",
                      "Cover photo: “2016 Phnom Penh, Wat Phnom (07)” by Marcin Konsek, CC BY-SA 4.0, via Wikimedia Commons. Cropped and toned.",
                      place("Wat Phnom", "វត្តភ្នំ", "Phnom Penh", "រាជធានីភ្នំពេញ"), "50% 40%"),
    "performance": ("kulen-commons.jpg",
                    "Cover photo: “PhnomKulen” by Narith5, CC BY 2.0, via Wikimedia Commons. Cropped and toned.",
                    place("Phnom Kulen waterfall", "ទឹកធ្លាក់ភ្នំគូលែន", "Siem Reap", "ខេត្តសៀមរាប"), "50% 40%"),
    "release-engineering": ("central-market-commons.jpg",
                            "Cover photo: “PhsarThmei” by Jpatokal (Wikivoyage), CC BY-SA 4.0, via Wikimedia Commons. Cropped and toned.",
                            place("Central Market", "ផ្សារធំថ្មី", "Phnom Penh", "រាជធានីភ្នំពេញ"), "50% 40%"),
    "data-networking": ("mekong-kratie-commons.jpg",
                        "Cover photo: “Mekong River Scene - Kratie - Cambodia” by Adam Jones, CC BY-SA 2.0, via Wikimedia Commons. Cropped and toned.",
                        place("The Mekong River", "ទន្លេមេគង្គ", "Kratie", "ខេត្តក្រចេះ"), "50% 55%"),
    "accessibility-localization": ("national-museum-commons.jpg",
                                   "Cover photo: “2016 Phnom Penh, Muzeum Narodowe Kambodży (10)” by Marcin Konsek, CC BY-SA 4.0, via Wikimedia Commons. Cropped and toned.",
                                   place("National Museum of Cambodia", "សារមន្ទីរជាតិ", "Phnom Penh", "រាជធានីភ្នំពេញ"), "50% 45%"),
    "developer-workflow": ("silver-pagoda-commons.jpg",
                           "Cover photo: “2016 Phnom Penh, Pałac Królewski, Srebrna Pagoda (05)” by Marcin Konsek, CC BY-SA 4.0, via Wikimedia Commons. Cropped and toned.",
                           place("Silver Pagoda, Royal Palace", "វត្តព្រះកែវមរកត ព្រះបរមរាជវាំង", "Phnom Penh", "រាជធានីភ្នំពេញ"), "50% 40%"),
    "c-cpp": ("bayon-commons.jpg",
              "Cover photo: “Bayon” by lumoplank, CC0, via Wikimedia Commons. Cropped and toned.",
              heritage("Bayon, Angkor Thom", "ប្រាសាទបាយ័ន អង្គរធំ", ANGKOR), "50% 40%"),
    "rust": ("ta-prohm-commons.jpg",
             "Cover photo: “Ta Prohm, Angkor 22” by LBM1948, CC BY-SA 4.0, via Wikimedia Commons. Cropped and toned.",
             heritage("Ta Prohm, Angkor", "ប្រាសាទតាព្រហ្ម អង្គរ", ANGKOR), "50% 40%"),
    "java": ("bokor-commons.jpg",
             "Cover photo: “View over Catholic Church from Rear - Bokor Hill Station” by Adam Jones, CC BY-SA 2.0, via Wikimedia Commons. Cropped and toned.",
             place("Bokor Hill Station", "ភ្នំបូកគោ", "Kampot", "ខេត្តកំពត"), "50% 40%"),
    "spring-boot": ("beng-mealea-commons.jpg",
                    "Cover photo: “Ancient Khmer Temple of Beng Mealea” by Gary Todd, CC0, via Wikimedia Commons. Cropped and toned.",
                    place("Beng Mealea", "ប្រាសាទបឹងមាលា", "Siem Reap", "ខេត្តសៀមរាប"), "50% 45%"),
}

# Captions for the covers that were set up by hand.
CAPTIONS = {
    "dart": heritage("Angkor Wat, Angkor", "ប្រាសាទអង្គរវត្ត អង្គរ", ANGKOR),
    "swift": place("Independence Monument", "វិមានឯករាជ្យ", "Phnom Penh", "រាជធានីភ្នំពេញ"),
    "kotlin": heritage("Temple of Preah Vihear", "ប្រាសាទព្រះវិហារ", (7, 7, 2008)),
    "javascript": heritage("Sbek Thom, Khmer shadow theatre", "ល្ខោនស្បែកធំ", (25, 11, 2005), True),
    "typescript": heritage("Koh Ker", "ប្រាសាទកោះកេរ", (17, 9, 2023)),
    "web": heritage("Sambor Prei Kuk", "ប្រាសាទសំបូរព្រៃគុក", (8, 7, 2017)),
}


# Topic books whose title does not say they are about mobile apps: "for Mobile Apps" in small type after the title.
FOR_MOBILE = ["observability", "release-engineering", "data-networking", "accessibility-localization", "developer-workflow"]


def apply_covers(courses):
    """Give every course its heritage cover and caption. Called by build_lessons.py once all courses are known."""
    for key, (photo, credit, caption, position) in PHOTO_COVERS.items():
        keep = {k: v for k, v in courses[key]["cover"].items() if k in ("icon_width", "fade", "photo_pos")}
        courses[key]["cover"] = {**photo_cover(courses[key], photo, credit, caption, position), **keep}
    for key, caption in CAPTIONS.items():
        courses[key]["cover"]["caption"] = caption
    for key in FOR_MOBILE:
        courses[key]["cover"]["label"] = {"en": "for Mobile Apps", "km": "សម្រាប់ Mobile App"}
        courses[key]["cover"]["label_style"] = "inline"  # chosen by the author on 2026-11-11, over a label above the title


# ------------------------------------------------------------------ logo honeycombs on covers
# A book that is not about one technology shows a honeycomb on its cover: its own mark in the middle, and the platforms
# and tools it covers around it, so it is clear the book is about mobile apps. iOS is shown by the Swift logo (Apple's
# own logo may not be used). Drawn by assets/logos/build_logo_sets.py; rules and credits in assets/logos/README.md.

# name: (file, hexagon color, logo size as a share of the hexagon's radius)
LOGO_FILES = {
    "html5": ("assets/logos/html5/html5-icon.svg", "#F2F2F2", 1.25),
    "css": ("assets/logos/css/css-icon.svg", "#663399", 1.15),
    "javascript": ("assets/logos/javascript/javascript-icon.svg", "#F7DF1E", 1.15),
    "typescript": ("assets/logos/typescript/typescript-icon.svg", "#3178C6", 1.15),
    "react": ("assets/logos/react-native/react-native-icon.svg", "#20232A", 1.15),
    "firebase": ("assets/logos/firebase/firebase-icon.svg", "#FFFFFF", 1.05),
    "git": ("assets/logos/git/git-icon.svg", "#FFFFFF", 0.95),
    "android": ("assets/logos/android/android-robot-head.svg", "#FFFFFF", 1.05),
    "swift": ("assets/logos/swift/swift-icon.svg", "#F05138", 1.15),
    "flutter": ("assets/logos/flutter/flutter-icon.svg", "#FFFFFF", 0.95),
    "kotlin": ("assets/logos/kotlin/kotlin-icon.svg", "#FFFFFF", 0.85),
    "dart": ("assets/logos/dart/dart-icon.svg", "#FFFFFF", 1.0),
    "vscode": ("assets/logos/vscode/vscode-icon.svg", "#FFFFFF", 0.95),
    "android-studio": ("assets/logos/android-studio/android-studio-icon.svg", "#FFFFFF", 1.0),
}

MOBILE = ["android", "swift", "flutter", "react", "kotlin"]
# course: (middle, the six around it, clockwise from the top left)
LOGO_SETS = {
    "web": ("html5", ["javascript", "typescript", "react", "firebase", "git", "css"]),
    "ci-cd": ("ci-cd", ["git"] + MOBILE),
    "automated-testing": ("automated-testing", MOBILE + ["dart"]),
    "mobile-architecture": ("mobile-architecture", MOBILE + ["dart"]),
    "mobile-security": ("mobile-security", MOBILE + ["dart"]),
    "observability": ("observability", ["firebase"] + MOBILE),
    "performance": ("performance", ["android-studio"] + MOBILE),
    "release-engineering": ("release-engineering", MOBILE + ["dart"]),
    "data-networking": ("data-networking", ["firebase"] + MOBILE),
    "accessibility-localization": ("accessibility-localization", MOBILE + ["dart"]),
    "developer-workflow": ("developer-workflow", ["git", "vscode", "android-studio", "android", "swift", "flutter"]),
}

LOGO_CREDITS = {
    "android": "The Android robot is reproduced or modified from work created and shared by Google and used according to terms described in the Creative Commons 3.0 Attribution License.",
    "google": "Android, Android Studio, Dart, Flutter, Firebase, and the related logos are trademarks of Google LLC.",
    "swift": "Swift and the Swift logo are trademarks of Apple Inc.",
    "kotlin": "Kotlin is a trademark of the Kotlin Foundation.",
    "react": "React Native and the React logo are trademarks of Meta Platforms, Inc.",
    "git": "Git Logo by Jason Long is licensed under the Creative Commons Attribution 3.0 Unported License.",
    "vscode": "Visual Studio Code and the Visual Studio Code icon are trademarks of Microsoft Corporation.",
}


def apply_logo_sets(courses):
    """Covers of the courses in LOGO_SETS use their honeycomb, larger than a single logo, with the logos' credits."""
    for key, (center, around) in LOGO_SETS.items():
        course = courses[key]
        course["icon"] = f"assets/logos/honeycomb/{key}.svg"
        course["cover"]["icon_width"] = 72
        if key == "web":
            continue  # its credit line was written by hand
        used = set(around)
        lines = [LOGO_CREDITS["android"]] if "android" in used else []
        lines.append(LOGO_CREDITS["google"])
        lines += [LOGO_CREDITS[k] for k in ("swift", "kotlin", "react", "git", "vscode") if k in used]
        course["credit"] = " ".join(lines) + " " + course["credit"]
