---
id: "5db71574b6d7de91"
title: "Why not run Qwen 3.8 Flash Next with the full n-gram-table?"
url: "https://reddit.com/r/LocalLLaMA/comments/1x8am0i/why_not_run_qwen_38_flash_next_with_the_full"
link: "https://reddit.com/r/LocalLLaMA/comments/1x8am0i/why_not_run_qwen_38_flash_next_with_the_full"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T13:44:17Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["sillynoobhorse"]
language: "en"
summary: "Already posted here https://www.reddit.com/r/LocalLLaMA/comments/1x85hfj/strata_qwen_38_flash_next_fast_but_whats_it/phavui9/ , but I believe this topic deserves it's own post. The PLE, aka the n-gram table that sits on the SSD, is quantized heavily in the common GGUFs and has a measurable impact on performance, demonstrated here by /u/MarkoMarjamaa :…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba", "xAI"]
topics: ["models & research", "search & media"]
content_source: "post"
word_count: 317
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8am0i/why_not_run_qwen_38_flash_next_with_the_full/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Why not run Qwen 3.8 Flash Next with the full n-gram-table?

Reddit · sillynoobhorse · 2026-10-17

Already posted here https://www.reddit.com/r/LocalLLaMA/comments/1x85hfj/strata_qwen_38_flash_next_fast_but_whats_it/phavui9/ , but I believe this topic deserves it's own post. The PLE, aka the n-gram table that sits on the SSD, is quantized heavily in the common GGUFs and has a measurable impact on performance, demonstrated here by /u/MarkoMarjamaa : https://www.reddit.com/r/LocalLLaMA/comments/1x6kw7k/qwen38_flash_next_unsloth_quants_kldtop1_with/ Further down in the comments, /u/Eyelbee mentions running the full bf16 n-gram table. I asked Grok and apparently that only works in llama.cpp et.al and is called the bf16 sidecar, Strata needs FP8 but that should be close to full quality, over my head to be honest. and it recommended I build an FP8 version with ple_fp8_pack.py and indeed it seems to positively impact results. I run iq3_s and before the change the model made many more stupid mistakes. No impact on speed! Only needs a bit more disk space. If you want to try this, you need model-00005 up to model-00037.safetensors and model.safetensors.index.json from https://huggingface.co/Qwen/Qwen3.8-Flash-Next-FP8/tree/main (Edit: I accidentally linked the original repo and not the FP8 one!), then pack them into a GGUF with tools/ple_fp8_pack.py --model /media/your_ssd/Strata-data/download_folder --out /media/your_ssd/Strata-data/ple/ple-fp8.gguf and load it in your strata-xxx.json with "--ple-gguf", "/media/your_ssd/Strata-data/ple/ple-fp8.gguf" Adjust your file paths obviously. Sorry I can't upload 47gigs. :-) Maybe someone has uploaded it already but I couldn't find it. Not sure how to properly test performance, but here's two scenes with the same silly prompt. Build a beautiful 3D scene of a train driving through a futuristic cyberpunk city in HTML. dystopian vibes, detailed models, try not to use too many boxes in the models. Be creative and add some user interactivity like camera and weather controls. IQ3_S with the included PLE (quantized to IQ4_NL) https://output.jsbin.com/fojexecanu/ IQ3_S with the full FP8 PLE from Qwen https://output.jsbin.com/hosusuponi/ Imo a clear improvement is visible. I noticed that with Hermes agent too and was able to add several features to a KDE app (haruna). 3D models seem to have less errors like missing faces.
