# Linux for Security — Slide and Book Design

Follows the shared [style guide](../../STYLE-GUIDE.md), except that each course has its own look. The theme is "terminal": the near-black screen and bright prompt of a Linux command line, because this course lives on the command line.

| | Linux for Security |
|---|---|
| Title slides | Near-black, a bright green prompt mark (`$`), the course mark, title in white |
| Headings and accents | Terminal green on near-black; dark slate on light slides |
| Body slides | Light background (cool grey-white), slate headings, dark text |
| Tables | Slate header row, light rows, green rule under the header |
| Code/terminal panels | Near-black with a green prompt, white commands, muted comments (Fira Code) |
| Output blocks | Pale, with a green left edge |
| Recap slides | Pale green, with a slate top edge |
| Fonts | Work Sans (text) and Fira Code (terminal/code), both open-licensed |
| Khmer font | Google Sans |
| Book cover | Near-black with a terminal-prompt motif (a green `$` and cursor, lines of dimmed commands), the course mark, title in white, author and date |

Corners stay square. Commands and their output use a terminal panel: a green prompt (`dara@ubuntu:~$`), the command in white, and the output below.

## Logo

- No brand logo. The **course mark** is a near-black tile with a white "terminal" icon from Material Symbols (Apache License 2.0). Made by the shared `assets/build_course_icons.py`.
- The Linux penguin (Tux) and distribution logos are not used as the course mark; distributions are referred to by name.
- **Credits:** "Course mark icon from Material Symbols by Google, Apache License 2.0. Linux is a registered trademark of Linus Torvalds. Ubuntu is a trademark of Canonical Ltd. Used here only to refer to the software."

## Diagrams

Drawn for this course in `assets/diagrams/03-linux/` once the diagrams are built.

| Lesson | Diagram |
|---:|---|
| 1 | Where Linux runs (servers, cloud, phones, devices) |
| 3 | The Linux file system tree (/, /home, /etc, /var, …) |
| 5 | The permission string `-rwxr-xr--` broken into owner/group/other |
| 6 | A process list and systemd managing services |
| 8 | A pipeline: command → pipe → command → output |
| 9 | A machine's network identity and open connections |
| 11 | SSH: client, key pair, and server |
| 12 | A hardened server: layers (updates, firewall, SSH keys, least privilege) |

## Screenshots

Captured from the learner's own Ubuntu VM (set up in lesson 2): the installer, the desktop, a terminal. No private data; a generic `dara` account. Follows the style guide's screenshot rules.
