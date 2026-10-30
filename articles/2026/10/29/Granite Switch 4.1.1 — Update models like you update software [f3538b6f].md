---
id: "f3538b6fb36f4f58"
title: "Granite Switch 4.1.1 — Update models like you update software"
url: "https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1"
link: "https://huggingface.co/blog/ibm-granite/granite-switch-4-1-1"
source: "Hugging Face"
domain: "huggingface.co"
source_type: "company_blog"
collector: "rss"
date: "2026-10-29T13:37:07Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Kate Soule", "Luis A Lastras", "Subhajit Chaudhury", "Abraham Daniels"]
language: "en"
summary: "Granite Switch 4.1.1 — Update models like you update software\nJust over a week ago, we released Granite Switch 4.1, showing that our modular Switch architecture lets you configure a language model with specialized, cache-efficient adapters — adding new expertise on a single endpoint.\nGranite Switch 4.1.1 is a patch release. The version number means what it means in software: fully backwards…"
tags: []
orgs: ["IBM"]
topics: ["products & launches", "models & research"]
content_source: "fulltext"
word_count: 236
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Granite Switch 4.1.1 — Update models like you update software

Hugging Face · Kate Soule, Luis A Lastras, Subhajit Chaudhury, Abraham Daniels · 2026-10-29

Granite Switch 4.1.1 — Update models like you update software
Just over a week ago, we released Granite Switch 4.1, showing that our modular Switch architecture lets you configure a language model with specialized, cache-efficient adapters — adding new expertise on a single endpoint.
Granite Switch 4.1.1 is a patch release. The version number means what it means in software: fully backwards compatible with 4.1, no migration, incremental improvements under the hood.
- Updated Granite Speech ASR model — multilingual speech-to-text across 10 languages with native punctuation and capitalization, so transcripts are ready for downstream models without a formatting pass.
- Updated Decision adapter in granitelib-core — featuring improved overall performance on the Jev Decision Index test set.
While we are excited about these new features, what is notable is the speed and efficiency with which our teams could release this update. Apart from training the new ASR model and Decision adapter, nothing was recomputed: the base model is untouched. You compose the latest adapters you want and deploy.
This pattern can power far more than patch releases to an IBM-provided model. We're working on tutorials and an Adapter SDK so developers and third-party providers can build their own adapters — iterate on versions, test features, and ship updates the way you ship software. More soon.
Until then, test out our latest models, and try out the new multilingual and punctuation capabilities powering our Speech-to-Decisions demo.
