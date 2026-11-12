---
title: "How Computers Work — Section 12: Explore a Running System"
videos:
  1: Who, What, and Which Files
  2: Boot, and Tying It All Together
---

<!-- 1.1 -->
<!-- layout: title -->

# Explore a Running System

## Video 1 · Who, What, and Which Files

How Computers Work · Section 12

In this video, you will learn:

- How to see this whole course on a real machine
- Who you are, and what is running
- How to identify and read files

**Run these on your own computer only. You are looking, not changing.**

---

<!-- 1.2 -->

# The goal: see the ideas for real

You've built a full model of a computer. This lesson makes it **real** with a few commands, the way security people start on an unfamiliar system:

- **Who am I, what can I do?** (lesson 5)
- **What is running?** (lesson 6)
- **What are these files, really?** (lesson 7)
- **How long up, how did it start?** (lessons 4, 9)

Open a terminal on **your own** computer and follow along.

---

<!-- 1.3 -->

# Who am I, and what is running

```console
$ whoami
user
$ ps -o pid,ppid,%cpu,%mem,comm
  PID  PPID %CPU %MEM COMM
 1521     1   0.3  1.8 WindowServer
 2983  2970   1.2  4.1 Google Chrome
 3001  2983   0.0  2.2 Google Chrome Helper
$ ps -e | wc -l
     900
```

- `whoami`: your account, your powers depend on it (lesson 5).
- `ps`: **PID**, **parent**, resources (Helper's parent is Chrome). ~900 processes, all isolated (lesson 6). *(Windows: Task Manager.)*

---

<!-- 1.4 -->

# Identifying and reading files

```console
$ file greet
greet: Mach-O 64-bit executable arm64
$ printf 'Mina\n' | xxd
00000000: 4d69 6e61 0a                             Mina.
```

- `file` reports the **real type** from content, not the name (lessons 7, 8).
- `xxd`: **offset · hex · text** (lesson 2). `4d`=M, `69`=i, `6e`=n, `61`=a, `0a`=newline.
- `strings` pulls readable text from a program (lesson 8), a first analysis step.

---

<!-- 1.5 -->
<!-- layout: recap -->

# Recap: who, what, files

- `whoami` → who you are and your powers (lesson 5).
- `ps` → what's running, with parents and resources (lesson 6).
- `file` + `xxd` → a file's real type and its raw bytes (lessons 2, 7, 8).

**Next video:** boot, and tying the whole course together.

---

<!-- 2.1 -->
<!-- layout: title -->

# Explore a Running System

## Video 2 · Boot, and Tying It All Together

How Computers Work · Section 12

In this video, you will learn:

- How long since boot
- How five commands map to the whole course
- Where you go next

---

<!-- 2.2 -->

# How long up, and how it started

```console
$ uptime
22:32  up 6 days, 23:47, 1 user, load averages: 1.31 1.43 1.70
```

- **"up 6 days":** the boot chain (firmware → bootloader → kernel → init) finished almost a week ago (lesson 9).
- Every process traces back through **init (PID 1)** to that boot.
- "1 user" is you (lesson 5); load averages hint at CPU busyness (lesson 4).

The system also keeps **logs**, where investigators build a timeline (forensics).

---

<!-- 2.3 -->
<!-- layout: table -->

# Five commands, the whole course

| Command | What you saw | Lesson |
|---|---|---|
| `whoami` / `id` | Who you are; privileges | 5 |
| `ps` | Running processes | 6 |
| `file` | A file's real type | 7, 8 |
| `xxd` | Raw bytes: offset, hex, text | 2, 3 |
| `uptime` | Time since boot | 4, 9 |

This is the **real starting posture** of SOC triage, incident response, forensics, and reversing.

---

<!-- 2.4 -->

# A computer is not magic

You've proven it to yourself: every concept, bits, encoding, CPU, OS, processes, memory, files, programs, boot, virtualization, is **real, visible, inspectable** with simple tools.

That demystified, confident view of the machine is the **true deliverable** of this course.

**Where next:** Linux (03) turns these into real skill; Networking (04) adds how machines talk; then the paths open, offensive, defensive, engineering.

---

<!-- 2.5 -->
<!-- layout: recap -->

# Recap: you understand the machine

- Five simple commands reveal the **whole stack** this course taught.
- It's how security work **actually begins**: who, what, which files, how it started.
- A computer is **inspectable, not magic**, that's the real deliverable.
- Carry the habit: meet a new system, **look at it**, and connect what you see to how computers work.

**You've finished How Computers Work. You understand the machine. Everything ahead builds on this.**
