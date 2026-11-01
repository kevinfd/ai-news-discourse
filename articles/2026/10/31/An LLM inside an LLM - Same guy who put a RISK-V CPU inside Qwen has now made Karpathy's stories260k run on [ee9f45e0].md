---
id: "ee9f45e036f9032d"
title: "An LLM inside an LLM - Same guy who put a RISK-V CPU inside Qwen has now made Karpathy's stories260k run on an NPU compiled inside Qwen 3.5-4B's weights"
url: "https://reddit.com/r/LocalLLaMA/comments/1xkiuut/an_llm_inside_an_llm_same_guy_who_put_a_riskv_cpu"
link: "https://reddit.com/r/LocalLLaMA/comments/1xkiuut/an_llm_inside_an_llm_same_guy_who_put_a_riskv_cpu"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T19:18:53Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["LatentSpacer"]
language: "en"
summary: "Code: https://github.com/divagr18/QwenPU Weights: https://huggingface.co/divagr1925/QwenPU From the original tweet : 1/3 A CPU inside an LLM is one thing, but running another LLM inside an LLM would be taking things a bit too far, wouldn't it? Anyways, here's an LLM running inside an LLM : QwenPU, an LLM (@karpathy's stories260k) running on an NPU compiled inside Qwen 3.5-4B's weights. 2/3…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 144
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xkiuut/an_llm_inside_an_llm_same_guy_who_put_a_riskv_cpu/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# An LLM inside an LLM - Same guy who put a RISK-V CPU inside Qwen has now made Karpathy's stories260k run on an NPU compiled inside Qwen 3.5-4B's weights

Reddit · LatentSpacer · 2026-10-31

Code: https://github.com/divagr18/QwenPU Weights: https://huggingface.co/divagr1925/QwenPU From the original tweet : 1/3 A CPU inside an LLM is one thing, but running another LLM inside an LLM would be taking things a bit too far, wouldn't it? Anyways, here's an LLM running inside an LLM : QwenPU, an LLM (@karpathy's stories260k) running on an NPU compiled inside Qwen 3.5-4B's weights. 2/3 stories260K is just a C program. To run it inside Qwen, I compiled an NPU into Qwen's weights that does matmuls, softmax and attention bit-exact. The LLM weights are in Qwen's own memory, with no external tools. A lot of work went into making it fast, more on that soon. 3/3 I'm super sick right now, so the full writeup is still a work in progress, and I'm working on optimisations and size reductions too. Stay tuned, I'll finish the blog & post it soon.
