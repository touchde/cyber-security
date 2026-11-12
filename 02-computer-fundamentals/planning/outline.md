# HOW COMPUTERS WORK — COMPLETE TABLE OF CONTENTS

The second Foundation course. It assumes only Security Fundamentals (course 01); no programming and no prior computer-internals knowledge. It explains what a computer is and how it runs, from bits to the boot process, because you cannot attack, defend, or analyze what you do not understand. A little code appears (hex, Base64, a tiny C program), always explained from zero.

## Chapter 1: What a Computer Does
1. The Idea of a Computer
2. Input, Processing, Output, and Storage
3. Hardware and Software
4. Everything Inside Is Numbers
5. Instructions and Data
6. Why Security People Must Understand the Machine
7. A Map of This Course

## Chapter 2: Binary, Hexadecimal, and Bits
1. Bits and Bytes
2. Counting in Binary
3. Converting Between Binary and Decimal
4. Hexadecimal, and Why It Is Used
5. Units: Kilobytes, Megabytes, and Bits vs. Bytes
6. Bitwise Thinking: AND, OR, XOR, and NOT
7. How Negative Numbers Are Stored
8. Reading a Hex Dump

## Chapter 3: Representing Text: ASCII, Unicode, and Base64
1. How Text Becomes Numbers
2. ASCII
3. The Problem of Other Languages
4. Unicode and UTF-8
5. Khmer and Other Scripts in Unicode
6. Base64: Encoding, Not Encryption
7. URL and Percent Encoding
8. Why Encoding Matters in Security

## Chapter 4: The CPU, Memory, and Storage
1. The CPU and the Fetch–Execute Cycle
2. Registers
3. RAM: Fast and Temporary
4. Storage: Slower and Permanent
5. The Memory Hierarchy and Cache
6. Clock Speed, Cores, and Threads
7. Why "Volatile" Matters (a Forensics Preview)

## Chapter 5: What an Operating System Does
1. The OS as the Manager
2. The Kernel
3. User Space and Kernel Space
4. System Calls
5. Drivers and Hardware
6. Multitasking
7. Users, Permissions, and the OS as a Security Boundary

## Chapter 6: Processes, Threads, and Memory
1. What a Process Is
2. How a Process Is Laid Out in Memory
3. The Stack and the Heap
4. Threads
5. Virtual Memory and Isolation
6. How the OS Keeps Processes Apart
7. Looking at Running Processes

## Chapter 7: Files and File Systems
1. What a File Really Is
2. File Systems
3. Paths and Directories
4. Metadata and Permissions
5. File Types and Magic Bytes
6. Deleting vs. Really Deleting (a Forensics Preview)
7. Mounting and Devices

## Chapter 8: How Programs Are Built and Run
1. From Source Code to a Running Program
2. Compiled vs. Interpreted Languages
3. The Build Pipeline: Compile and Link
4. Machine Code and Assembly
5. Libraries: Static and Dynamic
6. What an Executable File Is (ELF and PE)
7. Why This Matters for Reversing and Malware

## Chapter 9: The Boot Process
1. From Power Button to Desktop
2. Firmware: BIOS and UEFI
3. The Bootloader
4. Loading the Kernel
5. Init and the First Processes
6. Where Malware Hides at Boot
7. Secure Boot

## Chapter 10: Virtual Machines and Containers
1. What Virtualization Is
2. Hypervisors and Virtual Machines
3. Containers, and How They Differ From VMs
4. Why Security Work Relies on Both
5. Snapshots and Clean States
6. The Limits of Isolation

## Chapter 11: A First Look at C and Memory
1. Why Security People Learn a Little C
2. A Tiny C Program
3. Variables Are Places in Memory
4. Pointers, Gently
5. The Stack and a Buffer
6. What a Buffer Overflow Is (a Preview)
7. Memory Safety, and Why It Matters

## Chapter 12: Practical Project: Explore a Running System
1. The Goal: See the Ideas for Real
2. Inspecting Processes and Memory
3. Hex-Dumping and Identifying Files
4. Watching the Boot and System Logs
5. Tying It Together
