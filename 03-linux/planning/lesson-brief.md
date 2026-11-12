# Lesson Brief (Linux for Security)

The standard instructions for writing a lesson in this course.

**Read first:**

1. [`STYLE-GUIDE.md`](../../STYLE-GUIDE.md): lesson structure, rules for book/slides/script, Writing Khmer, the no-storyline rule, and the code rules.
2. The teaching style in the [production plan](production-plan.md#teaching-style).
3. [`GLOSSARY.md`](../../GLOSSARY.md): add every new term and command you introduce.
4. The lesson's topics in the [lesson plan](section-plan.md) and the [outline](outline.md).
5. The [sources](sources.md). Record the exact distribution and versions behind command output.
6. A finished lesson, for format only: How Computers Work [`sections/01-what-a-computer-does/`](../../02-computer-fundamentals/sections/01-what-a-computer-does/), or any command-led lesson there (e.g. `06-processes-threads-memory`). Do not copy wording.

## Writing the English

Produce `en/book.md`, `en/slides.md`, `en/script.md` in `03-linux/sections/<lesson>/`, and `examples/` for command transcripts or scripts. Slides title: `"Linux for Security — Section N: <Lesson name>"`. Khmer: `"Linux for Security — ផ្នែកទី N៖ <name>"`.

**Content**

- No running story. Each lesson stands alone. Define every command and flag on first use; assume no command-line background.
- Tie every skill to security: permissions → least privilege, processes → finding malware, logs → detection, SSH → remote attack/defense, hardening → defense.
- Point forward to the courses that go deep (SOC 25, Incident Response 27, Pentesting 13, Network Defense 22).

**Commands and output**

- Show commands and their output in ```` ```console ```` blocks, with the standard prompt `dara@ubuntu:~$`, copied from real runs. Portable commands (`ls`, `grep`, `chmod`, pipes) are run for real; Linux-specific commands (`apt`, `systemctl`, `journalctl`, `ufw`) are shown in their real Ubuntu form.
- Any script in `examples/` (e.g. a shell script) must run. A ```` ```bash ```` block that is a complete script comes from `examples/`.
- **Warn on destructive commands** (`rm`, `chmod`, `dd`, config edits). Remind learners to snapshot their VM (lesson 2).
- Everything runs in the learner's own VM; nothing targets a system they do not own.

**Slides and script**

- Follow the shared structure. Put a blank line between **Show**, **Say**, **Do**, and **Time** in the script. In **Do**, name the command to run on screen.

## Writing the Khmer

After the English is reviewed, produce `km/book.md`, `km/slides.md`, `km/script.md` in natural Khmer, technical terms and command names in English, no transliteration. Name the mistakes section `## កំហុសដែលជួបញឹកញាប់`.

## Before You Finish

```sh
python3 tools/check_lesson.py 03-linux/sections/<lesson>
python3 tools/check_overlap.py 03-linux/sections/<lesson>
python3 tools/build_lessons.py linux <lesson>
```

(The build needs `linux` registered in `tools/course_themes.py` with the terminal theme; done in milestone 0.)
