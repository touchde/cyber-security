# Cyber Security Learning Materials

This repository is a collection of learning outlines and draft teaching content for cyber security, from the fundamentals to attack, defense, and specialist fields. It is planned as material for books, slides, and videos in English and Khmer, in the same format as the mobile-development repository.

## Ethics First

Every attack in these courses is tried **only on systems you own, or have written permission to test**: our own example code and the home lab built in the Home Lab course. Every key, password, and token in the examples is made up. Each lesson that shows an attack says this clearly. The dark web course explains how those networks and markets work, and how defenders monitor them; it never shows how to buy, sell, or hide illegal things.

## How Each Topic Is Organized

Every topic folder follows the same layout. A topic grows into it as work progresses.

```text
01-security-fundamentals/
├── README.md             ← what the topic covers, status, and lesson links
├── planning/             ← outline, section-plan, production-plan, tasks,
│                           lesson-brief, storyline, slide-design, sources
└── sections/             ← one folder per lesson
    └── 01-what-cybersecurity-is/
        ├── examples/     ← runnable code and lab files (private to the teacher)
        ├── en/           ← book.md, slides.md, script.md
        └── km/           ← the same three files in Khmer
```

## Learning Order

Everyone takes **Foundations** first, in order. Then pick a path: Offensive, Defensive, or Engineering. The Specialized courses can be taken after any path, and the Capstone comes last. A full security professional eventually takes all of them.

| Path | Courses, in order |
|---|---|
| Foundations (everyone) | [Security Fundamentals](01-security-fundamentals/) → [How Computers Work](02-computer-fundamentals/) → [Linux for Security](03-linux/) → [Networking for Security](04-networking/) → [Windows and Active Directory Fundamentals](05-windows-active-directory/) → [Scripting With Bash and PowerShell](06-scripting-bash-powershell/) → [Python for Security](07-python-for-security/) → [Building a Home Lab](08-home-lab/) → [Applied Cryptography](09-cryptography/) |
| Offensive (red team) | [OSINT: Open-Source Intelligence](10-osint/) → [Web Application Security](11-web-application-security/) → [Mobile App Penetration Testing](12-mobile-app-pentesting/) → [Network Penetration Testing](13-network-penetration-testing/) → [Active Directory Attack and Defense](14-active-directory-security/) → [Wireless and Radio Security](15-wireless-security/) → [Social Engineering and Physical Security](16-social-engineering/) → [Reverse Engineering](17-reverse-engineering/) → [Binary Exploitation](18-binary-exploitation/) → [Advanced Exploitation and Vulnerability Research](19-advanced-exploitation/) → [IoT and Hardware Hacking](20-iot-hardware-security/) → [Red Teaming and Adversary Emulation](21-red-teaming/) |
| Defensive (blue team) | [Network Defense and Security Architecture](22-network-defense/) → [Endpoint and System Hardening](23-endpoint-hardening/) → [Vulnerability Management](24-vulnerability-management/) → [Security Operations (SOC)](25-security-operations/) → [Detection Engineering and Threat Hunting](26-detection-engineering/) → [Incident Response](27-incident-response/) → [Digital Forensics](28-digital-forensics/) → [Malware Analysis](29-malware-analysis/) → [Cyber Threat Intelligence](30-threat-intelligence/) → [Anonymity, Privacy, and the Dark Web](31-dark-web/) |
| Engineering | [Secure Development and DevSecOps](32-secure-development/) → [Data Security and Backups](33-data-security/) → [Cloud Security](34-cloud-security/) → [Container and Kubernetes Security](35-container-security/) → [Identity and Access Management](36-identity-access-management/) |
| Specialized and career | [OT and Industrial Control System Security](37-ot-ics-security/) → [Fraud and Banking Security](38-fraud-banking-security/) → [Blockchain and Smart Contract Security](39-blockchain-security/) → [AI Security](40-ai-security/) → [Governance, Risk, and Compliance](41-governance-risk-compliance/) → [Security Careers and Certifications](42-career-certifications/) → [Capstone and CTF Practice](43-capstone-ctf/) |

The developer side of mobile security is in the mobile-development repository (course 14). This repository's Mobile App Penetration Testing course is the tester's side.

## Progress

| Topic | Path | Lessons (draft) | Outline | Written |
|---|---|---:|:---:|:---:|
| [01. Security Fundamentals](01-security-fundamentals/) | Foundations | 12 | ✅ | ✅ All 12, en |
| [02. How Computers Work](02-computer-fundamentals/) | Foundations | 12 | ⬜ | ⬜ |
| [03. Linux for Security](03-linux/) | Foundations | 13 | ⬜ | ⬜ |
| [04. Networking for Security](04-networking/) | Foundations | 15 | ⬜ | ⬜ |
| [05. Windows and Active Directory Fundamentals](05-windows-active-directory/) | Foundations | 12 | ⬜ | ⬜ |
| [06. Scripting With Bash and PowerShell](06-scripting-bash-powershell/) | Foundations | 11 | ⬜ | ⬜ |
| [07. Python for Security](07-python-for-security/) | Foundations | 14 | ⬜ | ⬜ |
| [08. Building a Home Lab](08-home-lab/) | Foundations | 10 | ⬜ | ⬜ |
| [09. Applied Cryptography](09-cryptography/) | Foundations | 15 | ⬜ | ⬜ |
| [10. OSINT: Open-Source Intelligence](10-osint/) | Offensive | 14 | ⬜ | ⬜ |
| [11. Web Application Security](11-web-application-security/) | Offensive | 22 | ⬜ | ⬜ |
| [12. Mobile App Penetration Testing](12-mobile-app-pentesting/) | Offensive | 14 | ⬜ | ⬜ |
| [13. Network Penetration Testing](13-network-penetration-testing/) | Offensive | 13 | ⬜ | ⬜ |
| [14. Active Directory Attack and Defense](14-active-directory-security/) | Offensive | 14 | ⬜ | ⬜ |
| [15. Wireless and Radio Security](15-wireless-security/) | Offensive | 13 | ⬜ | ⬜ |
| [16. Social Engineering and Physical Security](16-social-engineering/) | Offensive | 13 | ⬜ | ⬜ |
| [17. Reverse Engineering](17-reverse-engineering/) | Offensive | 14 | ⬜ | ⬜ |
| [18. Binary Exploitation](18-binary-exploitation/) | Offensive | 14 | ⬜ | ⬜ |
| [19. Advanced Exploitation and Vulnerability Research](19-advanced-exploitation/) | Offensive | 12 | ⬜ | ⬜ |
| [20. IoT and Hardware Hacking](20-iot-hardware-security/) | Offensive | 13 | ⬜ | ⬜ |
| [21. Red Teaming and Adversary Emulation](21-red-teaming/) | Offensive | 13 | ⬜ | ⬜ |
| [22. Network Defense and Security Architecture](22-network-defense/) | Defensive | 13 | ⬜ | ⬜ |
| [23. Endpoint and System Hardening](23-endpoint-hardening/) | Defensive | 12 | ⬜ | ⬜ |
| [24. Vulnerability Management](24-vulnerability-management/) | Defensive | 11 | ⬜ | ⬜ |
| [25. Security Operations (SOC)](25-security-operations/) | Defensive | 13 | ⬜ | ⬜ |
| [26. Detection Engineering and Threat Hunting](26-detection-engineering/) | Defensive | 12 | ⬜ | ⬜ |
| [27. Incident Response](27-incident-response/) | Defensive | 12 | ⬜ | ⬜ |
| [28. Digital Forensics](28-digital-forensics/) | Defensive | 14 | ⬜ | ⬜ |
| [29. Malware Analysis](29-malware-analysis/) | Defensive | 12 | ⬜ | ⬜ |
| [30. Cyber Threat Intelligence](30-threat-intelligence/) | Defensive | 10 | ⬜ | ⬜ |
| [31. Anonymity, Privacy, and the Dark Web](31-dark-web/) | Defensive | 14 | ⬜ | ⬜ |
| [32. Secure Development and DevSecOps](32-secure-development/) | Engineering | 15 | ⬜ | ⬜ |
| [33. Data Security and Backups](33-data-security/) | Engineering | 11 | ⬜ | ⬜ |
| [34. Cloud Security](34-cloud-security/) | Engineering | 13 | ⬜ | ⬜ |
| [35. Container and Kubernetes Security](35-container-security/) | Engineering | 13 | ⬜ | ⬜ |
| [36. Identity and Access Management](36-identity-access-management/) | Engineering | 10 | ⬜ | ⬜ |
| [37. OT and Industrial Control System Security](37-ot-ics-security/) | Specialized and Career | 11 | ⬜ | ⬜ |
| [38. Fraud and Banking Security](38-fraud-banking-security/) | Specialized and Career | 12 | ⬜ | ⬜ |
| [39. Blockchain and Smart Contract Security](39-blockchain-security/) | Specialized and Career | 11 | ⬜ | ⬜ |
| [40. AI Security](40-ai-security/) | Specialized and Career | 11 | ⬜ | ⬜ |
| [41. Governance, Risk, and Compliance](41-governance-risk-compliance/) | Specialized and Career | 11 | ⬜ | ⬜ |
| [42. Security Careers and Certifications](42-career-certifications/) | Specialized and Career | 10 | ⬜ | ⬜ |
| [43. Capstone and CTF Practice](43-capstone-ctf/) | Specialized and Career | 10 | ⬜ | ⬜ |
| **Total: 43 courses** | | **544** | | |

## Current Work

- **Done on 2026-11-11:** the full course list and a draft lesson list for every course; the shared `STYLE-GUIDE.md` (adapted, no-storyline) and a seed `GLOSSARY.md`; the `tools/` and `assets/` build system brought over from mobile-development; **course 01 (Security Fundamentals) fully planned, all 12 lessons written in English, and built to PDF** (lesson books + slides + a 104-page full book, in `output/01-security-fundamentals/`)
- **Next:** your review of course 01's 12 English lessons; then optional diagrams and the Khmer versions; then course 02
