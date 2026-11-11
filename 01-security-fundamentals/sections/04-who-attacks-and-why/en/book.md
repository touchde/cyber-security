# Section 4: Who Attacks and Why

> Covers chapter 4 in the [outline](../../../planning/outline.md).

## What You Will Learn

- Why the "lone hooded hacker" picture is mostly wrong.
- The main kinds of attacker, from opportunists to nation-states.
- Why insiders are a special and often underrated threat.
- The motivations behind attacks: money, information, disruption, and belief.
- What knowing your likely attackers means for how you defend.

## Before You Start

Read lessons 1 to 3. This lesson puts faces to the "threat sources" from lesson 3, and connects them to the risks you would put in a register. No programming or networking is needed.

---

## 1. The Myth of the Hooded Hacker

Films show a lone genius in a dark room, in a hoodie, breaking into a bank in minutes by typing fast. Real attackers look nothing like this, and believing the myth leads to poor defenses.

The reality:

- Most attacks are **not** targeted at you personally. They are automated, sweeping the whole internet for any weak system, the way a thief tries every car door in a street.
- Many serious attackers are **organized groups**, run like businesses, with staff, budgets, and office hours, not lone geniuses.
- Most break-ins use **ordinary weaknesses**, a reused password, an unpatched program, a convincing email, not movie-style wizardry.
- The slow, boring parts, researching a target, waiting, trying again, matter far more than fast typing.

Knowing who really attacks, and why, lets you defend against the attacks you will actually face, instead of the ones in films. We will go through the main kinds of attacker, usually grouped by skill, organization, and motive.

## 2. Script Kiddies and Opportunists

At the least-skilled end are **script kiddies**: people who use tools and attacks that others built, without deeply understanding them. The name sounds harmless, but they do real damage, because the tools are powerful and freely available.

Closely related are **opportunists**: attackers who are not after you specifically, but will take any easy target they find. Most automated internet attacks are opportunistic. They scan millions of addresses for a known weakness and attack whatever answers.

- **Skill:** low to moderate; they rely on ready-made tools.
- **Targets:** whoever is easy; no particular victim.
- **Motive:** curiosity, showing off, small money, or just because they can.
- **Defense:** basic security stops most of them. Keep software updated, use strong unique passwords, and don't expose services you don't need. Opportunists move on to an easier target.

The key lesson: because so many attacks are opportunistic, **ordinary, basic defenses stop the majority of attacks**. You do not need to be unbreakable, only harder than the next target.

## 3. Cybercriminals and Ransomware Crews

The largest serious threat to most businesses is **organized cybercrime**: groups that attack for money, run like companies. Ransomware crews are the most visible today.

They operate as a real industry. Some groups write the ransomware and rent it to others (this is called **ransomware-as-a-service**). Others specialize in breaking in, or in laundering the money. They have support desks, negotiators, and profit targets. They often steal the data first and then lock it, so they can threaten to publish it even if you have backups (this is called **double extortion**).

- **Skill:** moderate to high, and well-resourced.
- **Targets:** anyone who can pay, from hospitals to small businesses; they pick by profit, not grudge.
- **Motive:** money, directly.
- **Defense:** the full defense-in-depth stack, offline backups above all, plus training, patching, and multi-factor authentication. The whole defensive side of this program exists largely to counter these groups.

## 4. Insiders

Not every attacker is outside. An **insider** is someone who already has legitimate access: an employee, a contractor, a supplier. Insiders are dangerous precisely because they are trusted and already inside your defenses.

There are two kinds:

- **Malicious insiders:** people who abuse their access on purpose, to steal data, to commit fraud, or out of anger (for example, a worker who copies the customer list before quitting to join a rival).
- **Accidental insiders:** people who cause harm by mistake, by far the more common, who fall for phishing, misconfigure a server, email a file to the wrong person, or lose a laptop.

Insiders are underrated because defenses usually point outward. The controls that help are **least privilege** (give each person only the access they need, lesson 7), **logging and monitoring** (accounting, lesson 2), separation of duties, and a culture where people feel able to report mistakes rather than hide them.

## 5. Hacktivists

**Hacktivists** attack to make a political or social point. The word joins "hacker" and "activist". Their aim is usually attention, not money: defacing a website with a message, leaking documents they think the public should see, or knocking a service offline to protest an organization's actions.

- **Skill:** varies widely, from basic to capable.
- **Targets:** organizations they oppose: governments, companies, institutions in the news.
- **Motive:** belief, protest, publicity.
- **Defense:** the same fundamentals, with extra attention to anything public-facing (websites, social accounts) and to the ability to withstand a flood of traffic. Because the goal is attention, availability attacks and public defacement are common.

## 6. Nation-State and Advanced Persistent Threats

At the top end are **nation-state** attackers: teams funded by governments. In security their long campaigns are often called **APTs**, for **Advanced Persistent Threat**. The three words describe them well:

- **Advanced:** well-funded, highly skilled, sometimes using weaknesses nobody else knows about yet (called **zero-days**).
- **Persistent:** they do not give up after one try. They may stay hidden inside a network for months or years, pursuing a long-term goal.
- **Threat:** they have clear intent and real capability.

Their motives are national: espionage (stealing secrets from governments and companies), sabotage (damaging an enemy's systems, including power and industry, the subject of the OT/ICS course), and influence.

- **Targets:** governments, defense, large companies, infrastructure, and sometimes smaller companies used as a stepping-stone to a bigger one.
- **Defense:** very hard to stop completely. Most organizations cannot outspend a government. The realistic goals are to make yourself a costly target, to detect intrusions quickly (the SOC and threat-hunting courses), and to limit the damage.

Most small businesses will never be a nation-state's direct target, but they can be caught in a **supply-chain** attack, where the real target is a bigger customer reached through them.

## 7. Motivations: Money, Information, Disruption, and Belief

Cutting across all these groups are a few basic motives. Knowing the motive helps you predict what an attacker wants and how they will behave.

| Motive | What they want | Typical attacker |
|---|---|---|
| **Money** | Direct payment, fraud, stolen accounts, resold data | Cybercriminals, ransomware crews |
| **Information** | Secrets, designs, personal data, credentials | Nation-states, competitors, data thieves |
| **Disruption** | To stop a service, damage, or cause chaos | Hacktivists, nation-states, disgruntled insiders |
| **Belief** | To make a point, protest, or gain attention | Hacktivists |
| **Ego / curiosity** | To prove it can be done, or to learn | Script kiddies, some opportunists |

Most attacks you will meet in business are about **money**. That is why ransomware and fraud dominate, and why the defensive courses spend so much time on them.

## 8. What This Means for Defending

You cannot defend equally against everyone, so you defend against the attackers you are actually likely to face. This is sometimes called knowing your **threat model**.

- A **small shop** mostly faces opportunists and ransomware crews. Basic hygiene, updates, strong passwords, MFA, and offline backups, defeats the large majority of what it will meet.
- A **hospital or bank** faces the same, plus targeted criminals and, for a bank, fraud rings. It needs the full defensive stack and strong monitoring.
- A **government department or defense contractor** faces nation-states as well, and must plan for persistent, skilled attackers and quick detection.
- **Every** organization faces insiders, so least privilege and logging matter everywhere.

The encouraging news from this lesson is that most attacks are opportunistic and use ordinary weaknesses, so ordinary, well-applied defenses stop most of them. You rarely need to be unbreakable. You need to be a harder, less profitable target than the next one, and to detect and recover quickly when something does get through. The rest of this course builds those ordinary defenses, and the paths that follow make them deep.

---

## Common Mistakes

**1. Defending against the movie hacker.** Real attacks are mostly automated, opportunistic, and use ordinary weaknesses. Defend against those first.

**2. "We're too small to be targeted."** Opportunistic attacks don't choose you; they find you. Small organizations are attacked constantly, precisely because they are soft.

**3. Ignoring insiders.** Most defenses point outward, but trusted people, usually by accident, cause a large share of incidents.

**4. Assuming every attacker is a genius.** Many use ready-made tools. Basic defenses stop them. Save your worry for the threats your organization actually faces.

**5. Planning to stop nation-states as a small business.** You usually cannot outspend a government. Aim to be costly to attack, quick to detect, and able to recover.

**6. Forgetting the motive.** Knowing whether an attacker wants money, information, or attention tells you what they'll go for and how they'll behave.

## Summary

| Attacker | Skill | Motive | Main defense |
|---|---|---|---|
| Script kiddies / opportunists | Low | Curiosity, small gain | Basic hygiene; be harder than the next target |
| Cybercriminals / ransomware | Moderate–high | Money | Defense in depth; offline backups |
| Insiders | Any (they're trusted) | Money, anger, or accident | Least privilege; logging; culture |
| Hacktivists | Varies | Belief, publicity | Protect public-facing systems; withstand floods |
| Nation-states / APTs | Very high | Espionage, sabotage | Detect fast; limit damage; be costly to hit |

## Check Your Understanding

1. Give two ways the real picture of attackers differs from the movie "hooded hacker".
2. Why do basic defenses stop most opportunistic attacks?
3. What is double extortion, and why does it defeat backups alone?
4. Name the two kinds of insider, and say which is more common.
5. What do the three words in "Advanced Persistent Threat" each mean?
6. Match these motives to a likely attacker: money; information; publicity.
7. A small shop asks what it should worry about most. What do you tell it?

**Answers**

1. Any two: most attacks are automated and opportunistic, not targeted; many serious attackers are organized groups, not lone geniuses; most break-ins use ordinary weaknesses, not movie wizardry.
2. Because opportunists go after whoever is easy, not a specific victim. If you are harder than the next target, they move on. Updates, strong passwords, and not exposing needless services defeat most of them.
3. Stealing the data before locking it, so the attacker can threaten to publish it. Backups let you restore, but they do not stop the threat to leak the stolen copy.
4. Malicious insiders (abuse access on purpose) and accidental insiders (cause harm by mistake). Accidental is far more common.
5. Advanced: well-funded and highly skilled, sometimes using unknown weaknesses. Persistent: they don't give up, and may hide for months or years. Threat: real intent and capability.
6. Money → cybercriminals/ransomware crews; information → nation-states (or competitors); publicity → hacktivists.
7. Opportunists and ransomware. Basic hygiene, updates, strong unique passwords, MFA, and offline backups, defeats the large majority of what a small shop will face.

## Practice

Think about one organization: your workplace, your school, or a small business you know.

1. List the **three kinds of attacker** it is most likely to face, from this lesson.
2. For each, write the attacker's likely **motive** and **one defense** that would help.
3. Name one **insider** risk it has (malicious or accidental), and one control that would reduce it.

### A Worked Example

For a small online clothing shop:

1. Opportunists; ransomware crews; (occasionally) hacktivists if it became controversial.
2. Opportunists, motive easy gain, defense: keep the website software updated. Ransomware crews, motive money, defense: offline nightly backups and staff training. Hacktivists, motive publicity, defense: protect the public website and social accounts, and be able to withstand a traffic flood.
3. Insider risk: a staff member accidentally emailing the customer list to the wrong person. Control: least privilege (few people can export the full list) plus logging of exports.
