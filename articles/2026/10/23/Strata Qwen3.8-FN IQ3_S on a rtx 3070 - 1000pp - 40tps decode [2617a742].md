---
id: "2617a7421d097557"
title: "Strata: Qwen3.8-FN IQ3_S on a rtx 3070 - 1000pp - 40tps decode"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdoclb/strata_qwen38fn_iq3_s_on_a_rtx_3070_1000pp_40tps"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdoclb/strata_qwen38fn_iq3_s_on_a_rtx_3070_1000pp_40tps"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T19:57:56Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["SetNo7692"]
language: "en"
summary: "I've been messing around with strata the last couple of days and I want to share my config and results. If anyone knows how I can get even more speed from my system do let me know, thanks. Pc: ryzen 5 5600 4x16gb 2666mhz ram(bumped to 3000cl18) rtx 3070 (running at pcie3.0 due to a b350 mobo) (got the kit this week for 100 euro btw :D) System is running ubuntu server. I have also used this gpu…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 369
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdoclb/strata_qwen38fn_iq3_s_on_a_rtx_3070_1000pp_40tps/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Strata: Qwen3.8-FN IQ3_S on a rtx 3070 - 1000pp - 40tps decode

Reddit · SetNo7692 · 2026-10-23

I've been messing around with strata the last couple of days and I want to share my config and results. If anyone knows how I can get even more speed from my system do let me know, thanks. Pc: ryzen 5 5600 4x16gb 2666mhz ram(bumped to 3000cl18) rtx 3070 (running at pcie3.0 due to a b350 mobo) (got the kit this week for 100 euro btw :D) System is running ubuntu server. I have also used this gpu unlock thingy today; https://github.com/Zagitta/gpu-unlock This honestly did not give me that much extra performance, maybe 50-100tps prefill. People with a rtx 3060 will probably get more gains since more experts are loaded in vram. Here's the config: { "exe": "/home/user/Strata/engine/strata", "args": [ "--pack", "/home/user/Strata-data/packs/iq3_s", "--native", "/home/user/Strata-data/models/IQ3_S/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00001-of-00002.gguf", "--ple-gguf", "/home/user/Strata-data/models/IQ3_S/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00002-of-00002.gguf", "--expert-profile", "/home/user/Strata/data/expert-profile.bin", "--expert-cache", "auto", "--prefill", "auto", "--spec", "4", "--max-context", "262144", "--kv", "int8", "--vision", "--vram-reserve-mib", "512", "--kv-resident", "20480", "--adapt-async", "1", "--spec-min-p", "0.5", "--prompt-cache-tail" ], "cwd": "/home/user/Strata", "tokenizer": "/home/user/Strata-data/packs/iq3_s/tokenizer", "model_name": "qwen3.8-flash-next-iq3_s", "log": "/home/user/Strata/strata-iq3_s.log", "lib_dirs": [ "/usr/local/cuda-13.4/bin", "/usr/local/cuda-13.4/lib64" ], "port": 8080, "gpu": 0, "gpus_asked": true, "vision": { "exe": "/home/user/Strata/engine/strata-vision", "mmproj": "/home/user/Strata-data/models/mmproj-Qwen3.8-Flash-Next-BF16.gguf", "model": "/home/user/Strata-data/models/IQ3_S/Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S-00001-of-00002.gguf", "gpu": false, "max_tokens": 300, "threads": 6 }, "sampling": { "temperature": 1.0, "top_p": 0.95, "top_k": 20, "min_p": 0.0, "presence_penalty": 0.0, "repetition_penalty": 1.0 }, "fit_max_tokens": true, "host": "0.0.0.0", "env": { "STRATA_HC_Q8": "1", "STRATA_ROUTE_TAIL_SKIP": "7", "STRATA_ATTN_DAILY": "1", "STRATA_EXPDEC": "1", "STRATA_QSA_SPLIT_ATTN": "1", "STRATA_PROMPT_ATTN_IMMA": "1", "STRATA_HC_UPMIX": "1", "STRATA_AUX_CPUS": "auto", "STRATA_EXCHANGE_ROTATE": "1", "STRATA_PREFILL_CPU_SHARE": "auto", "STRATA_PREFILL_CPU_SHARE_MAX": "16384" } } I'm too lazy to do a/b testing but when I started with the vanilla config(mtp turned off already tho) at the same context and whatever I was getting like 500tps prefill and maybe 2-3tps decode less. Biggest gains were STRATA_HC_Q8 (quantizes the hyper connection matrices so you get more free vram for experts. Apparently slightly worse kld) and the prefill sharing with the cpu. These account for most of the prefill speedups. some requests with my config I'm honestly just blown away at what this pretty mediocre system can do, never in a 100 years did I think I could run such a big model at these speeds. Edit: forgot to mention this, I'm using a q8 n-gram table instead of the bundled iq4_nl one. Running on a sata ssd so this could maybe hamper performance a bit, not sure tho
