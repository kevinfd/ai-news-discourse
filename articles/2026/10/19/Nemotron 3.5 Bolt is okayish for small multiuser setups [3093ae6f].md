---
id: "3093ae6f41989a96"
title: "Nemotron 3.5 Bolt is okayish for small multiuser setups"
url: "https://reddit.com/r/LocalLLaMA/comments/1x9lkh5/nemotron_35_bolt_is_okayish_for_small_multiuser"
link: "https://reddit.com/r/LocalLLaMA/comments/1x9lkh5/nemotron_35_bolt_is_okayish_for_small_multiuser"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T02:48:40Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["1ncehost"]
language: "en"
summary: "https://preview.redd.it/0tljsfsl7cwh1.png?width=349&format=png&auto=webp&s=4428c2ab4743ce471d2862eef502ffa38381c8d3 I have been shopping for a faster model than 27B for a workload that Nemotron Ultra was doing well at. Ultra was pretty underwhelming since it came out, as there have been smaller models that are better, but its been free on openrouter, so why not use it if it works? Bolt is at…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 475
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x9lkh5/nemotron_35_bolt_is_okayish_for_small_multiuser/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Nemotron 3.5 Bolt is okayish for small multiuser setups

Reddit · 1ncehost · 2026-10-19

https://preview.redd.it/0tljsfsl7cwh1.png?width=349&format=png&auto=webp&s=4428c2ab4743ce471d2862eef502ffa38381c8d3 I have been shopping for a faster model than 27B for a workload that Nemotron Ultra was doing well at. Ultra was pretty underwhelming since it came out, as there have been smaller models that are better, but its been free on openrouter, so why not use it if it works? Bolt is at first glance another model that should be passed over as well. It does have some impressive quantization, but its nothing to write home about when 27B is around, much less Flash Next. However, it was just the right size for my 128 GB setup (4x MI100), as it was designed for Sparks, so I took a look at it. A few interesting facts about Bolt: The decoders are 2 bit quantized, and other more sensitive parts are NVFP4 in the stock model. There are other quants in the model, but those are most of the weights. It has 1 layer of full attention (GQA) for every 5 layers of linear attention (Mamba2), which is a lower ratio than Qwen3 which has 4 layers of linear for every 1 layer of full. Its attention is much less wide than Qwen3, so a 30k context is only 200 MB, compared to 500 MB for Flash Next, and 952 MB for 27B. A 256k context is 1 GB for Bolt, compared to 3.4 GB for FN, and 8.5 GB for 27B. The new Nemotron Super has identical attention, so same numbers. As far as I've seen, these new Nemotrons are the most efficient KV caches of new models except for DS v4.1 Flash. It is basically a REAP-ed Nemotron 3.5 Super with additional post training Its intelligence isn't great by today's standards, but it is about the same as Qwen3.6 27B, so not bad. One place it does shine relatively is non-hallucination rate, which is better than some top models. In my testing, this means it tends to wander in thought over many turns, running lots of diagnostics and checks before trying solutions and testing them thoroughly. https://preview.redd.it/1od8gwpw1cwh1.png?width=573&format=png&auto=webp&s=6ca23fce924f8e89bb2c53b4f7fafe4cceb1405b Its reasonably fast so far; about double 27B on my hardware. Where most of the model is just adequate, the place it stands out is it can fit a lot of context into memory, and also a large prefix cache too. This means Bolt is good for small multiuser scenarios like at small businesses. You can realistically fit millions of context tokens into memory, and a single 5090 (with native NVFP4 and 32 GB of memory) or one of the 128 GB SFF is probably the ideal hardware for this model. Its an interesting model, and I hope more like it are released. It certainly has been a long time waiting for a 70B model to pop up again. I'll be testing it some more, but it seems decent so far and I recommend it.
