---
name: write-course-lesson
description: Write, rewrite, fix, review, or build a lesson (book.md, slides.md, script.md, and examples/) in any course of this cyber-security teaching repo, or set up a new course (planning + theme). Use whenever the user says "continue <course>", "do lesson N", "write the next lesson", "complete this course", "start the next course", "rewrite/fix lesson N", "why does the build fail", or asks for book/slide/script changes in a course folder (01-security-fundamentals … 43-capstone-ctf), even if they don't say "lesson". Also use for starting a new course (planning files + theme registration + cover).
---

# Write a Cyber-Security Course Lesson

A lesson is `NN-course/sections/NN-title/` with optional `examples/` (real code/scripts), `en/book.md`, `en/slides.md`, `en/script.md` (and later `km/`). The book is the source of truth; slides are cut from it; the script is what the teacher says per slide. `CLAUDE.md` has the repo facts and commands; this skill is the order of work and the rules that only the author's feedback taught. **Read `CLAUDE.md` first** if not already in context.

## The defining rule of this repo: NO storyline

Unlike mobile-development, these courses are **topic-driven**. Each lesson stands alone. Open each topic with the concept itself and a concrete, *varied* example (a dental clinic, a bank balance, "Acme Co.", a specific command) — never one narrative carried across lessons, never a recurring character, and never "understanding this needs lesson N's example". Pointers *forward* to other courses by name are good ("studied in Binary Exploitation, course 18").

## Before writing a lesson

Read, in this order, only what you need:

1. The course's `planning/section-plan.md` and `outline.md`: the lesson's topic list. Cover every listed topic.
2. `planning/production-plan.md` (teaching style) and `planning/lesson-brief.md`.
3. The previous lesson's `en/` files as the shape to copy (headings, slide layouts, script format). Do **not** copy its sentences.

## Order of work (one lesson)

1. **Examples first (only if the lesson has code/commands).** Write programs/scripts in `examples/` and **run them for real on this Mac** to capture output. C compiles with `clang`; shell commands run in the shell. For Linux-specific tools not on macOS (`apt`, `systemctl`, `journalctl`, `ufw`), use accurate Ubuntu-format output with the standard prompt `dara@ubuntu:~$`. Concept-led courses/lessons (Security Fundamentals, most of GRC) have no `examples/`.
2. **book.md.** `# Section N: Title`; a `>` line naming the outline chapter; `## What You Will Learn`; `## Before You Start` (prerequisite courses/lessons + the ethics note for any attack lesson); `---`; numbered `## N. Topic` each with a concept paragraph (bold new terms) → code/`console` block → real output → "How it works"/bullets; `---`; `## Common Mistakes` (bold numbered); `## Summary` (table); `## Check Your Understanding` (questions then **Answers**); `## Practice` (task then a worked example/solution).
3. **slides.md.** Front matter `title` + `videos`; slides separated by `---`, each starting `<!-- V.S -->`; a `<!-- layout: title -->` per video, content slides, `<!-- layout: table -->`/`<!-- layout: warning -->` where useful, and a `<!-- layout: recap -->` ending each video with **Next video/lesson:**. Every slide must stand on its own (full sentences, not fragments).
4. **script.md.** `# Section N: Title — Video Scripts`, a small table of videos (title, slides, length), then per slide `### V.S — Title` with **Show:**, **Say:** (spoken, "we"/"you"), **Do:** (name the command to run, for command lessons), **Time:** about M:SS — blank lines between each.
5. **Diagrams & images (do not skip — the author asked for visuals, not walls of text).** Each course has an `assets/build_<slug>_diagrams.py` (model on `assets/build_linux_diagrams.py`) using `assets/diagram_kit.py`; it writes SVGs to `assets/diagrams/<folder>/`. Add 1–3 diagrams per lesson for the ideas that are clearer as a picture (a tree, a layout, a pipeline, layers, a flow), render them, **screenshot each via Chrome and look at it** (check for title/label collisions and lines crossing boxes), then embed with `![alt](../../../../assets/diagrams/<folder>/<name>.svg)`. Real product/tool logos (e.g. `assets/logos/linux/tux.svg`) can be embedded small with `<img src="…" width="110" align="right">`. The build (`build_lessons.py`) renders SVG/`<img>` into the PDF.
6. **Verify IDs & leaks** before building:
   ```bash
   cd NN-course/sections/NN-title/en
   diff <(grep -oE '<!-- [0-9]+\.[0-9]+ -->' slides.md | grep -oE '[0-9]+\.[0-9]+') \
        <(grep -oE '^### [0-9]+\.[0-9]+' script.md | grep -oE '[0-9]+\.[0-9]+')   # must match
   grep -nE 'examples/|\.dart' book.md slides.md    # must be empty
   ```
7. **Build:** `python3 tools/build_lessons.py <course-key> <NN-title>` — must report `0 slide(s) do not fit`. If a slide overflows, trim or split it.

## Starting a NEW course

Follow the "Starting a NEW course" section of `CLAUDE.md`: write the 7 planning files (no `storyline.md`), add a course mark to `assets/build_course_icons.py` and run it, register a theme in `tools/course_themes.py` with its **own distinct look and a new font pair** (model on the `linux` entry — needs a `_motif(w,h,mm)` function and an `art` PNG path), build `--cover`, read the PNG and fix any title-overflow or byline/motif collision, then update the course and root READMEs.

## Rules the author has required (and why)

- **No storyline, lessons stand alone** (the author chose this over mobile-development's running story: a reader who knows a topic can skip it).
- **Ethics in every attack lesson:** near the top, "only test systems you own or have written permission to test". All keys/passwords/tokens/personal data are made up. Teach how attacks work and how to defend — never ship a ready-to-use weapon (e.g. no deployable ransomware; show mechanics and defense instead).
- **All output is REAL**, from runs on this Mac (` ```console ` / ` ```text `). Standardize the Linux prompt `dara@ubuntu:~$`. Warn on destructive commands (`rm`, `chmod`, config edits) and remind about VM snapshots. Never hand-write output.
- **Security framing throughout:** tie each concept to attack/defense and name the later course that goes deep.
- **Never name `examples/` or a file name** in book or slides; only script **Show:/Do:** lines may.
- **Each course gets a distinct theme and font pair**; don't reuse another course's palette or fonts.
- **No subagents unless the user asks.** Do the work directly, one lesson at a time.
- **Commit/push only when asked.** Author commits as the user; **never add a Claude author or co-author line** (the user has explicitly required this). The global git identity (Den TOUCH) is already correct; `gh` is authenticated as `touchde`.

## Gotchas

- To regenerate a cover, delete the cached `assets/covers/patterns/<slug>-cover-background.png` and `assets/covers/{en,km}/<folder>-cover.png` first, else `--cover` reuses the old PNG.
- `output/**/*.html` is gitignored but the PDFs are committed.
- Keep `CLAUDE.md`'s Status section and the course/root READMEs updated as courses complete.
- A long word in a cover title overflows — reduce the cover `size` (e.g. 64–76pt) and re-read the PNG.
