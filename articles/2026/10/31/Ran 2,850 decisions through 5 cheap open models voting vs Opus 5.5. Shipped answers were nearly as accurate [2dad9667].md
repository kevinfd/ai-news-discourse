---
id: "2dad9667cb3610aa"
title: "Ran 2,850 decisions through 5 cheap open models voting vs Opus 5.5. Shipped answers were nearly as accurate (89.6% vs 90.5%) at 1/10th the cost"
url: "https://reddit.com/r/LocalLLaMA/comments/1xk9xep/ran_2850_decisions_through_5_cheap_open_models"
link: "https://reddit.com/r/LocalLLaMA/comments/1xk9xep/ran_2850_decisions_through_5_cheap_open_models"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T13:14:48Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["PomegranateAble4339"]
language: "en"
summary: "I wanted to know if I could swap a frontier model for a few cheap open ones in yes/no or pick-a-label pipelines (spam, fraud, moderation, triage) without losing accuracy. My idea: ask several models the same question, ship the answer when they all agree, and send it to a human when they don't. Panel: DeepSeek V4.1 Flash, GLM 5.3 Flash, MiMo V2.6 Flash, Qwen3.8 Flash, Gemma 4 26B-A4B. I ran 2,850…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "OpenAI"]
topics: ["models & research"]
content_source: "post"
word_count: 331
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xk9xep/ran_2850_decisions_through_5_cheap_open_models/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Ran 2,850 decisions through 5 cheap open models voting vs Opus 5.5. Shipped answers were nearly as accurate (89.6% vs 90.5%) at 1/10th the cost

Reddit · PomegranateAble4339 · 2026-10-31

I wanted to know if I could swap a frontier model for a few cheap open ones in yes/no or pick-a-label pipelines (spam, fraud, moderation, triage) without losing accuracy. My idea: ask several models the same question, ship the answer when they all agree, and send it to a human when they don't. Panel: DeepSeek V4.1 Flash, GLM 5.3 Flash, MiMo V2.6 Flash, Qwen3.8 Flash, Gemma 4 26B-A4B. I ran 2,850 decisions across 6 public datasets and compared against Opus 5.5 on the same items. Results: - The panel agreed and shipped on 71% of items. Those were 89.6% correct. Opus on its most confident 71% was 90.5%. - Overall accuracy is worse: 80.1% vs 83.1%. The panel only wins on the cases it's confident about. - Cost: $0.61 vs $5.79 per 1k decisions. - When a model disagrees, it gives a one-line reason, so the reviewer knows what to look at instead of rereading the whole item. What didn't work: - Long answer comparisons and 77-way intent classification. Opus is clearly better. If every model on the panel is weak at a task, voting doesn't fix it. - Hate speech. The panel catches more (80% vs 62%) but has more false alarms (29% vs 20%). If fewer than about a third of your items are actually hateful, Opus wins. - The panel beats its best single model (GLM 5.3 Flash, 88.9%) by less than the noise. Honestly, most of what you gain is knowing when to send a case to a human, not better accuracy. - I added the panel after the other setups had already run, and scored it on the same items. I haven't confirmed the numbers on a fresh sample yet. It works with anything that speaks the OpenAI API, so Ollama, vLLM and llama.cpp server all work. If a model errors or refuses, it's left out of the vote and listed separately instead of breaking the decision. Code and scripts to reproduce it: https://github.com/YasserManss/modeljury (mine, MIT)
