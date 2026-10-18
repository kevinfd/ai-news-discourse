---
id: "f8ce749a8de099e9"
title: "Fish Audio Drama 3 says it needs a 48 GB NVIDIA card. My 16 GB Radeon disagrees."
url: "https://reddit.com/r/LocalLLaMA/comments/1x8kces/fish_audio_drama_3_says_it_needs_a_48_gb_nvidia"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8kces/fish_audio_drama_3_says_it_needs_a_48_gb_nvidia"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T20:27:46Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["fechyyy"]
language: "en"
summary: "Drama 3 officially needs an NVIDIA GPU with 48 GB. I wanted it on my RX 9070, so I built Red Curtain together with Claude. How it works: it's a 35B MoE with ~3B active per token. The FP8 experts (~32 GB) stay in system RAM and only the ones that actually get used are cached on the GPU. Everything else runs in BF16 on the card. Numbers on my machine: - load ~17 s - 3.3 s of speech in ~13 s, 11.6…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "Anthropic", "Hugging Face", "AMD"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 239
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8kces/fish_audio_drama_3_says_it_needs_a_48_gb_nvidia/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Fish Audio Drama 3 says it needs a 48 GB NVIDIA card. My 16 GB Radeon disagrees.

Reddit · fechyyy · 2026-10-17

Drama 3 officially needs an NVIDIA GPU with 48 GB. I wanted it on my RX 9070, so I built Red Curtain together with Claude. How it works: it's a 35B MoE with ~3B active per token. The FP8 experts (~32 GB) stay in system RAM and only the ones that actually get used are cached on the GPU. Everything else runs in BF16 on the card. Numbers on my machine: - load ~17 s - 3.3 s of speech in ~13 s, 11.6 s in ~37 s - ~11–12 GB VRAM, ~35 GB RAM So it's slower than realtime, but fine for short takes. Comes with a small web UI: voice cloning from a reference clip, multi-speaker scripts, and the same tags as Fish's own editor ([laughing], [sighing], <whisper>…</whisper> etc.). Known issue: sometimes a take says the first line and then goes silent. That's a known Drama 3 thing (the vLLM recipe mentions it too), I checked it against Fish's reference code and it's not the AMD port. What helped a lot: top-k off instead of 30, giving each speaker a reference voice, and not starting a line with a sound tag. All of that is the default now. Only tested on the RX 9070 (gfx1201) so far, would be cool to hear if it works on other cards. Weights aren't included, you download them from Hugging Face. Not affiliated with Fish Audio. Built with Fish Audio. https://github.com/re133/red-curtain
