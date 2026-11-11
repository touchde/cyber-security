# Section 3: Threats, Vulnerabilities, and Risk — Video Scripts

Three videos, about 11 minutes in total. Slide IDs match [`slides.md`](slides.md). No code demos.

| Video | Title | Slides | Length |
|---|---|---|---|
| 1 | The Three Words, and Where Weakness Comes From | 1.1–1.5 | about 4 min |
| 2 | Measuring Risk | 2.1–2.5 | about 4 min |
| 3 | Treating Risk | 3.1–3.5 | about 3.5 min |

---

## Video 1 — The Three Words, and Where Weakness Comes From

### 1.1 — Title

**Show:** slide 1.1

**Say:** In lesson 1 we used three words loosely: threat, vulnerability, and risk. In this lesson we make them precise, because precision here is the difference between guessing and actually managing security. Let's start with the three words.

**Time:** about 0:25

### 1.2 — The three words, precisely

**Show:** slide 1.2

**Say:** A threat is something bad that could happen, or an actor who could cause it, like a ransomware group. A vulnerability is a weakness that a threat can use, like staff who open attachments without checking. And a risk is the combination: the chance that a threat meets a matching vulnerability, and how bad the result would be, like a ransomware outbreak that stops the business for days. Why be so careful? Because each word points to a different fix. You usually can't remove the threat, criminals exist, but you can often remove the vulnerability, by training staff and filtering email, and you can always try to reduce the risk, by adding a backup so the impact is smaller. Naming the right word tells you where to act.

**Time:** about 0:55

### 1.3 — Where vulnerabilities come from

**Show:** slide 1.3

**Say:** So where do vulnerabilities come from? Everywhere a system is built and used. Software bugs, like a flaw that lets an attacker run commands. Misconfiguration, like a database left open to the internet with no password. Weak design, like a system that trusts whatever the user's app tells it. People, falling for phishing or reusing passwords. Process, where nobody applies updates or reviews who has access. Physical, like an unlocked server room. And third parties, a weakness in a library or supplier you rely on. Notice most of these aren't exotic hacking tricks; they're ordinary gaps. And when a software weakness is published, it gets a public ID called a CVE, so everyone can track and fix the same issue.

**Time:** about 0:55

### 1.4 — Not every threat is a hacker

**Show:** slide 1.4

**Say:** It helps to split a threat into two parts: the source, who or what could cause harm, and the event, the specific thing they do. Threat sources come in four groups. Adversarial: people who mean harm, from lone attackers to criminal groups to nation-states. Accidental: a user who deletes the wrong file. Structural: equipment that fails, a disk that dies. And environmental: fire, flood, power loss. This is a useful reminder that not every threat is a hacker. A flood that destroys your only server breaks availability just as surely as an attacker, and a good risk assessment includes both.

**Time:** about 0:50

### 1.5 — Recap

**Show:** slide 1.5

**Say:** To recap: a threat is the bad event or actor, a vulnerability is the weakness, and a risk is likelihood times impact of the two meeting. Each points to a different fix, and you focus on removing vulnerabilities and reducing risk. And threats aren't only attackers, accidents, failures, and nature count too. Next, how we actually measure risk.

**Time:** about 0:30

---

## Video 2 — Measuring Risk

### 2.1 — Title

**Show:** slide 2.1

**Say:** You can't fix everything at once, so you have to measure risk and rank it. In this video: likelihood and impact, then two ways to rate risk, with bands and with money.

**Time:** about 0:20

### 2.2 — Likelihood and impact

**Show:** slide 2.2

**Say:** Every risk has two dimensions. Likelihood: how probable is it that this happens and succeeds? And impact: if it does happen, how bad is it, measured in money, downtime, harm to people, legal trouble, and reputation? Keep them apart, because they call for different responses. A high-likelihood, low-impact risk, like a mistyped order, you fix cheaply or just accept. A low-likelihood, high-impact risk, like a fire, you handle with insurance and off-site backups even though it's rare. And the high-likelihood, high-impact risks, those you fix first. That's the whole reason for the formula: risk equals likelihood times impact.

**Time:** about 0:55

### 2.3 — Qualitative rating

**Show:** slide 2.3

**Say:** There are two ways to rate risk. The first is qualitative: simple bands, Low, Medium, High, placed on a grid of likelihood against impact. You put each risk in a cell and deal with the High cells first. It's quick, it needs no exact data, and it's good enough for most small organizations. Its weakness is that "High" is a judgement, and two people may disagree about where something sits.

**Time:** about 0:40

### 2.4 — Quantitative rating

**Show:** slide 2.4

**Say:** The second way is quantitative, using real money. You estimate the yearly cost of a risk with three numbers. SLE, single loss expectancy, is the cost of one occurrence, say fifteen hundred dollars for a stolen laptop. ARO, annualized rate of occurrence, is how many times a year you expect it, say two. And ALE, annualized loss expectancy, is SLE times ARO, so three thousand dollars a year. Now you can compare: if a control costs a thousand dollars a year and halves the loss, it saves fifteen hundred for a thousand, so it's worth doing. This is powerful for big decisions, but remember the numbers are only estimates, so don't mistake the precision for certainty.

**Time:** about 0:55

### 2.5 — Recap

**Show:** slide 2.5

**Say:** So, keep likelihood and impact apart, and risk is the two multiplied. Qualitative rating with Low, Medium, High sorts things quickly; quantitative rating with SLE, ARO, and ALE guides the big money decisions. Most real work mixes both. Next, once you've ranked a risk, what do you actually do about it?

**Time:** about 0:30

---

## Video 3 — Treating Risk

### 3.1 — Title

**Show:** slide 3.1

**Say:** You've found and ranked your risks. Now you treat them. In this video: the four ways to treat a risk, the idea of residual risk, and how to write a simple risk register.

**Time:** about 0:20

### 3.2 — The four ways to treat a risk

**Show:** slide 3.2

**Say:** There are only four options. Reduce, also called mitigate: add controls to lower the likelihood or the impact, like training staff and filtering email. Transfer: make it someone else's cost, usually with insurance. Avoid: stop doing the risky thing, for example by letting a payment provider store card numbers so you never hold them. And accept: decide the risk is small enough to live with. Two notes. Accepting is a real, legitimate choice, but it has to be a decision made by someone with authority, not just ignoring the risk. And you often combine treatments: reduce with controls, transfer what remains with insurance, accept the small part left.

**Time:** about 0:55

### 3.3 — Residual risk

**Show:** slide 3.3

**Say:** No treatment removes a risk completely. What's left after your controls is called residual risk. Say phishing is a High risk. You add training, an email filter, and multi-factor authentication. The likelihood drops a lot, but not to zero, someone may still click, and a filter may still miss a clever message. That remaining chance is the residual risk, and the organization's leaders decide, explicitly, whether it's acceptable. If it is, they accept it; if not, they add more controls. This is exactly why security is never "finished".

**Time:** about 0:45

### 3.4 — A simple risk register

**Show:** slide 3.4

**Say:** Finally, organizations keep their risks in a risk register: a simple table listing each risk, its rating, its treatment, and who owns it. Even a one-page register, kept up to date, puts a small business ahead of most. Ransomware via phishing: High, reduce with training, a filter, and offline backups, owned by the manager. Laptop lost or stolen: Medium, reduce with encryption and transfer with insurance, owned by IT. And so on. The register turns a vague worry, "are we secure?", into a short list of specific decisions, each owned by a real person.

**Time:** about 0:50

### 3.5 — Recap

**Show:** slide 3.5

**Say:** To recap the lesson: there are four treatments, reduce, transfer, avoid, and accept, often combined. Residual risk always remains and must be accepted on purpose. And a risk register turns the big vague question into a short list of owned decisions. That's risk management: not removing every risk, which is impossible, but seeing them clearly and deciding what to do about each. Next lesson, we look more closely at the attackers themselves: who attacks, and why.

**Time:** about 0:35
