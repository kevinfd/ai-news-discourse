---
id: "0d984d80f3cea682"
title: "I ran the same Halloween animation prompt through five coding agents on one local Qwen model"
url: "https://reddit.com/r/LocalLLaMA/comments/1xv5dsb/i_ran_the_same_halloween_animation_prompt_through"
link: "https://reddit.com/r/LocalLLaMA/comments/1xv5dsb/i_ran_the_same_halloween_animation_prompt_through"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T11:25:12Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["seti_at_home"]
language: "en"
summary: "I gave Claude Code, OpenCode, GitHub Copilot Desktop, Pi, and Codex the same prompt to build a looping pixel-art Halloween diorama. I pointed all five at the same local model, Qwen3.8 Flash Next (Unsloth UD-Q4_K_XL) , served by Halogen. The attached video shows 30 seconds of each result playing together. ### My setup - CPU/GPU: AMD Ryzen AI Max+ 395 (Strix Halo), Radeon 8060S integrated…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Microsoft", "AMD", "Alibaba"]
topics: ["agents & coding", "models & research", "chips & infrastructure", "jobs & society"]
content_source: "post"
word_count: 582
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xv5dsb/i_ran_the_same_halloween_animation_prompt_through/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I ran the same Halloween animation prompt through five coding agents on one local Qwen model

Reddit · seti_at_home · 2026-11-13

I gave Claude Code, OpenCode, GitHub Copilot Desktop, Pi, and Codex the same prompt to build a looping pixel-art Halloween diorama. I pointed all five at the same local model, Qwen3.8 Flash Next (Unsloth UD-Q4_K_XL) , served by Halogen. The attached video shows 30 seconds of each result playing together. ### My setup - CPU/GPU: AMD Ryzen AI Max+ 395 (Strix Halo), Radeon 8060S integrated graphics. - Memory: 128 GB unified memory, with about 122 GiB visible to Linux and a 512 MiB fixed GPU reservation. The GPU can use shared system memory. - OS: Ubuntu 26.04.1 LTS, kernel 7.0.0-43-generic. - Inference: Halogen Flash Server 0.20.4 in rootless Podman. I used the Unsloth Q4_K_XL checkpoint converted to Halogen's HGN format, with the vision tower enabled and MTP speculative decoding. - Server settings: 262,144-token context and KV pool, one serving slot, 16,384-token prefill chunks, prompt caching enabled, and the API bound to localhost. OpenCode, Pi, and Copilot used Chat Completions. Claude Code used the Anthropic Messages endpoint, and Codex used Responses. The clients had their own tool definitions, system prompts, and history management. Pi used High reasoning with a 4,096-token thinking budget. I raised Halogen's default output limit from 8,192 to 32,768 tokens before the recorded Codex rerun after the earlier attempt hit the smaller cap. ### What the server measured Agent Elapsed time or last completed response Result Requests Output Tokens Prefill tok/s Decode tok/s Cache Reuse Claude Code 14m 42s Final Answer 15 31,373 582 38.1 95.6% Open Code 36m 30s Final Response 54 77,832 377 39.3 98.3% Github Copilot Desktop 58m 30s Final Response 29 54,393 472 20.2 85.4% PI 1h 18m 25s Last Completed request before a memory stall 108 135,469 450 38.7 98.6% Codex 4h 11m 15s Last completed request before the turn was aborted 355 402,803 695 37.0 96.9% Elapsed times start at the first model request. Prefill rates count uncached tokens, decode rates include thinking tokens, and both are weighted by total processing time. I excluded smoke tests and incomplete requests. The video uses my earlier rounded labels for Pi and Codex. The table uses the server logs for both. Claude Code reached a final answer in about 15 minutes and used 31K output tokens. OpenCode decoded slightly faster but used roughly 2.5× as many tokens. Copilot made fewer calls than OpenCode but decoded at about half the rate, and three full prompt rereads after the initial request added almost 10 minutes of prefill. Pi still had a tool loop running when the server hit a memory stall. Codex made 355 requests before the turn was aborted, with its largest prompt reaching about 229K tokens. ### How I made the video I captured the original live browser previews for Claude Code, OpenCode, Copilot, and Pi. Codex made a Python renderer and supplied an MP4, so I captured playback of that original loop. Each capture is 1920×1080 at 30 FPS. I trimmed them to 30 seconds and synchronized them in a grid. I left the projects as they were. This was one run per client. The timing covers what each agent actually did, and I didn't score output quality or run a controlled benchmark with identical token streams. The video is there so you can compare the results for yourself. And apologies for the slop but it was interesting to see how the harnesses are working. I've tried to work with Deepseek Harness but it got stuck plenty of times so I just abandoned that exepriment. Cheers
