"""Fill a Khmer template with the exact code and output blocks of the English file.

Write the Khmer with a line that is only @@ wherever a fenced block goes, then:

    python3 tools/fill_km_blocks.py en/book.md template.md km/book.md

Code and output are copied, so they cannot differ from the English.
"""
import pathlib
import re
import sys

en, template, out = map(pathlib.Path, sys.argv[1:4])
blocks = re.findall(r"^```[\w-]+\n.*?^```$", en.read_text(), re.M | re.S)
lines = template.read_text().split("\n")
markers = sum(1 for line in lines if line == "@@")
if markers != len(blocks):
    raise SystemExit(f"{template.name}: {markers} markers, but {en} has {len(blocks)} blocks")
remaining = iter(blocks)
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(next(remaining) if line == "@@" else line for line in lines))
print(f"wrote {out} with {markers} blocks")
