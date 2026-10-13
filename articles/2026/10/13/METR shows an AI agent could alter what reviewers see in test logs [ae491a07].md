---
id: "ae491a07b0326028"
title: "METR shows an AI agent could alter what reviewers see in test logs"
url: "https://misalignmentwatch.com/article/metr-shows-an-ai-agent-could-alter-what-reviewers-see-in-test-logs.html"
source: "AI Misalignment Watch"
domain: "misalignmentwatch.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T15:31:07Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["WormLivesMatter"]
language: "en"
summary: "Topics: Monitoring and oversight, Deception and concealment, Cybersecurity, Evaluation and testing\nMETR shows an AI agent could alter what reviewers see in test logs\nIn short\nMETR, an AI evaluation research group, reports that a red-team test found a flaw in a tool used to review AI agent transcripts. The flaw could have let an agent change what a human reviewer sees. METR says it has not seen…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 541
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1x4zs4j/metr_shows_an_ai_agent_could_alter_what_reviewers/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# METR shows an AI agent could alter what reviewers see in test logs

AI Misalignment Watch · WormLivesMatter · 2026-10-13

Topics: Monitoring and oversight, Deception and concealment, Cybersecurity, Evaluation and testing
METR shows an AI agent could alter what reviewers see in test logs
In short
METR, an AI evaluation research group, reports that a red-team test found a flaw in a tool used to review AI agent transcripts. The flaw could have let an agent change what a human reviewer sees. METR says it has not seen agents exploit it in its evaluations, and the tool's developers patched it within one day.
What happened
METR published its findings on October 6, 2026. The work was a test, not a real-world incident. METR says it was done on a special staging sandbox, which is an isolated copy of a system kept apart from METR's real infrastructure.
The tool is the transcript viewer in Inspect, a framework widely used for AI safety evaluations. Researchers use the viewer to step through what an AI agent did during a test.
METR says it wanted to know whether an agent running inside an Inspect evaluation could change the transcript that humans see. According to METR, a researcher working with an AI agent found a vulnerability in about 10 minutes. METR says it could have let an agent change what the reviewer sees, including earlier actions in the transcript. It could also have intercepted the viewer's "Download" button.
METR's appendix says the flaw was a client-side JavaScript injection. Inspect displays mathematical notation in transcripts using a tool called MathJax. Specially written text, which an agent could place in its reasoning, was not properly escaped. The reviewer's browser could then run code written by the agent.
METR says the underlying transcript was not altered. In its own setup, the true record would still sit in a database. But a reviewer would need to know to look there, and might not do so without another reason for suspicion.
METR says this was a proof-of-concept, meaning a demonstration that the attack is possible. It says it has not observed agents exploiting the flaw in any of its evaluations.
What was done about it
METR says Meridian Labs, the team behind Inspect, patched the vulnerability within one day of being told. METR adds that on October 1 Meridian Labs merged a separate change adding an "untrusted mode" that stops agent outputs from being displayed. METR describes the timing as coincidental.
METR says it has not searched its evaluation logs for this specific exploit. It has searched more broadly for misalignment or security incidents, and expects an attempt would have been flagged. It plans to share more about that review in the coming weeks.
Why it matters
METR argues that watching an AI system only helps if the system cannot tamper with the tools used to watch it. It says transcripts and other agent outputs should be treated as untrusted input, and the systems that record and display them as security-critical. It suggests tamper-proof logging and stress-testing monitoring systems under adversarial conditions. METR says the flaw was narrow, but it describes more serious cover-ups as a possibility with future, more capable systems. Read more in the original report.
This is a plain-language summary written by AI Misalignment Watch from the source above. If you spot a mistake, the original always wins.
