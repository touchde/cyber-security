"""Shared drawing helpers for course diagrams. Each course passes its own palette and fonts, so diagrams
look like their course. Square corners, as everywhere in the books and slides.

    kit = Kit(folder="02-flutter", primary="#4B3FCF", tint="#F2F0FE", ink="#1A1830", muted="#5D5A78", line="#CFCBEF",
              sans="'Figtree', sans-serif", mono="'Fira Code', monospace")
"""
import html
import pathlib

OUT = pathlib.Path(__file__).resolve().parent / "diagrams"
PAD = 14  # space between a box's edge and its text

# Rough character widths, as a share of the font size, for Helvetica-like sans fonts. Good enough to keep text inside boxes.
NARROW, WIDE = set("iljtfrI.,:;'|!() "), set("mwMWOQGDHNU@%")


def text_width(s, size, weight=400, mono=False):
    if mono:
        return len(s) * size * 0.61
    total = 0
    for ch in s:
        total += 0.28 if ch in NARROW else 0.82 if ch in WIDE else 0.64 if ch.isupper() or ch.isdigit() else 0.52
    return total * size * (1.08 if weight >= 600 else 1)


class Kit:
    def __init__(self, folder, primary, tint, ink, muted, line, sans, mono, accent=None):
        self.folder, self.primary, self.tint, self.ink, self.muted, self.line = folder, primary, tint, ink, muted, line
        self.sans, self.mono, self.accent = sans, mono, accent or primary

    def text(self, x, y, s, size=20, color=None, weight=400, anchor="middle", mono=False):
        return (f'<text x="{x}" y="{y}" font-family="{self.mono if mono else self.sans}" font-size="{size}" font-weight="{weight}" '
                f'fill="{color or self.ink}" text-anchor="{anchor}">{html.escape(s)}</text>')

    def box(self, x, y, w, h, fill="#FFFFFF", stroke=None, sw=2.5):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke or self.primary}" stroke-width="{sw}"/>'

    def fit(self, s, size, width, weight=400, mono=False, smallest=14):
        """The largest font size, at most `size`, at which `s` fits in `width` pixels (an estimate)."""
        while size > smallest and text_width(s, size, weight, mono) > width:
            size -= 1
        return size

    def node(self, x, y, w, h, title, sub=None, fill="#FFFFFF", stroke=None, color=None, sub_color=None):
        """A box with a bold title and an optional smaller line under it. Text shrinks to fit inside the box,
        with padding, and the second line wraps onto two lines if it is still too long."""
        inner = w - 2 * PAD
        mid = y + h / 2
        parts = [self.box(x, y, w, h, fill, stroke)]
        ts = self.fit(title, 23, inner, 700, smallest=16)
        if not sub:
            return "".join(parts + [self.text(x + w / 2, mid + ts * 0.35, title, ts, color, 700)])
        ss = self.fit(sub, 18, inner, smallest=15)
        lines = [sub]
        words = sub.split()
        if text_width(sub, ss, 400) > inner and len(words) > 1:
            best = min(range(1, len(words)), key=lambda i: abs(len(" ".join(words[:i])) - len(" ".join(words[i:]))))
            lines = [" ".join(words[:best]), " ".join(words[best:])]
            ss = min(self.fit(line, 18, inner, smallest=13) for line in lines)
        block = ts + 8 + len(lines) * (ss + 5)
        top = mid - block / 2
        parts.append(self.text(x + w / 2, top + ts * 0.8, title, ts, color, 700))
        for i, line in enumerate(lines):
            parts.append(self.text(x + w / 2, top + ts + 8 + ss * 0.85 + i * (ss + 5), line, ss, sub_color or self.muted))
        return "".join(parts)

    def steps(self, items, y, fills=(), w=300, h=100, x0=40, gap=60, drop=60):
        """Six (or more) steps as two rows of three, numbered, with a bent arrow from the end of row 1 to the start of row 2.
        Returns the SVG and the y just below row 2."""
        out, per = [], 3
        for i, (name, sub) in enumerate(items):
            row, col = divmod(i, per)
            x, top = x0 + col * (w + gap), y + row * (h + drop)
            out.append(self.node(x, top, w, h, f"{i + 1}. {name}", sub, fills[i] if i < len(fills) and fills[i] else "#FFFFFF"))
            if col:
                out.append(self.arrow(x - gap + 2, top + h / 2, x - 2, top + h / 2))
            elif row:
                ex, sx = x0 + (per - 1) * (w + gap) + w / 2, x0 + w / 2
                mid = top - drop / 2
                out.append(f'<path d="M{ex},{top - drop} L{ex},{mid} L{sx},{mid} L{sx},{top - 2}" fill="none" '
                           f'stroke="{self.muted}" stroke-width="2.5" marker-end="url(#head)"/>')
        rows = (len(items) + per - 1) // per
        return "".join(out), y + rows * h + (rows - 1) * drop

    def arrow(self, x1, y1, x2, y2, both=False):
        """A straight arrow. The head's tip lands on (x2, y2); the line stops under the head, so it never shows past the tip."""
        start = ' marker-start="url(#tail)"' if both else ""
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{self.muted}" stroke-width="2.5" marker-end="url(#head)"{start}/>'

    def step(self, x, y, n):
        return f'<rect x="{x - 15}" y="{y - 15}" width="30" height="30" fill="{self.accent}"/>' + self.text(x, y + 6, str(n), 17, "#FFFFFF", 700)

    def svg(self, name, w, h, title, subtitle, body):
        m = self.muted
        defs = (f'<defs><marker id="head" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="12" refX="11" refY="6" orient="auto">'
                f'<path d="M0,0 L14,6 L0,12 z" fill="{m}"/></marker>'
                f'<marker id="tail" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="12" refX="3" refY="6" orient="auto">'
                f'<path d="M14,0 L0,6 L14,12 z" fill="{m}"/></marker></defs>')
        head = self.text(40, 52, title, 30, self.ink, 700, "start") + self.text(40, 84, subtitle, 18, self.muted, 400, "start")
        (OUT / self.folder).mkdir(exist_ok=True)
        (OUT / self.folder / f"{name}.svg").write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(title)}">'
            f'<title>{html.escape(title)}</title>{defs}<rect width="{w}" height="{h}" fill="#FFFFFF"/>{head}{body}</svg>')
