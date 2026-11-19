---
id: "39d66ad7485bbfcb"
title: "How AI Is Making Software Easier To Reverse Engineer"
url: "https://forbes.com/councils/forbestechcouncil/2026/11/19/how-ai-is-making-software-easier-to-reverse-engineer"
link: "https://forbes.com/councils/forbestechcouncil/2026/11/19/how-ai-is-making-software-easier-to-reverse-engineer"
source: "Forbes"
domain: "forbes.com"
source_type: "mainstream_news"
collector: "rss"
date: "2026-11-19T11:45:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Klaudia Zaika, Forbes Councils Member"]
language: "en"
summary: "AI's impact on reverse engineering is still unfolding, and each new generation of models will likely make software analysis more accessible."
tags: ["Innovation", "/innovation", "technology", "standard"]
orgs: ["Google", "US government"]
topics: ["models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 896
paywalled: false
image: "https://imageio.forbes.com/specials-images/imageserve/6abaa8d3ad97754702a1578e/0x0.jpg?width=960"
discussion_url: null
score: null
comments: null
community: null
---

# How AI Is Making Software Easier To Reverse Engineer

Forbes · Klaudia Zaika, Forbes Councils Member · 2026-11-19

Klaudia Zaika is the CEO of Apriorit, a software development company that provides engineering services globally to tech companies.
AI has already changed the way we build software. At Google, 75% of all new code is now AI-generated and approved by engineers.
The same technology is also changing how software gets taken apart.
My company has been practicing ethical software reversing and helping others protect their products against it for more than 20 years. That’s why I want to talk about how exactly AI is changing reverse engineering, what this means for software companies and which practices can help reduce the new risks.
How AI Changes Software Reverse Engineering
Reverse engineering has always had three core requirements: deep expertise, expensive professional tools and a lot of time. AI has already changed at least two of the three.
The entry barrier is now much lower. A recent legal analysis in the National Law Review highlights that AI lets people with far less skill and time uncover how public-facing products work. I notice this in my company’s projects, too. Now, an open-source decompiler paired with a locally run large language model can handle much of the routine analysis that previously required engaging several experienced professionals and a set of dedicated paid tools.
Speed changes, too, but unevenly. My reverse engineers report AI noticeably accelerating initial research, such as mapping a binary’s structure or identifying what individual functions do. Validation, on the other hand, can now require extra time. This is all because AI can give a confident but wrong verdict about what a piece of code does, so every critical conclusion it offers needs to be double-checked by a competent human.
What AI-Powered Reverse Engineering Means For Software Creators
For companies that build software, the increasing adoption of AI for software reversing works in both directions. On the one hand, in-house security researchers can reverse-engineer their own builds and find weak spots before anyone else does. AI-assisted reverse engineering also helps with legacy systems, reconstructing bits and pieces of knowledge about software with limited or no access to the original documentation and talent.
On the other hand, AI-powered reversing introduces additional security and intellectual property risks. Cheaper, faster analysis can let attackers examine more of a product’s code and the network traffic it exchanges, looking for potential flaws and security gaps to exploit. AI can also help malicious actors reconstruct at least parts of a product’s architecture and core functionality. This, in turn, may give your unethical competitors a shortcut to building something similar with significantly lower costs and effort.
Legal experts, as cited above, also note that AI makes it easier to infer proprietary processes from public-facing products, which puts confidential know-how at greater risk.
How To Protect Your Product From AI-Powered Reverse Engineering
From what I’ve seen so far in our reverse-engineering projects, there are several practices that can make extracting valuable data from and about your product much harder and more expensive, even for AI.
Obfuscate Critical Code
It’s true that heavy obfuscation slows applications down. There are also early signs that AI tools may find ways around it, so applying obfuscation across an entire codebase never pays off.
Instead, have your team obfuscate only the most critical code and be deliberate about what gets this extra layer of protection and what doesn’t. But remember that obfuscation should never be your primary security mechanism, as its main goal is to extend time and increase costs of the analysis for attackers.
Generally, your approach should follow Kerckhoffs’ principle from cryptography: A system should remain secure even when everything about it except the key is public. This means that even if attackers can investigate and understand how your security controls work, these controls must still remain effective.
Keep Secrets Out Of What You Distribute
Anything distributed to users can be analyzed, so core algorithms and sensitive operations are better kept on the server side. Client applications can then work with short-lived tokens instead of long-lived credentials, which limits the damage if a token gets extracted.
This approach has its limits, though: Drivers, embedded software, on-premises products and applications that must work offline often can’t move their logic to a backend. For these cases, you’ll need the following measure.
Encrypt What Has To Stay On The Client
Any sensitive information that must remain on the client should be protected with secure key management practices and advanced cryptography. In particular, always make sure to follow the cryptographic standards and guidelines from NIST.
Hardware-backed protections should also be applied where possible.
Reverse Engineer Your Own Builds Before Someone Else Does
Regular penetration testing and exposure checks can show what a product reveals and which of its weaknesses can be exploited. My team often uses AI tools to reverse-engineer our own builds as part of prerelease security testing. This lets us examine a product the way an attacker would, discovering and prioritizing necessary fixes.
What’s Next?
AI’s impact on reverse engineering is still unfolding, and each new generation of models will likely make software analysis more accessible.
To stay prepared for this change, we need to adjust the way we think about building software. Software creators should now build their software assuming that anything they distribute can be examined and protect their products accordingly.
Forbes Technology Council is an invitation-only community for world-class CIOs, CTOs and technology executives. Do I qualify?
