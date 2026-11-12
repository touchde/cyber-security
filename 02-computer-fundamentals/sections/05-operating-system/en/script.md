# Section 5: What an Operating System Does — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | The OS, the Kernel, and System Calls | 1.1–1.5 | about 4 min |
| 2 | Multitasking and the Security Boundary | 2.1–2.5 | about 4 min |

---

## Video 1 — The OS, the Kernel, and System Calls

### 1.1 — Title

**Show:** slide 1.1

**Say:** Last lesson we looked at the hardware. This lesson is about the software that manages all of it, the operating system. We'll see what it does, meet the kernel at its core, and learn how programs ask it for things through system calls.

**Time:** about 0:25

### 1.2 — The OS as the manager

**Show:** slide 1.2

**Say:** Between the bare hardware and the apps you use sits the operating system, Windows, macOS, Linux, Android. It's the middle layer from lesson 1. Its job, in one sentence: the operating system manages the computer's hardware and resources and shares them safely among all the programs that want to use them. Think of a busy restaurant kitchen. The hardware is the stoves and knives; the programs are cooks, all wanting the same equipment at once. Without a manager they'd collide and cause chaos. The OS is the kitchen manager: it decides who uses what, when, and keeps them out of each other's way. And crucially, a program can't touch the disk or the network directly, it asks the OS. That funnel, every request passing through the OS, is what makes the OS the center of a computer's security.

**Time:** about 0:55

### 1.3 — The kernel, and the two spaces

**Show:** slide 1.3

**Say:** At the heart of the OS is the kernel: the core program that's always running and has complete control of the machine. If the OS is the manager, the kernel is the manager's brain and hands, the part that actually talks to hardware and enforces the rules. It runs with full privilege, so to protect it, the CPU itself enforces a hard line between two worlds. Kernel space is where the kernel runs, with full power and direct hardware access. User space is where normal programs run, your browser, your editor, with limited privilege and no direct access to hardware. This wall means a user-space program that crashes or misbehaves can't take down the whole machine or corrupt the kernel, because it never had the power to. And it means the kernel is the ultimate prize: control the kernel, and you control the entire machine, which is why the most serious malware, like rootkits, aims to get there.

**Time:** about 0:55

### 1.4 — System calls

**Show:** slide 1.4

**Say:** So if user-space programs can't touch hardware directly, how does your editor save a file to disk? It asks the kernel, through a system call. A system call is the official, controlled doorway from user space into kernel space. When a program needs something only the kernel can do, open a file, read from the network, start another program, it makes a system call: it asks the kernel, please do this for me. The kernel checks whether the program is allowed, does the work, and hands back the result. This makes system calls deeply important for security in two ways. First, they're the checkpoints: every file opened, every network connection, goes through a system call where the kernel enforces permissions. Second, they're how we watch programs: security tools and investigators observe a program's system calls to see what it really does, regardless of what it claims. In malware analysis, you learn far more from the calls a program makes than from what it says.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: the OS manages hardware and shares it, and apps ask it for everything. The kernel is the fully privileged core, and the line between user space and kernel space is a wall enforced by the CPU itself. And system calls are the controlled doorway, both the OS's checkpoint and a prime place to watch what a program really does. Next, how the OS runs many programs at once, and why it's the main security boundary on any computer.

**Time:** about 0:25

---

## Video 2 — Multitasking and the Security Boundary

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video: how the kernel talks to the endless variety of hardware through drivers, how it runs many programs at once through multitasking, and the heart of the matter, how the OS enforces who may do what.

**Time:** about 0:20

### 2.2 — Drivers, and multitasking

**Show:** slide 2.2

**Say:** First, drivers. Computers have endless different hardware, so the kernel can't know every device. Instead it uses drivers: software that each know how to talk to one specific kind of hardware, a translator. The kernel says "send this to the printer" in general terms, and the driver turns it into the exact signals that printer understands. The security weight here: most drivers run in kernel space, with full privilege, so a flaw in a driver is a flaw in the kernel's world, a serious attack path. Second, multitasking. A core can really only run one stream of instructions at a time, so the OS switches between programs thousands of times a second, pausing one, saving its state, and switching to the next. That swap is a context switch. With several cores, some of this is truly parallel. And each program's state is saved and isolated, so one program can't read another's working data just because they share the CPU.

**Time:** about 0:55

### 2.3 — Users and permissions

**Show:** slide 2.3

**Say:** Now the part that matters most for security. The OS doesn't just manage hardware, it enforces who is allowed to do what, which is authentication and authorization from Security Fundamentals, made real on an actual computer. Every modern OS has users, accounts, and every file and action has permissions saying which users may do it. There's usually one specially powerful account: root, or the superuser, on Linux and macOS, and Administrator on Windows, which can do almost anything. Ordinary accounts are deliberately limited. This is least privilege in practice: a normal user can run their own programs and edit their own files, but not change the system or read others' private data. And that means if malware runs under your limited account, it also can't change the system, so the damage is contained.

**Time:** about 0:55

### 2.4 — The OS is the main security boundary

**Show:** slide 2.4

**Say:** Which is exactly why attackers work so hard to escalate privilege: to go from an ordinary account to root or Administrator. The powerful account can change the system and read any data, so that jump is the single most common goal after breaking in, and a whole part of the pentesting courses is about it. Step back and see the big picture. The OS is the main security boundary on a computer. It isolates programs from each other through user and kernel space, it controls every real action through system calls, and it enforces who may do what through users and permissions. Nearly every attack is, in some form, an attempt to break one of these OS-enforced boundaries, and nearly every defense is about keeping them intact. That's why the OS gets its own deep courses, Linux and Windows, and why understanding it here is essential.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: drivers are privileged kernel code and a real attack surface. Multitasking switches the CPU between programs fast, with context switches, and keeps them isolated. The OS enforces users and permissions, with an all-powerful root or Administrator account, and attackers try to escalate to it. And the big theme: the OS is the main security boundary, so most attacks are attempts to break it. You now understand the hardware and the OS that manages it. Next lesson, we zoom into the most important thing the OS manages, where programs actually live and run: processes and their memory.

**Time:** about 0:35
