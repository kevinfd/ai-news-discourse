---
id: "59753eaa77fd1d71"
title: "Can an AI agent manufacture evidence simply by acting on bad information?"
url: "https://reddit.com/r/ArtificialInteligence/comments/1xxvlbb/can_an_ai_agent_manufacture_evidence_simply_by"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xxvlbb/can_an_ai_agent_manufacture_evidence_simply_by"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T17:33:36Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["sefulwrong"]
language: "en"
summary: "In July, ProPublica investigated Brownsville Energy Storage Terminals. The company was legally registered. Its website described a huge international oil-storage operation, complete with executives and facilities around the world. The reporters couldn't verify those executives or facilities. Google AI Overview was already repeating some of the website's claims, including a supposed industry…"
tags: ["r/ArtificialInteligence"]
orgs: ["Google"]
topics: ["agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 235
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xxvlbb/can_an_ai_agent_manufacture_evidence_simply_by/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Can an AI agent manufacture evidence simply by acting on bad information?

Reddit · sefulwrong · 2026-11-16

In July, ProPublica investigated Brownsville Energy Storage Terminals. The company was legally registered. Its website described a huge international oil-storage operation, complete with executives and facilities around the world. The reporters couldn't verify those executives or facilities. Google AI Overview was already repeating some of the website's claims, including a supposed industry award. We've seen this sort of thing before. Bad information gets repeated until it starts looking credible. But what happens when the next AI doesn't merely repeat it? Suppose an agent researching suppliers finds that company. It creates a vendor record, opens an investigation, sends an inquiry. All perfectly normal. A few months later, another agent reviews the supplier. It finds the company registration, the vendor record, the previous investigation, perhaps some correspondence. Those records are real. They weren't hallucinated or copied from the original website. They exist because the first agent acted on information that nobody had verified. And now we have a rather nasty problem. A system can generate genuine evidence that somebody took an action based on a claim. Later, another system may mistake that evidence for confirmation of the claim itself. Tracing copied sources won't necessarily catch this. The new records have their own origins. I'm interested in whether anyone building multi-agent systems has addressed this distinction. How do you track not only where information came from, but which decisions and records exist because an earlier system believed it?
