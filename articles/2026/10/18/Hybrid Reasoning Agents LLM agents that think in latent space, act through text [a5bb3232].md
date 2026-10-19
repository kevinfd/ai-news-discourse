---
id: "a5bb32320853f4db"
title: "Hybrid Reasoning Agents: LLM agents that think in latent space, act through text"
url: "https://arxiv.org/abs/2610.18861"
link: "https://arxiv.org/abs/2610.18861"
source: "arXiv"
domain: "arxiv.org"
source_type: "community"
collector: "hackernews"
date: "2026-10-18T20:48:14Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["allinonai"]
language: "en"
summary: "https://x.com/Jiaru_Zou/status/2110400256647340476 https://github.com/togethercomputer/HybridAgent https://huggingface.co/collections/togethercomputer/hybridag... Evaluations: https://arxiv.org/html/2610.18861v1#S5"
tags: []
orgs: ["Hugging Face"]
topics: ["models & research", "agents & coding", "search & media", "health & science"]
content_source: "fulltext"
word_count: 395
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50145337"
score: 432
comments: 214
community: "Hacker News"
---

# Hybrid Reasoning Agents: LLM agents that think in latent space, act through text

arXiv · allinonai · 2026-10-18

Computer Science > Computation and Language
  [Submitted on 13 Oct 2026]
Title:Hybrid Reasoning Agents
View PDF HTML (experimental)
            Abstract:How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge these two directions with Hybrid Reasoning Agents (HybridAgents), which dynamically navigate between latent reasoning and text-based interaction throughout a unified generation process. Architecturally, a lightweight HybridLink enables seamless transitions between text and latent modes, while the agent's continuous working memory preserves lossless hybrid context across multiple turns. These designs preserve tool-integrated agentic capabilities while making latent thoughts directly inspectable. Building on this architecture, we further develop dedicated post-training algorithms for hybrid reasoning: HybridSFT stabilizes tool-integrated hybrid generation by teaching the backbone to coordinate with HybridLink, then HybridRL scales reasoning by learning when to think in latent space and when to act through text. We evaluate HybridAgent at 3 model scales across 11 benchmarks covering mathematics, science, medicine, search, and agentic reasoning. Compared with frontier LLM Agents and agentic frameworks spanning both text-based and latent methods, HybridAgent consistently improves performance by 10.4%, while delivering 35.5%-54.7% token reduction, 1.8x-2.6x faster inference, and 2.7x-3.7x cost savings. Code and data are available at this https URL.
    
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
