---
id: "4c2a20eb72f4ee85"
title: "AI Model Groupthink"
url: "https://magicnumbers.io/2026/10/06/ai-model-groupthink"
source: "magicnumbers.io"
domain: "magicnumbers.io"
source_type: "community"
collector: "hackernews"
date: "2026-10-07T18:08:38Z"
published_date: "2026-10-07"
collected_at: "2026-10-13T20:17:27Z"
authors: ["io84"]
language: "en"
summary: "AI Model Groupthink\nAsk multiple AI models for a comparable opinion, and Chinese models seem to be more likely to respond in line with the wider consensus.\nI recently built/vibed a small web tool that asks a panel of 12 AI models any kind of “top three” question and tallies the answers like an Olympic medal table. The idea is to have a quick way to fetch hivemind recommendations on anything from…"
tags: []
orgs: ["China", "Anthropic", "Google", "DeepSeek", "Meta", "Alibaba", "Mistral", "OpenAI"]
topics: ["models & research", "products & launches"]
content_source: "fulltext"
word_count: 1479
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=49996542"
score: 29
comments: 9
community: "Hacker News"
---

# AI Model Groupthink

magicnumbers.io · io84 · 2026-10-07

AI Model Groupthink
Ask multiple AI models for a comparable opinion, and Chinese models seem to be more likely to respond in line with the wider consensus.
I recently built/vibed a small web tool that asks a panel of 12 AI models any kind of “top three” question and tallies the answers like an Olympic medal table. The idea is to have a quick way to fetch hivemind recommendations on anything from a good book to read, things to do in a city, or a low-stakes purchase.
The system prompt is simple and built around this request:
You are answering a ranking question with your own independent opinion. Give your top 3 answers, ranked from 1 (best) to 3.
The call explicitly asks each model for its own view, not to guess what the crowd thinks.
There is some normalization required: if we ask for the best castles in Ireland and Luna votes “Rock of Cashel” while Gemini votes “Cashel Rock”, we want to treat that as a consensus. The app uses Gemini Flash to adjudicate this.
The results – from conformist to contrarian
A word on reading the chart. Long bars and a winner at the top make it look like a leaderboard, as if more consensus is better. It isn’t necessarily. However, having clicked around a few of the queries: outlier responses are more likely to be interesting than to be an insightfully correct response that bests the responses of all the other models. I like that Gemini recommends you paint an adult bedroom terracotta while all the other models recommend green, cream, and greige, but I understand that many people will want their bots to stick to the cultural mainstream thank you very much.
Each model is scored against the consensus of the other eleven, getting full credit for the right item in the right podium spot and half credit for the right item in the wrong spot. A score of 1.0 would mean perfect agreement with the winning conclusions of the rest of the group; 0 would mean total contrarianism.
The top four conformists are all Chinese: DeepSeek, Kimi K2, Tencent’s Hy3 and GLM.
Group the scores by country and the gap holds. The five Chinese models average 0.47, the six American models 0.38, and Europe’s lone entrant, Mistral, scores 0.36.
The exception is Qwen, Alibaba’s model, which scores 0.38 and sits among the American models, just behind Grok and Nemotron (both 0.40). At the other end, the two most contrarian models are Meta’s Llama 4 Scout (0.34) and Anthropic’s Claude Haiku (0.32).
Detailed table:
Why would Chinese models agree more?
I don’t know. Here are some explanations I find plausible, roughly in order.
1. Distillation
Distillation means training a model on another model’s outputs, essentially a cloning technique. US labs, including OpenAI and Anthropic, have publicly accused Chinese labs of distilling their models at scale. Earlier this year Anthropic named DeepSeek and Kimi-maker Moonshot (and also MiniMax, which is not represented in the sample here) as running large distillation campaigns against Claude. That does not establish that distillation caused the pattern here, or even that these models were trained that way. But if a model was trained heavily on outputs from other models, one expected outcome is that its preferences converge with those of source models, especially when they converge. A model built that way is partly a consensus machine. It is striking that DeepSeek and Kimi, first and second in the table, are among the labs most often named in those accusations.
2. Chinese models learning from each other
The Chinese open-weight ecosystem is tightly knit. Labs release weights, publish methods and train on synthetic data produced by each other’s models. That could be giving the five Chinese models a family resemblance.
This matters because of how the score works. Five of the twelve models here are Chinese, so if they share a style, they help build the consensus they are scored against. A bloc that votes together will always look conformist. (Qwen breaking from the bloc is a point against this, or at least a sign the family isn’t that close.)
3. Model size and tier
The bottom of the table is crowded with smaller, cheaper models: Llama 4 Scout, Claude Haiku and Mistral Small. Smaller models hold less of the shared cultural canon in memory, so their picks are more scattered. Gemini Flash-Lite and DeepSeek’s Flash model are counter-examples, so size can’t be the whole story.
4. Knowledge cutoff
About half of new text appearing on crawl-worthy URLs is written by humans, and half by AI. A model trained more recently has read more of the slop. Most of the Chinese models here are mid-2026 releases. Again there are counter-examples: Kimi (knowledge through 2024-12) is second, while Luna has the newest cutoff on the panel and sits ninth.
5. Post-training personality
Perhaps US labs are investing in post-training in a way that gives more distinctive character, more willingness to pick the less obvious answer. If there’s a trade-off between personality and benchmark-maxxing that may also play into the flipside, where the Chinese labs are plausibly focusing more on hitting benchmarks.
6. The English canon
All prompts are in English. A model whose English training data leans on the most widely syndicated sources would tend to give the most canonical English-language answers, which is exactly what consensus rewards.
Caveats
More work needed, because…
- Small dataset. This is based on the first few hundred questions from my own usage and some humans in the wild who clicked from Reddit.
- Arbitrary panel composition. The measure of which answers are normal is itself defined via the panel’s composition. 6 US, 5 Chinese, and 1 European was an arbitrary choice by me based on my sense of the industry breakdown. More practical decisions were to have max one model per lab and avoid expensive models. Plausible additions would include models from MiniMax and ByteDance. At a stretch, and in the spirit of geo-diversity, the panel could also include Aleph Alpha (Germany), Apertus (Switzerland), Cohere (Canada), Falcon (UAE), Sarvam (India) or LG’s Exaone (South Korea). Adding flagships like Claude Sonnet, alongside the cheap tiers, might also show whether price tier matters.
- Agreement isn’t accuracy. A high score means a model says what others say, not that it’s right. On “best” questions there is often no right answer at all.
- English-language questions. The questions so far lean towards an English-speaking, Western frame.
Conclusion
Back to that bedroom recommendation:
- 11 x models recommended green, cream or greige
- 1 x model recommended terracotta
Which of these is more correct, and which is behavior we want to encourage? I suspect most of us want an AI ecosystem that isn’t a groupthink borg. We like a bit of Temperature. We want models to disagree, surprise us, occasionally push for the terracotta bedroom. I also suspect that, as users, we tend to reward models that give us answers that feel safe. These two instincts are going to be pulled apart by a lot of money over the next few years.
Multiply this out to millions of users seeking suggestions and it becomes something bigger: a quiet, constant pressure towards a lab-mediated consensus middle.
Commercially, being included in that consensus middle is already lucrative. For two decades companies have poured huge amounts of capital into efforts to rank well in search engines (SEO), and the smart ones have already switched to competing over placement in AI responses (AIO/GEO). Self-reinforcing loops will escalate the value of this prize. If the labs are competitively exfiltrating each other’s responses, getting a product highly placed in one model’s answers could enable it to flow into the next model’s training data, and the next. Consensus that was gamed once can be copied until it looks like a fact about the world.
Paint colours are a harmless starting point, but the same machinery will answer questions about which candidate to trust, which news source is reliable, which history is true. Decorating recommendations are obviously not equivalent to political or factual judgments, and models may behave very differently across domains, but the same basic machinery increasingly mediates all of them. When the models are copying each other’s opinions and feeding those opinions back into the real world, a consensus doesn’t need to be right. It only needs to be first.
For more decorating or political advice, you can ask the robots for recommendations here.
Links
Run queries here: top3.best
Stats page here: top3.best stats page
References for model data:
Implementation notes: The twelve models were called through OpenRouter, mostly in their cheaper “flash” or small variants, with reasoning switched off where the provider allows it. “Default” means the model was run with whatever reasoning behaviour the provider ships. I did not touch the Temperature parameter, nor did I explore what defaults the different models use.
