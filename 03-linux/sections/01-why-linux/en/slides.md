---
title: "Linux for Security — Section 1: Why Security People Use Linux"
videos:
  1: What Linux Is, and Where It Runs
  2: Tools, Distros, and the Command Line
---

<!-- 1.1 -->
<!-- layout: title -->

# Why Security People Use Linux

## Video 1 · What Linux Is, and Where It Runs

Linux for Security · Section 1

In this video, you will learn:

- What Linux is
- Why open source matters for security
- Where Linux runs, and why that matters

---

<!-- 1.2 -->

# What Linux is

**Linux is an operating system**, like Windows or macOS (course 02): it manages the hardware and runs programs.

- The name refers to the **kernel** (course 02's privileged core), written by Linus Torvalds in 1991, built on by thousands since.
- Two differences that matter for security: it is **free and open source**, and it is built around the **command line**.

Rare on home laptops; **everywhere behind the scenes** of the internet.

---

<!-- 1.3 -->

# Open source, and why it matters

**Open source** = the code is public; anyone can read, check, and change it. (The opposite of Windows' secret code.)

- **Anyone can inspect it:** flaws and backdoors are harder to hide; you can **verify**, not just trust.
- **You can see exactly what it does**, priceless for a security person.
- **Free and modifiable:** the whole security-tool ecosystem grew from it.

A field built on **understanding systems** prefers a system you're allowed to understand.

---

<!-- 1.4 -->
<!-- layout: table -->

# Where Linux runs

| Where | How much Linux |
|---|---|
| Web servers | Most of the world's servers |
| The cloud | Most cloud computers |
| Phones | Android (billions) is built on Linux |
| Devices (IoT) | Routers, TVs, cameras, cars |
| Supercomputers | Essentially all |

**The systems attackers target and defenders protect are mostly Linux.** Can't work on Linux → locked out of real security work.

---

<!-- 1.5 -->
<!-- layout: recap -->

# Recap: what Linux is

- Linux is a **free, open-source OS**; its kernel runs the systems that matter.
- **Open source** lets you verify, not just trust, it fits security's spirit.
- Most servers, the cloud, Android, and devices are Linux, the real targets and defenses.

**Next video:** security tools, distributions, and the command-line mindset.

---

<!-- 2.1 -->
<!-- layout: title -->

# Why Security People Use Linux

## Video 2 · Tools, Distros, and the Command Line

Linux for Security · Section 1

In this video, you will learn:

- Why security tools live on Linux
- Distributions, and which to use
- The command-line mindset

---

<!-- 2.2 -->

# Why security tools live on Linux

Most security software is built for Linux, and much runs **only** on Linux.

- **Deep control:** low-level access to packets, processes, files.
- **Scriptable:** combine tools and automate (the heart of efficient work).
- **Free:** run dozens of lab machines, no licensing.
- **The community builds there**, new tools appear on Linux first.

There's even **Kali Linux**: a distro pre-loaded with offensive tools (your future "attacker machine").

---

<!-- 2.3 -->
<!-- layout: table -->

# Distributions

No single "Linux" to download. Groups package the kernel + programs into a **distribution** (distro). Same kernel → skills transfer.

| Distro | Known for |
|---|---|
| **Ubuntu** | Friendly, popular, well-documented, **this course** |
| Debian | Stable, minimal (Ubuntu is built on it) |
| **Kali** | Offensive security tools (the attacker's distro) |
| Red Hat / Rocky | Enterprise servers |

Learn on **Ubuntu**; skills carry to all of them.

---

<!-- 2.4 -->

# The command-line mindset

On Linux, security work is done by **typing commands**, not clicking. Hard at first, then far faster and more powerful.

- **Precise:** does exactly what you say.
- **Powerful:** pipelines do more than clicks (lesson 8).
- **Repeatable/automatable:** save in a script, run anywhere.
- **Works everywhere:** servers have **no mouse**, you reach them by command (SSH).

Expect it to feel slow, then click, then clicking a mouse feels clumsy.

---

<!-- 2.5 -->
<!-- layout: recap -->

# Recap: tools, distros, command line

- Almost all **security tools** live on Linux (including Kali).
- A **distribution** packages Linux; this course uses **Ubuntu**; skills transfer.
- The **command line** is precise, powerful, automatable, and the only option on servers, embrace it.

**Next lesson:** install Linux in a virtual machine, your safe practice system.
