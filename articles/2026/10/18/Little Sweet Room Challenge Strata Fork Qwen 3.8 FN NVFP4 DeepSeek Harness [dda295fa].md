---
id: "dda295fa43feb901"
title: "Little Sweet Room Challenge | Strata Fork | Qwen 3.8 FN NVFP4 | DeepSeek Harness"
url: "https://reddit.com/r/LocalLLaMA/comments/1x9hpb3/little_sweet_room_challenge_strata_fork_qwen_38"
link: "https://reddit.com/r/LocalLLaMA/comments/1x9hpb3/little_sweet_room_challenge_strata_fork_qwen_38"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T23:34:53Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Beneficial-Ad-8127"]
language: "en"
summary: "Another little challenge I seen on a DeepSeek Thread. I thought I'd try out it out on Qwen FN NvFp4. It was a pretty straight forward prompt with 4 images attached in the doc. The thread was testing different harness and models and showing their results. Op of that thread has two other threads on the same Challenge just one with DeepSeek Harness so I used it as well. It took about 27 min(Not…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "DeepSeek", "OpenAI"]
topics: ["models & research"]
content_source: "post"
word_count: 629
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x9hpb3/little_sweet_room_challenge_strata_fork_qwen_38/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Little Sweet Room Challenge | Strata Fork | Qwen 3.8 FN NVFP4 | DeepSeek Harness

Reddit · Beneficial-Ad-8127 · 2026-10-18

Another little challenge I seen on a DeepSeek Thread. I thought I'd try out it out on Qwen FN NvFp4. It was a pretty straight forward prompt with 4 images attached in the doc. The thread was testing different harness and models and showing their results. Op of that thread has two other threads on the same Challenge just one with DeepSeek Harness so I used it as well. It took about 27 min(Not bad) and was surprised how it planned everything out, also I do have vision on this Model. I think the Vision on Qwen is also a big part in a lot of Accuracy calls and adjustments. Especially notice when I use blender for other projects. Havent had too much trouble after getting use to how to even use blender since i literally started 2 weeks ago and having an LLM run it has been pretty fun to use. So if you can run vision don't sleep on it. lol Any who this was the result and I like how Qwen tried to get all the placement, designs and little details to the references. Below are the measurements and hardware I use and what not. Full prompt is from the referenced Thread. Also if you run no harness for Qwen I would like to see the results or even results from other harnesses if possible. Last but not least thank you all to the community here and everyone who is contributing locally in many ways or even just interacting with the community, keep up the great work and looking forward towards the future of running Local. Thread for full Prompt doc https://www.reddit.com/r/DeepSeek/comments/1x8nnjy/deepseek_v41_flash_1017_vs_claude_haiku_55_same/ Just the text prompt: "Create a highly realistic 3D first-person game using JavaScript. The game will take place in a single room. The room is the one shown in the 1st image. Model the room in the 1st image exactly in JavaScript, with absolutely no differences. Do not make it cartoon-style. It must be extremely realistic. Model it in the best possible way, identically, with extremely realistic graphics, and make everything very cute. By “cute,” I mean the style of the 2nd, 3rd and 4th images: cute items with clearly defined edges. Build it in the same style, cute but also realistic and well made, like the 2nd, 3rd and 4th images. Examine all 4 images I sent pixel by pixel, in detail, so you can build it exactly as I want. Make it flawless and do an excellent job." Engine: https://github.com/sergqwer/strata-nvfp4 The stack Hardware: RTX 5090 32GB · Ryzen 7 9800X3D · 192GB DDR5-5600 · Windows 11 Engine: strata-nvfp4 (fork of Niko1221/Strata by sergqwer) on Windows, llama-swap as switcher Model: Qwen3.8-Flash-Next 125B-A6B hybrid MoE — abliterated checkpoint(windowsxp811203), self-converted NVFP4 Weights: NVFP4 experts (4.5-bit) + Q8_0 dense · KV: int8 · PLE: bf16 · Embeddings: bf16 MTP: draft head, spec 5, spec-min-p 0.7 · Context: 262,144 max · Compaction trip: 220,144 Sampling: temp 0.8 / presence_penalty 0.3 / min_p 0.02 · Vision: fp32 mmproj, encoder on CPU RAM tier: 63 GiB pinned experts · Harness: dsh (web GUI), OpenAI API Metrics — this run Metric | Value Wall: first message → last reply | 26m 17s − my approval latency | −0s (zero prompts) = pure agent working time | 26m 17s Turns | 1 (single prompt, no babysitting) Steps |103 Output tokens | 132,929 Fresh input tokens |247,232 Cache-read tokens |11,994,999 ( 98.0% hit ) Decode (engine-verified) | median 121.4 t/s · mean 121.2 · peak 187.8 TTFT |median 0.85s (max 32.9s at ~194k context) Prefill (fresh, engine-verified) |mean 2,757 t/s · peak 7,096 t/s Longest single burst |10,395 tokens Compactions | 0 (peaked at 194k, never near the 220k line) Tool calls | 179 total · 17m 29s runtime · 0 errors
