---
id: "29972242f8a1899a"
title: "[R] There is no free lunch in RLVR: under strategy specialization, every pass@1 gain provably costs some prompt, and the pass@k crossover has a tight bound [R]"
url: "https://reddit.com/r/MachineLearning/comments/1xlnu1y/r_there_is_no_free_lunch_in_rlvr_under_strategy"
link: "https://reddit.com/r/MachineLearning/comments/1xlnu1y/r_there_is_no_free_lunch_in_rlvr_under_strategy"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T04:30:11Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["SwimmingAmbition5148"]
language: "en"
summary: "Paper: https://arxiv.org/abs/2610.39295 Code + verification package (every number in the paper is checked by a script): https://github.com/yliusci/no-free-lunch-rlvr Browser diagnostic: https://huggingface.co/spaces/yliusci/passk-price I kept running into the same pattern in RLVR papers: the RL model wins at pass@1 and the base model catches up or wins at large k (Yue et al. 2025 and many…"
tags: ["r/MachineLearning"]
orgs: []
topics: ["models & research", "policy & regulation", "products & launches"]
content_source: "post"
word_count: 367
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/MachineLearning/comments/1xlnu1y/r_there_is_no_free_lunch_in_rlvr_under_strategy/"
score: null
comments: null
community: "r/MachineLearning"
---

# [R] There is no free lunch in RLVR: under strategy specialization, every pass@1 gain provably costs some prompt, and the pass@k crossover has a tight bound [R]

Reddit · SwimmingAmbition5148 · 2026-11-02

Paper: https://arxiv.org/abs/2610.39295 Code + verification package (every number in the paper is checked by a script): https://github.com/yliusci/no-free-lunch-rlvr Browser diagnostic: https://huggingface.co/spaces/yliusci/passk-price I kept running into the same pattern in RLVR papers: the RL model wins at pass@1 and the base model catches up or wins at large k (Yue et al. 2025 and many follow-ups). I wanted to know whether more training fixes this or whether it is structural. This is a theory paper, no new training runs. Setup: model RLVR as an exponential tilt of the base policy over solution strategies shared across prompts (exact for mirror descent, and GRPO stays within 3e-4 TV of it at matched entropy in simulation). What comes out: No free lunch. Under exclusive specialization, every update that raises pass@1 strictly lowers success on some prompt. The exact condition is a Stiemke duality statement (a strictly positive price on prompts that equalizes strategy fitness). Being the best strategy on each prompt is provably NOT enough: there is a 3x3 counterexample with a free lunch. The pass@k price. Once the losses reach the hardest prompts, a crossover is forced. The number of crossings is at most the sign variation of the shift in per-prompt success (Karlin total positivity). The bound is tight for 1 to 6 crossings, and the order-preserving case gives exactly one, which recovers the known single-crossover result. A frontier, not a bug. With a per-prompt floor, the constrained update traces the optimal pass@1 vs pass@k trade. Forbidding any per-prompt loss removes the crossover and the whole pass@1 gain with it. The same tilt gives the entropy-performance law with an identifiable exponent. Practical part: base and RL per-prompt success rates (already in any eval log) are enough to read off the crossing count, the bound, and the price (worst pass@k loss). On published GRPO numbers for Omni-MATH (transcribed from 2607.20543, so indicative only) it finds one crossing between k=64 and k=256. Where I expect pushback: the shared-strategy model is a population-limit abstraction, and the forced crossover needs a coverage assumption (the paper gives the regime where it fails). I would really like to see per-prompt logs where people observe 2+ crossings, since that is the signature of RL reordering prompt difficulty.
