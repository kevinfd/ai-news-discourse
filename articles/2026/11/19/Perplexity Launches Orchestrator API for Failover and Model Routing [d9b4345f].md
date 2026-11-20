---
id: "d9b4345f8c6e0d02"
title: "Perplexity Launches Orchestrator API for Failover and Model Routing"
url: "https://marktechpost.com/2026/11/19/perplexity-orchestrator-api-failover-model-routing"
link: "https://marktechpost.com/2026/11/19/perplexity-orchestrator-api-failover-model-routing"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T17:47:00Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Perplexity has launched the Perplexity Orchestrator API , a single endpoint for frontier and open-weight models. It picks a serving provider by availability, capacity and latency , and bills everything through 1 account. Developers get fewer integrations and 1 invoice. \n\n What is the Perplexity Orchestrator API? \n\n The Perplexity Orchestrator API is a hosted inference gateway that serves many…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "Enterprise AI", "For Devs", "New Releases", "Software Engineering", "Staff", "Tech News"]
orgs: ["Anthropic", "Perplexity", "OpenAI", "Google", "Amazon", "xAI", "DeepSeek", "Microsoft"]
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "summary"
word_count: 965
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Perplexity Launches Orchestrator API for Failover and Model Routing

MarkTechPost · Michal Sutter · 2026-11-19

Perplexity has launched the Perplexity Orchestrator API , a single endpoint for frontier and open-weight models. It picks a serving provider by availability, capacity and latency , and bills everything through 1 account. Developers get fewer integrations and 1 invoice. 

 What is the Perplexity Orchestrator API? 

 The Perplexity Orchestrator API is a hosted inference gateway that serves many models behind 1 base URL. It covers frontier models from OpenAI, Anthropic, Google and xAI . It also serves open-weight models such as GLM, Kimi and DeepSeek, hosted by Perplexity or inference partners. 

 It accepts OpenAI Chat Completions, OpenAI Responses and Anthropic Messages requests. Most teams only change the API key and base URL. The OpenAI base URL is https://api.perplexity.ai/orchestrator/v1 . Anthropic SDK users point at https://api.perplexity.ai/orchestrator , without /v1 . 

 Perplexity runs the same layer internally, across 85+ models and more than a dozen providers. 

 How does provider failover work? 

 Failover keeps the model fixed and swaps the deployment. A Claude request that fails on Anthropic can be served by AWS Bedrock instead. The reliability docs set these rules: 

 Triggers are provider errors, rate limits and timeouts. 

 Each attempt has a time-to-first-token limit and a total-duration limit. The values are not published. 

 Invalid or over-context requests return HTTP 400 and are not retried. 

 If every deployment fails, the API returns HTTP 429 with Retry-After . 

 Requests that fail before producing output are not billed. 

 You cannot pick a deployment yourself. 

 What do the reliability and speed numbers show? 

 Perplexity measured production traffic from October 4 to November 2, 2026. Claude and GPT requests through Perplexity succeeded more often than requests to any single provider measured. Daily success rates also varied less during provider incidents. The post gives no percentage success rates. 

 Speed varied by provider too. For Claude Opus 5.5, Anthropic was fastest on 15 of 30 days, AWS Bedrock on 15. Azure’s median output speed for GPT-5.6 Sol was 27% higher than OpenAI’s. Speed-aware routing is still in progress. 

 How does automatic routing with perplexity/auto work? 

 Routing is in preview. You set model to perplexity/auto and pass a routing object. It holds a default_model and 1 to 5 routes , each with a name, description and model. 

 A decision model reads the conversation and route descriptions. It never sees route names or model IDs. If nothing matches, or the decision model fails or times out, the default model answers. So do media inputs. 

 Response headers report the result: x-perplexity-autoroute-outcome , -route and -confidence . The default policy sends traffic to GPT-6.1 Sol, with simple requests going to GPT-6 Luna. Perplexity also lists built-in Lower cost, Balanced and Higher quality profiles, plus an Auto effort preview. 

 &&

 Can routing work around refusals? 

 Perplexity tested this on a 63-task subset of Terminal-Bench 4.1 , run in Claude Code. Anthropic documents that Claude Fable 5.2 safeguards can block benign security and life sciences work. 

 Claude Fable 5.2 alone: 38/63 tasks. 

 Fable plus routes to GPT-6.1 Sol: 41/63. 

 Fable plus routes to GPT-6 Astra: 41/63. 

 The routes covered security , biology and after_refusal requests. That is +3 tasks, at a higher estimated cost per task. Perplexity calls it an adjusted comparison; results vary by workload. 

 How is Orchestrator priced? 

 Each request is billed at the answering model’s published per-token rate. Failover to another provider does not change the rate. Perplexity says there is no additional platform fee on top of credits . 

 For example, perplexity/glm-5.3 lists $1.4 input, $4.4 output and $0.26 cache read per 1M tokens . Usage draws from prepaid Perplexity API credits, also purchasable through AWS Marketplace. 

 Access is tiered by cumulative credit purchases : 

 Tier 0: Google, xAI and open-weight models. 

 Tier 1 ($50): OpenAI and most Anthropic models. 

 Tier 2 ($250): Claude Opus 5, Opus 5.5 and the Fable models. 

 How does it compare with OpenRouter and Vercel AI Gateway? 

 Feature Perplexity Orchestrator OpenRouter Vercel AI Gateway Model catalog Frontier (OpenAI, Anthropic, Google, xAI) plus open-weight GLM, Kimi, DeepSeek; count not disclosed ( blog ) 400+ models, 70+ providers ( source ) 400+ models ( source ) API formats Chat Completions, Responses, Anthropic Messages ( docs ) Chat Completions, Responses, Anthropic Messages ( docs ) Chat Completions, Responses, Anthropic Messages ( docs ) Platform fee No additional platform fee on credits ( blog ) 5.5% on credit purchases (Standard), 8% (Business) ( pricing ) No platform fee, no token markup ( pricing ) Token pricing Answering model’s published rate ( FAQ ) Provider price passed through ( FAQ ) Provider list price ( docs ) Same-model provider failover Yes, automatic ( docs ) Yes, automatic fallback ( source ) Yes, automatic ( changelog ) Prompt-based auto router perplexity/auto , preview, 1 to 5 routes ( docs ) openrouter/auto , no router fee ( docs ) Not disclosed Bring your own key Not supported ( FAQ ) Supported, 5% fee above allowance ( FAQ ) Supported, no markup ( docs ) 

 Key Takeaways 

 1 endpoint for OpenAI, Anthropic, Google, xAI and open-weight models. 

 Same-model failover across providers, billed at the same rate. 

 perplexity/auto routes by plain-language descriptions, in preview. 

 Refusal routing: 38/63 to 41/63 on Terminal-Bench 4.1, self-reported. 

 Check out the launch post , technical blog , quickstart , model catalog and routing docs . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Perplexity Launches Orchestrator API for Failover and Model Routing appeared first on MarkTechPost .
