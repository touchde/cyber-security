# Section 3: Representing Text: ASCII, Unicode, and Base64 — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). The console demos use Python, `base64`, and `xxd`.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | How Text Becomes Numbers | 1.1–1.5 | about 4 min |
| 2 | Base64, URL Encoding, and Why It Matters | 2.1–2.5 | about 4 min |

---

## Video 1 — How Text Becomes Numbers

### 1.1 — Title

**Show:** slide 1.1

**Say:** Last lesson ended with a question: why is the letter H the byte `0x48`? This lesson answers it. We'll see how text becomes numbers, meet ASCII, and then meet Unicode and UTF-8, which handle every language in the world, including Khmer.

**Time:** about 0:25

### 1.2 — How text becomes numbers

**Show:** slide 1.2

**Say:** A computer stores only numbers, so to store the letter H it must store a number that stands for H. For that to work, everyone has to agree on which number means which character. That agreement is a character encoding: a table mapping each character to a number. Think of it as a codebook both sides share. The writer turns H into a number using the table, and the reader turns that number back into H using the same table. If the two use different tables, the reader gets the wrong characters, and that's exactly what garbled text is. So the answer to our question is simple: H is `0x48` because a standard table says so, and everyone agreed to use it.

**Time:** about 0:50

### 1.3 — ASCII

**Show:** slide 1.3

**Say:** That table, for basic English, is ASCII, from the 1960s. It gives a number from 0 to 127 to each basic English character, letters, digits, punctuation, space. Since the biggest value is 127, every ASCII character fits in 7 bits. In the demo, H is 72, which is `0x48`, exactly the byte from last lesson's hex dump. A is 65, a is 97, and two patterns are worth noticing. First, the digit character zero is the number 48, not zero, the character and the number are different things, and that catches people constantly. Second, uppercase and lowercase differ by 32: A is 65, a is 97, which is why changing case is so simple. But 128 characters can't hold the world, there's no é, and crucially, no Khmer.

**Time:** about 0:55

### 1.4 — Unicode and UTF-8

**Show:** slide 1.4

**Say:** The fix is Unicode: one giant table that gives every character in every writing system its own unique number, called a code point. Unicode kept ASCII at the bottom, so H is still 72, while Khmer, emoji, and Chinese all have their own code points higher up. But a code point is just a number; the computer still has to store it as bytes, and that's UTF-8's job. UTF-8 is brilliant for two reasons. It's backward-compatible with ASCII: any character 0 to 127 is stored as the same single byte as before, so all existing English text is already valid UTF-8. And it uses more bytes only when needed. In the demo, A is one byte, é is two, and the Khmer letter ក is three. So here's the crucial consequence: one character is not always one byte.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So, a character encoding is a shared table mapping characters to bytes. ASCII covers basic English, 0 to 127, with H as `0x48`, and remember the character zero is 48, not zero. Unicode plus UTF-8 handles every language, stays ASCII-compatible, and means one character is not one byte, a Khmer letter is three bytes. Next, two more encodings you'll meet everywhere, and the single most important security point in this lesson: encoding is not encryption.

**Time:** about 0:30

---

## Video 2 — Base64, URL Encoding, and Why It Matters

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video, two encodings you'll see constantly in security, Base64 and URL encoding, and the mistake that trips up almost every beginner: thinking encoding means the data is protected. It doesn't.

**Time:** about 0:20

### 2.2 — Base64 is encoding, not encryption

**Show:** slide 2.2

**Say:** Base64 is a way to represent any binary data, not just text, using only 64 safe printable characters. It exists because some systems, old email, parts of the web, URLs, can only carry plain text, so binary data gets Base64-encoded into text to pass through, then decoded on the other side. In the demo, "Mina Coffee" encodes to that string ending in an equals sign, and decodes right back with no key. You'll learn to recognize Base64 on sight: a run of letters and digits, often ending in one or two equals signs. And here's the crucial point: Base64 gives no secrecy at all. Anyone can decode it instantly, with no key, as the second command shows. So seeing Base64 in a token or config file does not mean the data is protected.

**Time:** about 0:55

### 2.3 — Encoding vs encryption

**Show:** slide 2.3

**Say:** This is the most important distinction in the lesson, so let's state it plainly. Encoding, that's ASCII, UTF-8, Base64, URL encoding, is a public rule for representing data. There's no secret and no protection, and it's reversible by anyone. Encryption, which you'll study in the Cryptography course, uses a secret key to make data unreadable without that key. So whenever you see encoded data, just read it, and never assume it's protected. And never try to secure a secret by encoding it, because that protects nothing.

**Time:** about 0:45

### 2.4 — URL (percent) encoding

**Show:** slide 2.4

**Say:** One more everyday encoding, because you'll meet it constantly in web security. URLs can only use a limited set of characters, so anything outside that set, spaces and special symbols, gets replaced by a percent sign followed by the character's byte in hex. In the demo, a space became `%20`, because a space is byte `0x20`, which is 32, the ASCII space from earlier. The ampersand became `%26`, equals became `%3D`, question mark became `%3F`. Same idea as always: a public rule for packing characters into a restricted channel, using hex byte values you already know. And this matters in web security because attackers use it to sneak dangerous characters past filters: a filter looking for a literal less-than sign might miss `%3C`, which the browser later turns back into less-than. Same bytes, read at two stages with two rules.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: Base64 is encoding, not encryption, decodable by anyone instantly. Encoding is a public rule; encryption needs a secret key; encoding never protects. URL encoding is percent plus the hex byte, and it's used to bypass filters. And the big theme underneath: ambiguity is an attack surface, when two parts of a system read the same bytes differently, attackers slip input through the gap. You now understand how both numbers and text become bytes. Next lesson, we leave pure data behind and look at the machine that works on it: the CPU, memory, and storage.

**Time:** about 0:35
