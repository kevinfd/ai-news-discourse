---
id: "0503faf26dacf250"
title: "Six months later, the best AI costs 20× less"
url: "https://modelcompare.ai/blog/ai-model-prices-over-time"
link: "https://modelcompare.ai/blog/ai-model-prices-over-time"
source: "ModelCompare"
domain: "modelcompare.ai"
source_type: "community"
collector: "reddit"
date: "2026-10-21T16:37:26Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Tgoc"]
language: "en"
summary: "To the folks that think AI is too expensive and needs to be subsidized forever to make sense."
tags: ["r/singularity"]
orgs: ["Anthropic", "OpenAI", "DeepSeek", "Google", "xAI", "China"]
topics: ["models & research", "products & launches", "business & funding", "policy & regulation"]
content_source: "fulltext"
word_count: 1015
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xbs5ay/six_months_later_the_best_ai_costs_20_less/"
score: null
comments: null
community: "r/singularity"
---

# Six months later, the best AI costs 20× less

ModelCompare · Tgoc · 2026-10-21

AI prices · October 2026
Six months later, the best AI costs 20× less
We tracked the price and score of 500 AI models since 2022. Six months after a model takes the top score, one that matches it typically costs about 20 times less. A year later, 105 times less. The price of the top model itself hasn’t come down.
In April, the highest-scoring AI model you could buy was Claude Opus 4.7, at $10 per million tokens. In October, Anthropic released Claude Haiku 5.5. It scores higher, 43.4 to 40.7 on the Artificial Analysis Intelligence Index, and costs 20 cents: a 50 times cut, 5½ months later.
That is how AI prices move. Pick any score on the index, and the price of reaching it collapses within months of the first model getting there. The price of the best model, meanwhile, goes sideways.
We followed the 10 models that took the top score between September 2024 and September 2025, long enough to follow for a full year, and divided each one’s launch price by the price of the cheapest model that matched it, day by day. In the first three months the typical top score got about 4 times cheaper. Then the price falls fast. Six months in, a model that scored as well typically cost about 20 times less. After a year it was typically 105 times less. OpenAI’s o3 cost $18 per million tokens when it took the top score in April 2025; Hy3-preview, an open-weight model from Tencent, scores higher for 10 cents.
The price of whichever model scores highest at the time doesn’t fall the same way. It sat near $30 through 2024. Since then it has bounced between $3.44 and $35 with no trend: the typical top model cost $6 in 2025 and $10 in 2026. Today’s, Claude Opus 5.5, costs $8.
Six months, give or take
Since September 2024, 21 models have taken the top score. For all 17 that have since been matched by a model under $1, the wait was between 2½ months and 8½ months. The median was 175 days.
The cheap models that caught up came from both sides of the Pacific: 4 of the 7 were open-weight models from Chinese labs (MiniMax, DeepSeek, Z.ai), and the rest were small models from xAI and OpenAI.
The four newest top models are still waiting, all from Anthropic. The oldest, Claude Fable 5, has held its score for 131 days, inside the usual range. The best model under $1 today, MiMo-V2.6-Pro from Xiaomi, scores 46.3; Claude Fable 5 scored 49.6. On the usual timetable, a sub-dollar model would match it by around December.
Part of the drop is the same model getting cheaper
A launch price is often a model’s highest. OpenAI cut o3’s price by 80% two months after launch, and cut GPT-5.6 Luna’s by 80% three weeks after launch. DeepSeek cut V4 Pro by 75% within a month, and Xiaomi cut its MiMo V2.5 models days later. The charts here use the price on each day, so those cuts show up as steps.
Pictures have prices too: ModelCompare lists 35 image models, each with what one picture costs.
Compare image models side by side
A cheaper token is not always a cheaper answer
Prices are per token, and models don’t use the same number of tokens. Some think at length before they answer, and the thinking is billed. We ran the same 163 conversations from our hallucination tests through 15 models and added up what each one cost.
The cheap models stay cheap, by less than their prices say. Claude Haiku 5.5 costs 40 times less than Claude Opus 5.5 per token and 17 times less per conversation. Some models are expensive in disguise: Gemini 3.8 Flash costs $1.50 per million tokens to GPT-6.1 Sol’s $4, and about the same per conversation. The only way to know is to run your own prompts.
GPT-6 Luna vs Claude Haiku 5.5: read the matchup
Every model we list, version by version
Here is the history behind each model on ModelCompare: every earlier version Artificial Analysis has scored, when it came out, and what it cost at launch. Most lines climb in score while their price holds or falls.
What to do with this
If a job only works on the best model, it costs what the best model costs, and that price isn’t falling. If the job can wait, or if last season’s best is good enough, the same quality has been available for under a dollar, usually within six months and so far never more than 8½ months later. Check again before you sign a long contract, and test the cheap model on your own prompts first: on our tests, cheap models pass almost everything, but not quite.
Method
Scores and prices come from Artificial Analysis, fetched on 2026-10-18: 500 models (each effort setting scored separately; we use the highest), with their release dates, Intelligence Index scores (the current version of the index, run on every model, at the highest effort published) and prices per million tokens, blended three input tokens to one output. Artificial Analysis lists today’s price; where a lab changed a price after launch, we used the price on each day, from the lab’s announcement or the history of models.dev, and added list prices for three Claude Sonnet versions and GLM-4.5, which it doesn’t price. Models with no price are left out of the price charts.
The index starts in September 2024 here: before that every model scores between 5 and 9 on the current version, too close to tell apart. “Top score” means the highest score among models with a price on that day; a model that matches it scores at least as high. Per-token prices are list prices; batch and cached-input discounts, which can cut a bill by half or more, are not counted. The bill chart uses the 163 conversations (out of 164) that every model finished in our hallucination tests on 18 October, run with each provider’s default settings rather than the highest effort the index uses.
