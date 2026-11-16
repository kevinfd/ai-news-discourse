---
id: "d83394486a34ff75"
title: "Hark Releases Handoff², a 2x Faster Computer-Use Agent for Hark Pro"
url: "https://marktechpost.com/2026/11/16/hark-handoff-2-computer-use-agent-2x-faster"
link: "https://marktechpost.com/2026/11/16/hark-handoff-2-computer-use-agent-2x-faster"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-16T09:08:37Z"
published_date: "2026-11-16"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Hark has released Handoff² , the second version of the computer-use agent inside its Hark Pro app. The Hark Handoff 2 computer-use agent finishes web tasks about 2x faster than the original, on average. Hark states that the gains come from reinforcement learning (RL) that penalized wasted turns and latency. For teams building browser agents, it is a case study in training for speed, not only…"
tags: ["Agentic AI", "AI Agents", "AI Shorts", "Applications", "Artificial Intelligence", "Computer-Use", "Editors Pick", "New Releases", "Staff", "Technology", "Uncategorized"]
orgs: ["Anthropic", "Meta", "Hugging Face"]
topics: ["models & research", "agents & coding", "products & launches", "safety & ethics"]
content_source: "summary"
word_count: 946
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Hark Releases Handoff², a 2x Faster Computer-Use Agent for Hark Pro

MarkTechPost · Michal Sutter · 2026-11-16

Hark has released Handoff² , the second version of the computer-use agent inside its Hark Pro app. The Hark Handoff 2 computer-use agent finishes web tasks about 2x faster than the original, on average. Hark states that the gains come from reinforcement learning (RL) that penalized wasted turns and latency. For teams building browser agents, it is a case study in training for speed, not only accuracy. You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 TL;DR 

 Runs on: Hark’s cloud. Each request gets a dedicated virtual computer. Users reach it from web, iOS and Android. No local or quantized option. 

 Performance: 82% task completion on Hark’s 478-task internal benchmark, about 2x faster end to end than v1. 

 Best: 93.8% on Hark’s internal alignment benchmark (v1: 90.3%). 

 Worst: 82% browsing completion still trails Claude Opus 5.5 (max), by up to 5 points, in the same harness. 

 Bottom line (best): Up to 3.8x faster flight booking and more than 5x faster long research. 

 Bottom line (worst): Every Handoff² number is self-reported. No third-party score exists yet. 

 What is Hark Handoff²? 

 Handoff² is a computer-use agent from Hark that operates websites the way a person does. It clicks, types and scrolls on live pages instead of calling APIs. Hark previewed Handoff in August and shipped it in Hark Pro in October. Since then, Hark says it has logged over 5.6M browsing sessions and handled over $20M in purchases. Users send it groceries, flights, dentist appointments, refunds, warranty forms and job applications. 

 How does Handoff² get 2x faster? 

 Hark co-evolved 2 things: the agent harness and the RL training recipe. The new harness lets the model emit more actions per turn. Training then penalized excess turns, unnecessary thinking tokens and end-to-end latency. 

 The model learned 3 habits: 

 Batch actions, such as filling several form fields in 1 turn. 

 Group repeated action patterns into reusable composite actions. 

 Reuse those composites as the task continues. 

 Each request runs on a dedicated virtual computer with its own browser, file system and terminal. The model outputs cursor and keyboard actions aimed at screen coordinates. Because savings stack per turn, gains grow on longer, browsing-heavy tasks. 

 How fast is Handoff² compared with Handoff? 

 Hark reports these speedups over v1 : 

 Average: about 2x faster end to end. 

 Flight booking: up to 3.8x faster. 

 Long research tasks: more than 5x faster. 

 Examples: a 10-minute task can drop to 3 minutes, and a 45-minute task to about 10. 

 What do the Handoff² benchmarks show? 

 Hark reports 2 internal benchmarks: 

 Browsing: 478 tasks across 238 websites. Handoff² completes 82%, up from 73% for v1. It takes 46% less time per task. 

 Hark ran Claude Opus 5.5 (max) in the same harness as Handoff². Handoff² lands within 5 points of it. Note that v1 was measured in its original harness, not the new one. 

 Alignment: 93.8% for Handoff², up from 90.3% for v1. The suite checks that the agent never checks out without approval. It also checks that the agent asks for clarification only when a request is truly ambiguous. 

 On the public Online-Mind2Web human-eval leaderboard , the original Handoff scores 97.67%. Yutori’s Navigator n1.5 sits at 97.3%. Hark has not posted an Online-Mind2Web result for Handoff² yet. 

&&

 How does Handoff² compare with other web agents? 

 Feature Hark Handoff² Hark Handoff (v1) Yutori Navigator n1.5 Meta Muse Type Consumer agent in Hark Pro Consumer agent in Hark Pro Computer-use model via API Consumer personal agent Released Nov 12, 2026 Preview Aug 2026; in Hark Pro Oct 2026 May 6, 2026 Sep 8, 2026 Model size Not disclosed Not disclosed Not disclosed Not disclosed (Muse Spark) Runtime Hark’s own cloud computer Dedicated virtual computer (browser, file system, terminal) Yutori API Muse Secure VM with its own browser Online-Mind2Web (human eval) Not reported 97.67% 97.3% Not reported Hark browsing benchmark (478 tasks) 82% 73% Not tested Not tested Hark alignment benchmark 93.8% 90.3% Not tested Not tested Speed vs Handoff v1 ~2x avg; up to 3.8x flights Baseline Not comparable Not comparable Pricing Free; $20/mo (2x usage); $100/mo (10x usage) Same plans Pay-as-you-go API, $5 free credits Free; $20/mo Power; $100/mo Maximum Access Web, iOS, Android Web, iOS, Android API US: iOS, Android, muse.ai, WhatsApp 

 How can users and developers access Handoff²? 

 Handoff² ships inside Hark Pro on the web, iOS and Android . Hark has not announced a public API or weights. Per the pricing page , Hark Pro is free. Pro² costs $20 a month for 2x usage. Pro³ costs $100 a month for 10x usage. All features are offered on all plans. 

 Key Takeaways 

 Handoff² averages 2x faster than v1: up to 3.8x on flights, 5x+ on long research. 

 RL penalized turns, thinking tokens and latency, so the model learned to batch actions. 

 Task completion rose from 73% to 82% on Hark’s 478-task internal benchmark. 

 Alignment rose to 93.8%, but every Handoff² number is self-reported. 

 Available now in Hark Pro: free, $20 or $100 a month. 

 Check out the Hark’s Handoff² announcement , the original Handoff research preview , and the Online-Mind2Web leaderboard . Try Hark Pro . You can check the deployment options and specs here through our GPULeaderboard.com chrome extension . 

 Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Hark Releases Handoff², a 2x Faster Computer-Use Agent for Hark Pro appeared first on MarkTechPost .
