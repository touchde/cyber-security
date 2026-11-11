"""Write a course's planning/section-plan.md lesson table from its outline: one lesson per chapter.

    python3 tools/lesson_plan_table.py <course folder> "<title>" "<who it is for>" parts.json

parts.json: {"parts": {"1": "Part 1: Start", ...}, "notes": {"3": "...", ...}, "titles": {"1": "Meet CI/CD"},
             "lesson1": ["topic", ...], "lesson1_note": "...", "per_topic_slides": 2.0}
"""
import json
import pathlib
import re
import sys

folder, title, who, spec = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3], json.loads(pathlib.Path(sys.argv[4]).read_text())
text = (folder / "planning/outline.md").read_text()
chapters = [(c.splitlines()[0].split(": ", 1)[1], len(re.findall(r"^\d+\.", c, re.M))) for c in re.split(r"^## ", text, flags=re.M)[1:]]
rows = []
for i, (name, count) in enumerate(chapters, 1):
    if str(i) in spec["parts"]:
        rows.append(f"| | **{spec['parts'][str(i)]}** | | | |")
    rows.append(f"| {i} | {spec['titles'].get(str(i), name)} | {i} | {count} | {spec['notes'].get(str(i), '')} |")
total = sum(c for _, c in chapters)
per = spec.get("per_topic_slides", 2.0)
topics = "\n".join(f"{n}. {t}" for n, t in enumerate(spec["lesson1"], 1))
(folder / "planning/section-plan.md").write_text(f"""# {title} — Lesson Plan

Each lesson is one chapter of the [outline](outline.md). A lesson that grows too big can split.

**Who it is for:** {who}

| # | Lesson | Chapter | Topics | Notes |
|---:|---|---:|---:|---|
""" + "\n".join(rows) + f"""
| | **Total** | **{len(chapters)} chapters** | **{total}** | |

## Lesson 1 Topics

{topics}

{spec.get("lesson1_note", "")}

## Size Estimate

Lesson 1 sets the real numbers. Until then:

| | Estimate |
|---|---:|
| Lessons | {len(chapters)} (a few more with splits) |
| Slides | ~{round(total * per, -1):.0f} |
| Videos | ~{round(len(chapters) * 4.2):.0f} |
| Video time | ~{round(total * 2.3 / 60):.0f} hours |
""")
print(len(chapters), "chapters,", total, "topics")
