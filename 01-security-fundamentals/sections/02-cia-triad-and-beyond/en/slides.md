---
title: "Security Fundamentals — Section 2: The CIA Triad and Beyond"
videos:
  1: The Three Core Goals
  2: Controlling Who Does What
  3: Balancing the Goals
---

<!-- 1.1 -->
<!-- layout: title -->

# The CIA Triad and Beyond

## Video 1 · The Three Core Goals

Security Fundamentals · Section 2

In this video, you will learn:

- Why security needs clear, named goals
- Confidentiality, integrity, and availability
- A quick test for each one

---

<!-- 1.2 -->

# Why we need clear goals

"Make it secure" is not a plan. Secure against what? Readable by whom? Working how often?

- Without named goals, two people both say "secure" and mean different things, and neither can check it.
- Security people use a small set of named goals, so you can **design for**, **test**, and **detect the failure of** each one.
- The oldest and most useful set is three: the **CIA triad**.

(The name is just the first letters. It has nothing to do with any agency.)

---

<!-- 1.3 -->

# Confidentiality

**Only the right people can _read_ the information.**

- Broken by a **data breach**: a stolen laptop, an open database, an email to the wrong person, traffic read on open Wi-Fi.
- Main tools: **encryption**, **access control**, **authentication**.

**Quick test:** if this fell into a stranger's hands, would it matter? If yes, it needs protecting.

---

<!-- 1.4 -->

# Integrity

**The information is correct, and _changed_ only by the right people, in the right way.**

- Covers **malicious** change (an attacker alters a payment) and **accidental** change (a bug, a faulty disk).
- Main tools: **hashing** (a fingerprint that changes if the data changes), **digital signatures**, **validation**.

**Quick test:** if someone changed this without permission, who would be harmed, and would we even notice?

---

<!-- 1.5 -->

# Availability

**The system _works_ when the people who need it need it.**

- Secret and correct data is useless if you cannot reach it (a hospital record in an emergency).
- Broken by ransomware, a flood of fake traffic, a power cut, a failed disk. Often harmed by accident, not only attackers.
- Main tools: **backups**, **redundancy**, **capacity and filtering**.

**Quick test:** if this were unreachable for an hour, a day, a week, what would it cost?

---

<!-- 1.6 -->
<!-- layout: recap -->

# Recap: the three core goals

- Named goals let us design, test, and detect failures.
- **Confidentiality:** who can read it. **Integrity:** who can change it. **Availability:** does it work when needed.
- Integrity covers accidents as well as attacks; availability is security too.

**Next video:** the goals that control who does what.

---

<!-- 2.1 -->
<!-- layout: title -->

# The CIA Triad and Beyond

## Video 2 · Controlling Who Does What

Security Fundamentals · Section 2

In this video, you will learn:

- Authentication, authorization, and accounting (AAA)
- What non-repudiation means
- How these support the CIA triad

---

<!-- 2.2 -->
<!-- layout: table -->

# AAA: who are you, what may you do, what did you do

The CIA triad says *what* we protect. **AAA** says *how we control who does what*.

| Goal | Answers | Example |
|---|---|---|
| **Authentication** | "Who are you?" | Password, code, fingerprint, passkey |
| **Authorization** | "What may you do?" | A teller and a manager differ |
| **Accounting** | "What did you do?" | The logs of who did what, when |

Order: you **authenticate**, the system **authorizes**, then it **accounts** for what you did.

---

<!-- 2.3 -->

# Non-repudiation

**Someone cannot credibly deny that they did something.**

- Sign a contract, and you cannot later claim you never did.
- Provided mainly by **digital signatures** plus solid **logs**.
- Matters most for **money, contracts, and legal records**.

It builds on **integrity** (the record was not changed) and **authentication** (we know who acted).

---

<!-- 2.4 -->
<!-- layout: recap -->

# Recap: controlling who does what

- **Authentication:** prove who you are. **Authorization:** what you may do. **Accounting:** the record of what you did.
- **Non-repudiation:** you cannot deny you did it.
- These support the CIA triad; weak authentication breaks both confidentiality and integrity.

**Next video:** why the goals pull against each other, and how to balance them.

---

<!-- 3.1 -->
<!-- layout: title -->

# The CIA Triad and Beyond

## Video 3 · Balancing the Goals

Security Fundamentals · Section 2

In this video, you will learn:

- Why improving one goal can cost another
- How to choose a balance on purpose
- Using the goals as a checklist for any system

---

<!-- 3.2 -->
<!-- layout: table -->

# The goals pull against each other

A good design is a **balance chosen on purpose**, not every goal maxed out.

| Push this up… | …and this can suffer |
|---|---|
| Confidentiality (more locks, more passwords) | Availability and ease of use |
| Availability (easy to reach) | Confidentiality (more ways in) |
| Integrity (approve every change) | Speed and availability |
| Security in general | Usability and cost |

A bank that needed five passwords per transaction would be very "secure" and completely unusable.

---

<!-- 3.3 -->
<!-- layout: table -->

# The goals as a checklist

For any system, ask seven questions. Take an online shop:

| Goal | Ask |
|---|---|
| Confidentiality | Who can read addresses and card details? |
| Integrity | Can anyone change a price or total? |
| Availability | What happens on the busiest day, or under attack? |
| Authentication | How do people prove who they are? |
| Authorization | Can a customer reach another's order? |
| Accounting | If money vanished, could we trace it? |
| Non-repudiation | Can a customer deny a purchase? |

---

<!-- 3.4 -->
<!-- layout: recap -->

# Recap: balancing the goals

- The goals trade against each other and against usability; choose a balance based on **risk**.
- Spend protection where the asset is valuable and the threat is real.
- The seven goals are a checklist for thinking about any system.

**Next lesson:** Threats, vulnerabilities, and risk, how we measure and manage the dangers these goals face.
