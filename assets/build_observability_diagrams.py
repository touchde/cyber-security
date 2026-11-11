"""Generate the Observability course's diagrams, in its green palette, into assets/diagrams/.

    python3 assets/build_observability_diagrams.py

They are written to diagrams/15-observability-monitoring/.
"""
from diagram_kit import Kit

k = Kit(folder="15-observability-monitoring", primary="#4F6B00", tint="#F3F8E6", ink="#141A10", muted="#55604A", line="#DDE7C4",
        sans="'Work Sans', 'Helvetica Neue', Arial, sans-serif", mono="'Martian Mono', Menlo, monospace", accent="#4F6B00")


def signals():
    rows = [("Logs", "what happened, step by step", "address_parse_failed, field: address"),
            ("Metrics", "numbers counted over time", "crash-free users: 75%"),
            ("Traces", "how long each step of one action took", "tap 'Deliver' → server → map: 2.9 s"),
            ("Crashes", "where and how the app died", "stack trace, device, version")]
    b = []
    for i, (name, sub, example) in enumerate(rows):
        y = 125 + i * 105
        b += [k.node(40, y, 380, 85, name, sub, k.tint if i % 2 == 0 else "#FFFFFF"), k.text(460, y + 50, example, 18, k.ink, 400, "start", True)]
    b.append(k.text(40, 565, "Together they answer questions you did not know you would need to ask.", 19, k.ink, 700, "start"))
    k.svg("signals", 1100, 600, "The signals", "Four kinds of data an app can send home", "".join(b))


def phone_to_dashboard():
    steps = [("Phones", "the app records signals", k.tint), ("Collection", "a service receives them", "#FFFFFF"),
             ("Storage", "kept, searchable", "#FFFFFF"), ("Dashboards", "alerts and questions", k.tint)]
    b = []
    for i, (name, sub, fill) in enumerate(steps):
        x = 30 + i * 268
        b.append(k.node(x, 160, 240, 110, name, sub, fill))
        if i:
            b.append(k.arrow(x - 26, 215, x - 2, 215))
    b += [k.text(30, 330, "Signals are sent in small batches, when the phone has a connection,", 19, k.ink, 700, "start"),
          k.text(30, 360, "and crashes are sent the next time the app starts.", 18, k.muted, 400, "start"),
          k.text(30, 420, "No names, phone numbers, or exact locations leave the phone.", 19, k.primary, 700, "start")]
    k.svg("phone-to-dashboard", 1100, 460, "From a phone to a dashboard", "How signals travel from users' phones to the team", "".join(b))


for make in (signals, phone_to_dashboard):
    make()
print("wrote 2 diagrams")
