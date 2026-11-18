---
id: "c028ef26047b1a43"
title: "Perplexity Computer Adds Multiagent: Up to 16 AI Agents That Cross-Check Work"
url: "https://marktechpost.com/2026/11/17/perplexity-computer-multiagent-effort-level"
link: "https://marktechpost.com/2026/11/17/perplexity-computer-multiagent-effort-level"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-17T22:52:04Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Perplexity has added Multiagent to Computer , its agent platform for research and multistep work. Perplexity Computer Multiagent is a new effort level that sits above Ultra. A lead agent runs a team of agents on different frontier models. Those agents work in parallel, share findings directly and check each other’s work. For developers and analysts, the change is structural. Supporting agents no…"
tags: ["Agentic AI", "AI Agents", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Harness", "New Releases", "Software Engineering", "Staff", "Tech News"]
orgs: ["Perplexity", "Anthropic", "Google", "xAI", "OpenAI", "Hugging Face"]
topics: ["agents & coding", "models & research", "products & launches", "business & funding"]
content_source: "summary"
word_count: 848
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Perplexity Computer Adds Multiagent: Up to 16 AI Agents That Cross-Check Work

MarkTechPost · Michal Sutter · 2026-11-17

Perplexity has added Multiagent to Computer , its agent platform for research and multistep work. Perplexity Computer Multiagent is a new effort level that sits above Ultra. A lead agent runs a team of agents on different frontier models. Those agents work in parallel, share findings directly and check each other’s work. For developers and analysts, the change is structural. Supporting agents no longer report only to a single lead. 

 TL;DR 

 Size: Up to 16 agents per task, plus the lead. Context length: Not disclosed. 

 Runs on: Perplexity’s cloud. Web only, Perplexity Max plan. No local or quantized option. 

 Performance: Not benchmarked. Perplexity published no accuracy or speed numbers. 

 Best: 16-agent cap with direct agent-to-agent checks across 3 default model families (Claude, GPT, Gemini). 

 What is Perplexity Computer Multiagent? 

 Multiagent is the highest effort level in Perplexity Computer. It coordinates AI models to analyze complex tasks and cross-check their work, per Perplexity’s announcement . 

 It builds on effort controls launched on September 17, 2026 . That release added 4 settings: Light, Standard, High and Ultra. Each setting picks the orchestrator model and its reasoning depth. Lower settings use less expensive models. 

 How does Multiagent work? 

 The lead agent plans the task and assigns parts to supporting agents. It can assign up to 16 agents and also does part of the work itself. 

 In Perplexity’s example, Claude Fable 5.2 plans the task. It splits work among agents running Claude Opus 5.5, GPT 6.1 Sol and Gemini 4 Carbon. Those 3 models form the default team. Fable 5.2 and GPT 6 Astra join as supporting agents only when requested or needed. 

 Key mechanics from the launch post : 

 Direct sharing: Agents use evidence found by others, question assumptions and flag discrepancies. 

 Shared files: Agents coordinate edits to shared files. One agent can update revenue assumptions and notify another to reuse them in a valuation. 

 Single point of contact: Users talk only to the lead. The lead merges findings into one response. 

 Follow-ups: The lead tells affected agents what changed. The team continues its existing work. 

 Control: Users see which agents and models are running. Stopping the thread stops the whole team. 

 Model choice: Users can name specific models in their query. 

 Multiagent vs Ultra vs Model Council 

 Perplexity now offers 3 ways to put several models on 1 problem: 

 Ultra: One lead delegates to supporting agents. Those agents report only to the lead. 

 Multiagent: The same lead model as Ultra coordinates agents. They talk to each other and edit shared deliverables. 

 Model Council: Several models answer the same question independently. Computer then shows where they agree and disagree. Model Council came to Computer in July 2026. 

 Perplexity positions Multiagent for large, interconnected work that can run in parallel. Its examples include deal data room diligence, multi-scenario forecasts, annual report review, competing-hypothesis research and year-end tax preparation. 

&&

 How does it compare with other multi-agent products? 

 Feature Perplexity Computer Multiagent Kimi Agent Swarm Manus Wide Research SuperGrok Heavy Max parallel agents 16 (plus lead) Up to 300 sub-agents “Hundreds”; tested up to 250 items Not disclosed Agent-to-agent communication Yes, direct, plus shared files Not disclosed Not disclosed (main agent assembles results) Agents compare work (per xAI launch claims) Models used Mixed vendors: Claude Opus 5.5, GPT 6.1 Sol, Gemini 4 Carbon (default) Kimi K3 (K3 Swarm) Not disclosed Grok 4 Heavy Published performance data None 4.5x faster than single-agent sequential (K2.6) None Not disclosed for current version Platforms Web only Web and mobile app Web Not disclosed Plan / price Perplexity Max, $167/month billed annually Not disclosed Not disclosed $300/month at launch 

 The clearest difference is model diversity. Perplexity mixes Anthropic, OpenAI and Google models in 1 team. Kimi and Grok run their own model families. Kimi trades depth of debate for scale, with up to 300 sub-agents. 

 Deployment and availability 

 Multiagent is available to all Perplexity Max subscribers. It runs on the web only. Users select Multiagent in Computer’s effort slider when starting a new task. 

 Perplexity’s pricing page lists Max at $167 per month billed annually. Max includes 10,000 Computer credits per month. The launch post does not state credit cost per Multiagent task. 

 Key Takeaways 

 Multiagent is a new Computer effort level above Ultra. 

 A lead runs up to 16 agents that share findings directly. 

 Default team: Claude Opus 5.5, GPT 6.1 Sol and Gemini 4 Carbon. 

 Max-only, web-only, with no published benchmarks. 

 Best fit: data room diligence and multi-scenario forecasting. 

 Check out the official announcement , the effort controls post and Perplexity pricing . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Perplexity Computer Adds Multiagent: Up to 16 AI Agents That Cross-Check Work appeared first on MarkTechPost .
