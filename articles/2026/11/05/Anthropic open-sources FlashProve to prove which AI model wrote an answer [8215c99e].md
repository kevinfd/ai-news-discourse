---
id: "8215c99e39b6536b"
title: "Anthropic open-sources FlashProve to prove which AI model wrote an answer"
url: "https://thenextweb.com/news/anthropic-flashprove-provable-inference-ai-model-identity"
link: "https://thenextweb.com/news/anthropic-flashprove-provable-inference-ai-model-identity"
source: "The Next Web"
domain: "thenextweb.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-05T06:26:00Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Ana Maria Constantin"]
language: "en"
summary: "Anthropic has released FlashProve, an open-source prototype that proves a reply came from a committed AI model. It can check a 400bn-parameter model on a single H100 chip."
tags: []
orgs: ["Anthropic", "Meta", "OpenAI", "Nvidia"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 447
paywalled: false
image: "http://www.bing.com/th?id=ONUT.e1qK4txyGPdrSkLnGtUdMg&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic open-sources FlashProve to prove which AI model wrote an answer

The Next Web · Ana Maria Constantin · 2026-11-05

Anthropic has released FlashProve, an open-source prototype that lets anyone check that an AI reply came from the model a provider says it used. The company published the code, a technical report and formal proofs in a research post on Monday.
Today a user cannot tell whether a router quietly swapped in a cheaper model, or whether an attacker tampered with the replies. FlashProve tackles this with “provable inference”. The provider publishes a fingerprint of its model weights. Each reply then comes with a cryptographic proof that those weights produced it.
The proof reveals nothing about the weights themselves, Anthropic said. That matters for labs such as Anthropic and OpenAI, which keep their weights private.
“This research post is meant to share intermediate progress, and not a completed research agenda.” Anthropic
How fast it is
FlashProve uses a type of zero-knowledge proof called a zkSNARK. Anthropic tested it on Meta’s open Llama 4 Maverick, a 400bn-parameter mixture-of-experts model. A single Nvidia H100 produced proofs at about 110 tokens a second, with a proof of about 19MB for each 1,024-token request.
That is 70 to 95 times the GPU time of running the model normally, Anthropic said. Checking a proof takes about 17 seconds on an ordinary CPU, with no GPU and no access to the weights. The only earlier proof of the same model took 14.3 hours for 1,000 tokens, according to the post.
Claude helped build the system, Anthropic said. Because Claude’s choices can be hard to audit, the team wrote the key security guarantees as machine-checked proofs in Lean, a formal verification language. The code is released under the Apache 2.0 licence.
Uses and limits
Anthropic sees several uses. Independent evaluators, who already test labs’ models, could confirm they are testing the model being served. Customers of routing services could check they got the model they paid for, not a cheaper or distilled one. Labs have accused rivals of distillation campaigns this year.
Regulators could also check that a provider’s chips were serving approved models. That links the work to Dario Amodei’s call to pace the frontier of AI.
The prototype has clear limits. It handles contexts of only 1,024 tokens, far below what chatbots use. It works only with mixture-of-experts models, and it hides the weights but not the model’s design. It does not cover timing attacks either.
There are no plans to deploy it at Anthropic or any other lab, TechCrunch reported. Anthropic said it met its own goal on verifying model outputs through a separate project, which signs its traffic and rechecks it on a trusted server.
Get the TNW newsletter
Get the most important tech news in your inbox each week.
