# Section 11: A First Look at C and Memory — Video Scripts

Two videos, about 9 minutes in total. Slide IDs match [`slides.md`](slides.md). The demos compile and run small C programs; have a terminal with a C compiler ready. The `c-wrong` example is shown to illustrate the bug only, never run.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Variables, Addresses, and Pointers | 1.1–1.5 | about 4.5 min |
| 2 | Buffers, Overflows, and Memory Safety | 2.1–2.5 | about 4.5 min |

---

## Video 1 — Variables, Addresses, and Pointers

### 1.1 — Title

**Show:** slide 1.1

**Say:** This lesson gets hands-on with memory, using the smallest possible amount of C. The goal isn't to teach you C, that's a whole course, but to let you see memory directly, because this is the exact foundation that binary exploitation is built on.

**Time:** about 0:25

### 1.2 — Why a little C

**Show:** slide 1.2

**Say:** Why C? Because C works directly with memory. Most modern languages, Python, JavaScript, Java, deliberately hide memory from you: they manage it automatically and stop you touching raw addresses, for safety. C does the opposite, it lets you see and manipulate memory directly, addresses, bytes, the stack. That's why it matters here. The systems you'll attack and defend are often written in C or C++, operating system kernels, core programs, embedded and IoT software. The most serious class of vulnerabilities, memory-corruption bugs like buffer overflows, lives in C-like languages. And it makes memory concrete, the stack and addresses stop being abstract once you see them in a few lines. You won't become a C programmer today, and you don't need to. You just need to read a handful of tiny programs and watch what happens to memory.

**Time:** about 0:55

### 1.3 — A variable is a place in memory

**Show:** slide 1.3

**Say:** Here's a complete program. It makes a variable called price, holding 2500, and prints two things. The value, with %d, and something new, the address, with %p, where that value lives in memory. The key is the ampersand before price: it means "the address of price". Running it, the first line is 2500, the value. The second line is the address where that value lives, shown in hex. Yours will be different and will change each run. And that second line is the whole point: a variable isn't just a value, it's a value stored at a place, and that place has an address. A variable has three things, really: a name, price; a value, 2500; and an address. Normally the language hides the address, and you think only about name and value. C lets you ask for the address. And this matters because memory attacks care about the address and the bytes there, not the name.

**Time:** about 0:55

### 1.4 — Pointers, gently

**Show:** slide 1.4

**Say:** If a variable has an address, you can store that address in another variable, and a variable that holds an address is called a pointer. Let's take it gently. The line `int *p = &price` creates a pointer p and stores in it the address of price, so p doesn't hold 2500, it holds where 2500 lives. Then `*p`, star-p, means "the value at the address p holds", following the pointer to what it points at, so reading it gives 2500. And `*p = 3000` writes 3000 to the address p points at, which is price's location, so it changes price itself. In the output, we changed price to 3000 without ever naming price on that line, only by going through its address. That's the essence of a pointer: a way to read and write memory by address. Think of a slip of paper with a house address on it: the slip isn't the house, but anyone holding it can go there and change what's inside. Pointers make C powerful, and they're also where much goes wrong, a pointer holding the wrong address reads or writes memory it shouldn't.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: C works directly with memory, which is why security uses it. A variable is a name, a value, and an address, and the ampersand gets the address. A pointer holds an address, and star-p reads or writes the memory it points at. And memory attacks are about addresses and bytes, not names. Next, we put a sequence of bytes into memory, a buffer, and see what happens when a program writes more than fits.

**Time:** about 0:25

---

## Video 2 — Buffers, Overflows, and Memory Safety

### 2.1 — Title

**Show:** slide 2.1

**Say:** Now the payoff. In this video: a buffer on the stack, the single most famous memory bug, the buffer overflow, and why some programming languages are fundamentally safer than others.

**Time:** about 0:20

### 2.2 — A buffer, used safely

**Show:** slide 2.2

**Say:** Recall the stack, where functions keep their local variables. Now meet a buffer: a block of memory set aside to hold a sequence of bytes, like text. In this program, `char name[8]` sets aside a buffer of 8 bytes on the stack, room for 7 characters plus the end-marker byte C uses to mark where text ends. Then strncpy copies the text "Dara" into the buffer, but at most 7 bytes, deliberately not more than it can hold. It prints "hello, Dara". The key words there are "at most 7 bytes". The buffer is a fixed size, 8 bytes, but the data you copy in might be any length. A careful program always checks that what it writes fits. And the whole drama of the next slide is what happens when a program does not check.

**Time:** about 0:50

### 2.3 — What a buffer overflow is

**Show:** slide 2.3

**Say:** A buffer overflow happens when a program writes more data into a buffer than it can hold, so the extra data spills past the end and over whatever sits next to it in memory. Picture the unsafe version, shown only to illustrate the bug, never something you'd write: it copies user input into the 8-byte buffer with strcpy and no length check. If the input is "Dara", fine. But if it's 50 characters, strcpy happily writes all 50 bytes, running 42 bytes past the end of the buffer, overwriting whatever's next on the stack. And recall what sits near local variables on the stack: the return address, where the CPU goes when the function finishes. That's the attack. By supplying carefully crafted over-long input, an attacker overflows the buffer and overwrites the return address with one of their choosing, so when the function returns, the CPU jumps there and runs the attacker's instructions. Over-long data has become control of the program. You're not exploiting anything here, that's the Binary Exploitation course, in a lab, on your own targets. The point is the attack is no longer mysterious, it's a direct consequence of everything you've learned.

**Time:** about 1:00

### 2.4 — Memory safety

**Show:** slide 2.4

**Say:** So why do buffer overflows exist at all? Because C and C++ are not memory-safe: they let a program read and write memory out of bounds, or misuse a pointer, without stopping it. The program just does it, and the result is a bug or an exploit. This one property is behind a huge share of the most serious vulnerabilities in history. The response comes in two forms. Defenses that make exploitation harder on existing C and C++ code: NX, a non-executable stack; ASLR, the randomized addresses you saw; stack canaries; and more. And memory-safe languages that prevent the bugs entirely, like Rust, and managed languages like Python, Java, and Go, which don't let a program write past a buffer or misuse a pointer. That's why there's a strong modern push to write new security-sensitive software in memory-safe languages: it removes an entire class of vulnerabilities at the source.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: a buffer is fixed-size, and not checking input length is the overflow bug. A buffer overflow can overwrite the return address, turning over-long data into control of the program. C and C++ aren't memory-safe, while languages like Rust and Python prevent these bugs, and defenses like NX and ASLR make exploitation harder on existing code. You've now looked at memory up close and seen, in a few lines, where the most serious attacks come from. One lesson remains: putting everything from this whole course together on a real, running system, with your own hands.

**Time:** about 0:35
