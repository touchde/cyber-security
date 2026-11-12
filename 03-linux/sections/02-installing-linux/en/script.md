# Section 2: Installing Linux in a Virtual Machine — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). This lesson is followed hands-on; the teacher installs Ubuntu in a VM on screen. Have a hypervisor and the Ubuntu ISO ready before recording.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Why a VM, and Getting Ubuntu | 1.1–1.5 | about 4 min |
| 2 | Install, Snapshot, and Update | 2.1–2.5 | about 4 min |

---

## Video 1 — Why a VM, and Getting Ubuntu

### 1.1 — Title

**Show:** slide 1.1

**Say:** In this lesson we build the machine you'll use for the rest of the course: a Linux virtual machine. In this first video, why we use a VM instead of your real computer, which Linux to install, and how to get it safely.

**Time:** about 0:25

### 1.2 — Why a virtual machine

**Show:** slide 1.2

**Say:** You will not install Linux directly onto your laptop. Instead you'll run it inside a virtual machine, a full simulated computer running on top of your real one, which you met in How Computers Work. Why? Safety: you'll run commands that can break a system, and in a VM a mistake harms only the VM, never your real computer or data. Snapshots: a VM can be saved and restored in seconds, so if you break something, you restore and you're instantly clean, which makes learning fearless. It keeps your real computer clean, no changes, and when you're done you just delete the VM. And it satisfies the one rule: the VM is yours, so everything you do, including the attacks you'll practise later, happens on a system you own. You run a VM with a hypervisor, the software that creates and runs them, which you install first.

**Time:** about 0:55

### 1.3 — Which distribution

**Show:** slide 1.3

**Say:** From last lesson, a distribution is a packaged version of Linux, and this course uses Ubuntu, specifically the current LTS, long-term support, desktop release, which is stable and supported for years. You'll also hear about Kali, the distribution pre-loaded with offensive tools, but you don't need it for this course, Ubuntu is the right choice for learning fundamentals, and you'll install Kali later as your attacker machine. So: one Ubuntu VM. Pick a hypervisor for your computer: VirtualBox on Windows, Linux, or Intel Macs; UTM on Apple Silicon Macs; or VMware. Install it from its official site, just like any other application.

**Time:** about 0:45

### 1.4 — Get and check the image

**Show:** slide 1.4

**Say:** Next, download the Ubuntu image, a single ISO file containing the installer, and here are two security habits to build from the very start. First, download only from the official site, ubuntu.com, never from a random mirror or torrent, because an operating system from an untrusted source could contain malware, and you'd be installing it yourself, that's the supply-chain risk from Security Fundamentals made concrete. Second, check the image is genuine. Official downloads come with a checksum, a hash, which is that fingerprint idea from How Computers Work. You compute the hash of your downloaded file and compare it to the official value; if they match, your file is the real, unmodified image. You don't need to master hashing yet, just build the habit: verify what you download, especially something as powerful as an operating system.

**Time:** about 0:50

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: install Linux in a VM, because it's safe, snapshot-able, isolated, and yours. Use Ubuntu LTS, with Kali coming later. And download from the official site and check the checksum. Next, we actually install it, take our first snapshot, and run the first update.

**Time:** about 0:25

---

## Video 2 — Install, Snapshot, and Update

### 2.1 — Title

**Show:** slide 2.1

**Say:** Now the hands-on part. In this video we create the VM, install Ubuntu, take a snapshot, which is the most important safety habit, and run the first security update.

**Time:** about 0:20

### 2.2 — Create and install

**Show:** slide 2.2

**Do:** Create a new VM in the hypervisor, point it at the Ubuntu ISO, set 2 CPU / 4 GB RAM / 25 GB disk, and start it.

**Say:** With the hypervisor installed and the image downloaded, create the VM. The clicks differ by hypervisor, but the steps are the same. Create a new virtual machine and point it at the Ubuntu ISO. Give it resources, a good start is 2 CPU cores, 4 gigabytes of RAM, and 25 gigabytes of disk, and recall from How Computers Work what each of those means. Start it, and it boots the installer, exactly like a real computer booting from a USB stick. In the installer, choose your language, a normal install, and when it asks about the disk, let it use the whole virtual disk, this is the VM's disk, empty and isolated, so "erase disk" here is completely safe. Then create your account: use the name dara, which all this course's examples use, pick a password you'll remember, and set the computer name to ubuntu, so your prompt reads dara-at-ubuntu, matching every example. Let it finish and restart, log in, and open the Terminal. You now have a real, working Linux machine.

**Time:** about 1:05

### 2.3 — Snapshots: your safety net

**Show:** slide 2.3

**Do:** In the hypervisor, take a snapshot and name it "clean install."

**Say:** Before you do anything else, learn the most important safety habit for a VM: the snapshot, from How Computers Work. A snapshot saves the VM's entire state so you can return to it instantly. Right now you have a clean, freshly installed Ubuntu, so take a snapshot and name it "clean install", it's a menu option in your hypervisor and takes a few seconds. Why immediately, and often? Because mistakes become free: this course has you run powerful commands, and if you ever break your VM, you just restore the snapshot and you're back to clean in seconds instead of reinstalling. It lets you experiment boldly, which is how you learn fastest. And it's a real security practice, analysts snapshot a VM before detonating malware and restore it afterward. Get into the rhythm: snapshot before anything risky, and whenever your VM is in a known-good state.

**Time:** about 0:55

### 2.4 — The first update

**Show:** slide 2.4

**Do:** In the terminal, run `sudo apt update`, then `sudo apt upgrade`, confirming with `y`.

**Say:** One real task before we finish, and it's a security task. A freshly installed system is already somewhat out of date, because fixes have been released since the image was built. So the first thing to do on any new Linux system is update it, applying the latest security patches. In the terminal you run two commands, and you'll learn exactly how they work in lesson 7; for now just run them. `sudo apt update` refreshes the list of available updates, where sudo runs the command with administrator power and will ask for your password. Then `sudo apt upgrade` downloads and installs the updates, type y to confirm. When it finishes, your system has the latest security fixes, so take another snapshot now, named "updated", giving you a clean, fully patched starting point to return to.

**Time:** about 0:50

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: you created the VM, installed Ubuntu with user dara on computer ubuntu, and opened the Terminal. You took a snapshot right away, named "clean install", so you can restore in seconds and learn fearlessly. And you updated first, with apt update and apt upgrade, then snapshotted again. You now have a real Linux system that's yours to explore and impossible to permanently break. In the next lesson, we start using it properly: the shell, the prompt, and the Linux file system.

**Time:** about 0:30
