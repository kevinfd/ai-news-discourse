---
id: "e086e2a5c6055677"
title: "Memorilla: Latent Semantic Memory for LLMs"
url: "https://arxiv.org/abs/2610.21375"
link: "https://arxiv.org/abs/2610.21375"
source: "arXiv"
domain: "arxiv.org"
source_type: "community"
collector: "hackernews"
date: "2026-11-06T18:03:33Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["handfuloflight"]
language: "en"
summary: "Computer Science > Machine Learning\n  [Submitted on 15 Oct 2026 (v1), last revised 3 Nov 2026 (this version, v3)]\nTitle:Memorilla: Latent Semantic Memory for LLMs\nView PDF HTML (experimental)\n            Abstract:Memory enables large language models (LLMs) to use information beyond their parameters, such as past user conversations, long documents, or an agent's earlier actions. For a frozen LLM,…"
tags: ["r/singularity"]
orgs: ["Hugging Face"]
topics: ["agents & coding", "models & research", "search & media"]
content_source: "fulltext"
word_count: 481
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50395919"
score: 108
comments: 13
community: "Hacker News"
---

# Memorilla: Latent Semantic Memory for LLMs

arXiv · handfuloflight · 2026-11-06

Computer Science > Machine Learning
  [Submitted on 15 Oct 2026 (v1), last revised 3 Nov 2026 (this version, v3)]
Title:Memorilla: Latent Semantic Memory for LLMs
View PDF HTML (experimental)
            Abstract:Memory enables large language models (LLMs) to use information beyond their parameters, such as past user conversations, long documents, or an agent's earlier actions. For a frozen LLM, access to this accumulated knowledge is limited to what a memory system places in its context window. However, gathering and combining relevant information needed for each query while keeping the model's context short remains challenging for existing systems. Here we introduce Memorilla, a memory system that gathers information from an entire document collection into a fixed number of query-dependent 'memory tokens' for a frozen LLM. Memorilla encodes documents (such as user chats, book chapters) once into reusable embeddings, then learns to retrieve and place query-specific information in the LLM's input embedding space. Using only 16 memory tokens, Memorilla achieves the best performance against baselines including Mem0 and MemoRAG on five of eight benchmarks spanning personalization, long-document and knowledge-intensive question answering. Notably, on FactKG, it reaches 84.33% accuracy versus 80.43% with full-context inference, while using 108x fewer tokens to represent the source documents. Furthermore, Memorilla can facilitate continual learning in agentic systems where the document count (the agent's past turns) increases throughout the trajectory. In a TextWorld environment, we show that Memorilla reduces the agent's tendency to wander between rooms it has already explored, and improves its average success rate from 18.6% with full-history in-context learning to 24.2%. Overall, Memorilla aids frozen LLMs in accumulating and using knowledge effectively across long-context interactions and takes a step towards building continually learning AI systems.
    
Submission history
From: Vignesh Kothapalli [view email]
[v1] Thu, 15 Oct 2026 06:55:55 UTC (3,660 KB)
[v2] Tue, 27 Oct 2026 04:28:12 UTC (3,660 KB)
[v3] Tue, 3 Nov 2026 07:03:31 UTC (3,660 KB)
Additional Features
References & Citations
    
    Loading...
Bibliographic and Citation Tools
            Bibliographic Explorer (What is the Explorer?)
          
            Connected Papers (What is Connected Papers?)
          
            Litmaps (What is Litmaps?)
          
            scite Smart Citations (What are Smart Citations?)
          
Code, Data and Media Associated with this Article
            alphaXiv (What is alphaXiv?)
          
            CatalyzeX Code Finder for Papers (What is CatalyzeX?)
          
            DagsHub (What is DagsHub?)
          
            Gotit.pub (What is GotitPub?)
          
            Hugging Face (What is Huggingface?)
          
            ScienceCast (What is ScienceCast?)
          
Demos
Recommenders and Search Tools
              Influence Flower (What are Influence Flowers?)
            
              CORE Recommender (What is CORE?)
            
              IArxiv Recommender
              (What is IArxiv?)
            
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
