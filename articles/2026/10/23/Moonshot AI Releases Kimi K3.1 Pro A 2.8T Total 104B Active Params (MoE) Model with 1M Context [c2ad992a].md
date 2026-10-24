---
id: "c2ad992a832700f4"
title: "Moonshot AI Releases Kimi K3.1 Pro: A 2.8T Total/104B Active Params (MoE) Model with 1M Context"
url: "https://marktechpost.com/2026/10/23/moonshot-ai-kimi-k3-1-pro-open-weight-model"
link: "https://marktechpost.com/2026/10/23/moonshot-ai-kimi-k3-1-pro-open-weight-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-23T22:52:40Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Moonshot AI has just released Kimi K3.1 Pro , the first model in its K3.1 series. Kimi K3.1 Pro is a 3T-class open-weight* model with a 1-million-token context window. Moonshot team positions it against the strongest proprietary models on coding, agentic and knowledge benchmarks. For developers, it is cheaper API pricing than K3 and open weights yet not available. *open weights are expected to…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Context Engineering", "Editors Pick", "For Devs", "Harness", "Language Model", "Large Language Model", "Machine Learning", "New Releases"]
orgs: ["OpenAI", "Anthropic", "Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches", "health & science"]
content_source: "summary"
word_count: 877
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Moonshot AI Releases Kimi K3.1 Pro: A 2.8T Total/104B Active Params (MoE) Model with 1M Context

MarkTechPost · Asif Razzaq · 2026-10-23

Moonshot AI has just released Kimi K3.1 Pro , the first model in its K3.1 series. Kimi K3.1 Pro is a 3T-class open-weight* model with a 1-million-token context window. Moonshot team positions it against the strongest proprietary models on coding, agentic and knowledge benchmarks. For developers, it is cheaper API pricing than K3 and open weights yet not available. *open weights are expected to release in November 2026 . 

 TL;DR 

 Size: 2.8T total, 104B active parameters (MoE) , 1M-token context. 

 Runs on: Kimi API today. For K3, Moonshot recommends supernodes of 64+ accelerators , with MXFP4 weights and MXFP8 activations. Not a single-GPU model. 

 Performance: Near the proprietary frontier on terminal coding; behind it on scientific terminal tasks. 

 Best: SWE-Marathon 51.7, ahead of every model in Kimi’s chart (self-reported). 

 Worst: Terminal-Bench Science 0.1 at 38.1, versus 68.1 for GPT-6 Astra in Kimi’s chart. 

 What is Kimi K3.1 Pro? 

 Kimi K3.1 Pro is a post-trained version of Kimi K3 with much larger post-training compute. Moonshot team ran joint reinforcement learning across hundreds of downstream domains. To support this, the Moonshot team optimized the RL framework, long-context inference, sandbox infrastructure and rollout scheduling. 

 The base K3 architecture uses Kimi Delta Attention (KDA) and Attention Residuals (AttnRes). It activates 16 of 896 experts through a Stable LatentMoE framework. The model accepts text, images and video through the API, per the quickstart docs . 

 Moonshot team also shipped Kimi K3.1 Pro Highspeed . According to the official Moonshot blog, it runs 2 to 3x faster . 

 How does Kimi K3.1 Pro perform on benchmarks? 

 All numbers below are self-reported by Moonshot at max reasoning effort, mostly with the Claude Code harness. 

 Coding : On Terminal-Bench 4.0, K3.1 Pro scores 65.7%. That is just behind Claude Opus 5.5 at 66.4% in Kimi’s chart. On SWE-Marathon it leads at 51.7, ahead of Opus 5.5 at 46.3. On Kimi Code Bench 3.0 Long-horizon, an internal benchmark, it scores 61.2, up from K3’s 55.95. 

 Science : Terminal-Bench Science 0.1 is the clear gap. K3.1 Pro scores 38.1, versus 68.1 for GPT-6 Astra and 63.3 for Opus 5.5 in Kimi’s chart. 

 3D and CAD : On BenchCAD with tools , K3.1 Pro scores 92.7. Opus 5.5 scores 96.2 and GPT-6 Astra 95.9. Without tools, K3.1 Pro scores 72.8, close to Opus 5.5 at 73.0. 

 Finance : K3.1 Pro reports a state-of-the-art 64.4 on OfficeQA Pro v2. It scores 58.6 on Frontier Finance. On internal finance tests, it gains 7.2 points in modeling and 11.6 in research over K3. 

 Hallucination : On Kimi Hallu Bench Hard, an internal stress test, claim-level hallucinations fell from 23.4% (K3) to 8.3%. That is roughly the 65% drop Moonshot cites. GPT-6 Astra still posts a lower 5.5% on the same test. 

&&

 How does Kimi K3.1 Pro handle cyber risk? 

 Moonshot removed cyber-related data from mid-training and RL for the open-weight release. On its internal xdev-bench-hard, an unfiltered checkpoint solved 90.5% at pass@3. The shipped K3.1 Pro solves 81.0%. Moonshot says it stays behind frontier proprietary models on offensive cyber tasks. 

 How can developers access Kimi K3.1 Pro? 

 The model is live on Kimi.ai, Kimi Work, Kimi Code and the Kimi API . The API IDs are kimi-k3.1-pro and kimi-k3.1-pro-highspeed . The endpoint is OpenAI-compatible. 

 Pricing for K3.1 Pro is $2.00 input and $10.00 output per million tokens. Cache hits cost $0.20. Highspeed costs $4.00 input and $20.00 output. K3 itself was priced at $3.00 and $15.00. 

 Practical limits from the quickstart : 

 Thinking mode is always on. Reasoning effort is low , high or max (default max ). 

 Temperature 1.0 and top-p 0.95 are fixed. 

 Output defaults to 131,072 tokens and can go up to 1,048,576. 

 Access unlocks after a minimum $1 top-up. 

 Vision input does not accept public image URLs. Use base64 or uploaded file IDs. 

 How does it compare with competing models? 

&&

 *Figure taken from Kimi’s comparison chart; not confirmed on the competitor’s own page. 

 What are the limitations? 

 Weights are not public yet, so self-hosting is not possible today. 

 The 2.8T size points to multi-node, supernode-class serving. 

 Science-heavy terminal work trails GPT-6 Astra and Opus 5.5 by 25+ points. 

 Several claimed wins come from internal benchmarks. 

 For K3, Moonshot warned that dropping reasoning history in a harness destabilizes output . The K3.1 Pro docs also say to return the full assistant message. 

 Key Takeaways 

 Kimi K3.1 Pro: 2.8T total, 104B active, 1M context. 

 Terminal-Bench 4.0 at 65.7%, 0.7 points behind Opus 5.5. 

 Leads SWE-Marathon at 51.7; trails badly on Terminal-Bench Science (38.1). 

 API costs $2/$10 per million tokens, cheaper than K3. 

 Open weights are expected in November 2026. 

 Check out the official tech blog , the API quickstart and the launch post on X . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Moonshot AI Releases Kimi K3.1 Pro: A 2.8T Total/104B Active Params (MoE) Model with 1M Context appeared first on MarkTechPost .
