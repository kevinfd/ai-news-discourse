---
id: "99487c74cfd6f86f"
title: "Looking for some help optimizing for a 300-page manual and transcripts"
url: "https://reddit.com/r/LocalLLaMA/comments/1xuwowk/looking_for_some_help_optimizing_for_a_300page"
link: "https://reddit.com/r/LocalLLaMA/comments/1xuwowk/looking_for_some_help_optimizing_for_a_300page"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T03:00:37Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["sacheltry"]
language: "en"
summary: "Hello, I am just getting started and I got great answers to my previous post asking what was possible . I still have lots to learn but, with the help of Claude, I was able to get something running and it is working pretty well. My goal as been to build a fully local AI study assistant to analyze a ~300-page technical training manual alongside instructor transcripts and generate chapter-based…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic", "Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 394
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xuwowk/looking_for_some_help_optimizing_for_a_300page/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Looking for some help optimizing for a 300-page manual and transcripts

Reddit · sacheltry · 2026-11-13

Hello, I am just getting started and I got great answers to my previous post asking what was possible . I still have lots to learn but, with the help of Claude, I was able to get something running and it is working pretty well. My goal as been to build a fully local AI study assistant to analyze a ~300-page technical training manual alongside instructor transcripts and generate chapter-based study guides and Quizlet flashcards with accurate page citations. The problem is: I'm running into is this error: request (34009 tokens) exceeds the available context size (32768 tokens). And this was after doing lots of tweaking and getting it not fail at 16,000 tokens. There are so many settings and configurations that I might be able to change to improve that, but it is overwhelming and I have no idea what to do. I would really appreciate any ideas, suggestions that I can do to get this working for what I am trying to achieve. Or let me know that it isn't possible. Here's my setup (sorry, AI slop to make it clearer): Hardware: Windows 11 PC: i7-14700K, 64GB RAM, RTX 4070 SUPER (12GB VRAM) Unraid server: Core Ultra 9 285K, 32GB RAM, RTX 5070 Ti (16GB VRAM) Software / Models: llama.cpp (CUDA, router mode) Open WebUI 0.12.3 Qwen3.6-35B-A3B UD-Q4_K_XL: Main model, context increased from 32K to 64K Gemma 4 12B Q4_K_M: Secondary model Both models run on the Windows PC. RAG configuration: Open WebUI Knowledge Base with the PDF and Markdown transcripts Embeddings: bge-m3 (1024 dimensions), hosted on Unraid Reranker: bge-reranker-v2-m3 on Unraid (API working; Open WebUI integration unverified) Focused Retrieval, chunk size 1000, overlap 100, Top K = 3 All inference and document processing must remain local. More details on the issue: Basic RAG questions work well. However, when I ask the model to analyze an entire chapter, cross-reference relevant trainer discussions, and create 15–25 Quizlet flashcards, I encounter context errors as I said above: request (34009 tokens) exceeds the available context size (32768 tokens) Increasing Qwen's configured context to 64K eliminated the immediate context error, but generation then stopped halfway through creating flashcards without an obvious error. I haven't confirmed whether an output-token limit caused this. I've tried reducing retrieval results, using smaller prompts, and starting fresh chats. These help, but I'd prefer a more automated and comprehensive workflow. Thank you!
