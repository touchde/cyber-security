---
title: "Security Fundamentals — Section 5: Common Attacks: Phishing, Malware, and More"
videos:
  1: How Attacks Start, and Attacking People
  2: Malware and Password Attacks
  3: Services, Networks, and the Attack Lifecycle
---

<!-- 1.1 -->
<!-- layout: title -->

# Common Attacks

## Video 1 · How Attacks Start, and Attacking People

Security Fundamentals · Section 5

In this video, you will learn:

- The three ways most attacks begin
- Phishing and social engineering
- How to recognize and resist a phish

**These attacks are explained to defend against. Only ever test systems you own or have written permission to test.**

---

<!-- 1.2 -->

# How most attacks start

Not a dramatic break-in. Small and quiet, almost always one of three doors:

1. **A person is tricked** into clicking, opening, or telling.
2. **A weakness is exploited** in exposed, unpatched software.
3. **A stolen or guessed password** is used to simply log in.

The attacker needs one click, one unpatched server, or one reused password. **Good news for defenders:** a few basic defenses on these three doors stop most attacks.

---

<!-- 1.3 -->

# Phishing and social engineering

**Social engineering** attacks the person, not the computer. **Phishing** is the most common form: a fake message pretending to be someone you trust.

- **Spear phishing:** targeted and personalized. **Whaling:** aimed at a CEO.
- **Smishing / vishing:** by text / by call.
- **Business email compromise:** posing as a boss or supplier to redirect a payment, no malware at all.

**Signs:** urgency, a password or payment request, a slightly wrong sender, a link that lies about where it goes.

---

<!-- 1.4 -->

# Defending against phishing

- **Train** staff and keep a healthy suspicion.
- **Verify** the real sender address, and any urgent request, through another channel.
- **Never act on urgency** without checking.
- **Email filtering** to catch the obvious ones.
- **Multi-factor authentication**, so a stolen password alone is not enough.

Modern phishing can be flawless, so don't rely on spotting typos. Verify.

---

<!-- 1.5 -->
<!-- layout: recap -->

# Recap: how attacks start

- Most attacks begin with a tricked person, an unpatched system, or a stolen password.
- Phishing attacks the person; it comes by email, text, and call.
- Verify the sender and the request; use MFA. Don't trust urgency.

**Next video:** malware and password attacks.

---

<!-- 2.1 -->
<!-- layout: title -->

# Common Attacks

## Video 2 · Malware and Password Attacks

Security Fundamentals · Section 5

In this video, you will learn:

- The main kinds of malware
- How passwords are attacked
- The defenses for each

---

<!-- 2.2 -->
<!-- layout: table -->

# Malware: the main kinds

**Malware** is any software written to do harm. Behavior matters more than the label.

| Type | How it behaves |
|---|---|
| Virus | Attaches to a file; spreads when a person runs/shares it |
| Worm | Spreads by itself across a network, no human action |
| Trojan | Pretends to be useful so you install it yourself |
| Ransomware | Locks/encrypts files and demands payment |
| Spyware | Secretly watches keystrokes, screens, passwords |
| Botnet | Turns your machine into one the attacker controls |

One real sample often combines several.

---

<!-- 2.3 -->

# Defending against malware

- **Update software:** worms spread through known, unpatched holes.
- **Don't run untrusted programs or attachments.**
- **Anti-malware tools.**
- **Least privilege:** so malware can't reach everything.
- **Offline backups:** so ransomware can't destroy your only copy.

Behavior, not the label, decides the defense.

---

<!-- 2.4 -->

# Password attacks

- **Brute force:** try millions of passwords.
- **Dictionary:** try common words and passwords first.
- **Credential stuffing:** reuse pairs leaked from one site on others, very effective, because people reuse passwords.
- **Spraying:** one common password against many accounts.

Attackers usually steal a **stored** password file and crack it **offline**, so how passwords are stored matters: slow **password hashing**, never plain text.

**Defenses:** unique passwords (a manager helps), **MFA**, strong hashing on the server.

---

<!-- 2.5 -->
<!-- layout: recap -->

# Recap: malware and passwords

- Malware spreads differently (virus, worm, trojan); defend by behavior: updates, least privilege, offline backups.
- Passwords are mostly cracked offline; credential stuffing feeds on reuse.
- Unique passwords plus MFA defeat most password attacks.

**Next video:** attacks on services and networks, and the attack lifecycle.

---

<!-- 3.1 -->
<!-- layout: title -->

# Common Attacks

## Video 3 · Services, Networks, and the Attack Lifecycle

Security Fundamentals · Section 5

In this video, you will learn:

- Web and network service attacks
- Denial of service and man-in-the-middle
- The attack lifecycle, and why defenders have the edge

---

<!-- 3.2 -->

# Web and network service attacks

Any internet-facing service is a door. Common web attacks:

- **SQL injection:** input the server mistakes for a command, exposing the database.
- **Cross-site scripting (XSS):** malicious code that runs in other users' browsers.
- **Broken access control:** reaching data you shouldn't, e.g. another user's account.

**Common thread:** trusting input that shouldn't be trusted. **Defense:** treat all input as untrusted; the **server** enforces the rules. (See the OWASP Top 10.)

---

<!-- 3.3 -->

# Denial of service, and man-in-the-middle

**Denial of service (DoS):** attacks **availability** by flooding a system so real users can't use it. **DDoS** sends the flood from many machines (a botnet), bigger and harder to block.
*Defense: capacity, filtering, anti-DDoS services.*

**Man-in-the-middle (MITM):** the attacker secretly sits between you and the other side (classic on open Wi-Fi), reading or changing traffic.
*Defense: encryption, HTTPS, a VPN; heed certificate warnings.*

---

<!-- 3.4 -->
<!-- layout: table -->

# The attack lifecycle

Serious attacks move through stages (Cyber Kill Chain, MITRE ATT&CK):

| Stage | What happens |
|---|---|
| Reconnaissance | Research the target |
| Initial access | Phish, exploit, or stolen password |
| Foothold | Keep access |
| Escalate privileges | Normal user → admin |
| Move laterally | Spread to valuable machines |
| Act on objective | Steal, encrypt, defraud |

**The attacker must win every stage. The defender only has to break the chain once.**

---

<!-- 3.5 -->
<!-- layout: recap -->

# Recap: services, networks, lifecycle

- Service attacks come from trusting input; the server must enforce rules.
- DoS attacks availability; MITM reads unencrypted traffic, encryption defeats it.
- Attacks move through stages, and **defense in depth** breaks the chain at any one of them.

**Next lesson:** passwords and authentication, in depth.
