# Section 6: Processes, Threads, and Memory — Video Scripts

Two videos, about 9 minutes in total. Slide IDs match [`slides.md`](slides.md). The console demo uses `ps`.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Processes and Their Memory | 1.1–1.5 | about 4.5 min |
| 2 | Threads, Isolation, and Seeing Processes | 2.1–2.5 | about 4.5 min |

---

## Video 1 — Processes and Their Memory

### 1.1 — Title

**Show:** slide 1.1

**Say:** This is one of the most important lessons in the course, because the memory layout we'll draw is the ground that reverse engineering and binary exploitation stand on. We zoom into a single running program, a process, and look at exactly how it lives in memory.

**Time:** about 0:25

### 1.2 — Program vs process

**Show:** slide 1.2

**Say:** First, a key distinction. A program is a file sitting on disk: a list of instructions, not doing anything. A process is a program that's running: loaded into memory, with the CPU executing its instructions. It's like a recipe versus actually cooking the dish, and one recipe can be cooked many times at once, which is why you can open two windows of the same app, two processes of one program. When you start a program, the OS creates a process: it loads the instructions into RAM, gives the process its own memory, assigns a unique number called the PID, and starts running it. Every process also has a parent, the process that started it, tracked by its PPID. That parent–child structure matters in security: investigators look at what started what, because a word processor spawning a command shell is exactly the kind of unusual relationship that reveals an attack.

**Time:** about 0:55

### 1.3 — A process's memory layout

**Show:** slide 1.3

**Say:** When a process runs, the OS gives it a block of memory, organized into regions, and knowing this map is essential. Picture a tall strip of memory. At the bottom sit the fixed parts: the code, which is the instructions themselves, and the data, the global variables and constants. Above them, two regions grow toward each other. The heap grows up from below, and the stack grows down from the top, with free space between them. Why does a security course care? Because attacks live in this map. The code region is what a reverse engineer reads. The stack is where classic buffer-overflow attacks happen. The heap is where a different family of attacks happens. For now, just fix the picture: instructions at the bottom, and the stack and heap growing toward each other.

**Time:** about 0:55

### 1.4 — The stack and the heap

**Show:** slide 1.4

**Say:** Let's look closer at those two regions. The stack is for short-lived, orderly data, especially the data of functions. Every time a function is called, a chunk called a stack frame is added to the top, holding that function's local variables and, crucially, the return address: where to continue when the function finishes. When the function returns, its frame is removed, neatly, last in first out. Now, that return address is one of the most important facts in all of security. A buffer overflow works by writing past the end of a buffer on the stack until it overwrites the return address, so when the function finishes, the CPU jumps to an address the attacker chose, running the attacker's instructions. The heap, by contrast, is for longer-lived data whose size isn't known in advance, memory the program requests while running, and the program must give it back. Mistakes there cause use-after-free bugs and leaks. Short version: stack is orderly and automatic; heap is flexible and manual.

**Time:** about 1:00

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: a program is a file on disk, a process is it running in memory, and the PID and PPID track a process and its parent. The memory layout has code and data at the bottom, with the heap growing up and the stack growing down. And the stack holds the return address, the classic exploit target. Next, how a process does several things at once with threads, and the virtual memory that keeps processes apart.

**Time:** about 0:25

---

## Video 2 — Threads, Isolation, and Seeing Processes

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video: threads, which let one process do several things at once, the virtual memory that isolates processes from each other, and finally, seeing real processes on a machine with the `ps` command.

**Time:** about 0:20

### 2.2 — Threads

**Show:** slide 2.2

**Say:** A process can do more than one thing at a time using threads. A thread is a single stream of execution within a process. A process always has at least one, and it can create more, one thread handling the screen while another downloads a file. Here's the key distinction. Processes are isolated from each other: each has its own separate memory, and one process can't see into another's. But threads within one process share that process's memory, they're all inside the same memory block, working on the same data. That sharing makes threads fast, but it's also a source of bugs. Because threads share memory and run at unpredictable, interleaved times, two threads can collide, both changing the same data at once, causing race conditions, where the outcome depends on exact timing. And race conditions aren't just reliability bugs; they're a real vulnerability class you'll meet in web security and exploitation.

**Time:** about 0:55

### 2.3 — Virtual memory and isolation

**Show:** slide 2.3

**Say:** Here's a deep question: if every process is just put into RAM, what stops one from reading or trashing another's memory? The answer is virtual memory. The trick is that each process is given its own private view of memory, as if it were the only program on the machine. A process sees a clean range of addresses starting from zero, its virtual address space, and believes it owns all of it. But those addresses aren't real physical locations: behind the scenes, the CPU and OS translate each process's virtual addresses to actual physical RAM, and they make sure each process maps to a different, separate part of RAM. The consequence is isolation: address `0x1000` in one process and `0x1000` in another point to completely different physical memory, so one process literally can't name, let alone touch, another's data. That's the main thing keeping your banking app's memory safe from a malicious app running beside it.

**Time:** about 0:55

### 2.4 — Seeing real processes: ps

**Show:** slide 2.4

**Say:** All of this is visible on any computer. The command that lists running processes is `ps` on Linux and macOS; Windows has Task Manager. Read the columns with what you now know. PID is the process's unique ID. PPID is its parent. Notice Google Chrome Helper, PID 3001, has PPID 2983, which is Google Chrome itself, the browser started its own helper, so that's the parent–child link made visible. Then %CPU and %MEM show how much processor time and memory it's using, and COMM is the name. This simple view is the foundation of a lot of defensive work. A SOC analyst scans process lists for the abnormal: a strange name, an unusual parent like a document viewer whose child is a command shell, or a process eating CPU for no reason. Malware hides among processes, and finding it starts with being able to read a list like this.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: threads share a process's memory, which is fast but causes race conditions, while processes are isolated. Virtual memory gives each process a private address space, and that's the isolation keeping them apart. Step back and the theme of the last three lessons is clear: a computer is a set of boundaries, process from process, user from kernel, readable from writable from executable, and security is largely about keeping those boundaries intact while attacks try to break them. And `ps` lets you see real processes, where finding malware begins. Next lesson, we look at where programs and data rest when they're not running: files and file systems.

**Time:** about 0:35
