---
id: "da52cf43de2b7257"
title: "Alibaba Releases Qwen4-Max: 2.4T MoE, 71B Active, 1M Context"
url: "https://marktechpost.com/2026/11/16/alibaba-qwen4-max-release"
link: "https://marktechpost.com/2026/11/16/alibaba-qwen4-max-release"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-16T09:44:17Z"
published_date: "2026-11-16"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Alibaba’s Qwen team has released Qwen4-Max , the first model of its Qwen4 generation. Qwen4-Max is a proprietary sparse MoE model with a 2.4T-parameter backbone and 71B parameters active per token. It accepts text, images and video, and supports a 1M-token context window . Alibaba also cut API prices and reports a 62% drop in average cost per task. \n\n TL;DR \n\n Size: 2.4T backbone parameters, 71B…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Context Engineering", "Editors Pick", "Enterprise AI", "For Devs", "Harness", "Language Model", "New Releases"]
orgs: ["Alibaba", "OpenAI", "Anthropic", "Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches", "business & funding"]
content_source: "summary"
word_count: 937
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Alibaba Releases Qwen4-Max: 2.4T MoE, 71B Active, 1M Context

MarkTechPost · Asif Razzaq · 2026-11-16

Alibaba’s Qwen team has released Qwen4-Max , the first model of its Qwen4 generation. Qwen4-Max is a proprietary sparse MoE model with a 2.4T-parameter backbone and 71B parameters active per token. It accepts text, images and video, and supports a 1M-token context window . Alibaba also cut API prices and reports a 62% drop in average cost per task. 

 TL;DR 

 Size: 2.4T backbone parameters, 71B active per token, plus 328B N-gram Embedding parameters. 1M context, 393K max output tokens. 

 Runs on: Hosted only: QwenCloud API, Token Plan, Qwen Studio, QwenWork and Qoder. No open weights, so no self-hosting or quantized builds. 

 Performance: A large jump over Qwen3.8-Max. Competitive with frontier models on agentic work, behind on hard coding and vision. 

 Best: HLAB-Vals-1.1 (legal agent work): 21.3, versus 11.7 for Kimi K3.1, the next-best model. 

 What is Qwen4-Max? 

 Qwen4-Max is a multimodal MoE language model from Alibaba, built for long-horizon professional work. A Token Plan-only preview opened this month only . 

 How does the Qwen4-Max architecture work? 

 Qwen4 upgrades the sparse MoE design in 3 places: attention, residual connections and embeddings. 

 GDN + Qwen Sparse Attention (QSA): Each QSA layer pairs with 3 Gated DeltaNet layers. These compress history into fixed-size states. QSA then uses a lightweight indexer to pick relevant context at micro-block granularity. This lowers attention and indexing cost on long sequences. 

 Gated Residual (GR): 4 parallel residual branches use dynamic read and write gates. The aim is stronger information flow and better training stability. 

 N-gram Embedding: 328B extra parameters provide lookups of local token patterns at layer 2. This adds capacity with little extra compute. 

 Alibaba reports no loss spikes across the 2.4T-scale pre-training run. On in-house tests, Qwen4-Max-Base shows 5 to 13% lower bits per byte than Qwen3.8-Max-Base. It does this while activating 25% fewer parameters. 

 How does Qwen4-Max perform on benchmarks? 

 Alibaba’s comparison chart covers 16 benchmarks. Rivals are Qwen3.8-Max-0902, Claude Opus 5.5, GPT-6.1 Sol, GPT-6 Astra and Kimi K3.1. Several scores are cited from third-party leaderboards. None were independently reproduced at launch. 

 Qwen4-Max ranks first on 4 of 16 benchmarks: 

 HLAB-Vals-1.1 (legal agents): 21.3, versus 11.7 for Kimi K3.1 and 9.2 for Opus 5.5. 

 Agents’ Last Exam v1.1: 46.7, versus 43.4 for Opus 5.5 and Kimi K3.1. 

 BioMysteryBench: 85.0, versus 84.4 for GPT-6.1 Sol. 

 DeepSWE v1.1: 75.7, versus 75.5 for Kimi K3.1. 

 Claude Opus 5.5 leads 7 of the 16 charts. Qwen4-Max trails most clearly on coding and vision: 

 ProgramBench: 31.5 versus 65.0 for Opus 5.5. 

 Terminal-Bench 4.0: 48.5 versus 67.2 for Kimi K3.1. 

 Chartography: 54.2 versus 71.1 for GPT-6 Astra. 

 Humanity’s Last Exam: 51.7 versus 59.8 for Opus 5.5. 

 On Alibaba’s own Work360 benchmark, Qwen4-Max scores 52.69, up from 47.74 for Qwen3.8-Max. Work360 spans 26 top-level domains and 721 specialized fields. 

 &&

 Why is Qwen4-Max cheaper to run? 

 Two things stack: fewer tokens and lower prices. On Work360, token use drops about 24% at Xhigh effort and 35% at High effort. On Terminal-Bench 4.0, the drops are about 48% and 49%. Average Work360 cost per task falls from $4.43 to $1.67, a 62% cut. 

 List prices fell too. Input is $1.50 per million tokens , down from $2 for Qwen3.8-Max . Output is $4.50, down from $6. Implicit cache reads drop 70%, from $0.25 to $0.075. 

 Qwen4-Max vs competitors 

 Metrics Qwen4-Max Qwen3.8-Max Claude Opus 5.5 GPT-6.1 Sol Kimi K3.1 Pro Total params 2.4T backbone + 328B N-gram emb. 2.4T Not disclosed Not disclosed 2.8T Active params 71B Not disclosed (blog implies about 95B) Not disclosed Not disclosed 104B Context 1M 1M 1M 1,050,000 1,048,576 Max output 393K 131K 128K 128K Not disclosed Input modalities Text, image, video Not disclosed Text, image Text, image Text, image Weights Proprietary, API only Not disclosed Proprietary Proprietary Open (Kimi K3.1 Pro License) Input / output price (per 1M) $1.50 / $4.50 $2 / $6 $4 / $20 $2 / $10 $2 / $10 Cached input (per 1M) $0.075 $0.25 $0.20 $0.10 $0.20 DeepSWE v1.1* 75.7 69.3 74.2 75.2 75.5 Terminal-Bench 4.0* 48.5 38.9 59.6 56.1 67.2 Humanity’s Last Exam* 51.7 43.9 59.8 54.0 51.1 ProgramBench* 31.5 28.0 65.0 52.5 25.0 HLAB-Vals-1.1* 21.3 15.4 9.2 6.3 11.7 

 *Scores from Alibaba’s Qwen4-Max chart . Qwen3.8 column is Qwen3.8-Max-0902. The chart labels Kimi as “Kimi K3.1”. Moonshot’s own card reports Terminal-Bench 4.0 of 65.7 for Kimi K3.1 Pro and 66.4 for Opus 5.5. 

 How can developers use Qwen4-Max? 

 The model ID is qwen4-max on QwenCloud . The API works with OpenAI-compatible and Anthropic-compatible clients. Supported features include function calling, structured outputs, context caching, batch processing, web search and fine-tuning. The default rate limit is 5,000,000 tokens per minute. Thinking mode is toggled with enable_thinking . 

 Subscription access runs through the Token Plan . 

 Key Takeaways 

 2.4T MoE backbone, only 71B active per token. 

 New QSA attention, Gated Residuals and 328B N-gram Embeddings. 

 First on 4 of 16 charted benchmarks, led by HLAB-Vals-1.1 at 21.3. 

 $1.50/$4.50 per million tokens, cached input down 70%. 

 Weak spots: ProgramBench (31.5) and Terminal-Bench 4.0 (48.5). 

 Check out the official Qwen4-Max blog , the QwenCloud model page and the Token Plan pricing page . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Alibaba Releases Qwen4-Max: 2.4T MoE, 71B Active, 1M Context appeared first on MarkTechPost .
