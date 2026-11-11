"""Generate the C/C++ course's diagrams, in its teal palette, into assets/diagrams/.

    python3 assets/build_c_cpp_diagrams.py

They are written to diagrams/21-c-cpp/. Square corners, as everywhere in the course.
"""
import html
import pathlib

OUT = pathlib.Path(__file__).resolve().parent / "diagrams"
TEAL, TINT, INK, MUTED, LINE, GRAPHITE = "#0B7A75", "#E6F4F2", "#172026", "#56636B", "#B7C9C7", "#171D22"
SANS = "'Source Sans 3', 'Helvetica Neue', Arial, sans-serif"
MONO = "'Source Code Pro', Menlo, Consolas, monospace"


def text(x, y, s, size=20, color=INK, weight=400, anchor="middle", mono=False):
    return (f'<text x="{x}" y="{y}" font-family="{MONO if mono else SANS}" font-size="{size}" font-weight="{weight}" '
            f'fill="{color}" text-anchor="{anchor}">{html.escape(s)}</text>')


def box(x, y, w, h, fill="#FFFFFF", stroke=TEAL, sw=2.5):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def node(x, y, w, h, title, sub=None, fill="#FFFFFF"):
    mid = y + h / 2
    parts = [box(x, y, w, h, fill)]
    if sub:
        parts += [text(x + w / 2, mid - 6, title, 23, weight=700), text(x + w / 2, mid + 24, sub, 18, MUTED)]
    else:
        parts += [text(x + w / 2, mid + 8, title, 23, weight=700)]
    return "".join(parts)


def arrow(x1, y1, x2, y2, both=False):
    start = ' marker-start="url(#tail)"' if both else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{MUTED}" stroke-width="2.5" marker-end="url(#head)"{start}/>'


def step(x, y, n):
    return (f'<rect x="{x - 15}" y="{y - 15}" width="30" height="30" fill="{TEAL}"/>' + text(x, y + 6, str(n), 17, "#FFFFFF", 700))


def svg(name, w, h, title, subtitle, body):
    defs = (f'<defs><marker id="head" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="12" refX="11" refY="6" orient="auto">'
            f'<path d="M0,0 L14,6 L0,12 z" fill="{MUTED}"/></marker>'
            f'<marker id="tail" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="12" refX="3" refY="6" orient="auto">'
            f'<path d="M14,0 L0,6 L14,12 z" fill="{MUTED}"/></marker></defs>')
    head = text(40, 52, title, 30, INK, 700, "start") + text(40, 84, subtitle, 18, MUTED, 400, "start")
    (OUT / "21-c-cpp").mkdir(exist_ok=True)
    (OUT / "21-c-cpp" / f"{name}.svg").write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}">'
        f'<title>{html.escape(title)}</title>{defs}<rect width="{w}" height="{h}" fill="#FFFFFF"/>{head}{body}</svg>')


def computer_parts():
    b = [node(30, 210, 240, 110, "Input", "keyboard, touch screen"),
         node(390, 115, 320, 110, "Processor (CPU)", "follows instructions", TINT),
         node(390, 300, 320, 110, "Memory (RAM)", "fast, lost with no power"),
         node(830, 210, 240, 110, "Output", "printer, screen"),
         node(390, 490, 320, 110, "Storage (SSD)", "slower, keeps data with no power"),
         arrow(270, 240, 388, 170), arrow(712, 170, 828, 240),
         arrow(550, 227, 550, 298, both=True), arrow(550, 412, 550, 488, both=True),
         step(535, 450, 1), step(320, 205, 2), step(535, 262, 3), step(780, 205, 4), step(600, 450, 5)]
    legend = ["1  Program copied to memory", "2  A key is pressed", "3  Processor reads and writes memory",
              "4  Result goes to the printer", "5  Sales saved to storage"]
    b += [text(745, 470 + i * 28, s, 19, MUTED, 400, "start") for i, s in enumerate(legend)]
    svg("computer-parts", 1100, 630, "The parts of a computer", "Following one order at Mina Coffee, from key press to receipt", "".join(b))


def byte_values():
    bits, places = "01001101", [128, 64, 32, 16, 8, 4, 2, 1]
    b, x = [], 130
    for bit, place in zip(bits, places):
        on = bit == "1"
        b += [text(x + 45, 165, str(place), 20, TEAL if on else MUTED, 700 if on else 400),
              box(x, 180, 90, 90, TEAL if on else "#FFFFFF", TEAL if on else LINE), text(x + 45, 240, bit, 40, "#FFFFFF" if on else MUTED, 700, mono=True)]
        x += 105
    b += [text(40, 170, "Place value", 18, MUTED, 400, "start"), text(40, 232, "One byte", 18, MUTED, 400, "start"),
          text(550, 325, "64 + 8 + 4 + 1 = 77", 27, INK, 700),
          text(550, 372, "The same value, three ways:  decimal 77   ·   hexadecimal 4D   ·   the letter M in ASCII", 20, MUTED)]
    svg("byte-values", 1100, 410, "Reading one byte", "Each bit is worth double the bit on its right. Add the values of the bits that are 1.", "".join(b))


def instruction_cycle():
    b = [node(90, 170, 240, 120, "1. Fetch", "read the next instruction", TINT), node(430, 170, 240, 120, "2. Decode", "work out what it means", TINT),
         node(770, 170, 240, 120, "3. Execute", "do the job", TINT), arrow(330, 230, 428, 230), arrow(670, 230, 768, 230),
         f'<path d="M890,290 L890,350 L210,350 L210,294" fill="none" stroke="{MUTED}" stroke-width="2.5" marker-end="url(#head)"/>',
         text(550, 340, "then the next instruction, billions of times every second", 18, MUTED)]
    rows = [("Read the price from memory", "10000"), ("Divide it by 5", "2000"), ("Subtract that from the price", "8000"), ("Write the result to memory", "8000 saved")]
    y = 390
    b += [text(90, y + 8, "Taking 20% off 10000 riel, in small jobs:", 19, INK, 700, "start")]
    for i, (job, result) in enumerate(rows):
        yy = y + 24 + i * 44
        b += [box(90, yy, 920, 40, "#FFFFFF", LINE, 1.5), step(112, yy + 20, i + 1), text(145, yy + 27, job, 19, INK, 400, "start"), text(990, yy + 27, result, 18, TEAL, 700, "end", True)]
    svg("instruction-cycle", 1100, 610, "How the processor runs a program", "It repeats the same three steps, one instruction at a time.", "".join(b))


def memory_boxes():
    cells = [("0x1000", "4D", "M"), ("0x1001", "69", "i"), ("0x1002", "6E", "n"), ("0x1003", "61", "a"),
             ("0x1004", "10", ""), ("0x1005", "27", ""), ("0x1006", "00", ""), ("0x1007", "00", "")]
    b, x = [], 90
    for i, (address, value, letter) in enumerate(cells):
        b += [text(x + 55, 178, address, 18, MUTED, mono=True), box(x, 190, 110, 100, TINT if i < 4 else "#FFFFFF"), text(x + 55, 240, value, 32, INK, 700, mono=True)]
        if letter:
            b.append(text(x + 55, 276, letter, 18, TEAL, 700))
        x += 115
    b += [f'<path d="M90,308 L90,322 L545,322 L545,308" fill="none" stroke="{TEAL}" stroke-width="2.5"/>', text(317, 352, "The text \"Mina\": 4 bytes", 20, TEAL, 700),
          f'<path d="M550,308 L550,322 L1005,322 L1005,308" fill="none" stroke="{TEAL}" stroke-width="2.5"/>', text(777, 352, "The number 10000: 4 bytes", 20, TEAL, 700),
          text(550, 402, "Every box holds one byte, and every box has its own number: its address.", 20, MUTED),
          text(550, 432, "The boxes do not say what they mean. The program decides.", 20, MUTED)]
    svg("memory-boxes", 1100, 460, "Memory as numbered boxes", "Eight bytes of memory, shown in hexadecimal. The addresses are examples.", "".join(b))


def compiler_interpreter():
    b = [text(40, 150, "Compiler: translate everything first, then run", 22, TEAL, 700, "start"),
         node(40, 170, 200, 100, "Source code", "hello.c"), node(320, 170, 200, 100, "Compiler", "checks and translates", TINT),
         node(600, 170, 200, 100, "Program file", "machine code"), node(880, 170, 180, 100, "Processor", "runs it"),
         arrow(240, 220, 318, 220), arrow(520, 220, 598, 220), arrow(800, 220, 878, 220),
         text(40, 315, "Used by C, C++, and Swift. Slower to start, but the program runs very fast.", 18, MUTED, 400, "start"),
         text(40, 390, "Interpreter: read and do, one piece at a time, while the program runs", 22, TEAL, 700, "start"),
         node(40, 410, 200, 100, "Source code", "hello.py"), node(460, 410, 240, 100, "Interpreter", "a running program", TINT), node(880, 410, 180, 100, "Processor", "runs the interpreter"),
         arrow(240, 460, 458, 460), arrow(700, 460, 878, 460),
         text(40, 555, "Used by Python and JavaScript, often with speed-up tricks. Easy to start, but usually slower.", 18, MUTED, 400, "start")]
    svg("compiler-interpreter", 1100, 590, "Compiler and interpreter", "Two ways to make a processor follow code that people wrote", "".join(b))


def input_process_output():
    b = [node(40, 150, 300, 120, "Input", "data comes in"), node(400, 150, 300, 120, "Processing", "exact steps, from a program", TINT),
         node(760, 150, 300, 120, "Output", "a result goes out"),
         arrow(340, 210, 398, 210), arrow(700, 210, 758, 210),
         text(190, 320, "Mina presses the key", 19, TEAL, 700), text(190, 346, "for an iced latte", 18, MUTED),
         text(550, 320, "take 20% off, add the tax", 19, TEAL, 700), text(550, 346, "billions of small steps a second", 18, MUTED),
         text(910, 320, "the receipt prints", 19, TEAL, 700), text(910, 346, "6600 riel", 18, MUTED),
         text(40, 420, "A phone, a laptop, and the chip in a coffee machine all follow this pattern.", 19, INK, 700, "start"),
         text(40, 452, "The computer knows nothing about lattes. It only follows the program.", 18, MUTED, 400, "start")]
    svg("input-process-output", 1100, 490, "What every computer does", "Input, processing, and output, again and again", "".join(b))


def operating_system():
    apps = [("Your C program", "a process"), ("Web browser", "a process"), ("Music app", "a process")]
    b = []
    for i, (name, sub) in enumerate(apps):
        b.append(node(40 + i * 345, 130, 330, 90, name, sub))
    b += [node(40, 290, 1020, 110, "Operating system", "runs programs · shares the processor · protects memory · manages files · talks to devices", TINT),
          node(40, 470, 1020, 90, "Hardware", "processor, memory, storage, screen, keyboard, network"),
          arrow(205, 222, 205, 288), arrow(550, 222, 550, 288), arrow(895, 222, 895, 288),
          arrow(550, 402, 550, 468),
          text(222, 262, "system call: \u201cprint this line\u201d", 17, TEAL, 700, "start"),
          text(40, 610, "Programs never touch the hardware directly. They ask the operating system.", 19, INK, 700, "start")]
    svg("operating-system", 1100, 640, "Where the operating system sits", "Between the programs you run and the machine itself", "".join(b))


def folder_tree():
    rows = [(0, "/", "folder", "the top of the tree"), (1, "tmp", "folder", ""), (2, "shop", "here", "pwd shows /tmp/shop"),
            (3, "receipts", "folder", "mkdir receipts"), (3, "menu.txt", "file", "cat menu.txt")]
    b, y0 = [], 140
    for i, (depth, name, kind, note) in enumerate(rows):
        x, y = 80 + depth * 70, y0 + i * 70
        fill = TINT if kind == "here" else "#FFFFFF"
        w = 200
        b.append(box(x, y, w, 50, fill, TEAL if kind != "file" else MUTED))
        b.append(text(x + 18, y + 33, name + ("/" if kind != "file" and name != "/" else ""), 21, INK, 700, "start", True))
        if depth:
            px = 80 + (depth - 1) * 70 + 30
            b.append(f'<path d="M{px},{y - 20} L{px},{y + 25} L{x},{y + 25}" fill="none" stroke="{LINE}" stroke-width="2.5"/>')
        if note:
            b.append(text(x + w + 30, y + 32, note, 18, TEAL if kind == "here" else MUTED, 700 if kind == "here" else 400, "start", kind != "folder" or i == 3))
    b += [text(780, 160, "The path to the file:", 19, INK, 700, "start"),
          text(780, 195, "/tmp/shop/menu.txt", 24, TEAL, 700, "start", True),
          text(780, 250, "cd ..  goes up one level,", 18, MUTED, 400, "start"),
          text(780, 276, "from receipts/ back to shop/.", 18, MUTED, 400, "start")]
    svg("folder-tree", 1100, 520, "Folders form a tree", "The shop folder from this section, and the path to one file", "".join(b))


def language_levels():
    levels = [("High-level language: C", "price + tax", "Most programmers", TINT),
              ("Assembly", "add w0, w1, w0", "Careful people", "#FFFFFF"),
              ("Machine code", "0b000020", "The processor", "#FFFFFF")]
    b = []
    for i, (name, code, who, fill) in enumerate(levels):
        y = 130 + i * 150
        b += [box(40, y, 700, 100, fill), text(70, y + 40, name, 22, INK, 700, "start"), text(70, y + 76, code, 22, TEAL, 700, "start", True),
              text(790, y + 46, "Read easily by:", 17, MUTED, 400, "start"), text(790, y + 74, who, 20, INK, 700, "start")]
        if i:
            b += [arrow(390, y - 48, 390, y - 2), text(410, y - 18, "compiler" if i == 1 else "assembler", 17, MUTED, 400, "start")]
    b.append(text(40, 590, "The same work at three levels. Higher is closer to how people think; lower is closer to the machine.", 18, MUTED, 400, "start"))
    svg("language-levels", 1100, 620, "From C down to machine code", "Adding the tax, written three ways (ARM processor)", "".join(b))


def biggest_order_flow():
    b = [node(60, 130, 300, 80, "Paper = 0", "the biggest so far"),
         node(60, 260, 300, 80, "Take the next order"),
         f'<polygon points="210,385 360,445 210,505 60,445" fill="{TINT}" stroke="{TEAL}" stroke-width="2.5"/>',
         text(210, 440, "Bigger than", 19, INK, 700), text(210, 464, "the paper?", 19, INK, 700),
         node(480, 405, 300, 80, "Paper = this order"),
         f'<polygon points="210,555 360,615 210,675 60,615" fill="{TINT}" stroke="{TEAL}" stroke-width="2.5"/>',
         text(210, 610, "More orders?", 19, INK, 700), text(210, 634, "", 19, INK, 700),
         node(480, 575, 300, 80, "Answer: the paper", fill=TINT),
         arrow(210, 212, 210, 258), arrow(210, 342, 210, 383),
         arrow(362, 445, 478, 445), text(400, 433, "yes", 17, TEAL, 700, "start"),
         arrow(210, 507, 210, 553), text(222, 522, "no", 17, MUTED, 700, "start"),
         f'<path d="M630,487 L630,530 L210,530" fill="none" stroke="{MUTED}" stroke-width="2.5"/>',
         arrow(362, 615, 478, 615), text(400, 603, "no", 17, MUTED, 700, "start"),
         f'<path d="M60,615 L30,615 L30,300 L58,300" fill="none" stroke="{MUTED}" stroke-width="2.5" marker-end="url(#head)"/>',
         text(38, 596, "yes", 17, TEAL, 700, "start"),
         text(840, 160, "Three patterns:", 19, INK, 700, "start"),
         text(840, 195, "Sequence: one step,", 18, MUTED, 400, "start"), text(840, 219, "then the next", 18, MUTED, 400, "start"),
         text(840, 260, "Decision: the diamonds", 18, MUTED, 400, "start"),
         text(840, 300, "Repetition: the arrow", 18, MUTED, 400, "start"), text(840, 324, "back up", 18, MUTED, 400, "start")]
    svg("biggest-order-flow", 1100, 710, "Finding the biggest order", "Vanna's steps, drawn as a flowchart", "".join(b))


for make in (computer_parts, byte_values, instruction_cycle, memory_boxes, compiler_interpreter,
             input_process_output, operating_system, folder_tree, language_levels, biggest_order_flow):
    make()
print("diagrams written")
