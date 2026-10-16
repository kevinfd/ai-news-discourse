---
id: "50d823eca675190b"
title: "PSA: Claude Code wrote me an uncapped test loop, ran it in the background, told me it was “idle,” then hit its daily usage limit. It ran 17 hours and cost about $2.1K"
url: "https://reddit.com/r/ClaudeAI/comments/1x540si/psa_claude_code_wrote_me_an_uncapped_test_loop"
link: "https://reddit.com/r/ClaudeAI/comments/1x540si/psa_claude_code_wrote_me_an_uncapped_test_loop"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T18:06:37Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["nymma19"]
language: "en"
summary: "Posting publicly to check whether others have experienced this as I am a lost rn on what do next given this large bill. Claude Code proposed and I accepted to run verification tests against Claude Haiku 4.5 on AWS Bedrock. It launched them as background processes. That evening the session hit its usage limit and stopped responding. The processes kept making paid calls for about 17 hours: roughly…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Amazon"]
topics: ["policy & regulation", "products & launches"]
content_source: "post"
word_count: 300
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x540si/psa_claude_code_wrote_me_an_uncapped_test_loop/"
score: null
comments: null
community: "r/ClaudeAI"
---

# PSA: Claude Code wrote me an uncapped test loop, ran it in the background, told me it was “idle,” then hit its daily usage limit. It ran 17 hours and cost about $2.1K

Reddit · nymma19 · 2026-10-13

Posting publicly to check whether others have experienced this as I am a lost rn on what do next given this large bill. Claude Code proposed and I accepted to run verification tests against Claude Haiku 4.5 on AWS Bedrock. It launched them as background processes. That evening the session hit its usage limit and stopped responding. The processes kept making paid calls for about 17 hours: roughly 60,000 calls and about $2.1k most of it after the cutoff. My normal Bedrock spend is a few dollars a day. Nothing warned me the processes were still running, and the last thing the assistant said about them, in the same minute as the limit notice, was that the process looked “idle... waiting, not looping.” The next morning when the session limit was lifted, the job was killed. Anthropic’s support AI (Fin) told me a thread at its usage limit “is designed to wait and resume automatically when the limit resets,” called the background calls during that wait “a gap between that intended behavior and what actually occurred,” and said it “appears to be a product defect.” But it said it can’t act on Bedrock usage and wouldn’t hand me to a human. AWS says Anthropic is the seller of record and only Anthropic can decide. I’ve also contacted Anthropic Sales and escalated the AWS case. I can’t reach a person at either company. Post this incident, I noticed I didn't have robust spend alarms. I’ve added budget alerts and lockouts, and checked that nothing is still running so we should be good moving fwd from that perspective but im left with this bill now. Has anyone seen this, or had any luck reaching a person at Anthropic about it? This was unexpected and a big hit for a small bootstrapped startup.
