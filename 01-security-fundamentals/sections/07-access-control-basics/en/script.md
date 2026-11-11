# Section 7: Access Control Basics — Video Scripts

Two videos, about 8 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | Authorization, Least Privilege, and Separation of Duties | 1.1–1.5 | about 4.5 min |
| 2 | Models, Roles, and Privilege Creep | 2.1–2.5 | about 4 min |

---

## Video 1 — Authorization, Least Privilege, and Separation of Duties

### 1.1 — Title

**Show:** slide 1.1

**Say:** Last lesson, authentication proved who you are. This lesson is about what you're allowed to do once you're known. We start with three core ideas: the difference between authentication and authorization, least privilege, and separation of duties.

**Time:** about 0:25

### 1.2 — Authentication vs. authorization

**Show:** slide 1.2

**Say:** These two words get confused constantly, so let's pin them down. Authentication answers "who are you?", and it happens once, at the door. Authorization answers "what are you allowed to do?", and it happens on every single action, after you're known. Think of an airport: showing your passport proves who you are, that's authentication. Your boarding pass says which flight and seat you may take, that's authorization. Proving your identity doesn't, by itself, let you board any plane you like. And this matters hugely, because a large share of real breaches come from broken authorization: a user logged in as themselves reaches data or actions they should never have been allowed, often just by changing a number in a web address. Getting authorization right is every bit as important as authentication.

**Time:** about 0:55

### 1.3 — Least privilege

**Show:** slide 1.3

**Say:** The single most important idea in access control is least privilege: give each person, program, and device only the access it needs to do its job, and no more. If a user only needs to read orders, they shouldn't be able to delete customers. Why does it matter so much? First, it limits the damage of any single failure. If a least-privilege account is phished, the attacker gets only that small slice, not the keys to everything, it turns a disaster into an incident. Second, it limits mistakes: you can't accidentally delete what you can't touch. And third, it shrinks the attack surface. A related habit: even an IT administrator should browse the web and read email as an ordinary user, and switch to their powerful account only for the specific task that needs it, so a bad click doesn't happen while they're holding the keys to everything.

**Time:** about 0:55

### 1.4 — Separation of duties

**Show:** slide 1.4

**Say:** The third idea is separation of duties: no single person can complete a sensitive process alone. A critical action is split so it needs two or more people. The classic example is money: the person who requests a payment shouldn't also be the one who approves it. One employee raises the invoice; a different one approves the funds. To commit fraud, you'd now have to corrupt two people, which is far harder and far more likely to be noticed. It pairs naturally with least privilege: least privilege limits how much power one role has, and separation of duties makes sure the most dangerous powers are split across roles.

**Time:** about 0:45

### 1.5 — Recap

**Show:** slide 1.5

**Say:** So: authentication is who you are, authorization is what you may do, checked on every action. Least privilege means only the access needed, which limits damage and mistakes. And separation of duties splits sensitive actions so no one person acts alone. Next, how systems actually decide access, and why access rots over time.

**Time:** about 0:30

---

## Video 2 — Models, Roles, and Privilege Creep

### 2.1 — Title

**Show:** slide 2.1

**Say:** In this video: the standard models for deciding who may do what, how users, groups, and roles organize access, and a slow problem called privilege creep.

**Time:** about 0:20

### 2.2 — The access control models

**Show:** slide 2.2

**Say:** How does a system actually decide who may do what? There are a few standard models, and you should recognize the names. DAC, discretionary access control, means the owner of a resource decides who may use it, like sharing a document and choosing who can view it. MAC, mandatory access control, means a central policy decides based on labels like "Secret", and users can't override it, used in military and high-security systems. RBAC, role-based access control, grants access to roles, and people are given roles, this is how most businesses work. And ABAC, attribute-based access control, decides from attributes and rules, like department, time of day, or device, common in large cloud systems. The two you'll meet most are DAC, for everyday sharing, and RBAC, the backbone of almost every business system. Real systems often blend them.

**Time:** about 0:55

### 2.3 — Users, groups, and roles

**Show:** slide 2.3

**Say:** Managing permissions for each person one by one doesn't scale and quickly becomes a mess, so access is organized in layers. A user is one account, one person or program or device. A group is a bundle of users, so you can grant access to many at once, like "Phnom Penh Store Staff". And a role is a named set of permissions tied to a job, like "Cashier", who can take payments and issue small refunds. The power is that you manage access by job, not by person. You decide once what a cashier may do, then give the cashier role to whoever works the till. When someone changes jobs, you change their role and their access follows. And when a new rule appears, you fix it in one place and everyone with that role is updated. That's RBAC in practice.

**Time:** about 0:55

### 2.4 — Privilege creep

**Show:** slide 2.4

**Say:** Access isn't a one-time decision; it rots over time. Privilege creep is the slow build-up of permissions a person no longer needs. It happens naturally: someone joins sales and gets sales access; they help finance for a month and get finance access; they move to support and get support access, but nobody ever removes the first two. After a few years, a long-serving employee can reach almost everything, which quietly destroys least privilege and makes that one account a huge prize. The fixes are process, not technology. Access reviews, called recertification, regularly check who has access to what and remove what's unused. A joiner-mover-leaver process grants access when someone joins, changes it when they move, and promptly removes all of it when they leave, because a former employee's working login is a classic way in. And time-limited access expires automatically so it can't linger.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** To recap: there are four models, DAC, MAC, RBAC, and ABAC, and DAC and RBAC are the everyday ones. You manage access by role, not per person, so changes happen in one place. And privilege creep rots least privilege over time, so you fix it with regular reviews and a proper leaver process. Access control is where confidentiality and integrity are enforced in daily practice. In the next lesson, we widen out to all the kinds of security control, and how they stack into defense in depth.

**Time:** about 0:30
