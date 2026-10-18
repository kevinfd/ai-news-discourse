---
id: "c2acf21e79d6c17a"
title: "Xolotl (Strata based) - DeepSeek-V4.1-Flash (552B) on a single 4090 at ~27 tok/s, Uncensored 1017 quant coming in a couple of days"
url: "https://reddit.com/r/LocalLLaMA/comments/1x8m0jj/xolotl_strata_based_deepseekv41flash_552b_on_a"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8m0jj/xolotl_strata_based_deepseekv41flash_552b_on_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T21:40:27Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["indrasmirror"]
language: "en"
summary: "Hey all, been meaning to post this for a while. I've been building an inference engine based off Strata called Xolotl that runs DeepSeek-V4.1-Flash, all 552B of it, on one gaming PC. My setup is a single RTX 4090 (24GB), a Ryzen 7 5700X, 90GB of DDR4 and an NVMe drive, nothing fancy. The weights get spread across VRAM, pinned RAM and NVMe, and the engine pulls in the experts each token actually…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 239
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8m0jj/xolotl_strata_based_deepseekv41flash_552b_on_a/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Xolotl (Strata based) - DeepSeek-V4.1-Flash (552B) on a single 4090 at ~27 tok/s, Uncensored 1017 quant coming in a couple of days

Reddit · indrasmirror · 2026-10-17

Hey all, been meaning to post this for a while. I've been building an inference engine based off Strata called Xolotl that runs DeepSeek-V4.1-Flash, all 552B of it, on one gaming PC. My setup is a single RTX 4090 (24GB), a Ryzen 7 5700X, 90GB of DDR4 and an NVMe drive, nothing fancy. The weights get spread across VRAM, pinned RAM and NVMe, and the engine pulls in the experts each token actually needs. What I'm getting on that machine: 27 tok/s decode, 180-320 tok/s prefill 512K context 21/21 HumanEval, 10/10 tool calls, 3/3 agentic bug-fix loops, all through the real server with thinking on It also runs GLM-5.3-Flash, Qwen3.8-Flash-Next and Qwen3.8-27B from the same engine. GitHub: https://github.com/Indras-Mirror/Xolotl My current quant (uncensored V4.1, 152 GiB) is here: https://huggingface.co/IndrasMirror/DeepSeek-V4.1-Flash-GSQ-Uncensored The 1017 update: I'm downloading the new DeepSeek-V4.1-Flash-1017 right now. It's slow going because my internet is a lemon, and it's 510GB, so yeah. Once it's down I'll abliterate it and quantise it for Xolotl. It's the same architecture and config as V4.1 (I checked, identical config and tokenizer), So it should run at the same throughput as the current one. The weights are all different though, so it's a full re-run of calibration and quant, not a quick patch. Hoping to have everything up in a couple of days, just wanted to get ahead of it since a few people have been asking. Happy to answer questions in the meantime.
