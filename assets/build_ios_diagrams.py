"""Generate the iOS course's diagrams, in its plum and gold palette, into assets/diagrams/.

    python3 assets/build_ios_diagrams.py

They are written to diagrams/04-ios-development/.
"""
from diagram_kit import OUT, Kit

k = Kit(folder="04-ios-development", primary="#6B3483", tint="#F6EEF9", ink="#24152B", muted="#6A5B6E", line="#DCCDB6",
        sans="'Manrope', 'Helvetica Neue', Arial, sans-serif", mono="'DM Mono', Menlo, monospace", accent="#B4841F")
GOLD = "#FBF3DF"


def imperative_declarative():
    b = [k.text(60, 140, "Imperative: give orders, step by step", 22, k.primary, 700, "start"),
         k.node(60, 160, 290, 90, "1. Make a label", "UILabel()", "#FFFFFF"), k.node(400, 160, 290, 90, "2. Set its text", "Points: 120", "#FFFFFF"),
         k.node(740, 160, 300, 90, "3. Points change", "set the text again", "#FFFFFF"),
         k.arrow(350, 205, 398, 205), k.arrow(690, 205, 738, 205),
         k.text(60, 285, "You must remember to update every label, every time.", 18, k.muted, 400, "start"),
         k.text(60, 360, "Declarative: describe the screen for any data", 22, k.primary, 700, "start"),
         k.node(60, 380, 290, 100, "Data", "points = 120", GOLD, "#B4841F"),
         k.node(400, 380, 290, 100, "body", "Text(\"Points: \\(points)\")", k.tint),
         k.node(740, 380, 300, 100, "Screen", "Points: 120", "#FFFFFF"),
         k.arrow(350, 430, 398, 430), k.arrow(690, 430, 738, 430),
         f'<path d="M205,480 L205,525 L890,525 L890,484" fill="none" stroke="{k.muted}" stroke-width="2.5" marker-end="url(#head)"/>',
         k.text(548, 552, "When the data changes, SwiftUI runs body again and updates the screen.", 18, k.muted)]
    k.svg("imperative-declarative", 1100, 590, "Two ways to build a screen", "UIKit gives orders; SwiftUI describes the result", "".join(b))


def app_parts():
    b = [k.node(60, 130, 330, 100, "MinaMembersApp", "@main · the app starts here", GOLD, "#B4841F"),
         k.node(60, 280, 330, 100, "WindowGroup", "a scene: the app's window", k.tint),
         k.node(60, 430, 330, 100, "ContentView", "a view: what is on screen", "#FFFFFF"),
         k.arrow(225, 230, 225, 278), k.arrow(225, 380, 225, 428),
         k.box(470, 130, 570, 400, "#FFFFFF", k.line, 2),
         k.text(500, 175, "struct ContentView: View {", 19, k.ink, 400, "start", True),
         k.text(530, 215, "var body: some View {", 19, k.ink, 400, "start", True),
         k.text(560, 255, "VStack {", 19, k.primary, 700, "start", True),
         k.text(590, 295, "Image(...)", 19, k.ink, 400, "start", True),
         k.text(590, 335, "Text(\"Mina Coffee\")", 19, k.ink, 400, "start", True),
         k.text(560, 375, "}", 19, k.primary, 700, "start", True),
         k.text(530, 415, "}", 19, k.ink, 400, "start", True), k.text(500, 455, "}", 19, k.ink, 400, "start", True),
         k.text(500, 505, "body describes the screen", 18, k.muted, 400, "start"),
         k.arrow(392, 480, 468, 400)]
    k.svg("app-parts", 1100, 570, "The parts of a SwiftUI app", "An App, a scene, and a view", "".join(b))


for make in (imperative_declarative, app_parts):
    make()
print("diagrams written")
