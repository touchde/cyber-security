"""Generate the Developer Workflow course's diagrams, in its violet and gold palette, into assets/diagrams/.

    python3 assets/build_developer_workflow_diagrams.py

They are written to diagrams/20-developer-workflow/.
"""
from diagram_kit import Kit

k = Kit(folder="20-developer-workflow", primary="#5B3FC4", tint="#F4F0FF", ink="#1A1726", muted="#5C5670", line="#DDD5F7",
        sans="'Karla', 'Helvetica Neue', Arial, sans-serif", mono="'Fragment Mono', Menlo, monospace", accent="#5B3FC4")
GOLD = "#D99A06"


def branch_and_merge():
    b = [f'<line x1="80" y1="330" x2="1020" y2="330" stroke="{k.primary}" stroke-width="4"/>',
         f'<path d="M260,330 C300,230 340,220 400,220 L640,220 C700,220 740,300 780,330" fill="none" stroke="{GOLD}" stroke-width="4"/>']
    for x, label in ((140, "docs: add a README"), (780, "Merge fix/member-discount")):
        b += [f'<circle cx="{x}" cy="330" r="16" fill="#FFFFFF" stroke="{k.primary}" stroke-width="4"/>', k.text(x, 380, label, 17, k.ink, 700)]
    b += [f'<circle cx="520" cy="220" r="16" fill="{GOLD}"/>', k.text(520, 180, "fix: members get 20% off, not 10%", 17, GOLD, 700),
          k.text(80, 300, "main", 20, k.primary, 700, "start"), k.text(400, 255, "fix/member-discount", 18, GOLD, 700, "start"),
          k.text(80, 460, "A branch lets Vanna work without changing main. A merge brings her finished work back.", 19, k.ink, 700, "start"),
          k.text(80, 492, "Everyone else keeps working on main the whole time.", 18, k.muted, 400, "start")]
    k.svg("branch-and-merge", 1100, 530, "A branch and a merge", "Vanna's fix, from her branch back into main", "".join(b))


def path_of_a_change():
    steps = [("Branch", "fix/member-discount"), ("Commits", "small, clear messages"), ("Pull request", "describe the change"),
             ("Checks", "format, analyze, test"), ("Review", "a teammate reads it"), ("Merge", "into main")]
    row, bottom = k.steps(steps, 130, (None, None, k.tint, None, k.tint, None))
    b = [row]
    b += [k.text(40, 450, "Machines check what machines can check. People check what only people can see:", 19, k.ink, 700, "start"),
          k.text(40, 482, "is it the right change, is it clear, and will the next person understand it?", 18, k.muted, 400, "start")]
    k.svg("path-of-a-change", 1100, 525, "The path of a change", "From Vanna's laptop to the team's main branch", "".join(b))


for make in (branch_and_merge, path_of_a_change):
    make()
print("wrote 2 diagrams")
