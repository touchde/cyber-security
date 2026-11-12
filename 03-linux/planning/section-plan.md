# Linux for Security — Lesson Plan

Each lesson is one chapter of the [outline](outline.md). This course is **hands-on**: nearly every topic shows a real command and its real output. A lesson that grows too big can split.

**Who it is for:** someone who has finished Security Fundamentals (01) and How Computers Work (02). No Linux and no command-line background.

| # | Lesson | Chapter | Topics | Commands |
|---:|---|---:|---:|---|
| | **Part 1: Getting In** | | | |
| 1 | Why Security People Use Linux | 1 | 7 | None (concepts) |
| 2 | Installing Linux in a Virtual Machine | 2 | 7 | Setup steps |
| 3 | The Shell and the File System | 3 | 7 | `pwd`, `cd`, `ls`, `man` |
| 4 | Files, Text, and Editors | 4 | 6 | `cp`, `mv`, `rm`, `cat`, `nano`, `find` |
| | **Part 2: Users and Processes** | | | |
| 5 | Users, Groups, and Permissions | 5 | 7 | `sudo`, `chmod`, `chown`, `id` |
| 6 | Processes and Services | 6 | 6 | `ps`, `top`, `kill`, `systemctl` |
| 7 | Packages and Updates | 7 | 6 | `apt` |
| | **Part 3: Text, Network, Logs** | | | |
| 8 | Pipes, Redirection, and Text Tools | 8 | 6 | `grep`, `cut`, `sort`, `uniq`, `wc`, `|`, `>` |
| 9 | Networking Commands | 9 | 6 | `ip`, `ping`, `ss`, `dig`, `curl` |
| 10 | Logs and the systemd Journal | 10 | 6 | `journalctl`, `/var/log` |
| | **Part 4: Remote and Hardening** | | | |
| 11 | SSH and Remote Access | 11 | 6 | `ssh`, `ssh-keygen`, `scp` |
| 12 | Hardening a Linux Server | 12 | 7 | `ufw`, SSH config, `fail2ban` |
| 13 | Practical Project: A Hardened Web Server | 13 | 5 | Everything, combined |
| | **Total** | **13 chapters** | **82** | |

## Note on the Environment

All commands are shown as run on **Ubuntu Linux** (the distribution the course installs in lesson 2), in an example account named `dara`. Portable commands (`ls`, `grep`, `chmod`, pipes) produce the same output on any Unix-like system; Linux-specific tools (`apt`, `systemctl`, `journalctl`, `ufw`) are shown in their real Ubuntu form. The learner runs everything in their own VM (lesson 2), which is also where the "only test what you own" rule is satisfied, the VM is theirs.

## Size Estimate

Lesson 1 sets the real numbers. Until then, rough:

| | Estimate |
|---|---:|
| Lessons | 13 |
| Slides | ~200 |
| Videos | ~42 |
| Video time | ~3 hours |
