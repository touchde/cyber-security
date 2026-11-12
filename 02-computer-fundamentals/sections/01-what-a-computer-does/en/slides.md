---
title: "How Computers Work — Section 1: What a Computer Does"
videos:
  1: What a Computer Is, and Its Four Jobs
  2: Numbers, Instructions, and Why It Matters
---

<!-- 1.1 -->
<!-- layout: title -->

# What a Computer Does

## Video 1 · What a Computer Is, and Its Four Jobs

How Computers Work · Section 1

In this video, you will learn:

- What a computer really is, under the surface
- The four things every computer does
- Hardware versus software

---

<!-- 1.2 -->

# What a computer is

**A computer is a machine that follows a list of instructions, step by step, very fast, to work with information.**

- It does not think or understand. It follows instructions, literally, billions of times a second.
- Everything it seems to "do" is a vast number of tiny, simple steps, done so fast it looks instant.

Two powers: **speed** (billions of steps a second) and **reliability** (exactly what the instructions say).

This is also the security problem: a computer follows *whatever* instructions it is given, **including an attacker's**.

---

<!-- 1.3 -->
<!-- layout: table -->

# The four jobs

Every computer, from a phone to a server, does four things:

| Stage | Means | Example |
|---|---|---|
| **Input** | Information comes in | Typing, a network message, a sensor |
| **Processing** | It works on it, following instructions | Calculating, deciding |
| **Output** | A result goes out | The screen, a reply |
| **Storage** | Kept for later | Saving a file |

When you meet an attack later, ask: **which of the four is it attacking?**

---

<!-- 1.4 -->

# Hardware and software

- **Hardware:** the physical machine, the parts you can touch. Processor, memory, disk, screen.
- **Software:** the instructions, the programs that tell the hardware what to do. An OS, an app, a virus.

**Software is a list of instructions; hardware is the machine that carries them out.**

Three layers: **hardware** at the bottom, the **operating system** managing it (lesson 5), your **apps** on top. Attacks hit every layer, especially the OS in the middle, whoever controls it controls everything above.

---

<!-- 1.5 -->
<!-- layout: recap -->

# Recap: what a computer is

- A computer follows numeric instructions, step by step, very fast, it doesn't "understand".
- The four jobs: **input, processing, output, storage**.
- **Hardware** is the machine; **software** is the instructions; the **OS** sits between.

**Next video:** why everything inside is numbers, and why that matters for security.

---

<!-- 2.1 -->
<!-- layout: title -->

# What a Computer Does

## Video 2 · Numbers, Instructions, and Why It Matters

How Computers Work · Section 1

In this video, you will learn:

- Why everything inside a computer is numbers
- Why instructions and data are stored the same way
- Why security people must understand the machine

---

<!-- 2.2 -->

# Everything inside is numbers

Inside a computer, **everything is numbers**, not just sums.

- A letter of text is a number (lesson 3).
- A color in a photo is numbers. A sound is a list of numbers.
- A program's instructions are numbers (lesson 8).

The computer has no idea what a number "means", the same number could be a letter, a brightness, or an instruction.

And the numbers are stored as huge quantities of **on-or-off switches**, patterns of 1s and 0s (next lesson).

---

<!-- 2.3 -->

# Instructions and data are the same stuff

A computer stores two different things the same way:

- **Data:** the information a program works on (a photo, a message).
- **Instructions:** the steps the program follows (the program itself).

Both are just numbers in the same memory, the **stored-program** idea.

- **Good:** to do something new, you just give it a new program, not a new machine.
- **Dangerous:** a computer can be tricked into treating **data as instructions**, the root of buffer overflows and code injection (later courses).

---

<!-- 2.4 -->
<!-- layout: table -->

# Why security needs the machine

**You cannot secure, attack, or investigate what you do not understand.**

| Security work | Machine knowledge it needs |
|---|---|
| Reverse engineering | Reading a program's instructions |
| Binary exploitation | Bending memory, especially the stack |
| Malware analysis | Executables, processes, the OS |
| Digital forensics | Recovering data from memory and disks |

This course is the trunk; those courses are the branches.

---

<!-- 2.5 -->
<!-- layout: recap -->

# Recap: numbers and why it matters

- Inside a computer, **everything is numbers**, stored as on/off switches.
- Instructions and data share the same memory (**stored-program**): flexible, but attackable.
- Every later security course, reversing, exploitation, forensics, rests on this machine knowledge.

**Next lesson:** the ons and offs themselves, bits, binary, and hexadecimal.
