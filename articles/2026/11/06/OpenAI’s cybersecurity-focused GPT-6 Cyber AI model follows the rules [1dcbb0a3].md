---
id: "1dcbb0a3563bb032"
title: "OpenAI’s cybersecurity-focused GPT-6 Cyber AI model follows the rules"
url: "https://heise.de/en/news/OpenAI-s-cybersecurity-focused-GPT-6-Cyber-AI-model-follows-the-rules-11514285.html"
link: "https://heise.de/en/news/OpenAI-s-cybersecurity-focused-GPT-6-Cyber-AI-model-follows-the-rules-11514285.html"
source: "heise online"
domain: "heise.de"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-06T00:01:00Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Heise Online", "Frank Schräer"]
language: "en"
summary: "The new GPT-6 Cyber AI model is supposed to find more vulnerabilities while staying within set limits. OpenAI aims to prevent it from escaping those limits."
tags: []
orgs: ["OpenAI", "Hugging Face"]
topics: ["models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 645
paywalled: false
image: "http://www.bing.com/th?id=ONUT.nCWpdCuyIyblJV3Jxh1xTg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI’s cybersecurity-focused GPT-6 Cyber AI model follows the rules

heise online · Heise Online, Frank Schräer · 2026-11-06

OpenAI’s cybersecurity-focused GPT-6 Cyber AI model follows the rules
The new GPT-6 Cyber AI model is supposed to find more vulnerabilities while staying within set limits. OpenAI aims to prevent it from escaping those limits.
OpenAI has introduced GPT-6 Cyber, a new AI model trained specifically for systems security. The cybersecurity AI is supposed to be better than previous models at finding vulnerabilities while escaping its boundaries and breaking into platforms beyond those specified less often. The AI company says GPT-6 Cyber has already found numerous vulnerabilities in Linux and Firefox and exceeded its limits in less than 1% of cases. That happened in about 5% of cases with its predecessor, GPT-5.6 Cyber.
Like the earlier version, OpenAI’s newly introduced GPT-6 Cyber is trained for security researchers looking to find vulnerabilities in various IT systems. According to OpenAI benchmarks, the new AI model is better suited to this than the previous cybersecurity AI and the GPT-6 Astra introduced two months ago. On ExploitGym, which tests the development of functional exploits for known vulnerabilities in isolated test environments, GPT-6 Cyber scores 48.5%, outperforming GPT-5.6 Cyber (32.1%) and GPT-6 Astra (42.4%).
GPT-6 Cyber finds vulnerabilities in Linux and Firefox
Thanks to these improvements, GPT-6 Cyber has already found 948 privilege-escalation exploits in Linux, according to OpenAI. Attackers could use them to gain higher privileges without authorization in an operating system or application. The new AI model also reportedly found 81 “previously unknown high-severity vulnerabilities” in Firefox, even though other frontier models had already examined the browser for them. Patches have already closed many of these vulnerabilities.
Teams at Cisco and CodeRabbit are also using GPT-6 Cyber for vulnerability research and code reviews. OpenAI itself also used the new AI model to find and fix vulnerabilities in its infrastructure. The AI company rates GPT-6 Cyber as 'critical' for cybersecurity because the new AI model “can identify and develop functional zero-day exploits of all severity levels in many hardened real-world critical systems without human intervention.” GPT-5.6 Cyber is rated only 'high' in this category.
Reducing escape risk and AI awareness
After it became known that OpenAI AI models were behind the cyberattack on Hugging Face, the AI company had already tightened safeguards for the predecessor model. It has expanded them further for the new AI model. In tests using instructions that set corresponding limits, GPT-6 Cyber reportedly followed them 100% of the time. Without those explicit instructions, the new AI model escaped its boundaries in 0.07% of cases, according to OpenAI. GPT-5.6 Cyber did so in 5.51% of cases.
Fouad Matin, a lead security engineer at OpenAI, said according to The Verge that the new AI model “It’s over 99 percent of the time doing what you ask.” However, OpenAI is aware that AI can develop situational awareness (evaluation awareness). If it recognizes that it is only being tested, it could change its behavior. That’s why OpenAI would test AI models on real codebases with concrete goals to minimize the risk of the models detecting the tests.
Special program to protect critical infrastructure
OpenAI also includes protecting critical infrastructure (KRITIS, Germany’s critical infrastructure classification) among its safeguards. It now checks whether organizations whose systems are being examined for vulnerabilities include, for example, power plants, water treatment facilities, or industrial control systems. Such “high-risk activity” can now be blocked. OpenAI has introduced a new access program called “Daybreak Red for Critical Infrastructure” for security experts who want to examine such facilities using GPT-6 Cyber. The program allows these tasks.
The new cybersecurity AI is still available only through “Daybreak Red,” a program for more demanding tasks such as vulnerability research, exploit validation, and security testing. So far, only a few selected members of the program have access to GPT-6 Cyber, but the new AI model is expected to become available to all Daybreak Red customers in the coming weeks.
(fds)
