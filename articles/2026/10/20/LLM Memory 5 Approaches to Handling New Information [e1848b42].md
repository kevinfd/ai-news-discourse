---
id: "e1848b42d5dc2fdd"
title: "LLM Memory: 5 Approaches to Handling New Information"
url: "https://reddit.com/r/artificial/comments/1xavo5m/llm_memory_5_approaches_to_handling_new"
link: "https://reddit.com/r/artificial/comments/1xavo5m/llm_memory_5_approaches_to_handling_new"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T15:47:01Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["LimeOptimal539"]
language: "en"
summary: "Came across this article on HuggingFace around LLM memory. It goes beyond the conventional approach of “memory layer” which is limited only to what LLMs can do today. It also asks how much history LLMs can retain across various approaches, and what happens when new info conflicts with old state. The table groups approaches into five categories: Store more: keep explicit history, as with KV…"
tags: ["r/artificial"]
orgs: ["Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "post"
word_count: 343
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xavo5m/llm_memory_5_approaches_to_handling_new/"
score: null
comments: null
community: "r/artificial"
---

# LLM Memory: 5 Approaches to Handling New Information

Reddit · LimeOptimal539 · 2026-10-20

Came across this article on HuggingFace around LLM memory. It goes beyond the conventional approach of “memory layer” which is limited only to what LLMs can do today. It also asks how much history LLMs can retain across various approaches, and what happens when new info conflicts with old state. The table groups approaches into five categories: Store more: keep explicit history, as with KV caches and retrieval/RAG. Old and new information can coexist, leaving the system to resolve which applies at read/retrieval time. Compress: fold history into a fixed-size state, as with linear attention, RetNet, and Mamba. This saves space, but stored associations can interfere, limiting recall abilities as context grows. Correct: control what changes through gates or prediction-error updates, as with gated linear attention, mLSTM, and DeltaNet. Typically more efficient than simple “compress”, but also has a hard time scaling with larger contexts. Learn at inference: update mutable parameters using incoming evidence, as with TTT and Titans. Distribute plasticity: spread changes across interacting parts of the state, as with Dragon Hatchling (BDH). Memory lives in high-dimensional space, being sparse and distributed. One example that can make this easier for me to understand is a coding agent that learns a function signature has changed. Keeping both the old and new definitions means it has retained the information but it still needs to determine which definition should govern its next call. It becomes inefficient at reading time. I’m skeptical if the categories belong at the same level of comparison. Some describe model-level mechanisms, while others describe system-level designs. Curious how people here think about this, particularly those who've built memory systems for your own agents. When something becomes outdated, do you update the memory right away or keep the history and let the model figure it out during retrieval? Wondering which approach actually works better as the amount of information grows. Table and framework: R. Vimalkanth and T. Chudiwal, IIT Madras, “ The Missing Piece in LLM Memory: Why Long Context and Retrieval Aren’t Enough for Belief Revision ,” a HF community article.
