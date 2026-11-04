---
id: "993e48dc4504c6f5"
title: "Anthropic is working on a system to prove AI models’ identity"
url: "https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity"
link: "https://techcrunch.com/2026/11/03/anthropic-is-working-on-a-system-to-prove-ai-models-identity"
source: "TechCrunch"
domain: "techcrunch.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-03T22:41:03Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Russell Brandom"]
language: "en"
summary: "Called FlashProve, the system would let anyone check that an AI response really came from the model it claims to be from."
tags: ["AI", "Anthropic", "cryptography", "inference"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 404
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic is working on a system to prove AI models’ identity

TechCrunch · Russell Brandom · 2026-11-03

Anthropic is working on an open source system to verify which AI model produced a given output, according to a blog post published Tuesday. The system, called FlashProve, is built to provide what researchers call “provable inference” — a cryptographic proof, essentially a mathematical guarantee, that a given output came from a specific model. It’s meant to let users confirm that the answer they received really came from the model they think they’re using.
Similar to cryptographic email signatures that let recipients confirm a message really came from its claimed sender, FlashProve would be robust against impostors attempting to disguise one model as another, even when the impostor is the lab that built and runs the model. In particular, the researchers note that the system could be used to prevent an AI company from secretly swapping in a cheaper model to cut costs, or a more expensive model to inflate its performance results.
FlashProve could also be used to verify claims by third parties that a specific task was done by an advanced model. “A developer might claim that their software library was scanned for vulnerabilities by a frontier cybersecurity model, or a company might claim that its business plan was given the go-ahead by an appropriate model,” the researchers write. “How can a user verify these claims?”
To work, the system requires AI labs to publish a “fingerprint” of each model they release that can later be matched to specific outputs and verified cryptographically. Crucially, the fingerprints don’t reveal a model’s weights, the internal numbers that define how it behaves and which closed-model makers like Anthropic and OpenAI keep private. That means labs could publish the fingerprints without giving up their most valuable asset, enabling the system to work with commercial models, too. The system is also designed to be lightweight, so verification could be performed on a local device.
As part of the announcement, researchers released a detailed technical specification and working code for various elements of the system, which is publicly available under an open source license on GitHub. Research in the system is ongoing, and there are no plans to deploy it at Anthropic or any other lab.
“This research post is meant to share intermediate progress, and not a completed research agenda,” researchers explain in the announcement post. “We are sharing this explicitly with the goal that others look at what we have done, take it, and improve it.”
