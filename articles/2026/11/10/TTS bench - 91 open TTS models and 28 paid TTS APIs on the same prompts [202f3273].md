---
id: "202f3273b1de6a24"
title: "TTS bench - 91 open TTS models and 28 paid TTS APIs on the same prompts"
url: "https://reddit.com/r/LocalLLaMA/comments/1xsqv86/tts_bench_91_open_tts_models_and_28_paid_tts_apis"
link: "https://reddit.com/r/LocalLLaMA/comments/1xsqv86/tts_bench_91_open_tts_models_and_28_paid_tts_apis"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T16:09:25Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["UkieTechie"]
language: "en"
summary: "This is the third round of tts-bench. Thanks to everyone who gave feedback on the first two posts: TTS benchmark comparison of all known TTS models Text-to-speech benchmark, revamped tts-bench runs every model through the sameish Python harness on the same prompts, so you can compare them fairly and actually listen to the output. This round adds a separate board for hosted APIs. What's in it 91…"
tags: ["r/LocalLLaMA"]
orgs: ["Apple"]
topics: ["models & research"]
content_source: "post"
word_count: 368
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsqv86/tts_bench_91_open_tts_models_and_28_paid_tts_apis/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# TTS bench - 91 open TTS models and 28 paid TTS APIs on the same prompts

Reddit · UkieTechie · 2026-11-10

This is the third round of tts-bench. Thanks to everyone who gave feedback on the first two posts: TTS benchmark comparison of all known TTS models Text-to-speech benchmark, revamped tts-bench runs every model through the sameish Python harness on the same prompts, so you can compare them fairly and actually listen to the output. This round adds a separate board for hosted APIs. What's in it 91 open models run locally on an RTX 5090 32GB, an RTX 3090 24GB, and an Apple M4 16GB (sometimes) 28 hosted APIs on their own board, tested with the same 6 prompts (medians over several days of warm calls from the Eastern US) Prompts in English, Spanish and French Audio samples for every model, plus time to first audio, realtime factor, UTMOS, WER, voice-cloning similarity, and price for the APIs Some results from the open board Fastest: AuroraTTS-100K. On the RTX 5090 it gets to first audio in 12ms (warm) and runs 603× realtime. On CPU (Ryzen 9 9950X3D) it's 38ms and 204× realtime. Top UTMOS (naturalness): Maya1 (4.487), Underdog Woof (4.442), Phonon 31m (4.424), Chatterbox (4.423) Best cloning similarity: LongCat-AudioDiT 3.5B (0.875), then LongCat-AudioDiT 1B (0.863) and FireRedTTS3 (0.843) And from the hosted board Fastest first speech: AssemblyAI 30 ms, Gradium 53 ms, Palabra 77 ms Best sounding by UTMOS was VUI Labs Luna (4.488). It also had the best cloning similarity of 21 APIs using my own voice as the reference, but it takes about 1.2 s to start talking. Cheapest is around $9 to $10 per 1M characters (Async, Giggy, Fish, Murf). ElevenLabs v4 is $80. What the numbers don't tell you ("objective metrics") UTMOS is an automated naturalness predictor, not human preference. That's why there are listen pages and a blind-vote arena. WER measures intelligibility through transcription. It doesn't rank which voice is best. Time to first audio isn't whole-clip latency, and I don't measure concurrency. Hosted and local models are never ranked against each other. Links Repo Open models board Hosted APIs board Arena with blind human votes If your favorite model scores differently than you'd expect, go listen to the samples and vote in the arena. I'm curious which ones people actually prefer by ear.
