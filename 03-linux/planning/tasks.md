# Linux for Security — Task Breakdown

Status: ⬜ not started · 🔄 in progress · ✅ done. **Stop** means wait for your review before going on.

## Milestone 0 — Get Ready

| ID | Status | Task |
|---|---|---|
| 0.1 | ✅ | Outline (13 chapters), lesson plan, production plan, slide design, sources, lesson brief |
| 0.2 | 🔄 | Register `linux` in `tools/course_themes.py` with the terminal theme (near-black + green, Work Sans + Fira Code, a prompt motif); generate the course mark; build the cover |
| 0.3 | ⬜ | Confirm portable commands run on this machine; standardize the `dara@ubuntu:~$` prompt for all transcripts |

## Milestone 1 — Pilot (Lesson 1)

| ID | Status | Task | Done when |
|---|---|---|---|
| 1.1 | ⬜ | **Lesson 1 English** ("Why Security People Use Linux"): `book.md`, `slides.md`, `script.md`. No commands | Reads standalone; slide/script IDs match; build passes |
| 1.2 | ⬜ | **Your review of the outline and lesson 1 English. Stop** | Your changes are made |
| 1.3 | ⬜ | Lesson 1 in Khmer | Checker and build pass |

## Notes

- **Every lesson from 3 onward has commands.** Command output goes in ```` ```console ```` blocks with the `dara@ubuntu:~$` prompt, copied from real runs (portable commands run for real; Linux-specific ones in real Ubuntu form). Scripts go in `examples/` and must run.
- **No storyline.** Topic-driven; each lesson stands alone.
- **Destructive commands carry warnings**, and snapshots (lesson 2) are stressed throughout.
- Later milestones are in the [production plan](production-plan.md#milestones).
