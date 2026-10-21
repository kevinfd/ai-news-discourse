---
id: "ec4d036399505ffc"
title: "[Paper] REMORY: Learning Residual Memory for Context Compaction"
url: "https://reddit.com/r/LocalLLaMA/comments/1xasp90/paper_remory_learning_residual_memory_for_context"
link: "https://reddit.com/r/LocalLLaMA/comments/1xasp90/paper_remory_learning_residual_memory_for_context"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T13:50:57Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["pmttyji"]
language: "en"
summary: "Long-horizon agents compact their history to continue within a finite context window, but a textual summary alone may not support every subsequent decision. We introduce REMORY, a neural memory network that supplements the summary with a bounded sequence of soft memory tokens. Given the history and summary, the network learns to generate tokens that help a frozen LLM approximate the continuation…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["agents & coding"]
content_source: "post"
word_count: 156
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xasp90/paper_remory_learning_residual_memory_for_context/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Paper] REMORY: Learning Residual Memory for Context Compaction

Reddit · pmttyji · 2026-10-20

Long-horizon agents compact their history to continue within a finite context window, but a textual summary alone may not support every subsequent decision. We introduce REMORY, a neural memory network that supplements the summary with a bounded sequence of soft memory tokens. Given the history and summary, the network learns to generate tokens that help a frozen LLM approximate the continuation it would produce with the full history. The tokens are conditioned on the summary and appended after it, forming an analogue of a residual connection along the sequence dimension. On SummHay, REMORY improves source attribution at nearly unchanged insight coverage and approaches the full-context joint score using only 5.2% of the input positions. Across long-horizon agent benchmarks, Qwen3.8-27B and GLM-5.3-Flash show consistent gains with residual memory. Both models also exhibit substantially fewer repeated tool outputs and tool errors on BrowseComp and Terminal-Bench 2.1. arXiv : https://arxiv.org/abs/2610.11287 PDF : https://arxiv.org/pdf/2610.11287 GitHub : https://github.com/fudan-generative-vision/Remory HuggingFace : https://huggingface.co/collections/fudan-generative-ai/remory
