---
id: "b00bd35ef821f48b"
title: "Moving a running model's layers between GPUs mid-reply (8 ms, no re-prefill)"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5i7o9/moving_a_running_models_layers_between_gpus"
link: "https://reddit.com/r/LocalLLaMA/comments/1x5i7o9/moving_a_running_models_layers_between_gpus"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T04:40:53Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["web3samy"]
language: "en"
summary: "I've been working on an inference engine called jitllm. The idea came from my background in operating systems and JIT compilers: generate kernels for whatever hardware is there, and treat layers a bit like processes the engine can place and move around. In the video, a cloud VM with T4s: mid-reply, all layers of Llama-3.2-3B move from one GPU to the other and back. And my puny laptop where the…"
tags: ["r/LocalLLaMA"]
orgs: ["Meta"]
topics: ["chips & infrastructure", "models & research"]
content_source: "post"
word_count: 217
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5i7o9/moving_a_running_models_layers_between_gpus/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Moving a running model's layers between GPUs mid-reply (8 ms, no re-prefill)

Reddit · web3samy · 2026-10-14

I've been working on an inference engine called jitllm. The idea came from my background in operating systems and JIT compilers: generate kernels for whatever hardware is there, and treat layers a bit like processes the engine can place and move around. In the video, a cloud VM with T4s: mid-reply, all layers of Llama-3.2-3B move from one GPU to the other and back. And my puny laptop where the model is split across CPU, CUDA and Vulkan (iGPU), rearranged while it's generating. The KV cache is paged and moves with the layers, so the prompt isn't re-processed and the output matches a run that didn't move. Hardware Model Move Pause Recomputed 2× T4 Llama-3.2-3B Q4_K_M GPU 0 → GPU 1 8.1 ms 0 tokens 2× T4 Llama-3.2-3B Q4_K_M GPU 1 → GPU 0 8.4 ms 0 tokens 2× V100 Llama-3.2-3B, 1.8k-token chat GPU 0 → GPU 1 20–21 ms 0 tokens RTX 3050 Ti laptop Llama-3.2-1B Q4_K_M CUDA → Vulkan 91 ms 0 tokens What excites me is the room the design leaves. Generated kernels mean every improvement reaches every machine, and the engine can fuse and tune for hardware it has never seen. Paging and relocation turn placement into scheduling: models bigger than memory, mismatched GPUs, work that shifts as conversations grow. Code -> https://github.com/jitllm/jitllm
