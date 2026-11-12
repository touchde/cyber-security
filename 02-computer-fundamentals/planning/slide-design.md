# How Computers Work — Slide and Book Design

Follows the shared [style guide](../../STYLE-GUIDE.md), except that each course has its own look. The theme is "circuit": the charcoal-and-teal feel of a circuit board, because this course opens up the machine and looks inside.

| | How Computers Work |
|---|---|
| Title slides | Deep charcoal, thin teal "trace" lines, the course mark, title in white |
| Headings and accents | Teal on charcoal; charcoal on light slides |
| Body slides | Light background (cool grey-white), charcoal headings, dark text |
| Tables | Charcoal header row, light rows, teal rule under the header |
| Code panels | Near-black with teal keywords, amber strings, mint numbers (JetBrains/Space Mono) |
| Output blocks | Pale, with a teal left edge |
| Recap slides | Pale teal, with a charcoal top edge |
| Fonts | Space Grotesk (text) and Space Mono (code), both open-licensed |
| Khmer font | Google Sans |
| Book cover | Charcoal with a teal circuit-trace motif, the course mark, title in white, author and date |

Corners stay square. Hex dumps, binary, and C code use the plain dark code panel with a light output box under it, as in the style guide.

## Logo

- No brand logo. The **course mark** is a charcoal tile with a white "memory/chip" icon from Material Symbols (Apache License 2.0), suggesting the hardware this course opens up. Made by the shared `assets/build_course_icons.py`.
- **Credits:** "Course mark icon from Material Symbols by Google, Apache License 2.0."

## Diagrams

Drawn for this course in `assets/diagrams/02-computer-fundamentals/` once the diagrams are built.

| Lesson | Diagram |
|---:|---|
| 1 | Input → processing → output → storage; hardware vs software layers |
| 2 | A byte as 8 bits; a binary→hex→decimal conversion strip |
| 3 | A character → code point → UTF-8 bytes → Base64 pipeline |
| 4 | The fetch–execute cycle; the memory hierarchy as a pyramid |
| 6 | Process memory layout (stack, heap, data, code) with the stack growing down |
| 8 | Source → compile → link → executable → run |
| 9 | The boot chain: firmware → bootloader → kernel → init |
| 10 | VMs vs containers, side by side |
| 11 | A stack frame with a buffer, and how an overflow runs past it |

## Screenshots

Few are needed. Where one helps (a real hex dump, a process list, a boot log), it is captured from our own machine or lab, with no private data, following the style guide's screenshot rules.
