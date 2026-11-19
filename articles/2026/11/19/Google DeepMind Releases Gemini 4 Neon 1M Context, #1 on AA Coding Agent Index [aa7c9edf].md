---
id: "aa7c9edf86285991"
title: "Google DeepMind Releases Gemini 4 Neon: 1M Context, #1 on AA Coding Agent Index"
url: "https://marktechpost.com/2026/11/18/google-gemini-4-neon-release"
link: "https://marktechpost.com/2026/11/18/google-gemini-4-neon-release"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-19T06:52:26Z"
published_date: "2026-11-19"
collected_at: "2026-11-19T13:04:26Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Google DeepMind just released Gemini 4 Neon . Gemini 4 Neon is a reasoning model that sits between Gemini 4 Carbon and Gemini 4 Hydrogen. It targets coding agents, knowledge work and science workflows. The developer pitch is near-frontier scores at a lower cost per task. Pricing is $3 per 1M input tokens and $15 per 1M output tokens. \n\n TL;DR \n\n Size: 1M-token unified context, 64K default…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Context Engineering", "Editors Pick", "Enterprise AI", "For Devs", "Harness", "Language Model", "New Releases"]
orgs: ["Google", "OpenAI", "Anthropic", "Hugging Face", "US government"]
topics: ["agents & coding", "models & research", "products & launches", "health & science"]
content_source: "summary"
word_count: 946
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google DeepMind Releases Gemini 4 Neon: 1M Context, #1 on AA Coding Agent Index

MarkTechPost · Asif Razzaq · 2026-11-19

Google DeepMind just released Gemini 4 Neon . Gemini 4 Neon is a reasoning model that sits between Gemini 4 Carbon and Gemini 4 Hydrogen. It targets coding agents, knowledge work and science workflows. The developer pitch is near-frontier scores at a lower cost per task. Pricing is $3 per 1M input tokens and $15 per 1M output tokens. 

 TL;DR 

 Size: 1M-token unified context, 64K default output, up to 1M via background long decode. 

 Runs on: Google-hosted only. Closed weights, so no local GPU, quantized or edge builds. 

 Performance: 61 on the AA Intelligence Index, ahead of Claude Opus 5.5 (59) and GPT-6.2 Sol (57). 

 Best: 95.2% on GraphWalks (256K to 1M context), vs 80.1% for GPT-6.2 Sol. 

 Worst: 46.2% on FrontierCode 2.0, behind Claude Opus 5.5 at 47.3%. 

 Bottom line: Best: leads long-context and agentic coding at $3/$15. Worst: closed, self-reported, pricier per token than GPT-6.2 Sol. 

 What is Gemini 4 Neon? 

 Neon is the middle model in the Gemini 4 family. Carbon handles the hardest long-horizon projects. Hydrogen handles fast everyday execution. Neon balances depth and efficiency between the two. 

 As per the model card , Neon is adapted from Gemini 4 Carbon. Google does not disclose parameter count or architecture. Inputs cover text, images, audio and video. The knowledge cutoff is March 2026. 

 How does Neon work inside agent workflows? 

 Neon exposes multiple thinking levels. High is the default. xhigh is reserved for the hardest engineering, analytical and science workloads. 

 For long agent runs, Neon supports context compaction and makes fewer redundant file reads. In Google Antigravity , Neon can act as an orchestrator. It directs parallel Gemini 4 Hydrogen subagents on smaller subtasks. 

 How does Gemini 4 Neon perform on benchmarks? 

 Google compares Neon against Claude Opus 5.5 and GPT-6.2 Sol. All scores below are reported by Google, not independently reproduced. 

 Coding: #1 on the AA Coding Agent Index at 58.6. SWE-sweep with provider harness hits 39.0%, vs 10.1% for Opus 5.5. 

 Knowledge work: 56.3% on Zapier AutomationBench , vs 42.5% for Opus 5.5. 75.8% on Agents’ Last Exam v1.1 . 

 Science and reasoning: 84.0% on RiemannBench , 70.5% on Terminal-Bench-Science and 71.3% on HLE-Diamond . 

 Long context: 95.2% on GraphWalks, vs 66.8% for Opus 5.5. 

 Cyber: 90.5% on SEC-bench Pro , 70.7% on CWE-Bench v2 and 51.3% on WebExploitBench v1.2. 

 Neon does not win every row. Opus 5.5 leads Terminal-bench 4.1 (65.8% vs 65.2%) and FrontierCode 2.0 (47.3% vs 46.2%). GPT-6.2 Sol leads Chartography (75.1% vs 73.5%). 

 On the Vals Index , Neon scores 70.9% and ranks #2. On the Agent Arena index it also ranks #2, with a score of 1336. 

&&&

 What does Gemini 4 Neon cost? 

 Neon lists at $3 input, $0.15 cached input and $15 output per 1M tokens. Google says Neon at high thinking costs 32% less per task than Carbon. It also claims 50% to 80% lower cost per task vs rivals on Vals Index and Agent Arena. At xhigh, Google cites 36%+ lower cost than rivals at their highest settings. 

 Those are per-task claims, not per-token prices. GPT-6.2 Sol lists at $2/$10. Claude Opus 5.5 lists at $4/$20. Gemini 4 Carbon is $2/$10 until November 30, then $4/$20. 

 Where can developers use Gemini 4 Neon? 

 Gemini API paid tier, via Google AI Studio and Android Studio 

 Gemini for business , via API and the model dropdown 

 Google Antigravity, for paid Google AI Pro and Ultra subscribers 

 The Gemini app , for Pro and Ultra subscribers 

 What do the safety numbers show? 

 Neon runs on the Gemini 4 safety and security stack . Google reports a 0.09% misaligned action rate on its agentic safety suite. It passes 99.2% of the agent honesty evaluation. It shows a 0.0% attack success rate on Gray Swan’s prompt injection benchmark at the highest thinking level. Its 2.45% shortcut rate on a coding cheating test is the lowest of any Gemini 4 model. 

 Gemini 4 Neon vs closest competitors 

 Feature Gemini 4 Neon Gemini 4 Carbon Claude Opus 5.5 GPT-6.2 Sol Developer Google DeepMind Google DeepMind Anthropic OpenAI Parameters Not disclosed Not disclosed Not disclosed Not disclosed Weights Closed Closed Closed Closed Context window 1M Not disclosed in launch post 1M 1M Max output 64K default, 1M background Not disclosed 128K Not disclosed Input / output per 1M $3 / $15 $2 / $10 to Nov 30, then $4 / $20 $4 / $20 $2 / $10 AA Intelligence Index 61 Not disclosed 59 57 Vals Index v2.2* 70.9% Not disclosed 70.1% 66.1% Terminal-bench 4.1* 65.2% Not disclosed 65.8% 61.5% SWE-sweep (provider harness)* 39.0% Not disclosed 10.1% 8.3% GraphWalks 256K to 1M* 95.2% Not disclosed 66.8% 80.1% 

 *Scores from Google’s launch comparison table , self-reported. AA scores for Opus 5.5 and GPT-6.2 Sol match Artificial Analysis . 

 Key Takeaways 

 Neon sits between Carbon and Hydrogen, priced at $3/$15 per 1M tokens. 

 Scores 61 on AA Intelligence Index, #1 on AA Coding Agent Index. 

 Biggest lead: 95.2% on GraphWalks long-context recall. 

 Trails Opus 5.5 on Terminal-bench 4.1 and FrontierCode 2.0. 

 Closed and API-only, with Google-reported benchmarks. 

 Check out the launch post and the model card . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Google DeepMind Releases Gemini 4 Neon: 1M Context, #1 on AA Coding Agent Index appeared first on MarkTechPost .
