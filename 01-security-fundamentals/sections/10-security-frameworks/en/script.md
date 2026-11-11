# Section 10: Security Frameworks and Standards — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Frameworks, NIST CSF, and CIS | 1.1–1.5 | about 4 min |
| 2 | ISO 27001, MITRE ATT&CK, and Compliance | 2.1–2.5 | about 4 min |

---

## Video 1 — Frameworks, NIST CSF, and CIS

### 1.1 — Title

**Show:** slide 1.1

**Say:** You now know the core ideas of security, goals, risk, controls, ethics. This lesson shows the organized, published ways professionals apply them, so you don't have to invent security from scratch. We'll meet the main frameworks, starting with why they exist, then the NIST Cybersecurity Framework and the CIS Controls.

**Time:** about 0:25

### 1.2 — Why frameworks exist

**Show:** slide 1.2

**Say:** A security program has dozens of moving parts: assets, risks, controls, people, processes. If every organization invented it alone, each would miss something, and you could never compare one organization's security to another's. Frameworks solve this. A framework is published, structured guidance, built by experts and refined over years, that tells you what to do and often how to organize it. It gives you four things: completeness, a checklist so you don't forget whole areas; a common language, so your team, auditors, and partners mean the same things; credibility, since following a recognized framework shows you're serious; and a starting point, so you adapt proven guidance instead of starting blank. There are many frameworks, they overlap, and you don't use all of them, because they serve different purposes.

**Time:** about 0:55

### 1.3 — NIST CSF 2.0: six functions

**Show:** slide 1.3

**Say:** The NIST Cybersecurity Framework is one of the most widely used. It's free, from the US National Institute of Standards and Technology, and used worldwide. Its strength is a simple structure of six functions that describe everything a program does. Govern: who's responsible, and what are our risks and policies? Identify: what do we have, and what matters? Protect: how do we safeguard it? Detect: how do we notice when something happens? Respond: what do we do during an incident? And Recover: how do we return to normal? Notice these map onto what you already know, Identify is assets and risk, Protect is controls, and Detect, Respond, Recover are the defensive courses ahead. Govern was added in version 2.0 to stress that security is a leadership responsibility, not just a technical one. For any organization, you can ask "how are they doing on each of the six?" and quickly find the gaps.

**Time:** about 1:00

### 1.4 — CIS Critical Security Controls

**Show:** slide 1.4

**Say:** Where NIST describes what areas to cover, the CIS Critical Security Controls give a concrete, prioritized list of specific things to do, ordered so the most effective come first. For someone asking "but what do I actually do on Monday?", CIS is the most practical answer. The early, highest-impact controls include: know your hardware and software, because you can't protect what you don't know you have; control accounts and access and use MFA; manage vulnerabilities by patching; keep and monitor logs; run awareness training; and have backup and recovery. CIS also defines Implementation Groups, tiers for small, medium, and large organizations. A small shop implements Group 1 and already blocks the large majority of common attacks, which echoes a theme of this whole course: ordinary, well-applied controls stop most attacks.

**Time:** about 0:55

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: frameworks give you completeness, a common language, credibility, and a starting point. The NIST CSF structures a whole program in six functions. And the CIS Controls tell you what to do first, with Implementation Group 1 sized for a small business. Next, the international standard, the attacker knowledge base, and a distinction that trips up even big companies.

**Time:** about 0:25

---

## Video 2 — ISO 27001, MITRE ATT&CK, and Compliance

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video: ISO 27001, the standard you can be certified against; MITRE ATT&CK, the shared map of attacker behavior; and the crucial difference between compliance and real security.

**Time:** about 0:20

### 2.2 — ISO/IEC 27001

**Show:** slide 2.2

**Say:** ISO/IEC 27001 is the leading international standard for information security management. Where NIST CSF is a flexible framework, ISO 27001 is a formal standard you can be certified against: an independent auditor checks your security management, and if it meets the requirements, issues a worldwide-recognized certificate. Its central idea is an Information Security Management System, an ISMS, which is not a product but an ongoing, documented process for managing security based on risk, applying controls, checking they work, and improving continuously. Its companion, ISO 27002, is a detailed catalogue of controls. Why does it matter? Many larger companies and many contracts require their suppliers to be ISO 27001 certified, so for a business selling to them, it's often a condition of doing business. It's more formal and more effort than CIS, usually a goal for a maturing organization rather than a first step.

**Time:** about 0:55

### 2.3 — MITRE ATT&CK

**Show:** slide 2.3

**Say:** MITRE ATT&CK is different from the others. It's not a program framework or a control list, but a detailed, public knowledge base of how attackers actually behave, organized by the stages of an attack, the attack lifecycle from lesson 5. For each stage it catalogues the specific techniques real attackers use, with descriptions, real examples, and, crucially, how to detect and defend against each. It's maintained from observing actual attacks, so it reflects the real world. Why is it so valuable, especially to defenders? It gives everyone a common language for attacker behavior, so teams and tools can communicate precisely. Defenders use it to measure coverage: which attacker techniques can we detect, and where are our blind spots? And it connects attack to defense. You'll use ATT&CK heavily in the defensive and red-team courses.

**Time:** about 0:55

### 2.4 — Compliance vs. security

**Show:** slide 2.4

**Say:** Now one of the most important distinctions in the whole field. Compliance means meeting the formal requirements of a framework, standard, or law, often to pass an audit. Security means actually being hard to attack. They overlap, but they are not the same thing, and confusing them is dangerous. You can be compliant but insecure: you ticked every box for the audit, but the controls are weak in practice or ignored day to day. "We passed the audit" is not "we are safe", and many breached companies were certified at the time. You can also be secure but not yet compliant: a small team with excellent habits that hasn't done the paperwork. The right way to see it: compliance is a floor, not a ceiling. Use frameworks to be thorough and to prove diligence, but never mistake a certificate for safety.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: ISO 27001 is a certifiable standard built on an ISMS, often needed to sell to big customers. MITRE ATT&CK is the shared map of attacker techniques, used for detection and defense. And compliance is a floor, not a ceiling, so build real security on top of it. These frameworks are complementary, not competing: a sensible combination is NIST to organize the program, CIS to decide what to do first, ATT&CK to guide detection, and ISO later if you need the certificate. The goal for now is simply that when you hear these names, you know what each means and why it's there. Next lesson, we look at the people who do this work: the roles and careers in security.

**Time:** about 0:35
