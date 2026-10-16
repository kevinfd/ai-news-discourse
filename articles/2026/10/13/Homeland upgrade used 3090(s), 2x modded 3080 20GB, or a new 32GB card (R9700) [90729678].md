---
id: "90729678d162e04a"
title: "Homeland upgrade: used 3090(s), 2x modded 3080 20GB, or a new 32GB card (R9700)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x58s5x/homeland_upgrade_used_3090s_2x_modded_3080_20gb"
link: "https://reddit.com/r/LocalLLaMA/comments/1x58s5x/homeland_upgrade_used_3090s_2x_modded_3080_20gb"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T21:06:56Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["MrSkullking"]
language: "en"
summary: "Hey all, First of all, apologies for the mobile formatting, will try and fix it in the morning. I'd like a second opinion before I spend real money in a GPU market that seems to go up every week. Current setup Xeon E5-2690 v4, 128GB DDR4-2133 ECC (quad channel), ASRock X99 Killer, Fractal Define R5 Proxmox host. For GPU, I am running RTX 3060 12GB + GTX 1660 6GB right now. They run Qwen3 14B…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia", "Alibaba"]
topics: ["chips & infrastructure", "models & research", "jobs & society", "agents & coding"]
content_source: "post"
word_count: 461
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x58s5x/homeland_upgrade_used_3090s_2x_modded_3080_20gb/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Homeland upgrade: used 3090(s), 2x modded 3080 20GB, or a new 32GB card (R9700)

Reddit · MrSkullking · 2026-10-13

Hey all, First of all, apologies for the mobile formatting, will try and fix it in the morning. I'd like a second opinion before I spend real money in a GPU market that seems to go up every week. Current setup Xeon E5-2690 v4, 128GB DDR4-2133 ECC (quad channel), ASRock X99 Killer, Fractal Define R5 Proxmox host. For GPU, I am running RTX 3060 12GB + GTX 1660 6GB right now. They run Qwen3 14B (EXL2/TabbyAPI) for small jobs (Paperless tagging, recipe parsing, a Telegram bot), plus Whisper/Kokoro for Home Assistant, Jellyfin transcoding and Immich ML. The board has two x16 slots spaced for dual-slot cards only, plus an x8 at the bottom that currently holds my boot NVMe on an adapter. I can move to SATA boot to free that slot. What I want to do with it: Run something like Hermes Agent as an orchestrator on a properly good model. Qwen3.8-27B looks like the one right now (who knows what magic Qwen 4 brings), and Flash-Next interests me too. Some of my Ideas: persistent memory, a daily log of what I did, recording meetings → transcript → tasks/ideas/paper suggestions, calendar planning, Home Assistant plus a wall tablet. I'm a PhD student, so keeping lab stuff local matters. It's mostly one user, but several services hit the endpoint, and I'd like Whisper/embeddings/a small router model running next to the main model. Options (prices in NL right now) - Used 3090(s): €1100–1400 each. Either one now next to the 3060, or two eventually. Fastest of the lot, but 24GB means 27B at Q4/Q5 on one card. Most are triple slot, so two won't fit my board without blowers or risers. - 2x modded 3080 20GB (blower): about €650–900 each, imported. 40GB total, dual slot, so both plus the 3060 fit. I'm worried about how much extra for tax, noise and how reliable the memory mods are long term. - New 32GB card: R9700 at about €2000. Warranty, one card, 27B at Q6 with plenty of context, and the 3060 stays next to it. But it's slower than a 3090 and not CUDA. The box is always on and power here is about €0.27/kWh, so a 1000W+ triple-GPU setup isn't free either. Questions - For agentic/tool-calling use, is 27B at Q4/Q5 noticeably worse than Q6/Q8 in practice? - Anyone running the modded 3080 20GBs for a while? How have they held up? - How are ROCm or SYCL/Vulkan in practice for llama.cpp/vLLM, especially passed through in Proxmox, and alongside an NVIDIA card in the same box? - Does PCIe 3.0 x16 on X99 hold back tensor parallel across two cards in practice? - Has anyone run Flash-Next with the experts offloaded to DDR4? Usable, or not worth it? Anything I'm missing? Thanks!
