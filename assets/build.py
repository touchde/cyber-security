"""Generate the slide templates and concept diagrams from theme/tokens.json.

Run from anywhere:

    python3 assets/build.py

Every SVG in templates/ and diagrams/ is overwritten. Edit this script (not the
SVGs) to change them, so colors and fonts stay consistent across all assets.
SVGs use presentation attributes rather than CSS so they import cleanly into
Keynote, PowerPoint, Google Slides, and Figma.
"""
import json
import pathlib
import re
from html import escape

ROOT = pathlib.Path(__file__).parent
T = json.loads((ROOT / "theme/tokens.json").read_text())
L, DK, C, CO, DG = T["light"], T["dark"], T["code"], T["callout"], T["diagram"]
SANS = "Inter, 'Helvetica Neue', Arial, sans-serif"
MONO = "'JetBrains Mono', Menlo, Consolas, monospace"


# ---------------------------------------------------------------- helpers

def icon_path(name):
    """Return the path data of a Material Symbols icon (viewBox 0 -960 960 960)."""
    svg = (ROOT / "icons/material-symbols" / f"{name}.svg").read_text()
    return re.search(r' d="([^"]+)"', svg)[1]


def icon(name, x, y, size, color):
    s = size / 960
    return (f'<g transform="translate({x} {y + size}) scale({s:.5f})">'
            f'<path d="{icon_path(name)}" fill="{color}"/></g>')


def text(x, y, s, size=20, color=None, weight=400, anchor="start", mono=False, italic=False):
    color = color or L["text"]
    style = ' font-style="italic"' if italic else ""
    return (f'<text x="{x}" y="{y}" font-family="{escape(MONO if mono else SANS)}" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}" '
            f'text-anchor="{anchor}"{style}>{escape(s)}</text>')


def rect(x, y, w, h, fill, stroke="none", sw=0, r=12, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    # Course style: square corners everywhere, so r is not used.
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def node(x, y, w, h, title, sub=None, kind="node", mono=True, title_size=20):
    """A labeled box. kind: node | alt | highlight | muted."""
    fill, stroke = {
        "node": (DG["node-fill"], DG["node-stroke"]),
        "alt": (DG["node-alt-fill"], DG["node-stroke"]),
        "highlight": (DG["highlight-fill"], DG["highlight"]),
        "muted": (L["surface"], L["border"]),
    }[kind]
    out = [rect(x, y, w, h, fill, stroke, 2)]
    cx = x + w / 2
    if sub:
        out.append(text(cx, y + h / 2 - 4, title, title_size, weight=600, anchor="middle", mono=mono))
        out.append(text(cx, y + h / 2 + 20, sub, 15, L["text-muted"], anchor="middle"))
    else:
        out.append(text(cx, y + h / 2 + title_size * 0.35, title, title_size, weight=600, anchor="middle", mono=mono))
    return "".join(out)


def group(x, y, w, h, label, code=False):
    """Dashed container. Plain labels are upper-cased; code labels keep their case."""
    label_svg = (text(x + 16, y + 30, label, 16, L["text-muted"], 700, mono=True) if code
                 else text(x + 16, y + 28, label.upper(), 13, L["text-muted"], 700))
    return rect(x, y, w, h, DG["group-fill"], DG["group-stroke"], 2, 16, "8 6") + label_svg


def arrow(x1, y1, x2, y2, color=None, dashed=False, label=None, label_pos=0.5,
          label_dx=0, label_dy=-10, label_anchor="middle", width=2.5):
    color = color or DG["arrow"]
    mid = "arrow-" + color.lstrip("#")
    dash = ' stroke-dasharray="7 6"' if dashed else ""
    out = (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
           f'stroke-width="{width}"{dash} marker-end="url(#{mid})"/>')
    if label:
        lx = x1 + (x2 - x1) * label_pos + label_dx
        ly = y1 + (y2 - y1) * label_pos + label_dy
        out += text(lx, ly, label, 15, color, 600, label_anchor)
    return out


def path_arrow(d, color=None, dashed=False):
    color = color or DG["arrow"]
    mid = "arrow-" + color.lstrip("#")
    dash = ' stroke-dasharray="7 6"' if dashed else ""
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.5"{dash} '
            f'marker-end="url(#{mid})"/>')


def markers(colors):
    out = []
    for c in sorted(set(colors)):
        out.append(f'<marker id="arrow-{c.lstrip("#")}" viewBox="0 0 14 12" refX="11" refY="6" markerUnits="userSpaceOnUse" '
                   f'markerWidth="14" markerHeight="12" orient="auto-start-reverse">'
                   f'<path d="M0,0 L14,6 L0,12 z" fill="{c}"/></marker>')
    return "<defs>" + "".join(out) + "</defs>"


def svg(w, h, body, title, bg=None):
    colors = re.findall(r'url\(#arrow-([0-9A-Fa-f]{6})\)', body)
    bg_rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">'
            f'<title>{escape(title)}</title>'
            + markers("#" + c for c in colors) + bg_rect + body + "</svg>\n")


def heading(w, title, subtitle=None):
    out = text(40, 52, title, 28, weight=700)
    if subtitle:
        out += text(40, 82, subtitle, 17, L["text-muted"])
    return out


def write(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)
    print("wrote", rel)


# ---------------------------------------------------------------- templates

def code_panel():
    """Dark code panel: window dots, file tab, highlighted line, output strip."""
    W, LH, X0, Y0 = 960, 34, 64, 118
    lines = [
        [("kw", "void "), ("fn", "main"), ("p", "() {")],
        [("t", "  "), ("kw", "final "), ("t", "name = "), ("s", "'Mina'"), ("p", ";")],
        [("t", "  "), ("kw", "final "), ("t", "age = "), ("n", "21"), ("p", ";")],
        [("t", "  "), ("fn", "print"), ("p", "("), ("s", "'$name is $age years old'"), ("p", ");")],
        [("t", "  "), ("c", "// Prints one line to the console")],
        [("p", "}")],
    ]
    color = {"kw": C["keyword"], "fn": C["function"], "s": C["string"], "n": C["number"],
             "c": C["comment"], "p": C["punctuation"], "t": C["text"]}
    highlight = 3
    H = Y0 + LH * len(lines) + 120
    b = [rect(0, 0, W, H, C["background"], C["border"], 2, 20)]
    for i, dot in enumerate(C["window-dots"]):
        b.append(f'<circle cx="{32 + i * 24}" cy="32" r="7" fill="{dot}"/>')
    b.append(text(W - 32, 38, "main.dart", 16, C["comment"], anchor="end", mono=True))
    b.append(f'<line x1="0" y1="64" x2="{W}" y2="64" stroke="{C["border"]}" stroke-width="2"/>')
    b.append(rect(2, Y0 + LH * highlight - 24, W - 4, LH, C["highlight-line"], r=0))
    b.append(rect(2, Y0 + LH * highlight - 24, 4, LH, DK["primary"], r=0))
    for i, toks in enumerate(lines):
        y = Y0 + LH * i
        b.append(text(36, y, str(i + 1), 18, C["comment"], anchor="end", mono=True))
        italic = ' font-style="italic"'
        spans = "".join(f'<tspan fill="{color[k]}"{italic if k == "c" else ""}>{escape(v)}</tspan>'
                        for k, v in toks)
        b.append(f'<text x="{X0}" y="{y}" font-family="{escape(MONO)}" font-size="22" '
                 f'xml:space="preserve">{spans}</text>')
    oy = Y0 + LH * len(lines) + 8
    b.append(f'<line x1="0" y1="{oy}" x2="{W}" y2="{oy}" stroke="{C["border"]}" stroke-width="2"/>')
    b.append(text(32, oy + 40, "OUTPUT", 13, C["comment"], 700))
    b.append(text(32, oy + 76, "Mina is 21 years old", 22, C["output"], mono=True))
    write("templates/code-panel.svg", svg(W, H, "".join(b), "Code panel template"))


def screenshot_placeholder(x, y, w, h, r=0):
    """Dashed screen area marking where a real screenshot goes."""
    cx, cy = x + w / 2, y + h / 2
    return "".join([
        rect(x, y, w, h, L["surface"], r=r),
        rect(x + 16, y + 16, w - 32, h - 32, "none", L["text-muted"], 2, max(r - 8, 8), "10 8"),
        icon("photo_camera", cx - 32, cy - 76, 64, L["text-muted"]),
        text(cx, cy + 22, "SCREENSHOT", 22, L["text-muted"], 700, "middle"),
        text(cx, cy + 52, f"{w} × {h}", 18, L["text-muted"], 400, "middle", mono=True),
        text(cx, cy + 82, "Replace with the running app", 16, L["text-muted"], 400, "middle"),
    ])


def write_frame(name, w, h, body, title, screen):
    """Write the empty frame and a placeholder version with the screen filled in."""
    write(f"templates/{name}-frame.svg", svg(w, h, body, title))
    write(f"templates/{name}-placeholder.svg",
          svg(w, h, screenshot_placeholder(*screen) + body, f"{name.capitalize()} screenshot placeholder"))


def phone_placeholder():
    """Plain 390x844 placeholder box. No device frame: the screenshot replaces it as-is."""
    W, H = 390, 844
    write("templates/phone-placeholder.svg",
          svg(W, H, screenshot_placeholder(0, 0, W, H, 24), "Phone screenshot placeholder, 390 by 844"))


def browser_frame():
    """Browser window. Content area is a transparent 1280x720 cutout at (0, 56)."""
    W, H, TB = 1280, 776, 56
    b = [f'<path d="M14 0 H{W - 14} A14 14 0 0 1 {W} 14 V{TB} H0 V14 A14 14 0 0 1 14 0 Z" fill="{L["surface"]}"/>',
         f'<path d="M0 {TB} H{W} V{H - 14} A14 14 0 0 1 {W - 14} {H} H14 A14 14 0 0 1 0 {H - 14} Z" '
         f'fill="none" stroke="{L["border"]}" stroke-width="2"/>',
         f'<line x1="0" y1="{TB}" x2="{W}" y2="{TB}" stroke="{L["border"]}" stroke-width="2"/>']
    for i, dot in enumerate(C["window-dots"]):
        b.append(f'<circle cx="{26 + i * 22}" cy="28" r="7" fill="{dot}"/>')
    b.append(rect(120, 12, W - 240, 32, L["background"], L["border"], 1.5, 16))
    b.append(icon("lock", 136, 19, 18, L["text-muted"]))
    b.append(text(162, 34, "localhost:8080", 16, L["text-muted"]))
    write_frame("browser", W, H, "".join(b),
                "Browser frame. Place a 1280 by 720 screenshot at x 0, y 56.", (0, TB, W, H - TB, 0))


def desktop_frame():
    """Desktop app window. Content area is a transparent 1280x760 cutout at (0, 40)."""
    W, H, TB = 1280, 800, 40
    b = [f'<path d="M12 0 H{W - 12} A12 12 0 0 1 {W} 12 V{TB} H0 V12 A12 12 0 0 1 12 0 Z" fill="{L["surface"]}"/>',
         f'<path d="M0 {TB} H{W} V{H - 12} A12 12 0 0 1 {W - 12} {H} H12 A12 12 0 0 1 0 {H - 12} Z" '
         f'fill="none" stroke="{L["border"]}" stroke-width="2"/>',
         f'<line x1="0" y1="{TB}" x2="{W}" y2="{TB}" stroke="{L["border"]}" stroke-width="2"/>']
    for i, dot in enumerate(C["window-dots"]):
        b.append(f'<circle cx="{24 + i * 22}" cy="20" r="6.5" fill="{dot}"/>')
    b.append(text(W / 2, 26, "My Flutter App", 15, L["text-muted"], 600, "middle"))
    write_frame("desktop", W, H, "".join(b),
                "Desktop window frame. Place a 1280 by 760 screenshot at x 0, y 40.", (0, TB, W, H - TB, 0))


def callouts():
    icons = {"note": "info", "tip": "lightbulb", "warning": "warning", "practice": "edit_note"}
    for kind, c in CO.items():
        W, H = 520, 120
        b = [rect(0, 0, W, H, c["tint"], r=14),
             rect(0, 0, 8, H, c["accent"], r=0),
             icon(icons[kind], 28, 22, 32, c["accent"]),
             text(70, 48, c["label"], 22, c["text"], 700),
             text(28, 92, "Short message goes here.", 19, c["text"])]
        write(f"templates/callout-{kind}.svg", svg(W, H, "".join(b), f"{c['label']} callout"))
        # Compact badge: icon + label only, for slide corners and section headers.
        bw = 60 + len(c["label"]) * 13
        b = [rect(0, 0, bw, 40, c["tint"], c["accent"], 2, 20),
             icon(icons[kind], 12, 8, 24, c["accent"]),
             text(44, 27, c["label"], 17, c["text"], 700)]
        write(f"templates/badge-{kind}.svg", svg(bw, 40, "".join(b), f"{c['label']} badge"))


# ---------------------------------------------------------------- diagrams

def widget_tree():
    W, H = 1100, 680
    b = [heading(W, "The widget tree", "Each widget describes part of the UI. Parents contain children.")]
    nodes = {
        "MaterialApp": (450, 120, "alt"), "Scaffold": (450, 220, "node"),
        "AppBar": (200, 330, "node"), "Center": (700, 330, "node"),
        "Text 'Home'": (200, 440, "node"), "Column": (700, 440, "node"),
        "Text 'Count: 0'": (520, 560, "node"), "ElevatedButton": (880, 560, "node"),
    }
    w, h = 200, 60
    edges = [("MaterialApp", "Scaffold"), ("Scaffold", "AppBar"), ("Scaffold", "Center"),
             ("AppBar", "Text 'Home'"), ("Center", "Column"), ("Column", "Text 'Count: 0'"),
             ("Column", "ElevatedButton")]
    for a, z in edges:
        ax, ay, _ = nodes[a]
        zx, zy, _ = nodes[z]
        b.append(f'<path d="M{ax + w / 2} {ay + h} V{(ay + h + zy) / 2} H{zx + w / 2} V{zy}" '
                 f'fill="none" stroke="{DG["arrow"]}" stroke-width="2.5"/>')
    for name, (x, y, kind) in nodes.items():
        b.append(node(x, y, w, h, name, kind=kind))
    for label, (cx, cy) in {"title:": (300, 432), "body:": (800, 322), "child:": (800, 432),
                            "children:": (800, 528)}.items():
        b.append(text(cx + 8, cy - 4, label, 15, L["text-muted"], 600))
    write("diagrams/02-flutter/widget-tree.svg", svg(W, H, "".join(b), "Flutter widget tree", L["background"]))


def layout_constraints():
    W, H = 1100, 560
    b = [heading(W, "How Flutter layout works", "Constraints go down. Sizes go up. Parents set positions.")]
    b.append(rect(80, 130, 940, 380, DG["node-alt-fill"], DG["node-stroke"], 2, 16))
    b.append(text(110, 170, "Parent", 22, weight=700, mono=True))
    b.append(text(110, 196, "e.g. Center inside a 400 × 800 screen", 15, L["text-muted"]))
    b.append(node(640, 300, 260, 120, "Child", "chooses 120 × 48", kind="node"))
    b.append(arrow(380, 300, 630, 330, DG["node-stroke"], label="① Constraints go down",
                   label_pos=0.0, label_dx=-10, label_dy=-46, label_anchor="start"))
    b.append(text(370, 278, "min 0 × 0, max 400 × 800", 15, L["text-muted"]))
    b.append(arrow(630, 400, 380, 430, DG["highlight"], label="② Size goes up",
                   label_pos=1.0, label_dx=0, label_dy=34, label_anchor="start"))
    b.append(text(380, 486, "“I'm 120 × 48”", 15, L["text-muted"]))
    b.append(path_arrow("M900 250 C 960 250, 960 290, 905 300", DG["arrow"], dashed=True))
    b.append(text(870, 236, "③ Parent sets position", 15, DG["arrow"], 600, "middle"))
    write("diagrams/02-flutter/layout-constraints.svg",
          svg(W, H, "".join(b), "Flutter layout: constraints down, sizes up, parent sets position", L["background"]))


def stateful_lifecycle():
    W, H = 1100, 640
    b = [heading(W, "StatefulWidget lifecycle", "Methods the framework calls on a State object")]
    w, h = 260, 64
    steps = [("createState()", "framework creates State", 120, "muted"),
             ("initState()", "once: set up controllers", 220, "node"),
             ("didChangeDependencies()", "inherited data changed", 320, "node"),
             ("build()", "describe the UI", 420, "alt")]
    x = 80
    for t_, sub, y, kind in steps:
        b.append(node(x, y, w + 60, h, t_, sub, kind, title_size=19))
    for y in (184, 284, 384):
        b.append(arrow(x + 160, y, x + 160, y + 34))
    # Rebuild triggers on the right
    rx = 560
    b.append(group(rx - 20, 110, 500, 300, "Triggers a rebuild"))
    triggers = [("setState()", "state changed", 160), ("didUpdateWidget()", "parent sent new config", 250),
                ("didChangeDependencies()", "inherited data changed", 340)]
    for t_, sub, y in triggers:
        b.append(node(rx, y, 300, 56, t_, sub, "node", title_size=17))
        b.append(arrow(rx, y + 28, x + 330, 452, DG["node-stroke"], dashed=True))
    # Teardown
    b.append(node(x, 530, 220, 60, "deactivate()", "removed for now", "muted", title_size=18))
    b.append(node(x + 320, 530, 220, 60, "dispose()", "removed for good", "highlight", title_size=18))
    b.append(arrow(x + 160, 484, x + 110, 524, label="removed from tree", label_dx=34, label_dy=4, label_anchor="start"))
    b.append(arrow(x + 225, 560, x + 314, 560))
    b.append(text(x + 560, 556, "Release controllers,", 15, DG["highlight"], 600))
    b.append(text(x + 560, 576, "listeners, and subscriptions", 15, DG["highlight"], 600))
    write("diagrams/02-flutter/stateful-lifecycle.svg",
          svg(W, H, "".join(b), "StatefulWidget lifecycle", L["background"]))


def app_architecture():
    W, H = 1100, 640
    b = [heading(W, "App architecture layers", "A common MVVM-style organization. Commands flow down, data flows up.")]
    layers = [("View", "widgets: display data, forward user actions", "alt"),
              ("ViewModel", "prepares UI state, exposes commands", "node"),
              ("Repository", "source of truth: caching, error handling", "node"),
              ("Service", "talks to external systems", "node")]
    x, w, h = 300, 500, 76
    for i, (t_, sub, kind) in enumerate(layers):
        y = 120 + i * 112
        b.append(node(x, y, w, h, t_, sub, kind))
        if i < 3:
            b.append(arrow(x + 180, y + h + 4, x + 180, y + 108 - 4, DG["node-stroke"]))
            b.append(arrow(x + 320, y + 108 - 4, x + 320, y + h + 4, DG["highlight"]))
    b.append(text(x - 20, 200, "commands", 16, DG["node-stroke"], 700, "end"))
    b.append(text(x - 20, 222, "flow down ↓", 16, DG["node-stroke"], 700, "end"))
    b.append(text(x + w + 20, 200, "data", 16, DG["highlight"], 700))
    b.append(text(x + w + 20, 222, "flows up ↑", 16, DG["highlight"], 700))
    ext = [("REST API", "api"), ("Database", "database"), ("Platform plugin", "smartphone")]
    for i, (t_, ic) in enumerate(ext):
        ex = 190 + i * 260
        b.append(rect(ex, 560, 200, 52, L["surface"], L["border"], 2))
        b.append(icon(ic, ex + 16, 574, 24, L["text-muted"]))
        b.append(text(ex + 50, 592, t_, 17, L["text"], 600))
        b.append(f'<line x1="{x + w / 2}" y1="{120 + 3 * 112 + h}" x2="{ex + 100}" y2="558" '
                 f'stroke="{DG["arrow"]}" stroke-width="2" stroke-dasharray="6 5"/>')
    write("diagrams/app-architecture-layers.svg",
          svg(W, H, "".join(b), "App architecture layers: View, ViewModel, Repository, Service", L["background"]))


def rest_flow():
    W, H = 1100, 560
    b = [heading(W, "A REST request, step by step", "The app asks; the server answers with a status code and JSON.")]
    b.append(group(40, 120, 380, 400, "Flutter app"))
    b.append(node(70, 170, 320, 64, "Widget", "user taps “Load todos”", "alt"))
    b.append(node(70, 290, 320, 64, "http.get(uri)", "send the request", "node"))
    b.append(node(70, 410, 320, 64, "Todo.fromJson(...)", "parse and show the data", "node"))
    b.append(arrow(230, 236, 230, 284))
    b.append(group(680, 120, 380, 400, "Server"))
    b.append(node(710, 230, 320, 64, "API endpoint", "GET /todos", "node"))
    b.append(node(710, 380, 320, 64, "Database", "reads the records", "muted"))
    b.append(arrow(870, 296, 870, 374))
    b.append(arrow(394, 312, 704, 262, DG["node-stroke"], label="GET /todos  ·  headers", label_dy=-24))
    b.append(arrow(704, 280, 394, 432, DG["highlight"]))
    b.append(text(560, 446, "200 OK  ·  JSON body", 15, DG["highlight"], 600, "middle"))
    b.append(text(560, 472, '[{"id": 1, "title": …}]', 14, L["text-muted"], anchor="middle", mono=True))
    write("diagrams/rest-request-flow.svg",
          svg(W, H, "".join(b), "REST request flow between a Flutter app and a server", L["background"]))


def state_management():
    W, H = 1100, 600
    b = [heading(W, "Local state vs shared state", "Start local. Lift state up when several widgets need it.")]
    # Local
    b.append(group(40, 120, 440, 440, "Local state · setState()"))
    b.append(node(90, 190, 340, 70, "CounterButton", "owns count", "alt"))
    b.append(path_arrow("M230 262 C 200 310, 330 310, 296 266", DG["node-stroke"]))
    b.append(text(260, 336, "setState(() => count++)", 16, DG["node-stroke"], 600, "middle", mono=True))
    b.append(text(260, 400, "Only this widget", 17, L["text-muted"], anchor="middle"))
    b.append(text(260, 424, "needs the value.", 17, L["text-muted"], anchor="middle"))
    # Shared
    b.append(group(520, 120, 540, 440, "Shared state · ChangeNotifier, Provider, BLoC…"))
    b.append(node(640, 180, 300, 70, "CartModel", "state holder", "highlight"))
    kids = [("CartBadge", 615), ("ProductList", 790), ("CheckoutPage", 965)]
    for name, cx in kids:
        b.append(node(cx - 80, 420, 160, 60, name, kind="node", title_size=16))
        b.append(arrow(790, 252, cx, 414, DG["highlight"], dashed=True))
    b.append(text(1045, 290, "notifies listeners → rebuild", 15, DG["highlight"], 600, "end"))
    b.append(path_arrow("M745 420 C 700 360, 700 300, 722 258", DG["node-stroke"]))
    b.append(text(696, 300, "add(item)", 15, DG["node-stroke"], 600, "end", mono=True))
    write("diagrams/state-local-vs-shared.svg",
          svg(W, H, "".join(b), "Local state compared with shared state", L["background"]))


def ci_cd():
    W, H = 1290, 440
    b = [heading(W, "A CI/CD pipeline", "Every change is checked automatically before it can reach users.")]
    ci = [("Push / PR", "code", "muted"), ("Format", "format_paint", "node"), ("Analyze", "search", "node"),
          ("Test", "science", "node"), ("Build", "build", "node")]
    cd = [("Internal testing", "group", "alt"), ("Store review", "verified_user", "alt"),
          ("Release", "rocket_launch", "highlight")]
    w, h, gap, y = 128, 96, 20, 200
    b.append(group(24, 140, 5 * (w + gap) + 12, 210, "Continuous integration"))
    b.append(group(24 + 5 * (w + gap) + 30, 140, 3 * (w + gap) + 12, 210, "Continuous delivery"))
    x = 40
    for i, (label, ic, kind) in enumerate(ci + cd):
        if i == 5:
            x += 30
        b.append(node(x, y, w, h, "", kind=kind))
        accent = DG["highlight"] if kind == "highlight" else DG["node-stroke"]
        b.append(icon(ic, x + w / 2 - 16, y + 16, 32, accent))
        b.append(text(x + w / 2, y + 76, label, 15, L["text"], 600, "middle"))
        if i < 7:
            nx = x + w + gap + (30 if i == 4 else 0)
            b.append(arrow(x + w + 3, y + h / 2, nx - 3, y + h / 2))
        x += w + gap
    b.append(text(40, 390, "A failed step stops the pipeline and reports back on the pull request.", 16,
                  L["text-muted"]))
    write("diagrams/ci-cd-pipeline.svg", svg(W, H, "".join(b), "CI/CD pipeline stages", L["background"]))


def git_branches():
    W, H = 1100, 420
    b = [heading(W, "Branches and pull requests", "Work on a branch, open a pull request, merge after review.")]
    main_y, feat_y = 200, 320
    b.append(f'<line x1="80" y1="{main_y}" x2="1020" y2="{main_y}" stroke="{DG["node-stroke"]}" stroke-width="4"/>')
    b.append(path_arrow(f"M240 {main_y} C 300 {main_y}, 300 {feat_y}, 360 {feat_y} H 700 "
                        f"C 760 {feat_y}, 760 {main_y}, 812 {main_y + 4}", DG["highlight"]))
    for cx in (120, 240, 560, 820, 980):
        b.append(f'<circle cx="{cx}" cy="{main_y}" r="12" fill="{L["background"]}" stroke="{DG["node-stroke"]}" stroke-width="4"/>')
    for cx in (400, 520, 640):
        b.append(f'<circle cx="{cx}" cy="{feat_y}" r="12" fill="{L["background"]}" stroke="{DG["highlight"]}" stroke-width="4"/>')
    b.append(text(80, main_y - 26, "main", 18, DG["node-stroke"], 700, mono=True))
    b.append(text(360, feat_y + 44, "feature/login-form", 18, DG["highlight"], 700, mono=True))
    b.append(text(520, feat_y - 24, "commits", 15, L["text-muted"], 600, "middle"))
    b.append(text(560, main_y - 26, "teammate's commit", 15, L["text-muted"], 600, "middle"))
    b.append(rect(740, 236, 180, 40, L["background"], DG["arrow"], 2, 20))
    b.append(icon("merge", 752, 244, 24, DG["arrow"]))
    b.append(text(782, 262, "PR: review + CI", 15, DG["arrow"], 600))
    write("diagrams/git-branch-and-merge.svg",
          svg(W, H, "".join(b), "Git feature branch merged into main through a pull request", L["background"]))


def dart_sync_async():
    W, H = 1100, 500
    b = [heading(W, "Synchronous vs asynchronous", "Async code starts slow work, keeps going, and handles the result later.")]
    rows = [("Synchronous", 150), ("Asynchronous", 320)]
    for label, y in rows:
        b.append(text(40, y + 6, label, 18, weight=700))
    # sync: blocked while waiting
    b.append(f'<line x1="240" y1="150" x2="1040" y2="150" stroke="{L["border"]}" stroke-width="2"/>')
    b.append(node(240, 126, 150, 48, "step 1", kind="alt", title_size=16))
    b.append(node(400, 126, 380, 48, "wait for network…", kind="muted", title_size=16))
    b.append(node(790, 126, 120, 48, "step 2", kind="alt", title_size=16))
    b.append(text(590, 204, "Nothing else can run while it waits", 15, DG["highlight"], 600, "middle"))
    # async
    b.append(f'<line x1="240" y1="320" x2="1040" y2="320" stroke="{L["border"]}" stroke-width="2"/>')
    b.append(node(240, 296, 150, 48, "start fetch", kind="alt", title_size=16))
    b.append(node(400, 296, 150, 48, "step 2", kind="alt", title_size=16))
    b.append(node(560, 296, 150, 48, "handle tap", kind="alt", title_size=16))
    b.append(node(820, 296, 200, 48, "use result", kind="highlight", title_size=16))
    b.append(path_arrow("M315 346 C 420 430, 760 430, 900 350", DG["highlight"], dashed=True))
    b.append(text(610, 440, "Future completes later  →  code after await runs", 15, DG["highlight"], 600, "middle"))
    write("diagrams/01-dart/sync-vs-async.svg",
          svg(W, H, "".join(b), "Synchronous compared with asynchronous execution", L["background"]))


def dart_isolates():
    W, H = 1100, 480
    b = [heading(W, "Isolates", "Each isolate has its own memory. They share data only by sending messages.")]
    for x, title, sub in ((60, "Main isolate", "UI, events, short tasks"), (640, "Worker isolate", "heavy CPU work")):
        b.append(group(x, 120, 400, 300, title))
        b.append(node(x + 40, 180, 320, 64, "event loop", sub, "alt", mono=False))
        b.append(rect(x + 40, 290, 320, 90, L["background"], DG["node-stroke"], 2, 12, "6 5"))
        b.append(icon("storage", x + 60, 318, 32, DG["node-stroke"]))
        b.append(text(x + 108, 340, "own memory (heap)", 17, L["text"], 600))
    b.append(arrow(464, 220, 636, 220, DG["highlight"], label="send message: data", label_dy=-14))
    b.append(arrow(636, 270, 464, 270, DG["highlight"], label="send message: result", label_dy=30))
    b.append(text(550, 450, "No shared mutable state between isolates", 16, L["text-muted"], 600, "middle"))
    write("diagrams/01-dart/isolates.svg", svg(W, H, "".join(b), "Two Dart isolates exchanging messages", L["background"]))


def chip(x, y, label, color=None):
    """A small variable name tag."""
    color = color or DG["node-stroke"]
    w = 24 + len(label) * 11
    return (rect(x, y, w, 34, L["background"], color, 2, 17)
            + text(x + w / 2, y + 23, label, 16, color, 600, "middle", mono=True))


def dart_scope():
    W, H = 1100, 600
    b = [heading(W, "Scope follows the curly braces",
                 "Code inside can use variables from outside. Code outside cannot use variables from inside.")]
    b.append(group(40, 110, 1020, 460, "File (top level)"))
    b.append(chip(250, 122, "shopName"))
    b.append(group(80, 190, 440, 340, "printOpening() { }", code=True))
    b.append(chip(110, 240, "hours", DG["highlight"]))
    b.append(text(110, 320, "✓ can use shopName", 17, L["text"], 600))
    b.append(text(110, 352, "✓ can use hours", 17, L["text"], 600))
    b.append(group(560, 190, 460, 340, "main() { }", code=True))
    b.append(text(590, 250, "✓ can use shopName", 17, L["text"], 600))
    b.append(text(590, 282, "✗ cannot use hours", 17, DG["highlight"], 600))
    b.append(group(590, 320, 400, 180, "if (...) { }", code=True))
    b.append(chip(620, 366, "message", DG["highlight"]))
    b.append(text(620, 440, "✓ can use message and shopName", 16, L["text"], 600))
    write("diagrams/01-dart/scope.svg", svg(W, H, "".join(b), "Variable scope in a Dart file", L["background"]))


def dart_call_stack():
    W, H = 1100, 560
    b = [heading(W, "How factorial(4) runs",
                 "Each call waits for a smaller call. Results come back up after the base case.")]
    w, h = 300, 64
    calls = [("factorial(4)", "4 × factorial(3)", "24"), ("factorial(3)", "3 × factorial(2)", "6"),
             ("factorial(2)", "2 × factorial(1)", "2"), ("factorial(1)", "base case", "1")]
    for i, (name, sub, result) in enumerate(calls):
        x, y = 80 + i * 150, 120 + i * 100
        b.append(node(x, y, w, h, name, sub, "highlight" if i == 3 else "node", title_size=19))
        if i < 3:
            nx, ny = x + 150, y + 100
            b.append(arrow(x + 60, y + h + 2, nx + 40, ny - 4, DG["node-stroke"]))
            b.append(arrow(nx + w - 30, ny - 4, x + w - 30 + 20, y + h + 4, DG["highlight"]))
            b.append(text(nx + w + 2, ny - 12, f"returns {calls[i + 1][2]}", 16, DG["highlight"], 700))
    b.append(text(80 + w + 20, 160, "= 24", 26, DG["highlight"], 700))
    b.append(text(80, 528, "calls go down", 16, DG["node-stroke"], 700))
    b.append(text(240, 528, "results come back up", 16, DG["highlight"], 700))
    write("diagrams/01-dart/recursion-call-stack.svg",
          svg(W, H, "".join(b), "Call stack of factorial(4)", L["background"]))


def caption(w, y, s_):
    return text(w / 2, y, s_, 18, L["text-muted"], 600, "middle")


def dart_set_operations():
    W, H = 1100, 620
    blue, orange = DG["node-stroke"], DG["highlight"]
    b = [heading(W, "Set operations", "Morning sales and afternoon sales at Mina Coffee")]
    b.append(f'<circle cx="430" cy="320" r="190" fill="{blue}" fill-opacity="0.10" stroke="{blue}" stroke-width="3"/>')
    b.append(f'<circle cx="670" cy="320" r="190" fill="{orange}" fill-opacity="0.10" stroke="{orange}" stroke-width="3"/>')
    b.append(text(300, 120, "morning", 20, blue, 700, "middle", mono=True))
    b.append(text(800, 120, "afternoon", 20, orange, 700, "middle", mono=True))
    b.append(text(340, 325, "Mocha", 22, weight=600, anchor="middle"))
    b.append(text(550, 305, "Latte", 22, weight=600, anchor="middle"))
    b.append(text(550, 345, "Croissant", 22, weight=600, anchor="middle"))
    b.append(text(760, 325, "Iced tea", 22, weight=600, anchor="middle"))
    rows = [("morning.union(afternoon)", "everything in either circle"),
            ("morning.intersection(afternoon)", "only the middle"),
            ("morning.difference(afternoon)", "only the left part")]
    for i, (code, meaning) in enumerate(rows):
        y = 545 + i * 26
        b.append(text(190, y, code, 17, weight=600, mono=True))
        b.append(text(590, y, meaning, 17, L["text-muted"]))
    write("diagrams/01-dart/set-operations.svg", svg(W, H, "".join(b), "Union, intersection, and difference of two sets", L["background"]))


def member_box(x, y, w, title_, lines, kind="node", code=True, grey=None, dash=None):
    """A box with a title and a list of members."""
    h = 58 + 28 * len(lines) + (30 if grey else 0)
    fill, stroke = {"node": (DG["node-fill"], DG["node-stroke"]), "alt": (DG["node-alt-fill"], DG["node-stroke"]),
                    "highlight": (DG["highlight-fill"], DG["highlight"])}[kind]
    out = rect(x, y, w, h, fill, stroke, 2, 0, dash)
    out += text(x + w / 2, y + 34, title_, 20, weight=700, anchor="middle", mono=code)
    out += f'<line x1="{x}" y1="{y + 48}" x2="{x + w}" y2="{y + 48}" stroke="{stroke}" stroke-width="1.5"/>'
    for i, line in enumerate(lines):
        out += text(x + 18, y + 74 + 28 * i, line, 17, mono=True)
    if grey:
        out += text(x + 18, y + 74 + 28 * len(lines), grey, 14, L["text-muted"])
    return out


def dart_class_and_object():
    W, H = 1100, 560
    b = [heading(W, "A class and its objects", "The class is the plan. Objects are real things made from it.")]
    b.append(member_box(70, 210, 340, "class MenuItem", ["String name", "int price", "describe()"], "alt"))
    b.append(member_box(690, 120, 340, "object latte", ["name = 'Latte'", "price = 6000"]))
    b.append(member_box(690, 330, 340, "object mocha", ["name = 'Mocha'", "price = 6500"]))
    b.append(arrow(414, 270, 684, 180, DG["node-stroke"]))
    b.append(arrow(414, 320, 684, 390, DG["node-stroke"]))
    b.append(text(500, 172, "MenuItem(...) creates", 15, DG["node-stroke"], 600, "middle", mono=True))
    b.append(text(500, 412, "MenuItem(...) creates", 15, DG["node-stroke"], 600, "middle", mono=True))
    b.append(caption(W, 520, "One class, many objects. Each object has its own data."))
    write("diagrams/01-dart/class-and-object.svg", svg(W, H, "".join(b), "A class and two objects made from it", L["background"]))


def dart_inheritance():
    W, H = 1100, 720
    b = [heading(W, "Inheritance", "A subclass receives everything from its superclass and adds more.")]
    b.append(member_box(390, 105, 320, "Object", ["toString()"], "alt"))
    b.append(member_box(390, 260, 320, "MenuItem", ["name, price", "describe()"]))
    b.append(member_box(110, 460, 400, "Drink", ["size, addedPrice"], grey="inherits name, price, describe()"))
    b.append(member_box(590, 460, 400, "Pastry", ["isWarm"], grey="inherits name, price, describe()"))
    b.append(arrow(550, 256, 550, 196, DG["arrow"]))
    b.append(text(562, 232, "extends", 15, DG["arrow"], 600, mono=True))
    b.append(arrow(310, 456, 480, 378, DG["arrow"]))
    b.append(text(345, 415, "extends", 15, DG["arrow"], 600, "end", mono=True))
    b.append(arrow(790, 456, 620, 378, DG["arrow"]))
    b.append(text(755, 415, "extends", 15, DG["arrow"], 600, mono=True))
    b.append(text(W / 2, 640, "Arrows point from the subclass to its superclass.", 16, L["text-muted"], 400, "middle"))
    write("diagrams/01-dart/inheritance.svg", svg(W, H, "".join(b), "Drink and Pastry extend MenuItem, which extends Object", L["background"]))


def dart_mixins():
    W, H = 1100, 620
    b = [heading(W, "Mixins", "Unrelated classes can reuse the same members.")]
    b.append(member_box(200, 120, 320, "mixin Taxable", ["tax, priceWithTax"], "highlight", dash="8 6"))
    b.append(member_box(590, 120, 320, "mixin Logger", ["log()"], "highlight", dash="8 6"))
    for x, name in ((80, "MenuItem"), (420, "Order"), (760, "Customer")):
        b.append(node(x, 370, 260, 80, name))
    for x1, x2 in ((300, 210), (420, 550), (690, 550), (810, 890)):
        b.append(arrow(x1, 210, x2, 364, DG["highlight"]))
    for x, y in ((225, 290), (505, 262), (690, 262), (905, 290)):
        b.append(text(x, y, "with", 15, DG["highlight"], 600, "middle", mono=True))
    b.append(caption(W, 530, "The classes do not need a common parent."))
    write("diagrams/01-dart/mixins.svg", svg(W, H, "".join(b), "Taxable and Logger mixins used by MenuItem, Order, and Customer", L["background"]))


def dart_nullable_types():
    W, H = 1100, 640
    bad, good = DG["highlight"], CO["tip"]["accent"]
    b = [heading(W, "Nullable and non-nullable types", "The ? adds one more possible value: null.")]
    b.append(rect(50, 120, 400, 340, DG["node-fill"], DG["node-stroke"], 2, 0))
    b.append(text(250, 158, "String (non-nullable)", 20, weight=700, anchor="middle", mono=True))
    for i, v in enumerate(("'Latte'", "'Less ice'", "''")):
        b.append(chip(90, 190 + i * 56, v))
    b.append(chip(250, 530, "null", bad))
    b.append(text(250, 512, "✗ cannot go inside", 16, bad, 700, "middle"))
    b.append(rect(650, 120, 400, 340, DG["node-alt-fill"], DG["node-stroke"], 2, 0))
    b.append(text(850, 158, "String? (nullable)", 20, weight=700, anchor="middle", mono=True))
    for i, v in enumerate(("'Latte'", "'Less ice'", "''")):
        b.append(chip(690, 190 + i * 56, v))
    b.append(text(690, 372, "any String", 15, L["text-muted"], 600))
    b.append(chip(690, 395, "null", bad))
    b.append(arrow(456, 240, 644, 240, good))
    b.append(text(550, 196, "Allowed: a String", 15, good, 700, "middle"))
    b.append(text(550, 218, "fits in a String?", 15, good, 700, "middle"))
    b.append(arrow(644, 340, 456, 340, bad, dashed=True))
    b.append(text(550, 372, "Not allowed: it may", 15, bad, 700, "middle"))
    b.append(text(550, 394, "be null. Check it first.", 15, bad, 700, "middle"))
    write("diagrams/01-dart/nullable-types.svg", svg(W, H, "".join(b), "String and String? compared", L["background"]))


def dart_try_catch_flow():
    W, H = 1100, 640
    good, bad = CO["tip"]["accent"], DG["highlight"]
    b = [heading(W, "How try, catch, and finally run", "finally always runs, on all three paths.")]
    b.append(node(390, 110, 320, 76, "try", "the code that may fail", "alt"))
    b.append(text(170, 235, "No problem", 17, good, 700, "middle"))
    b.append(text(562, 225, "Caught", 17, DG["node-stroke"], 700))
    b.append(text(930, 235, "No matching catch", 17, bad, 700, "middle"))
    b.append(arrow(420, 190, 200, 370, good))
    b.append(arrow(550, 190, 550, 252, DG["node-stroke"]))
    b.append(arrow(680, 190, 900, 370, bad))
    b.append(node(390, 258, 320, 76, "catch", "handle the problem", "node"))
    b.append(node(70, 376, 960, 76, "finally", "always runs: close the cash drawer", "highlight"))
    b.append(arrow(550, 338, 550, 370, DG["node-stroke"]))
    b.append(arrow(200, 456, 200, 512, good))
    b.append(arrow(550, 456, 550, 512, DG["node-stroke"]))
    b.append(arrow(900, 456, 900, 512, bad))
    b.append(node(70, 518, 300, 70, "The next line runs", kind="muted", mono=False, title_size=18))
    b.append(node(400, 518, 300, 70, "The next line runs", kind="muted", mono=False, title_size=18))
    b.append(node(730, 518, 300, 70, "Goes on to the caller", kind="highlight", mono=False, title_size=18))
    write("diagrams/01-dart/try-catch-flow.svg", svg(W, H, "".join(b), "The three paths through try, catch, and finally", L["background"]))


def dart_record_vs_class():
    W, H = 1100, 600
    b = [heading(W, "Record or class?", "Both group values. A class can also have methods and private fields.")]
    b.append(text(260, 140, "Record", 22, DG["node-stroke"], 700, "middle"))
    b.append(rect(100, 170, 320, 80, DG["node-alt-fill"], DG["node-stroke"], 2, 0))
    b.append(f'<line x1="260" y1="170" x2="260" y2="250" stroke="{DG["node-stroke"]}" stroke-width="2"/>')
    b.append(text(180, 218, "'Latte'", 20, weight=600, anchor="middle", mono=True))
    b.append(text(340, 218, "6000", 20, weight=600, anchor="middle", mono=True))
    b.append(text(180, 278, "$1", 17, L["text-muted"], 700, "middle", mono=True))
    b.append(text(340, 278, "$2", 17, L["text-muted"], 700, "middle", mono=True))
    for i, note in enumerate(("No class needed", "Compared by value", "Cannot be changed")):
        b.append(text(110, 340 + i * 30, "• " + note, 17))
    b.append(text(800, 140, "Class", 22, DG["highlight"], 700, "middle"))
    b.append(member_box(580, 170, 210, "class MenuItem", ["name", "price", "describe()"], "highlight"))
    b.append(member_box(860, 170, 200, "an object", ["'Latte'", "6000"]))
    b.append(arrow(794, 230, 854, 230, DG["arrow"]))
    for i, note in enumerate(("Needs a class first", "Can have methods", "Can have private fields")):
        b.append(text(590, 400 + i * 30, "• " + note, 17))
    b.append(caption(W, 560, "Use a record for a quick group of values. Use a class for a real thing in your program."))
    write("diagrams/01-dart/record-vs-class.svg", svg(W, H, "".join(b), "A record compared with a class", L["background"]))


def dart_destructuring():
    W, H = 1100, 560
    b = [heading(W, "Destructuring", "A pattern takes a value apart and puts each part in a new variable.")]
    b.append(text(W / 2, 140, "var (name, cups) = bestSeller();", 22, DG["node-stroke"], 700, "middle", mono=True))
    b.append(rect(100, 190, 340, 70, DG["node-alt-fill"], DG["node-stroke"], 2, 0))
    b.append(text(270, 233, "('Iced latte', 42)", 20, weight=600, anchor="middle", mono=True))
    b.append(node(680, 170, 320, 56, "name = 'Iced latte'", title_size=18))
    b.append(node(680, 240, 320, 56, "cups = 42", title_size=18))
    b.append(arrow(444, 215, 674, 198, DG["highlight"]))
    b.append(arrow(444, 235, 674, 268, DG["highlight"]))
    b.append(text(W / 2, 360, "var (:subtotal, :tax) = totals;", 20, DG["node-stroke"], 700, "middle", mono=True))
    b.append(rect(100, 400, 340, 70, DG["node-alt-fill"], DG["node-stroke"], 2, 0))
    b.append(text(270, 443, "(subtotal: 8000, tax: 800)", 18, weight=600, anchor="middle", mono=True))
    b.append(node(680, 384, 320, 50, "subtotal = 8000", title_size=17))
    b.append(node(680, 446, 320, 50, "tax = 800", title_size=17))
    b.append(arrow(444, 425, 674, 409, DG["highlight"]))
    b.append(arrow(444, 445, 674, 471, DG["highlight"]))
    b.append(text(560, 520, ":subtotal is short for subtotal: subtotal", 16, L["text-muted"], 600, "middle", mono=True))
    write("diagrams/01-dart/destructuring.svg", svg(W, H, "".join(b), "Destructuring a positional record and a named record", L["background"]))


def dart_type_hierarchy():
    W, H = 1100, 700
    b = [heading(W, "How types are related", "An arrow points from a type to its supertype. A value fits any type above it.")]
    w, h = 170, 52
    pos = {"Object?": (465, 110), "Object": (300, 210), "Null": (720, 210),
           "num": (90, 320), "String": (300, 320), "MenuItem": (510, 320),
           "int": (20, 430), "double": (200, 430), "Drink": (510, 430), "Never": (465, 590)}
    up = [("Object", "Object?"), ("Null", "Object?"), ("num", "Object"), ("String", "Object"), ("MenuItem", "Object"),
          ("int", "num"), ("double", "num"), ("Drink", "MenuItem")]
    for child, parent in up:
        cx, cy = pos[child]
        px, py = pos[parent]
        b.append(arrow(cx + w / 2, cy - 2, px + w / 2, py + h + 4, DG["arrow"]))
    for t in ("int", "double", "String", "Drink", "Null"):
        x, y = pos[t]
        nx, ny = pos["Never"]
        b.append(f'<line x1="{nx + w / 2}" y1="{ny}" x2="{x + w / 2}" y2="{y + h}" stroke="{L["border"]}" stroke-width="1.5" stroke-dasharray="5 5"/>')
    for name, (x, y) in pos.items():
        kind = "alt" if name == "Object?" else ("highlight" if name == "Never" else "node")
        b.append(node(x, y, w, h, name, kind=kind, title_size=18))
    b.append(text(760, 450, "Never is below every type:", 16, L["text-muted"], 600))
    b.append(text(760, 474, "code of type Never never", 16, L["text-muted"]))
    b.append(text(760, 498, "gives a value at all.", 16, L["text-muted"]))
    write("diagrams/01-dart/type-hierarchy.svg", svg(W, H, "".join(b), "Type hierarchy from Object? down to Never", L["background"]))


def dart_future_stream_timeline():
    W, H = 1100, 560
    good, bad = DG["node-stroke"], DG["highlight"]
    b = [heading(W, "Future and Stream", "A Future gives one value later. A Stream gives many values over time, then it is done.")]
    for y, label in ((190, "Future<String>"), (390, "Stream<String>")):
        b.append(text(60, y - 62, label, 20, weight=700, mono=True))
        b.append(f'<line x1="80" y1="{y}" x2="1000" y2="{y}" stroke="{L["border"]}" stroke-width="3"/>')
        b.append(f'<circle cx="80" cy="{y}" r="9" fill="{L["background"]}" stroke="{good}" stroke-width="3"/>')
    b.append(arrow(990, 190, 1030, 190, L["text-muted"]))
    b.append(text(1030, 225, "time", 15, L["text-muted"], 600, "end"))
    b.append(text(80, 228, "brew('Latte') called", 15, L["text-muted"], 600))
    b.append(text(440, 175, "waiting...", 17, L["text-muted"], 600, "middle"))
    b.append(f'<circle cx="760" cy="190" r="14" fill="{good}"/>')
    b.append(text(760, 160, "'Latte is ready.'", 17, good, 700, "middle", mono=True))
    b.append(text(760, 228, "completes once", 15, L["text-muted"], 600, "middle"))
    b.append(text(80, 428, "listen", 15, L["text-muted"], 600))
    for x, v in ((260, "received"), (440, "preparing"), (620, "ready"), (800, "paid")):
        b.append(f'<circle cx="{x}" cy="390" r="14" fill="{good}"/>')
        b.append(text(x, 360, v, 17, good, 700, "middle", mono=True))
    b.append(rect(940, 360, 10, 60, bad, r=0))
    b.append(text(945, 448, "done", 17, bad, 700, "middle"))
    b.append(text(W / 2, 515, "Either one can also end with an error instead of a value.", 16, L["text-muted"], 400, "middle"))
    write("diagrams/01-dart/future-stream-timeline.svg", svg(W, H, "".join(b), "One Future value compared with many Stream values over time", L["background"]))


def dart_json_round_trip():
    W, H = 1180, 600
    good, back = DG["node-stroke"], DG["highlight"]
    b = [heading(W, "Saving and loading JSON", "Serialization turns an object into text. Deserialization builds it again.")]
    boxes = [("MenuItem object", ["name: 'Mocha'", "price: 6500"]), ("Map", ["{'name': 'Mocha',", " 'price': 6500}"]),
             ("JSON text", ['{"name":"Mocha",', ' "price":6500}'])]
    xs = [40, 330, 620]
    for x, (title_, lines) in zip(xs, boxes):
        b.append(member_box(x, 230, 230, title_, lines, "alt" if x == 40 else "node", code=False))
    b.append(rect(930, 245, 200, 110, L["surface"], L["border"], 2, 0))
    b.append(icon("description", 1005, 262, 48, L["text-muted"]))
    b.append(text(1030, 340, "menu.json", 18, weight=700, anchor="middle", mono=True))
    top = [("toJson()", 270, 330), ("jsonEncode", 560, 620), ("writeAsString", 850, 930)]
    bottom = [("fromJson()", 270, 330), ("jsonDecode", 560, 620), ("readAsString", 850, 930)]
    for label, x1, x2 in top:
        b.append(arrow(x1 + 4, 215, x2 - 4, 215, good))
        b.append(text((x1 + x2) / 2, 200, label, 15, good, 700, "middle", mono=True))
    for label, x1, x2 in bottom:
        b.append(arrow(x2 - 4, 395, x1 + 4, 395, back))
        b.append(text((x1 + x2) / 2, 425, label, 15, back, 700, "middle", mono=True))
    b.append(text(40, 150, "Serialization (save) →", 18, good, 700))
    b.append(text(W - 40, 490, "← Deserialization (load)", 18, back, 700, "end"))
    write("diagrams/01-dart/json-round-trip.svg", svg(W, H, "".join(b), "Saving an object as JSON and loading it again", L["background"]))


def dart_package_layout():
    W, H = 1100, 760
    b = [heading(W, "The mina_coffee project", "Your code goes in bin/ and lib/. pub writes the lock file and .dart_tool/.")]
    rows = [(0, "folder", "mina_coffee/", ""), (1, "folder", "bin/", ""), (2, "description", "practice.dart", ""),
            (1, "folder", "lib/", ""), (2, "description", "mina_coffee.dart", ""), (2, "folder", "src/", ""),
            (3, "description", "menu_item.dart", ""), (3, "description", "menu_store.dart", ""), (3, "description", "prices.dart", ""),
            (1, "folder", "data/", ""), (2, "description", "menu.json, orders.json, orders.txt", ""),
            (1, "folder", "output/", ""), (1, "folder", "test/", ""),
            (1, "description", "pubspec.yaml", "you edit"), (1, "description", "pubspec.lock", "pub writes"),
            (1, "folder", ".dart_tool/", "pub writes")]
    y0, step = 120, 38
    ys = {}
    for i, (depth, ic, name, tag) in enumerate(rows):
        y = y0 + i * step
        x = 60 + depth * 40
        grey = tag == "pub writes"
        color = L["text-muted"] if grey else L["text"]
        b.append(icon(ic, x, y - 4, 24, L["text-muted"] if grey else DG["node-stroke"]))
        b.append(text(x + 34, y + 15, name, 17, color, 600, mono=True))
        if tag:
            b.append(text(560, y + 15, tag, 15, DG["highlight"] if tag == "you edit" else L["text-muted"], 700))
        ys[name] = (x, y)
    px, py = ys["practice.dart"]
    mx, my = ys["mina_coffee.dart"]
    b.append(path_arrow(f"M{px + 190} {py + 10} C {px + 330} {py + 10}, {mx + 330} {my + 10}, {mx + 210} {my + 10}", DG["node-stroke"]))
    b.append(text(500, py + 52, "import 'package:mina_coffee/mina_coffee.dart'", 15, DG["node-stroke"], 600, mono=True))
    for name in ("menu_item.dart", "menu_store.dart", "prices.dart"):
        sx, sy = ys[name]
        b.append(path_arrow(f"M{mx + 225} {my + 18} C {mx + 320} {my + 40}, {sx + 300} {sy + 10}, {sx + 225} {sy + 10}", DG["highlight"]))
    b.append(text(470, my + 75, "export", 15, DG["highlight"], 700))
    write("diagrams/01-dart/package-layout.svg", svg(W, H, "".join(b), "Folders and files of the mina_coffee project", L["background"]))


def dart_semantic_versioning():
    W, H = 1100, 600
    good, bad = CO["tip"]["accent"], DG["highlight"]
    b = [heading(W, "Semantic versioning", "Each part of a version number tells you what kind of change it is.")]
    parts = [("1", "MAJOR", "breaking change", 400), ("9", "MINOR", "new feature", 550), ("1", "PATCH", "bug fix", 700)]
    for digit, name, meaning, x in parts:
        b.append(text(x, 210, digit, 64, weight=700, anchor="middle", mono=True))
        b.append(f'<line x1="{x - 40}" y1="235" x2="{x + 40}" y2="235" stroke="{DG["node-stroke"]}" stroke-width="3"/>')
        b.append(text(x, 265, name, 18, DG["node-stroke"], 700, "middle"))
        b.append(text(x, 290, meaning, 15, L["text-muted"], 600, "middle"))
    b.append(text(475, 210, ".", 64, weight=700, anchor="middle", mono=True))
    b.append(text(625, 210, ".", 64, weight=700, anchor="middle", mono=True))
    versions = [("1.8.0", 140), ("1.9.0", 320), ("1.9.1", 470), ("1.10.0", 640), ("2.0.0", 900)]
    b.append(f'<line x1="100" y1="430" x2="1000" y2="430" stroke="{L["border"]}" stroke-width="3"/>')
    b.append(rect(320, 418, 560, 24, good, r=0))
    for v, x in versions:
        color = bad if v == "2.0.0" else (L["text-muted"] if v == "1.8.0" else L["text"])
        b.append(f'<line x1="{x}" y1="410" x2="{x}" y2="450" stroke="{color}" stroke-width="2"/>')
        b.append(text(x, 480, v, 17, color, 700, "middle", mono=True))
    b.append(text(600, 400, "^1.9.0 allows these", 17, good, 700, "middle", mono=True))
    b.append(text(900, 395, "✗", 26, bad, 700, "middle"))
    b.append(text(900, 520, "not allowed:", 15, bad, 700, "middle"))
    b.append(text(900, 542, "may break your code", 15, bad, 700, "middle"))
    write("diagrams/01-dart/semantic-versioning.svg", svg(W, H, "".join(b), "Parts of a version number and what ^1.9.0 allows", L["background"]))


# ---------------------------------------------------------------- testing and design patterns (Dart 11-12)

def dart_debugging_steps():
    W, H = 1180, 460
    b = [heading(W, "Debugging, step by step", "The same five steps work for every bug.")]
    steps = [("bug_report", "Reproduce", "input that shows", "the bug every time"),
             ("search", "Narrow down", "print, breakpoints,", "stack traces"),
             ("lightbulb", "Understand", "why do the values", "go wrong here?"),
             ("build", "Fix", "change the code,", "run it again"),
             ("check_circle", "Keep it fixed", "write a test that", "catches the bug")]
    for i, (ic, title_, l1, l2) in enumerate(steps):
        x = 40 + i * 226
        kind = "highlight" if i == 4 else "node"
        fill, stroke = (DG["highlight-fill"], DG["highlight"]) if kind == "highlight" else (DG["node-fill"], DG["node-stroke"])
        b.append(rect(x, 140, 190, 210, fill, stroke, 2))
        b.append(icon(ic, x + 71, 160, 48, stroke))
        b.append(text(x + 95, 245, title_, 20, weight=700, anchor="middle"))
        b.append(text(x + 95, 285, l1, 15, L["text-muted"], anchor="middle"))
        b.append(text(x + 95, 307, l2, 15, L["text-muted"], anchor="middle"))
        if i < 4:
            b.append(arrow(x + 194, 245, x + 222, 245, DG["arrow"]))
    b.append(caption(W, 410, "The test in step 5 stops the same bug from coming back: a regression."))
    write("diagrams/01-dart/debugging-steps.svg", svg(W, H, "".join(b), "Five steps of debugging: reproduce, narrow down, understand, fix, keep it fixed", L["background"]))


def dart_test_double():
    W, H = 1100, 600
    real, fake = DG["node-stroke"], DG["highlight"]
    b = [heading(W, "Test doubles", "The same Checkout code. Only its dependency changes.")]
    b.append(group(40, 110, 1020, 200, "In the app"))
    b.append(member_box(80, 150, 260, "Checkout", ["payByCard()"], "alt"))
    b.append(member_box(420, 150, 300, "real CardTerminal", ["charge(riel)"]))
    b.append(arrow(344, 205, 414, 205, real, label="uses"))
    b.append(rect(820, 160, 200, 110, L["surface"], L["border"], 2))
    b.append(icon("public", 896, 172, 48, L["text-muted"]))
    b.append(text(920, 254, "the bank: real money", 15, L["text-muted"], 600, "middle"))
    b.append(arrow(724, 205, 814, 205, real))
    b.append(group(40, 340, 1020, 220, "In a test"))
    b.append(member_box(80, 380, 260, "Checkout", ["payByCard()"], "alt"))
    b.append(member_box(420, 380, 300, "FakeTerminal or mock", ["charge(riel) => false", "charged: [8800]"], "highlight"))
    b.append(arrow(344, 435, 414, 435, fake, label="uses"))
    b.append(text(760, 420, "No bank, no money.", 17, fake, 700))
    b.append(text(760, 448, "Fast, and the same", 16, L["text-muted"]))
    b.append(text(760, 472, "result every time.", 16, L["text-muted"]))
    write("diagrams/01-dart/test-double.svg", svg(W, H, "".join(b), "Checkout uses a real card terminal in the app and a fake one in a test", L["background"]))


def dart_singleton():
    W, H = 1100, 560
    hi = DG["highlight"]
    b = [heading(W, "Singleton", "One object, shared by every part of the program.")]
    callers = ["takeOrder('Latte')", "takeOrder('Mocha')", "takeOrder('Green tea')"]
    for i, c in enumerate(callers):
        y = 130 + i * 120
        b.append(node(60, y, 300, 70, c, mono=True, title_size=18))
        b.append(arrow(364, y + 35, 634, 270 + (i - 1) * 40, DG["node-stroke"]))
    b.append(text(500, 168, "TicketCounter.instance", 15, DG["node-stroke"], 600, "middle", mono=True))
    b.append(member_box(640, 190, 380, "TicketCounter", ["static instance", "_last = 3", "next()"], "highlight"))
    b.append(text(830, 390, "the only object", 16, hi, 700, "middle"))
    b.append(rect(640, 430, 380, 60, L["surface"], L["border"], 2, 0, "6 5"))
    b.append(text(660, 467, "TicketCounter()", 18, L["text-muted"], 600, mono=True))
    b.append(text(1000, 467, "✗ private", 17, hi, 700, "end"))
    b.append(caption(W, 530, "The constructor is private, so nobody can make a second counter."))
    write("diagrams/01-dart/singleton.svg", svg(W, H, "".join(b), "Three callers share one TicketCounter object", L["background"]))


def dart_factory():
    W, H = 1100, 520
    hi = DG["highlight"]
    b = [heading(W, "Factory", "One constructor decides which class to create.")]
    b.append(node(40, 150, 280, 80, "{'type': 'drink', ...}", mono=True, title_size=16))
    b.append(node(40, 300, 280, 80, "{'type': 'pastry', ...}", mono=True, title_size=16))
    b.append(member_box(400, 170, 320, "MenuItem.fromJson", ["switch (json['type'])"], "highlight"))
    b.append(arrow(324, 190, 394, 230, DG["arrow"]))
    b.append(arrow(324, 340, 394, 260, DG["arrow"]))
    b.append(member_box(820, 120, 240, "Drink", ["name, price"]))
    b.append(member_box(820, 300, 240, "Pastry", ["name, price", "isWarm"]))
    b.append(arrow(724, 220, 814, 170, hi))
    b.append(arrow(724, 250, 814, 340, hi))
    b.append(text(762, 232, "'drink'", 15, hi, 700, mono=True))
    b.append(text(752, 332, "'pastry'", 15, hi, 700, "end", mono=True))
    b.append(caption(W, 480, "The caller only asks for a MenuItem. It never names Drink or Pastry."))
    write("diagrams/01-dart/factory.svg", svg(W, H, "".join(b), "A factory constructor creates a Drink or a Pastry from JSON", L["background"]))


def dart_builder():
    W, H = 1100, 520
    hi = DG["highlight"]
    b = [heading(W, "Builder", "Collect the parts step by step. build() checks them and creates the object.")]
    b.append(member_box(60, 130, 380, "OrderBuilder('Dara')", ["..add('Latte')", "..size('L')", "..iced()", "..note('less ice')"], "alt"))
    b.append(arrow(444, 230, 634, 230, hi, label="build()", label_dy=-14))
    b.append(text(539, 262, "checks the parts", 15, hi, 600, "middle"))
    b.append(member_box(640, 130, 400, "Order", ["customer: 'Dara'", "items: [Latte]", "size: 'L', iced: true", "note: 'less ice'"]))
    b.append(rect(60, 380, 380, 60, L["surface"], L["border"], 2, 0, "6 5"))
    b.append(text(80, 417, "no items?", 17, L["text-muted"], 600, mono=True))
    b.append(text(420, 417, "StateError", 17, hi, 700, "end", mono=True))
    b.append(caption(W, 490, "The finished Order cannot change. Only the builder can create it."))
    write("diagrams/01-dart/builder.svg", svg(W, H, "".join(b), "An OrderBuilder collects parts and builds an Order", L["background"]))


def dart_repository():
    W, H = 1100, 600
    b = [heading(W, "Repository", "The program asks for data. It does not know where the data is kept.")]
    b.append(node(380, 110, 340, 70, "printPrice(menu, 'Mocha')", mono=True, title_size=17))
    b.append(arrow(550, 184, 550, 224, DG["arrow"], label="asks", label_dx=30, label_dy=8, label_anchor="start"))
    b.append(member_box(380, 230, 340, "MenuRepository", ["all()", "find(name)"], "alt"))
    b.append(text(734, 262, "abstract class", 15, L["text-muted"], 600))
    kinds = [("FileMenuRepository", "description", "data/menu.json", "node"),
             ("InMemoryMenuRepository", "view_list", "a list, for tests", "node"),
             ("ServerMenuRepository", "cloud", "later: a server", "muted")]
    for i, (name, ic, sub, kind) in enumerate(kinds):
        x = 40 + i * 350
        b.append(node(x, 420, 320, 110, "", kind=kind))
        b.append(icon(ic, x + 20, 438, 36, DG["node-stroke"] if kind == "node" else L["text-muted"]))
        b.append(text(x + 66, 466, name, 17, weight=700, mono=True))
        b.append(text(x + 66, 500, sub, 15, L["text-muted"]))
        b.append(arrow(x + 160, 416, 470 + i * 80, 348, DG["arrow"], dashed=kind == "muted"))
    b.append(text(W - 40, 570, "Arrows: each repository extends MenuRepository.", 15, L["text-muted"], 400, "end"))
    write("diagrams/01-dart/repository.svg", svg(W, H, "".join(b), "printPrice uses a MenuRepository, which can be a file, a list, or a server", L["background"]))


def dart_dependency_injection():
    W, H = 1100, 620
    hi = DG["highlight"]
    b = [heading(W, "Dependency injection", "An object gets what it needs from outside, through its constructor.")]
    b.append(group(40, 110, 460, 200, "main(): the composition root"))
    b.append(node(70, 160, 400, 60, "FileMenuRepository('data/menu.json')", mono=True, title_size=15))
    b.append(text(70, 270, "PriceService(menu)", 18, hi, 700, mono=True))
    b.append(group(40, 350, 460, 200, "a test"))
    b.append(node(70, 400, 400, 60, "InMemoryMenuRepository({'Latte': 1})", mono=True, title_size=15))
    b.append(text(70, 510, "PriceService(testMenu)", 18, hi, 700, mono=True))
    b.append(member_box(640, 240, 400, "PriceService", ["final MenuRepository menu", "totalFor(items)"], "alt"))
    b.append(arrow(474, 190, 634, 280, hi, label="injects", label_dy=-12))
    b.append(arrow(474, 430, 634, 330, hi, label="injects", label_dy=30))
    b.append(caption(W, 595, "PriceService never creates its own menu, so any menu can be given to it."))
    write("diagrams/01-dart/dependency-injection.svg", svg(W, H, "".join(b), "main and a test each inject a different menu into PriceService", L["background"]))


def dart_adapter():
    W, H = 1180, 500
    hi = DG["highlight"]
    b = [heading(W, "Adapter", "Make a class that you cannot change fit the interface that your code expects.")]
    b.append(member_box(40, 150, 240, "Checkout", ["payByCard()"], "alt"))
    b.append(arrow(284, 205, 354, 205, DG["arrow"], label="needs"))
    b.append(member_box(360, 150, 300, "CardTerminal", ["bool charge(int riel)"], "node", dash="6 5"))
    b.append(text(676, 200, "what our code expects", 15, L["text-muted"], 600))
    b.append(member_box(360, 300, 300, "BankCardAdapter", ["riel → cents", "0 → true"], "highlight"))
    b.append(arrow(510, 296, 510, 240, hi))
    b.append(text(522, 274, "implements", 15, hi, 700, mono=True))
    b.append(member_box(820, 300, 320, "BankCardReader", ["int pay(int cents)"]))
    b.append(text(980, 412, "the bank's class", 14, L["text-muted"], 600, "middle"))
    b.append(arrow(664, 350, 814, 350, hi, label="calls"))
    b.append(caption(W, 470, "Only the adapter knows about the bank. Checkout and the bank never change."))
    write("diagrams/01-dart/adapter.svg", svg(W, H, "".join(b), "BankCardAdapter implements CardTerminal and calls the bank's card reader", L["background"]))


def dart_observer():
    W, H = 1100, 560
    hi = DG["highlight"]
    b = [heading(W, "Observer", "When something changes, every listener is told.")]
    b.append(member_box(60, 170, 380, "OrderBoard", ["addListener(l)", "removeListener(l)", "update(1, ready)"], "alt"))
    b.append(text(250, 160, "keeps a list of listeners", 15, L["text-muted"], 600, "middle"))
    listeners = [("Kitchen", "person", "node"), ("Customer screen", "desktop_windows", "node"), ("Log", "description", "muted")]
    for i, (name, ic, kind) in enumerate(listeners):
        y = 130 + i * 130
        b.append(node(680, y, 360, 90, "", kind=kind))
        b.append(icon(ic, 700, y + 22, 44, DG["node-stroke"] if kind == "node" else L["text-muted"]))
        b.append(text(760, y + 54, name, 19, weight=700))
        b.append(arrow(444, 270, 674, y + 45, hi, dashed=kind == "muted"))
    b.append(text(250, 370, "update() calls every listener", 15, hi, 700, "middle"))
    b.append(text(860, 540, "A new listener can join at any time.", 15, L["text-muted"], 400, "middle"))
    write("diagrams/01-dart/observer.svg", svg(W, H, "".join(b), "The order board tells the kitchen, the screen, and a log about each change", L["background"]))


def dart_strategy():
    W, H = 1100, 600
    hi = DG["highlight"]
    b = [heading(W, "Strategy", "Each rule is its own class. The rule can be swapped while the program runs.")]
    b.append(member_box(40, 130, 340, "Checkout", ["PriceStrategy strategy", "receipt(10000)"], "alt"))
    b.append(member_box(560, 130, 380, "PriceStrategy", ["String label", "int apply(int riel)"], "node", dash="6 5"))
    b.append(arrow(384, 190, 554, 190, DG["arrow"], label="uses"))
    rules = [("RegularPrice", "11000 riel", "node"), ("MemberPrice", "8800 riel", "highlight"), ("HappyHourPrice", "9900 riel", "node")]
    for i, (name, result, kind) in enumerate(rules):
        x = 40 + i * 350
        b.append(member_box(x, 380, 320, name, ["apply(riel)"], kind))
        b.append(text(x + 160, 505, "receipt: " + result, 16, hi if kind == "highlight" else L["text-muted"], 700, "middle"))
        b.append(arrow(x + 160, 376, 690 + i * 60, 250, DG["arrow"]))
    b.append(text(1060, 320, "implements", 15, DG["arrow"], 600, "end", mono=True))
    b.append(caption(W, 570, "Swap the rule: checkout.strategy = MemberPrice(). A new rule is a new class."))
    write("diagrams/01-dart/strategy.svg", svg(W, H, "".join(b), "Checkout uses one of three price strategies", L["background"]))


# ---------------------------------------------------------------- projects (Dart 13)

def dart_project_steps():
    W, H = 1180, 470
    b = [heading(W, "How to build a project", "Small steps. Run the program after each one.")]
    steps = [("edit_note", "Goal", "one or two", "sentences"),
             ("view_list", "Features", "mark the ones", "for version 1"),
             ("data_object", "Data", "classes, records,", "lists, maps"),
             ("play_arrow", "Smallest version", "build it,", "and run it"),
             ("refresh", "Add a feature", "then run", "again"),
             ("check_circle", "Test and clean", "dart test,", "dart format")]
    for i, (ic, title_, l1, l2) in enumerate(steps):
        x = 40 + i * 188
        hi = i in (3, 4)
        fill, stroke = (DG["highlight-fill"], DG["highlight"]) if hi else (DG["node-fill"], DG["node-stroke"])
        b.append(rect(x, 140, 160, 200, fill, stroke, 2))
        b.append(icon(ic, x + 58, 158, 44, stroke))
        b.append(text(x + 80, 238, title_, 17, weight=700, anchor="middle"))
        b.append(text(x + 80, 276, l1, 14, L["text-muted"], anchor="middle"))
        b.append(text(x + 80, 298, l2, 14, L["text-muted"], anchor="middle"))
        if i < 5:
            b.append(arrow(x + 163, 240, x + 185, 240, DG["arrow"]))
    b.append(path_arrow("M 920 344 C 920 400, 830 400, 830 348", DG["highlight"]))
    b.append(text(875, 420, "repeat for each feature", 15, DG["highlight"], 700, "middle"))
    write("diagrams/01-dart/project-steps.svg", svg(W, H, "".join(b), "Six steps to build a project, repeating add a feature", L["background"]))


def dart_final_project():
    W, H = 1180, 640
    hi = DG["highlight"]
    b = [heading(W, "The Mina Coffee order system", "How the parts of the final project fit together.")]
    b.append(node(40, 120, 300, 90, "bin/mina_coffee.dart", "reads commands, composition root", mono=True, title_size=18))
    b.append(member_box(440, 110, 300, "Shop", ["placeOrder(...)", "report()", "save(path)"], "alt"))
    b.append(arrow(344, 165, 434, 165, DG["arrow"], label="calls"))
    b.append(member_box(40, 330, 300, "MenuRepository", ["FileMenuRepository"], dash="6 5"))
    b.append(text(350, 380, "repository", 15, hi, 700))
    b.append(rect(40, 480, 300, 70, L["surface"], L["border"], 2))
    b.append(icon("description", 60, 494, 40, L["text-muted"]))
    b.append(text(110, 522, "data/menu.json", 17, weight=700, mono=True))
    b.append(arrow(190, 420, 190, 476, DG["arrow"], dashed=True))
    b.append(arrow(190, 326, 480, 284, DG["arrow"], label="menu injected", label_dy=-12))
    b.append(member_box(440, 400, 300, "PriceStrategy", ["RegularPrice", "MemberPrice"], dash="6 5"))
    b.append(text(590, 550, "strategy", 15, hi, 700, "middle"))
    b.append(arrow(590, 396, 590, 284, DG["arrow"], label="uses", label_dx=12, label_dy=0, label_anchor="start"))
    b.append(text(990, 104, "LISTENERS (OBSERVER)", 13, L["text-muted"], 700, "middle"))
    for i, name in enumerate(["Kitchen", "Cashier"]):
        y = 120 + i * 100
        b.append(node(860, y, 260, 70, name, mono=False, title_size=19))
        b.append(arrow(744, 170, 854, y + 35, hi))
    b.append(rect(860, 400, 260, 70, L["surface"], L["border"], 2))
    b.append(icon("description", 878, 414, 40, L["text-muted"]))
    b.append(text(926, 442, "output/orders.json", 15, weight=700, mono=True))
    b.append(arrow(744, 240, 990, 396, DG["arrow"], dashed=True, label="save()", label_dx=40, label_dy=0, label_anchor="start"))
    b.append(text(990, 520, "test/ checks Shop with a fake menu", 15, L["text-muted"], 600, "middle"))
    b.append(caption(W, 610, "Each part has one job, so each part can be changed and tested on its own."))
    write("diagrams/01-dart/final-project.svg", svg(W, H, "".join(b), "The parts of the Mina Coffee order system and how they connect", L["background"]))


if __name__ == "__main__":
    code_panel()
    phone_placeholder()
    browser_frame()
    desktop_frame()
    callouts()
    widget_tree()
    layout_constraints()
    stateful_lifecycle()
    app_architecture()
    rest_flow()
    state_management()
    ci_cd()
    git_branches()
    dart_sync_async()
    dart_isolates()
    dart_scope()
    dart_call_stack()
    dart_set_operations()
    dart_class_and_object()
    dart_inheritance()
    dart_mixins()
    dart_nullable_types()
    dart_try_catch_flow()
    dart_record_vs_class()
    dart_destructuring()
    dart_type_hierarchy()
    dart_future_stream_timeline()
    dart_json_round_trip()
    dart_package_layout()
    dart_semantic_versioning()
    dart_debugging_steps()
    dart_test_double()
    dart_singleton()
    dart_factory()
    dart_builder()
    dart_repository()
    dart_dependency_injection()
    dart_adapter()
    dart_observer()
    dart_strategy()
    dart_project_steps()
    dart_final_project()
