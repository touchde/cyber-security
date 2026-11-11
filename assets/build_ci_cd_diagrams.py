"""Generate the CI/CD course's diagrams, in its slate and lime palette, into assets/diagrams/.

    python3 assets/build_ci_cd_diagrams.py

They are written to diagrams/11-ci-cd/.
"""
from diagram_kit import OUT, Kit

k = Kit(folder="11-ci-cd", primary="#2F5573", tint="#EEF4F8", ink="#16212B", muted="#536373", line="#D3DEE7",
        sans="'Archivo', 'Helvetica Neue', Arial, sans-serif", mono="'Ubuntu Mono', Menlo, monospace", accent="#4E8A2A")
LIME = "#ECFADF"


def pipeline():
    stages = [("Push", "git push", k.tint), ("Checkout", "get the code", "#FFFFFF"), ("Build", "pub get, compile", "#FFFFFF"),
              ("Check", "format, analyze", "#FFFFFF"), ("Test", "dart test", "#FFFFFF"), ("Result", "green or red", LIME)]
    b = []
    for i, (name, sub, fill) in enumerate(stages):
        x = 30 + i * 178
        b.append(k.node(x, 160, 146, 104, name, sub, fill, "#4E8A2A" if fill == LIME else None))
        if i:
            b.append(k.arrow(x - 30, 212, x - 2, 212))
        if 1 <= i <= 4:
            b.append(k.step(x + 75, 290, i))
    b += [k.text(30, 370, "Each numbered step runs on a fresh machine, called a runner, in the order shown.", 19, k.ink, 700, "start"),
          k.text(30, 400, "If one step fails, the steps after it do not run, and the result is red.", 18, k.muted, 400, "start"),
          k.text(30, 455, "The team sees the result on the commit and on the pull request, within minutes.", 18, k.muted, 400, "start")]
    k.svg("push-to-result", 1100, 500, "A pipeline, from push to result", "What happens every time someone pushes a change", "".join(b))


def ci_cd_cd():
    rows = [("Continuous integration", "Every change is built and tested, many times a day", ["Merge", "Build", "Test"], 0),
            ("Continuous delivery", "Every passing change could be released; a person presses the button", ["Merge", "Build", "Test", "Package", "Release?"], 1),
            ("Continuous deployment", "Every passing change is released automatically", ["Merge", "Build", "Test", "Package", "Release"], 2)]
    b = []
    for title, sub, steps, r in rows:
        y = 130 + r * 140
        b += [k.text(40, y, title, 22, k.primary, 700, "start"), k.text(40, y + 26, sub, 17, k.muted, 400, "start")]
        for i, s in enumerate(steps):
            x = 40 + i * 205
            human = s.endswith("?")
            b.append(k.node(x, y + 42, 175, 56, s, None, LIME if s.startswith("Release") else "#FFFFFF", "#4E8A2A" if s.startswith("Release") else None))
            if i:
                b.append(k.arrow(x - 28, y + 70, x - 2, y + 70))
            if human:
                b.append(k.text(x + 87, y + 120, "a person decides", 16, k.muted))
    k.svg("integration-delivery-deployment", 1100, 560, "Integration, delivery, and deployment", "Three steps of automation; most mobile teams stop at delivery", "".join(b))


for make in (pipeline, ci_cd_cd):
    make()
print("wrote 2 diagrams")
