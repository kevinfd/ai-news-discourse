---
id: "a4d0e4e7a258fc74"
title: "Lipwise - Smart dictation with processing built in"
url: "https://reddit.com/r/LocalLLaMA/comments/1x4x5vm/lipwise_smart_dictation_with_processing_built_in"
link: "https://reddit.com/r/LocalLLaMA/comments/1x4x5vm/lipwise_smart_dictation_with_processing_built_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T13:49:51Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["lnenad"]
language: "en"
summary: "Lipwise is a [yet another] dictation app for Windows, macOS and Linux. You hold a hotkey, talk, and it types into whatever app has focus but with a twist. Since most of us that speak to our computers also use LLMs to do transformations I've thought why not do both in the same turn. I've played around with Qwen 3.5 9B and realized it could all be done locally, quickly and most importantly well.…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Alibaba", "Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "post"
word_count: 418
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x4x5vm/lipwise_smart_dictation_with_processing_built_in/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Lipwise - Smart dictation with processing built in

Reddit · lnenad · 2026-10-13

Lipwise is a [yet another] dictation app for Windows, macOS and Linux. You hold a hotkey, talk, and it types into whatever app has focus but with a twist. Since most of us that speak to our computers also use LLMs to do transformations I've thought why not do both in the same turn. I've played around with Qwen 3.5 9B and realized it could all be done locally, quickly and most importantly well. Plain speech-to-text gives you "um so the meeting is on tuesday no wait thursday", which is what you said, but you'd never send it like that. Lipwise runs the transcript through an LLM before outputting, with a prompt that handles corrections, spoken punctuation, lists, and instructions like "make it shorter". There's also a mode where you select text anywhere and say what to do with it ("reply saying yes but not before Monday", "translate to German"). How it works: Speech recognition always runs locally, through transcribe.cpp (ggml). There are 69 models to choose from: Parakeet, Whisper, Canary, Moonshine and others. I use Parakeet 0.6B for English. I thank Handy for the inspiration here. - The editing step. If you want to run it locally with a batteries included config - setup button checks your GPU, downloads a llama.cpp build and Qwen3.5 4B or 9B, verifies the hashes and runs it in the background. Or if not, point it at Claude, OpenAI, Ollama, LM Studio or anything OpenAI-compatible. - If the LLM is down or slow, you get the raw transcript instead of nothing. - Text goes in through the clipboard and a synthetic paste, then your clipboard is restored. - Rust and Tauri, about a 5 MB installer. - Three modes, Smart Dictation, the default recommendation, the reason I am releasing this. Plain dictation, if LLM is bugging out, not handling your text correctly or you just want those milliseconds back. And Command mode - this is for transformations/non dictation actions. Really great what it's able to do with such a small model and for simple use cases. Rough edges: Windows shows a SmartScreen warning because the installer isn't signed, and on Linux the global shortcuts depend on your compositor. The 4B model also sometimes treats a normal sentence that sounds like a command as a command. You can set a wake word so only speech that starts with it counts as an instruction. https://getlipwise.com/ https://github.com/lnenad/lipwise MIT licensed, no account, no telemetry. Happy to go into the prompts, the model choices, or anything else.
