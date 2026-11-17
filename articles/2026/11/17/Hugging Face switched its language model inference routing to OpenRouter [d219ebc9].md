---
id: "d219ebc99cf95704"
title: "Hugging Face switched its language model inference routing to OpenRouter"
url: "https://reddit.com/r/LocalLLaMA/comments/1xy9o6j/hugging_face_switched_its_language_model"
link: "https://reddit.com/r/LocalLLaMA/comments/1xy9o6j/hugging_face_switched_its_language_model"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T03:16:54Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["jomic01"]
language: "en"
summary: "Hugging Face announced on November 16, 2026, that requests to language models through Inference Providers now go through OpenRouter instead of Hugging Face's own router. OpenRouter picks a provider for each call based on live price, speed, and reliability, and retries on another provider if the first one fails. The same Hugging Face token still works, and the company says it does not add a…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "policy & regulation"]
content_source: "post"
word_count: 218
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xy9o6j/hugging_face_switched_its_language_model/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Hugging Face switched its language model inference routing to OpenRouter

Reddit · jomic01 · 2026-11-17

Hugging Face announced on November 16, 2026, that requests to language models through Inference Providers now go through OpenRouter instead of Hugging Face's own router. OpenRouter picks a provider for each call based on live price, speed, and reliability, and retries on another provider if the first one fails. The same Hugging Face token still works, and the company says it does not add a markup on top of the provider's price. You can still pin a provider or a policy with a suffix on the model id, such as :fastest, :cheapest, or a specific provider name. OpenRouter currently serves more than 800 trillion tokens a month across 600+ models from 80+ providers. Hugging Face notes that open-weight models went from 26.8% of tokens on OpenRouter in October 2025 to 71.7% at the end of September 2026, and that they cost about four times less on average than closed models. Image, video, and audio generation stay on Hugging Face's existing Inference Providers path and do not go through OpenRouter. One breaking change is that custom provider API keys no longer work for language model requests, which are now billed to the Hugging Face account. The automatic failover is the part that matters most here, because a single provider outage is usually what ruins a long run. Source: https://huggingface.co/blog/openrouter
