"""Generate the TypeScript course's diagrams, in its navy and TypeScript-blue palette, into assets/diagrams/.

    python3 assets/build_typescript_diagrams.py

They are written to diagrams/08-typescript/.
"""
from diagram_kit import Kit

k = Kit(folder="08-typescript", primary="#235A97", tint="#E6F0FB", ink="#111A26", muted="#4F5D70", line="#CFDDF0",
        sans="'Instrument Sans', 'Helvetica Neue', Arial, sans-serif", mono="'Spline Sans Mono', Menlo, monospace", accent="#3178C6")
RED, RED_TINT, GREEN_TINT = "#B3261E", "#FCE8E6", "#E3F5EC"


def when_found():
    """The same mistake, found at two different times."""
    stages = [("Write", "you type the code"), ("Check", "the editor and tsc"), ("Run", "on your computer"), ("Customer", "Friday night, at the shop")]
    b = []
    for i, (name, sub) in enumerate(stages):
        x = 40 + i * 262
        b.append(k.node(x, 130, 222, 96, name, sub, k.tint if i == 1 else "#FFFFFF"))
        if i:
            b.append(k.arrow(x - 38, 178, x - 2, 178))
    b += [k.box(40 + 3 * 262, 270, 222, 70, RED_TINT, RED), k.text(40 + 3 * 262 + 111, 300, "JavaScript finds it here", 18, RED, 700),
          k.text(40 + 3 * 262 + 111, 325, "the total is 6000500", 16, RED),
          k.box(40 + 262, 270, 222, 70, GREEN_TINT, "#1B7A44"), k.text(40 + 262 + 111, 300, "TypeScript finds it here", 18, "#1B7A44", 700),
          k.text(40 + 262 + 111, 325, "a red line under the mistake", 16, "#1B7A44"),
          k.arrow(40 + 262 + 111, 268, 40 + 262 + 111, 230), k.arrow(40 + 3 * 262 + 111, 268, 40 + 3 * 262 + 111, 230),
          k.text(40, 400, "The earlier a mistake is found, the cheaper it is to fix: a red line in the editor costs seconds;", 19, k.ink, 700, "start"),
          k.text(40, 430, "a wrong total at the counter costs money, time, and a customer's trust.", 19, k.muted, 400, "start")]
    k.svg("when-mistakes-are-found", 1100, 470, "When is the mistake found?", "The same mistake, in JavaScript and in TypeScript", "".join(b))


def types_disappear():
    """Check, then remove the types: what runs is plain JavaScript."""
    b = [k.node(40, 140, 250, 110, "order.ts", "TypeScript: code + types", k.tint),
         k.node(345, 140, 250, 110, "Check", "tsc or the editor", "#FFFFFF"),
         k.node(650, 140, 250, 110, "Remove types", "tsc, Node.js, or a bundler", "#FFFFFF"),
         k.arrow(292, 195, 343, 195), k.arrow(597, 195, 648, 195),
         k.box(40, 300, 250, 120, "#FFFFFF", k.line), k.text(55, 335, "price: number", 19, k.primary, 600, "start", True),
         k.text(55, 365, "→ checked, then", 17, k.muted, 400, "start"), k.text(55, 395, "price", 19, k.ink, 600, "start", True),
         k.node(650, 300, 250, 120, "JavaScript", "runs in a browser, Node.js, or React Native", k.tint),
         k.arrow(775, 252, 775, 298),
         k.box(345, 300, 250, 120, RED_TINT, RED), k.text(470, 345, "A type error?", 19, RED, 700),
         k.text(470, 375, "You see it now,", 16, RED), k.text(470, 398, "before the code runs.", 16, RED),
         k.arrow(470, 252, 470, 298),
         k.text(40, 480, "Types exist only while you write and check the code. The program that runs has no types at all.", 19, k.ink, 700, "start")]
    k.svg("check-then-run", 1000, 520, "Check, then the types disappear", "What happens to TypeScript code before it runs", "".join(b))


def the_edge():
    """Types protect the code inside the program, not the data that comes in."""
    b = [k.box(330, 130, 440, 270, k.tint, k.primary), k.text(550, 170, "Your program", 22, k.primary, 700),
         k.text(550, 205, "TypeScript checks this code", 17, k.muted),
         k.node(370, 230, 360, 70, "total(price: number)", None, "#FFFFFF"),
         k.node(370, 315, 360, 60, "receipt(order: Order)", None, "#FFFFFF")]
    sources = [("Server", "JSON over the network", 140), ("Keyboard", "what a person types", 270), ("Files", "data saved earlier", 400)]
    for name, sub, y in sources:
        b += [k.node(40, y - 40, 220, 80, name, sub, "#FFFFFF"), k.arrow(262, y, 328, y)]
    b += [k.box(820, 190, 240, 150, RED_TINT, RED), k.text(940, 225, "Not checked", 20, RED, 700),
          k.text(940, 255, "Data from outside", 16, RED), k.text(940, 278, "can be anything:", 16, RED),
          k.text(940, 308, '"6000" instead of 6000', 16, RED, 600, mono=True),
          k.text(40, 470, "Types stop at the edge of your program. Data that comes in must be checked while the program runs.", 19, k.ink, 700, "start")]
    k.svg("types-stop-at-the-edge", 1100, 510, "Types stop at the edge", "What TypeScript can check, and what it cannot", "".join(b))


for make in (when_found, types_disappear, the_edge):
    make()
print("diagrams written")
