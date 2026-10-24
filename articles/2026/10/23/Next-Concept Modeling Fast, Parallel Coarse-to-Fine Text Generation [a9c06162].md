---
id: "a9c06162812cf7ad"
title: "Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation"
url: "https://arxiv.org/abs/2610.14162"
link: "https://arxiv.org/abs/2610.14162"
source: "Lobsters"
domain: "arxiv.org"
source_type: "community"
collector: "rss"
date: "2026-10-23T17:25:34Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["arxiv.org via Yogthos"]
language: "en"
summary: "Comments"
tags: ["ai"]
orgs: ["Hugging Face"]
topics: ["models & research", "search & media"]
content_source: "fulltext"
word_count: 363
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation

Lobsters · arxiv.org via Yogthos · 2026-10-23

Computer Science > Computation and Language
  [Submitted on 9 Oct 2026]
Title:Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation
View PDF HTML (experimental)
            Abstract:Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and require many passes over the dataset to reach good quality. We introduce Next-Concept Modeling (NCM), a two-stage, coarse-to-fine framework: a multiscale residual VQ-VAE encodes text into a hierarchy of discrete codes, and a transformer generates one level at a time, predicting all codes within a level in parallel. At matched parameter scales, NCM achieves better generative perplexity than the strongest DLM baseline on LM1B while running $21\times$ faster. On OpenWebText, NCM is competitive with the strongest DLM while running $10\times$ faster; on XSum, it matches the strongest DLM's ROUGE-L while being $31\times$ faster. On the reasoning task of Sudoku, NCM outperforms autoregressive and diffusion baselines across all difficulty levels, using fewer function evaluations. On the reasoning task of Sudoku, NCM outperforms autoregressive and diffusion baselines across all difficulty levels, using fewer function evaluations.
    
Additional Features
Current browse context:
cs.CL
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
