---
id: "14a22af93bc05685"
title: "Google’s Gemini 4 Neon tripled its coding score without changing the model"
url: "https://thenewstack.io/gemini-neon-antigravity-harness"
link: "https://thenewstack.io/gemini-neon-antigravity-harness"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T00:45:11Z"
published_date: "2026-11-19"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Google’s new Gemini 4 Neon resolved 12.8% of the SWE-sweep coding benchmark using the mini-SWE harness, but that score jumped to 39.0% when the same model ran inside Antigravity . \n\n The more-than-threefold improvement raises questions about how much coding-agent performance comes from the underlying model and how much depends on the harness… \n\n Both results were reported Wednesday as part of…"
tags: ["AI Agents", "AI Models", "Developer tools"]
orgs: ["Google", "Anthropic", "OpenAI"]
topics: ["models & research", "agents & coding", "business & funding", "products & launches"]
content_source: "summary"
word_count: 535
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google’s Gemini 4 Neon tripled its coding score without changing the model

The New Stack · Amanda Caswell · 2026-11-19

Google’s new Gemini 4 Neon resolved 12.8% of the SWE-sweep coding benchmark using the mini-SWE harness, but that score jumped to 39.0% when the same model ran inside Antigravity . 

 The more-than-threefold improvement raises questions about how much coding-agent performance comes from the underlying model and how much depends on the harness… 

 Both results were reported Wednesday as part of the Neon launch. The more-than-threefold improvement raises questions about how much coding-agent performance comes from the underlying model and how much depends on the harness managing its tools, context, and execution. 

 A day earlier, a FrontierHarness benchmark found that running the same open model could cost up to five times more depending on the harness 

 Same model, different scores 

 Google’s Gemini 4 Neon model card compares three frontier models on SWE-sweep using their respective provider harnesses and a shared mini-SWE baseline. 

 Neon and Opus performed substantially better with their providers’ harnesses, but Sol did not. 

 Claude Opus 5.5 climbed from 3.6% with mini-SWE to 10.1% with Claude Code, while GPT-6.2 Sol went the other way, falling from 11.6% with mini-SWE to 8.3% with Codex. Neon and Opus performed substantially better with their providers’ harnesses, but Sol did not. 

 Google tested each model in two harness configurations, though the comparison does not isolate which changes account for the differences or whether the results would hold up across other benchmarks and repositories. 

 The harness does the work 

 Antigravity’s harness was co-trained with Gemini, and Neon has been updated to make fewer unnecessary file reads and better manage context during long coding sessions. Antigravity can also run subagents in separate Git worktrees and verify their changes. 

 Google only tested Neon against mini-SWE, so there’s no data yet on how it performs with other harnesses. 

 It’s unclear which of those changes contributed most to the SWE-sweep improvement, since they weren’t tested separately. Google only tested Neon against mini-SWE, so there’s no data yet on how it performs with other harnesses. 

 Neon plans, Hydrogen builds 

 Neon is joining the model-switching system Google introduced with Gemini 4 Hydrogen . It handles planning and harder coding problems, leaving routine work to Hydrogen, and can run multiple Hydrogen subagents in parallel using the /swarm feature introduced with Carbon . 

 Google hasn’t said how much this setup affects Neon’s SWE-sweep results or what it means for the cost of completing a task. 

 Counting the cost per task 

 The company reports that Neon scored 65.2% on Terminal-Bench 4.1 and 46.2% on FrontierCode 2.0 at its default high reasoning setting. It also topped the Artificial Analysis Coding Agent Index with a score of 58.6. 

 At its default high thinking level, the model costs 32% less per task than Gemini 4 Carbon, according to Google’s comparison using the Artificial Analysis Intelligence Index. API pricing is $3 per million input tokens and $15 per million output tokens, with cached input at $0.15 per million tokens and a 1 million-token context window. 

 Neon is available through the Gemini API, Google AI Studio, and Gemini for Business. Google AI Pro and Ultra subscribers can also access it through Antigravity. 
 The post Google’s Gemini 4 Neon tripled its coding score without changing the model appeared first on The New Stack .
