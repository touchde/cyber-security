"""Fill the video table at the top of a script: replaces the line TABLE_PLACEHOLDER, and the
"N videos." opening with the total time. Run after writing or changing a script.

    python3 tools/script_table.py 02-flutter/sections/01-meet-flutter/en/script.md
"""
import re
import sys
import pathlib

p = pathlib.Path(sys.argv[1])
t = p.read_text()
rows = ["| Video | Title | Slides | Spoken words | Length with demos |", "|---|---|---|---|---|"]
total = 0
for part in re.split(r"(?=^## Video )", t, flags=re.M)[1:]:
    n, title = re.match(r"## Video (\d+) — (.+)", part).groups()
    ids = re.findall(r"^### (\d+\.\d+)", part, re.M)
    words = sum(len(s.split()) for s in re.findall(r"\*\*Say:\*\*(.*?)(?=\n\*\*Time|\n\*\*Do)", part, re.S))
    secs = sum(int(a) * 60 + int(b) for a, b in re.findall(r"\*\*Time:\*\* about (\d+):(\d+)", part))
    total += secs
    rows.append(f"| {n} | {title} | {ids[0]}–{ids[-1]} | about {round(words, -1)} | about {round(secs / 60)} min |")
table = "\n".join(rows)
t = re.sub(r"^TABLE_PLACEHOLDER$|^\| Video \| Title .*?(?=\n\n)", lambda m: table, t, count=1, flags=re.M | re.S)
t = re.sub(r"^(\w+) videos(?:, about \d+ minutes in total)?\.", lambda m: f"{m.group(1)} videos, about {round(total / 60)} minutes in total.", t, count=1, flags=re.M)
p.write_text(t)
print(table)
