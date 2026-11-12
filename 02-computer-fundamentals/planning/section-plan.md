# How Computers Work — Lesson Plan

Each lesson is one chapter of the [outline](outline.md). This course is concept-led with **a little hands-on code and commands**: reading a hex dump, decoding Base64, listing processes, and one tiny C program. Everything is explained from zero. A lesson that grows too big can split.

**Who it is for:** someone who has finished Security Fundamentals (course 01). No programming, no computer-internals background.

| # | Lesson | Chapter | Topics | Code / commands |
|---:|---|---:|---:|---|
| | **Part 1: Numbers and Text** | | | |
| 1 | What a Computer Does | 1 | 7 | None |
| 2 | Binary, Hexadecimal, and Bits | 2 | 8 | A little (hex, bitwise) |
| 3 | Representing Text: ASCII, Unicode, and Base64 | 3 | 8 | A little (Base64, encoding) |
| | **Part 2: The Machine** | | | |
| 4 | The CPU, Memory, and Storage | 4 | 7 | None |
| 5 | What an Operating System Does | 5 | 7 | A little (system calls demo) |
| 6 | Processes, Threads, and Memory | 6 | 7 | Commands (list processes) |
| 7 | Files and File Systems | 7 | 7 | Commands (files, magic bytes) |
| | **Part 3: Programs and Boot** | | | |
| 8 | How Programs Are Built and Run | 8 | 7 | A little (compile a program) |
| 9 | The Boot Process | 9 | 7 | Commands (boot logs) |
| 10 | Virtual Machines and Containers | 10 | 6 | None (concept; lab is course 08) |
| | **Part 4: Memory, Up Close** | | | |
| 11 | A First Look at C and Memory | 11 | 7 | Yes (small C programs) |
| 12 | Practical Project: Explore a Running System | 12 | 5 | Commands (put it together) |
| | **Total** | **12 chapters** | **83** | |

## Note on Code

Where a lesson shows code or commands, the examples live in `examples/` and must run and show real output, checked the way the shared [style guide](../../STYLE-GUIDE.md) describes. Languages used: a little **C** (lessons 8 and 11, compiled with Clang), small **shell commands** (lessons 3, 6, 7, 9, 12), and the occasional **Python** one-liner (lesson 2–3). All are introduced from zero; this is still a beginner course. Reading and running a command is taught here; deep command-line skill is the Linux course (03).

## Size Estimate

Lesson 1 sets the real numbers. Until then, rough:

| | Estimate |
|---|---:|
| Lessons | 12 |
| Slides | ~190 |
| Videos | ~40 |
| Video time | ~3 hours |
