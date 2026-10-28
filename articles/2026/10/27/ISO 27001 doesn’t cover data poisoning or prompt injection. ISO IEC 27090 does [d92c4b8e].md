---
id: "d92c4b8e18ac4600"
title: "ISO 27001 doesn’t cover data poisoning or prompt injection. ISO/IEC 27090 does."
url: "https://reddit.com/r/ArtificialInteligence/comments/1xh5ler/iso_27001_doesnt_cover_data_poisoning_or_prompt"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xh5ler/iso_27001_doesnt_cover_data_poisoning_or_prompt"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T21:36:45Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Comfortable_Gene5180"]
language: "en"
summary: "ISO/IEC 27090 was published on 14 October. I do not think it is receiving enough attention. Here is the gap it addresses. Most organizations already rely on ISO 27001 for information security. That standard was never made for AI‑specific attacks. A model can be compromised in ways that a normal server cannot and ISO 27090's the first international standard built around that. It explains the…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["models & research", "safety & ethics"]
content_source: "post"
word_count: 290
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xh5ler/iso_27001_doesnt_cover_data_poisoning_or_prompt/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# ISO 27001 doesn’t cover data poisoning or prompt injection. ISO/IEC 27090 does.

Reddit · Comfortable_Gene5180 · 2026-10-27

ISO/IEC 27090 was published on 14 October. I do not think it is receiving enough attention. Here is the gap it addresses. Most organizations already rely on ISO 27001 for information security. That standard was never made for AI‑specific attacks. A model can be compromised in ways that a normal server cannot and ISO 27090's the first international standard built around that. It explains the threats. Two of the ones are: 1. Data poisoning: Someone tampers with the training data so the model learns the wrong patterns. Think of a fraud detection system that has been quietly taught that fraudulent transactions look normal. 2. Prompt injection: instructions hidden in an input that push the AI to ignore its safety rules and leak information it should not. It also covers seven threats: evasion attacks, membership inference, model exfiltration, model inversion, direct model poisoning, sensitive model output and output that contains injection attacks. First it is guidance, not a certification standard. Unlike ISO 27001 or ISO 42001 there is no audit and no badge. It is a framework for managing risk which means companies cannot simply tick a box and say they are covered. Second it applies to everything from classic machine learning to generative AI across banking, healthcare, recruitment and more. It is aimed at people, in cybersecurity AI development, governance, risk and auditing. If you work in any of those areas it is worth knowing. I made a video that breaks it down if you want a walkthrough, watch the latest video @ Latha-ai-governance For those already working with these frameworks: does a guidance‑only standard actually get adopted or does it sit on a shelf without a certification attached? I am curious how your organization is handling AI security now.
