"""Diagrams for the Linux for Security course (03-linux). Terminal palette: green on white, Work Sans + Fira Code.

    python3 assets/build_linux_diagrams.py

SVGs are written to assets/diagrams/03-linux/. Referenced from lessons as
![alt](../../../../assets/diagrams/03-linux/<name>.svg).
"""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from diagram_kit import Kit, PAD  # noqa: E402

kit = Kit(
    folder="03-linux",
    primary="#15803D", tint="#EBF5EF", ink="#122017", muted="#4E6357", line="#CFE3D6",
    sans="'Work Sans', sans-serif", mono="'Fira Code', monospace", accent="#15803D",
)
GREEN, DARK, PALE = "#15803D", "#0A1711", "#EBF5EF"


# --- Lesson 1: where Linux runs -------------------------------------------------
def where_linux_runs():
    items = [
        ("Web servers", "most of the internet"),
        ("The cloud", "AWS, Google, Azure"),
        ("Phones", "Android (billions)"),
        ("Devices / IoT", "routers, TVs, cars"),
        ("Supercomputers", "essentially all"),
        ("Security tools", "Kali and the rest"),
    ]
    body = []
    cx = 500
    ky = 130
    body.append(kit.node(cx - 120, ky, 240, 68, "Linux kernel", fill=DARK, color="#FFFFFF"))
    # 6 uses in two rows of three, each linked from the kernel's bottom edge
    w, h, gx, gy = 280, 80, 24, 70
    total = 3 * w + 2 * gx
    x0 = cx - total / 2
    row_y = ky + 68 + 80
    for i, (t, s) in enumerate(items):
        row, col = divmod(i, 3)
        x = x0 + col * (w + gx)
        y = row_y + row * (h + gy)
        # line from kernel bottom-center to the top-center of each top-row box; second row links from the box above
        if row == 0:
            body.append(f'<path d="M{cx},{ky + 68} L{cx},{ky + 68 + 40} L{x + w / 2},{ky + 68 + 40} L{x + w / 2},{y}" '
                        f'fill="none" stroke="{kit.line}" stroke-width="2.5"/>')
        else:
            body.append(f'<line x1="{x + w / 2}" y1="{y - gy}" x2="{x + w / 2}" y2="{y}" stroke="{kit.line}" stroke-width="2.5"/>')
        body.append(kit.node(x, y, w, h, t, s, fill=PALE, stroke=GREEN))
    kit.svg("where-linux-runs", 1000, row_y + 2 * h + gy + 30, "Where Linux runs",
            "the systems you attack and defend are mostly Linux", "".join(body))


# --- Lesson 3: the file system tree --------------------------------------------
def filesystem_tree():
    body = []
    root = ("/", "the root of everything", 420, 130, 160, 64)
    body.append(kit.node(*root[2:], root[0], root[1], fill=DARK, color="#FFFFFF"))
    children = [
        ("/home", "users' files"),
        ("/etc", "configuration"),
        ("/var", "logs, changing data"),
        ("/usr", "programs"),
        ("/bin", "core commands"),
    ]
    n = len(children)
    w, h, gap = 170, 72, 18
    total = n * w + (n - 1) * gap
    x0 = 500 - total / 2
    for i, (name, sub) in enumerate(children):
        x = x0 + i * (w + gap)
        body.append(f'<path d="M500,194 L500,250 L{x + w / 2},250 L{x + w / 2},300" fill="none" stroke="{kit.line}" stroke-width="2.5"/>')
        body.append(kit.node(x, 300, w, h, name, sub, fill=PALE, stroke=GREEN))
    # one example leaf under /home
    body.append(f'<path d="M{x0 + w / 2},372 L{x0 + w / 2},420" fill="none" stroke="{kit.line}" stroke-width="2.5"/>')
    body.append(kit.node(x0 - 10, 420, 190, 60, "/home/dara", "your home directory", fill="#FFFFFF", stroke=kit.muted))
    kit.svg("filesystem-tree", 1000, 510, "The Linux file system",
            "one tree from the root /, not separate drive letters", "".join(body))


# --- Lesson 5: a permission string ---------------------------------------------
def permissions():
    body = []
    chars = list("-rwxr-xr--")
    cw = 66
    x0 = 150
    y = 180
    for i, ch in enumerate(chars):
        x = x0 + i * cw
        fill = DARK if i == 0 else PALE
        color = "#FFFFFF" if i == 0 else GREEN if ch != "-" else kit.muted
        body.append(kit.box(x, y, cw - 6, 76, fill=fill, stroke=GREEN if i else kit.muted))
        body.append(kit.text(x + (cw - 6) / 2, y + 50, ch, 34, color, 700, mono=True))
    # group brackets
    groups = [(0, 1, "type", "file / dir"), (1, 4, "owner", "rwx = read, write, execute"),
              (4, 7, "group", "r-x = read, execute"), (7, 10, "others", "r-- = read only")]
    for a, b, label, desc in groups:
        gx = x0 + a * cw
        gw = (b - a) * cw - 6
        by = y + 90
        body.append(f'<path d="M{gx},{by} L{gx},{by + 14} L{gx + gw},{by + 14} L{gx + gw},{by}" fill="none" stroke="{GREEN}" stroke-width="2.5"/>')
        body.append(kit.text(gx + gw / 2, by + 46, label, 21, kit.ink, 700))
        body.append(kit.text(gx + gw / 2, by + 74, desc, 15, kit.muted))
    kit.svg("permissions", 1000, 380, "Reading a permission string",
            "-rwxr-xr-- : one type character, then owner, group, and others", "".join(body))


# --- Lesson 8: a pipeline ------------------------------------------------------
def pipeline():
    body = []
    stages = [("cat auth.log", "read the file"), ("grep 'Failed'", "keep failed logins"),
              ("sort", "group them"), ("uniq -c", "count each")]
    w, h, gap = 210, 80, 46
    y = 170
    x0 = 40
    for i, (cmd, sub) in enumerate(stages):
        x = x0 + i * (w + gap)
        body.append(kit.node(x, y, w, h, cmd, sub, fill=PALE, stroke=GREEN))
        if i:
            mx = x - gap
            body.append(kit.text(mx + gap / 2, y + h / 2 - 10, "|", 30, GREEN, 700, mono=True))
            body.append(kit.arrow(x - gap + 6, y + h / 2, x - 2, y + h / 2))
    # final output
    fx = x0 + len(stages) * (w + gap)
    body.append(kit.arrow(fx - gap + 6, y + h / 2, fx - 2, y + h / 2))
    body.append(kit.node(fx, y, 190, h, "12 Failed", "the answer", fill=DARK, color="#FFFFFF", sub_color="#9FE0C8"))
    body.append(kit.text(40, y + h + 56, "Each command's output becomes the next command's input. One line does the work of many.",
                         18, kit.muted, anchor="start"))
    kit.svg("pipeline", 1200, 320, "A pipeline",
            "small commands joined by | (pipe) into one powerful line", "".join(body))


# --- Lesson 12: hardening layers -----------------------------------------------
def hardening_layers():
    body = []
    layers = [
        ("Updates", "patch known holes"),
        ("Least privilege", "non-root users, sudo"),
        ("SSH keys, no passwords", "and fail2ban"),
        ("Host firewall (ufw)", "only needed ports open"),
        ("Remove what you don't need", "fewer services = smaller attack surface"),
    ]
    w = 620
    h = 66
    gap = 16
    x = 500 - w / 2
    for i, (t, s) in enumerate(layers):
        y = 130 + i * (h + gap)
        shade = f"#E3F2E9" if i % 2 == 0 else PALE
        body.append(kit.node(x, y, w, h, t, s, fill=shade, stroke=GREEN))
    body.append(kit.text(500, 130 + len(layers) * (h + gap) + 30,
                         "Defense in depth: an attacker must beat every layer.", 18, kit.muted))
    kit.svg("hardening-layers", 1000, 560, "A hardened server",
            "several layers, so one failure is not a break-in", "".join(body))


if __name__ == "__main__":
    where_linux_runs()
    filesystem_tree()
    permissions()
    pipeline()
    hardening_layers()
    print("wrote 5 Linux diagrams to assets/diagrams/03-linux/")
