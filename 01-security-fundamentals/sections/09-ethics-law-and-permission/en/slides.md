---
title: "Security Fundamentals — Section 9: Ethics, the Law, and Permission to Test"
videos:
  1: The One Rule, and Authorized Testing
  2: The Law, Your Data Duties, and Finding a Bug
---

<!-- 1.1 -->
<!-- layout: title -->

# Ethics, the Law, and Permission to Test

## Video 1 · The One Rule, and Authorized Testing

Security Fundamentals · Section 9

In this video, you will learn:

- Why ethics matters more than any technique
- The one rule, made precise
- Scope, rules of engagement, and bug bounties

*This lesson teaches the shape of the rules, not legal advice. Confirm your own country's current law.*

---

<!-- 1.2 -->

# Why ethics comes first

You can now describe how attacks work. That knowledge is what a **defender** needs and what a **criminal** uses.

**The only difference is permission and intent.**

- Ethics isn't a soft add-on; it's the line between professional and criminal.
- A security career is built on **trust**: deep access, powerful tools.
- One serious breach, testing without permission, peeking at data, ends that trust, and often a career.

---

<!-- 1.3 -->
<!-- layout: warning -->

# The one rule, restated

> **Only access or test a system when you own it, or have clear, specific, written permission from someone with the authority to grant it.**

- **Clear & specific:** which systems, what actions, when.
- **Written:** verbal permission protects no one.
- **From someone with authority:** a friend who works there can't authorize it.

Not permission: "I was curious" · "it was exposed" · "I only looked" · "I wanted to help." **No fifth exception.**

---

<!-- 1.4 -->

# Authorized testing: scope and RoE

When security work *is* authorized, it's written down before any testing:

- **Scope:** exactly what may be tested, and what is **out of scope** and must not be touched.
- **Rules of engagement:** *how*, the time window, allowed techniques ("no DoS", "no social engineering"), emergency contacts, handling of real data.
- **Signed authorization** from someone with authority, before starting.

A professional never starts without it. These protect everyone.

---

<!-- 1.5 -->

# Bug bounties and responsible disclosure

Two legal ways to work on real systems:

- **Bug bounty:** a published invitation, "test these systems, within these rules, for a reward." The scope **is** your written permission, stay strictly inside it.
- **Responsible disclosure:** found a real flaw with no bounty? Report it privately, give time to fix, don't exploit or publish.

**Boundary:** finding a bug is *not* permission to dig further.

---

<!-- 1.6 -->
<!-- layout: recap -->

# Recap: permission

- Permission and intent are the only line between professional and criminal.
- The one rule: own it, or clear, specific, written permission, no exceptions.
- Authorized work uses scope + rules of engagement; bug bounties and responsible disclosure are the legal paths.

**Next video:** the law, your data duties, and what to do if you find a bug.

---

<!-- 2.1 -->
<!-- layout: title -->

# Ethics, the Law, and Permission to Test

## Video 2 · The Law, Your Data Duties, and Finding a Bug

Security Fundamentals · Section 9

In this video, you will learn:

- The shape of computer-crime law
- Your duties around personal data
- What to do if you find a vulnerability

---

<!-- 2.2 -->

# The shape of computer-crime law

Almost every country outlaws unauthorized access. The shape is consistent:

- **Unauthorized access** is an offense, **often regardless of harm**, just logging in without permission can be a crime.
- **Unauthorized modification** is treated more seriously.
- **Damage or financial gain** raises the penalties.
- **Making/supplying attack tools** for crime can be an offense.

**Cambodia** has its own developing framework, **confirm the current law**. "I'm a student" is not a defense.

---

<!-- 2.3 -->

# Your duties around personal data

Personal data = information about identifiable people (names, phones, health, messages). Shared principles:

- **Collect only what you need**, use it only for its purpose.
- **Protect it**; **limit who can see it** (least privilege).
- **Keep it only as long as needed**, then delete.
- **Report breaches** to authorities and affected people.

Your practical duty: access only what the task needs, never copy, share, or snoop. Misuse can be a **crime and a firing offense.**

---

<!-- 2.4 -->

# If you find a vulnerability

1. **Stop.** Don't probe further or exploit it.
2. **Check for a path:** a bug bounty, a security contact, a `security.txt`.
3. **Report privately** with enough detail to reproduce.
4. **Give reasonable time** to fix; keep records of good-faith contact.
5. **Don't demand payment**, that looks like extortion.

Report it the way you'd want someone to report a flaw in *your* system.

---

<!-- 2.5 -->
<!-- layout: recap -->

# Recap: law, data, disclosure

- Unauthorized access is a crime in almost every country, often regardless of harm; confirm local law.
- Handle personal data with care: least access, no copying, no snooping.
- Found a bug? Stop, report privately, give time, never demand payment.
- **Defend, don't exploit; help, don't harm; act only with permission.**

**Next lesson:** the frameworks and standards that organize security.
