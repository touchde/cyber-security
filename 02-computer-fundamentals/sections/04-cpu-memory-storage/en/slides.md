---
title: "How Computers Work — Section 4: The CPU, Memory, and Storage"
videos:
  1: The CPU and How It Works
  2: Memory, Storage, and Volatility
---

<!-- 1.1 -->
<!-- layout: title -->

# The CPU, Memory, and Storage

## Video 1 · The CPU and How It Works

How Computers Work · Section 4

In this video, you will learn:

- What the CPU is, and the fetch–execute cycle
- Registers
- Clock speed, cores, and threads

---

<!-- 1.2 -->

# The CPU and the fetch–execute cycle

The **CPU** (processor) is the part that follows instructions, the "brain" that obeys, not thinks.

It repeats one loop, billions of times a second, the **fetch–execute cycle**:

1. **Fetch** the next instruction from memory.
2. **Decode** what it means.
3. **Execute** it (add, move, compare).
4. Repeat.

A program is a long list of tiny instructions; the CPU marches through them. **Exploits work by changing which instruction it fetches next.**

---

<!-- 1.3 -->

# Registers

The CPU needs somewhere for the few values it's using **right now**: **registers**, tiny, ultra-fast slots built into the processor.

- Fastest memory there is (inside the CPU), but very few, holding a few bytes each.
- A workbench, not a warehouse.

Two to know by name:

- **Program counter:** holds the address of the **next instruction**. Change it → change what runs next (the goal of many exploits).
- **Stack pointer:** tracks the top of the stack (lesson 6).

---

<!-- 1.4 -->

# Clock speed, cores, and threads

- **Clock speed (GHz):** cycles per second. 3 GHz = 3 billion ticks/sec, a little work each tick.
- **Cores:** complete processors on one chip. Quad-core = 4 CPUs = 4 things **truly** at once.
- **Threads:** separate streams of instructions the OS schedules onto cores (lesson 6).

A modern computer does many things **truly** at once (per core) and more **apparently** at once (switching fast). Reasoning about thread order is hard → **race conditions**.

---

<!-- 1.5 -->
<!-- layout: recap -->

# Recap: the CPU

- The CPU repeats **fetch → decode → execute**, billions of times a second.
- **Registers** are tiny ultra-fast slots; the program counter picks the next instruction.
- **Cores** do parallel work; **clock speed** is work per tick.

**Next video:** where the bytes live, memory, storage, and volatility.

---

<!-- 2.1 -->
<!-- layout: title -->

# The CPU, Memory, and Storage

## Video 2 · Memory, Storage, and Volatility

How Computers Work · Section 4

In this video, you will learn:

- RAM vs storage
- The memory hierarchy and cache
- Why "volatile" matters for forensics

---

<!-- 2.2 -->

# RAM vs storage

The running program and its data live in **RAM** (memory); files live in **storage** (disk).

| | RAM | Storage (SSD/HDD) |
|---|---|---|
| Speed | **Fast** | Slower |
| Keeps data without power? | **No (volatile)** | **Yes (persistent)** |

- Open a file → copied from storage into RAM to work on.
- **Save** → written back to storage.

That's why unsaved work vanishes on a power cut: it was in **volatile** RAM.

---

<!-- 2.3 -->
<!-- layout: table -->

# The memory hierarchy

Faster memory is smaller and pricier; larger is slower. So computers layer them:

| Level | Speed | Size | Survives power off? |
|---|---|---|---|
| Registers | Fastest | Dozens of slots | No |
| **Cache** | Very fast | A few MB | No |
| RAM | Fast | GB | No |
| Storage | Slow | GB–TB | **Yes** |

**Cache** holds recently/soon-needed data near the CPU, avoiding the slow trip to RAM.

---

<!-- 2.4 -->
<!-- layout: warning -->

# Why "volatile" matters

- **RAM is volatile:** holds live secrets, open files, decrypted data, typed passwords, **keys**, but is **erased when power is cut**.
- **Storage is persistent:** survives power-off, but live secrets may exist **only in RAM**.

**Order of volatility:** in a live investigation, capture the most volatile evidence **first**, RAM before disk.

A laptop seized running, with an encrypted disk: the **key is in RAM**. Pull the plug → key gone → disk unreadable. **Capture RAM first.**

---

<!-- 2.5 -->
<!-- layout: recap -->

# Recap: memory and storage

- **RAM:** fast, holds the running program, **volatile**. **Storage:** slower, **persistent**.
- Memory hierarchy: registers → cache → RAM → storage; cache speeds up RAM.
- **Capture volatile memory (RAM) first** in a live investigation, it holds the keys.

**Next lesson:** the software that manages all this hardware, the operating system.
