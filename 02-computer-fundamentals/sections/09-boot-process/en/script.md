# Section 9: The Boot Process — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). One console demo uses `uptime`.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | From Power Button to Running OS | 1.1–1.5 | about 4 min |
| 2 | Boot Malware and Secure Boot | 2.1–2.5 | about 4 min |

---

## Video 1 — From Power Button to Running OS

### 1.1 — Title

**Show:** slide 1.1

**Say:** We've seen the running computer in detail. Now let's rewind all the way to the start: how does a cold, powered-off machine become a running operating system? That's the boot process, and it's a security battleground, because whoever gets in early controls everything after.

**Time:** about 0:25

### 1.2 — Boot is a chain

**Show:** slide 1.2

**Say:** When you press the power button, the computer is just hardware with nothing running: RAM is empty, because it's volatile, and the operating system is only a file on the disk, not yet loaded. Yet in a few seconds you reach a running desktop. That journey is the boot process, from bootstrapping, because the computer has to start itself from almost nothing. The whole thing is a chain: each stage is small and simple, and its main job is to find, check, and start the next, bigger stage. Firmware wakes the hardware and finds a drive to boot from. The bootloader on that drive finds and loads the kernel. The kernel takes over and sets up the system. And init starts the first user programs, leading to the login screen and desktop. Each link hands control to the next, and that's exactly why boot matters for security: whoever controls an early link controls everything that comes after it. A chain is only as trustworthy as its first link.

**Time:** about 0:55

### 1.3 — Firmware: BIOS and UEFI

**Show:** slide 1.3

**Say:** The very first code to run isn't on the hard drive at all, it's firmware: a small, permanent program stored on a chip on the motherboard. Because it's on a chip, it's there the instant power arrives, before any disk is read. Its job: wake and test the hardware, find a bootable drive, and run the first piece of software from it, the bootloader. Firmware has two generations to know by name. BIOS is the old standard, now largely replaced. UEFI is the modern replacement on nearly all current computers, more capable, and importantly, able to perform security checks on what it boots. And because firmware runs before the OS and any antivirus, malware that infects it runs first and can survive reinstalling the OS or even replacing the hard drive, because it doesn't live on the drive. That's advanced and rare, but it shows the principle: the earlier the attacker, the harder to see and remove.

**Time:** about 0:55

### 1.4 — Bootloader, kernel, and init

**Show:** slide 1.4

**Say:** The firmware doesn't know how to start a whole operating system, so it hands off to a specialist: the bootloader, a small program whose one job is to find the kernel on the drive, load it into memory, and start it. It's also what sometimes shows a menu to pick between Windows and Linux. Then the kernel takes over: it initializes the hardware and loads drivers, sets up memory management including the virtual memory that isolates every process, and starts the first user-space program. That first program is init, and from lesson 6 you know every process has a parent, forming a tree. Init is the root of that tree, the first user-space process, with the famous process ID of 1. It starts the services, the login screen, and eventually everything you open. So the full chain is firmware, bootloader, kernel, init, desktop.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: boot is a chain, firmware to bootloader to kernel to init to desktop, each stage starting the next. Firmware lives on a chip and runs first, before the OS. Init is PID 1, the ancestor of every process. And the key security idea: control an early link, and you control everything after. Next, exactly how attackers exploit that, and how modern computers defend the start of the chain.

**Time:** about 0:25

---

## Video 2 — Boot Malware and Secure Boot

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video, the security payoff of the boot chain: why it's such a target, where malware hides in it, why you can't trust a compromised machine's own report, and how Secure Boot defends the whole chain.

**Time:** about 0:20

### 2.2 — Where malware hides at boot

**Show:** slide 2.2

**Say:** The boot chain is attractive to attackers for one reason above all: persistence. Malware wants to survive restarts, and if it only lived in RAM, a reboot would wipe it. So it seeks a foothold in the boot process, to be loaded automatically every time, early and often invisibly. And the earlier it sits, the more dangerous it is. In firmware, a firmware implant runs before the OS and survives reinstalls and even disk replacement. In the bootloader, a bootkit runs before the kernel and can load a tampered kernel. In the kernel, as a driver, a rootkit runs with full privilege and can hide itself, files, and processes from the OS. And in startup programs, autostart persistence is common but easier to find. The deep ones are so serious because they load before the tools that would detect them, and can then lie to those tools.

**Time:** about 0:55

### 2.3 — Why you can't trust a compromised machine

**Show:** slide 2.3

**Say:** Let's dwell on that, because it's a profound point. A rootkit runs with full privilege and can hide its own files and processes from the operating system's own tools. So the machine lies about itself: you ask it "list your processes" and the malware simply removes itself from the answer. This is why serious forensics sometimes examines a suspect's disk from a separate, trusted machine. If the suspect system's own OS is compromised, you can't trust anything it tells you about itself. It's the lesson-1 principle at full force: control an early link, and you can hide from everything later.

**Time:** about 0:45

### 2.4 — Secure Boot: verify each link

**Show:** slide 2.4

**Say:** So if the danger is a tampered early link, the defense is to check each link before trusting it, and that's exactly what Secure Boot does. Built into UEFI firmware, Secure Boot uses digital signatures, a cryptography idea you'll study later, to verify that each stage of the boot is genuine and unmodified before running it. The idea is a chain of trust: the firmware only runs a bootloader that carries a valid, trusted signature; that bootloader only loads a properly signed kernel; and so on. If any link has been tampered with, its signature no longer matches, and Secure Boot refuses to continue, stopping a bootkit before it runs. Each link verifies the next, so trust extends from the firmware all the way up to the OS. It's defense in depth applied to the very start of a computer's life.

**Time:** about 0:50

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: malware targets boot for persistence, and bootkits and rootkits load early and hide. A compromised machine can't be trusted to report on itself, so you examine it from outside. And Secure Boot verifies each stage's signature, a chain of trust, to stop tampering early. You now understand a computer's full life, from power-on to a running system, and why each early step is a security concern. In the next lesson, we look at a technology that lets one physical computer safely run many separate systems at once, which is the foundation of the practice lab you'll build: virtual machines and containers.

**Time:** about 0:35
