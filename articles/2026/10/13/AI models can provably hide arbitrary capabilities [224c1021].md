---
id: "224c102190be4dc2"
title: "AI models can provably hide arbitrary capabilities"
url: "https://arxiv.org/abs/2610.13928"
source: "arXiv"
domain: "arxiv.org"
source_type: "community"
collector: "hackernews"
date: "2026-10-13T02:07:08Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["sbulaev"]
language: "en"
summary: "Computer Science > Machine Learning\n  [Submitted on 9 Oct 2026]\nTitle:AI Models Can Provably Hide Arbitrary Capabilities\nView PDF HTML (experimental)\n            Abstract:Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under…"
tags: []
orgs: ["Hugging Face"]
topics: ["models & research", "search & media"]
content_source: "fulltext"
word_count: 345
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50065692"
score: 268
comments: 135
community: "Hacker News"
---

# AI models can provably hide arbitrary capabilities

arXiv · sbulaev · 2026-10-13

Computer Science > Machine Learning
  [Submitted on 9 Oct 2026]
Title:AI Models Can Provably Hide Arbitrary Capabilities
View PDF HTML (experimental)
            Abstract:Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under cryptographic assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations. We implement our proof of concept constructions in PyTorch and evaluate elicitation through fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training on a small chemical reaction prediction task - a proxy for CBRN-relevant capabilities. Our results demonstrate resistance to these methods and, together with our cryptographic guarantees, reveal a limit of elicitation-based capability audits. We release our models to support the improvement of defenses.
    
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
