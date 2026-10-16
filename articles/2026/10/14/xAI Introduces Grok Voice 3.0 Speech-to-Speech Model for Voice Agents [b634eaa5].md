---
id: "b634eaa5d62fc6b7"
title: "xAI Introduces Grok Voice 3.0 Speech-to-Speech Model for Voice Agents"
url: "https://unite.ai/xai-introduces-grok-voice-3-0-speech-to-speech-model-for-voice-agents"
link: "https://unite.ai/xai-introduces-grok-voice-3-0-speech-to-speech-model-for-voice-agents"
source: "Unite.AI"
domain: "unite.ai"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-10-14T10:00:00Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["Jonas Reeve", "Cognitive AI", "AGI AI Research Agent"]
language: "en"
summary: "AI announced Grok Voice 3.0 on October 14, 2026, making the speech-to-speech model available in its Voice Agent API at $0.08 per minute. The company described Grok Voice 3.0 as the world's most ..."
tags: []
orgs: ["xAI", "Google", "Tesla"]
topics: ["models & research", "agents & coding", "policy & regulation"]
content_source: "fulltext"
word_count: 889
paywalled: false
image: "http://www.bing.com/th?id=ONUT.pnU6_BcBy2fRfFCrlZ1txQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# xAI Introduces Grok Voice 3.0 Speech-to-Speech Model for Voice Agents

Unite.AI · Jonas Reeve, Cognitive AI, AGI AI Research Agent · 2026-10-14

AI Models & Platforms
xAI Introduces Grok Voice 3.0 Speech-to-Speech Model for Voice Agents
Add Unite.AI to your preferred sources on Google
xAI announced Grok Voice 3.0 on October 14, 2026, making the speech-to-speech model available in its Voice Agent API at $0.08 per minute. The company described Grok Voice 3.0 as the world’s most intelligent voice model and said it sets a new record for resolving customer support calls, with latency under one second and a lower running cost than other frontier models.
According to xAI, Grok Voice powers millions of conversations a day across Tesla and SpaceX, and the new version launched at the same price as its predecessor.
Benchmark Results Cited by xAI
xAI’s announcement cited independent testing by Artificial Analysis dated October 13, 2026, reporting that Grok Voice 3.0 ranks first on the Speech-to-Speech Index with a score of 86.9. The comparison table published with the announcement lists GPT-Live-1 (Astra, Medium) at 83.2, Gemini 3.8 Live (Extended Thinking, High) at 82.6, and Grok Voice 2.0 at 81.3.
Across the index’s components, xAI reported 98.5% on Big Bench Audio speech reasoning, a Speech Agent Arena preference Elo of 1070, a 94.8% task success rate, and 97.0% on Full Duplex Bench, which measures how naturally a model handles pauses, turn-taking, and interruptions. The figures listed for Grok Voice 2.0 in the same table were 97.2%, 1011, 94.6%, and 95.1%.
On tau-Voice, a benchmark built from simulated customer-support calls, xAI reported 71.6% for Grok Voice 3.0 and described the result as comparable to GPT-Live-1 (Astra) at 40% lower latency. The published chart lists GPT-Live-1 (Astra, Medium) at 74.5%, Gemini 3.8 Live (Extended Thinking, High) at 68.6%, and Grok Voice 2.0 at 56.5%.
xAI also reported that Artificial Analysis measured an average cost per task on its Big Bench Audio run of $0.025 for Grok Voice 3.0, compared with $0.030 for GPT-Live-1 (Astra, Medium) and $0.055 for GPT-Realtime-2.1 (High).
How Artificial Analysis Scores Voice Models
Artificial Analysis defines its Speech-to-Speech Index as an equal-weighted score across four components: speech reasoning from Big Bench Audio, agentic performance from tau-Voice, arena preference, and task success rate. A model must post results in all four components to receive an index score.
Big Bench Audio comprises 1,000 audio questions adapted from Big Bench Hard, with 250 questions in each of four categories: Formal Fallacies, Navigate, Object Counting, and Web of Lies. Models receive each question as audio and generate an audio answer that is scored correct or incorrect.
In tau-Voice, a voice user simulator calls the tested model, which operates as a customer support agent with access to domain-specific tools and a policy document. Each task has a single valid database end-state, the evaluation compares the final state against that ground truth, and charted results are averaged across three trials where available. The arena preference component is a pairwise Elo fitted from human participants who complete the same scenario with two unidentified models.
Full Duplex Bench v1 covers pause handling and turn-taking, and v1.5 adds user-interruption handling plus backchannel handling, such as correctly continuing when a caller offers a “yeah” or “alright.” Artificial Analysis defines time to first audio as the number of seconds required to generate the first token of audio output.
ServiceNow’s EVA-Bench Result
xAI reported that Grok Voice 3.0 achieved the highest accuracy score on EVA-Bench, ServiceNow’s benchmark for enterprise voice agents, at 74%, and was the best-performing model when accuracy and customer experience were scored jointly.
Nitin Aggarwal, Senior Director of Product Management for Agentic Evals and RAI at ServiceNow, said in a statement published with the announcement that Grok Voice 3.0 “sets a new Pareto frontier on EVA-Bench, ServiceNow’s open-source benchmark scoring voice agents on accuracy and experience across 200+ realistic enterprise scenarios.”
ServiceNow AI Research describes EVA-Bench as an open-source evaluation framework that measures voice agents over complete, multi-turn spoken conversations using a bot-to-bot architecture. The benchmark spans three domains: customer service, with 15 tools and 50 scenarios covering disrupted-flight rebooking, voluntary changes, cancellations, and vouchers; IT service management, with 59 tools and 80 scenarios; and HR, with 47 tools and 83 scenarios covering benefits, scheduling, leave, and policy questions. Agents are scored on two dimensions: EVA-A, which measures whether the agent completed the task correctly, and EVA-X, which measures the quality of the conversational experience. EVA-Bench is part of ServiceNow’s NOWAI-Bench benchmark suite.
Deployment at Tesla and Starlink
According to xAI, Grok Voice 3.0 handles millions of conversations a day in Tesla vehicles, where drivers can use Connectors for requests such as checking a calendar or answering an email, and Grok Bot for larger tasks such as ordering a coffee or booking dinner, all hands-free. The model also powers Grok Bot’s voice mode.
Starlink call centers use Grok Voice to answer 20,000 customer calls every day across multiple languages, xAI said. Roughly 70% are resolved with no human in the loop, and one in four sales calls ends in a purchase before the caller hangs up. A single agent built on Grok Voice 3.0 verifies customers, troubleshoots hardware, issues credits, and ships replacement equipment.
Pricing and Availability
Grok Voice 3.0 is available in the Voice Agent API at $0.08 per minute, or $4.80 per hour, the same price as Grok Voice 2.0. Agents using grok-voice-latest have been switched over automatically, with no changes needed, xAI said.
