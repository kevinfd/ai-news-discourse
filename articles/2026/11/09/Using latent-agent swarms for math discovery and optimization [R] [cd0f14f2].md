---
id: "cd0f14f2d016000d"
title: "Using latent-agent swarms for math discovery and optimization [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xrunu7/using_latentagent_swarms_for_math_discovery_and"
link: "https://reddit.com/r/MachineLearning/comments/1xrunu7/using_latentagent_swarms_for_math_discovery_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T15:30:50Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["QileHQ"]
language: "en"
summary: "Last year Google DeepMind's AlphaEvolve found a faster way to multiply 4x4 complex matrices, beating a record that had stood since 1969. The idea is to let an LLM write a program, score it, and iteratively improve it. So it's called \" evolve \". But AlphaEvolve runs on Gemini models. Similar open-source implementations are also usually slow and expensive. We tried to make it faster, cheaper, and…"
tags: ["r/MachineLearning"]
orgs: ["Google"]
topics: ["models & research", "agents & coding", "health & science"]
content_source: "post"
word_count: 282
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xrunu7/using_latentagent_swarms_for_math_discovery_and/"
score: null
comments: null
community: "r/MachineLearning"
---

# Using latent-agent swarms for math discovery and optimization [R]

Reddit · QileHQ · 2026-11-09

Last year Google DeepMind's AlphaEvolve found a faster way to multiply 4x4 complex matrices, beating a record that had stood since 1969. The idea is to let an LLM write a program, score it, and iteratively improve it. So it's called " evolve ". But AlphaEvolve runs on Gemini models. Similar open-source implementations are also usually slow and expensive. We tried to make it faster, cheaper, and better. SwarmEvolve is our new paper, a scalable framework for math discovery and optimization. We run swarms of hundreds of latent-reasoning agents on Qwen3 8B, 14B and 32B. In ~5 minutes, they reach scores that took OpenEvolve, ShinkaEvolve and CodeEvolve >1 hour. Here's how: Inspired by recent works in LatentMAS, our agents never write out their thoughts. They reason in latent space and pass KV caches to each other, so ideas from different agents mix right inside the model. This massively improved throughput. Small agents are cheap, so we can run a lot of them, each with a different focus, organized in swarms. More agents means more diverse ideas each round, more exploration of the solution space, and the swarm finds good programs much faster. It works at every model size we tried. With just the 8B model, it even matched the best known circle packing. Framework has been extended to work with Qwen3.5 and Muse models as well, showing even better performance. Paper: https://www.alphaxiv.org/abs/2611.08483 Code (available soon): https://github.com/Qile-J/SwarmEvolve Let me know if this makes sense or not. Also I'm really interested in apply such "evolve" frameworks on real scientific discovery problems - material science, biology, etc - so if anyone has any ideas for next steps / collaboration, I'm open to hear about it!
