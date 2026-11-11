# Security Fundamentals — Task Breakdown

Status: ⬜ not started · 🔄 in progress · ✅ done. **Stop** means wait for your review before going on.

## Milestone 0 — Get Ready

| ID | Status | Task |
|---|---|---|
| 0.1 | ✅ | Outline (12 chapters), lesson plan, production plan, slide design, sources, lesson brief |
| 0.2 | ✅ | Shared repo files: `STYLE-GUIDE.md` (adapted, no-storyline), `GLOSSARY.md` (seed); `tools/` and `assets/` brought over from mobile-development |
| 0.3 | ✅ | Course mark (`assets/icons/courses/security-fundamentals.svg`) and the blueprint theme registered in `tools/course_themes.py` |

## Milestone 1 — All English Lessons

| ID | Status | Task | Done when |
|---|---|---|---|
| 1.1 | ✅ | **All 12 lessons, English, topic-first (no storyline).** Each has `en/book.md`, `en/slides.md`, `en/script.md`; slide and script IDs match across every lesson; no `examples/` leaks; ~29k words of book text | Checks pass (verified) |
| 1.2 | ✅ | **Full-book files:** `book/README.md`, `book/how-to-use.en.md`, `book/references.en.md` | Drafted |
| 1.3 | ⬜ | **Your review of the outline and the 12 English lessons. Stop** | Your changes are made |
| 1.4 | ✅ | **Build tooling ported and adapted:** `tools/` and `assets/` (minus other courses' cover art) brought over; `security-fundamentals` registered in `tools/course_themes.py` with the blueprint theme (Inter + JetBrains Mono, navy/amber, `blueprint_motif`); course mark generated | `build_lessons.py` runs |
| 1.5 | ✅ | **PDFs built:** all 12 lesson book + slide PDFs, and the 104-page full book, in `output/01-security-fundamentals/`. 0 slides overflow | Build passes; PDFs present |
| 1.6 | ⬜ | **Optional diagrams** (blueprint style): three questions; defense-in-depth layers; CIA+AAA; risk; attack lifecycle; auth factors; NIST CSF functions. Lessons read fine without them | They render clearly |
| 1.7 | ⬜ | **All 12 lessons in Khmer**, after the English review, then rebuild (book-km, slides-km, full book-km) | Checker and build pass |

## Notes

- **No code in these lessons.** Fundamentals is concept-led, so no `examples/` folders were created. The section plan's note about a small hashing demo in lessons 5–6 was dropped: hashing is described in prose, and runnable code waits for the Cryptography and Python courses, where the checker can verify it.
- **Lesson 1 history:** it was first drafted around a running "Monday at Mina Coffee" story, then rewritten topic-first after the no-storyline decision. The ransomware incident is now a one-off illustration in topic 1; later topics and lessons use their own standalone examples. It is the reference lesson others copy for format.
- **Pending shared infrastructure:** `assets/` (diagram builders, theme, course mark) and `tools/` (checker, builder) still need to be brought over from mobile-development and adapted before diagrams and PDFs can be produced.

Later milestones are in the [production plan](production-plan.md#milestones).
