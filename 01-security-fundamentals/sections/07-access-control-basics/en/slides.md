---
title: "Security Fundamentals — Section 7: Access Control Basics"
videos:
  1: Authorization, Least Privilege, and Separation of Duties
  2: Models, Roles, and Privilege Creep
---

<!-- 1.1 -->
<!-- layout: title -->

# Access Control Basics

## Video 1 · Authorization, Least Privilege, and Separation of Duties

Security Fundamentals · Section 7

In this video, you will learn:

- Authentication vs. authorization
- The principle of least privilege
- Separation of duties

---

<!-- 1.2 -->

# Authentication vs. authorization

- **Authentication:** "who are you?" Happens once, at the door. (Lesson 6.)
- **Authorization:** "what are you allowed to do?" Happens on **every action**, after you're known.

At an airport: your **passport** proves who you are (authentication); your **boarding pass** says which flight and seat (authorization).

A huge share of breaches are **broken authorization**: a logged-in user reaches data they should never have, often by changing a number in a web address.

---

<!-- 1.3 -->

# Least privilege

**Give each person, program, and device only the access it needs, and no more.**

The single most important idea in access control.

- **Limits damage:** a phished account gains only its small slice, not everything. Turns a disaster into an incident.
- **Limits mistakes:** you can't delete what you can't touch.
- **Shrinks the attack surface.**

Even admins browse and read email as an **ordinary user**, elevating only for the task that needs it.

---

<!-- 1.4 -->

# Separation of duties

**No single person can complete a sensitive process alone.**

- Classic example: the person who **requests** a payment is not the one who **approves** it.
- To commit fraud you'd now have to corrupt two people, much harder and more likely to be noticed.

Pairs with least privilege: least privilege limits one role's power; separation of duties splits the most dangerous powers across roles.

---

<!-- 1.5 -->
<!-- layout: recap -->

# Recap: the core principles

- **Authentication** = who you are; **authorization** = what you may do, checked on every action.
- **Least privilege:** only the access needed; limits damage and mistakes.
- **Separation of duties:** split sensitive actions so no one person acts alone.

**Next video:** the models, roles, and why access rots over time.

---

<!-- 2.1 -->
<!-- layout: title -->

# Access Control Basics

## Video 2 · Models, Roles, and Privilege Creep

Security Fundamentals · Section 7

In this video, you will learn:

- The four access control models
- Users, groups, and roles
- Privilege creep, and how to catch it

---

<!-- 2.2 -->
<!-- layout: table -->

# The access control models

| Model | How access is decided | Seen in |
|---|---|---|
| **DAC** | The **owner** decides who may use it | Sharing a file or document |
| **MAC** | A **central policy** decides from labels | Military, high-security |
| **RBAC** | Access granted to **roles**; people get roles | Most businesses |
| **ABAC** | Decided by **attributes & rules** (dept, time, device) | Large cloud systems |

You'll meet **DAC** (everyday sharing) and **RBAC** (the business backbone) most. Real systems blend them.

---

<!-- 2.3 -->

# Users, groups, and roles

Managing permissions per person doesn't scale. Organize access by **job, not person**.

- **User:** one account (a person, program, or device).
- **Group:** a bundle of users ("Phnom Penh Store Staff").
- **Role:** a named set of permissions for a job ("Cashier" takes payments, issues small refunds).

Decide once what a role may do; assign it to whoever does that job. Change jobs → change role → access follows. This is **RBAC**.

---

<!-- 2.4 -->

# Privilege creep

**The slow build-up of permissions a person no longer needs.**

- Join sales → sales access. Help finance → finance access. Move to support → support access. Nobody removes the old ones.
- After years, one account can reach almost everything, a huge prize for an attacker.

**Fixes (process, not tech):**

- **Access reviews** (recertification): remove what's unused.
- **Joiner-mover-leaver:** grant, change, and *promptly remove* access.
- **Time-limited access** that expires automatically.

---

<!-- 2.5 -->
<!-- layout: recap -->

# Recap: models, roles, creep

- Four models: **DAC, MAC, RBAC, ABAC**; DAC and RBAC are the everyday ones.
- Manage access by **role**, not per person; changes happen in one place.
- **Privilege creep** rots least privilege over time; fix it with reviews and a leaver process.

**Next lesson:** all the kinds of security control, and how they stack into defense in depth.
