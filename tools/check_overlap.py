"""List sentences in a lesson that repeat, or nearly repeat, a sentence in another course.

Each course explains things in its own words, so run this after writing a lesson's English.

    python3 tools/check_overlap.py 21-c-cpp/sections/01-how-computers-work

Fixed labels and shared facts may stay the same; rewrite everything else that it lists.
"""
import difflib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COURSES = ("01-dart", "03-swift", "21-c-cpp")
NAMES = re.compile(r"\b(dart|swift|c\+\+|c)\b")
FIXED = ("in this video, you will learn", "your output should look like this", "for about 5 seconds", "we are not endorsed",
         "write your own version before", "time is a planning estimate")


def sentences(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    found = []
    for line in text.splitlines():
        if line.startswith(("|", "<!--", "#", "title:")):
            continue
        line = re.sub(r"[*`>]", "", line).strip("- ").strip()
        # Fixed wording that every course shares is not a repeat: the prerequisites label and the "(section N in this book)" pointer.
        if line.strip() == "You should already be able to:":
            continue
        line = re.sub(r"\s*\(sections? [\d, and]+ in this book\)", "", line)
        found += [s.strip() for s in re.split(r"(?<=[.!?។])\s+", line) if len(s.split()) >= 6]
    return found


def normal(sentence):
    return NAMES.sub("X", sentence.lower())


lesson = pathlib.Path(sys.argv[1]).resolve()
own = lesson.relative_to(ROOT).parts[0]
known = {}
for course in COURSES:
    if course != own:
        for f in (ROOT / course / "sections").glob("*/en/*.md"):
            for s in sentences(f.read_text()):
                known[normal(s)] = f"{course}: {s}"
keys = list(known)
count = 0
for f in sorted(lesson.glob("en/*.md")):
    for s in sentences(f.read_text()):
        n = normal(s)
        if any(label in n for label in FIXED):
            continue
        match = n if n in known else next(iter(difflib.get_close_matches(n, keys, n=1, cutoff=0.82)), None)
        if match:
            count += 1
            print(f"{f.name}: {s}\n    {known[match]}")
print(f"{count} repeated sentence(s)")
