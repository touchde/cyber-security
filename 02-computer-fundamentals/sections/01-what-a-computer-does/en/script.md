# Section 1: What a Computer Does — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | What a Computer Is, and Its Four Jobs | 1.1–1.5 | about 4 min |
| 2 | Numbers, Instructions, and Why It Matters | 2.1–2.5 | about 4 min |

---

## Video 1 — What a Computer Is, and Its Four Jobs

### 1.1 — Title

**Show:** slide 1.1

**Say:** Welcome to How Computers Work, the second Foundation course. In Security Fundamentals you learned what to protect and why. To actually attack or defend a system, you have to understand the machine it runs on, and that's what this course builds. We start at the very top: what a computer actually is.

**Time:** about 0:30

### 1.2 — What a computer is

**Show:** slide 1.2

**Say:** A computer looks complicated, but the core idea is simple: a computer is a machine that follows a list of instructions, step by step, very fast, to work with information. That's all it fundamentally does. It doesn't think or understand. It follows instructions, one after another, billions of times a second, without ever getting bored or making a different choice than the instructions say. Everything a computer appears to do, play a video, run a game, send a message, is really a huge number of tiny, simple steps carried out so quickly that the result looks instant. Two things make it powerful: speed, billions of steps a second, and reliability, it does exactly what the instructions say, every time. And that's also the security problem in one sentence: a computer will follow whatever instructions it's given, including an attacker's, if the attacker can get their instructions to run.

**Time:** about 1:00

### 1.3 — The four jobs

**Show:** slide 1.3

**Say:** Every computer, from a phone to a giant server, does four things, and the whole course hangs on these four words. Input: information comes in, by typing, a tap, a network message, a sensor. Processing: the computer works on it, following instructions, calculating, sorting, deciding. Output: a result goes out, to the screen, as a sound, as a network reply. And storage: information is kept for later, a saved file, a remembered setting. Here's a habit worth forming: when you meet a new attack later in the program, ask which of the four it's attacking. Is it poisoning the input, hijacking the processing, reading the output, or stealing the storage? That question will orient you every time.

**Time:** about 0:55

### 1.4 — Hardware and software

**Show:** slide 1.4

**Say:** A computer has two sides. Hardware is the physical machine, the parts you could touch: the processor, the memory chips, the disk, the screen. Software is the instructions, the programs that tell the hardware what to do, an operating system, an app, a game, or a virus. The relationship is simple: software is a list of instructions, and hardware is the machine that carries them out. Hardware with no software is an inert lump; software with no hardware is just a list that does nothing. Between the two sits a special piece of software called the operating system, Windows, macOS, Linux, Android, which manages the hardware and lets other programs use it. So picture three layers: hardware at the bottom, the operating system in the middle, your apps on top. Attacks hit every layer, and the most serious often target the operating system in the middle, because whoever controls it controls everything above.

**Time:** about 1:00

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So, a computer follows numeric instructions, step by step, very fast, and it doesn't understand anything. The four jobs are input, processing, output, and storage. And there are three layers: hardware, the operating system, and your apps. Next, the single most surprising idea in this course: everything inside a computer is numbers, and why that matters for security.

**Time:** about 0:30

---

## Video 2 — Numbers, Instructions, and Why It Matters

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video, the idea that unlocks the rest of the course: everything inside a computer is numbers. We'll see why instructions and data are stored the same way, and why a security person has to understand all this.

**Time:** about 0:25

### 2.2 — Everything inside is numbers

**Show:** slide 2.2

**Say:** Here's the idea that surprises people most. Inside a computer, everything is numbers, and not just sums and prices, everything. A letter of text is a number, which we'll see in lesson 3. A color in a photo is a set of numbers. A sound is a long list of numbers. A program's instructions are numbers. Images, video, documents, web pages, all numbers. And the computer has no idea what a number means, the same number could be a letter, a brightness, or an instruction, depending only on how the computer is told to treat it. That's a deep fact: one machine, working only with numbers, can handle every kind of information. And the numbers themselves are stored in the simplest possible way, as huge quantities of on-or-off switches, patterns of ones and zeros, which the next lesson opens up.

**Time:** about 0:55

### 2.3 — Instructions and data are the same stuff

**Show:** slide 2.3

**Say:** Since everything is numbers, a computer stores two very different things the same way. Data is the information a program works on, a photo, a message, a list of prices. Instructions are the steps the program follows, the program itself. Both are just numbers in the same memory. This idea, holding instructions and data together in one memory, is called the stored-program design, and almost every computer works this way. It's why computers are so flexible: to make one do something new, you don't rebuild the machine, you just give it a new program. But it has a dangerous side, and it's the root of a whole class of attacks. If instructions and data live in the same memory and look the same, a computer can be tricked into treating data as instructions. An attacker sends what looks like ordinary data, a message, a file, an image, but arranges it so the computer runs part of it as instructions. That's the essence of buffer overflows and code injection, which you'll study later. It all starts right here.

**Time:** about 1:05

### 2.4 — Why security needs the machine

**Show:** slide 2.4

**Say:** You might wonder why a security course spends time on CPUs and memory. Because you cannot secure, attack, or investigate what you don't understand. Reverse engineering means reading a program's instructions and memory. Binary exploitation means bending how a program uses memory, especially the stack. Malware analysis needs executables, processes, and the OS. And digital forensics means recovering data from memory, disks, and deleted files. Notice how often those later courses appear: this course is the trunk, and they're the branches. When a forensic analyst recovers a deleted file, they're using what lesson 7 teaches. When an exploit developer overflows a buffer, they're using lessons 6 and 11. Skip the trunk, and the branches never hold. There's also a simpler reason: understanding the machine removes fear. A computer isn't magic, it's a fast, literal follower of numeric instructions, and once you see that, security becomes something you can reason about.

**Time:** about 1:00

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: inside a computer, everything is numbers, stored as on-and-off switches. Instructions and data share the same memory, the stored-program idea, which makes computers flexible but also attackable. And every later security course, reversing, exploitation, forensics, rests on understanding this machine. Everything we do is on our own machines, for understanding and defending. In the next lesson, we go all the way to the bottom, to the ones and zeros themselves: bits, binary, and hexadecimal.

**Time:** about 0:35
