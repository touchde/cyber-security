# Section 1: What Cybersecurity Is

> Covers chapter 1 in the [outline](../../../planning/outline.md).

## What You Will Learn

- What cybersecurity is, in plain words, and what it protects.
- Why it matters now, for a business, a person, and a whole country.
- The three questions every security person asks: can the wrong people **read** it, **change** it, or **stop** it?
- What a threat, a vulnerability, and a risk are, and how they differ.
- Why defense is built in layers, and why security is everyone's job.
- Why we learn to attack: to defend well, you must understand how attacks work.
- The one rule you must never break: only test what you own, or have written permission to test.

## Before You Start

You need nothing but a computer, a web browser, and curiosity. No programming, no networking, and no security knowledge. This is the first lesson of the whole program; the courses that teach the keyboard skills, Linux, networks, and code come after it.

**The one rule, from the very first lesson:** everything in these courses is for defending. Later you will learn real attacks, but you try them **only** on systems you own, or that you have clear written permission to test, such as the practice lab you will build in a later course. Attacking anyone else's computer, phone, website, or account, even "just to look", can harm real people, and in Cambodia and almost every country it is a crime. Topic 10 returns to this rule, and lesson 9 is devoted to it.

---

## 1. A Real Incident: How One Email Locked a Business

Start with a kind of attack that happens somewhere in the world every day.

A small business runs on computers: a tablet takes orders, a laptop handles payroll, files sit on a shared drive. One morning the laptop shows a full-screen message in red: *"Your files are locked. Pay to get them back."* The sales records, the staff details, the supplier list, none of them will open.

What happened? A week earlier, an employee received an email that looked like it came from the company's internet provider: *"Your bill is overdue, open the attached invoice."* They opened the attachment. It quietly installed a program that encrypted the files and waited.

Nobody picked a lock. Nobody broke a window. One email, one click, and a business lost access to everything it runs on. This kind of attack is called **ransomware**, and it is one of the most common serious attacks today. It is a good first example because it shows the whole subject in one picture: something valuable (the files), a way in (a fake email), a weakness (an employee who clicked), and harm (a business that cannot work). Cybersecurity is the practice of understanding that picture and changing the ending.

## 2. What Cybersecurity Is

**Cybersecurity is protecting information and the systems that hold it from people who should not read it, change it, or stop it from working.**

Break that sentence into its parts:

- **Information** is anything worth protecting: sales records, a phone number, a password, a photo, a bank balance.
- **Systems** are the things that store, move, and use that information: laptops, phones, servers, apps, websites, and the networks between them.
- **People who should not** are the attackers: from a curious insider, to a criminal who locks files for money, to a team paid by a government.

An older name is **information security**, or **infosec**. People use "cybersecurity", "information security", and simply "security" to mean much the same thing. In this program we usually say **security**.

Security is not a product you buy once, and it is not a single lock. It is an ongoing practice: understanding what could go wrong, deciding what is worth protecting, putting defenses in place, and watching for the attacks that get through.

## 3. Why It Matters Now

Thirty years ago, a business kept its records on paper in a drawer. To steal them, you had to be in the room. Today those same records sit on a computer connected to the whole world, and an attacker can reach them from another country, at no cost, while you sleep.

Almost everything now runs on computers and networks: shops, banks, hospitals, schools, phones, cars, power stations. That makes life easier, and it makes a new kind of harm possible:

| What depends on computers | What an attack can do |
|---|---|
| A business's records and payroll | Lock the files; stop the business for days |
| A person's phone and messages | Read private chats; steal money from a banking app |
| A bank or payment app | Move money; take over accounts |
| A hospital's records | Block access to patient information during an emergency |
| A city's power or water | Turn off a service that millions depend on |

This is close to home. In Cambodia, as smartphones, online banking, and QR payments have spread, scams and account takeovers have grown with them. Security is no longer a concern only for large foreign companies. It matters for a small business, for every person with a phone, and for the country.

Security is about **risk**, not perfection. No system is ever perfectly safe, and trying to make one perfect would cost more than it is worth. The useful questions are always: what could go wrong, how likely is it, how bad would it be, and what does it cost to prevent? A coffee shop needs less protection than a bank. Neither needs zero.

## 4. What We Protect: Information and Systems

Before you can defend something, you have to know what is worth defending. Security people call these things **assets**. An asset is anything that has value to you, and therefore might have value to an attacker.

Think about a dental clinic. Its assets include:

| Asset | Why it has value |
|---|---|
| Patient records | Private and legally protected; valuable to steal or hold for ransom |
| The appointment system | If it goes down, the clinic cannot see patients |
| The payment and banking details | Direct access to money |
| Staff accounts and passwords | A way in to everything else |
| The clinic's reputation | Patients who feel unsafe go elsewhere |

Notice the last one. It is not a file or a machine. **Trust and reputation are assets too.** A clinic can restore locked files from a backup in an hour, but winning back a patient who heard "that clinic leaked my records" can take far longer.

Knowing your assets is the first step of every security decision, because you cannot protect everything equally. You protect what matters most, first.

## 5. The Three Questions

When a security person looks at any system, they ask three questions. These three are the heart of the subject, and the next lesson studies them in depth as the **CIA triad**. In plain words:

1. **Can the wrong people _read_ it?** Keeping information from people who should not see it is called **confidentiality**. Example: only your bank and you should be able to read your account balance.
2. **Can the wrong people _change_ it?** Keeping information correct, and changed only in the right way, is called **integrity**. Example: nobody should be able to change the price on an online order from $100 to $1.
3. **Can the wrong people _stop_ it?** Keeping a system working when people need it is called **availability**. Example: a hospital's records must open during an emergency.

These three give you a quick way to describe almost any attack. The ransomware in topic 1 was an **availability** attack: the files were not read or changed, they were locked, so the business could not use them. Quietly copying a customer list to sell is a **confidentiality** attack. Giving yourself a discount you did not earn is an **integrity** attack. Almost every idea in this whole program protects one of these three: read, change, or stop.

## 6. Threats, Vulnerabilities, and Risk

Three words get used constantly, and mixing them up causes confusion. They are different things.

- A **threat** is something bad that _could_ happen, or someone who could make it happen. "A criminal could lock our files for money" is a threat.
- A **vulnerability** is a weakness that would let the bad thing happen. "Staff open email attachments without checking" is a vulnerability.
- A **risk** is the chance of the threat meeting the vulnerability, together with how bad the result would be. "It is fairly likely a staff member opens a bad attachment, and it would stop the business for days" is a risk.

A simple way to hold them together:

> **Risk = how likely × how bad.**

A threat with no matching vulnerability is not much of a risk. A locked door is a threat to someone with the wrong key, but not to someone with the right one. And a vulnerability that no threat targets may sit harmlessly for years, until one day it does not. Security work is finding the risks that are both likely and serious, and reducing them first.

Lesson 3 rates and manages risk properly. For now, keep the three words apart: a **threat** is the bad event, a **vulnerability** is the weakness, and a **risk** is the chance and the cost of the two meeting.

## 7. Defense Is Layers

The business in topic 1 did not have to lose its files. Suppose it had done a few ordinary things:

1. **Training**, so the employee paused at a strange invoice email.
2. **An email filter**, that quietly moved the message to junk.
3. **Up-to-date software**, so the attachment's trick no longer worked.
4. **A separate account** for daily work, so the locking program could not reach every file.
5. **A backup**, made every night and kept disconnected, so the files could be restored in an hour.

Now the attacker has to get past *all five*. Miss the email filter? Training stops the click. Click anyway? The backup saves the day. This is **defense in depth**: several layers of protection, so that one failure does not become a disaster.

No single defense is perfect. People get tired and click. Software has bugs. Filters miss things. Because every layer can fail, we never rely on just one. A good security plan assumes each defense will sometimes fail, and places another one behind it. Lesson 8 returns to this idea with the different kinds of control.

## 8. Security Is Everyone's Job

It is tempting to think security is one expert's job, or one product you install. It is neither. In the ransomware example, the weak point was not a machine. It was an ordinary email and an ordinary click.

Everyone involved has a part:

| Who | Their part in security |
|---|---|
| The owner or manager | Decides what matters, pays for backups and training, sets the rules |
| The staff | Spot strange emails, use good passwords, follow the rules |
| The developer | Builds software that does not leak data or trust the wrong things |
| The server / IT | Checks every request and owns the important decisions |
| The security specialist | Finds weaknesses, watches for attacks, and responds when one gets through |

A common and dangerous mistake is for each part to assume another is handling it: "the developer made it secure, so we're fine", or "we have antivirus, so we don't need backups". Security holds only when each part does its own job, and does not assume the others cover for it.

## 9. Why We Learn to Attack

This program teaches you how attacks work, and how to carry them out, in a safe lab. That surprises some people. Why learn to attack, if the goal is to defend?

Because **you cannot defend against what you do not understand.** If you have never seen how a file gets locked, how a password is cracked, or how a fake email is built, your defenses are guesses. The people who protect banks and governments are the same people who know, in detail, how to break in. They have simply chosen to use that knowledge to defend, and to use it only where they are allowed.

Think of a locksmith. To fit good locks, a locksmith must understand how locks are picked. The skill is the same; what differs is permission and intent. A locksmith who picks a lock because the owner hired them is doing their job. The same person picking a stranger's door is a burglar.

So in these courses you will learn real attacks: reading a password out of a program, intercepting network traffic, taking over a practice server. You will do all of it on systems built for the purpose. Which brings us to the rule that makes all of this safe and legal.

## 10. Ethics and the Law: The One Rule

Here is the rule again, because it matters more than any technique in this program:

> **Only ever test systems that you own, or that you have clear, written permission to test.**

Everything you will learn, every attack and every tool, is powerful. Used on your own lab, or on a system whose owner has hired you, it is a valuable skill that pays well. Used on anyone else's system without permission, the exact same action is a crime, whatever your reason.

- "I was only curious" is not permission.
- "The website was easy to break into" is not permission.
- "I didn't change anything, I only looked" is not permission.
- "I found a bug and wanted to help" is not permission, unless the owner invited you to look.

Getting permission properly, scope, rules of engagement, and bug bounty programs, is covered in lesson 9 and again in the offensive courses. Until then, the safe rule is simple: your own lab, or written permission. There is no third option. A skilled person who respects this rule is a professional. One who does not is a criminal, and the skill is exactly the same.

## 11. The Road Ahead

This is one of 43 courses. They fit together like this:

| Stage | Courses | What you gain |
|---|---|---|
| **Foundations** | Security basics, how computers work, Linux, networking, Windows, scripting, Python, a home lab, cryptography | The ground every security person stands on |
| **Offensive** | Web, mobile, network, and wireless attacks, reverse engineering, exploitation, red teaming | How attacks really work, hands-on in the lab |
| **Defensive** | Security operations, incident response, forensics, malware analysis, threat intelligence | How to watch, catch, and recover from attacks |
| **Engineering** | Secure development, cloud, containers, identity | How to build systems that are hard to attack |
| **Specialized** | Industrial systems, fraud and banking, blockchain, AI security, governance, careers | Deep fields, and turning the skills into a job |

Everyone starts with Foundations, in order. After that you pick a path. You do not have to finish all 43 to be useful; after Foundations and one path, you are employable. But a complete security professional eventually touches all of them.

By the end of **this course**, Security Fundamentals, you will understand the core ideas, speak the language, and be ready for the hands-on courses. The next lesson begins that work by studying the three questions in depth: the CIA triad and beyond.

---

## Common Mistakes

**1. Thinking "we are too small to be a target."** Attackers often do not choose you on purpose. Automated attacks sweep the whole internet, and a small business with a weak defense is an easier catch than a bank.

**2. Buying one product and feeling safe.** Antivirus, or a firewall, or a password rule, is one layer. Security is many layers, plus people and habits.

**3. Confusing threat, vulnerability, and risk.** The bad event, the weakness, and the chance-and-cost of the two meeting are three different things. Keep them apart.

**4. Chasing perfect security.** No system is perfectly safe. Spend your effort on the risks that are both likely and serious.

**5. Thinking security is only the expert's job.** The weakest point is often an ordinary person and an ordinary click. Everyone has a part.

**6. Believing "learning to attack is wrong."** Learning how attacks work is how you defend. What matters is that you only ever practise on your own systems, or with written permission.

**7. Testing a system you do not own.** Curiosity is not permission. Only your own lab, or clear written permission. This one has no exceptions.

## Summary

| Idea | Remember |
|---|---|
| Cybersecurity | Protecting information and systems from people who should not read, change, or stop them |
| Why it matters now | Everything runs on computers and networks; attacks reach you from anywhere |
| Risk, not perfection | Protect against what is likely and serious; nothing is ever perfectly safe |
| Assets | The things worth protecting, including trust and reputation |
| The three questions | Can the wrong people read it, change it, or stop it? (confidentiality, integrity, availability) |
| Threat / vulnerability / risk | The bad event / the weakness / the chance and cost of the two meeting |
| Defense in depth | Several layers, so one failure is not a disaster |
| Everyone's job | Owner, staff, developer, server, and specialist each have a part |
| Learn to attack | You cannot defend what you do not understand; permission and intent make it right |
| The one rule | Only test what you own, or have written permission to test |

## Check Your Understanding

1. In one sentence, what is cybersecurity?
2. A ransomware attack locks a business's files but does not read or steal them. Which of the three questions (read, change, stop) does that attack belong to?
3. Give one example each of a threat, a vulnerability, and a risk, different from the ones in the lesson.
4. Why is "trust and reputation" called an asset, when it is not a file or a machine?
5. What is defense in depth, and why do we use it instead of one strong defense?
6. A friend says, "learning to hack is just learning to be a criminal." How would you answer?
7. State the one rule for testing systems, and explain why "I was only curious" does not meet it.

**Answers**

1. Cybersecurity is protecting information and the systems that hold it from people who should not read it, change it, or stop it from working.
2. Availability: the files were not read or changed, but the business could not use them when it needed them.
3. Any sensible set, for example: threat, "someone could steal an employee's phone"; vulnerability, "the phone has no screen lock"; risk, "phones are often lost, and this one holds the company's banking app, so the risk is high".
4. Because it has value and an attacker can damage it. If customers hear their data leaked, they stop trusting the business, which costs it money, even though no machine was broken.
5. Several layers of defense, so that if one fails, another still stops the attack. We use it because every single defense can fail: people click, software has bugs, filters miss things.
6. Learning how attacks work is how you build real defenses, just as a locksmith must understand lock-picking to fit good locks. What makes it right or wrong is permission and intent: we only ever practise on our own systems, or with written permission.
7. Only test systems you own, or have clear written permission to test. Curiosity is not permission: the harm to the owner, and the law, do not change because you were curious or meant no harm.

## Practice

Think about a system you use every day: your phone, a messaging app, your school or work email, or an online bank.

1. List three **assets** it holds or protects that would matter to you if an attacker reached them.
2. For each asset, say which of the three questions worries you most: could the wrong people **read** it, **change** it, or **stop** it?
3. Name one **layer** of defense that already protects it (for example a screen lock, a password, two-step sign-in), and one more layer you could add.

There is no single right answer. The goal is to practise looking at an everyday system the way a security person does: what is valuable, what could go wrong, and what layers stand in the way.

### A Worked Example

For a phone with a banking app:

1. Assets: the money in the banking app; private messages; saved photos.
2. Worries: for the banking app, that the wrong people could **change** it (move money) or **stop** it; for messages and photos, that the wrong people could **read** them.
3. A layer already there: the phone's screen lock and the app's sign-in. A layer to add: two-step sign-in (a code as well as a password) on the banking app, so a stolen password alone is not enough.
