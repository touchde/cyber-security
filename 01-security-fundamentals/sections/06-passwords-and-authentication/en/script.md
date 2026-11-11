# Section 6: Passwords and Authentication — Video Scripts

Three videos, about 11 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Authentication and the Three Factors | 1.1–1.4 | about 3 min |
| 2 | Passwords: Why They Fail, and How to Make Them Strong | 2.1–2.5 | about 4.5 min |
| 3 | MFA and Passkeys | 3.1–3.4 | about 3.5 min |

---

## Video 1 — Authentication and the Three Factors

### 1.1 — Title

**Show:** slide 1.1

**Say:** This lesson is the practical heart of the course. The habits in it protect you more than almost anything else you'll learn. We start with what authentication actually is, and the three kinds of proof it can use.

**Time:** about 0:25

### 1.2 — What authentication is

**Show:** slide 1.2

**Say:** Authentication is proving that you are who you say you are. It's the lock on the front door of almost every system: before it lets you read or change anything, it checks your identity. Keep two words apart. Identification is claiming an identity, "I am Dara", usually a username. Authentication is proving it, "and here is my password, or fingerprint, or code". A username isn't a secret; it's often just your email address. The secret is the proof. So the whole strength of a login rests on how good that proof is, which is what this lesson is about.

**Time:** about 0:45

### 1.3 — The three factors

**Show:** slide 1.3

**Say:** There are three fundamentally different kinds of proof, called factors. Something you know: a secret in your head, like a password or PIN. Something you have: a physical thing you possess, like a phone or a security key. And something you are: a trait of your body, like a fingerprint or face. Each has a weakness. Something you know can be guessed, phished, or reused. Something you have can be lost or stolen. Something you are can't be changed if it leaks. The power comes from combining different factors: if a login needs two different kinds, an attacker has to beat both, and beating a password is very different from stealing your phone. Using two of the same kind, two passwords, isn't nearly as strong, because one attack, phishing, can take both.

**Time:** about 0:55

### 1.4 — Recap

**Show:** slide 1.4

**Say:** So: authentication proves who you are, and the username is just the claim. There are three factors, something you know, have, and are. And two different factors are far stronger than two of the same kind. Next, the factor we all use most and struggle with most: passwords.

**Time:** about 0:25

---

## Video 2 — Passwords: Why They Fail, and How to Make Them Strong

### 2.1 — Title

**Show:** slide 2.1

**Say:** Passwords are the oldest and most common factor, and the most troublesome. In this video: why they fail, how they're actually stored and cracked, and how to make them strong without losing your mind.

**Time:** about 0:25

### 2.2 — Why passwords fail

**Show:** slide 2.2

**Say:** Passwords fail for human and technical reasons. People choose weak ones; "123456" and "password" top every leaked-password list, year after year. People reuse them, so one breach unlocks every account that shares the password. People can be tricked into typing them into a fake login page. They can be guessed in bulk, billions of tries against a stolen file. And we simply have too many, hundreds of accounts, far more than anyone can remember with unique strong passwords, so we cut corners. None of this means passwords are useless. It means a password alone is weak, and must be made strong and backed by a second factor.

**Time:** about 0:50

### 2.3 — How passwords are stored and cracked

**Show:** slide 2.3

**Say:** To check your password, a system has to store something to compare against, and those stores get stolen all the time. The worst way is plain text, saving the password as-is; if the file leaks, every password is instantly exposed. The right way is hashing: the system stores a scrambled one-way fingerprint that can't be turned back into the password. But hashing isn't enough by itself, because attackers crack a stolen file of hashes offline, guessing passwords and hashing each guess at billions a second. Two techniques make that much harder. Salting adds a unique random value to each password, so identical passwords get different hashes and can't all be cracked at once. And slow hashing uses a function built to be deliberately slow, so each guess costs real time. You don't need the math yet, but here's the takeaway: a strong password matters because storage can be stolen, and good storage buys you time even when it is. And notice, length helps enormously, because every extra character multiplies the number of guesses.

**Time:** about 1:05

### 2.4 — Strong passwords and password managers

**Show:** slide 2.4

**Say:** So what makes a password strong? Not mostly strange symbols, but length and unpredictability. Length wins: every extra character multiplies the work, so aim for at least twelve to sixteen. Passphrases are both strong and memorable, four or five random unrelated words like correct-harbor-tiger-bottle, as long as they're truly random and not a famous phrase. And beware: "P-at-ss-zero-rd-bang" looks complex but is one of the first things cracking tools try, because the substitutions are obvious. Randomness beats cleverness, and every password should be unique per site. Now, remembering a unique long password for every account is impossible by hand, and that's exactly what a password manager solves. It generates, stores, and fills a different strong password for every account; you remember one master password. It fills passwords only on the correct site, which quietly defends against phishing, and it stores everything encrypted. It's one of the best security habits you can adopt.

**Time:** about 1:05

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: passwords fail because they're weak, reused, phishable, guessable, and too many. Good storage is salted, slow hashing, never plain text, and length multiplies the attacker's work. And long unique passphrases, managed by a password manager, solve most of the problem. Next, the two steps that matter most on top of a good password: MFA and passkeys.

**Time:** about 0:30

---

## Video 3 — MFA and Passkeys

### 3.1 — Title

**Show:** slide 3.1

**Say:** Even a strong password can be stolen or phished. In this video, the two steps that close that gap: multi-factor authentication, and the passwordless future, passkeys.

**Time:** about 0:20

### 3.2 — Multi-factor authentication

**Show:** slide 3.2

**Say:** Multi-factor authentication, also called two-factor or two-step, requires two different factors to log in: usually your password, something you know, plus a code or a tap on your phone, something you have. It's the single most effective step most people and businesses can take, because it breaks the most common attacks. A stolen or guessed password is now useless on its own; the attacker also needs your second factor. Credential stuffing, most phishing, and bulk cracking all fail against it. But not all second factors are equal. SMS codes texted to your phone are far better than nothing, but can be intercepted or redirected, so they're the weakest. Authenticator apps that show a changing six-digit code are stronger. And security keys and passkeys are strongest, because they also verify the site and can't be phished. Turn MFA on everywhere it's offered, starting with email, which can reset all your other passwords. And one caution: some phishing now tries to trick you into approving an MFA prompt, so never approve one you didn't start.

**Time:** about 1:05

### 3.3 — Passkeys

**Show:** slide 3.3

**Say:** The newest and most promising answer removes the password altogether. A passkey is a secret that lives on your device and proves your identity without ever sending a password to the site. You unlock it the way you unlock your phone, with your fingerprint, face, or PIN. Why are they better? There's nothing to phish, because there's no password to type, and the passkey checks it's talking to the real site. There's nothing to reuse or leak in a breach, because each one is unique and the site never stores a crackable secret. And they're easy, signing in is just unlocking your device. They're built on well-tested public-key cryptography, supported by the major platforms, and more websites add them every month. They're the direction the whole industry is moving.

**Time:** about 0:50

### 3.4 — Recap

**Show:** slide 3.4

**Say:** So, to bring the lesson together: multi-factor authentication adds a second, different factor and defeats stolen passwords, so turn it on everywhere, email first. SMS is the weakest factor; apps and keys are stronger. And passkeys remove the password entirely: unphishable, unique per site, the future. Your practical plan is three things: a password manager for unique strong passwords, MFA everywhere, and passkeys wherever a site offers them. In the next lesson, we move one step past the front door: once a system knows who you are, how does it decide what you're allowed to do? That's access control.

**Time:** about 0:35
