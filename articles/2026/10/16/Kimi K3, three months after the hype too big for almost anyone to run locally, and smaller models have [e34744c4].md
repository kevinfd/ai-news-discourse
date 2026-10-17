---
id: "e34744c4ede484c8"
title: "Kimi K3, three months after the hype: too big for almost anyone to run locally, and smaller models have already caught it"
url: "https://reddit.com/r/LocalLLaMA/comments/1x7s89u/kimi_k3_three_months_after_the_hype_too_big_for"
link: "https://reddit.com/r/LocalLLaMA/comments/1x7s89u/kimi_k3_three_months_after_the_hype_too_big_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T21:14:31Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["Sanbi_Ai"]
language: "en"
summary: "K3 came out in July hyped as the best open model you could download, and it scored 57 on Artificial Analysis, right up there with Opus 4.8 and GPT-5.5. I went back to see what running it actually looks like now, using Unsloth's quant docs, the model card, AA and the license. Short version: it's still a monster, and the field caught up. Full model is 1.56 TB. 104B active doesn't save you any…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI", "Anthropic", "DeepSeek", "Alibaba", "China"]
topics: ["models & research"]
content_source: "post"
word_count: 393
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x7s89u/kimi_k3_three_months_after_the_hype_too_big_for/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Kimi K3, three months after the hype: too big for almost anyone to run locally, and smaller models have already caught it

Reddit · Sanbi_Ai · 2026-10-16

K3 came out in July hyped as the best open model you could download, and it scored 57 on Artificial Analysis, right up there with Opus 4.8 and GPT-5.5. I went back to see what running it actually looks like now, using Unsloth's quant docs, the model card, AA and the license. Short version: it's still a monster, and the field caught up. Full model is 1.56 TB. 104B active doesn't save you any memory, all 2.8T params still have to be loaded. Smallest quant Unsloth recommends is 594 GB and wants about 610 GB of RAM+VRAM. It doesn't fit in 512 GB, and Unsloth say they're still trying to get it under. 1-bit agrees with the full model on the next token 79% of the time. 2-bit gets you to 90%, but that's 861 GB. About 20 tok/s on B200s if it fits in memory. If not, it offloads to disk and crawls. It's now 44 on AA's index. Most of that drop is AA changing the index, not the model, but GLM-5.3 (753B) now scores 45 and Step 5 Preview (600B) ties it at 44. Slow on the API too. 43 tok/s on Kimi's own API, and on AA's agentic benchmark it averaged almost an hour and over $10 per task. The bit people miss is the license. It isn't MIT. If your company runs any model-as-a-service business and makes more than $20M in total over any 12 months, you need a separate deal with Moonshot before using K3 commercially, even if K3 itself makes you nothing. Caveat: AA tests the full model at max reasoning through the API. I couldn't find real task benchmarks for the 1-bit quant, so 79% token agreement is a proxy, not a quality score. So... is anyone actually running K3 at home? And if you had 600 GB to play with, would you take 1-bit K3 or something like GLM-5.3 at a much higher quant? PS: I'm a co-founder of Sanbi.ai, where we track how AI assistants like ChatGPT, Claude and more choose and cite sources for brands, and we're expanding into Chinese models, which is why I've been digging into Kimi, DeepSeek and Qwen lately. Happy to talk about how these models search if anyone's curious. The open-weight side is something I follow as an engineer, so this one was more curiosity than work.
