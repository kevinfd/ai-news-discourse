---
id: "e9c61df9318beb73"
title: "One Hacker Used AI Agents to Breach 100+ Company Websites for About $5,000"
url: "https://kylesinvestigation.com/2026/10/20/one-hacker-used-ai-agents-to-breach-100-company-websites-for-about-5000"
link: "https://kylesinvestigation.com/2026/10/20/one-hacker-used-ai-agents-to-breach-100-company-websites-for-about-5000"
source: "KYLES INVESTIGATION"
domain: "kylesinvestigation.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T16:03:11Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Much-Television-9449"]
language: "en"
summary: "October 20, 2026 – A Chinese-speaking hacker pointed autonomous AI agents at online shops and let them do nearly all the work, according to NorForge, a threat intelligence firm. NorForge’s researcher saw it happen because the operators left their control panels open on the internet.\nPrincipal threat researcher Snorre Fagerland said the agents attempted more than 1,200 sites, mostly in the US,…"
tags: ["r/artificial"]
orgs: ["Anthropic", "DeepSeek", "China"]
topics: ["agents & coding", "search & media"]
content_source: "fulltext"
word_count: 632
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xaw48m/one_hacker_used_ai_agents_to_breach_100_company/"
score: null
comments: null
community: "r/artificial"
---

# One Hacker Used AI Agents to Breach 100+ Company Websites for About $5,000

KYLES INVESTIGATION · Much-Television-9449 · 2026-10-20

October 20, 2026 – A Chinese-speaking hacker pointed autonomous AI agents at online shops and let them do nearly all the work, according to NorForge, a threat intelligence firm. NorForge’s researcher saw it happen because the operators left their control panels open on the internet.
Principal threat researcher Snorre Fagerland said the agents attempted more than 1,200 sites, mostly in the US, Canada, Australia and Japan, starting September 25. They got into sites tied to more than 100 companies. Reuters, which reviewed the attacker’s own records, named Deere, SharkNinja and Cummins among them. How much data was taken, if any, is not known.
How it worked
The attacker used Cairn, an open-source platform that gives AI agents a goal and lets them pursue it step by step, posting findings to a shared board. It is a general-purpose tool that can be used for authorized penetration testing, and here it was aimed at sites without permission. Cairn’s author, who posts as “le1xia0,” told Reuters it wasn’t designed for hacking and that misuse was not their intention.
The operator’s instructions were minimal: fewer than 100 Chinese characters outlining preferred tactics, Reuters reported. A typical task told agents to find a way to run code on a shop and then plant a web shell uploader, a foothold that attackers can later swap for something more dangerous.
NorForge confirmed one claimed break-in at a large hardware-parts vendor, where the web shell was live. It also independently confirmed the compromise of a very large US retailer, where the agents found the single cookie setting that selected a vulnerable backend server. In one documented intrusion, the agents chained unauthorized write access to a memcached session store, unsafe handling of saved PHP objects and a flaw in old Zend Framework code. NorForge notes that the paths differed from victim to victim.
The economics
Fagerland told Reuters the campaign used about $5,000 in tokens, roughly $50 per successful hack. Successful intrusions averaged just under 23 hours. NorForge’s own report is more cautious: it puts the average at about $5 per task, counting failed and abandoned attempts, with considerable uncertainty. It also puts the overall success rate across the tools it observed at around 10%.
The agents ran under a worker name suggesting DeepSeek V4.1 Flash driven by Claude Code. Neither NorForge nor Reuters confirmed the models, and Reuters said only that the campaign appeared to use DeepSeek and Claude Code.
How it was found
Fagerland found the activity by scanning for exposed Cairn panels, identifying about two dozen being used maliciously beginning around October 2. The panels showed targets, discovered weaknesses and stolen credentials. NorForge ran the secrets scanner TruffleHog over the data and found hundreds of secrets, 11% of which were still valid. That means the open panels exposed the victims’ secrets as well as the attackers’ plans. NorForge’s search followed a September Gambit Security report on a separate criminal campaign that used Cairn, and no source links the two.
Company responses
The three named companies told Reuters the damage appeared limited. Deere said it took steps to fix the problem and had no sign that sensitive information was accessed. SharkNinja said the attack hit a standalone product-support site and that it had contained the threat. Cummins said it was investigating a report of a possible attack on a website run by one of its vendors. Two smaller businesses also told Reuters they were compromised.
What defenders can do
(Our analysis, drawing on NorForge’s findings.) Check that no AI agent control panels are reachable from the public internet without a login. Hunt for unexpected file-upload forms in hidden directories, which is the foothold these agents aimed for. Patch aggressively, and use behavior-based monitoring rather than signatures alone, since agents adapt when blocked.
Sources: NorForge report, Reuters, The Hacker News
