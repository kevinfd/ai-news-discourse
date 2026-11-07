---
id: "190596d373bb5713"
title: "Scylla's Band v4, open source TTS with code to run everywhere"
url: "https://reddit.com/r/LocalLLaMA/comments/1xpq3l0/scyllas_band_v4_open_source_tts_with_code_to_run"
link: "https://reddit.com/r/LocalLLaMA/comments/1xpq3l0/scyllas_band_v4_open_source_tts_with_code_to_run"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T22:26:59Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["clockentyne"]
language: "en"
summary: "This has been a long one for me: almost a year as a solo project, learning how to build a TTS model from the ground up. I wanted something fast, small enough to run on a phone, multilingual, and (the part I cared about most) able to do something a little different from the other small TTS models. So it sings. The demo video speech and singing are all entirely from the model. The instrumental/fx…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face", "UK"]
topics: ["models & research"]
content_source: "post"
word_count: 397
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpq3l0/scyllas_band_v4_open_source_tts_with_code_to_run/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Scylla's Band v4, open source TTS with code to run everywhere

Reddit · clockentyne · 2026-11-06

This has been a long one for me: almost a year as a solo project, learning how to build a TTS model from the ground up. I wanted something fast, small enough to run on a phone, multilingual, and (the part I cared about most) able to do something a little different from the other small TTS models. So it sings. The demo video speech and singing are all entirely from the model. The instrumental/fx are not and were added in afterwards. What it is: - ~131M parameters (plus a 30M phonemizer), 14 voices, English (US/UK), Spanish, French, German, Italian and Vietnamese. All voices can speak all languages supported. - Intensity, pace and pitch controls per line, multi-voice dialogue with inline tags, streaming - Sings from a JSON score (each word with its note and beats), pop or ballad. English only for singing format for now. - Warm first audio around 30 ms on an M5 Max, 70 ms on an iPhone 17 Pro Max, 120 ms on a Galaxy Z Fold 8 (CPU only); over 30x real time on a desktop CPU - English WER 0.85%, UTMOS 4.35 on the Open TTS Leaderboard eval (submission pending) - Apache 2.0 The GitHub and Hugging Face repos have the original PyTorch weights plus ports for LiteRT, Core ML, Core AI, ONNX Runtime and WebGPU, and a C++ runtime with a C API that handles text normalization and phonemes, so numbers, dates and odd words come out right. There's sample code for Python, iOS and Android (both apps have a Sing tab), and benchmarks from real devices. The sample apps from both allow for music score and full control over text to speech generation. Python examples for combining both and doing things like singing in unison are provided as samples. Limitations, up front: it only speaks in its own 14 voices (no voice cloning), it still trips on the odd word, and some voices get rough on fast, wide pitch jumps when singing. This is literally the first usable version of it singing, and it's something that I'm planning on improving over time... v1 was released a few months ago, and I wasn't happy with the improvements made to it until now. GitHub: https://github.com/lowkeytea/scyllasband Hugging Face: https://huggingface.co/spybyscript/scyllasband Try it in your browser: https://lowkeytea.dev/scyllasband/demo/ Happy to answer questions about training it, the singing, or getting it running on a device.
