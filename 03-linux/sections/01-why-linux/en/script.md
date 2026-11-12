# Section 1: Why Security People Use Linux — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). No command demos (that starts in lesson 2).

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | What Linux Is, and Where It Runs | 1.1–1.5 | about 4 min |
| 2 | Tools, Distros, and the Command Line | 2.1–2.5 | about 4 min |

---

## Video 1 — What Linux Is, and Where It Runs

### 1.1 — Title

**Show:** slide 1.1

**Say:** Welcome to Linux for Security, the third Foundation course. In How Computers Work you met the operating system in general. This course is about one operating system in particular, Linux, the one security people live in. In this first video, what Linux is, why open source matters, and where Linux actually runs.

**Time:** about 0:30

### 1.2 — What Linux is

**Show:** slide 1.2

**Say:** Linux is an operating system, like Windows or macOS: the software that manages a computer's hardware and runs its programs. Technically the name refers to the kernel, the privileged core you met in course 02, written originally by Linus Torvalds in 1991 and developed since by thousands of people worldwide; in everyday use, Linux means the whole operating system built around that kernel. Two things make it different from Windows and macOS, and both matter for security. It's free and open source, anyone can get it, study it, and change it. And it's built around the command line, where its real power lives. You may rarely see Linux on a home laptop, but step behind the scenes of the internet and it's everywhere.

**Time:** about 0:50

### 1.3 — Open source, and why it matters

**Show:** slide 1.3

**Say:** Open source means the source code is public: anyone can read it, check it, and change it. That's the opposite of closed software like Windows, whose code is a company secret. Why does this matter so much for security? First, anyone can inspect it, so flaws and backdoors are far harder to hide, and crucially, you can verify open software instead of trusting a vendor's word. Second, you can see exactly what it does, which for a security person is priceless, you can read how a tool works and understand the system to its core. Third, it's free and modifiable, which is why the whole ecosystem of security tools grew up around it. A field built on understanding systems naturally prefers a system you're allowed to understand completely.

**Time:** about 0:50

### 1.4 — Where Linux runs

**Show:** slide 1.4

**Say:** So if Linux is rare on home laptops, where is it? Nearly everywhere else that matters. The large majority of the world's web servers run Linux. Most cloud computers run Linux. Android, on billions of phones, is built on the Linux kernel. Routers, smart TVs, cameras, and cars run Linux. And essentially all of the world's supercomputers run Linux. Think about what that means: the systems attackers target, and that defenders protect, are mostly Linux. When you investigate a hacked web server, it's almost certainly Linux. When you secure a company's cloud, you're securing Linux machines. A security professional who can't work on Linux is locked out of most of the real targets and most of the real defense. That's why Linux comes this early in the program.

**Time:** about 0:50

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: Linux is a free, open-source operating system, and its kernel runs the systems that matter. Open source lets you verify rather than just trust, which fits the spirit of security. And most servers, the cloud, Android, and devices run Linux, so they're both the real targets and the real defenses. Next, why the security tools themselves live on Linux, the distributions you'll use, and the command-line mindset this course asks of you.

**Time:** about 0:30

---

## Video 2 — Tools, Distros, and the Command Line

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video: why almost every security tool runs on Linux, what a distribution is and which one we'll use, and the single biggest mindset shift this course asks of you, embracing the command line.

**Time:** about 0:25

### 2.2 — Why security tools live on Linux

**Show:** slide 2.2

**Say:** Beyond being the systems you attack and defend, Linux is also where the tools live. The overwhelming majority of security software, scanners, packet analyzers, exploitation frameworks, forensic kits, is built for Linux, and much of it runs only on Linux. Why? Linux gives deep, low-level control, to raw network packets, to processes, to the file system, that a locked-down consumer OS doesn't. It's scriptable and automatable, which is the heart of efficient security work. It's free, so you can run dozens of lab machines without licensing fees. And the community builds there, so new tools appear on Linux first. There's even a distribution made specifically for offensive security, Kali Linux, pre-loaded with hundreds of tools, which you'll use as your attacker machine later. The point is simple: to use the tools of the trade, you have to be comfortable on Linux.

**Time:** about 0:55

### 2.3 — Distributions

**Show:** slide 2.3

**Say:** Here's something that surprises newcomers: there's no single Linux you download. Because it's open source, many groups package the kernel together with different programs, settings, and looks, into a complete operating system, and each packaged version is called a distribution, or distro. They all share the same kernel, so your skills transfer between them, but they differ in their default tools and focus. Ubuntu is friendly, popular, and well-documented, great for learning and for servers. Debian is stable and minimal, and Ubuntu is built on it. Kali is pre-loaded with offensive tools, the attacker's distro. And Red Hat and Rocky are common in big companies. This course uses Ubuntu, because it's beginner-friendly, widely used on real servers, and well-documented. You'll meet Kali later, when you need its attack tools. Don't worry about choosing a distro yourself yet, learn on Ubuntu, and the skills carry everywhere.

**Time:** about 0:55

### 2.4 — The command-line mindset

**Show:** slide 2.4

**Say:** Now the biggest shift for a newcomer: on Linux, security work is done mostly by typing commands, not clicking buttons. Linux has graphical desktops, but the command line, the shell, is where the real power is. It feels harder at first, then becomes far faster and more powerful, and embracing it is the most important mindset change this course asks of you. Why do security people prefer it? It's precise, doing exactly what you say with no hidden behavior. It's powerful, small commands combine into pipelines that do in one line what would take many clicks. It's repeatable and automatable, saved in a script and run on one machine or a thousand, and you can't automate clicking. And it works everywhere: a server has no screen or mouse, so you reach it over the network and work entirely by command. Don't expect to love it on day one. Expect it to feel slow and strange, and then, around the time you build your first pipeline, to click.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: almost all security tools live on Linux, including Kali, the attacker's distro. A distribution is a packaged version of Linux, and this course uses Ubuntu, with skills that transfer everywhere. And the command line is precise, powerful, automatable, and the only option on the servers you'll work on, so embrace it. Everything in this course is hands-on and happens in your own Ubuntu virtual machine, which keeps it safe and legal, because the VM is yours. In the next lesson, we build that machine: installing Linux in a virtual machine, your personal, safe practice system.

**Time:** about 0:30
