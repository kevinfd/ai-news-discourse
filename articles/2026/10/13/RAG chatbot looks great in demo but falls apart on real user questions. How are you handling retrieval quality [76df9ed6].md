---
id: "76df9ed649884647"
title: "RAG chatbot looks great in demo but falls apart on real user questions. How are you handling retrieval quality?"
url: "https://reddit.com/r/artificial/comments/1x4suc4/rag_chatbot_looks_great_in_demo_but_falls_apart"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T10:16:41Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Sad_Lavishness_53"]
language: "en"
summary: "Working on a RAG based support bot for a client project and hit a wall I did not expect. On our test questions it looks great, but real users type messy stuff like half sentences, typos, and questions that need info from 2 or 3 different docs. Retrieval keeps pulling the wrong chunks and the model then answers confidently anyway. What we have tried so far: Smaller chunks with overlap (helped a…"
tags: ["r/artificial"]
orgs: []
topics: ["models & research", "policy & regulation", "search & media"]
content_source: "post"
word_count: 136
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1x4suc4/rag_chatbot_looks_great_in_demo_but_falls_apart/"
score: null
comments: null
community: "r/artificial"
---

# RAG chatbot looks great in demo but falls apart on real user questions. How are you handling retrieval quality?

Reddit · Sad_Lavishness_53 · 2026-10-13

Working on a RAG based support bot for a client project and hit a wall I did not expect. On our test questions it looks great, but real users type messy stuff like half sentences, typos, and questions that need info from 2 or 3 different docs. Retrieval keeps pulling the wrong chunks and the model then answers confidently anyway. What we have tried so far: Smaller chunks with overlap (helped a bit, but hurt on long policy docs) Hybrid search (BM25 plus embeddings), which was the biggest improvement so far A reranker on the top 20 results (better quality, but adds latency) Still struggling with multi-doc questions, and with getting the bot to say "I don't know" instead of guessing. Has anyone found a reliable way to evaluate this without manually reading hundreds of outputs?
