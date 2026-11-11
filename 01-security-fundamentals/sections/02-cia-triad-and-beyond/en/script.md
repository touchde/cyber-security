# Section 2: The CIA Triad and Beyond — Video Scripts

Three videos, about 11 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | The Three Core Goals | 1.1–1.6 | about 4.5 min |
| 2 | Controlling Who Does What | 2.1–2.4 | about 3 min |
| 3 | Balancing the Goals | 3.1–3.4 | about 3 min |

---

## Video 1 — The Three Core Goals

### 1.1 — Title

**Show:** slide 1.1

**Say:** In the last lesson we asked three questions about any system: can the wrong people read it, change it, or stop it. In this lesson we give those questions their proper names, the CIA triad, and add the goals that sit around them. Let's start with why we need named goals at all.

**Time:** about 0:25

### 1.2 — Why we need clear goals

**Show:** slide 1.2

**Say:** "Make it secure" is not a plan. Secure against what? Readable by whom? Working how often? Without named goals, two people can both say a system is secure and mean completely different things, and neither can check whether it's true. So security people use a small set of named goals. When you can say which goal you're protecting, you can design for it, test it, and tell when it fails. The oldest and most useful set is three, known together as the CIA triad. And just to clear this up: the name is only the first letters. It has nothing to do with any intelligence agency.

**Time:** about 0:50

### 1.3 — Confidentiality

**Show:** slide 1.3

**Say:** The first goal is confidentiality: only the right people can read the information. This is what most people first think of as security, keeping secrets secret. It's broken by a data breach: a stolen laptop, a database left open on the internet, an email sent to the wrong person, or traffic read on an open Wi-Fi network. The main tools are encryption, which scrambles data so only someone with the key can read it; access control, deciding who may open what; and authentication, proving who someone is. A quick test: if this fell into a stranger's hands, would it matter? If yes, it needs protecting.

**Time:** about 0:55

### 1.4 — Integrity

**Show:** slide 1.4

**Say:** The second goal is integrity: the information is correct, and changed only by the right people, in the right way. Confidentiality is about reading; integrity is about changing. A bank balance anyone could edit would be useless, even if nobody could read it. And integrity covers two kinds of change: malicious, like an attacker altering a payment, and accidental, like a bug or a faulty disk corrupting a file. The main tools are hashing, which is a short fingerprint of the data that changes if the data changes; digital signatures; and validation. Quick test: if someone changed this without permission, who would be harmed, and would we even notice?

**Time:** about 0:55

### 1.5 — Availability

**Show:** slide 1.5

**Say:** The third goal is availability: the system works when the people who need it need it. Information that's perfectly secret and perfectly correct is still useless if you can't reach it. A hospital record you can't open in an emergency has failed, even though nobody read it or changed it. Availability is broken by ransomware, by a flood of fake traffic, by a power cut, by a failed disk. It's the goal most often harmed by accident, not just by attackers. The main tools are backups, redundancy, which means spare servers and power, and enough capacity plus filtering against floods. Quick test: if this were unreachable for an hour, a day, a week, what would it cost?

**Time:** about 0:55

### 1.6 — Recap

**Show:** slide 1.6

**Say:** So, named goals let us design, test, and detect failures. Confidentiality is who can read it. Integrity is who can change it. Availability is whether it works when needed. Remember that integrity covers accidents as well as attacks, and that availability is security too, not just an IT concern. Next, the goals that control who does what.

**Time:** about 0:30

---

## Video 2 — Controlling Who Does What

### 2.1 — Title

**Show:** slide 2.1

**Say:** The CIA triad says what we protect. This video is about how we control who does what. You'll meet three supporting goals, together called AAA, and one more called non-repudiation.

**Time:** about 0:20

### 2.2 — AAA

**Show:** slide 2.2

**Say:** AAA stands for authentication, authorization, and accounting. Authentication answers "who are you?", usually with a password, a code, a fingerprint, or a passkey. Authorization answers "what are you allowed to do?" A bank teller and a bank manager sign in the same way but may do different things. And accounting, also called auditing, answers "what did you do?" It's the record, the logs, of who did what and when. Accounting doesn't stop an attack by itself, but it lets you detect one, investigate it, and prove what happened. A simple way to remember the order: you authenticate to prove who you are, the system authorizes what you can do, and it accounts for what you did.

**Time:** about 0:55

### 2.3 — Non-repudiation

**Show:** slide 2.3

**Say:** The last goal is non-repudiation: someone cannot credibly deny they did something. If you sign a contract, you shouldn't be able to later claim you never did. In the digital world this comes mainly from digital signatures plus solid logs, which tie an action to a person strongly enough that they can't plausibly deny it. It matters most for money, contracts, and legal records. Notice it builds on two earlier goals: integrity, so the record wasn't changed, and authentication, so we know who acted.

**Time:** about 0:45

### 2.4 — Recap

**Show:** slide 2.4

**Say:** To recap: authentication proves who you are, authorization decides what you may do, accounting records what you did, and non-repudiation means you can't deny you did it. These support the CIA triad, weak authentication, for example, breaks both confidentiality and integrity. Next, why these goals pull against each other, and how to balance them.

**Time:** about 0:30

---

## Video 3 — Balancing the Goals

### 3.1 — Title

**Show:** slide 3.1

**Say:** We now have seven goals. In this last video, we see why you can't just turn all of them up to maximum, and how to use them as a practical checklist.

**Time:** about 0:20

### 3.2 — The goals pull against each other

**Show:** slide 3.2

**Say:** The goals pull against each other. Improving one often costs another. Push confidentiality up with more locks and more passwords, and you hurt availability and ease of use. Make everything easy to reach for availability, and you open more ways to leak. Approve every change for integrity, and you slow everything down. And security in general always trades against usability and cost. Picture a bank that required five passwords and a manager's approval for every single transaction. Very strong on confidentiality and integrity, completely unusable. So a good design is a balance, chosen on purpose, not every goal maxed out.

**Time:** about 0:50

### 3.3 — The goals as a checklist

**Show:** slide 3.3

**Say:** The real value of these goals is as a checklist for any system. Take an online shop. Confidentiality: who can read addresses and card details? Integrity: can anyone change a price or an order total? Availability: what happens on the busiest sales day, or under attack? Authentication: how do customers and staff prove who they are? Authorization: can a customer reach another customer's order? Accounting: if money went missing, could we trace it? And non-repudiation: can a customer deny a purchase they made? You won't have perfect answers yet, that's what the rest of the program is for, but asking these seven questions already puts you ahead of most people building systems.

**Time:** about 0:55

### 3.4 — Recap

**Show:** slide 3.4

**Say:** So: the goals trade against each other and against usability, and you choose a balance based on risk, spending protection where the asset is valuable and the threat is real. And the seven goals together make a checklist for thinking about any system. Next lesson, we look at how we actually measure and manage the dangers these goals face: threats, vulnerabilities, and risk.

**Time:** about 0:35
