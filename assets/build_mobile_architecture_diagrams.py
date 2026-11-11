"""Generate the Mobile Architecture course's diagrams, in its blueprint palette, into assets/diagrams/.

    python3 assets/build_mobile_architecture_diagrams.py

They are written to diagrams/13-mobile-architecture/.
"""
from diagram_kit import Kit

k = Kit(folder="13-mobile-architecture", primary="#1F5F9E", tint="#EEF5FC", ink="#0F1E2E", muted="#4D6075", line="#D3E1F0",
        sans="'Noto Sans', 'Helvetica Neue', Arial, sans-serif", mono="'Noto Sans Mono', Menlo, monospace", accent="#1F5F9E")
AZURE = "#DCEBFA"


def tangled_and_separated():
    jobs = ["read the order text", "price rules", "receipt layout", "print"]
    b = [k.text(40, 135, "Before: one function does everything", 21, k.primary, 700, "start"),
         k.box(40, 155, 470, 300, "#FFFFFF", "#B23A3A", 2.5)]
    for i, job in enumerate(jobs):
        b.append(k.text(70, 205 + i * 62, "• " + job, 20, k.ink, 400, "start"))
    b += [k.text(275, 485, "Change one job, and you touch them all.", 17, "#B23A3A", 700),
          k.text(590, 135, "After: parts with one job each", 21, k.primary, 700, "start"),
          k.node(590, 160, 470, 80, "Order", "what an order is (data)", AZURE),
          k.node(590, 265, 470, 80, "orderTotal", "how much it costs (rules)", k.tint),
          k.node(590, 370, 470, 80, "receiptLines", "how it looks (presentation)", "#FFFFFF"),
          k.text(825, 485, "Change one job, and the others stay the same.", 17, k.primary, 700)]
    k.svg("tangled-and-separated", 1100, 520, "Separation of concerns", "The same receipt code, before and after", "".join(b))


def layers():
    rows = [("UI layer", "screens and what they show: receipt, SMS, cart", "#FFFFFF"),
            ("Domain layer", "the shop's rules: discounts, tax, points", AZURE),
            ("Data layer", "where data comes from and goes: server, database, files", k.tint)]
    b = []
    for i, (name, sub, fill) in enumerate(rows):
        y = 130 + i * 130
        b += [k.box(80, y, 700, 100, fill, k.primary), k.text(110, y + 45, name, 24, k.ink, 700, "start"), k.text(110, y + 75, sub, 18, k.muted, 400, "start")]
        if i < 2:
            b.append(k.arrow(430, y + 100, 430, y + 128))
    b += [k.text(820, 190, "Each layer only", 18, k.primary, 700, "start"), k.text(820, 215, "talks to the one", 18, k.primary, 700, "start"),
          k.text(820, 240, "below it.", 18, k.primary, 700, "start"),
          k.text(820, 330, "The rules know", 18, k.muted, 400, "start"), k.text(820, 355, "nothing about", 18, k.muted, 400, "start"),
          k.text(820, 380, "screens or servers.", 18, k.muted, 400, "start")]
    k.svg("layers", 1100, 540, "Three layers", "The usual shape of a mobile app; lesson 3 looks closer", "".join(b))


for make in (tangled_and_separated, layers):
    make()
print("wrote 2 diagrams")
