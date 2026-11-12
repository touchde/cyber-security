# Section 12: Explore a Running System — Video Scripts

Two videos, about 7 minutes in total. Slide IDs match [`slides.md`](slides.md). The demos use `whoami`, `ps`, `file`, `xxd`, and `uptime`; run them on your own computer only.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Who, What, and Which Files | 1.1–1.5 | about 3.5 min |
| 2 | Boot, and Tying It All Together | 2.1–2.5 | about 3.5 min |

---

## Video 1 — Who, What, and Which Files

### 1.1 — Title

**Show:** slide 1.1

**Say:** This is the final lesson, and it's a project. Instead of new theory, we use everything you've learned to explore a real, running computer with a few simple commands. One rule first: run these on your own computer only, and remember you're just looking, not changing anything.

**Time:** about 0:25

### 1.2 — The goal: see the ideas for real

**Show:** slide 1.2

**Say:** You've built a complete mental model of a computer: bits, encoding, the CPU, memory, the OS, processes, files, programs, boot, and virtualization. This lesson makes it real, because all of it is visible on the machine in front of you. And this is how security people actually begin with an unfamiliar system. A defender triaging a possibly-compromised machine asks the same basic questions you're about to ask: who am I and what can I do, what's running, what are these files really, and how long has this been up and how did it start. Open a terminal on your own computer and follow along.

**Time:** about 0:45

### 1.3 — Who am I, and what is running

**Show:** slide 1.3

**Say:** Start with the most basic question every attacker and defender asks on a new system: who am I? The `whoami` command shows your user account. This matters because, from lesson 5, what you're allowed to do depends on who you are, a limited user and root see completely different possibilities. Next, what's running? From lesson 6, `ps` lists processes, each with a PID, a parent PPID, and its CPU and memory use. Notice Google Chrome Helper's parent is Google Chrome, the parent–child tree in action. And counting them, a typical machine has hundreds, here about 900 processes, all sharing the CPU through multitasking and each isolated in its own virtual memory. On Windows, Task Manager shows the same thing. This list is where a defender hunts for the abnormal.

**Time:** about 0:55

### 1.4 — Identifying and reading files

**Show:** slide 1.4

**Say:** Now files. First, identify what a file really is by its content, not its name, with `file`, which reads the magic bytes from lesson 7. Here it reports a compiled executable in this machine's Mach-O format, ELF on Linux, PE on Windows, and it would say that even if the file were misleadingly named, which is why defenders trust content over the extension. Then read a file's raw bytes with `xxd`. Every idea from lessons 2 and 3 is here: the offset on the left, the bytes in hex in the middle, 4d is M, 69 is i, 6e is n, 61 is a, 0a is the newline, and the text on the right. You're reading memory the way a reverse engineer or forensic analyst does. And remember from lesson 8, running `strings` on a program pulls the readable text straight out, a first step in analyzing anything unknown.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: `whoami` shows who you are and your powers, `ps` shows what's running with parents and resources, and `file` plus `xxd` show a file's real type and its raw bytes. Three commands, and you've already touched users, processes, files, binary, and encoding. Next, the boot, and how this all ties together into the way security work begins.

**Time:** about 0:25

---

## Video 2 — Boot, and Tying It All Together

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this final video: how long the system has been up, how just five commands map onto the entire course, and where you go from here.

**Time:** about 0:20

### 2.2 — How long up, and how it started

**Show:** slide 2.2

**Say:** From lesson 9, the whole system came to life through the boot chain, firmware, bootloader, kernel, init, desktop, and everything running now descends from that boot. See how long ago it completed with `uptime`. "Up 6 days" means the boot chain finished almost a week ago and the system has run continuously since. Every one of those hundreds of processes traces its ancestry back through init, PID 1, to that boot. The "1 user" is you, and the load averages hint at how busy the CPU has been. If you wanted to go deeper, and you will in the Linux and defensive courses, the system keeps logs of what happened, including at boot, which is where investigators reconstruct a timeline. The point here is the connection: a single uptime line ties back to the entire boot lesson.

**Time:** about 0:50

### 2.3 — Five commands, the whole course

**Show:** slide 2.3

**Say:** Step back and see what you did. With five simple commands you examined a real computer across the whole stack this course taught. `whoami` and `id` showed who you are and your privileges, lesson 5. `ps` showed the running processes, lesson 6. `file` showed a file's real type, lessons 7 and 8. `xxd` showed raw bytes, offset, hex, and text, lessons 2 and 3. And `uptime` showed how long since the boot chain completed, lessons 4 and 9. This isn't a toy exercise; it's the real starting posture of security work. A SOC analyst or incident responder begins triage with exactly these questions. A forensic analyst reads bytes and timestamps the same way. And a reverse engineer or malware analyst uses file, xxd, and strings as their first moves on an unknown program.

**Time:** about 0:55

### 2.4 — A computer is not magic

**Show:** slide 2.4

**Say:** More importantly, you've proven to yourself that a computer is not magic. Every concept from this course, bits, encoding, the CPU, the OS, processes, memory, files, programs, boot, and virtualization, is real, visible, and inspectable with simple tools. That demystified, confident view of the machine is the true deliverable of this course, and the foundation everything ahead is built on. Where do you go next? The Linux course turns these first commands into real command-line skill. The Networking course adds how machines talk. And from there the paths open up: offensive, defensive, engineering.

**Time:** about 0:45

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To close: five simple commands reveal the whole stack this course taught, and it's how security work actually begins, who, what, which files, how it started. A computer is inspectable, not magic, and that's the real deliverable. Whichever path you take next, carry this lesson's habit: when you meet a new system, look at it, and connect what you see to how computers actually work. You've finished How Computers Work. You understand the machine. Everything from here builds on that. Well done, and see you in the next course.

**Time:** about 0:30
