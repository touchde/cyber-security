"""Generate the JavaScript course's diagrams, in its black and yellow palette, into assets/diagrams/.

    python3 assets/build_javascript_diagrams.py

They are written to diagrams/07-java-script/.
"""
from diagram_kit import OUT, Kit

k = Kit(folder="07-java-script", primary="#141414", tint="#FFF8C4", ink="#141414", muted="#5A5748", line="#E7DD9C",
        sans="'Space Grotesk', 'Helvetica Neue', Arial, sans-serif", mono="'Space Mono', Menlo, monospace", accent="#141414")


def where_it_runs():
    b = [k.node(410, 120, 280, 100, "JavaScript code", ".js files", k.tint)]
    places = [("Web browsers", "Chrome, Safari, Firefox, Edge", 40), ("Servers", "Node.js, Deno, Bun", 300),
              ("Mobile apps", "React Native", 560), ("Desktop apps", "Electron, VS Code", 820)]
    for name, sub, x in places:
        b += [k.node(x, 300, 240, 100, name, sub, "#FFFFFF"), k.arrow(550, 220, x + 120, 298)]
    b += [k.text(550, 470, "The same language everywhere. Each place adds its own tools:", 20, k.ink, 700),
          k.text(550, 500, "the browser adds the web page (the DOM); Node.js adds files and the network.", 18, k.muted)]
    k.svg("where-it-runs", 1100, 540, "Where JavaScript runs", "One language, many homes", "".join(b))


def engine():
    steps = [("Your code", "welcome.js", k.tint), ("Engine", "V8, SpiderMonkey, JavaScriptCore", "#FFFFFF"),
             ("Machine code", "made while it runs", "#FFFFFF"), ("Result", "Welcome to Mina Coffee!", k.tint)]
    b = []
    for i, (name, sub, fill) in enumerate(steps):
        x = 40 + i * 265
        b.append(k.node(x, 150, 230, 110, name, sub, fill))
        if i:
            b.append(k.arrow(x - 35, 205, x - 2, 205))
    b += [k.text(40, 330, "No separate compile step: the engine reads your code, and turns the busy parts", 19, k.ink, 700, "start"),
          k.text(40, 360, "into fast machine code while the program runs (just-in-time compilation).", 19, k.muted, 400, "start"),
          k.text(40, 425, "Every engine follows the same rules: the ECMAScript standard, updated every June.", 19, k.ink, 700, "start")]
    k.svg("engine", 1100, 470, "How JavaScript runs", "An engine inside the browser or Node.js runs your code", "".join(b))


for make in (where_it_runs, engine):
    make()
print("diagrams written")
