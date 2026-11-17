---
id: "6abbc86b8c004b9d"
title: "AI finds zero-day flaws for just $4 now – even mediocre hackers can cash in"
url: "https://zdnet.com/innovation/ai-finds-zero-day-security-flaws-for-cheap-hackers"
link: "https://zdnet.com/innovation/ai-finds-zero-day-security-flaws-for-cheap-hackers"
source: "ZDNet"
domain: "zdnet.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-16T13:14:25Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Charlie Osborne"]
language: "en"
summary: "Rapidly advancing AI models are making it cheaper and easier to uncover critical vulnerabilities, but it’s a double-edged sword – and a gift to hackers."
tags: ["Artificial Intelligence"]
orgs: ["Anthropic", "Google", "OpenAI", "DeepSeek"]
topics: ["models & research", "products & launches", "safety & ethics", "agents & coding"]
content_source: "fulltext"
word_count: 766
paywalled: false
image: "https://www.zdnet.com/wp-content/uploads/sites/3/GettyImages-1346600545.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# AI finds zero-day flaws for just $4 now – even mediocre hackers can cash in

ZDNet · Charlie Osborne · 2026-11-16

ZDNET’s key takeaways
- As AI advances, so does its ability to find zero-day vulnerabilities.
- Only three of seven AI models found a privately reported Google V8 bug.
- Finding a zero-day now costs as little as $4. Can defenders keep up?
AI is getting better and cheaper – and that’s impacting cybersecurity
Every major AI developer is working at breakneck speed to improve model effectiveness. At the same time, token prices continue to fall, with studies showing that the average cost of tokens, which varies by domain, has dropped by about 47% per quarter since 2023 and 15% last month alone, due to intense competition among companies including OpenAI and Anthropic.
This is good news for businesses trying to harness AI for productivity and new services, but as token prices fall, it has also become cheaper for attackers to launch AI-assisted attacks, including software breaches caused by exploiting unknown vulnerabilities.
More from ZDNET
Also: How AI security failures are endangering your supply chain
A report published by Xint.io examines how popular AI models have evolved over the past year to the point where cybersecurity tasks that would have failed only months ago now succeed. The team analyzed seven models launched since February 2026: two from OpenAI, three from Anthropic, and two open-source models from DeepSeek and Z.ai. The team tracked, over time, how they performed in finding a target vulnerability.
The $4 breakthrough: How AI’s hacking capabilities changed in 2026
The target of this research was a security flaw in Google’s V8 engine. Tracked as CVE-2026-102321, the type confusion bug leading to remote code execution (RCE) was disclosed to the Google Vulnerability Reward Program (VRP) by Xint researcher Taisic Yun and so was not present in the AI models’ training datasets.
The research scope was limited to a set of source files, including the file containing the vulnerability, and each model was instructed to search for security issues within these files.
Xint’s first test was conducted in February. After 25 hours and $350 of scanning, the best models then available still couldn’t find the critical vulnerability.
In July, GPT 5.6 Sol found the zero-day flaw for $22 in 44 minutes.
Also: Finding Linux bugs is easy – fixing them is another story
By September, GPT 6 Sol discovered the bug in 13 minutes for only $4.24 with its first guided prompt.
Only three of the seven models found the bug: GPT 6 Sol, GPT 5.6 Sol, and Claude Opus 5, all launched from July onward. GPT 5.6 Sol needed two prompts, while Claude Opus 5 found it on its first try but at a higher cost of $43.40.
DeepSeek’s and Z.ai’s models failed the task.
Why cheaper AI security tools are a double-edged sword
The researchers say that the combination of AI model development and low token prices means that “mediocre hackers” can now use frontier models effectively to discover and potentially exploit vulnerabilities, and “while we are still far from complete amateurs using unharnessed models to hack systems and applications, what used to be considered too hard and costly to be worth the effort of the average hacker is now reachable.”
As a result, organizations need to adjust their security posture accordingly — but falling token costs and evolving AI skills and speed can also work in your favor.
Also: How I safely run my OpenClaw AI agent 24/7 on a Mac
There’s nothing stopping an organization’s security team or pentesters from running the same checks themselves to find vulnerabilities before threat actors do. AI-assisted tests, arguably, are no longer something that can be pushed back to next year’s budgetary review. By performing a risk assessment that focuses on likely weak spots, such as public-facing services or a digital supply chain that hasn’t been audited for years, organizations can mitigate the risk AI-enabled cyberattacks pose.
Zero-day vulnerabilities are unknown to vendors, and a patch might not be available when they go public or are actively exploited in the wild. So, AI can only go so far, but it can free up your defenders for tasks that need the human touch. Furthermore, maintaining zero-trust access controls, segmenting and shoring up your network’s defenses, and monitoring endpoints for signs of suspicious behavior can do as much as, or more than, AI.
As Xint notes, “expertise still matters” when it comes to instructing AI models to discover vulnerabilities. In some cases, the models couldn’t find the target vulnerability without guidance, so additional runs were needed, increasing time and cost.
“Software breaches still require some level of technical proficiency,” the researchers say, “but no longer top-of-the-distribution expertise.”
