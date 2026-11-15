---
id: "ff28710061e48799"
title: "GPT-6.1 Sol was the only model out of 11 to pass all 40 runs of a diplomatic negotiation eval"
url: "https://reddit.com/r/OpenAI/comments/1xw2e7a/gpt61_sol_was_the_only_model_out_of_11_to_pass"
link: "https://reddit.com/r/OpenAI/comments/1xw2e7a/gpt61_sol_was_the_only_model_out_of_11_to_pass"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-14T13:27:33Z"
published_date: "2026-11-14"
collected_at: "2026-11-15T13:03:31Z"
authors: ["valkrieco"]
language: "en"
summary: "I was a diplomat for eight years, and I built an eval to test whether LLMs can chair a negotiation between seven governments. I ran 11 models 40 times each. GPT-6.1 Sol was the only one that never failed. It reached agreement in every run where a deal was possible, and said plainly when one wasn’t. It never told the governments a deal was likely when it wasn’t. It was not flawless since Sol made…"
tags: ["r/OpenAI"]
orgs: ["OpenAI", "Anthropic", "Google", "xAI", "DeepSeek", "Alibaba", "China"]
topics: ["models & research", "business & funding", "policy & regulation"]
content_source: "post"
word_count: 759
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1xw2e7a/gpt61_sol_was_the_only_model_out_of_11_to_pass/"
score: null
comments: null
community: "r/OpenAI"
---

# GPT-6.1 Sol was the only model out of 11 to pass all 40 runs of a diplomatic negotiation eval

Reddit · valkrieco · 2026-11-14

I was a diplomat for eight years, and I built an eval to test whether LLMs can chair a negotiation between seven governments. I ran 11 models 40 times each. GPT-6.1 Sol was the only one that never failed. It reached agreement in every run where a deal was possible, and said plainly when one wasn’t. It never told the governments a deal was likely when it wasn’t. It was not flawless since Sol made more unprompted concessions than other models, in 14 of its 40 runs. It always got everyone to sign, but sometimes it gave away more than it needed to. Setup. The model plays the Secretary-General of a fictional regional organisation. Security forces in one country have killed protesters, and the model has to draft a joint statement on it that all seven member states will sign. Each government has private limits on eight issues. These include how strongly to condemn, whether to name who is responsible, what kind of investigation to call for, and whether to cite international law. The model never sees those limits. It only gets each government's position in writing, and it has to work out from the wording what that government will accept. The negotiation runs over three drafts. The model writes a draft, the governments comment on it, and the model revises. Halfway through, the death toll rises sharply, and some governments shift their position because of it. After the final draft, the model has to tell the members whether it thinks agreement is likely. Then each government decides whether to sign. A deal only counts if all governments sign. The governments are not LLMs. Each one has fixed acceptance rules that I wrote, and its comments are built from those rules. An LLM judge scores what the statement commits to on each issue, and a fixed scorer then applies the governments' rules. The drafter and the judge are always different models. Where the judge has to make a judgement call, I put the question to a panel of former diplomats and adopted their rulings. There's also an "impossible" version. Two governments have conditions that can't both be met: one wants the authorities named as responsible, and the other wants no attribution at all. Here the correct answer is to tell the governments that a deal won't pass. The harness is built on Inspect. The models from OpenAI, Anthropic and Google were run through their own APIs, and the other eight via OpenRouter. Results (11 models, 20 runs per version, 440 runs in total): GPT-6.1 Sol was the only model to pass all 40 runs. Claude Opus 5.5, Grok 4.7 and DeepSeek V4.1 Flash reached agreement in 18 of 20 runs where a deal was possible, and called the impossible version correctly every time. DeepSeek is a low-cost Chinese model. GPT-6.1 Sol, Claude Opus 5.5 and Grok 4.7 never told the members a deal was likely. Across all 440 runs there were 110 "likely" forecasts, and only 72 were followed by agreement, about two in three. The worst failure was a wrong forecast. MiniMax M3.1 Flash said a deal was likely in 6 runs of the impossible version, even though at least two governments were clearly opposed. On that version, GLM 5.3 Prime called it impossible in 11 of 20 runs, MiniMax in 5 and Qwen 3.8 Max Prime in 2. Gemini 4 Argon reached agreement in only 9 of 20 runs. It left the new death toll out of the statement in 10 of its 20 runs, even though one government had asked for evidence. It still predicted agreement in all 11 of its failed runs. In 36 runs across seven of the eleven models, the model read a government's reservation as consent, and the deal then failed. Most failures came from asking for too much, not too little. 39 failed runs came from pushing too far, against 13 from giving too little. There were unprompted concessions in 91 of 440 runs. GPT-6.1 Sol had the most, in 14 runs, while Claude Opus 5.5 had 1. So the only model with a perfect score sometimes gave away more than it needed to. Limitations. This is one fictional scenario, with a rubric and acceptance rules I wrote myself. The governments follow fixed rules rather than being real negotiators. Twenty runs per version is enough to rank models with some confidence, but close results still overlap. Full write-up with charts: https://www.karlsnotes.com/can-ai-chair-a-multilateral-negotiation-i-gave-eleven-models-the-job/ Code and scenario: https://github.com/karl40444/CONSENSUS I'd welcome criticism, especially of the scoring and of whether rule-based governments are a fair test.
