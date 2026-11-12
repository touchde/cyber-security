# How Computers Work — Task Breakdown

Status: ⬜ not started · 🔄 in progress · ✅ done. **Stop** means wait for your review before going on.

## Milestone 0 — Get Ready

| ID | Status | Task |
|---|---|---|
| 0.1 | ✅ | Outline (12 chapters), lesson plan, production plan, slide design, sources, lesson brief |
| 0.2 | ✅ | Registered `computer-fundamentals` in `tools/course_themes.py` with the circuit theme (charcoal + teal, Space Grotesk + Space Mono, `circuit_motif`); course mark generated; cover built |
| 0.3 | ✅ | Confirmed the toolchain on this Mac (Clang, `xxd`, `base64`, `file`, `ps`, `uptime`); all C examples compile and run |

## Milestone 1 — All English Lessons

| ID | Status | Task | Done when |
|---|---|---|---|
| 1.1 | ✅ | **All 12 lessons, English.** Each has `en/book.md`, `en/slides.md`, `en/script.md`; code lessons (8, 11) have runnable `examples/`; command output is real, from this machine | Build passes, 0 slides overflow (verified) |
| 1.2 | ✅ | **Full-book files:** `book/README.md`, `book/how-to-use.en.md`, `book/references.en.md` | Drafted |
| 1.3 | ✅ | **PDFs built:** 12 lesson books + 12 slide decks + the 102-page full book, in `output/02-computer-fundamentals/` | Build passes; PDFs present |
| 1.4 | ⬜ | **Your review of the outline and the 12 English lessons. Stop** | Your changes are made |
| 1.5 | ⬜ | **All 12 lessons in Khmer**, after the English review | Checker and build pass |

## Notes

- **This course has code**, unlike Security Fundamentals: small C programs (lessons 8, 11, in `examples/`) and shell commands (lessons 2, 3, 6, 7, 9, 12). Command output is shown in ```` ```console ```` blocks, copied from real runs on this machine; C output is from compiled, run examples.
- **No storyline.** Topic-driven; each lesson stands alone.
- Later milestones are in the [production plan](production-plan.md#milestones).
