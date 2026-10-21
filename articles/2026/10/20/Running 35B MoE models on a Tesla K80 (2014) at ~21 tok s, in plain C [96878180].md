---
id: "96878180d7433576"
title: "Running 35B MoE models on a Tesla K80 (2014) at ~21 tok/s, in plain C"
url: "https://reddit.com/r/LocalLLaMA/comments/1xaz06x/running_35b_moe_models_on_a_tesla_k80_2014_at_21"
link: "https://reddit.com/r/LocalLLaMA/comments/1xaz06x/running_35b_moe_models_on_a_tesla_k80_2014_at_21"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T17:49:47Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Electrical_Ninja3805"]
language: "en"
summary: "I've spent about a year on an inference engine that doesn't need modern hardware. It's called Pantheon (LLM engine) on top of Foundry (ML library), both in C with no outside libraries. The CUDA backend targets Kepler ( sm_37 ), so a Tesla K80 you can buy used for very little does real work. Measured on one K80 (both dies) in a 2-core, 8 GB, no-AVX host: Qwen3.6-35B-A3B and Nex-N2-mini (Q3_K_M):…"
tags: ["r/LocalLLaMA"]
orgs: ["Tesla", "OpenAI", "Nvidia"]
topics: ["models & research"]
content_source: "post"
word_count: 257
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xaz06x/running_35b_moe_models_on_a_tesla_k80_2014_at_21/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Running 35B MoE models on a Tesla K80 (2014) at ~21 tok/s, in plain C

Reddit · Electrical_Ninja3805 · 2026-10-20

I've spent about a year on an inference engine that doesn't need modern hardware. It's called Pantheon (LLM engine) on top of Foundry (ML library), both in C with no outside libraries. The CUDA backend targets Kepler ( sm_37 ), so a Tesla K80 you can buy used for very little does real work. Measured on one K80 (both dies) in a 2-core, 8 GB, no-AVX host: Qwen3.6-35B-A3B and Nex-N2-mini (Q3_K_M): ~21 tok/s decode Prompt reading: ~110-120 tok/s up to ~8k tokens; ~75 at 14k, ~55 at 30k Weights live on the card, not in system RAM, which is why an 8 GB host is enough Prefix caching is built in. Send a session id and later turns only process what's new. opencode does this on its own: its second turn (14k-token system prompt) went from 170 s to 9 s. Honest limits: prefill is the K80's weak spot. Chat, writing, Q&A and background jobs feel fine; pasting a 30k-token codebase every request means minutes before the first word. git clone --recursive https://git.teamide.dev/David/Pantheon.git cd Pantheon && ./install.sh --k80 ./k80_qwen36.sh # or ./k80_nexn2.sh install.sh --k80 builds it (no CUDA toolkit needed, just the NVIDIA 470 driver). The run script downloads and checks the model, then serves an OpenAI-compatible API. 🔗 Pantheon: https://git.teamide.dev/David/Pantheon 🔗 Foundry: https://git.teamide.dev/David/Foundry 🤗 https://huggingface.co/dcherrera/Qwen3.6-35B-A3B-Pantheon-K80 https://huggingface.co/dcherrera/Nex-N2-mini-Pantheon-K80 It's early and I want feedback: build problems, bugs, anything confusing. Open an issue or PR on git.teamide.dev (sign in with GitHub), or DM me. It also runs Ornith 1.5 on Tenstorrent Blackhole cards, if you have one of those.
