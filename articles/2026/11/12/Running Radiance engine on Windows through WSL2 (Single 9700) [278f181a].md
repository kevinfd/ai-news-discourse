---
id: "278f181aacc7b0c1"
title: "Running Radiance engine on Windows through WSL2 (Single 9700)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xuhdgk/running_radiance_engine_on_windows_through_wsl2"
link: "https://reddit.com/r/LocalLLaMA/comments/1xuhdgk/running_radiance_engine_on_windows_through_wsl2"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T16:31:45Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["bruns20"]
language: "en"
summary: "Hey guys, not going to take much credit since claude did 90% of this, but wanted to share the patches I used to get StillDeadcode's Radiance running on my windows pc. I'm sure that multiple people have done this already, but I couldn't find a post, so thought I'd throw this out there if anybody else wants to use it. https://github.com/bruns20/radiance-wsl Radiance is Linux-only, and the author…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "AMD"]
topics: ["products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 269
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xuhdgk/running_radiance_engine_on_windows_through_wsl2/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Running Radiance engine on Windows through WSL2 (Single 9700)

Reddit · bruns20 · 2026-11-12

Hey guys, not going to take much credit since claude did 90% of this, but wanted to share the patches I used to get StillDeadcode's Radiance running on my windows pc. I'm sure that multiple people have done this already, but I couldn't find a post, so thought I'd throw this out there if anybody else wants to use it. https://github.com/bruns20/radiance-wsl Radiance is Linux-only, and the author has said WSL won’t be supported in the main tree, which is fair. So this is unofficial . Please send problems to my repo, not upstream. What it does build.sh builds any Radiance release from upstream’s own source and Dockerfile, with a few small WSL patches applied. When a new release comes out, it’s ./build.sh 1.18.0 . make-runtime.sh grabs a ROCm runtime that actually works under WSL. The stock ROCm 10.1 hangs on the first GPU job if your PC also has an integrated GPU ( ROCm/rocm-systems#13291 ), and AMD’s 10.3 nightlies fix it. run.sh serves an OpenAI-compatible API on 127.0.0.1:8000. Two of the four patches are godzillakong’s from codeberg #341. They did the hard part of getting it running without /dev/kfd . Numbers (R9700 32 GB, Qwen3.8-27B MXFP4 + DFlash2, 131k context) start until serving ~8 s (vLLM on the same box: 70-75 s) prefill, 9.4k / 36k-token prompt 3,223 / 2,784 tok/s decode, prose ~75-80 tok/s decode, code ~145-160 tok/s Tested on: R9700 + Ryzen 5 7600 (with its iGPU), Windows 11 26200, Adrenalin 26.10.1, Radiance 1.17.0. That’s the only setup I’ve tried. Other gfx1201 cards (RX 9070 / 9070 XT) should work, but I’d love to hear either way.
