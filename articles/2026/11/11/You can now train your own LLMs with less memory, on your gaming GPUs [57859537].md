---
id: "5785953773a669da"
title: "You can now train your own LLMs with less memory, on your gaming GPUs"
url: "https://reddit.com/r/LocalLLaMA/comments/1xtgnh9/you_can_now_train_your_own_llms_with_less_memory"
link: "https://reddit.com/r/LocalLLaMA/comments/1xtgnh9/you_can_now_train_your_own_llms_with_less_memory"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T12:36:21Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["oguzeldereli"]
language: "en"
summary: "TL;DR: You can train your own 27B model on a 3090 with 24GB VRAM, though you would have to go through hundreds of billions of tokens for it to be good. I am working on conversion of existing models. Check repos for code and the paper if you are interested in more. I have a 40.4GB Qwen Flash Next GGUF Hi, I do AI research. I have been working on an optimizer that doesn't need the ~16 bytes of…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 568
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xtgnh9/you_can_now_train_your_own_llms_with_less_memory/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# You can now train your own LLMs with less memory, on your gaming GPUs

Reddit · oguzeldereli · 2026-11-11

TL;DR: You can train your own 27B model on a 3090 with 24GB VRAM, though you would have to go through hundreds of billions of tokens for it to be good. I am working on conversion of existing models. Check repos for code and the paper if you are interested in more. I have a 40.4GB Qwen Flash Next GGUF Hi, I do AI research. I have been working on an optimizer that doesn't need the ~16 bytes of VRAM per weight to train a model that AdamW does. I focused on training ternary networks bcs BitNet (Ma et al.) shows they match full precision quality in large scales. The problem is BitNet also keeps the full precision weights during training which means you still need to use the same amount of memory. I got this down from 16 bytes to 1 byte or even less per weight. For you, this means, you can train your own 10-20B parameter models on your consumer GPUs. I fitted 27B model training on a single 24GB 3090 and a 23B model on a 16GB GPU. The trained model costs ~1.6 bits per weight (~6GB at 27B), 10x smaller than 16bit, and 5x smaller than Q8. I have also been working on converting existing models and training them. This is harder and I am still working on it but I have some promising results. I quantized and trained a Qwen3.8 27B though the file I published below has adapters which are about 2GBs, pushing the file size to 8GB. I am also making a no-adapter version right now. It scores GSM8K 0.895, the same as full precision, HumanEval 0.84 vs 0.93 and runs on a 12 GB GPU at ~2 3 tok/s on my crippled 12GB laptop 4080, though this number can heavily be improved with custom kernels, engineering, etc. I will leave it to you guys to help me with that too. I also quantized and trained Qwen Flash Next down to 40.4 GBs including its n-gram table (at 8GB). It largely retains the skills of the network (scores equivalent on GSM8K benchmark, a little behind on HumanEval, I unfortunately don't have compute for the larger benchmarks such as TerminalBench2.1 but perhaps some of you can help me out) but forgets facts. It mostly works fine if you give it web search as far as my experience goes but this is not strictly measured. To add to that, these models are not extremely good, they sometimes loop, and suck at remembering facts. However, unlike unsloth's gguf's you can actually keep training them yourself, in that sense they are pure, and you can train them on your consumer GPUs, that is to say you can get rid of the looping behavior, teach it facts that you want it to know, or specialize it for some purpose. I am still doing work on this and I will keep working on it, perhaps even for many years. The code is open for non-commercial use. Check out: The core repo for training: https://github.com/oguzeldereli/ttf-ternary The repo for conversion: https://github.com/oguzeldereli/ttf-conversion Repo for running models trained by ttf: https://github.com/oguzeldereli/ttf-home GGUF for a converted Qwen 3.8 27B (around 8 GB and 6.7GB): https://huggingface.co/oguzeldereli/ttf-Qwen3.8-27B-GGUF GGUF for a converted Qwen 3.8 Flash Next (around 40.4GB): https://huggingface.co/oguzeldereli/ttf-Qwen3.8-Flash-Next-GGUF I will convert a Qwen 4 27B instance when it drops. Full paper: https://github.com/oguzeldereli/ttf-ternary/blob/main/paper/ttf_paper1_training.pdf Also, I would appreciate github stars if you like the project.
