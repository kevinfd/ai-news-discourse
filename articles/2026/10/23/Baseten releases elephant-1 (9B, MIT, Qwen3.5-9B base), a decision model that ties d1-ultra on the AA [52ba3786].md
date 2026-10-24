---
id: "52ba3786ebb675cc"
title: "Baseten releases elephant-1 (9B, MIT, Qwen3.5-9B base), a decision model that ties d1-ultra on the AA Decision Index at about a quarter of the cost"
url: "https://reddit.com/r/LocalLLaMA/comments/1xdirky/baseten_releases_elephant1_9b_mit_qwen359b_base_a"
link: "https://reddit.com/r/LocalLLaMA/comments/1xdirky/baseten_releases_elephant1_9b_mit_qwen359b_base_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T16:26:41Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Balance-"]
language: "en"
summary: "Base Labs at Baseten has released open weights for elephant-1, a 9B decision model post-trained from Qwen3.5-9B. It doesn't generate text. You give it a state (a ticket, a document, a prompt to screen) and a set of yes/no, multiple-choice or ordered-score questions, and it returns a probability for every option, read straight off the option-letter logits. All questions share one prefill of the…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "safety & ethics"]
content_source: "post"
word_count: 453
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xdirky/baseten_releases_elephant1_9b_mit_qwen359b_base_a/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Baseten releases elephant-1 (9B, MIT, Qwen3.5-9B base), a decision model that ties d1-ultra on the AA Decision Index at about a quarter of the cost

Reddit · Balance- · 2026-10-23

Base Labs at Baseten has released open weights for elephant-1, a 9B decision model post-trained from Qwen3.5-9B. It doesn't generate text. You give it a state (a ticket, a document, a prompt to screen) and a set of yes/no, multiple-choice or ordered-score questions, and it returns a probability for every option, read straight off the option-letter logits. All questions share one prefill of the state, so each extra question only costs a forward pass over its own short suffix. Artificial Analysis evaluated it independently and scored it 65 on their Decision Index, tied with d1-ultra. elephant-1 costs about $8 per 1M tasks against roughly $31 for d1-ultra. That index is an equal-weight blend of AA-Omniscience-Decision (knowledge and hallucination), HLE-MultiChoice, When2Call and WildGuardTest. On the Jev Decision Index 0.4 it scores 62.65, the best result under 15B and tied for #8 of 208. Its 27B sibling, mammoth-1, is #1 at 71.24. The per-benchmark breakdown shows where the score comes from. It gets 95 on When2Call and 93 on WildGuardTest. On Omniscience it has a 93 non-hallucination rate but only 12 accuracy, so it says "I don't know" a lot rather than guessing. That was trained for deliberately, but it means this isn't a model for obscure-fact recall. Routing, guardrails, tool-call gating and LLM-as-judge at volume look like the sweet spot. Architecturally, the GDN layers stay causal. The causal mask on the full-attention layers is swapped for a block-bidirectional one, so the question block can see all of its options and the prefix cache can be reused across questions. The report claims 48.6 vs 44.8 over causal with the data held fixed, but that is a single run. According to the report, most of the gains came from data. The training mix has 6.21M examples: 58% core decision skills, 16% safety and abstention, 16% judging and expert domains, and 10% converted public datasets. Synthetic sources went through a 5-judge labelling panel that needed 4 of 5 to agree, then decontamination, agent review for answer giveaways, and short pilot training runs. Growing the mix 16× took their public Jev score from 45.5 to 66.0, and auditing and repairing all 253 sources added most of the remaining ~8 points. The loss is cross-entropy plus a Brier term, with a trained "I don't know" option, run for one epoch on 128 H100s. Self-hosting needs a single CUDA GPU via the included setup.sh . Max context is 16k, and longer requests are refused rather than truncated. It's also free on Baseten's API, with zero data retention, until Oct 27, 11:59 PM PT. Has anyone run it against their own classification evals yet? Links elephant-1 weights: https://huggingface.co/baselabs/elephant-1 mammoth-1 weights: https://huggingface.co/baselabs/mammoth-1 Technical report: https://labs.baseten.co/articles/mammoth-1-and-elephant-1-frontier-decision-models Blog: https://www.baseten.co/blog/the-best-decision-models-in-the-world-mammoth-1-and-elephant-1/ Try it (free week): https://www.baseten.co/library/elephant-1/
