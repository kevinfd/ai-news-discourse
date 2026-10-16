---
id: "84f4bcc51f991ccb"
title: "5 Fun Projects for LLM Inference Engineering"
url: "https://kdnuggets.com/5-fun-projects-for-llm-inference-engineering"
link: "https://kdnuggets.com/5-fun-projects-for-llm-inference-engineering"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-10-14T12:00:00Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Kanwal Mehreen"]
language: "en"
summary: "Want to understand what makes LLMs fast? Build the systems yourself."
tags: []
orgs: ["OpenAI", "Meta", "Nvidia", "Apple", "Hugging Face", "Alibaba"]
topics: ["models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 984
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/5-Fun-Projects-for-LLM-Inference-Engineering.png"
discussion_url: null
score: null
comments: null
community: null
---

# 5 Fun Projects for LLM Inference Engineering

KDnuggets · Kanwal Mehreen · 2026-10-14

5 Fun Projects for LLM Inference Engineering
Want to understand what makes LLMs fast? Build the systems yourself.
Training large language models gets most of the attention, but once a model is trained, another engineering problem begins: how do you serve it quickly and efficiently?
LLM inference engineering focuses on reducing latency, increasing throughput, lowering memory consumption, and getting more useful work from the available hardware. This involves techniques such as KV caching, continuous batching, quantization, prefix caching, speculative decoding, optimized attention kernels, and distributed inference. The best way to learn these concepts is not by reading about them individually — it is by building something and seeing what happens. In this article, we will look at 5 projects that progressively introduce the most important ideas behind modern LLM inference systems.
1. Building a Mini-vLLM From Scratch
If you want one project that exposes you to almost the entire inference stack, this is probably the best place to start. Nano-vLLM is a small educational implementation of a vLLM-style inference engine, with its core implementation small enough to actually read. It includes scheduling, KV-cache block management, prefix caching, tensor parallelism, CUDA graphs, and other optimizations while using a real Qwen model. Instead of simply cloning it and running the example, rebuild one component at a time: first perform normal autoregressive generation, then add KV caching, then batching, then block-based KV-cache allocation. Benchmark tokens per second after every addition. By the end, you will understand concepts like PagedAttention and continuous batching in a much better way.
2. Writing Your Own FlashAttention Kernel With Triton
A normal attention implementation uses large matrices and repeatedly moves data between GPU memory and fast on-chip memory. FlashAttention restructures the computation to reduce that memory traffic. Triton's official tutorial provides an implementation of a FlashAttention-style fused attention kernel, making it a great starting point for learning kernel-level optimization. This video also builds FlashAttention from scratch while explaining HBM versus SRAM, arithmetic intensity, tiling, online softmax, benchmarking, and finally integrating the kernel into an inference engine. I would recommend it to those who prefer video-based learning. This project teaches you that making an LLM faster is not always about doing fewer mathematical operations. Sometimes it is about moving less data.
3. Building an LLM Quantization Lab
Take one small open model and run several versions — for example FP16, INT8, and 4-bit. Measure model size, peak memory, model-load time, time to first token (TTFT), tokens per second, and quality on a small evaluation set. Hugging Face supports multiple quantization approaches, including AWQ, GPTQ, bitsandbytes-based 8-bit and 4-bit loading, and several newer formats. llama.cpp also supports a wide range of low-bit quantization formats and runs across CPUs, Apple Silicon, NVIDIA GPUs, and several other hardware backends. For an extra challenge, quantize both the weights and KV cache and see whether using fewer bits always improves latency or not.
4. Implementing Speculative Decoding
Speculative decoding is one of the most enjoyable inference optimizations to implement. Instead of asking the expensive target model to generate every token sequentially, a smaller draft model proposes several candidate tokens. The target model then verifies those candidates together. Choose a small target/draft pair, implement normal autoregressive decoding as the baseline, and then build the draft-and-verify loop. Track not only tokens per second but also acceptance rate — which is the percentage of draft tokens accepted by the target model. Then experiment with drafting 2, 4, 6, or 8 tokens at a time. The Columbia high-performance machine learning project experiments with both speculative decoding and quantization using the Llama model family while evaluating latency, throughput, perplexity, and code-generation quality. An interesting extension is to test different workloads. Code, repetitive text, factual question-answering, and creative writing can produce very different draft acceptance behavior.
5. Building Your Own Production LLM Inference Service
The final project is a capstone where we combine KV caching, quantization, batching, and benchmarking into a single system. Start with a basic OpenAI-compatible inference endpoint. Deploy it on a GPU. Add streaming. Add load testing. Instrument TTFT and token-generation latency. Introduce quantization. Experiment with speculative decoding. Add prefix caching. Push concurrency higher and identify what breaks first. The Time to First Token project provides an interesting structure for doing this. Its roadmap revolves around continuously improving one inference service rather than completing disconnected exercises. It covers deployment, instrumentation, heavy concurrency testing, quantization, speculative decoding, routing, and reproducible benchmarking. For an even harder extension, add a request router that decides which model or GPU should process each request based on queue length, expected generation length, or latency requirements.
Wrapping Up
You need enough machine learning knowledge to understand transformers and attention, but many of the hardest problems have surprisingly little to do with training models. They involve memory allocation, scheduling, batching, caching, kernel optimization, networking, load testing, and figuring out how to keep very expensive hardware busy.
This is why building projects is such a good way to learn the field.
Start by generating one token inefficiently. Add a KV cache. Batch several users together. Break the cache into pages. Quantize the weights. Let a smaller model speculate about future tokens. Write a GPU kernel. Then put everything behind an API and bombard it with requests. By the time you finish, tools such as vLLM and SGLang will no longer feel like black boxes. You will have built smaller versions of many of the ideas that make them fast.
 
Kanwal Mehreen is a machine learning engineer and a technical writer with a profound passion for data science and the intersection of AI with medicine. She co-authored the ebook "Maximizing Productivity with ChatGPT". As a Google Generation Scholar 2022 for APAC, she champions diversity and academic excellence. She's also recognized as a Teradata Diversity in Tech Scholar, Mitacs Globalink Research Scholar, and Harvard WeCode Scholar. Kanwal is an ardent advocate for change, having founded FEMCodes to empower women in STEM fields.
