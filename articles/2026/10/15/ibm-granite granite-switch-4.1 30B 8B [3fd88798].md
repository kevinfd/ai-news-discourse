---
id: "3fd88798aaa0dd94"
title: "ibm-granite/granite-switch-4.1 30B/8B"
url: "https://reddit.com/r/LocalLLaMA/comments/1x6wwx2/ibmgranitegraniteswitch41_30b8b"
link: "https://reddit.com/r/LocalLLaMA/comments/1x6wwx2/ibmgranitegraniteswitch41_30b8b"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T20:38:05Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["jacek2023"]
language: "en"
summary: "Granite Switch 4.1 30B 📝 Read the launch blog: Granite Switch 4.1: Chat, Decisions, and Speech from One Endpoint Model Summary: Granite Switch 4.1 30B is a modular LLM that composes a base model, multiple adapters and an encoder together so that a single hosted endpoint can move between natural-language responses, general and specialized decisions, and speech-to-text. Adapters are activated on…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 176
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6wwx2/ibmgranitegraniteswitch41_30b8b/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# ibm-granite/granite-switch-4.1 30B/8B

Reddit · jacek2023 · 2026-10-15

Granite Switch 4.1 30B 📝 Read the launch blog: Granite Switch 4.1: Chat, Decisions, and Speech from One Endpoint Model Summary: Granite Switch 4.1 30B is a modular LLM that composes a base model, multiple adapters and an encoder together so that a single hosted endpoint can move between natural-language responses, general and specialized decisions, and speech-to-text. Adapters are activated on demand via control tokens in the chat template. For full details on model composition and adapter configuration, see BUILD.md . Base Model: ibm-granite/granite-4.1-30b (30B params, 128K context) Adapters: 2 — decision (aLoRA, general-purpose Decisions) and guardian-core (aLoRA, from granitelib-guardian-r1.0 ) Audio: embedded speech-to-text via ibm-granite/granite-speech-5.0-470m-turboctc (470M params, English) License: Apache 2.0 Release Date: October 14, 2026 Backends: HuggingFace Transformers, vLLM Automatically Composed with: granite-switch Granite Switch is also available in granite-switch-4.1-8b (same Chat + Decisions + Guardian + speech configuration, 8B base), and with the complete Granite Libraries bundle (no audio) in granite-switch-4.1-30b-preview , -8b-preview , and -3b-preview . https://huggingface.co/ibm-granite/granite-switch-4.1-30b https://huggingface.co/ibm-granite/granite-switch-4.1-8b https://preview.redd.it/t9gf1xv60pvh1.png?width=868&format=png&auto=webp&s=0db599d4a29b463b3f3515f7ce09bf352d0e9485 (video on the blog) I think llama.cpp support is not yet ready? https://github.com/ggml-org/llama.cpp/pull/30621
