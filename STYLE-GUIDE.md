# Style Guide

Shared rules for every topic's section drafts and slides. Each topic's `planning/slide-design.md` adds only what is specific to that topic, such as its logo, code language, and special visuals.

This is still an early direction. Colors, layouts, illustrations, and level of detail can change as the slides are built.

## Lesson Structure

Every section becomes a **lesson** with three outputs: a book chapter, slides, and video scripts.

**Languages:** English is written first; Khmer is translated from the reviewed English. Every lesson has English and Khmer slides and scripts. The videos are **spoken in Khmer**. Code, program output, and screenshots are the same in both languages. Each lesson has a Khmer book chapter too.

```text
<topic>/sections/NN-short-title/
├── examples/          ← runnable code and lab files, shared by both languages
│   ├── 01_first_example.py   (the language depends on the course)
│   └── ...
├── en/
│   ├── book.md        ← written first; the most complete version
│   ├── slides.md      ← cut down from the book
│   └── script.md      ← what the teacher says, slide by slide
└── km/                ← translated from en/ after it is reviewed
    ├── slides.md      ← same slide IDs and code as en/slides.md
    ├── script.md      ← Khmer narration for the videos (needed to record)
    └── book.md        ← the Khmer book chapter, same structure as en/book.md
```

[Security Fundamentals section 1: What Cybersecurity Is](01-security-fundamentals/sections/01-what-cybersecurity-is/) is the reference lesson. Copy its shape for new lessons. Some courses (Fundamentals, GRC, careers) are concept-led and may have no code at all; code-led courses (Python, scripting, web, exploitation) follow the code rules below.

Sections that still have a single `NN-short-title.md` file are older drafts. They become the starting point for that lesson's `en/book.md`.

**Workflow:** write the examples → `en/book.md` → `en/slides.md` → `en/script.md` → review → translate `en/book.md`, `en/slides.md`, and `en/script.md` to `km/` using the [glossary](GLOSSARY.md) → Khmer review → add screenshots → record.

### Rules for All Three

- **The book is the source of truth.** Slides and scripts may leave things out, but must never say something the book does not.
- **`examples/` is private.** Learners get the book and the videos, never the example files. Book and slide text must not mention `examples/` or an example's file name, and every practice solution is printed in the book. Only the teacher's notes in `script.md` (**Show**, **Do**) use the file names. Learners type the code themselves into their own file.
- **Every code example in a book chapter is a complete program or a complete, runnable command:** it has everything it needs to run on its own (for a program, a `main()` or entry point and any imports; for a shell example, the full command), so a learner can type it and run it. Slides may show only the important lines.
- **Every code sample comes from `examples/`** and must pass the course's checker (`tools/check_lesson.py`) and run. Show the real output, copied from a real run. Re-run the examples after any change. Output of security tools goes in ```` ```console ```` blocks, copied from a real run on our own lab. Insecure or vulnerable code shown to be fixed uses the `-wrong` form (for example ```` ```python-wrong ````) and is not run.
- **Write simple English.** It is easier to learn from and to translate. Use short sentences, one idea per sentence, and the same word for the same thing every time. Avoid idioms, jokes that depend on wordplay, and phrasal verbs when a plain verb exists ("start", not "kick off").
- **No running storyline.** Unlike the mobile-development repository, these courses are topic-driven, like a standard security reference. Each lesson stands on its own, so a reader who already knows a topic can skip it without losing a thread. Use **concrete, realistic examples** to make an idea clear (a named sample company, a specific command, a real tool's output), but do not carry one narrative across lessons, and never make understanding a lesson depend on an earlier lesson's story. Where a scenario company helps, a neutral placeholder such as "Acme Co." is fine; keep money and places local (riel, Cambodia) where that aids the reader.
- **Explain each technical term the first time it appears,** and add it to the [glossary](GLOSSARY.md).
- **Code is the same in both languages.** Identifiers, strings, and output stay in English. Only explanations are translated.
- **Ethics in every attack lesson.** Any lesson that shows an attack states, near the top, that attacks are tried only on systems we own or have written permission to test (our own example code, or the home-lab from course 08). Every key, password, token, and personal detail in an example is made up and looks made up. No lesson is a ready-to-use weapon: we teach how attacks work and how to defend, never a deployable tool aimed at real systems.

### Book Chapter (`book.md`)

For self-study and later reference. Each numbered topic follows the same pattern:

1. **Why:** what problem this solves, in one or two sentences.
2. **Code:** a short example from `examples/`.
3. **Output:** the real output, in a `text` block.
4. **How it works:** a few bullets that walk through the code.

The chapter starts with *What you will learn* and *Before you start*, and ends with **Common mistakes** (using the real compiler messages), a **Summary** table, **Check your understanding** questions with answers, and a **Practice** exercise with a solution in `examples/`.

### Slides (`slides.md`)

**Every slide must be understandable on its own.** The videos are narrated in Khmer and the slides are in English, so a learner who reads only the slide must still understand the idea. A heading and a few keywords is not enough.

Every content slide has at least:

1. **A plain explanation:** 1–3 full sentences that say what the idea is, written for someone who has never seen it. Define every new term in the slide where it first appears.
2. **Why it matters:** the problem it solves, in one sentence. An everyday comparison helps (a function is like the "Latte" button on a coffee machine).
3. **An example:** code with its real output, or a table. The code must show everything needed to understand the output.
4. **Key points:** 2–4 bullets written as **full short sentences**, not fragments. "`void` means the function gives nothing back," not "`void` = nothing".

Title slides list what the video teaches. Recap slides repeat the key points as full sentences and say what comes next.

Other rules:

- Slides are separated by `---`. Each slide starts with an ID comment, `<!-- 2.3 -->`, meaning video 2, slide 3. Scripts use the same IDs.
- One idea per slide. If a slide needs more than about 14 lines of code, or more than four key points, split it into two slides.
- Suggest a layout with a comment, such as `<!-- layout: two-column — code left, explanation right -->`.
- Group slides into videos of 5–10 minutes. Each video starts with a title slide and ends with a recap slide.
- Mark visuals that still need to be made with `<!-- VISUAL TODO: ... -->` and screenshots with `SCREENSHOT TODO` (see [App Screenshots](#app-screenshots)).
- The format is plain Markdown, so it can be turned into slides with Marp, Slidev, or by hand in Keynote.

### Video Script (`script.md`)

One `##` heading per video, and one block per slide, using the slide ID:

```markdown
### 1.2 — Declare and call a function

**Show:** slide 1.2, then switch to VS Code with `01_declare_and_call.dart`

**Say:** Spoken words, written the way a teacher talks: short sentences, "you" and "we".

**Do:** Run the file. Point at the two lines of output.

**Time:** about 1:00
```

- Put a blank line between **Show**, **Say**, **Do**, and **Time**. Without it, Markdown joins them into one paragraph.
- Write the **Say** part to be spoken, not read. Do not repeat the slide word for word; explain it.
- English speech is about 130–150 words per minute. Use that to estimate **Time**.
- Every video ends by telling learners what comes next.

### Writing Khmer (`km/slides.md`, `km/script.md`, `km/book.md`)

Write the way Cambodian developers and IT teachers actually talk and write. **Explain the meaning in natural Khmer. Do not translate word for word, and do not invent Khmer words for technical terms.**

- **Technical terms stay in English:** function, parameter, argument, return, variable, type, scope, closure, and so on. Do not transliterate them (not ប៉ារ៉ាម៉ែត្រ, អាគុយម៉ង់) and do not coin Khmer replacements (not បោះតម្លៃត្រឡប់). The [glossary](GLOSSARY.md) lists each term with a short Khmer explanation to use the first time it appears.
- **Everyday words are in Khmer** when that is how people normally say them: កូដ, កម្មវិធី, តម្លៃ, លទ្ធផល, ប្រកាស (declare), ហៅ (call).
- **Translate the meaning, not the sentence.** Read the English slide, then write how you would explain it to a Khmer student. Sentences can be shorter, combined, or reordered.
- Example. English: "A function is a group of instructions that has a name."
  - Too literal: Function គឺជាក្រុមនៃបញ្ជាដែលមានឈ្មោះ។
  - Natural: **Function** គឺជាប្លុកនៃកូដសម្រាប់អនុវត្តការងារជាក់លាក់ណាមួយ។
- Keep the **same structure** as the English file: the same slide IDs, headings in the same order, and the same tables.
- **Code and output blocks are copied unchanged**, including the English comments. `tools/check_lesson.py` checks the Khmer files too.
- Use the Khmer font **Google Sans** (in [`assets/fonts/google-sans/`](assets/fonts/google-sans/)) for Khmer text, and JetBrains Mono for code. Khmer text needs more line height; if a slide is crowded, shorten the wording, but keep every key point.

### Khmer Video Script (`km/script.md`)

The learner sees the slides and code while hearing Khmer, so the narration must connect the two.

- Translate only the **Say** parts. Keep the slide IDs, **Show**, **Do**, and **Time** lines in English so they match the slides and files exactly.
- Write it the way a teacher talks to a class: relaxed, clear, natural spoken Khmer, not formal written Khmer.
- Say technical terms and code names in English (`addPrices`, `void`, `required`), exactly as they appear on screen.
- Khmer speech may be longer or shorter than English. Re-estimate **Time** after a practice read.

## Overall Feel

- Friendly and approachable, with occasional programming humor.
- Clear enough for someone new to the topic to follow.
- Modern, with generous whitespace and readable text.

## Code Examples

- Show code in the dark navy panel from [`assets/templates/code-panel.svg`](assets/templates/code-panel.svg): square corners, subtle window controls, and bright syntax colors on a clean background.
- Use JetBrains Mono for code and the `code` syntax colors in [`assets/theme/tokens.json`](assets/theme/tokens.json).
- Keep examples short enough to understand at a glance. Highlight the relevant lines when useful.
- Pair code with a plain-language explanation, and show expected output or a small result where that helps.
- Use the small colored circles at the top of a panel as an occasional visual cue, not on every slide.

## Branding and Images

- Use only the official logos in [`assets/logos/`](assets/logos/). Each brand's usage rules and credit lines are in the [logos README](assets/logos/README.md). Never use the Apple logo or other Apple icons.
- Use the topic's logo on the cover or section-opening slides, and possibly on the final slide. Pick the `-light-bg` or `-dark-bg` version to match the slide background.
- Keep logos at their original proportions and colors. Do not stretch them or place them behind code.
- **Use square corners** on panels, callouts, and diagram boxes. Do not round them.
- Put the author and date on every book cover and on the title slide of every video: *By TOUCH DEN · November 2, 2026*. In Khmer, the name is written in Khmer: *រៀបរៀងដោយ ទូច ដែន · ថ្ងៃទី ២ ខែវិច្ឆិកា ឆ្នាំ ២០២៦*.
- End every deck with a credits slide that includes the trademark credit lines required for each logo used in it.
- Add illustrations, diagrams, or screenshots when they make a concept easier to understand. Prefer visuals that explain over generic decoration. Start from [`assets/diagrams/`](assets/diagrams/) and use the [Material Symbols icons](assets/icons/material-symbols/).
- Show phone screenshots as they are, without a device frame.

## App Screenshots

Screenshots are captured by hand from our own example code, never taken from the internet. Where a lesson needs one, put a note on its own line in the book and on the slide, with the file name first:

```markdown
<!-- SCREENSHOT TODO: file: xcode-new-project-options.png; Device: Mac, Xcode 26; Show: the "Choose options for your new project" sheet filled in as in the table. Crop to the sheet; no Team or personal name visible. -->
```

- Until the picture exists, the build draws a dashed placeholder box in its place, in the book and on its own slide, with what to show and where to save it. A phone, simulator, or emulator gets a tall box; everything else a wide one.
- Save the picture as `assets/screenshots/<course folder>/<file>`, for example `assets/screenshots/04-ios-development/xcode-new-project-options.png`, and build again: the picture replaces the box. The note can stay.
- `tools/check_lesson.py` lists every screenshot that is still missing, with its path.
- Crop out anything private: account and machine names, private paths, the menu bar, and the Dock.

- Use light humor, a playful mascot, or funny code-related images occasionally so they stay memorable.

## Content on Each Slide

A slide might include a short explanation, a code example, a diagram or image, a quick output or result, or a practice prompt. Use only the elements the topic needs.

- Give each slide one main topic.
- Avoid long paragraphs and crowded code examples.
- Include small practice prompts where they help learners apply a concept.
- Use section titles to help learners see where they are in the course.

## Layout and Readability

- Use Inter for headings and text, and the colors in [`assets/theme/tokens.json`](assets/theme/tokens.json).
- Use a light background for most slides, with dark code panels for contrast.
- Use the Note, Tip, Warning, and Practice callouts in [`assets/templates/`](assets/templates/) for asides.
- Keep headings, body text, code, and visuals distinct and readable from a distance.
- Use color consistently to show meaning, such as keywords, important values, or output.
- Vary layouts as needed: code with explanation, comparison, process diagram, or practice prompt.
- Keep spacing and alignment consistent while letting each topic use a suitable layout.

## Open for Later Decisions

- How often to use humor, illustrations, and screenshots
- Whether logos appear only at the start and end or throughout a deck
- Whether section openers use a repeated format
- How much code and practice to include for each topic
- Which tool turns section drafts into slides
