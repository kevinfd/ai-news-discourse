---
id: "0f7159a858191438"
title: "DialFork: a benchmark for procedural hallucination in conversational agents [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xofjrn/dialfork_a_benchmark_for_procedural_hallucination"
link: "https://reddit.com/r/MachineLearning/comments/1xofjrn/dialfork_a_benchmark_for_procedural_hallucination"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T10:44:15Z"
published_date: "2026-11-05"
collected_at: "2026-11-05T13:04:25Z"
authors: ["sergbur"]
language: "en"
summary: "Hi all, author here (Idiap Research Institute, joint work with Logitech). We recently released DialFork and thought it might interest people here. It's a benchmark for a failure mode of LLM agents that is easy to miss: every turn is fluent and factual, the tool calls are correct, yet the agent stops following the procedure it was given. For example, asked for the weather, it fetches the forecast…"
tags: ["r/MachineLearning"]
orgs: ["Hugging Face"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 547
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xofjrn/dialfork_a_benchmark_for_procedural_hallucination/"
score: null
comments: null
community: "r/MachineLearning"
---

# DialFork: a benchmark for procedural hallucination in conversational agents [R]

Reddit · sergbur · 2026-11-05

Hi all, author here (Idiap Research Institute, joint work with Logitech). We recently released DialFork and thought it might interest people here. It's a benchmark for a failure mode of LLM agents that is easy to miss: every turn is fluent and factual, the tool calls are correct, yet the agent stops following the procedure it was given. For example, asked for the weather, it fetches the forecast (correct tool call) but never tells you, and starts asking you to rate its service instead. Most steps of a conversational procedure aren't tool calls but things the agent has to say: asking, confirming, telling the result. When an agent drifts from these steps, we call it procedural hallucination : a third axis, alongside factual accuracy and correct tool use, and one that has been largely overlooked. To our knowledge, DialFork is the first benchmark aimed at measuring this axis: what the agent has to say, and in what order. How it's built: we simulate dialogues where an agent follows its workflow (24 tasks, 12 domains), then fork them: we replay each one and, at a chosen turn, give the agent an instruction that makes it drift, in different, complementary ways. That gives over 36k dialogues where we know where each drift starts and how far it goes, checked with 30 human annotators and an LLM judge calibrated on them. Three tasks, from the turn to the whole set. Because we know where each drift starts, and that an earlier drift goes further, we define three tasks that measure procedural hallucination at different levels: The turn (Task 3). Given a dialogue, either whole or turn by turn as it unfolds (streaming), find the turn where the drift starts, or say there is none. Useful as a live guardrail. The dialogue (Task 2). Given a correct dialogue and its hallucinated versions, measure how far each one drifts from it; the earlier a version drifts, the larger its distance should be. A dialogue and its own hallucinated versions talk about the same thing; what sets them apart is how they unfold. Today, comparing dialogues means comparing their content, with embeddings and semantic similarity. This task opens a new dimension, procedural distance. Useful for retrieving or clustering conversations by how they went, not just by what they're about. The set (Task 1). Given a set of correct dialogues and a set of hallucinated ones, output a single procedural distance between the two sets as a whole, comparing them as distributions rather than matching dialogues one to one. Useful for monitoring agents, e.g. whether they drift after a model upgrade, or whether a user simulator's dialogues unfold like real ones. Open problems, and a leaderboard to track them. In the paper, we report first results on all three tasks, from embedding-based distances to streaming detectors and zero-shot LLMs. They leave plenty of room. To track progress, each task has its own track on a public leaderboard on Hugging Face; adding your method takes a single CSV file of predictions. Everything is open (data, code, every prediction from the paper, and the human judgments), and we hope it's a useful starting point for the community: Leaderboard: https://huggingface.co/spaces/DialFork/leaderboard Code: https://github.com/idiap/dialfork Paper: https://arxiv.org/abs/2610.21561 Dataset: https://huggingface.co/datasets/DialFork/dialfork Happy to answer questions, and feedback (including critical) is very welcome.
