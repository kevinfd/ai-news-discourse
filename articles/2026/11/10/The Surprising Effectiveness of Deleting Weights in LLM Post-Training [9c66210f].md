---
id: "9c66210f6a51f5ee"
title: "The Surprising Effectiveness of Deleting Weights in LLM Post-Training"
url: "https://arxiv.org/abs/2611.10866"
link: "https://arxiv.org/abs/2611.10866"
source: "arXiv"
domain: "arxiv.org"
source_type: "community"
collector: "hackernews"
date: "2026-11-10T22:44:49Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["theanonymousone"]
language: "en"
summary: "How little of a pretrained large language model (LLM) has to change for it to acquire new capabilities? We find that zeroing fewer than 0.05% of its weights, with no other modification, matches full fine-tuning (FFT) at scale across three LLM post-training regimes: reinforcement learning with verifiable rewards, supervised fine-tuning, and on-policy distillation. Our method, Deletion Tuning,…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face"]
topics: ["models & research", "business & funding", "policy & regulation", "search & media"]
content_source: "fulltext"
word_count: 359
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50447363"
score: 25
comments: 0
community: "Hacker News"
---

# The Surprising Effectiveness of Deleting Weights in LLM Post-Training

arXiv · theanonymousone · 2026-11-10

Computer Science > Machine Learning
  [Submitted on 7 Nov 2026]
Title:The Surprising Effectiveness of Deleting Weights in LLM Post-Training
View PDF HTML (experimental)
            Abstract:How little of a pretrained large language model (LLM) has to change for it to acquire new capabilities? We find that zeroing fewer than 0.05% of its weights, with no other modification, matches full fine-tuning (FFT) at scale across three LLM post-training regimes: reinforcement learning with verifiable rewards, supervised fine-tuning, and on-policy distillation. Our method, Deletion Tuning, learns a binary mask over the gate projection of transformer blocks. Two practical advantages follow: the trained mask is hundreds to thousands of times smaller than the corresponding FFT checkpoint, and Deletion Tuning forgets far less, which addresses a central challenge in continual learning. Under reinforcement learning, its prior-task accuracy stays near the base level while FFT, LoRA, and random sparse fine-tuning lose up to 5.4 points. To understand why masking alone suffices, we analyze the geometry of the learned weight changes under reinforcement learning using stable rank, spectrum drift, and principal-weight overlap. Compared with LoRA and random sparse fine-tuning, Deletion Tuning is closest to FFT across the three measures.
    
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
