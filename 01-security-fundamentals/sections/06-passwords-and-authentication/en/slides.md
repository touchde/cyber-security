---
title: "Security Fundamentals — Section 6: Passwords and Authentication"
videos:
  1: Authentication and the Three Factors
  2: Passwords: Why They Fail, and How to Make Them Strong
  3: MFA and Passkeys
---

<!-- 1.1 -->
<!-- layout: title -->

# Passwords and Authentication

## Video 1 · Authentication and the Three Factors

Security Fundamentals · Section 6

In this video, you will learn:

- What authentication is
- The three factors of proof
- Why combining factors is strong

---

<!-- 1.2 -->

# What authentication is

**Authentication is proving that you are who you say you are.** The lock on the front door of almost every system.

- **Identification:** *claiming* an identity ("I am Dara"), a username, not a secret.
- **Authentication:** *proving* it ("here is my password / fingerprint / code").

The username is often public (an email). The whole strength of a login rests on how good the **proof** is.

---

<!-- 1.3 -->
<!-- layout: table -->

# The three factors

| Factor | Meaning | Examples |
|---|---|---|
| **Something you know** | A secret in your head | Password, PIN |
| **Something you have** | A thing you possess | Phone, security key |
| **Something you are** | A body trait | Fingerprint, face |

Each has a weakness: what you know can be phished; what you have can be stolen; what you are can't be changed if it leaks.

**Strength comes from combining _different_ factors.**

---

<!-- 1.4 -->
<!-- layout: recap -->

# Recap: authentication and factors

- Authentication proves who you are; the username is just the claim.
- Three factors: something you know, have, are.
- Two *different* factors are far stronger than two of the same kind.

**Next video:** passwords, why they fail, and how to make them strong.

---

<!-- 2.1 -->
<!-- layout: title -->

# Passwords and Authentication

## Video 2 · Passwords: Why They Fail, and How to Make Them Strong

Security Fundamentals · Section 6

In this video, you will learn:

- Why passwords fail so often
- How passwords are stored and cracked
- Strong passwords, passphrases, and password managers

---

<!-- 2.2 -->

# Why passwords fail

- People choose **weak** ones ("123456", "password").
- People **reuse** them, so one breach unlocks many accounts.
- People can be **tricked** into giving them away.
- They can be **guessed in bulk**, billions of tries against a stolen file.
- We simply have **too many** to manage by memory.

A password *alone* is weak. It must be made strong, and backed by a second factor.

---

<!-- 2.3 -->

# How passwords are stored and cracked

A system must store *something* to check against, and stores get stolen.

- **Plain text (worst):** a leak exposes every password instantly.
- **Hashing (right):** store a one-way "fingerprint"; you can't reverse it.

Attackers crack stolen hashes **offline**, billions of guesses a second. Two defenses:

- **Salting:** a unique random value per password, so identical passwords differ.
- **Slow hashing** (bcrypt, Argon2): each guess costs real time.

**Length helps:** every extra character multiplies the guessing work.

---

<!-- 2.4 -->

# Strong passwords and password managers

Length and unpredictability beat strange symbols.

- **Length wins:** aim for 12–16+ characters.
- **Passphrases:** 4–5 random words, `correct-harbor-tiger-bottle`, long, memorable, hard to guess.
- **`P@ssw0rd!` is weak:** the substitutions are the first thing tools try.
- **Unique per site**, always.

A **password manager** makes unique strong passwords effortless, fills them **only on the correct site** (anti-phishing), and stores them **encrypted**. One of the best habits you can adopt.

---

<!-- 2.5 -->
<!-- layout: recap -->

# Recap: passwords

- Passwords fail because they're weak, reused, phishable, guessable, and too many.
- Good storage is salted, slow hashing, never plain text; length multiplies the work.
- Long unique passphrases + a password manager solve most of it.

**Next video:** the two steps that matter most, MFA and passkeys.

---

<!-- 3.1 -->
<!-- layout: title -->

# Passwords and Authentication

## Video 3 · MFA and Passkeys

Security Fundamentals · Section 6

In this video, you will learn:

- What multi-factor authentication is, and why it works
- Which second factors are strongest
- What passkeys are, and why they're the future

---

<!-- 3.2 -->

# Multi-factor authentication

**MFA requires two _different_ factors:** usually your password (know) + a code or tap on your phone (have).

**The single most effective step** for most people and businesses: a stolen password is now useless on its own.

- Credential stuffing, most phishing, and bulk cracking all **fail** against MFA.

Not all equal: **SMS** is weakest (can be redirected); **authenticator apps** stronger; **security keys / passkeys** strongest (also verify the site).

**Turn it on everywhere, email first.** Never approve a prompt you didn't start.

---

<!-- 3.3 -->

# Passkeys: the direction of travel

A **passkey** lives on your device and proves who you are **without sending a password**. You unlock it with your fingerprint, face, or PIN.

- **Nothing to phish:** no password to type; it checks it's the real site.
- **Nothing to reuse or leak:** unique per site; no stored secret to crack.
- **Easy:** signing in is just unlocking your device.

Built on public-key cryptography, supported by the major platforms, and growing.

---

<!-- 3.4 -->
<!-- layout: recap -->

# Recap: MFA and passkeys

- **MFA** adds a second, different factor and defeats stolen passwords; turn it on everywhere, email first.
- SMS is the weakest factor; apps and keys are stronger.
- **Passkeys** remove the password: unphishable, unique per site, the future.
- **Practical plan:** password manager + MFA everywhere + passkeys where offered.

**Next lesson:** once a system knows who you are, how it decides what you may do, access control.
