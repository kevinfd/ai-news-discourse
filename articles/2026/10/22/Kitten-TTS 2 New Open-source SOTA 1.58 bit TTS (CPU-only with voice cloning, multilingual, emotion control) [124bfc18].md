---
id: "124bfc18656ea433"
title: "Kitten-TTS 2: New Open-source SOTA 1.58 bit TTS (CPU-only with voice cloning, multilingual, emotion control)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xc48or/kittentts_2_new_opensource_sota_158_bit_tts"
link: "https://reddit.com/r/LocalLLaMA/comments/1xc48or/kittentts_2_new_opensource_sota_158_bit_tts"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T00:33:11Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["ElectricalBar7464"]
language: "en"
summary: "KittenML has just released code and weights of Kitten-TTS 2, which is a super-efficient frontier TTS model, and the world's first 1.58-bit TTS model . It runs in real time on just a CPU, with zero-shot voice cloning, multilingual support, and expressive / emphasis control. Code and weights are open-source. Ternary(1.58-bit) Weights means it can run locally or be self-hosted for super-cheap.…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 249
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xc48or/kittentts_2_new_opensource_sota_158_bit_tts/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Kitten-TTS 2: New Open-source SOTA 1.58 bit TTS (CPU-only with voice cloning, multilingual, emotion control)

Reddit · ElectricalBar7464 · 2026-10-22

KittenML has just released code and weights of Kitten-TTS 2, which is a super-efficient frontier TTS model, and the world's first 1.58-bit TTS model . It runs in real time on just a CPU, with zero-shot voice cloning, multilingual support, and expressive / emphasis control. Code and weights are open-source. Ternary(1.58-bit) Weights means it can run locally or be self-hosted for super-cheap. Github: https://github.com/KittenML/KittenTTS Hugging Face: https://huggingface.co/KittenML/kitten-tts-2 KittenML's Discord: https://discord.com/invite/VJ86W4SURW Key features and Advantages Ternary TTS: Every linear weight in the body is one of three values (-1, 0, +1) with group size of 128 for scales. Tiny footprint and fast CPU inference. The model has 1.7B parameters. Real-time on CPU and consumer GPU's too : No GPU needed for real-time generation. Optimized ternary kernels for CPU inference provided. Expressive voice cloning : zero-shot cloning from less than 5 seconds of reference audio, and it keeps the expressivity, accent information etc. No fine-tuning needed. Multilingual TTS: Model supports voice cloning in 20+ languages. Cross-language voice cloning can be used to create accented speech too. Expressive / emphasis control: you can steer the delivery and stress specific words, not just pick a voice. Details in the Readme. Open source (hell yeah!) : code and weights are open-source and free to use. It's an oss alternative to elevenlabs for gpu-poor folks. easy to self-deploy or run locally. 7. What changed from V0.8 to 2: higher quality. Completely new architecture, natural sounding speech, ternary weights, zero-shot voice cloning, multilingual, and emphasis/emotion control.
