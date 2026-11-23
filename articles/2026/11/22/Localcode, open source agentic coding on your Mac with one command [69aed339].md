---
id: "69aed33940f7c08d"
title: "Localcode, open source agentic coding on your Mac with one command"
url: "https://github.com/mjwsolo/localcode"
link: "https://github.com/mjwsolo/localcode"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-22T22:18:48Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["mjwsolo"]
language: "en"
summary: "Agentic coding. Local models. On your Mac.\nuv pip install localcode\nUpgrade with uv pip install -U localcode.\ncd your-project\nlocalcode\nTo use the running model from another local app, open /server or run localcode api for its\nOpenAI compatible endpoint. See the Local API guide.\n- Reads and edits files in your project\n- Runs your tests, builds, Git and shell commands inside the project on its…"
tags: []
orgs: ["Alibaba", "OpenAI", "Apple", "Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches", "chips & infrastructure"]
content_source: "fulltext"
word_count: 623
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50604540"
score: 65
comments: 17
community: "Hacker News"
---

# Localcode, open source agentic coding on your Mac with one command

GitHub · mjwsolo · 2026-11-22

Agentic coding. Local models. On your Mac.
uv pip install localcode
Upgrade with uv pip install -U localcode.
cd your-project
localcode
To use the running model from another local app, open /server or run localcode api for its
OpenAI compatible endpoint. See the Local API guide.
- Reads and edits files in your project
- Runs your tests, builds, Git and shell commands inside the project on its own, and asks before touching anything outside it
- Searches code by name, content or structure
- Scaffolds and launches apps, then checks that they respond
- Remembers the task across messages
- Mac with Apple Silicon, macOS 13 or newer
- 16 GB unified memory or more
- Python 3.10 or newer
- Disk space for LocalCode and your chosen model (download sizes below)
Choose from 12 models and 169 quant options for coding, image input and typed decisions. Models download from Hugging Face. Downloads run in parallel and can resume if interrupted. Switch with /models. LocalCode recommends the most capable one that fits your Mac's memory and marks it with a star.
Speed: Gemma 4, Qwen 3.6, Muse Glimmer and Qwen 3.8 draft tokens with the vendor's own speculative drafter, which downloads with the model. The model server's GPU kernels ship precompiled, so the first start after an install is quicker.
What LocalCode adds on top of the stock model server to make local models faster and better at coding.
Speed
- Drafting: the vendor's own drafter guesses tokens ahead (about 2x faster replies on Gemma 4, Qwen 3.6, Qwen 3.8 and Muse Glimmer)
- Copy drafting: when the model rewrites a file it already read, it copies instead of generating (3.5 to 4x faster on rewrites)
- Prompt cache reuse: the system prompt stays the same every turn, so the model only reads what is new
- Warm-up: the first request's prompt is read while the model loads, so your first message starts sooner
- Precompiled GPU kernels: no half-minute shader compile on first start
- Threads matched to your Mac's performance cores
- Flash attention on by default
- Inkling 2: its experts run on the GPU (were silently on the CPU, about 5x slower), banded attention and a fused activation op halve its GPU memory and read prompts 20 to 30% faster
- Downloads run in parallel, resume if interrupted, and keep going while you use another model
Memory
- 8-bit KV cache by default: half the memory of full precision, so longer context fits
- Inkling 2 uses a 16-bit cache instead: its attention reads it directly, so long prompts read 1.4 to 1.8x faster and it needs 3.3 GB less memory at 128K context
- Context sized from what the server reports, so long chats compact before they run out of room
- The picker recommends the most capable model that fits your Mac
Quality
- Hidden thinking off by default, so answers come straight away; a model that gets stuck thinking is recovered instead of failing
- Plan panel: the model keeps a task list and is reminded to update it
- Stuck detection: a model that makes no progress, or keeps failing the same check, is nudged to change approach and then stopped so it reports what it has
- Every release is tested live on every model (load, reply, tool calls, images) before it ships
Inference is local. Three features use the network: model downloads, the web_search and web_fetch tools, and any MCP servers you add. See Network Boundary for the full list.
Powerful, personal AI should work for everyone, on any device, anywhere. That means running it locally. localcode is a first step.
To sponsor localcode, reach out.
See CONTRIBUTING.md.
Apache 2.0. See LICENSE.
