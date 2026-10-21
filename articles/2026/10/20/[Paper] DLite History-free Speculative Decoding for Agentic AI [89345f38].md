---
id: "89345f38dad91c5c"
title: "[Paper] DLite: History-free Speculative Decoding for Agentic AI"
url: "https://reddit.com/r/LocalLLaMA/comments/1xasomp/paper_dlite_historyfree_speculative_decoding_for"
link: "https://reddit.com/r/LocalLLaMA/comments/1xasomp/paper_dlite_historyfree_speculative_decoding_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T13:50:16Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["pmttyji"]
language: "en"
summary: "Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent multi-turn interactions. Under such workloads, we observe that existing draft…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 196
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xasomp/paper_dlite_historyfree_speculative_decoding_for/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] DLite: History-free Speculative Decoding for Agentic AI

Reddit · pmttyji · 2026-10-20

Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent multi-turn interactions. Under such workloads, we observe that existing draft models suffer from up to an 80% degradation in acceptance length, while maintaining their historical KV cache introduces substantial system overhead. In this paper, we identify the growing historical context as a common source of both problems and introduce DLite, a history-free speculative decoding framework for agentic AI. DLite directly reuses contextual hidden states from the target model and performs local speculative prediction without explicitly maintaining the historical context, transforming an increasingly complex modeling problem into local simple prediction problem. A lightweight sequential head further restores intra-block causal dependencies with low overhead. To effectively train this heterogeneous history-free architecture, we introduce a tailored two-stage training strategy. Experiments on general-purpose, long-context and agentic workloads show that DLite achieves 2-6 acceptance length and outperforms the state-of-the-art speculative decoding method, DSpark, up to 70%. arXiv : https://arxiv.org/abs/2610.23787 PDF : https://arxiv.org/pdf/2610.23787 GitHub : https://github.com/SJTU-DAI-Sys/DLite HuggingFace : https://huggingface.co/collections/SJTU-DAI-Sys/dlite
