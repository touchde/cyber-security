"""Generate the Accessibility and Localization course's diagrams, in its high-contrast palette, into assets/diagrams/.

    python3 assets/build_accessibility_localization_diagrams.py

They are written to diagrams/19-accessibility-localization/.
"""
from diagram_kit import Kit

k = Kit(folder="19-accessibility-localization", primary="#1A4FD6", tint="#EEF3FF", ink="#111111", muted="#3D4350", line="#C9D6F5",
        sans="'Atkinson Hyperlegible Next', 'Helvetica Neue', Arial, sans-serif", mono="'Atkinson Hyperlegible Mono', Menlo, monospace", accent="#1A4FD6")


def contrast():
    samples = [("#C8A27A", "Light brown on cream", "2.2 to 1", False), ("#5D3A1A", "Dark brown on cream", "9.5 to 1", True),
               ("#000000", "Black on white", "21 to 1", True)]
    b = []
    for i, (color, name, ratio, ok) in enumerate(samples):
        x = 40 + i * 345
        bg = "#FFF8EC" if i < 2 else "#FFFFFF"
        b += [k.box(x, 140, 320, 170, bg, "#111111", 2), k.text(x + 160, 215, "Iced latte", 34, color, 700), k.text(x + 160, 265, "6000 riel", 24, color, 400),
              k.text(x + 160, 345, name, 18, k.ink, 700), k.text(x + 160, 375, ratio, 22, k.ink, 700),
              k.text(x + 160, 405, "passes (4.5 to 1 or more)" if ok else "fails: too faint", 18, k.primary if ok else "#B00020", 700)]
    b.append(k.text(40, 470, "WCAG asks for at least 4.5 to 1 for normal text, and 3 to 1 for large text.", 19, k.ink, 700, "start"))
    k.svg("contrast", 1100, 510, "Contrast you can measure", "The same text in three colors, with its contrast ratio", "".join(b))


def text_out_of_code():
    b = [k.node(40, 150, 300, 110, "Code", "message('km', 'welcome')", "#FFFFFF"),
         k.node(420, 120, 300, 80, "English messages", "welcome → Welcome to...", k.tint),
         k.node(420, 220, 300, 80, "Khmer messages", "welcome → សូមស្វាគមន៍...", k.tint),
         k.node(800, 150, 260, 110, "Screen", "the right language", "#FFFFFF"),
         k.arrow(340, 205, 418, 160), k.arrow(340, 205, 418, 260), k.arrow(720, 205, 798, 205),
         k.text(40, 360, "The code asks for a key. The message table for the user's language gives the words.", 19, k.ink, 700, "start"),
         k.text(40, 392, "A missing Khmer message falls back to English, instead of showing nothing.", 18, k.muted, 400, "start"),
         k.text(40, 424, "Translators edit the tables, never the code.", 18, k.muted, 400, "start")]
    k.svg("text-out-of-code", 1100, 460, "Text kept out of the code", "One key, a message in each language", "".join(b))


for make in (contrast, text_out_of_code):
    make()
print("wrote 2 diagrams")
