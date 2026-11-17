---
id: "2fadee92459bcdcc"
title: "Thinking Machines 4-bit replication: I trained a GPT end to end with a 4-bit forward pass on one B200"
url: "https://reddit.com/r/LocalLLaMA/comments/1xyawzz/thinking_machines_4bit_replication_i_trained_a"
link: "https://reddit.com/r/LocalLLaMA/comments/1xyawzz/thinking_machines_4bit_replication_i_trained_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T04:19:51Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["OtherRaisin3426"]
language: "en"
summary: "Thinking Machines wrote last week that Inkling 2 Small was trained with a native 4-bit forward pass. I wanted to check this for myself. What I ran: 1x B200 on Modal, PyTorch 2.8, plus a small CUDA library that calls cuBLASLt's real NVFP4 and FP8 matmuls on raw pointers, loaded with ctypes Forward pass in NVFP4 (4-bit values with one scale per 16), backward pass in FP8 with stochastic rounding,…"
tags: ["r/LocalLLaMA"]
orgs: ["Thinking Machines"]
topics: ["models & research"]
content_source: "post"
word_count: 276
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xyawzz/thinking_machines_4bit_replication_i_trained_a/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Thinking Machines 4-bit replication: I trained a GPT end to end with a 4-bit forward pass on one B200

Reddit · OtherRaisin3426 · 2026-11-17

Thinking Machines wrote last week that Inkling 2 Small was trained with a native 4-bit forward pass. I wanted to check this for myself. What I ran: 1x B200 on Modal, PyTorch 2.8, plus a small CUDA library that calls cuBLASLt's real NVFP4 and FP8 matmuls on raw pointers, loaded with ctypes Forward pass in NVFP4 (4-bit values with one scale per 16), backward pass in FP8 with stochastic rounding, master weights in high precision GPT at widths 2,048, 4,096 and 8,192 (219M, 840M, 3.3B parameters) on TinyStories Results: 4-bit training finished faster. On the 840M model, 2,000 training steps took about 5.5 minutes in normal 16-bit (BF16) and about 4.3 minutes with a 4-bit forward pass. I ran each twice and got nearly the same times. The model learned just as well. Final validation loss was about 1.69 either way (1.688 for 16-bit, 1.691 for 4-bit). A difference that small is noise at this scale. Bigger models gain more. Each training step was 18% faster on the 219M model, 28% faster on the 840M model and 38% faster on the 3.3B model. Two things to improve: Blackwell's convert instruction rounds exact ties toward zero, while my software reference rounded to even. Tiny difference, but it breaks bit-for-bit checks until you know. PyTorch's attention backward is not bit-repeatable, so any test that compares gradients across runs has to leave attention out. Not tested: multiple GPUs, MoE dispatch and combine, Four Over Six, MXFP8 block scales in the backward pass. The width-8,192 run is only 1,000 steps and undertrained. Write-up with every figure: https://4bit.vizuara.ai Code: https://github.com/VizuaraAI/4bit-training-b200 3-hour walkthrough from first principles, if you want the theory: https://youtu.be/a3nV32Guxcc
