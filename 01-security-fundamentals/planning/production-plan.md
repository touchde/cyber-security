# Security Fundamentals — Production Plan

How we make this course: a book, slides, and video scripts for each lesson, in English and Khmer, plus one full book at the end. The lesson format is the shared one in [`STYLE-GUIDE.md`](../../STYLE-GUIDE.md). The look and examples are this course's own. The lessons are in the [lesson plan](section-plan.md).

**The learner:** a complete beginner. No security, programming, or networking background. Many will be students or career-changers in Cambodia.

**Content first:** we write every lesson before recording videos. Claude writes each lesson, one at a time, with no agents unless you ask.

## Teaching Style

- **Topic-driven, no running story.** Each lesson stands alone. Use concrete, realistic examples to explain, but never make a lesson depend on an earlier lesson's narrative. A reader who knows a topic can skip it.
- **Plain language.** This is the first course; assume nothing. Define every term the first time it appears, and add it to the [glossary](../../GLOSSARY.md).
- **Concepts before tools.** This course builds the mental model. The hands-on tools come in the Foundations courses that follow.
- **Ethics first, from lesson 1.** The rule "only test what you own or have written permission to test" appears in lesson 1 and gets its own lesson (9).
- **No fear, no hype.** Explain real risks plainly. No scare tactics, no "unhackable" claims.
- **Honest about change.** Security advice and frameworks change. Cite sources with dates (see [sources](sources.md)).

## What Is Different in a Fundamentals Course

| Topic | What it means for the lessons |
|---|---|
| **No prerequisites** | Nothing may assume Linux, code, or networking. Where an example needs a term, define it or defer it to its own course. |
| **Mostly no code** | Lessons 5 and 6 may show a tiny hashing example to make an idea concrete; everything else is prose, tables, and diagrams. |
| **Breadth over depth** | This course names and frames every big idea. Depth is the job of later courses, which this course points to. |
| **Standardized content** | Fundamentals are well-settled. Follow the mainstream (NIST, CIS, OWASP); do not invent private definitions. |

## Milestones

| Milestone | Lessons | Notes |
|---:|---|---|
| 0 | — | **Get ready:** outline, lesson plan, this plan, design, sources, lesson brief, and the shared style guide and glossary. **In progress** |
| 1 | 1 | **Pilot:** lesson 1 in English, reviewed. Sets the real format and size. |
| 2 | 2–3 | The CIA triad, and risk |
| 3 | 4–5 | Attackers and attacks |
| 4 | 6–8 | Passwords, access control, controls |
| 5 | 9–12 | Ethics, frameworks, roles, roadmap |
| 6 | — | Khmer versions, then read the whole course and build the full book |

## Decisions

| Decision | Answer |
|---|---|
| Storyline | **None.** Topic-driven; standalone lessons (see teaching style) |
| Framework base | NIST CSF 2.0, CIS Controls, OWASP, MITRE ATT&CK, cited with dates |
| Scenario names | Neutral placeholders ("Acme Co.") when a company helps; local money and places where useful |
| Look | Deep blue and amber "blueprint" theme: see the [design](slide-design.md) |

## Risks

| Risk | How we handle it |
|---|---|
| Assuming knowledge the learner lacks | Define every term; defer tools to their own course |
| Content going stale | Cite frameworks and figures with dates; re-check before publishing |
| Drifting into private definitions | Follow mainstream sources; link them |
| Ethics treated as a footnote | Ethics in lesson 1 and a full lesson (9); the rule repeats in every attack course |
