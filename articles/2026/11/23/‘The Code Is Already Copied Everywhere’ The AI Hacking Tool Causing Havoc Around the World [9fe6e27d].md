---
id: "9fe6e27d2189c901"
title: "‘The Code Is Already Copied Everywhere’: The AI Hacking Tool Causing Havoc Around the World"
url: "https://404media.co/the-code-is-already-copied-everywhere-the-ai-hacking-tool-causing-havoc-around-the-world-artex-github"
link: "https://404media.co/the-code-is-already-copied-everywhere-the-ai-hacking-tool-causing-havoc-around-the-world-artex-github"
source: "404 Media"
domain: "404media.co"
source_type: "tech_press"
collector: "rss"
date: "2026-11-23T14:16:47Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Joseph Cox"]
language: "en"
summary: "ARTEX, an open source framework that makes it easy for AI agents to hack companies at superspeed, is causing havoc. People using the tool appear to include Chinese hackers breaking into targets for espionage , and financially-motivated hackers too. Earlier this month, the FBI published a warning to potential targets, and said hackers using ARTEX have targeted government, healthcare,…"
tags: ["Hacking", "AI", "News"]
orgs: ["China", "Anthropic", "DeepSeek", "Google"]
topics: ["agents & coding", "models & research", "policy & regulation", "chips & infrastructure"]
content_source: "fulltext"
word_count: 887
paywalled: false
image: "https://storage.ghost.io/c/0f/76/0f76b548-bc58-4f25-abc3-3f5ebca07da4/content/images/2026/11/Hacker_26322642210237.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# ‘The Code Is Already Copied Everywhere’: The AI Hacking Tool Causing Havoc Around the World

404 Media · Joseph Cox · 2026-11-23

ARTEX, an open source framework that makes it easy for AI agents to hack companies at superspeed, is causing havoc. People using the tool appear to include Chinese hackers breaking into targets for espionage, and financially-motivated hackers too. Earlier this month, the FBI published a warning to potential targets, and said hackers using ARTEX have targeted government, healthcare, telecommunications, legal, defense, financial services, and semiconductor sectors globally.
ARTEX is written in Go, and all someone needs to do is connect their preferred LLM — from Anthropic, DeepSeek, or whoever — and ARTEX then creates a bunch of agents that are designed to focus on different hacking tasks. There is something qualitatively different about ARTEX when compared to other hacking tools. As the FBI explains, it uses agentic AI to automate much of the hacking process “at machine speed.” This can be reconnaissance — the scoping out of a target to understand their infrastructure — right up to actually hacking a target and stealing their data. An AI agent doesn’t need to sleep, eat, or commute home. ARTEX can complete an entire hack in just a few hours from start to finish, the FBI says. With a tool like ARTEX, a hacker can set up the tool and let it rip. As Google’s threat intelligence arm has noted, hackers are using other similar multi-agent frameworks like CAIRN, CyberStrikeAI, and PentAGI too.
The original author of ARTEX, who goes by Autumn-27 and writes in Chinese, took the tool off of GitHub in October. A message left on their GitHub says, “It has come to my attention that the ARTEX tool has recently been misused by malicious actors to carry out cyberattacks. As the creator of ARTEX, I wish to make the following formal statement.” They go on to say they are not associated with these attacks, that malicious use of the tool runs “entirely counter to my original intent,” and that they are moving ARTEX into a closed-source model and will no longer update it.
But ARTEX is already free. Several people have cloned and continue to publish versions of ARTEX that anyone can use, and anyone who already downloaded their copy from Autumn-27 may still have it saved locally. ARTEX is not going anywhere.
“I’m not going to remove the repository,” one person hosting a version of ARTEX, who goes by the handle Racem, told 404 Media. “The code is already copied everywhere, as the advisory notes; deleting this repository would remove the maintained version and its fixes, not the capability.”
Jiwoo Jung, CTO of an AI marketing company and who is also hosting a version of ARTEX on GitHub, said someone asked them to take the tool down. “On November 3, a user opened a public GitHub issue (#61) saying their service had been attacked by someone using ARTEX, and asked that the project be taken down or restricted until safeguards were added,” he told 404 Media in an email. “I replied that the project would stay up, pointing to its authorized-use terms, and suggested they work with law enforcement, which they said they had already contacted.”
Tools being available openly is, of course, the nature of open source software, and specifically penetration testing and cybersecurity tools. For decades, cybersecurity defenders have used offensive open source tools to test their own defenses or those of their clients. This lets them simulate what a hacker might do, and they can patch their systems, hopefully, before a hack. But, these tools can also be used by real attackers. Look at Russian state-sponsored hackers using the age old Metasploit framework.
What has changed is the “speed and the skill level required” to hack, Jung said. “Agentic tooling compresses steps that used to take a skilled operator days into hours. That is why I think defenders need to understand these tools and have detection signatures for them.”
Racem acknowledged the damage that ARTEX is causing. “The harm the [FBI] advisory describes is real, and I don’t minimize it,” they said. “The behaviour it lists (entering systems without authorization, taking data) is a crime, whoever commits it. I’m not going to pretend the tool is harmless: it automates a large part of the manual work of a penetration test, which is why it is useful, and why some people will misuse it. The authorization belongs to the operator, not to the tool.”
The reason Racem is hosting it is for small teams, they said. “I also maintain it for people testing their own systems: founders and small teams without a pentest budget can run it against their own infrastructure for the price of some API calls. I have seen people do that, and I use it myself on bug bounty programs and for AI security research,” Racem said.
Both Racem and Jung said they don’t know if the FBI advisory is talking about their specific versions of ARTEX, and really, they can’t possibly know. But, both admonished malicious use of the tool. “I take it seriously. Using ARTEX against systems without authorization is exactly what the project’s README and legal notice prohibit, and I’d encourage security teams to check their systems against the indicators of compromise the FBI published,” Jung added.
Jung said he has since added an email address people can contact if they think ARTEX was used against their systems.
