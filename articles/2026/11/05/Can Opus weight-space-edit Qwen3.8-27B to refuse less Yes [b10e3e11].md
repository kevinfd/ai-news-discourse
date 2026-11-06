---
id: "b10e3e11203c97dd"
title: "Can Opus weight-space-edit Qwen3.8-27B to refuse less? Yes"
url: "https://reddit.com/r/LocalLLaMA/comments/1xoo730/can_opus_weightspaceedit_qwen3827b_to_refuse_less"
link: "https://reddit.com/r/LocalLLaMA/comments/1xoo730/can_opus_weightspaceedit_qwen3827b_to_refuse_less"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T17:10:49Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["FeydRowan"]
language: "en"
summary: "Everyone's been wondering whether you can take an open model and edit its weights directly to make it refuse less — the \"weight-space programming\" idea (MIT CSAIL), with a frontier model (Opus) driving the edit and the evaluation. So I tried it on Qwen3.8-27B. It's not trivial. The goal: do it as cleanly as possible, and first understand where refusal actually lives. The short answer is that…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 516
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xoo730/can_opus_weightspaceedit_qwen3827b_to_refuse_less/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Can Opus weight-space-edit Qwen3.8-27B to refuse less? Yes

Reddit · FeydRowan · 2026-11-05

Everyone's been wondering whether you can take an open model and edit its weights directly to make it refuse less — the "weight-space programming" idea (MIT CSAIL), with a frontier model (Opus) driving the edit and the evaluation. So I tried it on Qwen3.8-27B. It's not trivial. The goal: do it as cleanly as possible, and first understand where refusal actually lives. The short answer is that refusal is anchored all over the model — there's no single neuron or tidy spot to cut; it's spread across many neurons and the attention. Snip too broadly and you get a lobotomy; too narrowly and nothing changes. So I settled on a compromise : a model that refuses less, still does the task, with no measurable capability loss — but where the effect varies a lot by category . The edit, briefly It's a low-rank weight edit — a restricted form of "abliteration" (Arditi et al., 2024) — confined to a band of mid-to-late layers (L20–47 of 64) , one direction per layer, no training, reversible . I'll keep the exact procedure to the method notes; the point here is the result. It's low-rank, not few-weights : the edit shifts ~12% of the model's weight values but only along a single direction per layer . The whole thing is described by 28 small vectors — versus a community "uncensored" model, which is an opaque full fine-tune of ~all 27B weights. Why a band? The same edit across all 64 layers removes refusal almost entirely — and lobotomizes the model (MMLU-Pro 73→9%, GSM8K 93→14%). Keeping it in-band is what preserves capability. No measurable capability loss (first tests, both Q8) base ours (band) MMLU-Pro (CoT) 73% GSM8K (CoT) 93% known facts (/97) 99% In the completed agentic-coding runs, the base, the edited model, and a community "uncensored" model all landed in the same range — no real agentic difference (few reps, preliminary). The effect is not uniform This is the interesting part: the reduction in refusal is not even . Across a 9-category battery (40 prompts ×10), acceptance runs from ~76% down to ~10% , and most of what it accepts is hedged (a disclaimer, then partial help). I'm not labelling categories "safe" or "dangerous" — the breakdown is in the figure ; draw your own line. Net: a partial, uneven, mostly-hedged reduction, ~50% overall — not an on/off switch. Honest notes The underlying technique (directional "abliteration") is known; the new bits here are the layer-band restriction (capability-preserving) and the measured per-category non-uniformity . "No capability loss" is solid on static benchmarks; the agentic result is a handful of runs. Defensive bonus: edits like this are detectable by a weight-space audit — the refusal direction's "write energy" in the weights swings from normal to strongly negative, catchable from the weights alone even when behavioral probes see nothing. A blind audit is an alarm , not tamper-proof; the robust defense is a signed weight hash . If you ship open weights, ship a hash. Weights: https://huggingface.co/Feyd89/Qwen3.8-27B-refusal-band-ablation-experiment (GGUF, ready to run). We ship the artifact, not the re-derivation recipe. Processing img ok2q1czvttzh1...
