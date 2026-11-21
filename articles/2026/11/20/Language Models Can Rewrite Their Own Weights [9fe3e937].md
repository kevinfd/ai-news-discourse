---
id: "9fe3e937f57a6930"
title: "Language Models Can Rewrite Their Own Weights"
url: "https://arxiv.org/abs/2611.21885"
link: "https://arxiv.org/abs/2611.21885"
source: "arXiv"
domain: "arxiv.org"
source_type: "community"
collector: "hackernews"
date: "2026-11-20T16:29:06Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["lwhsiao"]
language: "en"
summary: "Computer Science > Artificial Intelligence\n  [Submitted on 16 Nov 2026 (v1), last revised 18 Nov 2026 (this version, v2)]\nTitle:Language Models Can Rewrite Their Own Weights\nView PDF HTML (experimental)\n            Abstract:A language model is trained once and frozen. Making it better takes another training run, or a prompt, a harness or extra computation at inference that is gone once the task…"
tags: []
orgs: ["Hugging Face"]
topics: ["models & research", "search & media"]
content_source: "fulltext"
word_count: 541
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50577265"
score: 429
comments: 126
community: "Hacker News"
---

# Language Models Can Rewrite Their Own Weights

arXiv · lwhsiao · 2026-11-20

Computer Science > Artificial Intelligence
  [Submitted on 16 Nov 2026 (v1), last revised 18 Nov 2026 (this version, v2)]
Title:Language Models Can Rewrite Their Own Weights
View PDF HTML (experimental)
            Abstract:A language model is trained once and frozen. Making it better takes another training run, or a prompt, a harness or extra computation at inference that is gone once the task ends. We show a third way: to our knowledge for the first time, a language model rewrites its own weights by its own reasoning and becomes better, with no gradients and no training. We call this self-rewriting: the model is its own optimizer. In earlier work, a frontier model edited a much smaller one; here an open 27B model, given its weights, its graded answers and the ability to run itself, diagnoses its own failure and rewrites the weights behind it. It surpasses itself: its own edit makes it 6.6 points more accurate on problems it never saw. It keeps getting better: it tests its edits on practice problems and submits only what works, each edit improving on the last, and over eight consecutive sessions its accuracy only rises. It repairs a damaged copy of itself, like a broken robot that fixes itself without being rebuilt: the copy solves almost nothing, yet with no retraining and without ever reading the original weights, the model brings it back to over 80% of the original accuracy on image tasks it never saw. And the ability emerges with scale: in one model family, the smaller models make no edit or break themselves, and only the largest improves and repairs itself. Unlike test-time scaling, self-rewriting writes its gain into the weights, at no cost per answer; unlike training, it runs only forward passes, as serving does. The wall between training and inference is a limit of our tools, not a property of intelligence. We believe self-rewriting is a necessary step toward recursive self-improvement: a model that, like a human, does not separate training from inference could keep upgrading itself for life, with no larger model, no harness or prompt engineering, and no pre- or post-training.
    
Submission history
From: Jiajun Fan [view email]
[v1] Mon, 16 Nov 2026 20:55:08 UTC (6,363 KB)
[v2] Wed, 18 Nov 2026 08:57:59 UTC (6,379 KB)
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
