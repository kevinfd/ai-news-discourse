---
id: "c8b781f8f75360f0"
title: "Tessera-27B-B-CJK, Zellige AIs new finetune of Qwen with novel approaches to how we think about token savings"
url: "https://reddit.com/r/LocalLLaMA/comments/1x5xm28/tessera27bbcjk_zellige_ais_new_finetune_of_qwen"
link: "https://reddit.com/r/LocalLLaMA/comments/1x5xm28/tessera27bbcjk_zellige_ais_new_finetune_of_qwen"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T17:35:08Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["ghgi_"]
language: "en"
summary: "Tessera-27B-B-CJK is a Qwen3.8-27B coding agent that thinks in compressed CJK, and it spends fewer tokens doing it. Open weights, Apache-2.0. This is our first full \"Tessera\" lineup model drop! - Hugging Face: https://huggingface.co/ZelligeAI/Tessera-27B-B-CJK - Paper: https://zellige.ai/research/tessera-27b-b-cjk Tessera is our lineup of models and tunes that try new ways to save tokens, run…"
tags: ["r/LocalLLaMA"]
orgs: ["Hugging Face", "Alibaba", "China"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 475
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x5xm28/tessera27bbcjk_zellige_ais_new_finetune_of_qwen/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Tessera-27B-B-CJK, Zellige AIs new finetune of Qwen with novel approaches to how we think about token savings

Reddit · ghgi_ · 2026-10-14

Tessera-27B-B-CJK is a Qwen3.8-27B coding agent that thinks in compressed CJK, and it spends fewer tokens doing it. Open weights, Apache-2.0. This is our first full "Tessera" lineup model drop! - Hugging Face: https://huggingface.co/ZelligeAI/Tessera-27B-B-CJK - Paper: https://zellige.ai/research/tessera-27b-b-cjk Tessera is our lineup of models and tunes that try new ways to save tokens, run more efficiently and show other parts of our research. What it does: Agent loops pay for thinking on every turn. So we taught Qwen3.8-27B to think less, and to think in compressed CJK, a shorthand that mixes English, Chinese words and symbols. The thinking and the output are kept apart. The model thinks in the shorthand, but its answers and tool calls stay in plain English and code, so your harness sees normal output, This is simular to a few models such as bottlecap ai's thinkingcap but we are planning in these tessera models to go further and showcase more potential ways and research on token efficiency here and in the future. Here is one real turn from a held-out task, 27 tokens before two tool calls: 查看`linter`包; 查`FileWalker`; 查checker在`checkers`包中如何注册. The base model spent 137 tokens on the same step. That one is shorter than most. The typical turn is about half. Numbers: All of these compare against the untuned Qwen3.8-27B on the same inputs, on 11 held-out coding-agent tasks, at xhigh effort. - 0.50-0.64x the base model's thinking tokens per agent turn (typical turn 0.496x, 90% CI 0.385-0.624; token-weighted 0.644x) - 100% valid tool calls and 0 repetition loops in 88 matched turns, the same as base - 6 of 6 valid tool calls on prompts of 101K-131K tokens, Less tests at 131k+ but in the few that were done, they held up perfectly. It's built for agent loops. For competition math and hard algorithmic code, stick with the base. It scores lower there and loops more, We evaluated the bf16 model only. The GGUF and NVFP4 files are untested, so if you run them we'd love to hear how they do. How we trained it: Four short LoRA steps on Tinker, all built from the base model's own outputs. We rewrote its thinks into compressed CJK for a seed SFT, added a token-level anti-loop fix, then agentic SFT, then a rejection-sampling pass on its shortest clean rollouts. The paper has the full pipeline, the evals and some of the things that didn't work. The Hugging Face repo has the merged bf16 weights, and the LoRA, GGUF and NVFP4 versions are linked from it, all available to download and use today. Feedback, bug reports and quant results are very welcome. I meant to post this under the offical Zellige AI reddit account but reddit seems to be quite angry at anything posted by that new account so oh well. Currently traveling so I'll answer questions best I can in the meantime.
