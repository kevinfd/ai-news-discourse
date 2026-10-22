---
id: "8428fd8801f03b4d"
title: "I built a small on-device voice front-end for local assistants: type any wake word, keep only your voice before STT (5 models, 7.5 MB, Apache-2.0, early preview)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xbmhct/i_built_a_small_ondevice_voice_frontend_for_local"
link: "https://reddit.com/r/LocalLLaMA/comments/1xbmhct/i_built_a_small_ondevice_voice_frontend_for_local"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T12:59:41Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["cocktailpartyfixer"]
language: "en"
summary: "GitHub: https://github.com/alkove-ai/alkove (Apache-2.0, code and weights) Hi r/LocalLLaMA , A bit about me first: my day job is building LLM systems in production, a tool-calling assistant with its RAG, and two audio-heavy pipelines. The first turns a company's latest content into a two-host radio show in several languages: per-source digests, a structured script checked against the sources by…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "jobs & society", "agents & coding"]
content_source: "post"
word_count: 694
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xbmhct/i_built_a_small_ondevice_voice_frontend_for_local/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I built a small on-device voice front-end for local assistants: type any wake word, keep only your voice before STT (5 models, 7.5 MB, Apache-2.0, early preview)

Reddit · cocktailpartyfixer · 2026-10-21

GitHub: https://github.com/alkove-ai/alkove (Apache-2.0, code and weights) Hi r/LocalLLaMA , A bit about me first: my day job is building LLM systems in production, a tool-calling assistant with its RAG, and two audio-heavy pipelines. The first turns a company's latest content into a two-host radio show in several languages: per-source digests, a structured script checked against the sources by an LLM validator and code checks, one TTS call per turn with Whisper transcribing every turn back to catch truncated or invented speech, then mastering in code and ffmpeg (per-turn levelling, simulated overlaps between the hosts, loudness normalization, subtitles aligned on word timestamps). The second is a real-time voice agent in the browser: client-side VAD and denoising, an STT fallback chain, a small decision model judging each segment for end of turn, barge-in and "stop", and TTS read sentence by sentence. With that agent, most of the trouble wasn't in the LLM but before it: people talking around the user ended up in the transcript and triggered false barge-ins, and the denoiser couldn't help, since other voices are speech too. So I started working on that audio layer, the part that runs before speech-to-text and the LLM, and I'm sharing it as an early preview. It's called Alkove: five small models that run on the device and are meant to work together. - Lex (1.8 MB) turns a typed word into its likely pronunciations, so a wake word is just text: no training, no recording session. - Spot (2.8 MB) listens for those pronunciations, in 7 languages. - Timbre (0.74 MB) makes voiceprints. Three takes of the wake word give a first print, and it keeps learning while you talk. - Focus (1.1 MB) keeps your voice (the closest one, or the one matching your print) and removes noise, music and other voices before the STT. - Cue (1.1 MB) detects speech every 30 ms. Behind Focus with your print, your turns start and end on your voice only, so someone talking next to you doesn't open a new turn. The voiceprint is optional, and the same one serves all three: the wake word ignores other people, Focus keeps only you, and Cue becomes a personal VAD. Some technical details, since this sub likes them: - It runs on its own small inference engine written in Rust, not onnxruntime. One core is compiled to WebAssembly for the browser and natively for Python and Android, and gives the same output to the bit on ARM, x86 and wasm. - In the browser, the models run in workers fed by an AudioWorklet, with no COOP/COEP headers needed. The engine is 134 KB (brotli). - Native speed on one thread of a phone: Focus 38.6 ms per second of audio, Spot 7.5 ms, Cue 1.7 ms. - Packages: npm (browser and Node), pip (Linux, macOS, Windows, numpy as the only dependency), Android (Kotlin), and plugins for LiveKit Agents and Pipecat. Code and weights are Apache-2.0. A few numbers, with the protocols in the repo's bench folder: - On AMI meetings recorded on headset mics, words from other people reaching the transcript go from about 17 per minute to 0.5 with Focus and a voiceprint. - Spot, on typed single words, recalls 67% of them in English at one false alarm per hour, 90% in French, 85% in Portuguese. So for one fixed English word, a model trained on that word may well do better. What it doesn't do well yet (It's a 0.x preview and the API may still change): - It's made for a near mic and one person: a phone, a headset, a laptop. On a room mic in the middle of a table, it removes the other participants too. - When two people talk at exactly the same time, Focus only partly separates them, and two voices of the same register (two men, or two women) are much harder. That's the main thing I'm working on next. - Audio is processed at 16 kHz, so speech up to 8 kHz. I'd really appreciate feedback, especially from people running a local voice assistant: where it breaks, which integration you'd want next, and whether the API makes sense.
