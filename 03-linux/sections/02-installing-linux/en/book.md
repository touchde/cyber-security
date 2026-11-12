# Section 2: Installing Linux in a Virtual Machine

> Covers chapter 2 in the [outline](../../../planning/outline.md).

## What You Will Learn

- Why you install Linux in a virtual machine, not on your real computer.
- How to choose a distribution for this course.
- How to get the Linux image and check it is genuine.
- How to create the virtual machine.
- How to boot and log in for the first time.
- How to take a snapshot, your safety net.
- How to run the first system update.

## Before You Start

You need How Computers Work (02), especially its virtualization lesson, you know what a virtual machine, a hypervisor, and a snapshot are. This lesson turns that knowledge into a real, working Linux system you own. It is mostly steps to follow on your own computer. By the end you will have an Ubuntu virtual machine, the practice system for the rest of this course. Set aside about an hour; the download is the slow part.

---

## 1. Why a Virtual Machine

You will not install Linux directly onto your laptop. Instead you will run it inside a **virtual machine (VM)**, a full simulated computer running on top of your real one (How Computers Work, lesson 10). Everything in this course happens inside that VM.

Why a VM, and not your real machine?

- **Safety.** You will run commands that can break a system, change permissions, delete files, edit configuration. In a VM, a mistake harms only the VM, never your real computer and its data.
- **Snapshots.** A VM can be saved and restored in seconds (topic 6). Break something badly? Restore a snapshot and you are instantly back to a clean state. This makes learning fearless.
- **It keeps your real computer clean.** No changes to your laptop; when you are done, you can delete the VM and nothing remains.
- **It satisfies the one rule.** The VM is *yours*. Everything you do, including the attacks you will practise in later courses, happens on a system you own, so the "only test what you own" rule (Security Fundamentals, lesson 9) is met by construction.

This VM is the single practice machine for this course. (The full home lab, with multiple machines on an isolated network, comes in course 08; here you need just one.) You run it with a **hypervisor**, the software that creates and runs VMs, which you install first.

## 2. Choosing a Distribution: Ubuntu and Kali

From lesson 1, a **distribution** is a packaged version of Linux, and this course uses **Ubuntu**: beginner-friendly, widely used on real servers, and well-documented, so your skills apply to the real world. Specifically, use the current **Ubuntu LTS** ("Long-Term Support") desktop release, which is stable and supported for years.

You will also hear about **Kali Linux**, the distribution pre-loaded with offensive security tools. You do *not* need Kali for this course; Ubuntu is the right choice for learning Linux fundamentals. You will install Kali later, as your attacker machine, when the home lab (course 08) and the pentesting courses need it. For now: **one Ubuntu VM.**

Pick a hypervisor for your computer:

- **VirtualBox** (free, Windows/Linux, and Intel Macs) — the common choice.
- **UTM** (free, Apple Silicon Macs) — because VirtualBox support on Apple Silicon is limited.
- **VMware** (free for personal use) — another solid option.

Install the hypervisor for your system first, from its official site (see the [sources](../../../planning/sources.md)), the same way you install any application.

## 3. Getting and Checking the Image

Next, download the Ubuntu **image**: a single file (an `.iso`) containing the installer, from the official Ubuntu website only. Downloading an operating system from an unofficial site is a real risk: a tampered image could contain malware, and you would be installing it yourself. This is the supply-chain idea from Security Fundamentals, made concrete.

So, two security habits from the very start:

- **Download only from the official source** (`ubuntu.com`). Never from a random mirror, link, or torrent you do not trust.
- **Check the image is genuine.** Official downloads come with a **checksum** (a hash, How Computers Work lesson 2's fingerprint idea, studied fully in Cryptography): a long value that uniquely identifies the correct file. After downloading, you compute the hash of your file and compare it to the official value. If they match, your file is the real, unmodified image. If not, do not use it.

You do not need to master hashing yet; just know the habit, verify what you download, especially something as powerful as an operating system. Ubuntu's download page explains how to check the hash for your system.

## 4. Creating the Virtual Machine

With the hypervisor installed and the Ubuntu image downloaded, create the VM. The exact clicks differ by hypervisor, but the steps are the same everywhere:

1. **Create a new virtual machine** and point it at the Ubuntu `.iso` you downloaded.
2. **Give it resources.** A reasonable starting point: 2 CPU cores, 4 GB of RAM, and 25 GB of disk. (Recall from How Computers Work what each means.) You can adjust later.
3. **Start the VM.** It boots from the installer image, exactly as a real computer boots from a USB stick (the boot process, How Computers Work lesson 9).

<!-- SCREENSHOT TODO: file: 03-linux/vm-create-settings.png; Device: Mac/PC, your hypervisor; Show: the new-VM settings screen with the Ubuntu ISO selected and 2 CPU / 4 GB RAM / 25 GB disk set. Crop to the dialog; no personal info visible. -->

The VM is a computer-within-a-computer: it has its own virtual disk, memory, and network, all isolated from your real machine (How Computers Work lesson 10). When it starts, you are watching a fresh computer boot for the first time.

## 5. First Boot and Login

The VM boots into the Ubuntu **installer**. Follow its prompts; the defaults are sensible for learning:

1. Choose your language and keyboard.
2. Choose a normal installation.
3. When asked about the disk, let it use the whole (virtual) disk, remember, this is the VM's virtual disk, not your real one, so "erase disk" here is completely safe.
4. **Create your user account.** Use the name **`dara`** (this course's examples all use `dara`), pick a password you will remember, and set the computer's name to **`ubuntu`**. Your prompt will then read `dara@ubuntu`, matching every example in this course.
5. Let the installer finish and restart the VM.

<!-- SCREENSHOT TODO: file: 03-linux/ubuntu-create-account.png; Device: the Ubuntu installer; Show: the "Who are you?" screen with name dara and computer name ubuntu filled in. Crop to the form; use a throwaway password, not shown. -->

After it restarts, you log in with your password and reach the Ubuntu desktop. Open the **Terminal** application, the window where you type commands, and you will see your first prompt:

```console
dara@ubuntu:~$
```

That prompt is where you will live for the rest of this course. The next lesson explains exactly what every part of it means. You now have a real, working Linux machine.

## 6. Snapshots: Your Safety Net

Before you do anything else, learn the most important safety habit for a VM: the **snapshot** (How Computers Work, lesson 10). A snapshot saves the VM's entire state so you can return to it instantly.

Right now, you have a clean, freshly installed Ubuntu. **Take a snapshot and name it something like "clean install".** In your hypervisor, this is a menu option (often "Take Snapshot" or "Snapshots"). It takes a few seconds.

Why do this immediately, and often?

- **Mistakes become free.** This course has you run powerful commands. If you ever break your VM, delete the wrong files, misconfigure something, lock yourself out, you simply **restore the snapshot** and you are back to clean in seconds, instead of reinstalling.
- **You can experiment boldly.** Snapshots are what let you try things without fear, which is how you learn fastest.
- **It is a real security practice.** Analysts snapshot a VM before detonating malware, then restore it afterward (Malware Analysis, course 29). You are building the habit now.

Get into the rhythm: **snapshot before anything risky, and whenever your VM is in a known-good state.** It is the single habit that makes learning Linux (and later, handling malware) safe.

## 7. The First Update

One real task before you finish, and it is a security task. A freshly installed system is already somewhat out of date, because fixes have been released since the image was built. So the first thing to do on any new Linux system is **update it**, applying the latest security patches (the "updates are a security control" idea from Security Fundamentals and How Computers Work).

In the terminal, you run two commands (you will learn exactly how they work in lesson 7 on packages; for now, just run them):

```console
dara@ubuntu:~$ sudo apt update
dara@ubuntu:~$ sudo apt upgrade
```

- `sudo` runs the command with administrator power (you will meet it properly in lesson 5); it will ask for your password.
- `apt update` refreshes the list of available software and updates.
- `apt upgrade` downloads and installs the updates. Type `y` to confirm when asked.

When it finishes, your system has the latest security fixes. **Take another snapshot now** (name it "updated"), so you have a clean, fully updated starting point to return to.

You have done a great deal: you understand why a VM is the right place to learn, you have installed Ubuntu, logged in, taken your safety-net snapshots, and applied the first security updates. You have a real Linux system that is yours to explore and impossible to permanently break. In the next lesson, we start using it properly: the shell, the prompt, and the Linux file system.

---

## Common Mistakes

**1. Installing Linux on your real computer instead of a VM.** You will run commands that can break a system. A VM contains any mistake; your real machine and data stay safe.

**2. Downloading Ubuntu from an unofficial site.** An operating system from an untrusted source could be tampered with. Use the official site, and check the hash.

**3. Skipping snapshots.** Snapshots make mistakes free and learning fearless. Take one right after install, after updating, and before anything risky.

**4. Panicking about "erase disk" in the installer.** It means the VM's *virtual* disk, which is empty and isolated. Your real disk is untouched.

**5. Not updating a fresh install.** A new system is already behind on security fixes. Update it first, every time, on every new Linux system.

## Summary

| Step | Remember |
|---|---|
| Use a VM | Safe, snapshot-able, isolated, and yours (satisfies "only test what you own") |
| Distribution | Ubuntu LTS desktop for this course; Kali comes later as the attacker machine |
| Get the image | Official source only; verify the checksum (a hash) |
| Create the VM | Point it at the ISO; ~2 CPU, 4 GB RAM, 25 GB disk; boot it |
| Account | User `dara`, computer `ubuntu`, so your prompt matches the course |
| Snapshot | Save a clean state; restore in seconds; do it before anything risky |
| First update | `sudo apt update && sudo apt upgrade`, then snapshot again |

## Check Your Understanding

1. Give two reasons you install Linux in a VM instead of on your real computer.
2. Which distribution does this course use, and why not Kali?
3. Why must you download the Ubuntu image only from the official site, and what does checking the checksum prove?
4. In the installer, why is "erase disk" safe here?
5. What user name and computer name does the course use, and why does that matter?
6. What does a snapshot let you do, and when should you take one?
7. Why is updating a freshly installed system a security task, and which commands do it?

**Answers**

1. Any two: safety (mistakes harm only the VM); snapshots (restore a clean state in seconds); it keeps your real computer clean; it satisfies "only test what you own" because the VM is yours.
2. Ubuntu (LTS desktop). Not Kali because Ubuntu is beginner-friendly and right for learning fundamentals; Kali's attack tools come later, in the lab and pentesting courses.
3. Because an OS from an untrusted source could be tampered with (a supply-chain risk); checking the checksum (hash) proves the file matches the official, unmodified image.
4. Because it refers to the VM's virtual disk, which is empty and isolated from your real machine, so nothing real is erased.
5. User `dara` and computer `ubuntu`, so the prompt reads `dara@ubuntu` and matches every example in the course, avoiding confusion.
6. It saves the VM's entire state so you can restore it instantly. Take one after install, after updating, and before anything risky.
7. Because a fresh image is already behind on security fixes released since it was built, so updating applies the latest patches (a security control). The commands are `sudo apt update` then `sudo apt upgrade`.

## Practice

This practice is the lesson: set up your VM.

1. Install a hypervisor (VirtualBox, UTM, or VMware) for your computer, and download Ubuntu LTS from the official site. Check the checksum if you can.
2. Create a VM (about 2 CPU, 4 GB RAM, 25 GB disk), install Ubuntu with user `dara` and computer name `ubuntu`, and log in. Open the Terminal and confirm your prompt reads `dara@ubuntu:~$`.
3. Take a snapshot named "clean install". Then run `sudo apt update` and `sudo apt upgrade`, and take a second snapshot named "updated".

Write one sentence noting what each snapshot captures, so you know which to restore to later.

### A Worked Example

A completed setup: VirtualBox installed on a PC (or UTM on an Apple Silicon Mac); Ubuntu LTS downloaded from ubuntu.com and its SHA-256 checksum matched the official value; a VM with 2 CPUs, 4 GB RAM, and a 25 GB virtual disk; Ubuntu installed with user `dara` on computer `ubuntu`; the Terminal showing `dara@ubuntu:~$`; a snapshot "clean install" taken right after install, then `sudo apt update && sudo apt upgrade` run, then a snapshot "updated". Restore "updated" to return to a patched, clean system; restore "clean install" to go all the way back.
