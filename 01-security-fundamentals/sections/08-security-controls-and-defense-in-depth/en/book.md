# Section 8: Security Controls and Defense in Depth

> Covers chapter 8 in the [outline](../../../planning/outline.md).

## What You Will Learn

- What a security control is.
- Control types by function: preventive, detective, and corrective.
- Control categories by nature: technical, administrative, and physical.
- Defense in depth, explained properly.
- How controls combine into layers for a real system.
- Where controls fail, and why no single one is enough.
- The trade-off between security and usability.

## Before You Start

Read lessons 1 to 7. Lesson 1 introduced defense in depth; this lesson gives it structure, and organizes the many controls mentioned so far (backups, training, MFA, least privilege, logging) into a system you can reason about. No programming is needed.

---

## 1. What a Control Is

A **security control** is any measure you put in place to reduce risk. That is the whole definition: a control is a counter to a threat or a vulnerability. Everything you have met that protects a system is a control: a password, a backup, a locked door, a staff training session, an antivirus program, a log, a rule that says "two people must approve a payment".

Controls are how risk treatment (lesson 3) actually happens. When you decide to *reduce* a risk, you do it by adding controls. The art of security is choosing the right controls, enough to bring the risk down to an acceptable level, without spending more than the risk is worth or making the system unusable.

To choose well, it helps to classify controls in two ways: by **what they do** (their function), and by **what they are** (their nature). The next two topics cover each.

## 2. Control Types: Preventive, Detective, Corrective

Classified by **function**, when they act relative to an incident, controls fall into three main types:

| Type | When it acts | What it does | Examples |
|---|---|---|---|
| **Preventive** | Before | Stops an incident from happening | Passwords, MFA, locks, firewalls, training, least privilege |
| **Detective** | During / after | Notices that something happened | Logs, alarms, CCTV, monitoring, intrusion detection |
| **Corrective** | After | Fixes the damage and restores normal | Backups and restore, patching, rebuilding a server, an incident response plan |

A healthy security program needs all three. Preventive controls alone are not enough, because some attacks will get through; without **detective** controls you will not even know. And detection is useless if you cannot recover, which is what **corrective** controls do.

You will also hear of a few supporting types: **deterrent** controls discourage an attacker (a visible camera, a warning sign); **compensating** controls are an alternative when the ideal control is not possible (extra monitoring when you cannot yet patch a system). But the core three, prevent, detect, correct, are the ones to remember, and they map neatly onto the stages of an incident: stop it, spot it, fix it.

## 3. Control Categories: Technical, Administrative, Physical

Classified by **nature**, what the control actually *is*, there are three categories:

| Category | What it is | Examples |
|---|---|---|
| **Technical** (logical) | Built into technology | Passwords, encryption, firewalls, MFA, access control, logging |
| **Administrative** (managerial) | Rules, processes, and people | Policies, training, access reviews, separation of duties, hiring checks |
| **Physical** | Things in the real world | Locks, doors, guards, cameras, a safe, a disconnected backup drive |

This categorization carries a crucial lesson: **security is not only technology.** Many people think of security as firewalls and encryption, the technical controls. But administrative controls, the rules and habits, and physical controls, the locks and doors, are just as important. The ransomware in lesson 1 got in past all the technology because of a missing administrative control: training. A server with perfect software security is still lost if someone can walk out with the physical machine.

The two classifications combine. A single control has both a type and a category: a backup is a *corrective, technical* control; staff training is a *preventive, administrative* control; a security camera is a *detective* (and *deterrent*) *physical* control. Thinking in this grid helps you spot gaps, for example, plenty of preventive controls but nothing to detect what gets past them.

## 4. Defense in Depth, Properly

**Defense in depth means using multiple layers of controls, so that if one fails, others still protect the asset.** It is sometimes called a layered defense, or the "castle" approach: a moat, then walls, then a locked keep, so breaching one barrier is not enough.

The reasoning behind it is simple and powerful: **every single control can fail.** A password gets phished. A patch is missed. A firewall is misconfigured. A guard is distracted. If your security depends on one control, then the day that control fails, you are fully exposed. With layers, one failure is absorbed by the next.

Good defense in depth deliberately mixes:

- **Types:** preventive controls to stop attacks, detective controls to catch what gets through, corrective controls to recover. (Assume prevention will sometimes fail, and plan to detect and recover.)
- **Categories:** technical, administrative, and physical, so a weakness in one area is covered by another.

Recall the attack lifecycle from lesson 5: the attacker must succeed at every stage, while the defender only has to break the chain once. Defense in depth is how you give yourself many chances to break it. It is the single most important design idea in practical security, and it is why the rest of this program teaches many controls rather than one magic solution.

## 5. Layered Defense: A Worked Example

Here is defense in depth for one concrete asset: a small business's customer database. Watch how the layers mix types and categories.

| Layer | Control | Type | Category |
|---|---|---|---|
| 1 | Staff trained to spot phishing | Preventive | Administrative |
| 2 | Email filtering | Preventive | Technical |
| 3 | MFA on all accounts | Preventive | Technical |
| 4 | Least privilege: few can read the whole database | Preventive | Technical/Admin |
| 5 | The database is encrypted | Preventive | Technical |
| 6 | Logging and alerts on large data exports | Detective | Technical |
| 7 | Locked server room / secured cloud account | Preventive | Physical |
| 8 | Nightly offline backups | Corrective | Technical |
| 9 | An incident response plan | Corrective | Administrative |

No single layer is perfect, and that is the point. If an attacker phishes a password (beating layer 1), MFA (layer 3) still blocks them. If they get an account anyway, least privilege (layer 4) limits what they reach, and the export alert (layer 6) catches them. If the worst happens, backups (layer 8) and the response plan (layer 9) let the business recover. An attacker now has to defeat *many* controls of *different kinds*, which is dramatically harder than beating any one.

## 6. Where Controls Fail

Controls are not magic, and understanding how they fail keeps you honest:

- **Misconfiguration:** a control that is present but set up wrong, an "open" firewall, a backup that was never actually tested. This is one of the most common real-world failures.
- **Human bypass:** people work around controls that get in their way, propping a door open, sharing a password, clicking past a warning. A control nobody follows is no control.
- **Decay over time:** patches stop being applied, access reviews lapse, a backup drive quietly fails. Controls need maintenance.
- **Unknown weaknesses:** a brand-new attack (a zero-day) that no existing control anticipated.

Two habits address these. First, **test your controls**: a backup you have never restored from is a hope, not a control; a plan you have never rehearsed will not work under pressure. Second, lean again on **defense in depth**: because any one control can fail silently, you never rely on one. The assumption behind mature security is not "this will not fail" but "when this fails, what catches it?"

## 7. Security vs. Usability

Every control has a cost, in money, in effort, and above all in **usability**. Push security too hard and you get a system so annoying that people route around it, which makes it *less* secure, not more. Force password changes every 30 days and people pick "Summer2026!", then "Summer2026!!". Lock screens after 30 seconds and people disable them. The most secure-looking control can backfire if it ignores how people actually work.

So the goal is not maximum security; it is **appropriate** security, the right controls for the risk, applied in a way people can live with. This echoes two earlier ideas: security is about **risk, not perfection** (lesson 1), and the goals **trade off** against each other and against usability (lesson 2). A good security program:

- Puts the strongest controls where the risk is highest, and keeps friction low elsewhere.
- Prefers controls that are easy to live with (a password manager, passkeys, single sign-on) over ones that fight the user.
- Measures whether controls are actually followed, not just whether they exist on paper.

That balance, strong where it matters, usable everywhere, is the mark of security done well. It is also where the technical side meets the human side, which is why the next lessons turn to the rules, frameworks, and people that hold a security program together, starting with ethics and the law.

---

## Common Mistakes

**1. Thinking security is only technology.** Administrative controls (training, policy, reviews) and physical controls (locks, doors) matter as much as technical ones. The biggest gaps are often non-technical.

**2. Relying only on prevention.** Some attacks get through. Without detective controls you won't know, and without corrective controls you can't recover. You need all three types.

**3. Depending on a single control.** Every control can fail. One failure should never mean full exposure. Layer them.

**4. Never testing controls.** An untested backup or an unrehearsed plan is a hope, not a control. Test restores and rehearse responses.

**5. Letting controls decay.** Patching lapses, reviews stop, drives fail. Controls need ongoing maintenance.

**6. Over-tightening until people route around it.** A control nobody follows is no control. Match the friction to the risk, and prefer usable controls.

## Summary

| Term | Remember |
|---|---|
| Control | Any measure that reduces risk |
| Types (function) | Preventive (before), detective (during/after), corrective (after) |
| Categories (nature) | Technical, administrative, physical |
| Defense in depth | Multiple layers, so one failure is not full exposure |
| Mix the layers | Different types and categories, so a gap in one is covered by another |
| How controls fail | Misconfiguration, human bypass, decay, unknown attacks |
| Security vs. usability | Aim for appropriate, usable security, not maximum |

## Check Your Understanding

1. What is a security control, in one sentence?
2. Name the three control types by function, and say when each acts.
3. Name the three control categories by nature, with an example of each.
4. A nightly offline backup, which type and which category is it?
5. State the core idea and the core reason behind defense in depth.
6. Give two different ways a control can fail.
7. Why can too much security make a system less secure?

**Answers**

1. A security control is any measure you put in place to reduce risk.
2. Preventive (acts before an incident, to stop it), detective (acts during or after, to notice it), and corrective (acts after, to fix the damage and recover).
3. Technical (built into technology, e.g. encryption), administrative (rules and processes, e.g. training), physical (real-world, e.g. a locked door).
4. A corrective control (it helps you recover after an incident) and a technical control.
5. Idea: use multiple layers of controls so that if one fails, others still protect the asset. Reason: every single control can fail, so relying on one means full exposure the day it does.
6. Any two: misconfiguration (present but set up wrong), human bypass (people work around it), decay over time (maintenance lapses), or an unknown new attack.
7. Because controls that are too annoying make people route around them (weak predictable passwords, disabled lock screens), which leaves the system less secure than a usable control would.

## Practice

Choose one asset you care about: your laptop, your phone, a small business's customer list, or a website.

1. List **four controls** protecting it (or that should), and label each by **type** (preventive / detective / corrective) and **category** (technical / administrative / physical).
2. Check your list for gaps: do you have at least one **detective** control and one **corrective** control, not only preventive ones?
3. Pick one control you listed and say how you would **test** that it actually works.

### A Worked Example

For a laptop with important files:

1. Controls: a login password (preventive, technical); disk encryption (preventive, technical); keeping it in a locked drawer when out (preventive, physical); an automatic cloud backup (corrective, technical).
2. Gap check: plenty of prevention and a corrective backup, but no detective control. I'd add "find my device" / login alerts to notice theft or unusual sign-ins.
3. Testing the backup: restore a few files onto a different machine to confirm the backup is real and complete, not just that it "runs".
