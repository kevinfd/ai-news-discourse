---
id: "ecc07393279513fe"
title: "OpenAI will watermark ChatGPT outputs by default—but only in the EU"
url: "https://arstechnica.com/ai/2026/10/openai-will-watermark-chatgpt-outputs-by-default-but-only-in-the-eu"
source: "Ars Technica"
domain: "arstechnica.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-06T20:50:32Z"
published_date: "2026-10-06"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Samuel Axon"]
language: "en"
summary: "OpenAI will begin automatically watermarking text generated with ChatGPT in the European Union, the company has announced. It will also offer the watermarking feature in other regions, but it will be off by default outside of the EU. \n The move in Europe is driven by a need to comply with the EU AI Act, which took effect in August. It requires marking content produced by AI models in a way that…"
tags: ["AI", "ChatGPT", "Codex", "EU", "openai", "textGrain", "watermark"]
orgs: ["OpenAI", "EU"]
topics: ["policy & regulation"]
content_source: "fulltext"
word_count: 222
paywalled: false
image: "https://cdn.arstechnica.net/wp-content/uploads/2026/09/chatgpt-icon-1152x648-1789154124.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# OpenAI will watermark ChatGPT outputs by default—but only in the EU

Ars Technica · Samuel Axon · 2026-10-06

OpenAI will begin automatically watermarking text generated with ChatGPT in the European Union, the company has announced. It will also offer the watermarking feature in other regions, but it will be off by default outside of the EU.
The move in Europe is driven by a need to comply with the EU AI Act, which took effect in August. It requires marking content produced by AI models in a way that another tool can detect. Unfortunately, there is still no completely effective and reliable way to do that. A few standards already exist, like SynthID and the C2PA project, but they are relatively easy to circumvent for anyone with basic know-how.
The same is likely true for OpenAI’s watermark. Its method is proprietary; the company calls it textGrain, and has published a technical paper explaining how it works. But in general, it works like other LLM watermarking tools we’ve seen in the past: It puts patterns in the word choices that are not clear to a human reader and that don’t meaningfully change the general quality of the output, but that someone with a key can use a specialized detector to find. OpenAI says it will be giving access to the detector to a limited number of researchers and organizations and providing a request-for-approval process for others to be added over time.
