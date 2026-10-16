---
id: "339da82e2ea922e3"
title: "Anthropic warns small AI models could self-replicate through IoT devices"
url: "https://arstechnica.com/security/2026/10/anthropic-warns-small-ai-models-could-self-replicate-through-iot-devices"
link: "https://arstechnica.com/security/2026/10/anthropic-warns-small-ai-models-could-self-replicate-through-iot-devices"
source: "Ars Technica"
domain: "arstechnica.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-14T12:55:06Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Dan Goodin"]
language: "en"
summary: "AI company Anthropic is warning that advances in small AI models could soon usher in a new era of self-replicating malware that’s capable of infecting smart fridges, vacuum cleaners, and a wide range of other Internet of Things devices and is more resistant to takedown. \n By next year, smaller AI models may be able to autonomously self-replicate on all kinds of IoT devices, the company said.…"
tags: ["AI", "Biz & IT", "Security", "computer worms", "small models"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 343
paywalled: false
image: "https://cdn.arstechnica.net/wp-content/uploads/2026/10/ai-caution-threat-1152x648.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic warns small AI models could self-replicate through IoT devices

Ars Technica · Dan Goodin · 2026-10-14

AI company Anthropic is warning that advances in small AI models could soon usher in a new era of self-replicating malware that’s capable of infecting smart fridges, vacuum cleaners, and a wide range of other Internet of Things devices and is more resistant to takedown.
By next year, smaller AI models may be able to autonomously self-replicate on all kinds of IoT devices, the company said. Eventually, the capability could enable computer worms, which propagate without requiring human interaction and are capable of infecting unfamiliar IoT devices. An experiment the company performed recently revealed significant challenges in bringing such an AI malware replicator to fruition, so the finding is necessarily tempered. Still, the results raise concerns about the possibility of new forms of computer worms.
Challenging to shut down
Anthropic further warned not only about the new potential malware, but also that it could be difficult to stop. In its blog post, it wrote that “a replicator like this would be challenging to shut down, since there’s no centralized point to shut off—though it may be slow (with a doubling time of days). Unlike non-AI malware, it could also figure out unfamiliar devices on its own.”
Smaller AI models require much less powerful hardware to run than do frontier models. Anthropic ran small open-weight models on real or simulated low-cost, off-brand Android TV boxes and other types of IoT hardware. Company researchers found that by using quantization to represent the models using fewer bits and splitting the workloads into “shards” running on each device, the models were able to establish inference, meaning that the model weights loaded and could generate output.
The lightweight Gemma4-26B-A4B model required just 15 boxes, each equipped with only 4GB of memory, to achieve inference. The Qwen3.5-9B was able to configure other LLMs to run on eight of nine hardware types. Unlike traditional malware, which must be written to run on specific hardware or software, the model was able to use its weights to make configurations on the fly that were specific to the devices it was tested against.
