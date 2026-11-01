---
id: "0c5859d9893e10fb"
title: "Betelgeuse running Qwen 3.8 Flash Next IQ4_XS at 24 tok/s on 2x8GB DDR4 (14 tok/s on a single 16GB stick) + RTX 3060 12GB — 0 dropped experts, 100% byte-exact"
url: "https://reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at"
link: "https://reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T18:06:52Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["zyxciss"]
language: "en"
summary: "In my last thread on Betelgeuse ( bel-cli / bel-server ), the main pushback in the comments was: \"Okay cool, 22 tok/s on IQ2_XS , but 2-bit is too low—what happens on an actual 4-bit quant like IQ4_XS where the experts are almost 2x larger?\" \"Why were you testing on a single 16GB stick of DDR4 instead of normal dual-channel 2x 8GB ?\" Fair questions. So I upgraded the oracle + victim-cache DMA…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek", "Hugging Face", "Alibaba"]
topics: ["business & funding"]
content_source: "post"
word_count: 466
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Betelgeuse running Qwen 3.8 Flash Next IQ4_XS at 24 tok/s on 2x8GB DDR4 (14 tok/s on a single 16GB stick) + RTX 3060 12GB — 0 dropped experts, 100% byte-exact

Reddit · zyxciss · 2026-10-31

In my last thread on Betelgeuse ( bel-cli / bel-server ), the main pushback in the comments was: "Okay cool, 22 tok/s on IQ2_XS , but 2-bit is too low—what happens on an actual 4-bit quant like IQ4_XS where the experts are almost 2x larger?" "Why were you testing on a single 16GB stick of DDR4 instead of normal dual-channel 2x 8GB ?" Fair questions. So I upgraded the oracle + victim-cache DMA path, packed IQ4_XS (~100GB+ class, full 4-bit experts), and tested it on the exact same RTX 3060 12GB under both RAM configs (still 16GB total system RAM in both tests): Config A: 1x 16GB DDR4 (single-channel, ~19 GB/s host bandwidth) Config B: 2x 8GB DDR4 (normal dual-channel 16GB gaming PC setup, ~38 GB/s host bandwidth) Measured Results on IQ4_XS (RTX 3060 12GB + 16GB Total RAM) Model / Quant RAM Config (16GB Total) Stock llama.cpp Strata ( --low-ram ) Betelgeuse ( bel-server ) Output Parity vs. Stock IQ4_XS (4-bit) 1x 16GB (Single-Channel) ~0.5 tok/s (thrash) ~4–5 tok/s 14.0 tok/s 100% Byte-Exact IQ4_XS (4-bit) 2x 8GB (Dual-Channel) ~0.6 tok/s (thrash) ~5–6 tok/s 24.0 tok/s 100% Byte-Exact IQ2_XS (GSQ-RCO) 1x 16GB (Single-Channel) 1.47 tok/s 8.11 tok/s 22.03 tok/s (48 tok/s bursts) 100% Byte-Exact Q8_K_XL (8-bit) 1x 16GB (Single-Channel) OOM / <0.1 tok/s Does not fit 8.0 cold / 12.0 warm tok/s 100% Byte-Exact Why switching from 1x 16GB to 2x 8GB jumped IQ4_XS from 14 tok/s $\to$ 24 tok/s: Because Betelgeuse uses an Exclusive Host RAM Victim Cache + Async Hardware DMA ( MOE_DMA=1 ) between the VRAM slot pool and the NVMe drive: When an expert gets evicted from VRAM, it lands in the host RAM victim cache (while MOE_DROP_MMAP drops duplicate GGUF pages from the OS page cache so VRAM and RAM never hold duplicates). On a single 16GB stick , single-channel DDR4 caps out around ~17–19 GB/s, so the CPU and the PCIe H2D DMA engine fight over one 64-bit memory channel ( 14 tok/s on IQ4_XS ). On 2x 8GB dual-channel DDR4 (still 16GB total RAM, which is what 95% of normal 16GB gaming PCs actually have), host RAM bandwidth doubles, letting the GPU's hardware DMA engine pull victim-cache hits across PCIe at full speed while the upgraded oracle pre-stages cold NVMe misses in the background—jumping IQ4_XS straight to 24 tok/s . Links & What's Next GitHub (Betelgeuse Engine — bel-cli & bel-server ): [https://github.com/Betelgeuse-AI/Betelgeuse] HuggingFace (Pre-packed Alpha-Orionis-XS 3.2GB Dense + Experts bundle): https://huggingface.co/Betelgeuse-AI/Alpha-Orionis-XS Upstream llama.cpp PR: [https://github.com/ggml-org/llama.cpp/pull/31469] What I'm working on next: We're currently bringing this exact streaming + victim-cache architecture over to DeepSeek V4.1 Flash (1017) —early testing under development is already sitting around ~25 tok/s on the same hardware class. Happy to answer any questions or have people poke holes in the benchmarks! Leave us a Star :)
