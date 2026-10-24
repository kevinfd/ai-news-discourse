---
id: "326dc0d7ea8dd99b"
title: "Small post about what are the unlocks for RTX consumer GPUs, which ones are affected, in which tasks and which ones are feasible to do an unlock."
url: "https://reddit.com/r/LocalLLaMA/comments/1xdg0v0/small_post_about_what_are_the_unlocks_for_rtx"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdg0v0/small_post_about_what_are_the_unlocks_for_rtx"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T14:44:31Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["panchovix"]
language: "en"
summary: "Hello guys, hoping you're doing fine! Small post I want to make since seeing a lot of posts about the unlocks and such. What is the unlock in simple terms? NVIDIA on purpose, neutered the performance of operations that use FP32 accumulation with GEMMs, with the objective of market segmentation and making consumer GPUs slower to train, or do some inference tasks slowly as well when compute is…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 579
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdg0v0/small_post_about_what_are_the_unlocks_for_rtx/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Small post about what are the unlocks for RTX consumer GPUs, which ones are affected, in which tasks and which ones are feasible to do an unlock.

Reddit · panchovix · 2026-10-23

Hello guys, hoping you're doing fine! Small post I want to make since seeing a lot of posts about the unlocks and such. What is the unlock in simple terms? NVIDIA on purpose, neutered the performance of operations that use FP32 accumulation with GEMMs, with the objective of market segmentation and making consumer GPUs slower to train, or do some inference tasks slowly as well when compute is involved (like diffusion, prompt generation). Those are "unlocked" on the prosumer and datacenters gpus. Cards with "unlocked" FP32 accumulation performance: Turing: RTX Quadro 8000 RTX Quadro in general Ampere: RTX A6000 A40 A100 RTX AXXX in general, and AXXX in general Ada: RTX 6000 Ada L40 RTX XXXX Ada in general (do not confuse with RTX 40 series) LXX in general Hopper: All unlocked Blackwell Datacenter: All unlocked Blackwell 2.0: RTX 6000 PRO RTX PRO series in general And card with locked/neutered FP32 accumulation performance: Turing: RTX 20 series in general Ampere: RTX 30 series in general Ada: RTX 40 series in general Blackwell 2.0 RTX 50 series in general So, in which parts are consumer cards affected? Turing: FP16 performance with FP32 accumulation is halved Ampere: FP16 performance with FP32 accumulation is halved BF16 performance with FP32 accumulation is halved Ada: FP16 performance with FP32 accumulation is halved BF16 performance with FP32 accumulation is halved FP8 performance with FP32 accumulation is halved Blackwell 2.0: FP16 performance with FP32 accumulation is halved BF16 performance with FP32 accumulation is halved FP8 performance with FP32 accumulation is halved FP4 is surprisingly unnafected You can also check on the papers, RTX Blackwell Paper here and RTX Blackwell PRO Paper here . And which kind of tasks does this affect?: Training: Like LoRAs, finetuning, etc. Diffusion: Models that do txt2img, txt2vid, img2img, img2vid, txt2aud, etc. Prefill on LLMs: Sadly, it does affect it, that's why a 6000 PRO on my case is like 70% faster vs a 5090, while being in theory just 10-15% faster in core count. TG with big batching: Same as above. Where it doesn't matter much: TG with batch size 1: Almost entirely bandwidth bound. CUDA compute without tensor cores INT4/INT8 GEMMs operations with FP16 accumulation instead, but is not very used. So then, what is the chance of them being unlocked? RTX 30 series can be easily make to work, with enough RE tools. All seems to be unlocked already on https://github.com/Zagitta/gpu-unlock RTX 20 series as well, similarly to RTX 30 series. RTX 40 series is more feasible and is tested working on https://huggingface.co/TOTORONG/AD103_win_unlocker , it just has to be ported to Ada in general. And sadly, on RTX 50 series is way harder, since NVIDIA added fuses where they read the flag to neuter performance there. So, RTX 20/30 series in general: high chance, RTX 40 series: relatively high chance, RTX 50 series: low chances at the moment, since NVIDIA shenanigans. I digged a lot on the code and it is really just a flag, with "HALF_SPEED" or "FULL_SPEED" lol, and all consumer GPUs are with "HALF_SPEED" for FP32 accumulation. The hard part is being able to modify this. Does unlocking them has a any risk for the card? Nope, since for example, A6000 and 3090Ti are the EXACT same dies, the only difference is that a flag into the card itself has "FULL_SPEED" for the A6000, and "HALF_SPEED" for the 3090 Ti. So pretty similar with 4090/6000 Ada, RTX 2080Ti/RTX Titan, 5090/6000 PRO, etc. Hope this post helps!
