"""Generate the Flutter course's diagrams, in its indigo palette, into assets/diagrams/.

    python3 assets/build_flutter_diagrams.py

They are written to diagrams/02-flutter/.
"""
from diagram_kit import OUT, Kit

k = Kit(folder="02-flutter", primary="#4B3FCF", tint="#F2F0FE", ink="#1A1830", muted="#5D5A78", line="#CFCBEF",
        sans="'Figtree', 'Helvetica Neue', Arial, sans-serif", mono="'Fira Code', Menlo, monospace", accent="#0A8FC7")
SKY = "#E3F5FD"


def layers():
    rows = [("Your app", "the Mina Coffee code, in Dart", "#FFFFFF", k.primary),
            ("Framework", "widgets, Material, layout, and painting, in Dart", k.tint, k.primary),
            ("Engine", "draws every pixel, runs Dart; written in C++", SKY, "#0A8FC7"),
            ("Embedder", "the window, touch, and keyboard of each system", "#FFFFFF", k.muted)]
    b = []
    for i, (title, sub, fill, stroke) in enumerate(rows):
        y = 120 + i * 105
        b += [k.box(80, y, 640, 88, fill, stroke), k.text(110, y + 40, title, 24, k.ink, 700, "start"), k.text(110, y + 68, sub, 18, k.muted, 400, "start")]
    b += [k.text(770, 165, "You write this", 18, k.primary, 700, "start"), k.text(770, 190, "every day", 18, k.muted, 400, "start"),
          k.text(770, 270, "Open source, in Dart:", 18, k.primary, 700, "start"), k.text(770, 295, "you can read all of it", 18, k.muted, 400, "start"),
          k.text(770, 375, "Comes with Flutter", 18, "#0A8FC7", 700, "start"), k.text(770, 400, "inside every app", 18, k.muted, 400, "start"),
          k.text(770, 480, "One for each system:", 18, k.ink, 700, "start"), k.text(770, 505, "Android, iOS, web, desktop", 18, k.muted, 400, "start"),
          k.text(400, 572, "The screen is a canvas. Flutter paints the buttons and text itself.", 19, k.ink, 700)]
    k.svg("layers", 1100, 600, "How Flutter is built", "Four layers, from the code you write down to the device", "".join(b))


def one_codebase():
    b = [k.node(60, 230, 230, 120, "lib/main.dart", "one Dart codebase", k.tint),
         k.node(390, 230, 230, 120, "flutter build", "one command per target", "#FFFFFF")]
    b += [k.arrow(290, 290, 388, 290)]
    targets = [("Android", "APK or app bundle"), ("iOS", "an app for the App Store"), ("Web", "HTML and JavaScript"),
               ("macOS, Windows, Linux", "a desktop app")]
    for i, (name, sub) in enumerate(targets):
        y = 120 + i * 105
        b += [k.node(720, y, 330, 85, name, sub, SKY if i % 2 == 0 else "#FFFFFF", "#0A8FC7"), k.arrow(620, 290, 718, y + 42)]
    b += [k.text(60, 470, "The same widgets on every target,", 19, k.ink, 700, "start"),
          k.text(60, 498, "so the app looks the same everywhere.", 19, k.muted, 400, "start")]
    k.svg("one-codebase", 1100, 560, "One codebase, many platforms", "The same Dart code becomes an app for each system", "".join(b))


def first_tree():
    nodes = [("MinaCoffeeApp", 400, 120), ("MaterialApp", 400, 215), ("Scaffold", 400, 310), ("AppBar", 220, 410),
             ("Center", 580, 410), ("Text: Mina Coffee", 220, 505), ("Text: Today's special", 580, 505)]
    b = []
    edges = [(0, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6)]
    for a, c in edges:
        b.append(f'<line x1="{nodes[a][1] + 130}" y1="{nodes[a][2] + 60}" x2="{nodes[c][1] + 130}" y2="{nodes[c][2]}" stroke="{k.muted}" stroke-width="2.5"/>')
    for i, (name, x, y) in enumerate(nodes):
        b.append(k.node(x, y, 260, 60, name, None, k.tint if i == 0 else ("#FFFFFF" if i < 5 else SKY), "#0A8FC7" if i >= 5 else None))
    b += [k.text(900, 260, "Widgets inside", 19, k.primary, 700, "start"), k.text(900, 286, "widgets: a tree.", 19, k.muted, 400, "start"),
          k.text(900, 345, "The leaves are what", 19, k.primary, 700, "start"), k.text(900, 371, "you see on screen.", 19, k.muted, 400, "start")]
    k.svg("first-tree", 1100, 600, "The widget tree of the first screen", "Each widget holds the widgets below it", "".join(b))


for make in (layers, one_codebase, first_tree):
    make()
print("wrote 3 diagrams")
