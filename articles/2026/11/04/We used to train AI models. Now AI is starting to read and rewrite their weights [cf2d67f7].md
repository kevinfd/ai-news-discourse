---
id: "cf2d67f7385eb4ab"
title: "We used to train AI models. Now AI is starting to read and rewrite their weights."
url: "https://reddit.com/r/ArtificialInteligence/comments/1xo0zre/we_used_to_train_ai_models_now_ai_is_starting_to"
link: "https://reddit.com/r/ArtificialInteligence/comments/1xo0zre/we_used_to_train_ai_models_now_ai_is_starting_to"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-04T21:48:56Z"
published_date: "2026-11-04"
collected_at: "2026-11-05T13:04:25Z"
authors: ["Powermadlux"]
language: "en"
summary: "I’ve been thinking about what happens when the weights of a trained AI model stop being just the end result of training and become something another AI can inspect and modify. On November 2, researchers from MIT CSAIL reported experiments where GPT-6 Astra inferred what some small neural networks had learned by examining their weights. In a separate experiment, it used tools and test runs to…"
tags: ["r/ArtificialInteligence"]
orgs: ["OpenAI", "Alibaba"]
topics: ["models & research"]
content_source: "post"
word_count: 253
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xo0zre/we_used_to_train_ai_models_now_ai_is_starting_to/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# We used to train AI models. Now AI is starting to read and rewrite their weights.

Reddit · Powermadlux · 2026-11-04

I’ve been thinking about what happens when the weights of a trained AI model stop being just the end result of training and become something another AI can inspect and modify. On November 2, researchers from MIT CSAIL reported experiments where GPT-6 Astra inferred what some small neural networks had learned by examining their weights. In a separate experiment, it used tools and test runs to edit a small Qwen model and reduce a reasoning-loop problem. It’s early research, and the experiments have very specific limits. But the implications are fascinating. For years, the story felt like it went in one direction: training data goes in, the weights are created, and the model produces responses. Now we’re starting to explore the other direction. Could we eventually look at the weights and infer more about what shaped a model? Not just what it can do, but something about the data or training process behind it? And if we can modify the weights after training, how precisely could we change its behavior? Could we correct a specific problem without affecting everything else? Could someone change how a model responds without its users knowing? I’m not saying this research has solved those questions. To me, it feels like the beginning of opening a very large Pandora’s box. I wrote a short working paper exploring these questions. If anyone is interested, I can share it. What do you think is more consequential: being able to read what’s inside a trained model, or being able to rewrite it?
