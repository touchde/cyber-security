"""Generate the Performance course's diagrams, in its orange palette, into assets/diagrams/.

    python3 assets/build_performance_diagrams.py

They are written to diagrams/16-performance-profiling/.
"""
from diagram_kit import Kit

k = Kit(folder="16-performance-profiling", primary="#C2410C", tint="#FFF3EA", ink="#1F130B", muted="#66554A", line="#F5DCC9",
        sans="'Sora', 'Helvetica Neue', Arial, sans-serif", mono="'Azeret Mono', Menlo, monospace", accent="#C2410C")


def frame_budget():
    b = [k.text(40, 140, "At 60 Hz, each frame has 16.7 ms", 21, k.primary, 700, "start")]
    widths = [(11, "#FFFFFF"), (14, "#FFFFFF"), (29, "#FFD8C2"), (9, "#FFFFFF"), (12, "#FFFFFF")]
    x = 40
    for i, (ms, fill) in enumerate(widths):
        w = ms * 12
        b += [k.box(x, 170, w, 70, fill, k.primary if fill != "#FFFFFF" else k.muted, 2), k.text(x + w / 2, 213, f"{ms} ms", 18, k.ink, 700)]
        x += w + 8
    b += [f'<line x1="40" y1="260" x2="{40 + 16.7 * 12}" y2="260" stroke="{k.primary}" stroke-width="3"/>',
          k.text(40, 290, "16.7 ms budget", 16, k.primary, 700, "start"),
          k.text(40, 350, "One frame took 29 ms: the screen showed the old frame twice. Users see a stutter, called jank.", 19, k.ink, 700, "start"),
          k.text(40, 382, "At 120 Hz, the budget is only 8.3 ms.", 18, k.muted, 400, "start")]
    k.svg("frame-budget", 1100, 420, "The frame budget", "Every frame must be ready before the screen refreshes", "".join(b))


def percentiles():
    times = [620, 640, 650, 660, 680, 690, 700, 710, 720, 730, 740, 750, 760, 780, 800, 820, 850, 900, 3900, 4200]
    b = []
    for i, ms in enumerate(times):
        h = ms / 4200 * 300
        slow = ms > 1000
        b.append(f'<rect x="{60 + i * 38}" y="{440 - h}" width="28" height="{h}" fill="{k.primary if slow else "#F5B48A"}"/>')
    for label, value, color, dy in (("average 1065 ms", 1065, k.ink, -4), ("p50 730 ms", 730, "#8A5A3C", 18), ("p95 3900 ms", 3900, k.primary, 6)):
        y = 440 - value / 4200 * 300
        b += [f'<line x1="50" y1="{y}" x2="830" y2="{y}" stroke="{color}" stroke-width="2" stroke-dasharray="8 6"/>',
              k.text(845, y + dy, label, 17, color, 700, "start")]
    b += [k.text(60, 480, "20 starts of the ordering app, sorted. Most are under a second; two take about 4 seconds.", 18, k.muted, 400, "start"),
          k.text(60, 510, "The average says \u201cabout 1 second\u201d. The p95 says \u201csome people wait 4 seconds\u201d.", 19, k.ink, 700, "start")]
    k.svg("percentiles", 1100, 540, "Averages hide slow users", "The same start times, described three ways", "".join(b))


for make in (frame_budget, percentiles):
    make()
print("wrote 2 diagrams")
