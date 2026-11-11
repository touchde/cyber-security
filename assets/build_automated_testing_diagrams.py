"""Generate the Automated Testing course's diagrams, in its purple palette, into assets/diagrams/.

    python3 assets/build_automated_testing_diagrams.py

They are written to diagrams/12-automated-testing/.
"""
from diagram_kit import Kit

k = Kit(folder="12-automated-testing", primary="#5E3594", tint="#F5F0FC", ink="#1E1430", muted="#5E5470", line="#E1D8F0",
        sans="'Lexend', 'Helvetica Neue', Arial, sans-serif", mono="'Inconsolata', Menlo, monospace", accent="#1F8A4F")
GREEN = "#E7F7EE"


def pyramid():
    levels = [("End-to-end", "the whole app on a device", 300, "#FFFFFF"),
              ("Integration", "several parts together", 440, k.tint),
              ("UI component", "one screen or widget", 580, k.tint),
              ("Unit", "one function or class", 720, GREEN)]
    b = []
    for i, (name, sub, width, fill) in enumerate(levels):
        y = 120 + i * 108
        b.append(k.node(430 - width / 2, y, width, 96, name, sub, fill, "#1F8A4F" if fill == GREEN else None))
    b += [k.text(840, 165, "Fewer, slower,", 18, k.muted, 400, "start"), k.text(840, 190, "costly to keep", 18, k.muted, 400, "start"),
          k.text(840, 490, "Many, fast,", 18, "#1F8A4F", 700, "start"), k.text(840, 515, "cheap to keep", 18, "#1F8A4F", 700, "start"),
          k.arrow(820, 470, 820, 200)]
    k.svg("pyramid", 1100, 580, "The test pyramid", "Many small, fast tests at the bottom; a few big ones at the top", "".join(b))


def anatomy():
    parts = [("Arrange", "set up what the test needs", "prices = [6000, 4000]", k.tint),
             ("Act", "do the one thing being tested", "orderTotal(prices, member: true)", "#FFFFFF"),
             ("Assert", "check the result", "expect(..., 8800)", GREEN)]
    b = []
    for i, (name, sub, code, fill) in enumerate(parts):
        x = 40 + i * 355
        b += [k.node(x, 140, 320, 110, name, sub, fill, "#1F8A4F" if fill == GREEN else None), k.text(x + 160, 290, code, 18, k.ink, 400, "middle", True)]
        if i:
            b.append(k.arrow(x - 33, 195, x - 2, 195))
    b += [k.text(40, 370, "A test is a small program that checks another program.", 20, k.ink, 700, "start"),
          k.text(40, 402, "If the result is not what you expected, the test fails, and tells you what it got instead.", 18, k.muted, 400, "start")]
    k.svg("anatomy", 1100, 450, "What a test does", "Three steps: arrange, act, assert", "".join(b))


for make in (pyramid, anatomy):
    make()
print("wrote 2 diagrams")
