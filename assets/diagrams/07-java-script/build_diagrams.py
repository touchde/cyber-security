"""Draw the JavaScript book's diagrams (lessons 6 to 17) in its black and yellow palette.

    python3 assets/diagrams/07-java-script/build_diagrams.py

Uses the shared helpers in assets/diagram_kit.py. Lesson 1's two diagrams come from assets/build_javascript_diagrams.py.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from diagram_kit import Kit  # noqa: E402

k = Kit(folder="07-java-script", primary="#141414", tint="#FFF8C4", ink="#141414", muted="#5A5748", line="#E7DD9C",
        sans="'Space Grotesk', 'Helvetica Neue', Arial, sans-serif", mono="'Space Mono', Menlo, monospace", accent="#141414")
Y = k.tint


def label(x, y, s, size=19, weight=700, anchor="start", color=None, mono=False):
    return k.text(x, y, s, size, color or k.ink, weight, anchor, mono)


def scope_chain():
    b = [k.box(40, 110, 1020, 420, "#FFFFFF"), label(60, 145, "Global scope"), label(60, 178, "TAX_RATE = 0.1", 18, 400, mono=True),
         label(330, 178, "order()", 18, 400, mono=True),
         k.box(90, 205, 920, 300, Y), label(110, 240, "order's scope"), label(110, 273, "total = 6000", 18, 400, mono=True),
         label(330, 273, "line()", 18, 400, mono=True),
         k.box(140, 300, 460, 180, "#FFFFFF"), label(160, 335, "line's scope"), label(160, 368, 'name = "Latte"', 18, 400, mono=True),
         label(160, 410, "Looking for TAX_RATE:", 17, 400, color=k.muted), label(160, 438, "1. here? no   2. in order? no", 17, 400, color=k.muted),
         label(160, 462, "3. in global? yes", 17, 400, color=k.muted),
         k.arrow(700, 330, 700, 232), k.arrow(700, 222, 700, 132),
         label(720, 290, "step 2: search order", 17, 400, color=k.muted), label(720, 180, "step 3: search global", 17, 400, color=k.muted),
         label(640, 420, "The search goes outward only.", 18, 700), label(640, 448, "order cannot see name.", 17, 400, color=k.muted)]
    k.svg("scope-chain", 1100, 560, "The scope chain", "A name is searched for from the inside out", "".join(b))


def call_stack():
    b = []
    stacks = [("1. Start", ["global"]), ("2. printReceipt(1000)", ["global", "printReceipt"]),
              ("3. withTax(1000)", ["global", "printReceipt", "withTax"]), ("4. withTax returns", ["global", "printReceipt"]),
              ("5. printReceipt returns", ["global"])]
    for i, (title, frames) in enumerate(stacks):
        x = 40 + i * 212
        b.append(label(x + 90, 140, title, 16, 700, "middle"))
        for j, f in enumerate(frames):
            top = 430 - j * 80
            b.append(k.node(x, top, 180, 66, f, None, Y if j == len(frames) - 1 else "#FFFFFF"))
        if i:
            b.append(k.arrow(x - 30, 465, x - 4, 465))
    b.append(label(40, 545, "The box on top is the function running now. A call pushes a box; a return pops it.", 18, 400, color=k.muted))
    k.svg("call-stack", 1100, 580, "The call stack", "The stack while printReceipt calls withTax", "".join(b))


def closure():
    b = [k.node(40, 130, 330, 90, "makeCounter()", "has returned; its call is over", "#FFFFFF"),
         k.node(40, 280, 330, 90, "nextOrder", "a function", Y), k.node(40, 430, 330, 90, "nextTable", "a function", Y),
         k.node(640, 280, 300, 90, "count = 3", "kept for nextOrder", "#FFFFFF"),
         k.node(640, 430, 300, 90, "count = 1", "kept for nextTable", "#FFFFFF"),
         k.arrow(370, 325, 638, 325), k.arrow(370, 475, 638, 475),
         label(400, 310, "remembers", 17, 400, color=k.muted), label(400, 460, "remembers", 17, 400, color=k.muted),
         label(420, 175, "Each call to makeCounter made a new count.", 18, 400, color=k.muted),
         label(420, 200, "No other code can reach these boxes.", 18, 400, color=k.muted)]
    k.svg("closure", 1000, 560, "A closure", "A returned function keeps the variables it was created with", "".join(b))


def references():
    b = [k.node(40, 150, 220, 80, "first", "a variable", Y), k.node(40, 330, 220, 80, "second", "a variable", Y),
         k.node(560, 220, 380, 130, "{ price: 7000 }", "one object in memory"),
         k.arrow(260, 190, 558, 260), k.arrow(260, 370, 558, 310),
         label(40, 470, "const second = first; copies the arrow, not the object.", 18, 700),
         label(40, 500, "A change made through second is seen through first.", 18, 400, color=k.muted)]
    k.svg("references", 1000, 540, "Two names, one object", "Objects are shared by reference", "".join(b))


def prototype_chain():
    b = []
    items = [("latte", "name, price", Y), ("Drink.prototype", "describe()", "#FFFFFF"),
             ("Object.prototype", "toString(), hasOwnProperty()", "#FFFFFF"), ("null", "the end of the chain", "#FFFFFF")]
    for i, (t, s, fill) in enumerate(items):
        x = 40 + i * 265
        b.append(k.node(x, 160, 230, 110, t, s, fill))
        if i:
            b.append(k.arrow(x - 35, 215, x - 2, 215))
    b += [label(40, 330, "latte.describe(): not on latte, so JavaScript follows [[Prototype]] to Drink.prototype.", 18, 700),
          label(40, 360, "latte.toString(): two steps up, on Object.prototype. Reaching null means the property does not exist.", 18, 400, color=k.muted)]
    k.svg("prototype-chain", 1100, 400, "The prototype chain", "Each arrow is a [[Prototype]] link", "".join(b))


def event_loop():
    d = 40
    b = [k.box(40, 120 + d, 300, 400, "#FFFFFF"), label(190, 155 + d, "Call stack", 20, 700, "middle"),
         k.node(70, 420 + d, 240, 70, "main script", None, Y), k.node(70, 340 + d, 240, 70, "a callback", None, "#FFFFFF"),
         k.node(470, 130 + d, 300, 100, "Web APIs / Node.js", "timers, network, files"),
         k.node(470, 300 + d, 300, 100, "Microtask queue", "promise callbacks: first"),
         k.node(470, 440 + d, 300, 100, "Task queue", "timer callbacks: after"),
         k.node(850, 300 + d, 210, 100, "Event loop", "when the stack is empty"),
         k.arrow(340, 180 + d, 468, 180 + d), k.arrow(620, 230 + d, 620, 298 + d), k.arrow(770, 350 + d, 848, 350 + d),
         k.arrow(770, 490 + d, 955, 490 + d), k.arrow(955, 490 + d, 955, 402 + d),
         f'<path d="M470,{205 + d} L430,{205 + d} L430,{490 + d} L466,{490 + d}" fill="none" stroke="{k.muted}" stroke-width="2.5" marker-end="url(#head)"/>',
         f'<path d="M955,{300 + d} L955,110 L190,110 L190,{116 + d}" fill="none" stroke="{k.muted}" stroke-width="2.5" marker-end="url(#head)"/>',
         label(600, 132, "moves the next callback onto the stack", 16, 400, color=k.muted)]
    b += [label(40, 620, "1. Run the script. 2. Run every microtask. 3. Run one task. Repeat from 2.", 19, 700)]
    k.svg("event-loop", 1100, 650, "The event loop", "How waiting work gets back onto the call stack", "".join(b))


def promise_states():
    b = [k.node(60, 210, 260, 100, "pending", "the work is still running", Y),
         k.node(560, 120, 300, 100, "fulfilled", "has a value; then() runs"),
         k.node(560, 300, 300, 100, "rejected", "has an error; catch() runs"),
         k.arrow(320, 245, 558, 175), k.arrow(320, 275, 558, 345),
         label(330, 165, "resolve(value)", 17, 400, color=k.muted, mono=True), label(330, 385, "reject(error)", 17, 400, color=k.muted, mono=True),
         label(60, 460, "A promise settles once. After that its state and value never change.", 19, 700)]
    k.svg("promise-states", 920, 500, "The states of a promise", "Pending, then fulfilled or rejected", "".join(b))


def dom_tree():
    nodes = {"document": (420, 120), "html": (420, 220), "head": (220, 320), "body": (620, 320), "title": (220, 420),
             "h1": (470, 420), "ul#menu": (770, 420), "li Latte": (680, 520), "li Mocha": (880, 520)}
    w, h = 170, 60
    b = []
    edges = [("document", "html"), ("html", "head"), ("html", "body"), ("head", "title"), ("body", "h1"), ("body", "ul#menu"),
             ("ul#menu", "li Latte"), ("ul#menu", "li Mocha")]
    for a, c in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[c]
        b.append(f'<line x1="{x1 + w / 2}" y1="{y1 + h}" x2="{x2 + w / 2}" y2="{y2}" stroke="{k.muted}" stroke-width="2.5"/>')
    for n, (x, y) in nodes.items():
        b.append(k.node(x, y, w, h, n, None, Y if n.startswith("li") or n == "ul#menu" else "#FFFFFF"))
    b.append(label(40, 640, "Each box is a node. A line joins a parent (above) to its children (below).", 18, 400, color=k.muted))
    k.svg("dom-tree", 1100, 670, "The DOM tree of the menu page", "The browser turns HTML into a tree of objects", "".join(b))


def event_flow():
    b = [k.node(60, 130, 300, 80, "document", None, "#FFFFFF"), k.node(60, 260, 300, 80, "ul#menu", "a listener can catch it here", Y),
         k.node(60, 390, 300, 80, "button Latte", "the target: clicked", "#FFFFFF"),
         k.arrow(450, 170, 450, 428), k.arrow(620, 428, 620, 172),
         label(470, 300, "1. capture", 18, 700), label(640, 300, "2. bubble", 18, 700),
         label(400, 500, "The click travels down to the target, then bubbles back up.", 18, 400, color=k.muted),
         label(400, 528, "Event delegation puts one listener on ul#menu.", 18, 400, color=k.muted)]
    k.svg("event-flow", 900, 560, "How an event travels", "Capturing goes down; bubbling goes up", "".join(b))


for make in (scope_chain, call_stack, closure, references, prototype_chain, event_loop, promise_states, dom_tree, event_flow):
    make()
print("diagrams written")
