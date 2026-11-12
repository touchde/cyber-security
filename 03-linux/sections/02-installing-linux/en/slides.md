---
title: "Linux for Security — Section 2: Installing Linux in a Virtual Machine"
videos:
  1: Why a VM, and Getting Ubuntu
  2: Install, Snapshot, and Update
---

<!-- 1.1 -->
<!-- layout: title -->

# Installing Linux in a Virtual Machine

## Video 1 · Why a VM, and Getting Ubuntu

Linux for Security · Section 2

In this video, you will learn:

- Why you install Linux in a VM, not on your real computer
- Which distribution to use
- How to get and check the Ubuntu image

---

<!-- 1.2 -->

# Why a virtual machine

Everything in this course runs in a **VM** (How Computers Work, lesson 10), not on your real laptop.

- **Safety:** a mistake harms only the VM, never your real machine or data.
- **Snapshots:** restore a clean state in **seconds**, learning is fearless.
- **Clean:** no changes to your laptop; delete the VM and nothing remains.
- **The one rule:** the VM is **yours**, so "only test what you own" is met by construction.

Run it with a **hypervisor** (VirtualBox / UTM / VMware).

---

<!-- 1.3 -->

# Which distribution

- **This course: Ubuntu LTS desktop**, friendly, used on real servers, well-documented.
- **Kali** (attacker's distro) comes **later**, in the lab and pentest courses. You don't need it now.

**One Ubuntu VM.**

Pick a hypervisor for your machine:

- **VirtualBox** (Windows/Linux/Intel Mac) · **UTM** (Apple Silicon) · **VMware** (personal use).

---

<!-- 1.4 -->

# Get and check the image

Download the Ubuntu **`.iso`** (the installer) from the **official site only**.

Two security habits from the start:

- **Official source only** (`ubuntu.com`), an OS from an untrusted site could be tampered with (supply-chain risk).
- **Check the checksum** (a hash, course 02): compute your file's hash and compare it to the official value. Match = genuine, unmodified.

Verify what you download, especially an operating system.

---

<!-- 1.5 -->
<!-- layout: recap -->

# Recap: why a VM, and getting Ubuntu

- Install in a **VM**: safe, snapshot-able, isolated, and yours.
- Use **Ubuntu LTS**; Kali comes later.
- Download from the **official site** and **check the checksum**.

**Next video:** install Ubuntu, take a snapshot, and run the first update.

---

<!-- 2.1 -->
<!-- layout: title -->

# Installing Linux in a Virtual Machine

## Video 2 · Install, Snapshot, and Update

Linux for Security · Section 2

In this video, you will learn:

- Creating the VM and installing Ubuntu
- Snapshots: your safety net
- The first update

---

<!-- 2.2 -->

# Create and install

1. **New VM** → point it at the Ubuntu `.iso`.
2. **Resources:** ~2 CPU cores, 4 GB RAM, 25 GB disk.
3. **Start** → it boots the installer (like booting from a USB stick).
4. In the installer: language, normal install, **use the whole (virtual) disk** (safe, it's the VM's disk).
5. **Account:** user **`dara`**, computer **`ubuntu`** → prompt reads `dara@ubuntu`.

<!-- SCREENSHOT TODO: file: 03-linux/ubuntu-create-account.png; the installer account screen with name dara, computer ubuntu. -->

Open **Terminal** → `dara@ubuntu:~$`. You have a real Linux machine.

---

<!-- 2.3 -->

# Snapshots: your safety net

A **snapshot** saves the VM's whole state so you can restore it instantly (course 02).

**Right after install, take a snapshot named "clean install."**

- **Mistakes become free:** break your VM → restore → clean in seconds.
- **Experiment boldly**, how you learn fastest.
- **A real practice:** analysts snapshot before detonating malware (course 29).

**Snapshot before anything risky, and whenever the VM is known-good.**

---

<!-- 2.4 -->

# The first update

A fresh system is already behind on fixes. **Updating is a security task**, do it first on every new Linux system.

```console
dara@ubuntu:~$ sudo apt update
dara@ubuntu:~$ sudo apt upgrade
```

- `sudo`: run with admin power (lesson 5); asks for your password.
- `apt update`: refresh the list of updates.
- `apt upgrade`: install them (`y` to confirm).

Then **snapshot again** ("updated"), a clean, patched starting point.

---

<!-- 2.5 -->
<!-- layout: recap -->

# Recap: install, snapshot, update

- Create the VM, install Ubuntu with user **`dara`** on **`ubuntu`**, open the Terminal.
- **Snapshot** right away ("clean install"), restore in seconds, learn fearlessly.
- **Update first** (`sudo apt update && sudo apt upgrade`), then snapshot again.

**Next lesson:** start using it, the shell, the prompt, and the file system.
