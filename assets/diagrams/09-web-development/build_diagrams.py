"""Draw the Web Development book's diagrams for lessons 2 to 34, in its aubergine and raspberry palette.

    python3 assets/diagrams/09-web-development/build_diagrams.py

Uses the shared helpers in assets/diagram_kit.py. Lesson 1's diagrams come from assets/build_web_diagrams.py.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from diagram_kit import Kit  # noqa: E402

k = Kit(folder="09-web-development", primary="#B0204F", tint="#FBE9F0", ink="#1C1426", muted="#5E5366", line="#EED3DD",
        sans="'Geist', 'Helvetica Neue', Arial, sans-serif", mono="'Geist Mono', Menlo, monospace", accent="#B0204F")
MINT = "#E2F7F2"


def label(x, y, s, size=18, weight=400, anchor="start", color=None):
    return k.text(x, y, s, size, color or k.muted, weight, anchor)


def pixel_pipeline():
    steps = [("Request", "DNS, TCP, TLS, HTTP"), ("Parse", "HTML to DOM, CSS to CSSOM"), ("Render tree", "visible nodes + styles"),
             ("Layout", "sizes and positions"), ("Paint", "pixels for each layer"), ("Composite", "layers into one frame")]
    body, bottom = k.steps(steps, 120, fills=(MINT, "#FFFFFF", "#FFFFFF", k.tint, k.tint, MINT))
    body += label(40, bottom + 45, "JavaScript and CSS changes can send the browser back to layout, paint, or only composite.", 18, 700, color=k.ink)
    k.svg("pixel-pipeline", 1100, bottom + 80, "From URL to pixels", "The steps a browser takes for every page", body)


def box_model():
    b = [k.box(80, 120, 640, 400, "#FFF4E5"), label(95, 148, "margin", 18, 700, color=k.ink),
         k.box(130, 165, 540, 310, "#333333", sw=0), label(145, 192, "border", 18, 700, color="#FFFFFF"),
         k.box(150, 205, 500, 250, MINT, sw=0), label(165, 232, "padding", 18, 700, color=k.ink),
         k.node(230, 260, 340, 130, "content", "width x height"),
         label(760, 200, "box-sizing: content-box", 18, 700, color=k.ink), label(760, 228, "width = content only"),
         label(760, 290, "box-sizing: border-box", 18, 700, color=k.ink), label(760, 318, "width = content + padding"),
         label(760, 342, "+ border")]
    k.svg("box-model", 1100, 560, "The CSS box model", "Every element is a box of four layers", "".join(b))


def cascade():
    steps = [("Origin and importance", "!important, author, browser"), ("Cascade layers", "@layer order"), ("Specificity", "id > class > element"),
             ("Order", "the later rule wins")]
    b = []
    for i, (t, s) in enumerate(steps):
        x = 40 + i * 265
        b.append(k.node(x, 140, 230, 110, f"{i + 1}. {t}", s, k.tint if i == 2 else "#FFFFFF"))
        if i:
            b.append(k.arrow(x - 35, 195, x - 2, 195))
    b.append(label(40, 310, "When two rules set the same property, the browser compares them in this order; the first difference decides.", 18, 700, color=k.ink))
    k.svg("cascade", 1100, 350, "How the cascade picks a winner", "Checked from left to right", "".join(b))


def flex_axes():
    b = [k.box(60, 130, 760, 200, "#FFFFFF")]
    for i, t in enumerate(["Latte", "Mocha", "Tea"]):
        b.append(k.node(90 + i * 230, 175, 200, 110, t, "flex item", MINT))
    b += [k.arrow(60, 370, 818, 370), label(440, 400, "main axis (flex-direction: row)", 18, 700, "middle", k.ink),
          k.arrow(860, 130, 860, 328), label(880, 235, "cross axis", 18, 700, color=k.ink),
          label(60, 450, "justify-content arranges items along the main axis; align-items, along the cross axis.", 18)]
    k.svg("flex-axes", 1100, 480, "Flexbox axes", "A flex container lays its items out in one direction", "".join(b))


def grid_lines():
    b = []
    for r in range(2):
        for c in range(3):
            b.append(k.node(100 + c * 220, 130 + r * 140, 200, 120, f"cell {r * 3 + c + 1}", None, MINT if (r, c) != (0, 0) else k.tint))
    for c in range(4):
        x = 90 + c * 220
        b.append(label(x, 420, f"line {c + 1}", 16, 700, "middle", k.ink))
    b += [label(780, 200, "grid-template-columns:", 17, 700, color=k.ink), label(780, 226, "repeat(3, 1fr)"),
          label(780, 290, "Lines are numbered from 1;", 17), label(780, 314, "items can span between lines.", 17)]
    k.svg("grid-lines", 1100, 450, "A grid with three columns", "Columns, rows, and the numbered lines between them", "".join(b))


for make in (pixel_pipeline, box_model, cascade, flex_axes, grid_lines):
    make()
print("diagrams written")
