---
id: "4c49524faa866de0"
title: "AI to find vulnerabilities in global legislation"
url: "https://github.com/lexifina/global-law/tree/main/vulnerabilities"
link: "https://github.com/lexifina/global-law/tree/main/vulnerabilities"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T23:17:46Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["SnooPeripherals5313"]
language: "en"
summary: "\"Could we get sued by AI?\" AI for cybersecurity is taking the world by storm, leading to the need to harden systems all over software. But we have access to the same engines for law. Our global law repo keeps a versioned history of law/caselaw across the world. So, we pointed AI at it, and found all sorts of loopholes and logical errors. Pah, you say. Most of this is unenforcable in reality. And…"
tags: ["r/singularity", "r/ClaudeAI"]
orgs: []
topics: ["policy & regulation"]
content_source: "fulltext"
word_count: 228
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xrc3pt/ai_to_find_vulnerabilities_in_global_legislation/"
score: null
comments: null
community: "r/singularity"
---

# AI to find vulnerabilities in global legislation

GitHub · SnooPeripherals5313 · 2026-11-08

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert
Legal exploits: 5 worked-through examples and 74,000 issues flagged by type
vulnerabilities.mp4
Each case is a logical mistake in the law itself, laid out as a legal zero-day in the sense of Legal Zero-Days: A Novel Risk Vector for Advanced AI Systems: the rule, what the official text says, why the two don't fit, what follows, who could use it, and the strongest objections, each rated. We first present the categories of error by number; the five in-depth examples are linked under More.
More
5 in-depth examples: the five mistakes walked through step by step, further confirmed mistakes, and empty periods
Confirmed cases (JSON): every case checked against official sources, with links
Are these real loopholes? They are drafting mistakes confirmed against official sources, but none has been tested in court; this is theoretical research.
How were they found? Detectors read the git history of 107 national law corpora in this repository, language models filtered the 74,000 flags, and the strongest survivors were checked by hand against gazettes and consolidated texts.
Can I report a correction? Yes: open an issue in this repository with the provision and an official source.
