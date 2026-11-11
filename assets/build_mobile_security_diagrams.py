"""Generate the Mobile Security course's diagrams, in its crimson palette, into assets/diagrams/.

    python3 assets/build_mobile_security_diagrams.py

They are written to diagrams/14-mobile-security/.
"""
from diagram_kit import Kit

k = Kit(folder="14-mobile-security", primary="#A3123A", tint="#FCF0F3", ink="#1D0E12", muted="#64505A", line="#F0D2D9",
        sans="'Barlow', 'Helvetica Neue', Arial, sans-serif", mono="'Overpass Mono', Menlo, monospace", accent="#A3123A")
SAFE = "#EAF4EE"


def attacker_controls():
    b = [k.text(40, 135, "On the attacker's phone: they control all of this", 21, k.primary, 700, "start"),
         k.box(40, 150, 600, 330, k.tint, k.primary, 2.5)]
    items = ["the app file: read every string and every line of logic", "the app's memory while it runs",
             "every request before it is sent", "every response before the app sees it", "the device itself, even the system"]
    for i, s in enumerate(items):
        b.append(k.text(70, 200 + i * 56, "• " + s, 19, k.ink, 400, "start"))
    b += [k.text(690, 135, "On your server: only you control this", 21, "#2E7D4F", 700, "start"),
          k.box(690, 150, 370, 330, SAFE, "#2E7D4F", 2.5)]
    for i, s in enumerate(["secret keys", "the record of every sale", "the rules for points", "who may do what"]):
        b.append(k.text(720, 210 + i * 62, "• " + s, 19, k.ink, 400, "start"))
    b.append(k.text(550, 525, "Anything that must stay secret or be trusted belongs on the right.", 19, k.ink, 700))
    k.svg("attacker-controls", 1100, 560, "What the attacker controls", "Your app runs on a device you do not own", "".join(b))


def where_trust_lives():
    b = [k.text(40, 130, "Trusting the app", 21, k.primary, 700, "start"),
         k.node(40, 150, 300, 90, "App", "asks: add 5000 points", k.tint), k.node(620, 150, 300, 90, "Server", "adds 5000 points", "#FFFFFF"),
         k.arrow(340, 195, 618, 195), k.text(480, 270, "The server believes whatever the app says.", 17, k.primary, 700),
         k.text(40, 340, "Letting the server decide", 21, "#2E7D4F", 700, "start"),
         k.node(40, 360, 300, 90, "App", "says: I paid for sale-1042", k.tint), k.node(620, 360, 300, 90, "Server", "looks up the sale: 8800", SAFE, "#2E7D4F"),
         k.arrow(340, 405, 618, 405), k.text(770, 485, "8800 riel → 8 points", 19, "#2E7D4F", 700),
         k.text(480, 530, "The app asks; the server checks its own records and decides.", 17, k.muted)]
    k.svg("where-trust-lives", 1100, 560, "Where trust lives", "The same request, designed two ways", "".join(b))


for make in (attacker_controls, where_trust_lives):
    make()
print("wrote 2 diagrams")
