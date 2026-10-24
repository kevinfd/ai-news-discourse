---
id: "513b83e21d390cf0"
title: "I pretrained an efficient SLM for you to finetune for specialised tasks."
url: "https://reddit.com/r/LocalLLaMA/comments/1xddmfu/i_pretrained_an_efficient_slm_for_you_to_finetune"
link: "https://reddit.com/r/LocalLLaMA/comments/1xddmfu/i_pretrained_an_efficient_slm_for_you_to_finetune"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T13:10:35Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Nameis19letterslong"]
language: "en"
summary: "tl;dr in caveman: I make small model, you take small model, shape small model into thing you like. I pretrained a tiny ass SLM on ~5.7B token. Model specs and stuff It’s a sparse 11M MoE with a 7.28M Backbone (Active 5.52M, top-1 routing out of 2 experts) and 4.21M ngrams. It‘s not on the Open SLM Leaderboard yet but it would rank top 64% overall, top 47.4% for sub 50M models and top 37.6% for…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 376
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xddmfu/i_pretrained_an_efficient_slm_for_you_to_finetune/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I pretrained an efficient SLM for you to finetune for specialised tasks.

Reddit · Nameis19letterslong · 2026-10-23

tl;dr in caveman: I make small model, you take small model, shape small model into thing you like. I pretrained a tiny ass SLM on ~5.7B token. Model specs and stuff It’s a sparse 11M MoE with a 7.28M Backbone (Active 5.52M, top-1 routing out of 2 experts) and 4.21M ngrams. It‘s not on the Open SLM Leaderboard yet but it would rank top 64% overall, top 47.4% for sub 50M models and top 37.6% for sub 10M models. Doesn’t sound impressive but it’s a sparse model with a thick embedding (makes up ~3M of model, so actual active FFN is only 2M). Another hidden benefit of it is that it comes with a modest 2048 context window, as compared to the 256/512 context in models of similar size. Purpose of this? This model is essentially a base for you to use. The corpus used is a pretrain set that targets a mix of everything, such as general knowledge, chat, maths, tool calling, instruct and code. This makes it easier to adapt it to a specialist or specific task, such as summarisation, code autocomplete, routing models or text classification. Basically it removes the need to ride the hype train of a bajillion new repetitive model releases (cough cough Jev) and can be more accurate on your specific workflows as long as you are willing to throw in some compute to train it. How do I finetune it? Recently I've open sourced my entire training pipeline. It's a high level (low level settings can still be accessed) + minimal setup training engine designed for training SLMs (<1b tested). It uses Cuda and is optimised for Blackwell 2.0 (50 series and Blackwell pro) but CPU has full parity. All you need is to download the model checkpoint, throw in a dataset, and then train it for a few minutes to a few hours. I'll train an example autocomplete model sometime soon. If you want to get started, the quickstart guide (~5mins) is on the bottom of the Huggingface model card. Or maybe give me some ideas for a use case, and I'll make like 2-3 finetunes for the model as a demo. Links: Detailed model benchmarks and descriptions: Post on r/LocalLMtraining Huggingface: https://huggingface.co/Dsg2/LS-Micro-Base Training + inference engine: https://github.com/Dsg2/cudalm-c
