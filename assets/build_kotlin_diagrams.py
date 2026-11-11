"""Generate the Kotlin course's diagrams, in its magenta and orange palette, into assets/diagrams/.

    python3 assets/build_kotlin_diagrams.py

They are written to diagrams/05-kotlin/.
"""
from diagram_kit import OUT, Kit

k = Kit(folder="05-kotlin", primary="#A61E6E", tint="#FCF1F6", ink="#1E1219", muted="#6B5462", line="#F0D6E3",
        sans="'Plus Jakarta Sans', 'Helvetica Neue', Arial, sans-serif", mono="'Red Hat Mono', Menlo, monospace", accent="#E8672A")
ORANGE = "#FFF1E6"


def where_it_runs():
    b = [k.node(430, 120, 240, 100, "Kotlin code", ".kt files", k.tint)]
    targets = [("Kotlin/JVM", "servers, desktop, tools", 40), ("Android", "phone and tablet apps", 300),
               ("Kotlin/Native", "iOS, Mac, Linux, Windows", 560), ("Kotlin/JS and Wasm", "web browsers", 820)]
    for name, sub, x in targets:
        b += [k.node(x, 300, 240, 100, name, sub, ORANGE if name in ("Kotlin/JVM", "Android") else "#FFFFFF", "#E8672A"),
              k.arrow(550, 220, x + 120, 298)]
    b += [k.box(40, 450, 1020, 80, k.tint, k.primary),
          k.text(550, 485, "Kotlin Multiplatform: share the same code between several of these targets", 20, k.ink, 700),
          k.text(550, 513, "for example, one set of price rules for the Android and iOS apps", 18, k.muted)]
    k.svg("where-it-runs", 1100, 570, "Where Kotlin runs", "One language, compiled for different machines", "".join(b))


def to_the_jvm():
    steps = [("Welcome.kt", "your source code", k.tint), ("kotlinc", "the Kotlin compiler", "#FFFFFF"),
             ("bytecode", ".class files in a .jar", ORANGE), ("JVM", "runs the bytecode", "#FFFFFF")]
    b = []
    for i, (name, sub, fill) in enumerate(steps):
        x = 40 + i * 265
        b.append(k.node(x, 150, 225, 110, name, sub, fill, "#E8672A" if fill == ORANGE else None))
        if i:
            b.append(k.arrow(x - 40, 205, x - 2, 205))
    b += [k.text(40, 330, "The JVM (Java Virtual Machine) is a program that runs bytecode on any computer that has it:", 19, k.ink, 700, "start"),
          k.text(40, 362, "macOS, Windows, or Linux. You install it with a JDK (Java Development Kit).", 19, k.muted, 400, "start"),
          k.text(40, 420, "In the terminal:", 19, k.primary, 700, "start"),
          k.text(40, 455, "kotlinc Welcome.kt -include-runtime -d welcome.jar", 19, k.ink, 400, "start", True),
          k.text(40, 488, "java -jar welcome.jar", 19, k.ink, 400, "start", True)]
    k.svg("to-the-jvm", 1100, 530, "From source code to a running program", "Kotlin on the JVM: compile once, run on any system with a JVM", "".join(b))


def nullable_types():
    b = [k.box(40, 120, 470, 230, "#FFFFFF", k.primary),
         k.text(275, 160, "String", 24, k.primary, 700, "middle", True),
         k.text(275, 192, "always holds text", 18, k.muted),
         k.node(90, 225, 170, 70, '"Latte"', None, k.tint),
         k.node(290, 225, 170, 70, '"less ice"', None, k.tint),
         k.box(590, 120, 470, 230, "#FFFFFF", "#E8672A"),
         k.text(825, 160, "String?", 24, "#E8672A", 700, "middle", True),
         k.text(825, 192, "text, or null: no value at all", 18, k.muted),
         k.node(620, 225, 130, 70, '"Latte"', None, k.tint),
         k.node(760, 225, 130, 70, '"less ice"', None, k.tint),
         k.node(900, 225, 130, 70, "null", None, ORANGE, "#E8672A")]
    tools = [("note?.length", "call only if not null;", "otherwise the result is null", 40),
             ('note ?: "no note"', "use a default", "when the value is null", 395),
             ("note!!.length", "promise it is not null;", "crashes if it is", 750)]
    for code, l1, l2, x in tools:
        b += [k.box(x, 400, 310, 130, "#FFFFFF" if x != 750 else ORANGE, k.line if x != 750 else "#E8672A"),
              k.text(x + 155, 440, code, 20, k.ink, 700, "middle", True),
              k.text(x + 155, 475, l1, 17, k.muted),
              k.text(x + 155, 500, l2, 17, k.muted)]
    k.svg("nullable-types", 1100, 570, "Nullable and non-null types",
          "A ? after the type lets the value be null; the compiler then asks you to handle it", "".join(b))


def classes_and_objects():
    b = [k.box(40, 205, 340, 280, k.tint, k.primary),
         k.text(210, 250, "class Drink", 24, k.primary, 700, "middle", True),
         k.text(210, 280, "the blueprint", 18, k.muted),
         k.text(80, 340, "name: String", 19, k.ink, 400, "start", True),
         k.text(80, 375, "price: Int", 19, k.ink, 400, "start", True),
         k.text(80, 410, "describe()", 19, k.ink, 400, "start", True),
         k.text(80, 455, "properties and functions", 16, k.muted, 400, "start")]
    objects = [("latte", '"Latte"', "6000", 200), ("mocha", '"Mocha"', "6500", 345), ("tea", '"Green tea"', "4500", 490)]
    for var, name, price, y in objects:
        b += [k.box(600, y - 60, 460, 120, "#FFFFFF" if var != "latte" else ORANGE, "#E8672A"),
              k.text(630, y - 20, f"val {var} = Drink({name}, {price})", 18, k.ink, 700, "start", True),
              k.text(630, y + 15, f"name = {name}", 17, k.muted, 400, "start", True),
              k.text(630, y + 42, f"price = {price}", 17, k.muted, 400, "start", True),
              k.arrow(382, 345, 596, y)]
    b += [k.text(550, 615, "One class, many objects: each object has its own values, and all share the same functions.", 19, k.ink, 700)]
    k.svg("classes-and-objects", 1100, 650, "Classes and objects",
          "A class describes what every drink has; each object is one real drink", "".join(b))


def collection_pipeline():
    stages = [("prices", "[6000, 6500,", "4500, 4000]", k.tint, None),
              ("filter { it >= 4500 }", "[6000, 6500,", "4500]", "#FFFFFF", None),
              ("map { it + it / 10 }", "[6600, 7150,", "4950]", "#FFFFFF", None),
              ("sum()", "18700", "", ORANGE, "#E8672A")]
    b = []
    for i, (code, l1, l2, fill, stroke) in enumerate(stages):
        x = 20 + i * 270
        b += [k.box(x, 170, 240, 170, fill, stroke or k.primary),
              k.text(x + 120, 215, code, 17 if i else 20, k.primary if i < 3 else "#E8672A", 700, "middle", True),
              k.text(x + 120, 270, l1, 18, k.ink, 400, "middle", True),
              k.text(x + 120, 300, l2, 18, k.ink, 400, "middle", True)]
        if i:
            b.append(k.arrow(x - 28, 255, x - 2, 255))
    notes = [("a list of 4", 140), ("keeps 3: drops 4000", 410), ("adds tax to each", 680), ("one number", 950)]
    for text, x in notes:
        b.append(k.text(x, 375, text, 17, k.muted))
    b += [k.text(550, 450, "prices.filter { it >= 4500 }.map { it + it / 10 }.sum()", 20, k.ink, 700, "middle", True),
          k.text(550, 490, "Each step makes a new list and hands it on; nothing changes the original prices.", 18, k.muted)]
    k.svg("collection-pipeline", 1100, 530, "A collection pipeline", "filter, then map, then sum: small steps, each with one job", "".join(b))


def suspend_resume():
    b = [k.text(40, 150, "one thread", 18, k.muted, 700, "start"),
         k.box(40, 165, 1020, 4, k.line, k.line, 0)]
    # time axis
    b += [k.text(40, 470, "time", 17, k.muted, 400, "start")]
    b.append(k.arrow(90, 465, 1060, 465))
    for i, t in enumerate(["0 s", "", "", "1 s"]):
        if t:
            b.append(k.text(110 + i * 290, 495, t, 16, k.muted))
    rows = [("milk", 210, k.tint), ("beans", 290, "#FFFFFF"), ("cups", 370, ORANGE)]
    for name, y, fill in rows:
        b.append(k.text(40, y + 32, name, 18, k.ink, 700, "start"))
    # runs: (row, x, w, label)
    runs = [(0, 120, 150, "ask"), (1, 280, 150, "ask"), (2, 440, 150, "ask"),
            (0, 600, 140, "answer"), (1, 750, 140, "answer"), (2, 900, 140, "answer")]
    for r, x, w, label in runs:
        name, y, fill = rows[r]
        b += [k.box(x, y, w, 50, fill, k.primary if fill != ORANGE else "#E8672A"), k.text(x + w / 2, y + 32, label, 17, k.ink, 700)]
    for r, x1, x2 in [(0, 270, 600), (1, 430, 750), (2, 590, 900)]:
        name, y, fill = rows[r]
        b += [k.box(x1, y + 22, x2 - x1, 6, k.line, k.line, 0), k.text((x1 + x2) / 2, y + 14, "suspended", 15, k.muted)]
    b += [k.text(550, 545, "delay(1000) suspends: the coroutine waits without holding the thread,", 18, k.ink, 700),
          k.text(550, 575, "so the thread runs the other coroutines. Each resumes when its answer is due.", 18, k.muted)]
    k.svg("suspend-resume", 1100, 600, "A coroutine suspends and resumes",
          "Three questions on one thread: the waits overlap, so all three finish in about one second", "".join(b))


def flow_pipeline():
    stages = [("producer", "flow { emit(sale) }", "the till emits sales", k.tint, k.primary),
              ("operators", "filter, map, runningFold", "each value passes through", "#FFFFFF", k.primary),
              ("collector", "collect { ... }", "the screen shows each one", ORANGE, "#E8672A")]
    b = []
    for i, (title, code, sub, fill, stroke) in enumerate(stages):
        x = 40 + i * 360
        b += [k.box(x, 150, 300, 150, fill, stroke),
              k.text(x + 150, 195, title, 22, k.primary if i < 2 else "#E8672A", 700),
              k.text(x + 150, 235, code, 17, k.ink, 700, "middle", True),
              k.text(x + 150, 270, sub, 16, k.muted)]
        if i:
            b.append(k.arrow(x - 58, 225, x - 2, 225))
    values = ["6600", "4400", "7150"]
    b.append(k.arrow(100, 362, 1040, 362))
    for j, v in enumerate(values):
        b += [k.box(150 + j * 300, 340, 110, 44, "#FFFFFF", k.primary), k.text(205 + j * 300, 369, v, 17, k.ink, 400, "middle", True)]
    b += [k.text(550, 430, "Cold: nothing runs until a collector calls collect.", 19, k.ink, 700),
          k.text(550, 462, "Values arrive one at a time, when they are ready; emit waits while the collector is busy.", 18, k.muted)]
    k.svg("flow-pipeline", 1100, 500, "A Flow from producer to collector",
          "Values over time, not all at once like a list", "".join(b))


def kmp_shared():
    b = [k.box(210, 140, 680, 120, k.tint, k.primary),
         k.text(550, 182, "commonMain", 24, k.primary, 700, "middle", True),
         k.text(550, 215, "finalPrice, receiptTotal, expect fun platformName()", 17, k.ink, 400, "middle", True),
         k.text(550, 243, "Kotlin + the standard library + multiplatform libraries", 16, k.muted)]
    targets = [("jvmMain", "actual: \"the JVM\"", "Android, servers, desktop", 40, ORANGE, "#E8672A"),
               ("jsMain", "actual: \"JavaScript\"", "web browsers, Node.js", 400, ORANGE, "#E8672A"),
               ("iosMain", "actual: an iPhone's name", "iPhone and iPad (built on a Mac)", 760, "#FFFFFF", k.line)]
    for name, code, runs, x, fill, stroke in targets:
        b += [k.arrow(550, 262, x + 150, 338),
              k.box(x, 340, 300, 130, fill, stroke),
              k.text(x + 150, 380, name, 22, k.ink, 700, "middle", True),
              k.text(x + 150, 413, code, 16, k.ink, 400, "middle", True),
              k.text(x + 150, 444, runs, 16, k.muted)]
    b += [k.text(550, 520, "The shared code is written once; each target adds only what differs.", 19, k.ink, 700)]
    k.svg("kmp-shared", 1100, 560, "Shared code in Kotlin Multiplatform",
          "One module, compiled for several platforms", "".join(b))


for make in (where_it_runs, to_the_jvm, nullable_types, classes_and_objects, collection_pipeline, suspend_resume, flow_pipeline, kmp_shared):
    make()
print("diagrams written")
