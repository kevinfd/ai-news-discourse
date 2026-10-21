---
id: "710212fb2d26a0ef"
title: "3M token pool for Nemotron 3.5 Super on a single RTX PRO 6000"
url: "https://reddit.com/r/LocalLLaMA/comments/1xaz9cs/3m_token_pool_for_nemotron_35_super_on_a_single"
link: "https://reddit.com/r/LocalLLaMA/comments/1xaz9cs/3m_token_pool_for_nemotron_35_super_on_a_single"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T17:59:01Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["TechNerd10191"]
language: "en"
summary: "I installed https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 last night and tried it today with SGLang and can easily have a 3M token pool which means 4 concurrent requests, all with ~750k tokens each. While benchmark figures are lagging behind Qwen3.8-Flash-Next, Nemotron 3.5 Super does not use any system memory (no 50GB lookup table), is slightly faster (150 to 250…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["models & research", "chips & infrastructure", "jobs & society"]
content_source: "post"
word_count: 216
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xaz9cs/3m_token_pool_for_nemotron_35_super_on_a_single/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# 3M token pool for Nemotron 3.5 Super on a single RTX PRO 6000

Reddit · TechNerd10191 · 2026-10-20

I installed https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 last night and tried it today with SGLang and can easily have a 3M token pool which means 4 concurrent requests, all with ~750k tokens each. While benchmark figures are lagging behind Qwen3.8-Flash-Next, Nemotron 3.5 Super does not use any system memory (no 50GB lookup table), is slightly faster (150 to 250 tps tg vs 130 to 230 tps for 3.8 FN) and, most importantly, the tokens, as Qwen3.8 FN only allows for a ~450k token pool. Plus, I appreciate it Nemotron has native 1M context. The SGLang server arguments I used are the following. Note that CUDA graphs for prefill do not work (only decode does). args=( --model-path "$MODEL_PATH" --served-model-name "$MODEL_NAME" --host 127.0.0.1 --port 8000 --device cuda --random-seed 42 --trust-remote-code --cuda-graph-backend-prefill breakable --enable-multimodal --stream-interval 1 --tokenizer-worker-num 1 --detokenizer-worker-num 1 --mem-fraction-static 0.95 --context-length 786432 --kv-cache-dtype fp8_e4m3 --max-running-requests 4 --prefill-max-requests 4 --max-queued-requests 2 --chunked-prefill-size 4096 --max-prefill-tokens 32768 --page-size 1 --radix-eviction-policy lfu --reasoning-parser nemotron_3 --tool-call-parser qwen3_coder --cuda-graph-max-bs-decode 4 --cuda-graph-max-bs-prefill 4096 --enable-cudagraph-gc --sampling-backend flashinfer --mm-attention-backend flashinfer_cudnn --prefill-attention-backend flashinfer --decode-attention-backend flashinfer --linear-attn-decode-backend flashinfer --linear-attn-prefill-backend flashinfer --mamba-backend flashinfer --mamba-ssm-dtype bfloat16 --mamba-radix-cache-strategy extra_buffer_lazy --mamba-track-interval 256 --max-mamba-cache-size 16 --fp8-gemm-backend cutlass --fp4-gemm-backend flashinfer_cutlass --moe-runner-backend flashinfer_cutlass --speculative-algorithm EAGLE --speculative-num-steps 5 --speculative-eagle-topk 1 --speculative-num-draft-tokens 6 --speculative-moe-runner-backend flashinfer_cutlass --preferred-sampling-params '{ "temperature": 1.0, "top_p": 0.95, "top_k": 20, "min_p": 0.0, "presence_penalty": 0.0, "repetition_penalty": 1.0 }' )
