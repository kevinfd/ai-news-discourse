---
id: "6d162958c77c3708"
title: "Mirage: A 22 MB visual-language model that runs scene descriptions + object detection + OCR + segmentation + spatial relations analysis + extractions + decisions, in a single pass."
url: "https://reddit.com/r/LocalLLaMA/comments/1xpm8mw/mirage_a_22_mb_visuallanguage_model_that_runs"
link: "https://reddit.com/r/LocalLLaMA/comments/1xpm8mw/mirage_a_22_mb_visuallanguage_model_that_runs"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T19:46:41Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["Henrie_the_dreamer"]
language: "en"
summary: "Hey all, Henry from Cactus Compute here. We released Mirage, a small vision model for phones, wearables, robots and other consumer devices. Mirage runs scene descriptions, object detection, OCR, segmentation, spatial relations and decisions, with a 22 MB weights file. Our end-to-end measurements on a Samsung Galaxy S26 are 74 ms on the NPU and 107 ms on its CPU, and descriptions support English,…"
tags: ["r/LocalLLaMA"]
orgs: ["Samsung", "Alibaba"]
topics: ["models & research", "chips & infrastructure", "robotics & autonomy"]
content_source: "post"
word_count: 473
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xpm8mw/mirage_a_22_mb_visuallanguage_model_that_runs/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Mirage: A 22 MB visual-language model that runs scene descriptions + object detection + OCR + segmentation + spatial relations analysis + extractions + decisions, in a single pass.

Reddit · Henrie_the_dreamer · 2026-11-06

Hey all, Henry from Cactus Compute here. We released Mirage, a small vision model for phones, wearables, robots and other consumer devices. Mirage runs scene descriptions, object detection, OCR, segmentation, spatial relations and decisions, with a 22 MB weights file. Our end-to-end measurements on a Samsung Galaxy S26 are 74 ms on the NPU and 107 ms on its CPU, and descriptions support English, German, French, Spanish, Italian, Dutch and Polish. For the architecture, Mirage has 51.3M parameters, including a 7.8M image encoder, a 40.8M language decoder and 2.6M in the OCR and spatial heads. The encoder uses HConvGLU, which mixes channels through fixed Hadamard transforms and small learned convolutions. Detection and masks share image features, while the decoder uses the Simple Attention and Hadamard MLP family behind Needle and Whistle. Our research at Cactus is kinda specific, hence these small models; we aim to compress intelligence to its smallest pragmatic form to run locally on everyday consumer hardware. With Mirage, our argument is that constructing prose, joining descriptions with connective language and generating open-ended reasoning spend capacity that a small model could use on the image itself. We put structure into the problem through spatial heads, a dedicated text reader and short references that connect names to regions. The decoder still produces names, properties, relations and a compact reasoning trace. The key finding is that passing Mirage's output to a text-only LLM might give give the LLM VLM abilities without fine-tuning. On 256 VQAv2 questions from 128 images, Qwen3-0.6B went from 9.3 with the question alone to 31.3 with Mirage's structured record and full trace, measured as VQA consensus credit out of 100. Neither model was fine-tuned. Another image's record scored 22.2 , and removing the trace scored 33.1 . The image-specific observations helped in this sample; we did not find a reliable benefit from the trace, the structured response was enough. This does not hold for every model though. Larger text-only models gave mixed results. With the same prompt and Mirage observations, the VQA scores were. Text model Question only Mirage record and trace Qwen3-1.7B 27.5 31.6 Qwen3-4B-Instruct-2507 33.4 37.3 These runs required a JSON object with a string-valued `answer`, and responses that broke that format received zero credit. With the record and trace, Nemotron failed that requirement on 214 of 256 responses, and Qwen3-1.7B on 34. The scores therefore mix answer correctness with format compliance. There were perception failures too. In one skateboard photo, Mirage missed the skateboard and described cars, people and shoes. Qwen guessed `a skateboard` from the question alone, then answered `a car` after reading Mirage's record and trace. A larger reader still needs the relevant observation to be present. We will try fine-tuning the reader on Mirage records paired with questions and short answers, and share findings, but let us know your thoughts. Mirage playground: https://cactuscompute.com/blog/mirage
