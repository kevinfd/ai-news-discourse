---
id: "7140965f417bccaf"
title: "New Nvidia unlock works on Chinese 3080 20GB too"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdn33h/new_nvidia_unlock_works_on_chinese_3080_20gb_too"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdn33h/new_nvidia_unlock_works_on_chinese_3080_20gb_too"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T19:09:15Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["No-Refrigerator-1672"]
language: "en"
summary: "Just ran my own tests of the new GPU performance unlock by Zaggita . If you missed it: Nvidia locked down compute speed on consumer cards for some specific hardware instructions needed for AI; the unlock fixes it. TLDR: got +20% prefill impovement, 0% decode change after unlock. Details: Test bench: my two old 2x RTX3080 20GB , this time paired with Threadripper 1920x, both running PCIe 3.0 x16.…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "China"]
topics: ["chips & infrastructure", "models & research", "agents & coding"]
content_source: "post"
word_count: 521
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdn33h/new_nvidia_unlock_works_on_chinese_3080_20gb_too/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# New Nvidia unlock works on Chinese 3080 20GB too

Reddit · No-Refrigerator-1672 · 2026-10-23

Just ran my own tests of the new GPU performance unlock by Zaggita . If you missed it: Nvidia locked down compute speed on consumer cards for some specific hardware instructions needed for AI; the unlock fixes it. TLDR: got +20% prefill impovement, 0% decode change after unlock. Details: Test bench: my two old 2x RTX3080 20GB , this time paired with Threadripper 1920x, both running PCIe 3.0 x16. Both GPUs power limited to 240W. System: Proxmox 9.2.3, linux kernel 6.14.11-9-pve, proprietary Nvidia drivers 610.57.04, CUDA 13.3. Inference: vLLM 0.32.0 running inside Debian 13 LXC container, tensor parallel mode. Model: cyankiwi/Swift-1.5-Qwen3.8-27B-AWQ-INT4 , fp8 kv cache, MTP enabled. Full vLLM launch config: vllm serve cyankiwi/Swift-1.5-Qwen3.8-27B-AWQ-INT4 --max-num-seqs 4 --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --tensor-parallel-size 2 --enable-prefix-caching --kv-cache-memory-bytes 6G --kv-cache-dtype fp8_e4m3 --enable-prompt-tokens-details --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":3}' --enable-chunked-prefill --attention-backend FLASHINFER --default-chat-template-kwargs '{"reasoning_effort": "medium"}' Benchmark results for single stream: Prompt length tok TTFT before TTFT after TTFT change ITL mean before ITL mean after Prefill tok/s before Prefill tok/s after Prefill speed change Decode steps/s before Decode steps/s after 8 192 8 471 ms 7 013 ms -17.2% 22.27 ms 29.63 ms 967 1 168 +20.8% 16.05 15.98 16 384 17 573 ms 14 418 ms -18.0% 23.93 ms 22.65 ms 932 1 136 +21.9% 16.26 15.88 32 768 36 754 ms 29 970 ms -18.5% 23.89 ms 27.20 ms 892 1 093 +22.6% 16.54 16.36 65 536 79 432 ms 64 173 ms -19.2% 27.86 ms 24.57 ms 825 1 021 +23.8% 15.98 16.50 131 072 183 593 ms 146 010 ms -20.5% 22.42 ms 25.48 ms 714 898 +25.7% 16.36 16.73 261 900 465 890 ms 362 192 ms -22.3% 24.18 ms 23.00 ms 562 723 +28.6% 15.42 16.67 TTFT: Time To First Token. Prompt processing speed is defined as prompt_length / TTFT. Each prompt in the benchmark was randomly generated, so there was no prefix cache hits during test. ITL: Inter-Token Latency: amount of time passed between two streaming responses from the engine. Decode steps/s are defines as 1s/ITL. Why I report ITL and not token generation metric: due to activated MTP, the engine will respond with multiple tokens at once; but the amount of tokens in single responce will vary, due to acceptance rate. To isolate this varuable, I measure decode step rate. If MTP acceptange length is 0, each step generates 1 token; if MTP has perfect acceptance length of 3, then each step generates 4 tokens. So this means theoretical generation performance between 15 and 60 tok/s. Real-life MTP acceptance rate for agentic coding fluctuates around 2 for this model, so real-life perforamnce fluctuates around 45 tok/s. During the test, both GPUs hit light thermal throttling and lowered their core clocks to 1750Mhz. Cold GPUs reach 1950MHz. therefore, I could have about +10% more performance if I had better cooling. I also re-run the test with full 320W power limit, got both prefill and decode speeds within 2% of 240W, so for those particular cards, power limit does not impact real life speed, but does impact real life power bill. Congratulations to fellow Ampere owners, it's a bright day for us today!
