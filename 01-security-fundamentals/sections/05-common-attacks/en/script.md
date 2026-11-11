# Section 5: Common Attacks: Phishing, Malware, and More — Video Scripts

Three videos, about 12 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos. Every attack is explained to defend against; the ethics rule is stated on the opening slide.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | How Attacks Start, and Attacking People | 1.1–1.5 | about 4 min |
| 2 | Malware and Password Attacks | 2.1–2.5 | about 4 min |
| 3 | Services, Networks, and the Attack Lifecycle | 3.1–3.5 | about 4 min |

---

## Video 1 — How Attacks Start, and Attacking People

### 1.1 — Title

**Show:** slide 1.1

**Say:** This lesson is a map of the common attacks. Each one is explained so you can recognize and defend against it, and each is studied in depth, safely and legally, in a later course. One reminder before we start: everything here is for defending, and these are only ever tried on systems you own or have written permission to test. Let's begin with how attacks actually start.

**Time:** about 0:30

### 1.2 — How most attacks start

**Show:** slide 1.2

**Say:** Attacks usually aren't a single dramatic break-in. They start small and quiet, almost always through one of three doors. One: a person is tricked into clicking, opening, or telling. Two: a weakness is exploited in software that's exposed to the internet and hasn't been updated. Three: a stolen or guessed password is used to simply log in. Study after study of real breaches finds the same thing: the large majority start with one of these three, very often the first. The attacker doesn't need to be a genius; they need one click, one unpatched server, or one reused password. And that's actually good news for defenders, because a few basic defenses aimed at these three doors stop most attacks.

**Time:** about 0:55

### 1.3 — Phishing and social engineering

**Show:** slide 1.3

**Say:** Social engineering means attacking the person instead of the computer, tricking someone into helping the attacker. It works because it's far easier to fool a human than to break strong encryption. Phishing is the most common form: a fake message, usually email, pretending to be someone you trust, to make you click a link, open an attachment, or hand over a password. It has variants: spear phishing is targeted and personalized; whaling aims at an important person like a CEO; smishing and vishing are the same idea by text and by voice call. And business email compromise poses as a boss or supplier to get an employee to pay a fake invoice, stealing huge sums with no malware at all. The signs: urgency, a request for a password or payment, a slightly wrong sender address, and a link that doesn't go where it claims.

**Time:** about 1:00

### 1.4 — Defending against phishing

**Show:** slide 1.4

**Say:** How do you defend? Train staff and keep a healthy suspicion. Check the real sender address, and verify any urgent request through another channel, call the person, don't reply to the email. Never act on urgency without checking. Use email filtering to catch the obvious ones. And turn on multi-factor authentication, so even a stolen password isn't enough on its own. One warning: modern phishing can be flawless, with no typos at all, so don't rely on spotting mistakes. Verify the sender and the request.

**Time:** about 0:45

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: most attacks begin with a tricked person, an unpatched system, or a stolen password. Phishing attacks the person, and it comes by email, text, and call. Verify the sender and the request, use MFA, and don't trust urgency. Next, the attacks that target machines and passwords.

**Time:** about 0:30

---

## Video 2 — Malware and Password Attacks

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video we look at malware, the kinds and how they differ, and then at how passwords are attacked, which is a whole category of its own.

**Time:** about 0:20

### 2.2 — Malware: the main kinds

**Show:** slide 2.2

**Say:** Malware is any software written to do harm, and the word covers several kinds, grouped by how they spread and what they do. A virus attaches to a file or program and spreads when a person runs or shares it. A worm spreads by itself across a network, with no human action, by exploiting weaknesses. A trojan pretends to be something useful, a free game, a cracked app, so you install it yourself. Ransomware locks or encrypts your files and demands payment. Spyware secretly watches you. A botnet turns your machine into one of thousands the attacker controls. These overlap, one real sample can be a trojan that installs spyware and later ransomware, so what matters for defense is the behavior, not the label.

**Time:** about 0:55

### 2.3 — Defending against malware

**Show:** slide 2.3

**Say:** The defenses follow from the behavior. Keep software updated, because worms spread through known, unpatched holes. Don't run untrusted programs or attachments. Use anti-malware tools. Limit accounts to least privilege, so malware can't reach everything on the machine or network. And keep offline backups, so ransomware can't destroy your only copy. Notice how many of these we've already seen, updates, least privilege, backups, because the same basic defenses stop many different attacks.

**Time:** about 0:45

### 2.4 — Password attacks

**Show:** slide 2.4

**Say:** Because passwords guard so much, attacking them is its own category. Brute force tries millions of passwords. A dictionary attack tries common words and passwords first, because people pick them. Credential stuffing takes username-and-password pairs leaked from one breached site and tries them on others, and it's one of the most effective attacks today, purely because people reuse passwords. Password spraying tries one or two very common passwords against many accounts, to avoid locking any single one. Now, an important point: attackers rarely guess against a live login screen, which is slow and noisy. More often they steal a file of stored passwords and attack it offline. That's why how passwords are stored matters so much, they should be protected with slow password hashing, never plain text. The defenses: long unique passwords, which a password manager makes easy; multi-factor authentication, which defeats a stolen password; and, on the server side, strong slow hashing.

**Time:** about 1:00

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: malware spreads in different ways, virus, worm, trojan, and you defend by behavior with updates, least privilege, and offline backups. Passwords are mostly cracked offline, and credential stuffing feeds on password reuse. Unique passwords plus MFA defeat most password attacks. Next, attacks on services and networks, and how whole attacks are structured.

**Time:** about 0:30

---

## Video 3 — Services, Networks, and the Attack Lifecycle

### 3.1 — Title

**Show:** slide 3.1

**Say:** In this final video: attacks on web and network services, two network attacks called denial of service and man-in-the-middle, and the attack lifecycle that ties a whole attack together.

**Time:** about 0:20

### 3.2 — Web and network service attacks

**Show:** slide 3.2

**Say:** Any service exposed to the internet, a website, an app's back end, a mail server, is a door an attacker can knock on. Three common web attacks. SQL injection: sending crafted input that the server mistakes for a command, letting an attacker read or change the database. Cross-site scripting, or XSS: sneaking malicious code into a web page so it runs in other users' browsers. And broken access control: reaching data or actions you shouldn't, like viewing another user's account by changing a number in the address. The common thread is trusting input that shouldn't be trusted. The defense, broadly, is to treat all input as untrusted and make the server, not the user, enforce the rules. The standard list of these is the OWASP Top 10, which we'll meet in lesson 10.

**Time:** about 0:55

### 3.3 — Denial of service and man-in-the-middle

**Show:** slide 3.3

**Say:** Two network attacks. A denial-of-service attack doesn't steal or change data; it attacks availability, by overwhelming a system with a flood so real users can't use it. A distributed version, DDoS, sends the flood from many machines at once, often a botnet of thousands of infected devices, which makes it bigger and much harder to block. The defenses are extra capacity, filtering, and anti-DDoS services. The second attack is man-in-the-middle: the attacker secretly sits between you and who you think you're talking to, reading or changing the messages. The classic setting is open public Wi-Fi. If the traffic is unencrypted, they see everything. That's exactly why HTTPS matters: it encrypts the connection and checks you're really talking to the right site. So use encrypted connections everywhere, and heed certificate warnings instead of clicking past them.

**Time:** about 0:55

### 3.4 — The attack lifecycle

**Show:** slide 3.4

**Say:** Finally, most serious attacks aren't one action but a sequence of stages, and security people model that sequence with tools like the Cyber Kill Chain and MITRE ATT&CK. A simplified version: reconnaissance, researching the target; initial access, getting in; establishing a foothold to keep access; escalating privileges from a normal account to an administrator; moving laterally to more valuable machines; and finally acting on the objective, stealing data or deploying ransomware. Here's the key insight: the attacker has to succeed at every single stage, but the defender only has to stop one. Catch the phish and you stop stage two. Apply least privilege and you block the escalation. Monitor the network and you spot the lateral movement. Keep offline backups and you blunt the final act. Every layer is a chance to break the chain.

**Time:** about 1:00

### 3.5 — Recap

**Show:** slide 3.5

**Say:** So, to close the lesson: service attacks come from trusting input, so the server must enforce the rules. Denial of service attacks availability, and man-in-the-middle reads unencrypted traffic, which encryption defeats. And attacks move through stages, which means defense in depth lets you break the chain at any one of them. Next lesson, we go deep on the single most attacked thing in security: passwords and authentication.

**Time:** about 0:30
