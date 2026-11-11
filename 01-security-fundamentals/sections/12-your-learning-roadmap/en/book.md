# Section 12: Your Learning Roadmap

> Covers chapter 12 in the [outline](../../../planning/outline.md).

## What You Will Learn

- How this whole program is organized, and why.
- The Foundations, and why everyone does them first.
- How to choose a path once Foundations are done.
- How to build real skill in a home lab.
- How to practise with CTFs and challenges.
- How to build a portfolio that gets you hired.
- How to stay current, and stay safe and ethical, for the long run.
- Your concrete next step.

## Before You Start

Read lessons 1 to 11. This is the final lesson of Security Fundamentals. It does not add new security theory; it turns everything you have learned into a practical plan for the months and years ahead. No programming is needed.

---

## 1. How This Program Is Organized

The program is built as a path from knowing nothing to being ready for professional work. It has five stages, in a deliberate order:

| Stage | Courses | Purpose |
|---|---|---|
| **Foundations** | Security basics, how computers work, Linux, networking, Windows, scripting, Python, a home lab, cryptography | The ground every security person stands on |
| **Offensive** | Web, mobile, network, wireless, reverse engineering, exploitation, red teaming | How attacks really work, hands-on |
| **Defensive** | Security operations, incident response, forensics, malware analysis, threat intelligence, the dark web | How to watch, catch, and recover |
| **Engineering** | Secure development, cloud, containers, identity | How to build systems that resist attack |
| **Specialized** | Industrial systems, fraud and banking, blockchain, AI security, GRC, careers, and a final capstone | Deep fields, and turning skills into a job |

The order is not arbitrary. Each stage depends on the ones before it. You cannot meaningfully attack or defend a network you do not understand, and you cannot understand a network without the Foundations. So the single most important rule of the roadmap is: **do the Foundations first, in order, and do not rush them.**

## 2. The Foundations, and Why They Come First

It is tempting to jump straight to the exciting courses, "I want to hack things now". Resist it. Almost everyone who struggles later skipped or skimmed the Foundations, and almost everyone who progresses smoothly built them solidly.

Here is why each Foundation matters:

- **How Computers Work:** you cannot analyze what a program does if you do not know what a program *is*.
- **Linux:** the command line is the native environment of security tools; you will live in it.
- **Networking:** almost every attack and defense involves the network; this is the language of the field.
- **Windows and Active Directory:** most organizations run on Windows; most attacks target it.
- **Scripting and Python:** automation turns slow manual work into fast, repeatable work, and lets you build your own tools.
- **The Home Lab:** your safe, legal place to practise everything (topic 4).
- **Cryptography:** the math behind passwords, HTTPS, and signatures, understood, not memorized.

Think of the Foundations as learning the alphabet and grammar before writing essays. They are less flashy, but they are what separate someone who truly understands security from someone who can only follow recipes. Give them the time they deserve.

## 3. Choosing a Path

Once the Foundations are solid, you specialize. The three main paths match the role families from lesson 11:

- **Offensive**, if you love figuring out how things break, puzzles, and the attacker's mindset.
- **Defensive**, if you like watching, investigating, noticing patterns, and staying calm under pressure. This path has the most jobs and is a common, reliable way in.
- **Engineering**, if you like building, automating, and designing systems well, often a great fit if you come from development.

You do not have to choose forever, or choose only one. A sensible approach is to do the path that excites you most first, then broaden. Understanding more than one side makes you more valuable: defenders who understand attacks catch more; builders who understand both build better. The **Specialized** courses (fraud, cloud, AI, industrial systems, GRC) layer on top once you have a path, and often follow the local job market, in Cambodia, for instance, fraud and banking security and cloud are in strong demand.

How to decide: if unsure, start **Defensive**. It has the broadest job market, teaches you to think about attacks from the receiving end, and gives a strong base to pivot from later.

## 4. Building Skills in the Home Lab

**You cannot learn security by reading alone.** Reading about lock-picking does not make you a locksmith. The single most important study habit in this whole field is **hands-on practice in a safe, legal environment**, and that environment is your home lab (built in the Home Lab course).

A home lab is a set of virtual machines on your own computer: an attacker machine, some deliberately vulnerable targets, and a small network, all isolated from the real world and from systems you do not own. In it, the ethics rule is satisfied by design: everything belongs to you, so you can attack and defend freely and legally.

How to use it well:

- **Do, don't just watch.** For every technique you learn, perform it yourself in the lab.
- **Break things and fix them.** Attack a target, then defend it. Watching both sides teaches far more than either alone.
- **Take notes as you go.** Your notes become your portfolio (topic 6) and your memory.
- **Reset and repeat.** Snapshots let you return to a clean state and try again.

Every hands-on course in this program assumes you are practising in your lab, not just reading. Build it early, and use it constantly.

## 5. Practising: CTFs and Challenges

Beyond your own lab, the security community runs a huge amount of free, legal practice, and it is one of the best ways to sharpen skills and have fun doing it.

- **CTFs (Capture The Flag)** are security competitions where you solve challenges, finding a hidden "flag" by exploiting a weakness, in categories like web, cryptography, forensics, reverse engineering, and binary exploitation. They range from beginner-friendly to very hard. The final course of this program is devoted to them.
- **Practice platforms** host deliberately vulnerable machines and guided challenges you can work through at your own pace, legally, because they exist for exactly this purpose.
- **Wargames and labs** teach specific skills step by step.

Why practise this way: it is legal (the targets are made for it), it is graded (you know when you succeed), it builds real problem-solving stamina, and it connects you to a community. Doing challenges regularly, even 30 minutes a few times a week, compounds into serious skill over months. It also gives you concrete things to write about, which brings us to the portfolio.

## 6. Building a Portfolio

Remember from lesson 11: **skills and a portfolio get you hired.** A portfolio is simply evidence of what you can do, and you can start building it now, long before your first job. It matters especially when you lack formal experience, because it proves ability directly.

Good portfolio pieces:

- **Write-ups:** clear explanations of how you solved a CTF challenge or a lab, what the weakness was, how you found it, and how to fix it. Write-ups show both skill *and* communication, which employers prize.
- **A blog or notes site:** a simple place to publish what you learn. Teaching something proves you understand it.
- **Projects on a code-sharing site:** small security tools or scripts you have written (the Python and scripting courses produce these).
- **Documented lab work:** your home-lab setups and experiments.
- **Bug bounty or responsible-disclosure results**, once you are ready and strictly within the rules (lesson 9).

Two tips. Keep it **honest** (never claim work you did not do; integrity is everything in this field, lesson 9) and keep it **clear** (a well-explained simple project beats a vague complex one). Start a write-up habit with your very next challenge or lab.

## 7. Staying Current, and Staying Safe

Security never stands still; new attacks, tools, and defenses appear constantly. Staying effective is a career-long habit, not a one-time achievement. Ways to keep up:

- **Follow reputable sources:** security news, vendor and government advisories (like CISA), and respected practitioners.
- **Join communities:** local security groups, online forums, and chats. The field is unusually generous with knowledge, and in Cambodia a growing local community and remote communities both help.
- **Keep practising:** ongoing CTFs and lab work keep your skills sharp.
- **Keep learning deliberately:** the later courses, and new topics as they emerge, like AI security.

And, threaded through all of it, **stay safe and ethical** (lesson 9). As your skills grow, so does your power to cause harm, and the temptation to "just try" something you are not authorized to touch. The professionals who have long, respected careers are the ones who never cross that line. Your reputation for integrity is the most valuable thing you will build, and the easiest to destroy. Guard it from day one.

## 8. Your Next Step

You have finished Security Fundamentals. You now understand what security is, how attacks and defenses work, how to think about risk, the rules that keep your skills legal, the frameworks that organize the work, and the roles you could grow into. That is a real foundation, and more than many working people in the field started with.

Your next step is simple and concrete:

1. **Begin the next Foundation course**, How Computers Work, and continue the Foundations in order. Do not skip ahead, however tempting.
2. **Plan to build your home lab** as soon as that course arrives, so you have somewhere to practise.
3. **Start a write-up habit:** keep notes on everything you learn, from this lesson onward.
4. **Decide, loosely, which path calls to you** (offensive, defensive, engineering), knowing you can change your mind.

Security is a field where curiosity, persistence, and integrity matter more than raw talent, and where demand far exceeds supply. If you keep going, practise hands-on, build a portfolio, and never cross the ethical line, you can go a very long way. You have taken the first step. Keep going, and welcome to the field.

---

## Common Mistakes

**1. Rushing or skipping the Foundations.** Almost everyone who struggles later skimmed the basics. Build them solidly and in order; they are what separate real understanding from recipe-following.

**2. Learning by reading alone.** You cannot learn security without doing it. Practise everything hands-on in your home lab.

**3. Waiting for a job to start a portfolio.** Build evidence now, write-ups, projects, documented lab work. It proves ability before you have experience.

**4. Thinking you must master everything before specializing.** Do the Foundations, then pick the path that excites you. You can broaden later.

**5. Practising on systems you do not own.** Use your home lab and legal practice platforms. The ethics rule does not pause while you learn.

**6. Treating learning as a one-time event.** Security changes constantly. Staying current and staying ethical are career-long habits.

## Summary

| Idea | Remember |
|---|---|
| Program order | Foundations → a path (Offensive/Defensive/Engineering) → Specialized |
| Foundations first | Do them in order, don't rush; they are the real base |
| Choosing a path | Pick what excites you; if unsure, start Defensive; broaden later |
| Home lab | Your safe, legal place to practise; do, don't just watch |
| CTFs and challenges | Free, legal, graded practice that compounds into skill |
| Portfolio | Write-ups and projects prove ability and get you hired; keep it honest |
| Stay current and safe | Keep learning; never cross the ethical line |

## Check Your Understanding

1. What are the five stages of the program, in order?
2. Why must the Foundations come first, and what is the risk of rushing them?
3. If you are unsure which path to choose, which is suggested, and why?
4. Why can't you learn security by reading alone, and what is the main place to practise?
5. What makes CTFs and practice platforms a legal and effective way to practise?
6. Name two good portfolio pieces, and say why write-ups are especially valued.
7. Why does staying ethical get *harder*, and more important, as your skills grow?

**Answers**

1. Foundations, Offensive, Defensive, Engineering, and Specialized (including careers and the capstone).
2. Because each stage depends on the ones before it; you can't attack or defend what you don't understand. Rushing them is the most common cause of struggling later.
3. Defensive, because it has the broadest job market, teaches you to think about attacks from the receiving end, and gives a strong base to pivot from.
4. Because skill comes from doing, not just knowing, like a locksmith who must practise, not only read. The main place to practise is your own home lab.
5. The targets are built deliberately for practice, so using them is legal; the challenges are graded so you know when you succeed; and they build real problem-solving skill.
6. Any two: write-ups, a blog/notes site, security tools/scripts, documented lab work, responsible bug-bounty results. Write-ups are prized because they show both technical skill and clear communication.
7. Because greater skill means greater power to cause harm and more temptation to test things you're not authorized to touch; the professionals with long careers never cross that line, and integrity is the most valuable and most fragile thing you build.

## Practice

This final practice is a plan for yourself.

1. Write your **learning schedule**: realistically, how many hours a week can you give this, and when? (Consistency beats intensity: a steady few hours a week compounds.)
2. Write down the **path** you are leaning toward (offensive, defensive, or engineering) and one sentence on why. It is fine to change later.
3. Commit to a **write-up habit**: decide where you will keep your notes (a document, a blog, a notebook), and write a short one for *this* lesson, what were the three most useful things you learned in Security Fundamentals, and why.

### A Worked Example

1. Schedule: about six hours a week, one hour on weekday evenings and a longer session on Saturday morning.
2. Leaning Defensive, because I like investigating and noticing patterns, and it has the broadest job market to start in.
3. Write-ups: a simple blog. First entry, three most useful things from this course: the three questions (read/change/stop), because they frame every problem; "never trust the client / least privilege", because it reshapes how I see systems; and the one ethics rule, because it's the line my whole future career depends on.
