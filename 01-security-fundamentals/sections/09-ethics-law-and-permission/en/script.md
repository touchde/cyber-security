# Section 9: Ethics, the Law, and Permission to Test — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos. This lesson teaches the shape of the rules, not legal advice; the opening slide says so.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | The One Rule, and Authorized Testing | 1.1–1.6 | about 4.5 min |
| 2 | The Law, Your Data Duties, and Finding a Bug | 2.1–2.5 | about 3.5 min |

---

## Video 1 — The One Rule, and Authorized Testing

### 1.1 — Title

**Show:** slide 1.1

**Say:** This is the most important lesson in the course. By now you understand attacks and defenses well enough that one question becomes urgent: what am I actually allowed to do with this knowledge? One note first, this lesson teaches the shape of the rules, not legal advice; laws differ and change, so confirm your own country's current law.

**Time:** about 0:30

### 1.2 — Why ethics comes first

**Show:** slide 1.2

**Say:** You can now describe how phishing works, how passwords are cracked, how attacks move through a network. That knowledge is exactly what a defender needs, and exactly what a criminal uses. The only thing separating the two is permission and intent. So ethics isn't a soft add-on to security; it's the line that decides whether you're a professional or a criminal, with identical skills on both sides. And this is practical, not just moral. A security career is built on trust: employers and clients hand you deep access and powerful tools. One serious ethical breach, testing without permission, peeking at data you weren't authorized to see, ends that trust, and often a career, no matter how skilled you are.

**Time:** about 0:50

### 1.3 — The one rule, restated

**Show:** slide 1.3

**Say:** Here's the rule from lesson 1, now precise: only ever access or test a system when you own it, or you have clear, specific, written permission from someone with the authority to grant it. Every word matters. Clear and specific: it must say which systems, what you may do, and when, not just "test our stuff". Written: verbal permission protects no one; if it's not in writing, it didn't happen. And from someone with authority: a friend who works at a company can't authorize you to test the company's systems, only the owner or their delegate can. And the hard edges, again: curiosity is not permission, "it was exposed" is not permission, "I only looked" is not permission because looking is access, and "I wanted to help" is not permission unless you were invited. There is no fifth exception.

**Time:** about 1:00

### 1.4 — Authorized testing: scope and RoE

**Show:** slide 1.4

**Say:** When security work is authorized, a professional penetration test, say, the permission is written down in detail before any testing begins. Two documents matter. Scope defines exactly what may be tested, which systems are in scope, and, just as importantly, what's out of scope and must not be touched, because testing something out of scope, even by accident, can be illegal. Rules of engagement define how the test runs: the time window, which techniques are allowed, for example no denial-of-service or no social engineering of staff, who to contact in an emergency, and how to handle any real data found. Underneath both is a signed authorization from someone with authority. A professional never starts without it, and these documents protect everyone.

**Time:** about 0:55

### 1.5 — Bug bounties and responsible disclosure

**Show:** slide 1.5

**Say:** What if you're not hired, but you genuinely want to help? There are legitimate paths. Bug bounty programs are standing invitations: a company publishes a policy saying "you may test these systems, within these rules, and we'll reward valid findings". That published scope is your written permission, as long as you stay strictly inside it, and it's a popular, legal way to practise on real systems and earn money. Responsible disclosure is the path when there's no bounty and you've found a real flaw, usually in something you were legitimately using: you report it privately, give them time to fix it, and don't publish or exploit it meanwhile. But here's the crucial boundary: finding a flaw by chance is not permission to go digging further. The moment you probe beyond what you were invited to do, you've crossed into unauthorized access.

**Time:** about 0:55

### 1.6 — Recap

**Show:** slide 1.6

**Say:** So: permission and intent are the only line between professional and criminal. The one rule is own it, or clear, specific, written permission, with no exceptions. And authorized work uses scope and rules of engagement, while bug bounties and responsible disclosure are the legal ways to touch real systems. Next, the law itself, your duties around personal data, and what to do if you find a bug.

**Time:** about 0:30

---

## Video 2 — The Law, Your Data Duties, and Finding a Bug

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video: the shape of computer-crime law, the duties you carry when handling personal data, and a clear procedure for when you find a vulnerability.

**Time:** about 0:20

### 2.2 — The shape of computer-crime law

**Show:** slide 2.2

**Say:** Almost every country has laws against unauthorized access to computer systems, and while details vary, the shape is consistent. Unauthorized access, getting into a system you're not permitted to, is an offense, often regardless of whether you caused any harm, so simply logging in without permission can be a crime. Unauthorized modification, changing data, is treated more seriously. Causing damage or acting for financial gain raises the penalties further. And even making or supplying attack tools for criminal use can be an offense. Well-known examples are the US Computer Fraud and Abuse Act and the UK Computer Misuse Act, and most countries have equivalents. Cambodia has its own developing legal framework for computer offenses, so confirm the current law before relying on any detail. And remember, ignorance of the law is not a defense, and "I'm a student" or "I was learning" does not make unauthorized access legal.

**Time:** about 0:55

### 2.3 — Your duties around personal data

**Show:** slide 2.3

**Say:** Security people handle personal data constantly, logs, user records, the contents of a breach, and that carries legal and ethical duties. Personal data means information about identifiable people: names, phone numbers, health, finances, messages. The widely shared principles, seen in the EU's GDPR and many national laws including developing ones in Cambodia, are: collect only what you need and use it only for its stated purpose; protect it; limit who can see it, which is least privilege again; keep it only as long as needed, then delete it; respect people's rights over their data; and report breaches to authorities and affected people, often within a legal deadline. For you, the practical duty is simple: when your work exposes you to real personal data, access only what you need, never copy or share it, and never use it for curiosity or gain. Mishandling it can be both a crime and a firing offense.

**Time:** about 0:55

### 2.4 — If you find a vulnerability

**Show:** slide 2.4

**Say:** Finally, a situation you will meet: you find a vulnerability. What do you do? First, stop, don't probe further and don't exploit it; just note what you already saw in normal use. Second, check for a path: does the owner have a bug bounty or a security contact, often a security-dot-txt file or a "report a vulnerability" page? Third, report privately to the owner, with enough detail to reproduce it; don't post it publicly. Fourth, give them reasonable time to fix it before any disclosure, and keep records of your good-faith contact. And fifth, do not demand payment, because asking for money to stay quiet looks like extortion, which is a crime, even if you meant well. Report it the way you'd want someone to report a flaw in your system.

**Time:** about 0:50

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: unauthorized access is a crime in almost every country, often regardless of harm, so confirm your local law and never access what isn't yours without written permission. Handle personal data with care, least access, no copying, no snooping. And if you find a bug, stop, report privately, give time, and never demand payment. The instinct underneath all of it is the ethical core of this whole program: defend, don't exploit; help, don't harm; act only with permission. With that firmly in place, the next lesson looks at the frameworks and standards that organize security work at scale.

**Time:** about 0:35
