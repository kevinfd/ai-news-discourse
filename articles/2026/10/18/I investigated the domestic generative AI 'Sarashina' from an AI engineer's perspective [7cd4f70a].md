---
id: "7cd4f70ab9b81e28"
title: "I investigated the domestic generative AI 'Sarashina' from an AI engineer's perspective"
url: "https://note.com/humble_rose2342/n/n9bd0f0a7459d?hl=en"
link: "https://note.com/humble_rose2342/n/n9bd0f0a7459d?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-18T02:14:00Z"
published_date: "2026-10-18"
collected_at: "2026-10-18T12:05:49Z"
authors: ["Humble", "主に生成Ai系の調査やノウハウを投稿"]
language: "en"
summary: "IntroductionThis time, I have researched and summarized the latest information on 'Sarashina,' a domestic generative AI developed by SB Intuitions, a subsidiary of SoftBank.The reason is that the free ..."
tags: []
orgs: ["OpenAI", "SoftBank", "Meta", "Hugging Face"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 1219
paywalled: false
image: "http://www.bing.com/th?id=ONUT.hz2qDEcHfNJgOv1lWZMItw&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# I investigated the domestic generative AI 'Sarashina' from an AI engineer's perspective

note · Humble, 主に生成Ai系の調査やノウハウを投稿 · 2026-10-18

I investigated the domestic generative AI 'Sarashina' from an AI engineer's perspective
Introduction
This time, I have researched and summarized the latest information on 'Sarashina,' a domestic generative AI developed by SB Intuitions, a subsidiary of SoftBank.
The reason is that the free beta version of the 'Sarashina Service' launched on October 13, 2026, allowing the general public to access not just chat, but also the API. For those who have heard the name 'domestic LLM' but wondered what it's actually like, I would like to organize the key points you should know before trying it out as an engineer.
What is Sarashina?
Sarashina is a series of large language models strong in Japanese that SB Intuitions is building 'from scratch.' A major feature is that they are performing pre-training in-house rather than basing it on overseas models and adding Japanese to them.
I will also touch briefly on past models. On Hugging Face, the license for 'sarashina2-70b' is listed as MIT. On the other hand, 'sarashina2-8x70b' has a non-commercial license called the 'Sarashina Model NonCommercial License Agreement,' so the conditions vary even within the same series.
And the star of this show is the 'Sarashina3' generation, announced on June 30, 2026. First, two models, 'mini' and 'nano,' were released. The number of parameters was not stated in the official blog or API documentation I reviewed.
Inside Sarashina3 mini / nano
According to the technical blog, Sarashina3's mini/nano are 'non-reasoning' type Instruct models. They are not the so-called 'deep thinking models,' but rather the type that returns answers quickly. The comparison models were also evaluated in non-reasoning settings.
Pre-training is on the scale of about 30 trillion tokens, incorporating curriculum learning that optimizes the order of learning, as well as data synthesis. For post-training adjustments, methods such as multi-stage asynchronous reinforcement learning and OPSD (On-Policy Self-Distillation) are introduced. They have also created synthetic data for agents, and the design seems to be conscious of use cases that call multiple tools over several steps.
Agent capability cannot be dismissed as a 'weakness'
Officially, results are shown indicating that it is on par with GPT-4.1 in the tool-calling benchmark BFCL v3, and equivalent to or better than Qwen3-235B-A22B-Instruct-2507 in the Telecom category of the conversational agent evaluation τ2-bench.
On the other hand, it is also noted that now that reasoning models have become the norm, there are points where it has not yet reached the level required for agent capabilities and the like. In other words, it is not 'all bad' nor 'fully usable,' but because its design philosophy differs from reasoning models, its strengths and weaknesses depend on the task. If you are going to use it in practice, I think it is best to trust the results of testing it with your own tasks rather than the benchmark numbers.
Benchmark numbers
In QA regarding Japanese culture (JamC-QA), mini scored 0.82 and nano scored 0.61. Officially, it is explained that they outperform Qwen3-235B-A22B-Instruct-2507, GPT-4.1, and GPT-5.4 mini in non-reasoning settings.
Evaluations for τ2-bench and BFCL v3 were conducted using official implementations, while others were evaluated using internal implementation code using FlexEval. An LLM judge (gpt-oss-120b) was used for scoring ELYZA-tasks-100 and Answer Carefully.
Released not as a 'single model' but as a 'set of RAG components'
With Sarashina3, in addition to the chat model, peripheral specialized models were also released.
guard is a model that determines whether input or output is harmful, classifying it into 12 categories from T1 to T12. The F1 score is 71.2 for the input side, 65.0 for the output side, and 68.1 on average. In the document comparison, Llama Guard 3 (8B) was 43.5 for input, 57.9 for output, and 50.7 on average.
embedding supports MRL (a learning method where dimensions can be reduced later) and has been trained with dimensions of 1536, 1024, 512, 256, and 128. The official website also included results for 64 dimensions. Using a model merging method called DARE-TIES, a model specialized for search and a model specialized for classification were combined. While they averaged 77.62 and 77.81 respectively, the score became 78.22 after merging. There are 7 types of supported task types.
The JMTEB average is 78.22 at 1536 dimensions, 78.08 at 1024 dimensions, and 75.72 even at 256 dimensions. The previous generation Sarashina2 embedding (2560 dimensions) was 78.69, so while the new one has a slightly lower score, the number of dimensions is about 40% lower. Let me add one clarification here. This "40% reduction" is a comparison of the number of dimensions between the previous generation and the current generation, not a case of reducing the dimensions of the same model. Also, it does not necessarily mean that the cost of the entire vector DB will be reduced by 40% (it varies depending on the index type, metadata, etc.). In comparison with other models, ruri-v3-310m (768 dimensions) is 75.85, and plamo-embedding-1b (2048 dimensions) is 74.85.
rerank is a model based on SB Intuitions' ModernBERT-Ja-1.4B, which is a type that allows you to change the perspective of reordering by giving instructions. The average of the five datasets is 93.08, and the blog states that it is at the "same level" as the comparison target ruri-v3-reranker-310m (93.56). It does not say it is superior, and the official source itself writes that it is better to treat it as a "reference value for understanding the nature of the model."
translate is a model finished with synthetic parallel data, self-distillation using a quality estimation model, and further SFT and DPO. I will write the evaluation conditions separately.
First is the automatic evaluation. Using 997 sentences from WMT2024, GPT-5-mini decides the winner by comparing two translations. The method is to swap the presentation order and evaluate twice, and only determine the winner if the results match; if they do not match, it is a draw. All numbers are results viewed from Sarashina3 translate.
For English to Japanese, 
37.7% wins, 32.6% losses, and 29.7% draws against Google Cloud Translation API (Advanced)
46.8% wins, 23.8% losses, and 29.4% draws against plamo-2-translate
For Japanese to English, 
34.3% wins, 29.9% losses, and 35.8% draws against Google
44.0% wins, 24.1% losses, and 31.9% draws against plamo-2-translate
Next is the human evaluation. 
This is only a comparison with Google, and five in-house annotators evaluated them without knowing which was Sarashina.
For English to Japanese, there were 470 cases: 236 wins for Sarashina, 213 wins for Google, and 21 draws
For Japanese to English, there were 490 cases: 199 wins for Sarashina, 214 wins for Google, and 77 draws
In other words, the results show a split in trends, with Sarashina being slightly superior for English to Japanese, and Google being slightly superior for Japanese to English.
Both are limited test sets and in-house evaluations. I think it is too early to conclude that "Sarashina's translation is generally better (or worse) than Google's." Note that the input limit for translate is 5,000 characters.
When lined up like this, it is a configuration where you can assemble the standard RAG pipeline of "embedding → rerank → LLM → guard" with models from the same provider. There is a possibility that it will reduce the effort of looking for separate services for each component.
Computing resources and sovereign cloud
What cannot be left out when talking about Sarashina is computing resources.
