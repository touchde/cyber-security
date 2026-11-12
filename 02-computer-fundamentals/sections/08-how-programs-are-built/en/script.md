# Section 8: How Programs Are Built and Run — Video Scripts

Two videos, about 9 minutes in total. Slide IDs match [`slides.md`](slides.md). The demos compile a C program with Clang and inspect it with `file` and `strings`; have a terminal with a C compiler ready to run them live.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | From Source Code to a Running Program | 1.1–1.5 | about 4.5 min |
| 2 | Machine Code, Libraries, and Executables | 2.1–2.5 | about 4.5 min |

---

## Video 1 — From Source Code to a Running Program

### 1.1 — Title

**Show:** slide 1.1

**Say:** We've said a program is instructions in memory. But where do those instructions come from? Nobody writes raw machine instructions by hand. In this lesson we see how a human-written program becomes bytes the CPU can run, and why that journey is the foundation of reverse engineering and malware analysis.

**Time:** about 0:25

### 1.2 — Source code must be translated

**Show:** slide 1.2

**Say:** People write source code: instructions in a programming language humans can read, like C, Python, or JavaScript. But source code is just text, a file of characters, and the CPU can't run text, it runs machine code. Here's a tiny C program. Don't worry about the exact syntax, read it like English: it prints a line and adds two numbers. On its own, the CPU can't run this. Something must turn this readable text into the numeric machine instructions the CPU understands. And there are two main ways to do that, compiling and interpreting, and the difference shapes a lot of security.

**Time:** about 0:50

### 1.3 — Compiled vs interpreted

**Show:** slide 1.3

**Say:** Two strategies. Compiled languages, like C, C++, Rust, and Go, are translated ahead of time, in one step, into a file full of machine code, the executable. You run the executable directly, and the original source isn't needed or present on the user's machine. It's like translating a whole book once and handing out the translation. Interpreted languages, like Python and JavaScript, are translated as they run, line by line, by another program called the interpreter. You ship the source, and the user's interpreter runs it on the spot, like a live interpreter translating a speech sentence by sentence. For security this is huge. A compiled program ships as machine code, not readable source, so to understand it you must reverse engineer it, that's analyzing a mystery dot-exe. An interpreted program ships as source, so its logic is often easy to read, which is why malicious scripts are so common.

**Time:** about 0:55

### 1.4 — The build pipeline

**Show:** slide 1.4

**Say:** Turning C source into an executable actually takes a few steps, together called building. With Clang, our program builds and runs with one command, printing its two lines. But that one command hides two important stages. First, compiling: the compiler translates your source into machine code, producing an object file of raw instructions for your functions. Second, linking: the linker combines your object files with any library code you used, here the `printf` function, which you didn't write, into one finished executable that can actually run. So the shape is: source, compile, object files, link with libraries, executable. And here's the thing to remember, reverse engineering runs this journey backward, taking an executable and trying to recover readable meaning.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: the CPU runs machine code, not source, so source must be compiled or interpreted. Compiled code hides its logic in machine code, which you reverse engineer, while interpreted code ships readable source. And building a program is compiling, turning your code into machine code, plus linking, joining it with libraries into a runnable executable. Next, what that machine code actually is, the libraries programs depend on, and the executable files themselves.

**Time:** about 0:25

---

## Video 2 — Machine Code, Libraries, and Executables

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video: what the compiler actually produces, machine code and its readable form, assembly; the libraries that make up most of a program; and executable files, plus a trick that's often the very first step in malware analysis.

**Time:** about 0:20

### 2.2 — Machine code and assembly

**Show:** slide 2.2

**Say:** What does the compiler produce? Machine code: the raw numeric instructions the CPU fetches and executes. Each instruction is a pattern of bytes meaning something specific to the processor, add these registers, jump to this address. It's what the executable contains, and it's not readable by humans, it's just bytes. So there's a human-friendly version called assembly language, a text form where each instruction is written as a short mnemonic, like add, mov for move, cmp for compare, jmp for jump. Assembly is almost one-to-one with machine code, just readable. So picture a ladder: source code at the top, high level and readable; machine code at the bottom, the bytes the CPU runs; and assembly as the readable text form of that machine code. The compiler goes down the ladder. A reverse engineer, with only the executable, climbs partway back up, using a disassembler to turn machine code into assembly, because the original source is gone. That's why reversing is hard, skilled work.

**Time:** about 0:55

### 2.3 — Libraries: static and dynamic

**Show:** slide 2.3

**Say:** Our tiny program used `printf` to print, but we never wrote `printf`, it came from a library: ready-made code programs reuse. Almost every real program leans on many libraries, for math, networking, graphics, encryption, which is why Security Fundamentals called an app mostly other people's code. Libraries connect two ways. Static linking copies the library's code into the executable, so the program is self-contained but bigger. Dynamic linking keeps the library a separate file, a dot-dll on Windows, dot-so on Linux, loaded at run time, so many programs share one copy and it can be updated independently. For security: a vulnerability in a library affects every program using it, that's supply-chain risk. And because dynamically linked programs load libraries by name at run time, an attacker who plants a malicious library where the program looks can get their code loaded, a real technique called library hijacking.

**Time:** about 0:55

### 2.4 — Executables, and why strings matters

**Show:** slide 2.4

**Say:** An executable isn't just a naked blob of machine code. It's a structured file with the machine code plus information the OS needs to run it: where code goes in memory, which libraries to load, where to start. The format depends on the OS: ELF on Linux, PE, the familiar dot-exe, on Windows, and Mach-O on macOS. The `file` command identifies the format from the content. And here's something important: even though the program is compiled machine code, the text strings inside it, like "Mina Coffee," are still readable, the `strings` tool pulls them right out. That's why one of the very first steps in analyzing any unknown program, malware included, is to run `strings` on it: web addresses, messages, file names, and clues often sit in plain sight inside a compiled binary. It's the exact technique the mobile-security course used to read a secret out of an app.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: machine code is the bytes the CPU runs, and assembly is its readable form, which reverse engineers read. Libraries make up most of a program, static or dynamic, and bring supply-chain risk and hijacking. Executables are structured files, ELF, PE, or Mach-O, and `strings` and `file` are fast first wins in analysis. And the big picture: reverse engineering and malware analysis run this whole journey backward. Next lesson, we go right back to the start of a computer's life, how it gets from a cold power-off to a running operating system: the boot process.

**Time:** about 0:35
