# Linux for Security — Production Plan

How we make this course: a book, slides, and video scripts for each lesson, in English and Khmer, plus one full book. The lesson format is the shared one in [`STYLE-GUIDE.md`](../../STYLE-GUIDE.md). The look and examples are this course's own. The lessons are in the [lesson plan](section-plan.md).

**The learner:** finished Security Fundamentals (01) and How Computers Work (02). No Linux or command-line background. Many are students or career-changers in Cambodia.

**Content first:** we write every lesson before recording videos. Claude writes each lesson, one at a time, with no agents unless you ask.

## Teaching Style

- **Topic-driven, no running story.** Each lesson stands alone. Use concrete examples; never depend on an earlier lesson's narrative.
- **Hands-on, always.** This is a *doing* course. Nearly every topic shows a real command and its real output, and the learner runs it in their own VM. Reading about the shell is useless; using it is the point.
- **Type it yourself.** Learners type each command into their own machine. The book prints every command and its real output; the practice has them run commands and read the result.
- **From zero.** Assume no command line at all. Explain every command, every flag, the first time. Add terms to the [glossary](../../GLOSSARY.md).
- **Security framing throughout.** Each Linux skill is tied to why it matters for attack or defense: permissions to least privilege, processes to finding malware, logs to detection, SSH to remote attacks, hardening to defense.
- **Safe by construction.** Everything happens in the learner's own VM (lesson 2), satisfying the "only test what you own" rule. Snapshots make mistakes free to undo.

## What Is Different in This Course

| Topic | What it means for the lessons |
|---|---|
| **Every lesson has commands** | `examples/` holds command transcripts and any scripts. Portable commands are run for real; Linux-specific ones are shown in real Ubuntu form. |
| **The environment is a VM** | Lesson 2 sets up Ubuntu in VirtualBox/UTM (building on How Computers Work's virtualization lesson). The lab proper is course 08; this is a single practice VM. |
| **Real output matters** | Command output in ```` ```console ```` blocks is copied from real runs. Prompts, usernames, and paths are consistent (`dara@ubuntu:~$`). |
| **Destructive commands** | Commands like `rm` and `chmod` can break things. Every dangerous command carries a warning, and snapshots are stressed. |

## Milestones

| Milestone | Lessons | Notes |
|---:|---|---|
| 0 | — | **Get ready:** outline, lesson plan, this plan, design, sources, lesson brief; register the terminal theme; course mark. **In progress** |
| 1 | 1 | **Pilot:** lesson 1 in English, reviewed |
| 2 | 2–4 | Getting in: install, shell, files |
| 3 | 5–7 | Users, processes, packages |
| 4 | 8–10 | Text tools, networking, logs |
| 5 | 11–13 | SSH, hardening, the project |
| 6 | — | Khmer versions, then read the whole course and build the full book |

## Decisions

| Decision | Answer |
|---|---|
| Storyline | **None.** Topic-driven; standalone lessons |
| Distribution | **Ubuntu** for most lessons (common, friendly); Kali introduced in lesson 1/2 as the attacker distro used later |
| Example account | `dara` on host `ubuntu`, so prompts read `dara@ubuntu:~$` |
| Command output | Real; portable commands run on Unix, Linux-only commands shown in real Ubuntu form |
| Look | Near-black "terminal" theme with a green prompt accent: see the [design](slide-design.md) |

## Risks

| Risk | How we handle it |
|---|---|
| Overwhelming a beginner with commands | One idea per topic; explain every flag; show the output; tie to security |
| Learners breaking their system | Warn on destructive commands; stress snapshots (lesson 2) |
| Command output drifting from reality | Copy from real runs; keep prompt/username/paths consistent |
| Distro differences confusing readers | Standardize on Ubuntu; note where other distros differ only when it matters |
