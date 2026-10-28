---
id: "816708e4ebe4e9b1"
title: "I built a PyTorch optimizer for large GPU workloads — looking for feedback[P]"
url: "https://reddit.com/r/MachineLearning/comments/1xgqtxp/i_built_a_pytorch_optimizer_for_large_gpu"
link: "https://reddit.com/r/MachineLearning/comments/1xgqtxp/i_built_a_pytorch_optimizer_for_large_gpu"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T12:11:26Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Ready_Parking_5435"]
language: "en"
summary: "Hey, I've been working on a PyTorch optimizer called ApexW and figured I'd share it here to get some feedback from people who know more about this stuff than I do. The main goal is to reduce optimizer-state memory usage and see how much faster I can make optimizer steps on larger GPU workloads. I've been experimenting with compact optimizer states and a Triton-based execution path. In my current…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 397
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xgqtxp/i_built_a_pytorch_optimizer_for_large_gpu/"
score: null
comments: null
community: "r/MachineLearning"
---

# I built a PyTorch optimizer for large GPU workloads — looking for feedback[P]

Reddit · Ready_Parking_5435 · 2026-10-27

Hey, I've been working on a PyTorch optimizer called ApexW and figured I'd share it here to get some feedback from people who know more about this stuff than I do. The main goal is to reduce optimizer-state memory usage and see how much faster I can make optimizer steps on larger GPU workloads. I've been experimenting with compact optimizer states and a Triton-based execution path. In my current tests, the Triton + compact-state path was around 1.5x faster than PyTorch's fused AdamW on workloads with a few large tensors, and the optimizer-state memory usage was roughly cut in half. The results aren't all good, though. Those numbers are from optimizer-only benchmarks, not full model training. The automatic execution mode doesn't consistently get the same speedup yet, and workloads with lots of small tensors are much slower than PyTorch's fused optimizer. So I'm definitely not claiming this is a better AdamW replacement for every workload. I want to test it on more realistic models and different GPUs, and I'd appreciate a second pair of eyes on both the implementation and the benchmarks. the Reality Check (The Trade-Offs) I want to be completely realistic here—this is an engineering trade-off, not magic: Python Loop Overhead on Small Tensors: When testing a layout with many tiny tensors ( many-small test), ApexW’s Triton kernels suffer heavily from Python's launch latency. For example, at 128M parameters spread across many small tensors, PyTorch native was 16.1 ms/step while ApexW compact was 76.0 ms/step (~0.21x speedup). If your model is composed of many tiny layers, standard PyTorch is significantly better. End-to-End Impact: While the optimizer step itself is up to 1.5x faster, this step only represents a fraction of a full training step (which is dominated by forward and backward passes). In my end-to-end MLP test, PyTorch still runs slightly faster overall because of C++ deep integration. Why/When should you care? If you are training larger deep learning models (like Transformers or LLM fine-tuning) where you are constantly hitting Out-Of-Memory (OOM) barriers,**,**cutting your optimizer state memory strictly in half lets you increase your batch size or scale up your model size without upgrading your hardware. GitHub: https://github.com/omen42515-prog/apexw/tree/main If you've worked on PyTorch optimizers, Triton kernels, or training larger models, I'd be interested to hear what you think. Especially curious if there's an obvious issue with my benchmark setup or an important test I'm missing.
