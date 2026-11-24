---
id: "8f20e5199f558b31"
title: "Latent Introspection: LLMs Can Detect Prior Concept Injections"
url: "https://arxiv.org/abs/2602.20031"
link: "https://arxiv.org/abs/2602.20031"
source: "arXiv"
domain: "arxiv.org"
source_type: "community"
collector: "hackernews"
date: "2026-11-23T22:29:48Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["joecobb"]
language: "en"
summary: "Computer Science > Artificial Intelligence\n  [Submitted on 23 Feb 2026 (v1), last revised 7 Nov 2026 (this version, v3)]\nTitle:Latent Introspection: Models Can Detect Prior Concept Injections\nView PDF HTML (experimental)\n            Abstract:We uncover a latent capacity for introspection in a Qwen 32B model, demonstrating that the model can detect when concepts have been injected into its…"
tags: []
orgs: ["Hugging Face", "Alibaba"]
topics: ["models & research", "search & media"]
content_source: "fulltext"
word_count: 368
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50620328"
score: 68
comments: 5
community: "Hacker News"
---

# Latent Introspection: LLMs Can Detect Prior Concept Injections

arXiv · joecobb · 2026-11-23

Computer Science > Artificial Intelligence
  [Submitted on 23 Feb 2026 (v1), last revised 7 Nov 2026 (this version, v3)]
Title:Latent Introspection: Models Can Detect Prior Concept Injections
View PDF HTML (experimental)
            Abstract:We uncover a latent capacity for introspection in a Qwen 32B model, demonstrating that the model can detect when concepts have been injected into its earlier context and identify which concept was injected. While the model denies injection in sampled outputs, logit lens analysis reveals clear detection signals in the residual stream, which are attenuated in the final layers. Furthermore, prompting the model with accurate information about AI introspection mechanisms can dramatically strengthen this effect: the sensitivity to injection increases massively (0.3% -> 39.9%) with only a 0.6% increase in false positives. Also, mutual information between nine injected and recovered concepts rises from 0.61 bits to 1.05 bits, ruling out generic noise explanations. Our results demonstrate models can have a surprising capacity for introspection and steering awareness that is easy to overlook, with consequences for latent reasoning and safety.
    
Submission history
From: Martin VanÄ›k [view email]
[v1] Mon, 23 Feb 2026 16:39:42 UTC (977 KB)
[v2] Thu, 26 Feb 2026 12:43:02 UTC (998 KB)
[v3] Sat, 7 Nov 2026 10:50:14 UTC (1,144 KB)
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
            
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
