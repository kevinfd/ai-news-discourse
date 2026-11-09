---
id: "2239391eb5fc7ef8"
title: "MIT CSAIL: GPT-6 Astra edited 0.016% of a small Qwen model's weights and lifted MATH-500 from 7.9% to 48.1% -- critics say it's standard ML engineering"
url: "https://reddit.com/r/artificial/comments/1xr8gei/mit_csail_gpt6_astra_edited_0016_of_a_small_qwen"
link: "https://reddit.com/r/artificial/comments/1xr8gei/mit_csail_gpt6_astra_edited_0016_of_a_small_qwen"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T20:36:57Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["winer666"]
language: "en"
summary: "MIT CSAIL researchers (Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab) published 'Sparks of Weight-Space Programming' on Nov 2. They gave OpenAI's GPT-6 Astra access to the raw weights of Alibaba's small Qwen3.5-0.8B model plus a Python environment, and asked it to fix the model's habit of looping on math problems. Astra traced the looping to one direction in the MLPs of layers 15 and…"
tags: ["r/artificial"]
orgs: ["OpenAI", "Alibaba", "Hugging Face"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 279
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xr8gei/mit_csail_gpt6_astra_edited_0016_of_a_small_qwen/"
score: null
comments: null
community: "r/artificial"
---

# MIT CSAIL: GPT-6 Astra edited 0.016% of a small Qwen model's weights and lifted MATH-500 from 7.9% to 48.1% -- critics say it's standard ML engineering

Reddit · winer666 · 2026-11-08

MIT CSAIL researchers (Rikiya Takehi, Jayden Teoh, Alex Zhang and Omar Khattab) published 'Sparks of Weight-Space Programming' on Nov 2. They gave OpenAI's GPT-6 Astra access to the raw weights of Alibaba's small Qwen3.5-0.8B model plus a Python environment, and asked it to fix the model's habit of looping on math problems. Astra traced the looping to one direction in the MLPs of layers 15 and 19 and subtracted it from 64 output columns in each -- changing 131,072 weights (0.016% of the total), with no training run and no gradient descent. MATH-500 went from 7.9% to 48.1%. The full experiment logs are on GitHub, and Hugging Face's Ahsen Khaliq rebuilt the edited checkpoint from the logs (his rerun scored 51.0%). The pushback came within a day. spaCy creator Matthew Honnibal called the write-up 'massively misleading': the 'raw weights, no tools' setup only applied to experiments on tiny networks (17k-172k weights). Every experiment on a real language model used Python, and the Qwen run could also test the model on up to 50 batches of practice problems. Sean Goedecke made a similar point, describing the Qwen fix as an application of steering -- an existing technique. The authors themselves call the results 'exciting but still limited', noting context length and tooling as constraints. The work is a blog post with logs, not a peer-reviewed paper. Discussion: is this a genuinely new capability -- an LLM maintaining another model the way a programmer patches code -- or mostly well-executed ML engineering dressed up as 'reading weights'? And does the distinction matter if the practical result (a 6x benchmark jump from a targeted weight edit) holds up on replication? Source: https://rikiyat.github.io/blog/weight-space-programming/
