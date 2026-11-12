# How Computers Work — Production Plan

How we make this course: a book, slides, and video scripts for each lesson, in English and Khmer, plus one full book at the end. The lesson format is the shared one in [`STYLE-GUIDE.md`](../../STYLE-GUIDE.md). The look and examples are this course's own. The lessons are in the [lesson plan](section-plan.md).

**The learner:** someone who has finished Security Fundamentals (course 01). No programming or computer-internals background. Many will be students or career-changers in Cambodia.

**Content first:** we write every lesson before recording videos. Claude writes each lesson, one at a time, with no agents unless you ask.

## Teaching Style

- **Topic-driven, no running story.** Each lesson stands alone. Use concrete, realistic examples to explain, but never make a lesson depend on an earlier lesson's narrative.
- **Show it on a real machine.** Where an idea can be seen with a command (a hex dump, a process list, a boot log), show the real command and its real output. Reading a command is taught; mastery of the shell is the Linux course (03).
- **Build the ladder for later courses.** This course quietly lays the ground for the hard ones: the stack and buffers (→ Binary Exploitation), executables (→ Reverse Engineering, Malware Analysis), volatile memory and deleted files (→ Forensics), processes and the kernel (→ everything). Plant the seed, name the later course, keep it light here.
- **From zero, every time.** A beginner course. Define every term on first use; add it to the [glossary](../../GLOSSARY.md). Assume no math beyond arithmetic.
- **No fear, no hype.** Explain clearly and plainly.

## What Is Different in This Course

| Topic | What it means for the lessons |
|---|---|
| **Some real code and commands** | Lessons 2–3, 5–9, 11–12 show commands or small programs. Each `examples/` sample must run and show real output (shared checker rules). |
| **C appears early** | Lessons 8 and 11 use tiny C programs, compiled with Clang. C is introduced from zero; it is used to *see* memory, not to teach full C (that is course 21, in mobile-development, and not required here). |
| **Cross-platform ideas** | Concepts are general (CPU, OS, files); where a command is OS-specific, prefer Linux/macOS, and note the Windows equivalent. The dedicated OS courses are 03 (Linux) and 05 (Windows). |
| **Hex and encoding accuracy** | Hex dumps, ASCII, Unicode, and Base64 must be exact and real, copied from actual tool output. |

## Milestones

| Milestone | Lessons | Notes |
|---:|---|---|
| 0 | — | **Get ready:** outline, lesson plan, this plan, design, sources, lesson brief. Shared `tools/` and `assets/` already exist. **In progress** |
| 1 | 1 | **Pilot:** lesson 1 in English, reviewed. Sets the real format and size. |
| 2 | 2–3 | Numbers and text (hex, encoding) |
| 3 | 4–7 | The machine (CPU, OS, processes, files) |
| 4 | 8–10 | Programs, boot, virtualization |
| 5 | 11–12 | C and memory, and the project |
| 6 | — | Khmer versions, then read the whole course and build the full book |

## Decisions

| Decision | Answer |
|---|---|
| Storyline | **None.** Topic-driven; standalone lessons |
| How much code | Minimal and always explained; C only to *see* memory, not to teach C fully |
| Command platform | Linux/macOS first, Windows equivalents noted; the lab proper is course 08 |
| Look | Charcoal and teal "circuit" theme: see the [design](slide-design.md) |

## Risks

| Risk | How we handle it |
|---|---|
| Overwhelming a beginner with internals | Breadth over depth; one idea per topic; defer deep dives to later courses by name |
| Code scaring off non-programmers | Keep it tiny, explain every line, show the output, and say why it matters |
| OS-specific commands confusing readers | Pick one platform per example, note the other; full shell skills are course 03 |
| Hardware facts going stale | Teach durable concepts, not current product specs |
