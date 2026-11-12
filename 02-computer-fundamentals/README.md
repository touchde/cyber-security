# How Computers Work

What happens inside a computer: binary and hex, encodings, CPU and memory, operating systems, processes, files, and how programs run.

**Path:** Foundations
**Before this course:** Security Fundamentals.

**Status:** planning done; **all 12 lessons written in English**, and **built to PDF**, lesson books, slide decks, and the 102-page full book, in [`output/02-computer-fundamentals/`](../output/02-computer-fundamentals/). Next: your review, then the Khmer versions. See the [task breakdown](planning/tasks.md).

Build any time (needs Google Chrome):

```sh
python3 tools/build_lessons.py computer-fundamentals            # all 12 lessons
python3 tools/build_lessons.py computer-fundamentals --book     # the full book
```

## Planning

- [Outline](planning/outline.md): the full table of contents, by chapter
- [Lesson plan](planning/section-plan.md): the 12 lessons, parts, and size
- [Production plan](planning/production-plan.md): teaching style, milestones, decisions, and risks
- [Task breakdown](planning/tasks.md): the next steps, in order
- [Lesson brief](planning/lesson-brief.md): the instructions for writing a lesson
- [Slide design](planning/slide-design.md): this course's "circuit" look and diagrams
- [Sources](planning/sources.md): main references

This course has **no storyline** (topic-driven, each lesson stands alone) and **some hands-on code and commands** (a little C, and shell commands), unlike Security Fundamentals. The [full book](book/) compiles all 12 sections into one PDF.

## Lessons

Each lesson has an English book chapter, slides, and a video script in `sections/<lesson>/en/`.

| # | Lesson | Status |
|---:|---|---|
| 1 | [What a Computer Does](sections/01-what-a-computer-does/) | ✅ English written |
| 2 | [Binary, Hexadecimal, and Bits](sections/02-binary-hex-and-bits/) | ✅ English written |
| 3 | [Representing Text: ASCII, Unicode, and Base64](sections/03-text-encoding/) | ✅ English written |
| 4 | [The CPU, Memory, and Storage](sections/04-cpu-memory-storage/) | ✅ English written |
| 5 | [What an Operating System Does](sections/05-operating-system/) | ✅ English written |
| 6 | [Processes, Threads, and Memory](sections/06-processes-threads-memory/) | ✅ English written |
| 7 | [Files and File Systems](sections/07-files-and-file-systems/) | ✅ English written |
| 8 | [How Programs Are Built and Run](sections/08-how-programs-are-built/) | ✅ English written |
| 9 | [The Boot Process](sections/09-boot-process/) | ✅ English written |
| 10 | [Virtual Machines and Containers](sections/10-virtual-machines-and-containers/) | ✅ English written |
| 11 | [A First Look at C and Memory](sections/11-c-and-memory/) | ✅ English written |
| 12 | [Explore a Running System](sections/12-explore-a-running-system/) | ✅ English written |
