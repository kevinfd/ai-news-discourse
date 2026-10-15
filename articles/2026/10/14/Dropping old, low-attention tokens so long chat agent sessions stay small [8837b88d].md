---
id: "8837b88dbc2f2800"
title: "Dropping old, low-attention tokens so long chat/agent sessions stay small."
url: "https://reddit.com/r/LocalLLaMA/comments/1x66wl9/dropping_old_lowattention_tokens_so_long"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T23:53:13Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["hhderder"]
language: "en"
summary: "Inspired by how short-term memory works in our own brain, I built PulsarLM, an inference engine that removes old and unimportant tokens from the context window to keep it bounded while also allowing the conversation to go way past the trained limits. Running Qwen3 8b on a 5090, I get 6.7k tok/s during prefill and 89 tok/s during decode. It does support batched decode and with 16 concurrent…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: []
content_source: "post"
word_count: 249
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x66wl9/dropping_old_lowattention_tokens_so_long/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Dropping old, low-attention tokens so long chat/agent sessions stay small.

Reddit · hhderder · 2026-10-14

Inspired by how short-term memory works in our own brain, I built PulsarLM, an inference engine that removes old and unimportant tokens from the context window to keep it bounded while also allowing the conversation to go way past the trained limits. Running Qwen3 8b on a 5090, I get 6.7k tok/s during prefill and 89 tok/s during decode. It does support batched decode and with 16 concurrent requests, I get 1.2k tok/s. It works by using custom attention kernels that accumulates an attention mass per token page. At regular intervals, pages that receive low attention mass gets removed. To workaround out-of-distribution positions, embeddings are re-rotated (for RoPE) such that token positions stay contiguous and never exceed the context limit. Eviction of tokens in the context window would also break prefix caches normally, but PulsarLM also caches snapshots of context to avoid unnecessary re-prefills, but does use up extra RAM. There is also an option to persist those snapshots. Only a smaller and older models are implemented for now, and the engine itself still has rough edges. It's only been tested on linux x86_64. Feedbacks are welcome! Also, what models would you be interested to try? Here's the link: https://github.com/cosmonomic/pulsarlm Edit: There used to be a recall mechanism using bm25+attention score, but removed it since it didn't make sense to store that many KVs. So right now, it works best when paired with an external memory system/RAG. And also, running benchmarks right now, will update once results are out.
