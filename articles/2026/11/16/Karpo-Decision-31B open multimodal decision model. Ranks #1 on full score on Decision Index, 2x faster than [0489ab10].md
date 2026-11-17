---
id: "0489ab1026ebb5b0"
title: "Karpo-Decision-31B: open multimodal decision model. Ranks #1 on full score on Decision Index, 2x faster than Jev, at 20% lower cost"
url: "https://reddit.com/r/LocalLLaMA/comments/1xxrmt4/karpodecision31b_open_multimodal_decision_model"
link: "https://reddit.com/r/LocalLLaMA/comments/1xxrmt4/karpodecision31b_open_multimodal_decision_model"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-16T15:04:06Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Negative-Whereas3307"]
language: "en"
summary: "MachinePulse has released Karpo-Decision-31B, a Gemma 4 31B fine-tune for structured decisions over text and images. It scored 73.9 on the Nov 12 Decision Index board, the highest Full score among 300 entries, sharing the #1 rank with GLiDE 27B under the board’s tie rule How it works Built on Gemma 4 31B, with a trained linear readout that scores the supplied answer options. Three question…"
tags: ["r/LocalLLaMA"]
orgs: ["Google", "Amazon"]
topics: ["models & research"]
content_source: "post"
word_count: 359
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xxrmt4/karpodecision31b_open_multimodal_decision_model/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Karpo-Decision-31B: open multimodal decision model. Ranks #1 on full score on Decision Index, 2x faster than Jev, at 20% lower cost

Reddit · Negative-Whereas3307 · 2026-11-16

MachinePulse has released Karpo-Decision-31B, a Gemma 4 31B fine-tune for structured decisions over text and images. It scored 73.9 on the Nov 12 Decision Index board, the highest Full score among 300 entries, sharing the #1 rank with GLiDE 27B under the board’s tie rule How it works Built on Gemma 4 31B, with a trained linear readout that scores the supplied answer options. Three question types: choice, yes/no, and score. Returns probabilities directly, with up to 255 options per choice question. Multiple questions about the same input can be answered in one forward pass. Branch attention lets each question read the shared context and its own options while keeping the option branches separate. Supports text and images, including webpage screenshots. The documented sequence limit is 32,768 tokens; larger requests are split by question with the full state included in each part. Python API and HTTP server available. BF16 weights take approximately 62.5 GB, plus runtime memory. Use the provided inference code to load the decision head. One training detail worth a look: according to the team's write-up, full fine-tuning pushed the public score to 75.09 but reduced accuracy on unfamiliar domains by 2.3 percentage points. The final model averages five checkpoints: three from different stages of full fine-tuning and two from a LoRA run. They report a 1.6-point improvement on unfamiliar domains over the final single checkpoint, with no extra models to run at inference time Results Decision Index Full scores are measured by the benchmark maintainers on private tests, weighted 60% for skills covered by the public suite and 40% for tasks from new domains. Full score: 73.9 Private tests, familiar skills: 70.7 Private tasks, new domains: 78.6 Public index: 75.0, reported separately and excluded from the Full score. The team also reports the following comparisons against Google’s Gemini Decision 1: Benchmark Karpo-31B Gemini D1 ------------------------------------------- When2Call 90.4% 79.9% Mind2Web 90.0% 86.2% New Yorker Caption 90.5% 79.7% Amazon ESCI (F1) 64.7 58.7 Reported median latency is approximately 95 ms per request on the public Decision Index suite using one RTX PRO 6000. The 31B weights and inference code are both released under Apache 2.0. links: https://karpo.ai/models/decision https://huggingface.co/MachinePulseAI/karpo-decision-31B
