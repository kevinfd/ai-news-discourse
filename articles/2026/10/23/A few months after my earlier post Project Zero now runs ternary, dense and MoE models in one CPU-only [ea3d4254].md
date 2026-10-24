---
id: "ea3d4254a0b1290c"
title: "A few months after my earlier post: Project Zero now runs ternary, dense and MoE models in one CPU-only binary. We just shipped v0.2.0!"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdj98z/a_few_months_after_my_earlier_post_project_zero"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdj98z/a_few_months_after_my_earlier_post_project_zero"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T16:45:17Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["shifu_legend"]
language: "en"
summary: "A few months ago, I shared my earlier post here. I wanted to come back with an update because I’m genuinely excited about how far Project Zero has come. Project Zero is my CPU-first LLM inference engine, written primarily in C, with no external ML framework dependency. It now runs BitNet/Falcon ternary models, Ternary-Bonsai-27B, dense GGUF transformers, DeepSeek-V2 and Qwen3 MoE, and Mamba-1 -…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "OpenAI"]
topics: ["models & research", "products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 432
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdj98z/a_few_months_after_my_earlier_post_project_zero/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# A few months after my earlier post: Project Zero now runs ternary, dense and MoE models in one CPU-only binary. We just shipped v0.2.0!

Reddit · shifu_legend · 2026-10-23

A few months ago, I shared my earlier post here. I wanted to come back with an update because I’m genuinely excited about how far Project Zero has come. Project Zero is my CPU-first LLM inference engine, written primarily in C, with no external ML framework dependency. It now runs BitNet/Falcon ternary models, Ternary-Bonsai-27B, dense GGUF transformers, DeepSeek-V2 and Qwen3 MoE, and Mamba-1 - all through the same executable, pz . No GPU or Python runtime required. We’ve just shipped v0.2.0 , and the part I’m happiest about isn’t simply adding more flags. It’s seeing the performance work, correctness fixes, and usability work finally come together. MoE was the wall we kept hitting and overcoming it changed the project. The MoE milestone feels especially good DeepSeek-V2-Lite-Chat Q4_K_S went from roughly 6.3-7.3 tok/s to 11.7-12.6 tok/s on a 4-vCPU AVX-512 VNNI Xeon, at four threads. The recorded llama.cpp comparison on that host was 9.4-10.5 tok/s . Yes, finally Resident memory also dropped from 12.0 GB to 10.6 GB. That came from concrete changes: fused expert FFNs, integer kernels with 8-bit activations, dynamic expert scheduling, and keeping more weights in their quantized representation rather than widening them. Watching that work turn into a measurable improvement has been incredibly satisfying. It can also now serve multiple chats together The new --parallel N mode batches active chat requests into a shared forward pass for supported dense-attention models. With four concurrent clients on a four-vCPU Xeon, the recorded aggregate throughput increased: - SmolLM2-135M Q8_0: 45 → 101 tok/s. - SmolLM2-1.7B Q4_K_M: 12.7 → 29.8 tok/s. And it’s becoming easier to actually use There’s now: - A built-in browser chat UI and an OpenAI-compatible API. - A checksum-verified Linux x86-64 installer that doesn’t need root. - Guided pz config setup that explains the settings and can download a checksum-verified starter model. - Persistent settings, including server defaults editable from the web UI. - Grammar-constrained JSON output, speculative decoding, LoRA adapters, and int8/int4 or disk-backed KV cache options. Startup also dropped from the previous 20–70-second range to roughly 1–8 seconds. Not the flashiest benchmark, but a very noticeable quality-of-life improvement. GitHub : https://github.com/shifulegend/project-zero To try the source-build demo: git clone https://github.com/shifulegend/project-zero.git cd project-zero make demo That builds the engine, downloads SmolLM2-135M, and runs a test prompt. If you try it, please share your CPU, model/quant, thread count, and results - including the disappointing ones. I’d particularly appreciate help investigating the remaining dense Q4_K performance gap. Mostly, I’m just excited to come back here with something much more capable than before. Still plenty to fix. But we kept going. :)
