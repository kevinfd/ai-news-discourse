---
id: "6b17fe2d9ded4cd3"
title: "Gemini 4 Argon and Carbon score 91.7% and 92.6% on SimpleBench respectively. But Claude Fable 5.2 scores 94.9%, putting it in the lead instead."
url: "https://simple-bench.com"
link: "https://simple-bench.com"
source: "simple-bench.com"
domain: "simple-bench.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T17:57:58Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Profanion"]
language: "en"
summary: "We introduce SimpleBench, a multiple-choice text benchmark for LLMs where individuals\n                            with\n                            unspecialized (high school) knowledge outperform SOTA models. SimpleBench includes over 200\n                            questions covering spatio-temporal reasoning, social intelligence, and what we call\n                            linguistic…"
tags: ["r/singularity"]
orgs: ["Anthropic", "Google"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 191
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xstr95/gemini_4_argon_and_carbon_score_917_and_926_on/"
score: null
comments: null
community: "r/singularity"
---

# Gemini 4 Argon and Carbon score 91.7% and 92.6% on SimpleBench respectively. But Claude Fable 5.2 scores 94.9%, putting it in the lead instead.

simple-bench.com · Profanion · 2026-11-10

We introduce SimpleBench, a multiple-choice text benchmark for LLMs where individuals
                            with
                            unspecialized (high school) knowledge outperform SOTA models. SimpleBench includes over 200
                            questions covering spatio-temporal reasoning, social intelligence, and what we call
                            linguistic adversarial robustness (or trick questions). For the vast majority of text-based
                            benchmarks LLMs outperform a non-specialized human, and increasingly, exceed expert human
                            performance. However, on SimpleBench, a non-specialized human baseline is 83.7%, based on
                            our small sample of nine participants, outperforming every tested LLM, including
                            today's top model, Claude Fable, which scored 81.9%. While we expect model performance to improve over time, the
                            results of SimpleBench confirm that the memorized knowledge, and approximate reasoning
                            retrieval, utilized by frontier LLMs is not always enough to answer basic questions just
                            yet. 
For a deeper dive into our results and our methods, check out the full technical report here.
Use all of these models on the Simple Bench app - LMcouncil.ai
            temperature: 0.7, top-p: 0.95 (except o1 series)
            
*See Human Evaluation section of Report for details on how we calculated Human Baseline.
            
**We try an engineered prompt to optimize benchmark specific performance. See LLM Eval section of Report for
            details.
