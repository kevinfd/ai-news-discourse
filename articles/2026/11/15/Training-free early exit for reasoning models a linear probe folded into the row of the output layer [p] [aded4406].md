---
id: "aded4406ca76a14a"
title: "Training-free early exit for reasoning models: a linear probe folded into the row of the output layer [p]"
url: "https://reddit.com/r/MachineLearning/comments/1xx1xdm/trainingfree_early_exit_for_reasoning_models_a"
link: "https://reddit.com/r/MachineLearning/comments/1xx1xdm/trainingfree_early_exit_for_reasoning_models_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T17:52:41Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Good-Presentation-23"]
language: "en"
summary: "Reasoning models often reach the right answer early and then keep double-checking it for thousands of tokens. I got the model to stop at that point by changing a single row of weights. There's no training and no extra code at inference time; the edited model is an ordinary weights file that runs anywhere. Processing img 5yk991rjlt1i1... Background, Reasoning models (DeepSeek, Qwen, and so on)…"
tags: ["r/MachineLearning"]
orgs: ["DeepSeek", "Alibaba"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 570
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xx1xdm/trainingfree_early_exit_for_reasoning_models_a/"
score: null
comments: null
community: "r/MachineLearning"
---

# Training-free early exit for reasoning models: a linear probe folded into the row of the output layer [p]

Reddit · Good-Presentation-23 · 2026-11-15

Reasoning models often reach the right answer early and then keep double-checking it for thousands of tokens. I got the model to stop at that point by changing a single row of weights. There's no training and no extra code at inference time; the edited model is an ordinary weights file that runs anywhere. Processing img 5yk991rjlt1i1... Background, Reasoning models (DeepSeek, Qwen, and so on) "think" in a scratchpad before answering. The scratchpad ends when the model writes a special token, </think>. To pick each next token, the model first computes a summary of everything so far: a long list of numbers called the hidden state. The last layer, the output layer, has one row of weights per word in the vocabulary. Each word's score is its row multiplied by the hidden state, and the highest-scoring words are the likeliest next words. So the score for "stop thinking now" (</think>) comes from exactly one row of that layer. What I did Ran the model on 24 maths problems and recorded its hidden state at every token of its thinking. Marked the points where the right answer had already appeared and the model was only re-checking (specifically, the ends of paragraphs after that point), and treated everything else as "still working". Found the direction in the hidden state that best separates those two groups. This is a probe: a simple linear classifier (linear discriminant analysis), computed directly with linear algebra, with no gradient training. Added that direction, times a strength of 14, to the </think> row. The "stop" score now rises only when the model's state looks like "done, just re-checking". While it's still solving, nothing measurable changes. A useful side effect: because only one token's score changes, I can compute exactly what the edited model would do from recordings of the original, without rerunning it. That's how I picked the strength and searched for cases where it would stop too early. Processing img 0r3nr3xrlt1i1... On a problem it never saw: the answer appears at token 567, the original keeps thinking until token 7,415, and the edited model stops by token ~2,000 with 98% probability. Results (small samples, one run per setting) Processing img psaikkt6lt1i1... Qwen3.5-4B (runs in stock llama.cpp): same accuracy on 8 unseen MATH-500 problems with 54% fewer tokens. On 3 AIME 2025 problems with a 32k-token limit, the original ran out of tokens on all three while re-checking answers it already had; the edited model solved 2. DeepSeek V4.1 Flash (763B parameters, 2-bit, on my laptop with an 8 GB GPU, streaming weights from the SSD): 7/7 maths problems vs 6/7, with 40% fewer tokens. As a coding agent building a small website: 84% less thinking. It still thinks after an error or anything unexpected, and skips thinking after routine steps. Page quality held up; an LLM rating put it highest, and the screenshots are below so you can judge for yourself. Processing img 3q1n1yp8lt1i1... What isn't new: using a probe on the hidden state to stop reasoning early is published (e.g. Zhang et al. 2025, arXiv 2504.05419). What's new is putting the probe inside that one row of weights, so nothing extra runs, plus these measurements. Limitations: small sample sizes; the probe was fitted on maths only (the agent results are transfer); the AIME comparison uses a 32k budget, below the 81,920 Qwen recommends for competition maths. Write-up: https://think-graft.vercel.app Code and all logs: https://github.com/nextgen-user/think-graft Model (GGUF): https://huggingface.co/vaibhavrpi/Qwen3.5-4B-think-graft-GGUF
