# Section 2: Binary, Hexadecimal, and Bits — Video Scripts

Two videos, about 9 minutes in total. Slide IDs match [`slides.md`](slides.md). The console demos use Python and `xxd`; have a terminal ready if you want to run them live.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Bits, Bytes, and Binary | 1.1–1.5 | about 4.5 min |
| 2 | Hex, Bitwise, and Hex Dumps | 2.1–2.6 | about 4.5 min |

---

## Video 1 — Bits, Bytes, and Binary

### 1.1 — Title

**Show:** slide 1.1

**Say:** Last lesson we said everything inside a computer is numbers, stored as on-and-off switches. This lesson opens up those switches. We'll meet bits and bytes, learn to count in binary, and see that it's just the counting you already know with two digits instead of ten.

**Time:** about 0:25

### 1.2 — Bits and bytes

**Show:** slide 1.2

**Say:** At the very bottom, a computer stores everything with switches that are either off or on. We write off as zero and on as one. One of these switches is a bit, short for binary digit, and it's the smallest piece of information there is: one yes-or-no. One bit can't say much, only two things, so computers group bits together. Eight bits make one byte, and the byte is the basic unit a computer works with. How much can a byte hold? Eight bits, each 0 or 1, give two to the power of eight, which is 256 different patterns, from all zeros to all ones. So one byte represents 256 values, usually the numbers 0 to 255. Remember those two numbers, 256 and 255; they'll show up constantly.

**Time:** about 0:55

### 1.3 — Counting in binary

**Show:** slide 1.3

**Say:** The numbers you use every day are decimal, base 10: ten digits, and each column is worth ten times the one to its right, ones, tens, hundreds. Binary is base 2: only two digits, 0 and 1, and each column is worth two times the one to its right, not ten. So the columns are 1, 2, 4, 8, 16, 32, 64, 128, each a doubling. To read a binary number, you just add up the column values wherever there's a 1. Take `0000 1101`: there are 1s in the 8 column, the 4 column, and the 1 column, so that's 8 plus 4 plus 1, which is 13. And `1111 1111`, all eight columns, is 255. That's all binary is: the same counting you know, with two digits, because a switch has exactly two states.

**Time:** about 0:55

### 1.4 — Converting, and why you don't memorize it

**Show:** slide 1.4

**Say:** Converting goes both ways. Binary to decimal: add the column values where there's a 1. Decimal to binary: take the biggest power of two that fits, subtract it, and repeat. For 13, the biggest that fits is 8, leaving 5, then 4, leaving 1, then 1. So the 8, 4, and 1 columns are on. But here's the honest truth: you rarely do this by hand in real work, a tool does it. Here's Python, shown exactly as it ran: `bin(13)` gives `0b1101`, where the `0b` just means "this is binary", and `int("1010", 2)` reads binary 1010 back as 10. So understand what the columns mean, and let a tool do the arithmetic.

**Time:** about 0:50

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: a bit is one switch, eight bits make a byte, and a byte holds 256 values, 0 to 255. Binary columns double, 1, 2, 4, 8, and you read a binary number by adding the columns that have a 1. And don't memorize conversions, understand the columns, because tools convert for you. Next, the shorter way everyone actually writes bytes: hexadecimal.

**Time:** about 0:25

---

## Video 2 — Hex, Bitwise, and Hex Dumps

### 2.1 — Title

**Show:** slide 2.1

**Say:** Binary is correct, but eight characters per byte is a lot to read. In this video we meet hexadecimal, the short way to write bytes that security tools use everywhere, then bitwise operations, and finally how to read a hex dump.

**Time:** about 0:20

### 2.2 — Hexadecimal

**Show:** slide 2.2

**Say:** Binary `11111111` is eight characters for one byte, and easy to miscount, so tools almost always show bytes in hexadecimal, base 16, or just hex. Hex has sixteen digits: 0 through 9 as usual, then it borrows letters for ten to fifteen, A is 10, B is 11, up to F is 15. Why sixteen? Because 16 is two to the fourth, so one hex digit is exactly four bits, and two hex digits are exactly one byte. That neat fit is the whole reason hex is used, it's a short, exact way to write bytes. So one byte, which is `00000000` to `11111111` in binary, is just `00` to `FF` in hex, always two characters. You'll see it written with a `0x` prefix, so `0xFF` means hex FF, which is 255.

**Time:** about 0:55

### 2.3 — Bitwise: AND, OR, XOR, NOT

**Show:** slide 2.3

**Say:** Because everything is bits, computers can work on bits directly, one position at a time, and these bitwise operations are everywhere, in permissions, network masks, and simple ciphers. Line up two numbers and compare each position. AND gives 1 only if both bits are 1. OR gives 1 if either is 1. XOR, exclusive or, gives 1 if the bits are different. And NOT just flips every bit. In the demo, `1100` XOR `1010` is `0110`, a 1 wherever the two differ. XOR deserves special attention: apply the same XOR value twice and you get the original back, which is exactly why it's the heart of many simple ciphers. You'll meet it again in the Cryptography course.

**Time:** about 0:50

### 2.4 — Reading a hex dump

**Show:** slide 2.4

**Say:** Now let's put it together with a hex dump, a view of raw bytes shown in hex that security people use constantly, for files, memory, and network captures. Here's the text `Hi!` dumped with the `xxd` tool. Read it in three columns. On the left, `00000000` is the offset, how far into the data we are, in hex, here the very start. In the middle, `4869 21` is the bytes themselves in hex, three bytes: `48`, `69`, `21`. And on the right, `Hi!` is those same bytes shown as text. So the letter H is the byte `0x48`, i is `0x69`, and the exclamation mark is `0x21`. Why those exact numbers? That's text encoding, which is the whole next lesson.

**Time:** about 0:55

### 2.5 — Same bits, different meaning

**Show:** slide 2.5

**Say:** One more important idea before we finish. A byte's bits are fixed, but what number they mean depends on how the program reads them. The byte `1111 1111` is 255 if you read it as an unsigned number, but it's minus one if you read it as a signed number, using a scheme called two's complement. The bits are identical; only the interpretation differs. This is the lesson-1 idea coming back, numbers mean nothing until something decides how to read them, and it's the source of a whole family of bugs, integer overflows and sign errors, that you'll study in Binary Exploitation.

**Time:** about 0:45

### 2.6 — Recap

**Show:** slide 2.6

**Say:** To recap: hex is a short, exact way to write bytes, two digits per byte, with a `0x` prefix. AND, OR, XOR, and NOT work directly on bits, and XOR underlies simple ciphers. A hex dump is offset, then hex bytes, then text, and it's the everyday view of raw data in security. And the same bits can mean different numbers depending on how they're read. Next lesson, we answer the question we left hanging: why is the letter H the byte `0x48`? That's how text becomes numbers, with ASCII, Unicode, and Base64.

**Time:** about 0:35
