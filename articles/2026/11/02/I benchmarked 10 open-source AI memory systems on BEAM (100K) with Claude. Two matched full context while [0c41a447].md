---
id: "0c41a44740d55b21"
title: "I benchmarked 10 open-source AI memory systems on BEAM (100K) with Claude. Two matched full context while reading 24–35x less text"
url: "https://reddit.com/r/ClaudeAI/comments/1xlo7ls/i_benchmarked_10_opensource_ai_memory_systems_on"
link: "https://reddit.com/r/ClaudeAI/comments/1xlo7ls/i_benchmarked_10_opensource_ai_memory_systems_on"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T04:50:47Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Mundane-Educator75"]
language: "en"
summary: "TL;DR EverOS (70.1%) and Hindsight (67.8%) are the best. They scored as well as giving the model the whole conversation (69.5%) while reading 24–35x less text, and were the only two to clearly beat plain keyword search. EverOS saves chats as dated notes, which kept it strong on instructions, timing and facts that change. Hindsight was the best at recalling exact details. With only 60 questions,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI", "Hugging Face"]
topics: ["models & research", "search & media"]
content_source: "post"
word_count: 495
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlo7ls/i_benchmarked_10_opensource_ai_memory_systems_on/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I benchmarked 10 open-source AI memory systems on BEAM (100K) with Claude. Two matched full context while reading 24–35x less text

Reddit · Mundane-Educator75 · 2026-11-02

TL;DR EverOS (70.1%) and Hindsight (67.8%) are the best. They scored as well as giving the model the whole conversation (69.5%) while reading 24–35x less text, and were the only two to clearly beat plain keyword search. EverOS saves chats as dated notes, which kept it strong on instructions, timing and facts that change. Hindsight was the best at recalling exact details. With only 60 questions, ranks 3–8 aren't clearly separated. Results Rank System Score (95% CI) Retrieved tokens Retrieval p50 Ingest time (3 convs) Ingest cost (US$) 1 EverOS 70.1% (61.7–77.8) 3,336 1.2 s 14 min $1.05 – Full context (baseline) 69.5% (59.9–78.3) 115,541 – – – 2 Hindsight 67.8% (58.9–75.8) 4,913 2.2 s 13 min $1.50 3 Cognee 62.7% (53.1–71.4) 23,263 2.9 s 12 min $1.02 4 memsearch 61.8% (52.7–70.8) 1,822 0.2 s 10 min $0 (no LLM) 5 OpenViking 61.5% (51.9–70.9) 1,431 1.4 s 77 min $0.76 6 MemPalace 61.0% (51.1–70.6) 1,624 1.4 s 3 min $0 (no LLM) 7 LangMem 60.8% (51.1–70.1) 3,209 1.1 s 35 min $0.34 8 Mem0 55.6% (44.9–65.7) 1,164 1.3 s 132 min $1.22 – BM25 (baseline) 55.3% (44.6–65.4) 7,204 2 ms – – 9 claude-mem 51.5% (41.2–61.4) 30,015 0.3 s <1 min $0 (LLM unused) 10 Graphiti 43.7% (33.8–53.6) 354 1.2 s 29 min $1.92 Score by ability (%) Only 6 questions per ability, so treat these as signals. System Abstain Contradiction Event order Info extraction Instruction following Knowledge update Multi-session Preference Summarisation Temporal EverOS 83 83 37 57 92 75 55 86 49 83 Full context 83 73 46 63 92 50 58 100 57 75 Hindsight 83 81 47 79 75 33 49 100 56 75 Cognee 92 77 47 39 100 50 33 72 30 88 memsearch 92 65 38 39 79 83 41 83 32 67 OpenViking 83 48 47 35 79 75 46 79 32 92 MemPalace 83 65 34 67 83 58 31 83 22 83 LangMem 83 56 46 53 75 58 42 83 27 83 Mem0 83 71 37 44 79 17 34 96 28 67 BM25 83 44 40 44 71 50 27 96 32 67 claude-mem 83 40 35 33 79 50 33 96 33 33 Graphiti 92 63 42 33 58 17 31 75 19 8 Setup Benchmark: BEAM 100K (Tavakoli et al., Mohammadta/BEAM on Hugging Face). 3 conversations fixed in advance: #6 (Writing), #1 (Coding) and #13 (Recommendation). That's 345K tokens and 60 rubric-graded questions across 10 abilities. Models: Claude Haiku 5.5 (effort xhigh) ran each system's LLM calls and answered every question. Claude Opus 5.5 (xhigh) judged the answers. Seven systems used OpenAI text-embedding-3-small for embeddings; memsearch, Hindsight and claude-mem used their own. Answer step: the same prompt for all, given each system's full retrieved memory, with every system on default settings. Full context gets the whole conversation; BM25 fills an 8K-token budget by keyword search. Scoring: BEAM's judge prompt and rubric, scoring each item 1, 0.5 or 0, with 95% bootstrap CIs.
