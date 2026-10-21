---
id: "8f84a0b3f336f38b"
title: "[Paper] TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbkzll/paper_tokengate_adapting_llms_for_fast_and"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbkzll/paper_tokengate_adapting_llms_for_fast_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T11:49:21Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["pmttyji"]
language: "en"
summary: "Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context inputs. We introduce TokenGate, a small, drop-in component that extends existing trained models to enable end-to-end…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 181
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbkzll/paper_tokengate_adapting_llms_for_fast_and/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned Token Pruning

Reddit · pmttyji · 2026-10-21

Expert human readers process large inputs (e.g., code repositories and long documents) by skimming to closely read only what matters. On the other hand, language models process all input tokens through each model layer, resulting in significant processing costs for long-context inputs. We introduce TokenGate, a small, drop-in component that extends existing trained models to enable end-to-end learnable token pruning over long-context inputs for fast and memory-efficient prefill. To enable end-to-end learning despite the non-differentiable top-K operator for token pruning, we introduce token-gated attention, a mechanism inspired by Mixture-of-Experts that re-weights attention logits using token importance scores. Across diverse tasks, TokenGate achieves 1.4-11.3× faster time-to-first token (TTFT) and 1.5-3.4× lower peak memory at no accuracy degradation for prefill in transformers. Compared to the best-performing prior methods for token-pruning, TokenGate gives up to 6.4× faster prefill and 2× lower peak memory. TokenGate natively extends both standard transformers (e.g., Qwen3) and hybrid-attention models (e.g., Qwen3.5) with simple lightweight adaptation comparable to standard parameter-efficient fine-tuning. We make our code available at: this https URL . arXiv : https://arxiv.org/abs/2610.26754 PDF : https://arxiv.org/pdf/2610.26754 GitHub : https://github.com/token-gate-llms/TokenGate
