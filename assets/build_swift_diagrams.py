"""Generate the Swift course's diagrams, in its red-orange palette, into assets/diagrams/.

    python3 assets/build_swift_diagrams.py

They are written to diagrams/03-swift/.
"""
from diagram_kit import Kit

k = Kit(folder="03-swift", primary="#C2391F", tint="#FDF3EF", ink="#1D1A24", muted="#5F5A69", line="#EBDDD3",
        sans="'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif", mono="'IBM Plex Mono', Menlo, monospace")
SAND = "#FBF5F1"


def captured_values():
    """Lesson 4: two counters from makeTicketCounter(), each closure with its own captured lastTicket."""
    b = [k.text(40, 140, "Constant", 17, k.muted, 700, "start"),
         k.text(320, 140, "Closure", 17, k.muted, 700, "start"),
         k.text(700, 140, "Captured variable", 17, k.muted, 700, "start")]
    rows = [("counter", "lastTicket", "now 4, after four calls", 160), ("tomorrow", "lastTicket", "now 1, after one call", 300)]
    for name, var, value, y in rows:
        b += [k.node(40, y, 220, 100, name, "let", SAND),
              k.arrow(262, y + 50, 318, y + 50),
              k.node(320, y, 320, 100, "{ lastTicket += 1 }", "returns the next ticket"),
              k.arrow(642, y + 50, 698, y + 50),
              k.node(700, y, 360, 100, var, value, k.tint)]
    b += [k.text(40, 460, "Each call of makeTicketCounter() makes a new lastTicket, starting at 0.", 19, k.ink, 700, "start"),
          k.text(40, 492, "The closure holds on to that variable after the function has returned,", 19, k.muted, 400, "start"),
          k.text(40, 520, "so the two counters never share a number.", 19, k.muted, 400, "start")]
    k.svg("captured-values", 1100, 560, "A closure captures a variable", "Two ticket counters, each with its own lastTicket", "".join(b))


def optional_box():
    """Lesson 5: an optional is a box that holds a value or nothing, and the five ways to open it."""
    b = []
    for i, (call, inside, sub, fill) in enumerate([('Int("6000")', "6000", "the box holds a value", k.tint),
                                                   ('Int("six thousand")', "nil", "the box is empty", "#FFFFFF")]):
        x = 40 + i * 530
        b += [k.text(x, 145, call, 19, k.ink, 400, "start", True),
              k.text(x + 490, 145, "gives an Int?", 17, k.muted, 400, "end"),
              k.node(x, 160, 490, 100, inside, sub, fill)]
    b.append(k.text(40, 320, "Five ways to open the box", 20, k.ink, 700, "start"))
    tools = [("if let", "use it, if there"), ("guard let", "leave early if nil"), ("??", "use a default"),
             ("?.", "go on only if there"), ("!", "crash if nil")]
    for i, (name, sub) in enumerate(tools):
        b.append(k.node(40 + i * 206, 340, 190, 100, name, sub, SAND if name != "!" else "#FFFFFF",
                        "#9A2A16" if name == "!" else None))
    b.append(k.text(40, 490, "Swift never lets you use an Int? as an Int until you have opened it.", 19, k.muted, 400, "start"))
    k.svg("optional-box", 1100, 530, "An optional is a box", "It holds one value, or nothing (nil)", "".join(b))


def three_collections():
    """Lesson 6: an array, a set, and a dictionary, side by side."""
    b = []
    panels = [("Array", "[String]", "in order; repeats allowed", 40),
              ("Set", "Set<String>", "no order; each value once", 395),
              ("Dictionary", "[String: Int]", "find a value by its key", 750)]
    for name, typ, rule, x in panels:
        b += [k.text(x, 140, name, 22, k.ink, 700, "start"),
              k.text(x + 310, 140, typ, 17, k.muted, 400, "end", True),
              k.box(x, 155, 310, 250, SAND, k.line),
              k.text(x + 155, 440, rule, 18, k.muted)]
    for i, item in enumerate(["Latte", "Mocha", "Latte"]):
        y = 180 + i * 72
        b += [k.box(60, y, 50, 56, k.tint), k.text(85, y + 35, str(i), 20, k.primary, 700, mono=True),
              k.node(110, y, 220, 56, item)]
    for item, (x, y) in [("Dara", (420, 185)), ("Sokha", (550, 255)), ("Chenda", (430, 325))]:
        b.append(k.node(x, y, 130, 56, item))
    for i, (key, value) in enumerate([("Latte", "6000"), ("Mocha", "6500"), ("Iced tea", "4000")]):
        y = 180 + i * 72
        b += [k.node(770, y, 130, 56, key, fill=k.tint), k.arrow(902, y + 28, 938, y + 28), k.node(940, y, 100, 56, value)]
    k.svg("three-collections", 1100, 480, "Three kinds of collection", "Choose by how you need to find things", "".join(b))


def value_and_reference():
    """Lesson 7: a struct is copied on assignment; a class instance is shared by two names."""
    b = [k.text(40, 140, "Struct: a value", 22, k.ink, 700, "start"),
         k.text(590, 140, "Class: a reference", 22, k.ink, 700, "start")]
    for i, (name, price) in enumerate([("latte", "price: 6000"), ("copy", "price: 9999")]):
        y = 165 + i * 130
        b += [k.node(40, y, 160, 90, name, "let" if i == 0 else "var", SAND),
              k.arrow(202, y + 45, 268, y + 45),
              k.node(270, y, 250, 90, "DrinkCard", price, k.tint)]
    for i, name in enumerate(["dara", "sameDara"]):
        y = 165 + i * 130
        b += [k.node(590, y, 170, 90, name, "let", SAND), k.arrow(762, y + 45, 868, 255 + (i * 2 - 1) * 22)]
    b.append(k.node(870, 210, 190, 90, "CustomerCard", "visits: 4", k.tint))
    b += [k.text(40, 430, "Two separate values. Changing the copy", 18, k.muted, 400, "start"),
          k.text(40, 456, "leaves the original as it was.", 18, k.muted, 400, "start"),
          k.text(590, 430, "Two names for one instance. A change", 18, k.muted, 400, "start"),
          k.text(590, 456, "through either name is seen by both.", 18, k.muted, 400, "start")]
    k.svg("value-and-reference", 1100, 500, "Value types and reference types", "What happens when you assign one to another name", "".join(b))


def some_and_any():
    """Lesson 9: some is one fixed hidden type; any is a box that can hold a different type each time."""
    b = [k.text(40, 140, "some Discount", 22, k.ink, 700, "start", True),
         k.text(40, 168, "one real type, fixed when the code is compiled", 17, k.muted, 400, "start"),
         k.node(40, 190, 440, 90, "todaysMemberDeal()", "always returns MemberDiscount", SAND),
         k.arrow(260, 282, 260, 328),
         k.node(140, 330, 240, 80, "MemberDiscount", fill=k.tint),
         k.text(560, 140, "any Discount", 22, k.ink, 700, "start", True),
         k.text(560, 168, "a box; the type inside is chosen while running", 17, k.muted, 400, "start"),
         k.box(560, 190, 500, 220, SAND, k.line),
         k.text(810, 222, "[any Discount]", 18, k.muted, 400, mono=True)]
    for i, name in enumerate(["MemberDiscount", "HappyHour", "NoDiscount"]):
        b.append(k.node(572 + i * 162, 250, 152, 80, name, fill=k.tint))
    b += [k.text(810, 380, "different types, side by side", 17, k.muted),
          k.text(40, 470, "Prefer some: faster, and the compiler checks more. Use any when the type must change.", 19, k.ink, 700, "start")]
    k.svg("some-and-any", 1100, 510, "some and any", "Two ways to say \"a type that conforms to Discount\"", "".join(b))


def reference_cycle():
    """Lesson 10: Customer and Order keep each other alive with strong references; a weak back reference fixes it."""
    b = []
    for x, title, sub, back in [(40, "A strong reference cycle", "neither count reaches 0, so nothing is freed", False),
                                (590, "Fixed with weak", "the order does not keep Dara alive", True)]:
        b += [k.text(x, 140, title, 22, k.ink, 700, "start"), k.text(x, 168, sub, 17, k.muted, 400, "start"),
              k.node(x, 200, 180, 90, "dara", "variable, set to nil", SAND),
              k.node(x + 290, 200, 180, 90, "order", "variable, set to nil", SAND),
              k.node(x, 360, 180, 90, "Customer", "Dara", k.tint),
              k.node(x + 290, 360, 180, 90, "Order", "ticket 1", k.tint),
              f'<line x1="{x + 90}" y1="292" x2="{x + 90}" y2="356" stroke="{k.line}" stroke-width="2.5" stroke-dasharray="6 6"/>',
              f'<line x1="{x + 380}" y1="292" x2="{x + 380}" y2="356" stroke="{k.line}" stroke-width="2.5" stroke-dasharray="6 6"/>',
              k.arrow(x + 182, 390, x + 288, 390),
              k.text(x + 235, 380, "strong", 15, k.muted)]
        if back:
            b += [f'<line x1="{x + 288}" y1="425" x2="{x + 182}" y2="425" stroke="{k.primary}" stroke-width="2.5" '
                  f'stroke-dasharray="8 6" marker-end="url(#head)"/>', k.text(x + 235, 448, "weak", 15, k.primary, 700)]
        else:
            b += [k.arrow(x + 288, 425, x + 182, 425), k.text(x + 235, 448, "strong", 15, k.muted)]
    b.append(k.text(40, 500, "Dashed grey lines: the variables were set to nil, so they no longer hold anything.", 17, k.muted, 400, "start"))
    k.svg("reference-cycle", 1100, 530, "Reference cycles", "Dara and her order point at each other", "".join(b))


def tasks_and_actor():
    """Lesson 11: three child tasks run at the same time; the actor lets them in one at a time."""
    b = [k.node(40, 130, 240, 80, "Task group", "waits for all children", SAND),
         k.text(380, 125, "Child tasks run at the same time", 17, k.muted, 700, "start")]
    for i, (who, drink) in enumerate([("Dara", "Latte"), ("Sokha", "Mocha"), ("Chenda", "Green tea")]):
        y = 140 + i * 110
        b += [k.arrow(282, 170, 378, y + 40),
              k.node(380, y, 250, 80, f"brew({drink})", f"for {who}", k.tint),
              k.arrow(632, y + 40, 718, 260 + (i - 1) * 30)]
    b += [k.box(720, 170, 340, 180, SAND, k.primary),
          k.text(890, 210, "actor TicketCounter", 20, k.ink, 700, mono=True),
          k.text(890, 245, "one task inside at a time", 17, k.muted),
          k.node(760, 270, 260, 60, "last = 3", fill="#FFFFFF"),
          k.text(40, 500, "Tasks may finish in any order, but the actor never hands out the same ticket twice.", 19, k.ink, 700, "start")]
    k.svg("tasks-and-actor", 1100, 530, "Tasks and an actor", "Three drinks brew at once; tickets come from one actor", "".join(b))


def one_moment():
    """Lesson 12: one Date, four clock times."""
    b = [k.node(40, 230, 300, 110, "One Date", "2026-11-04T08:40:00Z", k.tint),
         k.text(40, 380, "Stored once, in UTC,", 17, k.muted, 400, "start"),
         k.text(40, 404, "the same moment everywhere", 17, k.muted, 400, "start")]
    zones = [("Asia/Phnom_Penh", "15:40 (UTC+7)"), ("UTC", "08:40 (UTC+0)"),
             ("Asia/Tokyo", "17:40 (UTC+9)"), ("Europe/Paris", "09:40 (UTC+1)")]
    for i, (zone, clock) in enumerate(zones):
        y = 120 + i * 95
        b += [k.arrow(342, 285, 568, y + 38), k.node(570, y, 490, 76, clock, zone, SAND if i else k.tint)]
    b.append(k.text(40, 520, "Store the moment; format it for the reader's time zone only when you show it.", 19, k.ink, 700, "start"))
    k.svg("one-moment", 1100, 560, "One moment, many clocks", "A Date has no time zone; formatting adds one", "".join(b))


def request_response():
    """Lesson 13: the trip of a request and its response."""
    b = []
    row1 = [("MenuClient", "your code", k.tint), ("URLRequest", "GET /v1/menu, headers", "#FFFFFF"),
            ("URLSession", "sends and waits", "#FFFFFF"), ("Server", "or a saved file", SAND)]
    row2 = [("[MenuItem]", "ready to use", k.tint), ("JSONDecoder", "Codable types", "#FFFFFF"),
            ("Status check", "200 to 299, or an error", "#FFFFFF"), ("HTTPURLResponse", "status, headers, body", SAND)]
    for i, (name, sub, fill) in enumerate(row1):
        x = 40 + i * 265
        b.append(k.node(x, 140, 230, 100, name, sub, fill))
        if i:
            b.append(k.arrow(x - 33, 190, x - 2, 190))
    b.append(k.text(40, 125, "Request", 17, k.muted, 700, "start"))
    b.append(k.arrow(950, 242, 950, 318))
    for i, (name, sub, fill) in enumerate(row2):
        x = 40 + i * 265
        b.append(k.node(x, 320, 230, 100, name, sub, fill))
        if i < 3:
            b.append(k.arrow(x + 263, 370, x + 232, 370))
    b.append(k.text(40, 455, "Response", 17, k.muted, 700, "start"))
    b.append(k.text(40, 505, "Every step can fail; map each failure to one clear error type.", 19, k.ink, 700, "start"))
    k.svg("request-response", 1100, 545, "A request and its response", "From your code to the server and back", "".join(b))


def package_structure():
    """Lesson 14: targets, products, and a dependency in the MinaCoffee package."""
    b = [k.box(40, 120, 640, 380, SAND, k.line),
         k.text(60, 152, "Package MinaCoffee", 20, k.ink, 700, "start"),
         k.node(60, 190, 240, 100, "MinaReceipt", "executable: mina-receipt"),
         k.node(60, 360, 240, 100, "MinaPricingTests", "test target"),
         k.node(400, 270, 240, 110, "MinaPricing", "library + menu.json", k.tint),
         k.arrow(302, 240, 398, 300), k.arrow(302, 410, 398, 350),
         k.node(820, 270, 240, 110, "RielText", "local package", "#FFFFFF"),
         k.arrow(642, 325, 818, 325),
         k.text(820, 410, "../RielText", 16, k.muted, 400, "start", True),
         k.text(40, 540, "Arrows point from a module to the module it uses. Products: MinaPricing (a library) and mina-receipt.", 17, k.muted, 400, "start")]
    k.svg("package-structure", 1100, 570, "Inside a package", "Targets are modules; arrows show what each one uses", "".join(b))


def test_doubles():
    """Lesson 15: code depends on a protocol; tests inject a pretend helper."""
    b = []
    for y, user, proto, real, fake in [(130, "Checkout", "PaymentProcessor", "CardMachine", "PretendProcessor"),
                                        (330, "MenuClient", "DataLoader", "FileLoader", "PretendServer")]:
        b += [k.node(40, y + 40, 220, 90, user, "depends on the protocol", k.tint),
              k.arrow(262, y + 85, 368, y + 85),
              k.node(370, y + 40, 280, 90, proto, "protocol", SAND),
              k.node(760, y, 300, 80, real, "the real one, in the app"),
              k.node(760, y + 100, 300, 80, fake, "a test double, in tests", SAND),
              k.arrow(758, y + 40, 652, y + 70), k.arrow(758, y + 140, 652, y + 100)]
    b.append(k.text(40, 560, "The same code runs with the real helper or the pretend one: tests need no card machine or network.", 18, k.ink, 700, "start"))
    k.svg("test-doubles", 1100, 590, "Test doubles", "Depend on a protocol, and inject the helper", "".join(b))


def result_builder_flow():
    """Lesson 16: how a result builder turns statements into one value."""
    lines = [('"Mina Coffee, Phnom Penh"', "buildExpression"), ("for item in items { item }", "buildArray"),
             ("if isMember { ... }", "buildOptional"), ("if cups >= 5 { ... } else { ... }", "buildEither")]
    b = [k.text(40, 128, "In the function body", 17, k.muted, 700, "start"),
         k.text(560, 128, "The builder method called", 17, k.muted, 700, "start")]
    for i, (code, method) in enumerate(lines):
        y = 145 + i * 85
        b += [k.box(40, y, 440, 64, "#FFFFFF", k.line),
              k.text(60, y + 39, code, 17, k.ink, 400, "start", True),
              k.arrow(482, y + 32, 558, y + 32),
              k.node(560, y, 240, 64, method, fill=k.tint),
              k.arrow(802, y + 32, 868, 290)]
    b += [k.node(870, 230, 190, 120, "buildBlock", "joins every part", SAND),
          k.arrow(965, 352, 965, 418),
          k.node(870, 420, 190, 80, "[String]", "the receipt")]
    k.svg("result-builder-flow", 1100, 540, "How a result builder works", "Each statement becomes a part; buildBlock joins the parts", "".join(b))


def order_system():
    """Lesson 17: the parts of the Mina Coffee order system."""
    b = [k.node(40, 130, 260, 100, "mina", "reads commands", SAND),
         k.node(40, 380, 260, 100, "MinaCoreTests", "PretendMenu, 8 tests", SAND),
         k.box(360, 120, 700, 390, k.tint, k.primary),
         k.text(380, 150, "MinaCore (library)", 19, k.ink, 700, "start"),
         k.node(380, 170, 300, 100, "actor Shop", "tickets, payments, report, save", "#FFFFFF"),
         k.node(740, 170, 300, 100, "PriceRules", "discounts, then tax", "#FFFFFF"),
         k.node(380, 360, 300, 100, "MenuSource", "BundledMenu: menu.json", "#FFFFFF"),
         k.node(740, 360, 300, 100, "Models", "CupSize, MenuItem, Order", "#FFFFFF"),
         k.arrow(302, 180, 378, 210), k.arrow(302, 430, 378, 300),
         k.arrow(682, 220, 738, 220), k.arrow(530, 272, 530, 358), k.arrow(682, 260, 738, 380)]
    b.append(k.text(40, 545, "The iOS course builds the app on the same MinaCore library.", 18, k.muted, 400, "start"))
    k.svg("order-system", 1100, 575, "The Mina Coffee order system", "One library, a command-line program, and tests", "".join(b))


def xcode_window():
    """Lesson 1: the main areas of the Xcode window, as a plain wireframe (no Apple artwork)."""
    x0, y0, w, h = 40, 120, 1020, 470
    b = [k.box(x0, y0, w, h, "#FFFFFF", k.line),
         k.box(x0, y0, w, 64, SAND, k.line),
         k.text(x0 + 24, y0 + 40, "Toolbar", 19, k.ink, 700, "start"),
         k.text(x0 + 120, y0 + 40, "Run ▶  and  Stop ■", 17, k.muted, 400, "start"),
         k.box(x0, y0 + 64, 230, h - 64, k.tint, k.line),
         k.text(x0 + 115, y0 + 220, "Navigator", 19, k.ink, 700),
         k.text(x0 + 115, y0 + 248, "files and folders", 16, k.muted),
         k.box(x0 + w - 210, y0 + 64, 210, h - 64, SAND, k.line),
         k.text(x0 + w - 105, y0 + 220, "Inspector", 19, k.ink, 700),
         k.text(x0 + w - 105, y0 + 248, "settings for the", 16, k.muted),
         k.text(x0 + w - 105, y0 + 270, "selected file", 16, k.muted),
         k.box(x0 + 230, y0 + h - 140, w - 440, 140, k.tint, k.line),
         k.text(x0 + 230 + (w - 440) / 2, y0 + h - 78, "Debug area", 19, k.ink, 700),
         k.text(x0 + 230 + (w - 440) / 2, y0 + h - 50, "the console shows the output", 16, k.muted),
         k.text(x0 + 230 + (w - 440) / 2, y0 + 190, "Editor", 22, k.ink, 700),
         k.text(x0 + 230 + (w - 440) / 2, y0 + 220, "read and write code here", 16, k.muted)]
    for i, width in enumerate((300, 220, 340, 260, 180)):  # a few gray lines that stand for code
        b.append(k.box(x0 + 270, y0 + 250 + i * 14, width * 0.7, 5, k.line, None, 0))
    b.append(k.text(40, 625, "Open a package with open Package.swift, then press Run (Command-R).", 18, k.muted, 400, "start"))
    k.svg("xcode-window", 1100, 655, "The Xcode window", "Five main areas", "".join(b))


if __name__ == "__main__":
    captured_values()
    optional_box()
    three_collections()
    value_and_reference()
    some_and_any()
    reference_cycle()
    tasks_and_actor()
    one_moment()
    request_response()
    package_structure()
    test_doubles()
    result_builder_flow()
    order_system()
    xcode_window()
