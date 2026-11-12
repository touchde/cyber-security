# Section 4: The CPU, Memory, and Storage — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | The CPU and How It Works | 1.1–1.5 | about 4 min |
| 2 | Memory, Storage, and Volatility | 2.1–2.5 | about 4 min |

---

## Video 1 — The CPU and How It Works

### 1.1 — Title

**Show:** slide 1.1

**Say:** We've spent three lessons on how information becomes bytes. Now we look at the hardware that works on those bytes. This video is about the CPU, the processor, how it runs instructions, and what the numbers like GHz and cores actually mean.

**Time:** about 0:25

### 1.2 — The CPU and the fetch–execute cycle

**Show:** slide 1.2

**Say:** The CPU, or processor, is the part of the computer that actually follows instructions. It's the brain, though as we said in lesson 1, it doesn't think, it obeys. The CPU works by repeating one simple loop, billions of times a second, called the fetch–execute cycle. Fetch: get the next instruction from memory. Decode: work out what it means. Execute: do it, add two numbers, move some data, compare two values. Then repeat with the next instruction. That's the heartbeat of every computer. A program is just a long list of these tiny instructions in memory, and the CPU marches through them faster than you can imagine. This loop is the foundation of reverse engineering and exploitation: a reverse engineer reads the instructions the CPU fetches, and an exploit works by changing which instruction the CPU fetches next, redirecting that loop to the attacker's own instructions.

**Time:** about 0:55

### 1.3 — Registers

**Show:** slide 1.3

**Say:** The CPU needs somewhere to hold the few values it's working on right now, the two numbers it's adding, the result, a note of which instruction comes next. For that it has registers: a very small number of tiny, extremely fast storage slots built right into the processor. They're the fastest memory in the computer because they're inside the CPU, but there are only a few dozen, each holding a few bytes. A workbench, not a warehouse. Two registers are worth knowing by name. The program counter holds the address of the next instruction to fetch, so if you change it, you change what the CPU does next, which is exactly the goal of many exploits. And the stack pointer tracks the top of the stack, a region of memory we'll meet in lesson 6 and bend in Binary Exploitation.

**Time:** about 0:50

### 1.4 — Clock speed, cores, and threads

**Show:** slide 1.4

**Say:** So how fast is a CPU? Three terms, often blurred in marketing. Clock speed, measured in gigahertz, is how many cycles the CPU ticks per second: a 3 GHz CPU ticks three billion times a second, doing a little work each tick. Cores are complete processors on one chip, so a quad-core CPU is really four CPUs in one, able to genuinely do four things at the same time. And threads are separate streams of instructions that the operating system schedules onto cores; a single core can switch between many threads so fast it looks simultaneous. The headline: a modern computer does many things truly at once, one per core, and many more apparently at once by switching fast. That's why it can run a browser, music, and a download together. And reasoning about the order of events across threads is genuinely hard, which is the root of a bug class called race conditions.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: the CPU repeats fetch, decode, execute, billions of times a second. Registers are tiny ultra-fast slots inside it, and the program counter picks the next instruction. Cores do real parallel work, while clock speed is work per tick. Next, where all the bytes actually live: memory, storage, and a property called volatility that shapes how investigations begin.

**Time:** about 0:25

---

## Video 2 — Memory, Storage, and Volatility

### 2.1 — Title

**Show:** slide 2.1

**Say:** The CPU runs instructions, but where do those instructions and all the data live? In this video: RAM versus storage, the memory hierarchy and cache, and the single most security-relevant idea in this lesson, volatility.

**Time:** about 0:20

### 2.2 — RAM vs storage

**Show:** slide 2.2

**Say:** There are two main places data lives. RAM, which we usually just call memory, is where a running program lives: its instructions and data are loaded into RAM, and the CPU reads and writes it constantly. RAM is fast, but it's volatile, meaning when the power goes off, it's wiped clean. Storage, the disk or SSD, is where files are kept permanently: it's slower than RAM, but it's persistent, it keeps its data with the power off. So using a computer is a constant movement between the two: files live in storage, when you open one it's copied into RAM to work on, and when you save, the changes are written back to storage. That's literally what "save your work" means, copy it from volatile RAM to persistent storage. And it's why you lose unsaved work in a power cut: the document was in RAM, not yet saved to storage.

**Time:** about 0:55

### 2.3 — The memory hierarchy

**Show:** slide 2.3

**Say:** We now have several kinds of memory, and they trade off the same way every time: faster memory is smaller and more expensive, larger memory is slower and cheaper. So computers use several layers at once, the memory hierarchy. At the top, registers, inside the CPU, fastest and tiniest. Then cache, very fast, a few megabytes. Then RAM, fast, gigabytes. Then storage, slow but huge, and the only level that keeps data without power. The new piece here is cache: a small amount of very fast memory in or near the CPU that holds copies of data it's used recently or will likely use next. Because programs reuse the same data, cache lets the CPU skip the slower trip to RAM most of the time. You don't manage any of this, the hardware does it automatically, but the pyramid, tiny and instant at the top, huge and slow at the bottom, explains a lot about performance.

**Time:** about 0:55

### 2.4 — Why "volatile" matters

**Show:** slide 2.4

**Say:** Now the most security-relevant idea in the lesson, because it decides how a real investigation begins. RAM is volatile: it holds the live state of a running system, open programs, decrypted files, typed passwords, encryption keys, network connections, but it's erased the instant the power is cut. Storage is persistent: it survives power-off, but a running system's live secrets may exist only in RAM and never touch the disk. This gives forensics a sharp rule called the order of volatility: when investigating a live machine, capture the most volatile evidence first, RAM before disk. Picture a laptop seized while running, with an encrypted disk. The decryption key is in RAM right now, so the data is readable. Pull the plug and the key is gone forever, and the disk becomes an unreadable scramble. A trained investigator knows to capture the RAM first, while the machine is still on, precisely because of what this lesson taught about volatile versus persistent memory.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: RAM is fast, holds the running program, and is volatile; storage is slower and persistent. The memory hierarchy runs registers, cache, RAM, storage, and cache speeds up access to RAM. And the big one: in a live investigation, capture volatile memory, RAM, first, because it holds the keys and vanishes on power-off. You now understand the hardware that works on bytes. Next lesson, the software that manages all this hardware and lets many programs share it: the operating system.

**Time:** about 0:35
