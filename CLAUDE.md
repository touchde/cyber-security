# CLAUDE.md

Guidance for Claude Code when working in this repository. Sibling repo `../mobile-development` uses the same tooling and an equivalent CLAUDE.md; this one captures what is different here.

## What This Repository Is

Teaching material, not an app: **43 courses** on cyber security, from fundamentals through offensive, defensive, engineering, and specialized/career tracks (see `README.md` for the full list, learning paths, and per-course status). Each **lesson** produces a **book chapter, slides, and video scripts**. English is written first; Khmer is translated from the reviewed English. Shared writing/slide rules are in `STYLE-GUIDE.md`; Khmer terms in `GLOSSARY.md`.

**Key difference from mobile-development: there is NO running storyline.** These courses are topic-driven, like a standard security reference. Each lesson stands alone, so a reader who already knows a topic can skip it. Use concrete, varied examples (a dental clinic's assets, a bank balance, "Acme Co."), never one narrative carried across lessons.

## Status (keep current)

- **01 Security Fundamentals** — all 12 lessons written (en) + built. Concept-led, no code.
- **02 How Computers Work** — all 12 lessons written (en) + built. Has C and shell examples.
- **03 Linux for Security** — in progress (planning done; lessons being written). Has shell commands.
- Courses 04–43: draft lesson lists only (in each `README.md`).
- Khmer versions: not started for any course yet.

## Layout

```text
NN-course/
├── README.md       scope, path, before-this-course, status, lesson table
├── planning/       outline.md (chapters), section-plan.md (chapters → lessons),
│                   production-plan.md, slide-design.md, sources.md, lesson-brief.md, tasks.md
│                   (NO storyline.md — this repo has no storyline)
├── book/           full-book front matter: README.md, how-to-use.en.md, references.en.md
└── sections/NN-lesson/
    ├── examples/   runnable code/scripts the book quotes (private: never named in book or slides)
    ├── en/         book.md, slides.md, script.md
    └── km/         same three files, translated (later)
tools/              check_lesson.py, check_overlap.py, build_lessons.py, course_themes.py (+ others)
assets/             fonts, icons, theme, templates, build_course_icons.py, diagram_kit.py,
                    build_<slug>_diagrams.py (per course), diagrams/<folder>/*.svg, logos/
                    (mobile mascots/diagrams/brand logos were pruned; assets/photos/ Cambodian
                     landmarks ARE kept — they are the cover photos. Keep it lean otherwise.)
output/             built PDFs, committed (output/<course>/<lesson>/ and output/<course>/<slug>/)
```

## Commands (run from repo root; Google Chrome required for builds)

```bash
# Build one lesson's PDFs (course key = the slug registered in course_themes.py)
python3 tools/build_lessons.py security-fundamentals 01-what-cybersecurity-is
python3 tools/build_lessons.py computer-fundamentals            # all written lessons in a course
python3 tools/build_lessons.py linux --book                     # the full book (run alone)
python3 tools/build_lessons.py linux --cover                    # cover image only (regenerate: delete the cached PNGs first)

# Check a lesson (runs/compiles examples, compares Output blocks, checks en/km structure)
python3 tools/check_lesson.py 02-computer-fundamentals/sections/11-c-and-memory

# Generate the course marks (after editing assets/build_course_icons.py)
python3 assets/build_course_icons.py
```

- Course keys registered so far in `tools/course_themes.py`: `security-fundamentals`, `computer-fundamentals`, `linux`. Each has its own look (see below).
- To force a cover rebuild, `rm` the cached `assets/covers/patterns/<slug>-cover-background.png` and `assets/covers/{en,km}/<folder>-cover.png` first.

## Starting a NEW course (the repeated setup)

1. **Planning files** in `NN-course/planning/`: `outline.md`, `section-plan.md`, `production-plan.md`, `slide-design.md`, `sources.md`, `lesson-brief.md`, `tasks.md`. Copy the shape from course 02 or 03. No `storyline.md`.
2. **Course mark:** add a row to `COURSES` in `assets/build_course_icons.py` → `(material-symbol-name, tile-color, corner-color)`; run it.
3. **Theme:** add an entry to `COURSES` in `tools/course_themes.py` (model on the `linux`/`computer-fundamentals` entries): `folder`, `code` (syntax lang, or `"text"`/`"bash"`), `name`, `slug`, the icon paths, `credit`, a `cover` (style `motif`, with its own `_motif(w,h,mm)` function and an `art` PNG path), `theme(...)`, `fonts`+`font_faces` (a NEW pair not used by another course), `slide_css`, `book_css`, and `text(...)`. Give each course its own distinct look and font pair.
4. Build the cover (`--cover`), read the PNG, fix title size / motif collisions with the byline.
5. Update the course `README.md` (status + planning links) and the root `README.md` progress row.

Registered looks: 01 blueprint (navy/amber, Inter+JetBrains Mono) · 02 circuit (charcoal/teal, Space Grotesk+Space Mono) · 03 terminal (near-black/green, Work Sans+Fira Code).

## Cover and logo rules

These differ from mobile-development (no Cambodian-heritage photos here). Keep them consistent across courses.

**Covers — like mobile-development: a light page + big logo + a Cambodian landmark PHOTO at the bottom, toned to the course color** (the author chose this over procedural motifs):
- Add the course to `PHOTO_COVERS` in `tools/course_themes.py`: `"<key>": (photo-filename, credit, caption, object-position)`. Photos live in `assets/photos/` (copied from mobile — Angkor temples etc.); captions use `heritage(en, km, (d,m,y), intangible?)` or `place(en, km, city_en, city_km)`. `apply_covers()` then builds a light cover from the course's `theme` colors (page = the accent mixed with white; the photo is toned to the accent). So the cover automatically matches each course's palette.
- The **big logo** on the cover is the course's `icon` (set in the theme entry): the real product logo for product courses (Linux→`assets/logos/linux/linux.svg`), or the Material-Symbols course mark for concept courses (Security Fundamentals→shield). Its `credit` line carries the trademark notice.
- Each course still has its own `theme(...)` palette + font pair (for slides/books). The old `_motif` functions and `cover: {style:"motif", …}` fields are now **unused** for the cover (apply_covers overrides them) — fine to leave or clean up.
- Build with `python3 tools/build_lessons.py <key> --cover`; to force a redraw, delete the cached `assets/covers/{en,km}/<folder>-cover.png` and `assets/covers/art/<folder>-cover-art.png` first. **Always Read the rendered PNG**: title fits, big logo visible, photo toned to the course color, caption + `TOUCH DEN` byline at the bottom, square corners.
- Course→photo so far: 01 Angkor Wat (navy) · 02 Bayon (teal) · 03 Ta Prohm (green). Assign a distinct Angkor/Cambodian landmark per new course; `assets/photos/README.md` has the credits.

**Logos — use REAL product logos, like mobile-development** (this is the author's explicit preference — do NOT default to a generic course mark):
- If a course is about a specific product/tool, its cover mark and in-book visuals use that product's **real logo**: Linux → **Tux** (`assets/logos/linux/tux-badge.svg` on the cover, `tux.svg` inline); and similarly Ubuntu, Kali, Docker, Kubernetes, AWS/Azure/GCP, Wireshark, Burp Suite, Metasploit, Python, Git, etc. for the courses about them. Set the theme entry's `icon`/`logo_dark`/`logo_light` to that logo. On a dark cover, put a dark logo on a light tile (square corners) so it is visible — see `tux-badge.svg`.
- Prefer the **official artwork** where its licence allows nominative use in teaching material; a clean SVG recreation is acceptable when the official file isn't to hand (the author can ask for exact artwork). Add the trademark credit to the course's `credit` line (e.g. "Linux is a registered trademark of Linus Torvalds; Tux by Larry Ewing").
- **Course mark (Material Symbols on a tile, via `build_course_icons.py`) is the FALLBACK**, only for concept courses with no single product (Security Fundamentals, GRC, Threat Intelligence…). Even those should use relevant real tool logos/images inside the lessons.
- Embed inline logos small and secondary (`<img … width="110" align="right">`); real screenshots/diagrams carry the teaching. Square corners everywhere; don't stretch or recolor a logo. Keep `assets/logos/` lean.
- See `assets/logos/README.md` for the per-course logo list.

## Writing rules (what the tools don't catch)

- **No storyline. Each lesson stands alone.** Never make understanding a lesson depend on an earlier lesson's example. Pointers forward to other courses by name are fine and encouraged ("studied in the Binary Exploitation course").
- **Ethics in every attack lesson:** state near the top that attacks are only tried on systems you own or have written permission to test (own code, or the course-08 home lab). Every key/password/token/personal detail is made up. No lesson is a ready-to-use weapon.
- **All command/code output is REAL.** Shell output goes in ```` ```console ```` blocks copied from real runs on this Mac; for Linux-specific tools (`apt`, `systemctl`, `journalctl`, `ufw`) use real Ubuntu-format output and standardize the prompt `dara@ubuntu:~$`. C examples compile and run (clang). Never hand-write output. Addresses change per run (ASLR) — say so.
- **Code examples** before "Common Mistakes" are complete programs from `examples/`; `-wrong` fences (```` ```c-wrong ````) show a bug and are not run/checked.
- **Never name `examples/` or a file name** in book or slides; only script **Show:/Do:** lines may.
- **Lesson shape:** `# Section N: Title`, a `>` outline-chapter line, What You Will Learn, Before You Start, `---`, numbered `## N.` topics, `---`, Common Mistakes (bold numbered), Summary (table), Check Your Understanding (+ **Answers**), Practice (+ worked example/solution). Slides: front matter `title`+`videos`, `---`-separated, each `<!-- V.S -->`, title/recap/table/warning layouts; verify slide IDs match the script. Script: `### V.S — Title` with **Show/Say/Do/Time**, blank lines between.
- **Security framing throughout:** tie each concept to attack/defense and name the later course that goes deep.
- **Use diagrams and images, not walls of text.** Each course has `assets/build_<slug>_diagrams.py` (uses `assets/diagram_kit.py`) generating SVGs into `assets/diagrams/<folder>/`; embed them with `![alt](../../../../assets/diagrams/<folder>/<name>.svg)`, and small logos (e.g. `assets/logos/linux/tux.svg`) with `<img … width="110" align="right">`. Always Chrome-screenshot a new diagram and look at it before using it (collisions, crossing lines). Courses 01–02 were written text-only and still need a diagram retrofit.
- **No subagents unless asked.** Commit/push only when asked; author as the user, **no Claude co-author line** (the user has required this).

See `.claude/skills/write-course-lesson/SKILL.md` for the full per-lesson workflow.
