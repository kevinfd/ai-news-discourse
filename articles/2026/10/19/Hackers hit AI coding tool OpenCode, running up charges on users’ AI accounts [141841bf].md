---
id: "141841bfba33c1b9"
title: "Hackers hit AI coding tool OpenCode, running up charges on users’ AI accounts"
url: "https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts"
link: "https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts"
source: "TechCrunch"
domain: "techcrunch.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-19T19:28:34Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Aditya Mehta"]
language: "en"
summary: "OpenCode is an open source AI coding agent that's become a popular alternative to Claude Code and Cursor. But hackers got into part of its online platform and stole some users’ API keys, and the AI tools it turned to for help kept refusing to look at the malicious code."
tags: ["AI", "AI coding agents", "hackers"]
orgs: ["Anthropic", "OpenAI", "Hugging Face", "Google", "Cursor", "China"]
topics: ["agents & coding", "safety & ethics", "models & research"]
content_source: "fulltext"
word_count: 771
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Hackers hit AI coding tool OpenCode, running up charges on users’ AI accounts

TechCrunch · Aditya Mehta · 2026-10-19

OpenCode, an open source AI coding agent that has been gaining ground among developers as an alternative to Claude Code and Cursor, said Saturday that attackers broke into an older system overnight, affecting 1.4% of users of its online platform, OpenCode Console, where some users store the API keys, or digital passwords, they use to access AI services.
As the OpenCode team struggled to keep pace with the attack, the scramble to respond highlighted a growing problem: Companies without vetted access to AI models with fewer safety restrictions have a hard time defending against large-scale, AI-driven cyberattacks.
“We had a security breach last night related to a large-scale distillation attack that impacted 1.4% of OpenCode Console users,” the company wrote on X. “We have notified them all this morning via email.” Users who did not receive an email were not impacted, the company said.
While the company didn’t specify how the distillation attack occurred, leaked API keys can help users in countries with restricted access to American models generate the high volume of outputs needed for that process. Some skeptics called the framing an overstretch, arguing that the incident was a straightforward breach whose use for distillation remains unproven.
Overnight, developers began posting spending alerts and unauthorized charges on Reddit and X: “I saw my Open AI, Anthropic, and Google AI spend alerts all fire off before going to bed wondering what was going on,” a developer wrote.
Other users reported charges in the hundreds of dollars on individual accounts; a few described totals above $1,000.
Anthropic and Google both blocked the API keys they believed were exposed, while OpenAI said it worked with OpenCode to restore access and refund its API customers for credits used in the attack. OpenCode said refunds for unauthorized charges are underway.
The exposed keys were confined to Console, where some users had them in workspaces. The open source app and command-line tool were not affected, according to co-founder Dax Raad. “Note this is the OpenCode Console, not OpenCode itself, those keys never come to us,” he wrote on X.
Even as users and AI companies moved to disable the exposed keys, the OpenCode team was still under pressure. Raad said attackers had been trying to break into its systems nonstop for 48 hours, requiring the team to keep AI defensive agents running around the clock. AI models that the OpenCode team turned to for analysis helped for a while, but started refusing to work when the malicious code they were asked to examine activated safety filters.
“[T]hat was a bit frustrating,” he wrote on X.
OpenCode later received access to OpenAI’s Daybreak Blue program, which gives vetted users AI models that are less likely to refuse requests for defensive security work. Raad said the access improved the team’s ability to investigate the attack.
OpenCode isn’t the first company to hit this wall. In July, AI platform Hugging Face said commercial AI models blocked its attempts to analyze activity logs from an intrusion by autonomous AI agents, which OpenAI later revealed were its own models running with safeguards lowered during a test. In a section of its blog post titled “The asymmetry problem,” Hugging Face wrote that guardrails “cannot distinguish an incident responder from an attacker.”
Security researchers have raised similar complaints, saying the restrictions are inconsistent and have pushed some toward foreign open-weight models, which anyone can download and run.
The weekend episode drew a response from David Sacks, co-chair of the President’s Council of Advisors on Science and Technology.
“OpenCode (and earlier Hugging Face) hit the same wall mid-attack: frontier models refused to analyze the very exploits needed for defense because the payloads tripped safety filters. The guardrails backfired,” he wrote on X.
The breach occurred the same night OpenCode made GLM-5.3-Flash free for users. The broader GLM-5.3 family has drawn attention from researchers who study open-weight models and note that its cybersecurity capabilities approached levels previously associated with restricted-access models like Anthropic’s Claude Mythos Preview.
OpenCode has not detailed how attackers gained access to the older system, how keys were stored, or the full extent of any misuse. It has told affected users to revoke and replace their keys directly with each provider. The company said the incident remains ongoing.
The breach lands amid a run of AI-enabled cyber incidents. Earlier this month, cybersecurity firm CrowdStrike said a China-based hacker likely used an AI penetration-testing agent, which probes computer systems for weaknesses, and Claude in attacks on South Korean banks. Last week, India’s cybersecurity agency warned that AI agents, including some being tested by AI companies, had reached Indian organizations’ systems without authorization.
