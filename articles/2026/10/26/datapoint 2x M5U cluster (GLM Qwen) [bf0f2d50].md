---
id: "bf0f2d50b0a6d99c"
title: "datapoint: 2x M5U cluster (GLM/Qwen)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xfybhu/datapoint_2x_m5u_cluster_glmqwen"
link: "https://reddit.com/r/LocalLLaMA/comments/1xfybhu/datapoint_2x_m5u_cluster_glmqwen"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T14:26:27Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Viktri1"]
language: "en"
summary: "Caveats: IDK how to set anything up and I asked Deepseek to handle it - not enough training data so without specific guides the set up doesn't work well. I'm not a programmer. My previous model was Qwen 3.8 27B q4 using ninfer. Was getting around 1.4k prefill and 100-120 tokens decode. Just want to provide data for anyone interested in purchasing M5U 256gb (80 cores) x 2. And if you have…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 206
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xfybhu/datapoint_2x_m5u_cluster_glmqwen/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# datapoint: 2x M5U cluster (GLM/Qwen)

Reddit · Viktri1 · 2026-10-26

Caveats: IDK how to set anything up and I asked Deepseek to handle it - not enough training data so without specific guides the set up doesn't work well. I'm not a programmer. My previous model was Qwen 3.8 27B q4 using ninfer. Was getting around 1.4k prefill and 100-120 tokens decode. Just want to provide data for anyone interested in purchasing M5U 256gb (80 cores) x 2. And if you have suggestions on how to optimize my set up I'd really appreciate it. GLM 5.3 flash q6 cluster: prefill 4.9k (idk if this is right but this is what the LLM says, two thunderbolt 5 cables), decode: 50 tok/s. oMLX set up with Deepseek API. Qwen Flash Next q6 cluster: prefill 8k and decode 200 using Tensorfold. I copied their guide, sent it to Deepseek, and asked it to set it up. GLM flash was too slow for me so I am using Qwen Flash Next. I am using Hermes as the harness (hermes has deepseek harness as research agent and Pi harness for coding agent). I am wondering whether using a different harness with less context overhead would make things faster or if since it is mostly context it doesn't really make a difference.
