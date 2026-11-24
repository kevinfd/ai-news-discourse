---
id: "40561376962072d7"
title: "China's Z.ai Says Its New AI Model Can Think Like One Four Times Its Size"
url: "https://decrypt.co/383851/chinas-zai-new-ai-model-glm-think-like-four-times-size"
link: "https://decrypt.co/383851/chinas-zai-new-ai-model-glm-think-like-four-times-size"
source: "Decrypt"
domain: "decrypt.co"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-23T15:07:00Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["Decrypt", "Jose Antonio Lanz"]
language: "en"
summary: "Z.ai's GLM-5.4 uses a looping architecture to squeeze more reasoning power from fewer parameters, challenging American AI giants."
tags: []
orgs: ["China", "Anthropic", "OpenAI", "DeepSeek", "Alibaba", "Google"]
topics: ["models & research", "agents & coding", "business & funding", "products & launches"]
content_source: "fulltext"
word_count: 780
paywalled: false
image: "http://www.bing.com/th?id=ONUT.svk9hgPUiBtNkO-1BO3j3g&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# China's Z.ai Says Its New AI Model Can Think Like One Four Times Its Size

Decrypt · Decrypt, Jose Antonio Lanz · 2026-11-23

In brief
- Z.ai launched GLM-5.4, a 750-billion-parameter AI model that reuses neural network layers to improve reasoning without adding parameters.
- Company experiments showed improvements in mathematics and scientific reasoning, but GLM-5.4 lacks independently verified flagship benchmarks against Claude or GPT.
- The model is available through coding subscriptions starting at $18 monthly, with API pricing and downloadable weights still pending.
Chinese AI developer Z.ai released GLM-5.4 on Monday, introducing a new architecture that it claims delivers the reasoning capabilities of models nearly four times its size without requiring nearly as many parameters.
The Beijing-based company says its new 750-billion-parameter model can compete with systems containing two to three trillion parameters. It also supports a one-million-token context window, accepts images and video, and can generate up to 128,000 tokens in a single response, according to its technical documentation. Parameters are the internal values a model learns during training, while tokens are the chunks of text it processes and generates—roughly equivalent to words or parts of words.
The release comes as American companies including OpenAI, Anthropic, and Google dominate the highest positions in AI performance rankings. Chinese developers, meanwhile, have increasingly focused on making powerful models cheaper to run, particularly for coding and autonomous agents.
Did you know?
You can now act on the news you read: Go long or short Anthropic with perpetual futures, all from your Decrypt Money Account.
Z.ai has been among China's strongest competitors. As Decrypt reported in August, its predecessor GLM-5.3 was already competitive with leading American coding models, although it still trailed the best proprietary systems on several software engineering tests.
How GLM-5.4 tries to get smarter without getting bigger
GLM-5.4 introduces what Z.ai calls a Loop Transformer, which processes information through the same 28 neural network layers twice. Traditional Transformers generally pass information through each layer once, so reusing layers effectively increases computational depth without increasing the number of stored parameters.
The company combines this approach with gated updates, which regulate how much information changes between passes, and a hybrid memory cache that avoids storing an entirely separate copy of previous calculations. Sparse attention also helps the model focus its computing power on relevant information rather than processing everything equally.
In controlled experiments on a smaller 30-billion-parameter model, Z.ai reported that its looping technique increased accuracy on AIME 2025, a mathematics examination benchmark scored by the percentage of correctly solved problems, from 19.17% to 30.42%.
GPQA Diamond, a graduate-level science question-answering test also scored by correct-answer percentage, improved from 47.58% to 56.26%. The experiments required approximately 10% additional training compute, while reducing generated reasoning tokens by 10% to 14% on several tests.
Those results concern the experimental architecture, not independently established performance for GLM-5.4 itself. Z.ai has not published a comprehensive flagship benchmark comparison demonstrating that the new model matches Claude or GPT.
The company is also promoting what it calls Generalized Coding: using programming to accomplish tasks beyond software development. Its demonstrations include building a video game, creating 3D environments, and designing a six-axis robotic arm using engineering software.
Can it compete with Claude and GPT on price?
GLM-5.4 is available through Z.ai's Coding Plan, which costs $18 monthly for Lite, $80 for Pro, and $168 for Max. Z.ai says subscribers receive 50% more GLM-5.4 usage than GLM-5.3 under comparable weekly quotas.
The company's previous flagship costs $1.40 per million input tokens and $4.40 per million output tokens through its API. By comparison, OpenAI's GPT-6.2 Sol costs $2 and $10, while Anthropic's Claude Opus 5.5 costs $4 and $20, respectively.
At those published rates, GLM-5.3 is considerably cheaper than its American counterparts, although GLM-5.4's own API pricing has not been announced. Its actual performance-per-dollar advantage therefore cannot yet be calculated.
China has other serious contenders. Alibaba's Qwen 4 Max recently topped Chinese competitors on Arena's agent leaderboard, while Moonshot's Kimi K3 and DeepSeek V4 have challenged American developers on coding performance and API pricing.
The performance gap remains contested. A U.S. government evaluation placed DeepSeek roughly eight months behind the American frontier, although researchers questioned its methodology.
Z.ai itself remains on the U.S. Commerce Department's Entity List, following its January 2025 designation over concerns that its AI research could support Chinese military modernization. The restrictions limit access to controlled American technology, but have not stopped the company from releasing new models.
GLM-5.4 is currently accessible to coding subscribers, with API access scheduled after security evaluations. Z.ai has also acknowledged that the model sometimes gets trapped in excessively long reasoning loops, a limitation it is working to address in its next generation.
Daily Debrief Newsletter
Start every day with the top news stories right now, plus original features, a podcast, videos and more.
