# Section 10: Virtual Machines and Containers — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Virtualization and VMs | 1.1–1.5 | about 4 min |
| 2 | Containers, Snapshots, and the Limits of Isolation | 2.1–2.5 | about 4 min |

---

## Video 1 — Virtualization and VMs

### 1.1 — Title

**Show:** slide 1.1

**Say:** So far, one computer has run one operating system. This lesson breaks that assumption, and it's the technology behind the practice lab you'll build and behind the whole cloud. We'll see what virtualization is, meet virtual machines and hypervisors, and see why security work depends on them.

**Time:** about 0:25

### 1.2 — What virtualization is

**Show:** slide 1.2

**Say:** Virtualization lets one physical computer pretend to be several separate computers, each running its own operating system, all at the same time and all kept apart. The trick is the same idea as virtual memory, but one level up. Virtual memory gave each process its own private view of memory; virtualization gives each operating system its own private view of a whole computer, its own CPU, memory, disk, and network, faked convincingly enough that the OS inside believes it's on real, dedicated hardware. Why is this so useful in security? Isolation: each virtual computer is sealed off from the others and from the real host. Safety: you can run dangerous or untrusted software, even real malware, inside one, study it, and throw the whole thing away. And efficiency: one powerful server can host many virtual servers, which is the foundation of cloud computing.

**Time:** about 0:55

### 1.3 — Virtual machines and hypervisors

**Show:** slide 1.3

**Say:** The most complete form is the virtual machine, a VM: a full, simulated computer running a complete operating system of its own, on top of your real one. On one laptop you could run a Windows VM and three Linux VMs at once, each behaving like a separate PC. Making this work is a special piece of software called a hypervisor: the manager that creates VMs and shares the real hardware among them, deciding which VM gets the CPU and how much memory each has, a manager of operating systems, the way an OS is a manager of programs. Tools you'll use include VirtualBox, VMware, and UTM on Apple Silicon Macs. A VM is a complete, independent computer: its own full OS, its own virtual hardware, strongly isolated. The cost is weight: each runs a full OS, so VMs use a lot of memory and disk and take time to start, because they're booting a whole computer.

**Time:** about 0:55

### 1.4 — Why security relies on VMs

**Show:** slide 1.4

**Say:** Virtualization isn't a side topic; it's woven through security. Your home lab is built on VMs: you'll run an attacker machine, often Kali Linux, and several vulnerable targets as VMs on your own computer, on an isolated virtual network. That's what makes it safe and legal to practise attacks, everything is your own, contained, and disposable, so the "only test what you own" rule is satisfied by design. Malware is analyzed in VMs: you detonate real malicious software in a disposable VM, watch it, and discard it. And the cloud is virtualization at scale: cloud servers are VMs and containers on providers' hardware. So this lesson is unusually practical, the very next hands-on things you do in this program rest on it.

**Time:** about 0:50

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: virtualization lets one computer run several isolated systems at once. A VM is a full simulated computer with its own OS, and a hypervisor runs them. And your lab, malware analysis, and the cloud all depend on VMs. Next, a lighter alternative to VMs, the snapshot feature that makes a lab so forgiving, and the important limits of all this isolation.

**Time:** about 0:25

---

## Video 2 — Containers, Snapshots, and the Limits of Isolation

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video: containers, a lighter form of isolation and how they differ from VMs; snapshots, the "undo for a whole computer"; and the crucial point that isolation, however strong, is never absolute.

**Time:** about 0:20

### 2.2 — Containers vs VMs

**Show:** slide 2.2

**Say:** A container is a lighter form of isolation. Like a VM, it packages a program in its own isolated environment. Unlike a VM, it doesn't run its own full operating system; all the containers on a machine share the host's single kernel, while each still gets its own isolated view of the file system, processes, and network. Side by side: a VM runs its own OS kernel, is heavy, gigabytes and slow to start, and is very strongly isolated. A container shares the host kernel, is light, megabytes and starts in seconds, and is strongly but less isolated. The analogy: a VM is a separate house with its own foundation and utilities, its own OS, while a container is an apartment in one building, its own locked door and rooms, but sharing the building's foundation, the host's kernel. Cheaper and quicker, a bit less independent. The best-known tool is Docker. Key fact: containers are lighter and faster, but share the host kernel, so their isolation is strong but not as strong as a VM's.

**Time:** about 0:55

### 2.3 — Snapshots: undo for a whole machine

**Show:** slide 2.3

**Say:** One VM feature deserves its own mention, because it makes them so valuable: the snapshot. A snapshot saves the entire state of a VM, its disk and its memory, at a moment in time, so you can return to that exact state later, instantly. Why is that powerful? You can experiment without fear: snapshot a clean machine, then try something risky, break things, run malware, make a mess, and when you're done, restore the snapshot and the VM is instantly clean again, as if nothing happened. It's an undo for the whole computer. For malware analysis, you infect a VM, study the damage, then restore a clean snapshot to analyze the sample again from an identical start. And it's a fast reset, seconds, not a slow OS reinstall. The combination of isolation, nothing escapes, and snapshots, reset to clean instantly, is what makes a virtual lab the ideal safe playground.

**Time:** about 0:55

### 2.4 — The limits of isolation

**Show:** slide 2.4

**Say:** But isolation, like every security control, is not perfect, and a good security person knows its limits. The isolation between a VM or container and its host is enforced by software, the hypervisor or the kernel, and software can have flaws. An attack that breaks out of a VM or container to reach the host, or another guest, is called a VM escape or container escape. These are rare and difficult, especially for VMs, and highly prized by attackers precisely because they defeat the isolation everyone relies on. The practical lessons: containers isolate less than VMs, because they share the host kernel, so for truly dangerous code, a VM gives stronger isolation. No isolation is absolute, so for the most dangerous malware, professionals add layers, a dedicated physical machine, an isolated network. And keep the host and hypervisor updated, because the isolation is only as strong as the software enforcing it.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: containers are light and fast but share the host kernel, strong but weaker isolation than a VM. Snapshots let you reset a VM to clean instantly, which is the heart of a safe lab. And isolation is strong but not absolute, escapes exist, so you layer it and patch it. You now understand how one computer can safely run many isolated systems, the foundation of your lab, malware analysis, and the cloud. In the next lesson, we go back down to the metal for a closer, hands-on look at memory with a little C, the ideas the exploitation courses are built on.

**Time:** about 0:35
