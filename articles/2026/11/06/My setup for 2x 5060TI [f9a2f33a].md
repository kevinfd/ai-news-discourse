---
id: "f9a2f33a11bfdd89"
title: "My setup for 2x 5060TI"
url: "https://reddit.com/r/LocalLLaMA/comments/1xp9v5s/my_setup_for_2x_5060ti"
link: "https://reddit.com/r/LocalLLaMA/comments/1xp9v5s/my_setup_for_2x_5060ti"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T10:48:46Z"
published_date: "2026-11-06"
collected_at: "2026-11-06T13:04:08Z"
authors: ["chocofoxy"]
language: "en"
summary: "Over the last few months I've been switching harnesses and engines until I finally landed on something good. I started with LM Studio + the Copilot extension and ended up here, so here are some tips for anyone running two 5060 Tis. Prefill is painful on these cards, so for hardware, make sure you have: A motherboard with both GPUs on CPU lanes , either two slots wired to the CPU or one x16 slot…"
tags: ["r/LocalLLaMA"]
orgs: ["Microsoft"]
topics: ["chips & infrastructure", "agents & coding"]
content_source: "post"
word_count: 582
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xp9v5s/my_setup_for_2x_5060ti/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# My setup for 2x 5060TI

Reddit · chocofoxy · 2026-11-06

Over the last few months I've been switching harnesses and engines until I finally landed on something good. I started with LM Studio + the Copilot extension and ended up here, so here are some tips for anyone running two 5060 Tis. Prefill is painful on these cards, so for hardware, make sure you have: A motherboard with both GPUs on CPU lanes , either two slots wired to the CPU or one x16 slot with PCIe bifurcation (x8/x8). My second card used to hang off the chipset; moving it to CPU lanes cut time-to-first-token by about 2.5x and doubled my batching throughput. A separate low-profile GPU just for system graphics. If one of your 5060 Tis drives the display, it burns 2-3 GB of VRAM, and since the layer split is even, the other card loses the same amount too. That's context you don't get. Model: these are Blackwell cards, so an NVFP4 quant gives you better prefill and decode. What I run: capy-flash (formerly ninfer-tp2) + OpenCode, Qwen3.8-27B NVFP4 with tensor parallel across both cards, MTP speculative decoding and int8 KV cache. I get 70-95 t/s decode and ~1,500 t/s prefill at 176K context (~3,500-4,000 t/s on shorter prompts). You can go to full context, I just don't have a third card. I'm running at PCIe Gen3 right now because I'm missing a Gen4 extender (my long riser turned out to be Gen3-rated and the second slot crashes at Gen4 with it). Prefill pushes 5-7 GB/s between the cards, which is close to the Gen3 x8 limit, so I expect Gen4 to give roughly +30-60% prefill on short/medium prompts and less at very long context, where attention compute dominates. Decode should stay about the same. P2P: you can enable it (patched open driver), but it only adds ~5% to decode and nothing to prefill. The 5060 Ti has ~4.6K CUDA cores, so compute, not the link, is the limit for decode. Harness: I use OpenCode, but honestly I don't think the harness matters much, so pick your own. The other harnesses I tried always hit context shift from compaction on long tasks, and I'd come home to find them errored out with "context limit reached." OpenCode's compaction fixed that for me, and it can now run for almost 3 days. Setup: 2x RTX 5060 Ti 16GB, Ryzen 7 5800X, B550 with x8/x8 bifurcation, capy-f NVFP4, int8 KV cache Prefill by context (single request, Gen3 x8/x8 direct to CPU, P2P on) Prompt tokens TTFT Prefill Decode 2k 0.5 s 3,860 t/s 83 t/s 8.5k 2.0 s 4,270 t/s 73 t/s 35k 9.9 s 3,520 t/s 79 t/s 71k 26.6 s 2,660 t/s 84 t/s 142k 80 s 1,770 t/s 71 t/s 176k 115 s 1,530 t/s 72 t/s Old vs. current vs. Gen4 (Gen4 column is an estimate, not measured yet) Metric 2nd GPU via chipset, no P2P Gen3 x8/x8 to CPU + P2P Gen4 x8/x8 + P2P (est.) GPU-to-GPU bandwidth ≈4 GB/s ≈7 GB/s ≈14 GB/s TTFT, 1.7k prompt 1.2 s 0.47 s ≈0.33 s Prefill, 35k 1,600–1,900 t/s 3,520 t/s ≈4,500-5,000 t/s Prefill, 176k 1,000–1,200 t/s 1,530 t/s ≈1,800-2,200 t/s Decode, 1 request ≈85 t/s 72-85 t/s about the same Decode total, 8 parallel 240–280 t/s 290 t/s ≈300-320 t/s Batching, 1.7k prompts, 4 parallel 0.79 req/s 1.50 req/s ≈1.8-2.0 req/s Batching, 1.7k prompts, 8 parallel 0.82 req/s 1.63 req/s ≈2.0-2.2 req/s P2P alone: decode ~78 → 82 t/s, prefill unchanged. i used AI to format the post only
