# Lesson Brief (How Computers Work)

The standard instructions for writing a lesson in this course.

**Read first:**

1. [`STYLE-GUIDE.md`](../../STYLE-GUIDE.md): lesson structure, rules for book/slides/script, Writing Khmer, the no-storyline rule, and the code rules.
2. The teaching style in the [production plan](production-plan.md#teaching-style).
3. [`GLOSSARY.md`](../../GLOSSARY.md): add every new term you define.
4. The lesson's topics in the [lesson plan](section-plan.md) and the [outline](outline.md).
5. The [sources](sources.md). Record the exact tool and version behind any command output.
6. A finished lesson, for format only: Security Fundamentals [`sections/01-what-cybersecurity-is/`](../../01-security-fundamentals/sections/01-what-cybersecurity-is/). Do not copy its wording.

## Writing the English

Produce `en/book.md`, `en/slides.md`, `en/script.md` in `02-computer-fundamentals/sections/<lesson>/`, and `examples/` when the lesson has code or commands. Slides title: `"How Computers Work — Section N: <Lesson name>"`. Khmer: `"How Computers Work — ផ្នែកទី N៖ <name>"`.

**Content**

- No running story. Each lesson stands alone. Define every term on first use; assume no programming.
- Breadth over depth: name and frame each idea, and point forward to the later course that goes deep (Linux 03, Windows 05, Reverse Engineering 17, Binary Exploitation 18, Forensics 28, etc.).
- When an idea can be shown with a real command, show the command and its real output.

**Code and commands**

- `examples/` holds the runnable material. **C** programs (lessons 8, 11) are compiled with Clang and must run; ```` ```c ```` blocks before "Common Mistakes" are complete programs with real ```` ```text ```` output. ```` ```c-wrong ```` shows an unsafe example (for example an overflow) and is not run.
- **Shell commands** and their output go in ```` ```console ```` blocks, copied from a real run on our own machine or lab. Name the tool and version in `sources.md`.
- Hex, ASCII, Unicode, and Base64 values must be exact and real, from actual tool output.
- Everything is for understanding and defending; nothing targets a system you do not own.

**Slides and script**

- Follow the shared structure. Put a blank line between **Show**, **Say**, **Do**, and **Time** in the script.

## Writing the Khmer

After the English is reviewed, produce `km/book.md`, `km/slides.md`, `km/script.md` in natural Khmer, technical terms in English, no transliteration. Name the mistakes section `## កំហុសដែលជួបញឹកញាប់`.

## Before You Finish

```sh
python3 tools/check_lesson.py 02-computer-fundamentals/sections/<lesson>
python3 tools/check_overlap.py 02-computer-fundamentals/sections/<lesson>
python3 tools/build_lessons.py computer-fundamentals <lesson>
```

(The build needs `computer-fundamentals` registered in `tools/course_themes.py` with the circuit theme; do that in milestone 0, like Security Fundamentals.)
