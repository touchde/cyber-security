# LINUX FOR SECURITY — COMPLETE TABLE OF CONTENTS

The third Foundation course. It assumes Security Fundamentals (01) and How Computers Work (02). It teaches the Linux command line, the native environment of security work, from the first login to hardening a server. Every lesson is hands-on: you run real commands on a real Linux system (an Ubuntu virtual machine). Commands are introduced from zero.

## Chapter 1: Why Security People Use Linux
1. What Linux Is
2. Open Source, and Why It Matters for Security
3. Where Linux Runs: Servers, Devices, and the Cloud
4. Why Security Tools Live on Linux
5. Distributions, and Which to Use
6. The Command-Line Mindset
7. What This Course Covers

## Chapter 2: Installing Linux in a Virtual Machine
1. Why a Virtual Machine
2. Choosing a Distribution: Ubuntu and Kali
3. Getting and Checking the Image
4. Creating the Virtual Machine
5. First Boot and Login
6. Snapshots: Your Safety Net
7. The First Update

## Chapter 3: The Shell and the File System
1. What a Shell Is
2. The Prompt, and Your First Commands
3. The Linux File System Tree
4. Moving Around: pwd, cd, and ls
5. Absolute and Relative Paths
6. Your Home Directory, and Hidden Files
7. Getting Help: man and --help

## Chapter 4: Files, Text, and Editors
1. Creating, Copying, Moving, and Deleting Files
2. Looking Inside Files: cat, less, head, and tail
3. Editing a File: nano
4. Wildcards
5. Finding Files: find and locate
6. File Timestamps, and What They Tell You

## Chapter 5: Users, Groups, and Permissions
1. Users, and the root Account
2. Becoming root Safely: sudo
3. Groups
4. Reading Permissions: rwx
5. Changing Permissions: chmod
6. Changing Ownership: chown
7. Least Privilege on the Command Line

## Chapter 6: Processes and Services
1. What Is Running: ps and top
2. Foreground, Background, and Jobs
3. Stopping a Process: kill and signals
4. Services and systemd
5. Controlling Services: systemctl
6. What Is Listening on the Machine

## Chapter 7: Packages and Updates
1. How Software Is Installed on Linux
2. The Package Manager: apt
3. Installing and Removing Software
4. Updating the Whole System
5. Repositories, and Where Software Comes From
6. Why Updates Are a Security Control

## Chapter 8: Pipes, Redirection, and Text Tools
1. Input, Output, and Error Streams
2. Redirection: Saving Output to Files
3. Pipes: Joining Commands
4. Searching Text: grep
5. Cutting and Counting: cut, sort, uniq, wc
6. Building a Pipeline: A First Log Analysis

## Chapter 9: Networking Commands
1. Your Machine's Network Identity: ip
2. Testing Reachability: ping
3. What Connections Are Open: ss
4. Looking Up Names: dig and host
5. Talking to Web Servers: curl and wget
6. A Networking Troubleshooting Checklist

## Chapter 10: Logs and the systemd Journal
1. Why Logs Matter in Security
2. Where Logs Live: /var/log
3. The systemd Journal: journalctl
4. Reading Authentication Logs
5. Log Rotation
6. What an Attacker Does to Logs

## Chapter 11: SSH and Remote Access
1. What SSH Is
2. Connecting to a Remote Machine
3. SSH Keys vs. Passwords
4. Copying Files: scp and sftp
5. The Attacker's View of SSH
6. Hardening SSH

## Chapter 12: Hardening a Linux Server
1. What Hardening Means
2. Users and Least Privilege
3. Updating and Removing What You Do Not Need
4. A Host Firewall: ufw
5. Protecting SSH, and fail2ban
6. Checking Your Work
7. A Server Hardening Checklist

## Chapter 13: Practical Project: A Hardened Web Server
1. The Goal
2. Installing a Web Server
3. Applying the Hardening Checklist
4. Verifying From the Outside
5. What You Built, and What Comes Next
