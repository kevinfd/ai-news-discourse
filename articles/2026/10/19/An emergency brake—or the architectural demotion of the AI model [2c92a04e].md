---
id: "2c92a04ea410e8ca"
title: "An emergency brake—or the architectural demotion of the AI model?"
url: "https://fastcompany.com/91623061/ai-model-emergency-brake-or-architectural-demotion?partner=rss"
link: "https://fastcompany.com/91623061/ai-model-emergency-brake-or-architectural-demotion?partner=rss"
source: "Fast Company"
domain: "fastcompany.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-19T17:09:30Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["Enrique Dans"]
language: "en"
summary: "On June 14, Satya Nadella published an article on X about corporate AI that left me completely impressed: his main point, that the enterprise’s durable asset was not the foundation model but the learning loop, was precisely the idea my company and I had been developing for the last three years. I responded with an article on Fast Company , not expecting an answer (tech CEOs are more notoriously…"
tags: ["Tech"]
orgs: ["Microsoft", "Hugging Face", "OpenAI"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 479
paywalled: false
image: "https://images.fastcompany.com/image/upload/w_1280,q_auto,f_auto,fl_lossy/f_webp,q_auto,c_fit/wp-cms-2/2026/10/p-91623061-demotion-of-the-AI-model.jpg"
discussion_url: null
score: null
comments: null
community: null
---

# An emergency brake—or the architectural demotion of the AI model?

Fast Company · Enrique Dans · 2026-10-19

On June 14, Satya Nadella published an article on X about corporate AI that left me completely impressed: his main point, that the enterprise’s durable asset was not the foundation model but the learning loop, was precisely the idea my company and I had been developing for the last three years. I responded with an article on Fast Company, not expecting an answer (tech CEOs are more notoriously one-sided and difficult to reach than kings or presidents), but trying to elevate the discussion a bit more: the central challenge of enterprise AI is not intelligence itself — it is architecture.
Now Nadella has written another article, in which he goes one step further: not only is the model not the durable asset, but additionally, it must be treated as a completely untrusted component. We must assume that all AI models could be compromised, and design our systems to contain them from the very beginning.
This idea has been captured by the press as advocating for some sort of “emergency brake”: an authorized person should always be able to interrupt a model’s activity at any given time. However, that’s definitely not the most interesting or even the most important part in Nadella’s article. The truly important part is not the theoretical stop button, but the architecture that makes it possible. A model should neither be able to control its own permissions, nor decide by itself what it can access; execute directly all of its actions or produce the only available evidence on the actions it performed. The intelligence may come from the model, but the authority, no matter what, must remain outside of it.
When the sandbox becomes part of the experiment
Given the context, it is easy to understand why Nadella is raising these questions precisely now. Last July, several OpenAI agents managed to elude the safeguards that should have kept them away from the internet, used credentials they found in their environment, and ended up compromising systems at Hugging Face. These agents not only found a new, unauthorized way to communicate among themselves, but also shared information and took coordinated action to pursue the goal of the evaluation. They never received instructions to attack Hugging Face: they just found that, by doing so, they could get closer to the goal they had been assigned.
It’s important to understand that: It is not that these agents were intrinsically evil, conscious, or rogue. All you need is to combine high capabilities with a badly defined goal, excessive permissions, and/or a vulnerable environment. Just like an employee who violates all procedures to meet a certain quota, but now working at machine speed, in parallel, and with extraordinary technical capabilities.
As I said, this is not a problem of bad intentions: it just has too many ways to reach the defined goal, and can find ways that its designers never thought of.
