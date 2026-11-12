# Section 3: The Shell and the File System — Video Scripts

Two videos, about 9 minutes in total. Slide IDs match [`slides.md`](slides.md). The teacher types the commands live in the Ubuntu VM. Have the Terminal open before recording.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | The Shell, the Prompt, and the File System | 1.1–1.5 | about 4.5 min |
| 2 | Moving Around, Paths, and Getting Help | 2.1–2.5 | about 4.5 min |

---

## Video 1 — The Shell, the Prompt, and the File System

### 1.1 — Title

**Show:** slide 1.1

**Say:** You've got your Ubuntu VM running and the Terminal open. This is where the hands-on course truly begins. In this video, what a shell actually is, what every part of the prompt means, and the shape of the Linux file system.

**Time:** about 0:25

### 1.2 — What a shell is

**Show:** slide 1.2

**Say:** When you open the Terminal, you're talking to a shell: a program that reads the commands you type, runs them, and shows you the result. The shell sits between you and the operating system, you type a command, the shell asks the kernel to do it, and the output comes back. Ubuntu's default shell is called Bash. Think of it as a conversation, one line at a time: you type a command and press Enter, the shell runs it, the output appears below, and a fresh prompt waits for your next command. Type, run, read, repeat, that loop is how all command-line work happens, from this first lesson to the most advanced attack later. It feels bare at first, but it's the most direct, honest way to use a computer: you say exactly what you want, and you see exactly what happens.

**Time:** about 0:55

### 1.3 — The prompt tells you who and where

**Show:** slide 1.3

**Do:** Point at each part of the prompt, then run `whoami`.

**Say:** Before you type anything, the shell shows a prompt, and every part of it tells you something. `dara` is your username, who you are. `ubuntu` is the computer's name, the one you set during install. The tilde is where you are right now, shorthand for your home directory. And the dollar sign means you're a normal user, if you ever see a hash sign there instead, you're root, the all-powerful account, and that's a sign to be careful. So the whole thing reads: the user dara, on the computer ubuntu, in the home directory, as a normal user. That little line answers the two questions every security person asks on a system: who am I, and where am I. Let's run our first command, whoami, which just prints your username: dara. The shell ran it, printed the answer, and showed a new prompt. That's the whole rhythm.

**Time:** about 0:55

### 1.4 — One tree, rooted at /

**Show:** slide 1.4

**Say:** Before we move around, you need the map. In How Computers Work you learned that files live in directories forming a tree. Linux organizes everything into one single tree, starting from a top called the root, written as a single slash. There are no separate drive letters like Windows' C-drive; every disk, every file, every device hangs somewhere off that one slash. A few directories matter again and again. Home holds each user's personal files, like slash-home-slash-dara. etc holds system configuration. var holds data that changes, especially logs, in slash-var-slash-log, which is where evidence of activity is kept, and we'll use it in the logs lesson. And usr and bin hold the installed programs and core commands. Don't memorize them all; just hold the shape: one tree rooted at slash, with home for users, etc for configuration, and var-log for logs.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: the shell, Bash, reads your commands, runs them, and shows the output, type, run, read, repeat. The prompt tells you the user, the computer, where you are, and whether you're a normal user or root. And Linux has one file system tree from the root slash, with home, etc, and var-log the places that matter most. Next, the commands that move you through that tree, and how to get help.

**Time:** about 0:30

---

## Video 2 — Moving Around, Paths, and Getting Help

### 2.1 — Title

**Show:** slide 2.1

**Say:** Now let's actually move around. In this video: the three commands you'll use constantly, the difference between two kinds of path, hidden files, and how to get help on any command.

**Time:** about 0:20

### 2.2 — Moving around: pwd, ls, cd

**Show:** slide 2.2

**Do:** Run `pwd`, then `ls`, then `cd Documents`, then `cd ..`, watching the prompt change.

**Say:** Three commands let you move and see. `pwd`, print working directory, tells you where you are, here slash-home-slash-dara, which is what the tilde meant. `ls`, list, shows what's in the current directory, the standard home folders. And `cd`, change directory, moves you somewhere else; when I cd into Documents, watch the prompt change from tilde to tilde-slash-Documents, the shell always shows where you are. To go back up one level to the parent, use cd dot-dot, that dot-dot from How Computers Work. And cd on its own, with nothing after it, always takes you home. With just these three, you can navigate the entire system.

**Time:** about 0:55

### 2.3 — Absolute vs relative paths

**Show:** slide 2.3

**Say:** When you tell a command where something is, you give a path, and there are two kinds. An absolute path starts from the root slash and names the full route, so it works from anywhere, like slash-home-slash-dara-slash-Documents. A relative path starts from where you are now, so if you're in your home directory, just "Documents" means the same place. Two shortcuts appear in relative paths: a single dot means here, and dot-dot means up one level. And this matters for security, because as we saw in How Computers Work, that dot-dot lets a careless program be pushed out of where it should stay, which is the path-traversal attack. Understanding absolute versus relative paths, and what dot-dot does, is the foundation for both using Linux and understanding that whole family of web attacks.

**Time:** about 0:55

### 2.4 — Hidden files, and getting help

**Show:** slide 2.4

**Do:** Run `ls`, then `ls -a`, then `man ls` (quit with `q`), then `ls --help`.

**Say:** But ls didn't show everything. Linux has hidden files: any file whose name starts with a dot is hidden from a normal listing, usually configuration files, hidden just to keep listings tidy. To see them, add the dash-a flag, for all, and now you see dot-files like dot-bashrc, your shell settings. Here's the security lesson: hidden does not mean secret or safe. These files are trivially visible with ls dash-a, and attackers often hide malicious files with dot-names, hoping a casual look misses them, so an investigator always lists hidden files. ls dash-a is a reflex. Finally, you'll never memorize every command, and you don't need to, because Linux documents itself. man, for manual, opens the full manual page for a command, press q to quit. And most commands accept dash-dash-help for a quick summary. Between the two, you can always find out what a command does, which is exactly how real professionals work: not memorizing, but knowing how to look things up.

**Time:** about 1:05

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: pwd, ls, and cd navigate the tree, with cd dot-dot going up and cd going home. Paths are absolute, from the root and working anywhere, or relative, from where you are, and dot-dot is also the path-traversal trick. ls dash-a reveals hidden files, because hidden isn't secret. And man and dash-dash-help mean you look things up instead of memorizing. You now have the foundation of every Linux session. In the next lesson, we start working with files themselves: creating, viewing, editing, and finding them.

**Time:** about 0:30
