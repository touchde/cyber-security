# Lesson Brief (Security Fundamentals)

The standard instructions for writing a lesson in this course.

**Read first:**

1. [`STYLE-GUIDE.md`](../../STYLE-GUIDE.md): the lesson structure, the rules for book, slides, and script, Writing Khmer, and the no-storyline rule.
2. The teaching style in the [production plan](production-plan.md#teaching-style).
3. [`GLOSSARY.md`](../../GLOSSARY.md): add every new term you define.
4. The lesson's topics in the [lesson plan](section-plan.md) and the [outline](outline.md).
5. The [sources](sources.md). Every figure and legal statement must trace to one, with a date.
6. A finished lesson, for format only: [`sections/01-what-cybersecurity-is/`](../sections/01-what-cybersecurity-is/). Do not copy its wording.

## Writing the English

Produce `en/book.md`, `en/slides.md`, and `en/script.md` in `01-security-fundamentals/sections/<lesson>/`, and `examples/` only if the lesson has code. Slides title: `"Security Fundamentals — Section N: <Lesson name>"`. Khmer title: `"Security Fundamentals — ផ្នែកទី N៖ <name>"`.

**Content**

- No running story. Each lesson stands alone. Use concrete examples, neutral placeholder names ("Acme Co.") where a company helps.
- This is a beginner course. Define every term on first use; assume no programming or networking.
- Breadth over depth: name and frame each idea, and point to the later course that goes deep.
- Every attack described (phishing, malware, cracking) is explained to be defended against, with the ethics rule stated. No step-by-step for harming real systems.
- Figures, breach numbers, and legal statements must cite a dated source. When unsure of current law, describe the shape and say "confirm the current local law", rather than state specifics.

**Code (only lessons 5–6)**

- If a lesson shows code, `examples/` is a small Python package; each top-level `.py` file is a program the checker runs. Learners never get these files.
- Every ```` ```python ```` block before "Common Mistakes" is a complete program with real ```` ```text ```` output. Insecure code uses ```` ```python-wrong ````.
- Secrets, hashes, and personal data in examples are made up.

**Slides and script**

- Follow the shared structure. Put a blank line between **Show**, **Say**, **Do**, and **Time** in the script.

## Writing the Khmer

After the English is reviewed, produce `km/book.md`, `km/slides.md`, and `km/script.md` in natural Khmer, technical terms in English, no transliteration. Name the mistakes section `## កំហុសដែលជួបញឹកញាប់`. Use `tools/fill_km_blocks.py` once the tools are set up.

## Before You Finish

```sh
python3 tools/check_lesson.py 01-security-fundamentals/sections/<lesson>
python3 tools/check_overlap.py 01-security-fundamentals/sections/<lesson>
python3 tools/build_lessons.py security-fundamentals <lesson>
```

(The shared `tools/` are brought over from mobile-development and adapted; until then, check by hand against this brief.)
