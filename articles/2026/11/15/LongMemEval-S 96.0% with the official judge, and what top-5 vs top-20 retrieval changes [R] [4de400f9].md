---
id: "4de400f92ef920b1"
title: "LongMemEval-S: 96.0% with the official judge, and what top-5 vs top-20 retrieval changes [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xwnloh/longmemevals_960_with_the_official_judge_and_what"
link: "https://reddit.com/r/MachineLearning/comments/1xwnloh/longmemevals_960_with_the_official_judge_and_what"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T05:40:25Z"
published_date: "2026-11-15"
collected_at: "2026-11-15T13:03:31Z"
authors: ["remoteinspace"]
language: "en"
summary: "We ran all 500 LongMemEval-S questions through our memory retrieval (Papr) using the official answer prompt and the unmodified gpt-4o-2024-08-06 judge. Per-question answers and judge labels are public, so the official metrics script reproduces the numbers. Results For comparison, Chronos reports 95.6% using full context and multi-turn agents, Hindsight reports 94.6% at 43.6k tokens per question…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 222
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xwnloh/longmemevals_960_with_the_official_judge_and_what/"
score: null
comments: null
community: "r/MachineLearning"
---

# LongMemEval-S: 96.0% with the official judge, and what top-5 vs top-20 retrieval changes [R]

Reddit · remoteinspace · 2026-11-15

We ran all 500 LongMemEval-S questions through our memory retrieval (Papr) using the official answer prompt and the unmodified gpt-4o-2024-08-06 judge. Per-question answers and judge labels are public, so the official metrics script reproduces the numbers. Results For comparison, Chronos reports 95.6% using full context and multi-turn agents, Hindsight reports 94.6% at 43.6k tokens per question (with a different judge), and gbrain reports 90.6%. Things I found useful Retrieval recall is close to saturated. All evidence sessions are in the top 5 for 460 of 470 answerable questions (97.9%). Most remaining errors are the reader, not retrieval. Top 20 vs top 5 is a trade, not a free win: 11 gained, 8 lost, net +3. Temporal reasoning went 123 → 130 of 133. Abstention stayed flat (27/30 both). A small reader gets most of the way: gpt-5-mini reaches 94.4% on the same retrieval. Caveats Used Papr-Embed 0.6B embedding model (open source and open weight), gemini flash 2.5 reranker (also tested Jev), and one turn answer model. Self-reported. Run-to-run variance is about ±3 questions, so 96.0 vs 95.6 is a tie but this run was optimized for token efficiency. We picked top 20 after reviewing the top-5 misses, so treat 96.0% as tuned on this set. No question-type labels are used in retrieval or answering. Write-up with charts: https://www.papr.ai/blog/papr-longmemeval-96 Results and code: https://github.com/Papr-ai/papr-longmemeval
