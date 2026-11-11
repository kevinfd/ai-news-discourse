---
id: "e1c7617b03642143"
title: "Fish Audio Releases Live 3, a Full-Duplex Voice Model That Reacts in 186 ms"
url: "https://marktechpost.com/2026/11/10/fish-audio-live-3-full-duplex-voice-model"
link: "https://marktechpost.com/2026/11/10/fish-audio-live-3-full-duplex-voice-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-11T04:43:53Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "Fish Audio has released Live 3 , a full-duplex voice model built for real-time voice agents. The Fish Audio Live 3 full-duplex voice model keeps listening while it speaks. That lets a caller pause, say “mm-hmm,” or change their mind without breaking the call. For developers, the pitch is simple. Turn-taking moves out of hand-tuned pipeline rules and into the speech model. \n\n TL;DR \n\n Product: A…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Audio Language Model", "Editors Pick", "Language Model", "Large Language Model", "New Releases", "Staff", "Tech News", "Technology"]
orgs: ["Google", "OpenAI", "Hugging Face"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "summary"
word_count: 929
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Fish Audio Releases Live 3, a Full-Duplex Voice Model That Reacts in 186 ms

MarkTechPost · Asif Razzaq · 2026-11-11

Fish Audio has released Live 3 , a full-duplex voice model built for real-time voice agents. The Fish Audio Live 3 full-duplex voice model keeps listening while it speaks. That lets a caller pause, say “mm-hmm,” or change their mind without breaking the call. For developers, the pitch is simple. Turn-taking moves out of hand-tuned pipeline rules and into the speech model. 

 TL;DR 

 Product: A full-duplex voice model built for real-time voice agents 

 Runs on: Hosted Fish Agent Platform and Fish Audio API; on-premises for enterprises. 

 Performance: Fish Audio shows behavior demos, but publishes no benchmark scores. 

 Best: Can decide to respond in as little as 186 ms for short reactions like “mm-hmm.” 

 What is Fish Audio Live 3? 

 Live 3 is a full-duplex voice model from Fish Audio that listens and speaks at the same time. 

 The core argument is that speed and timing are different problems. An agent can reply fast and still speak at the wrong moment. A pause after “What time do you open?” usually ends a turn. A pause in the middle of a phone number does not. 

 How does Live 3 handle turn-taking? 

 Most voice agents split recognition, reasoning, speech generation and turn-taking across separate pipeline stages. Fish Audio team states that Live 3 moves conversational timing into the speech model. It was trained on real human conversations to learn when to acknowledge, wait, respond or stop. 

 They framed the old approach as piling on “more rules and more thresholds.” Fish Audio instead wants the model to learn timing from data. A separate reasoning layer still holds the agent’s instructions and tools. 

 The Fish Audio team walks through 3 behaviors: 

 Acknowledging without taking over. A caller reads “415… 555… 0132.” Live 3 may say “okay, 415” between chunks, then wait. 

 Telling a backchannel from an interruption. A caller saying “yeah” lets the agent continue. “Wait, actually, I just need Thursday” makes it stop. 

 Waiting through corrections. For “two pizzas… no, three,” Live 3 waits instead of logging the wrong order. 

 How fast is Live 3? 

 Fish Audio states Live 3 can decide to respond in as little as 186 ms . That figure covers short reactions such as “mm-hmm,” “okay” and quick confirmations. The full answer is prepared in parallel. 

 This is a floor for small reactions, not time-to-first-audio for a complete reply. Fish Audio has not published a latency distribution. Third-party tracker OrcaRouter also reports no Artificial Analysis score for Live 3 as of November 11. 

&

 How do developers deploy Live 3? 

 Live 3 is available on the Fish Agent Platform , through the Fish Audio API, and on-premises for enterprises. The Agents platform is in public beta. 

 Agents expose a REST surface under /v1/agent/* . Browser sessions run through @fishaudio/agent-client or @fishaudio/agent-react . Agents can answer phone numbers, connect over WebRTC, or sit in a website widget. The Live 3 page lists 2,000,000+ library voices, including cloned voices. 

 A pending docs pull request shows Live 3 enabled with voice.engine: "live3" . With it on, speech recognition is fixed to fish_audio:transcribe-stream-1 . Fish Audio’s current docs say that model also classifies overlaps as interruptions or acknowledgements. 

 How much does Live 3 cost? 

 The Live 3 page lists $0.035 per minute , down 50% from $0.07 , until December 31, 2026. It says the plan includes Live 3. The pricing docs say the $0.07 list rate covers STT, TTS, basic LLMs, knowledge retrieval and tool calls. 

 Phone calls add $0.01 per minute . A number costs $1.20 per month . New accounts get a $5 trial balance. 

 How does Live 3 compare with other full-duplex voice models? 

 Metrics Fish Audio Live 3 OpenAI GPT-Live-1 Eleven Realtime v1 Max Gemini 3.8 Live Design Full duplex, timing learned in the speech model Full duplex, delegates reasoning to a backend model Cascaded, tuned end to end Live dialogue model, runs tools in the background Languages English only Not disclosed 90+ 97 Published timing 186 ms minimum (short reactions) Not disclosed in post text 0.57 s avg time to first audio Not disclosed Turn-taking score Not published +30 pp Full Duplex Bench vs GPT-Realtime-2.1 (self-reported) 94.1% Full-Duplex-Bench Not disclosed Reasoning / agent score Not published #1 on Tau3 with GPT-6 Astra (medium) 98.8% Big Bench Audio; 87.1% tool tasks Extended Thinking: 97.7% Big Bench Audio; 68.6% τ-Voice Price $0.035/min promo, $0.07 list (incl. STT, basic LLM, TTS) $0.05/min voice layer + backend tokens Session time + tokens Not disclosed in launch post Deployment Agent Platform, API, on-prem API, telephony ElevenAgents, Realtime API Gemini API, AI Studio, Gemini Enterprise (preview) 

 ElevenLabs scores come from Artificial Analysis, as reported by ElevenLabs. OpenAI and Google figures are self-reported. 

 Key Takeaways 

 Live 3 is Fish Audio’s full-duplex voice model for phone and web agents. 

 It learns turn-taking from real conversations instead of silence thresholds. 

 Short reactions can start in as little as 186 ms. 

 Agents cost $0.035 per minute until December 31, 2026, then $0.07. 

 English only, with no published benchmark scores yet. 

 Check out the launch post , try it at fish.audio/live3 , and see the Agents docs . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Fish Audio Releases Live 3, a Full-Duplex Voice Model That Reacts in 186 ms appeared first on MarkTechPost .
