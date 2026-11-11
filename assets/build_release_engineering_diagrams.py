"""Generate the Release Engineering course's diagrams, in its navy and red palette, into assets/diagrams/.

    python3 assets/build_release_engineering_diagrams.py

They are written to diagrams/17-release-engineering/.
"""
from diagram_kit import Kit

k = Kit(folder="17-release-engineering", primary="#1C3F73", tint="#F6F1E4", ink="#16202F", muted="#5B6170", line="#E8DFCB",
        sans="'Libre Franklin', 'Helvetica Neue', Arial, sans-serif", mono="'Courier Prime', Menlo, monospace", accent="#C8102E")


def life_of_a_release():
    steps = [("Code ready", "merged, tests green"), ("Build", "versioned, signed"), ("Test", "team and beta testers"),
             ("Store review", "Google and Apple"), ("Rollout", "1% → 100%"), ("Watch", "crashes, ratings")]
    row, bottom = k.steps(steps, 130, (k.tint, None, None, None, None, k.tint))
    b = [row]
    b += [k.text(40, 450, "A broken build stopped at any step before Rollout reaches nobody.", 19, k.ink, 700, "start"),
          k.text(40, 482, "A broken build found during Rollout reaches only the users who already have it.", 18, k.muted, 400, "start"),
          k.text(40, 535, "Once it is on a phone, the only fix is a new release.", 19, "#C8102E", 700, "start")]
    k.svg("life-of-a-release", 1100, 580, "The life of a release", "From merged code to users' phones", "".join(b))


def staged_rollout():
    stages = [(1, 20), (5, 100), (20, 400), (50, 1000), (100, 2000)]
    b = []
    for i, (pct, users) in enumerate(stages):
        x = 60 + i * 200
        h = 40 + pct * 3
        b += [f'<rect x="{x}" y="{460 - h}" width="140" height="{h}" fill="{k.primary if pct < 100 else "#C8102E"}" opacity="{0.35 + i * 0.15}"/>',
              k.text(x + 70, 490, f"{pct}%", 22, k.ink, 700), k.text(x + 70, 518, f"about {users} users", 16, k.muted)]
    b += [k.text(60, 140, "Each step waits a day or more, and moves on only if crashes and ratings look normal.", 19, k.ink, 700, "start"),
          k.text(60, 170, "A problem at 5% hurts about 100 people instead of 2000; the rollout is halted, and a fix follows.", 18, k.muted, 400, "start")]
    k.svg("staged-rollout", 1100, 550, "A staged rollout", "The ordering app's 2000 active users, a few at a time", "".join(b))


for make in (life_of_a_release, staged_rollout):
    make()
print("wrote 2 diagrams")
