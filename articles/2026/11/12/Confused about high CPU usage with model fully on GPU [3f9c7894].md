---
id: "3f9c7894f0ee98f2"
title: "Confused about high CPU usage with model fully on GPU"
url: "https://reddit.com/r/LocalLLaMA/comments/1xud7yq/confused_about_high_cpu_usage_with_model_fully_on"
link: "https://reddit.com/r/LocalLLaMA/comments/1xud7yq/confused_about_high_cpu_usage_with_model_fully_on"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T13:49:14Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["randomjapaneselearn"]
language: "en"
summary: "EDIT: FOUND THE REASON, LLAMA DIDN'T OFFLOAD ALL LAYERS TO GPU BECAUSE -ngl -1 DOESN'T MEAN ALL see here: https://www.reddit.com/r/LocalLLaMA/comments/1xun196/solved_high_cpu_usage_when_model_fit_in_gpu/ I'm not sure if i'm doing something wrong and handicapping myself with some wrong setting. I'm using Windows, nVidia 3090 24GB VRAM, 64GB RAM, Qwen 3.8 27B and Swift 1.5 27B (finetune of qwen)…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["chips & infrastructure", "models & research", "products & launches"]
content_source: "post"
word_count: 297
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xud7yq/confused_about_high_cpu_usage_with_model_fully_on/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Confused about high CPU usage with model fully on GPU

Reddit · randomjapaneselearn · 2026-11-12

EDIT: FOUND THE REASON, LLAMA DIDN'T OFFLOAD ALL LAYERS TO GPU BECAUSE -ngl -1 DOESN'T MEAN ALL see here: https://www.reddit.com/r/LocalLLaMA/comments/1xun196/solved_high_cpu_usage_when_model_fit_in_gpu/ I'm not sure if i'm doing something wrong and handicapping myself with some wrong setting. I'm using Windows, nVidia 3090 24GB VRAM, 64GB RAM, Qwen 3.8 27B and Swift 1.5 27B (finetune of qwen) but i often see 50% CPU usage even if the model is fully loaded on GPU , below there is my command line. Another problem i noticed is that llama-fit-params suggest that 131k context fit but if i launch it for real in the log i see that it doesn't load everything on gpu (all but one), i forced it to load everything on gpu with -ngl -1 (i'm also using llama-swap). on launch it say that "cahe resue 256" will not be used but it might help with other models so i left it there. Another problem is that when the model is doing nothing i sometimes see 130W gpu in idle (wrong) and some other times its at 10-18W (correct) i can't find what is causing this... Current stats: about 40 t/s in token generation I have no idea what KMP affinity is but i read it online, tried, it helped with 35A3B so i left it there in general i'm looking for tips to improve my launch arguments, note that temperature and few others are set by pidev but i'm using the recommended one on the model card. If the model is fully on GPU why there is a high CPU usage? but not always which is even more confusing.... set KMP_AFFINITY=granularity=fine,compact,1,0 llama-bin-win-cuda-13.4-x64\llama-server.exe -m Qwen3.8-27B-UD-Q4_K_M.gguf --ctx-size 131072 -ctk q8_0 -ctv q8_0 -ngl -1 -fa on --spec-type draft-mtp --spec-draft-n-max 2 -np 1 -b 4096 -ub 1024 --cache-reuse 256 --cache-ram 32768 --jinja
