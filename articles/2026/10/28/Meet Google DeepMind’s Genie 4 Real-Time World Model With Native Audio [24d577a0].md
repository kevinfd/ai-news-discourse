---
id: "24d577a03bff5826"
title: "Meet Google DeepMind’s Genie 4: Real-Time World Model With Native Audio"
url: "https://marktechpost.com/2026/10/28/google-deepmind-genie-4-world-model"
link: "https://marktechpost.com/2026/10/28/google-deepmind-genie-4-world-model"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T07:34:58Z"
published_date: "2026-10-28"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Google DeepMind has released Genie 4 as a research preview for trusted testers. The Genie 4 world model generates explorable worlds from text and image prompts in real time. It also generates the soundscape: ambient noise, music and character dialogue. Users move with keyboard controls and steer events with plain-language prompts. The bigger change is architectural. A Gemini model now runs…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "New Releases", "Staff", "Tech News"]
orgs: ["Google"]
topics: ["models & research", "agents & coding", "robotics & autonomy", "products & launches"]
content_source: "summary"
word_count: 994
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Meet Google DeepMind’s Genie 4: Real-Time World Model With Native Audio

MarkTechPost · Michal Sutter · 2026-10-28

Google DeepMind has released Genie 4 as a research preview for trusted testers. The Genie 4 world model generates explorable worlds from text and image prompts in real time. It also generates the soundscape: ambient noise, music and character dialogue. Users move with keyboard controls and steer events with plain-language prompts. The bigger change is architectural. A Gemini model now runs inside the simulation loop as a planner. That pattern is important for anyone building training environments for agents or robots. 

 TL;DR 

 Runs on: Google-hosted only (Project Genie web app, Gemini API early access). 

 Performance: Photorealistic worlds with native audio and live text steering. 

 Best: Scene consistency for up to 2 minutes, double Genie 3, per TechCrunch’s briefing . 

 Worst: Sessions last a few minutes , and objects drift after repeated prompt edits. 

 What is Genie 4? 

 Genie 4 is a world model from Google DeepMind that simulates interactive environments frame by frame. It is not a video clip generator. Each frame responds to user input as it arrives. 

 DeepMind states that the model is natively multimodal . Audio, music and dialogue are generated together with the visuals. It is DeepMind’s first real-time world model to generate audio natively. 

 It succeeds Genie 3 , announced in August 2025. Genie 3 ran at 720p and 24 frames per second, with visual memory reaching back 1 minute. 

 How does Genie 4 use Gemini? 

 Genie 4 borrows from 2 parts of the Gemini family. Gemini Omni anchors the look and behavior of each world. Other Gemini models handle the reasoning that keeps a simulation coherent. 

 The runtime loop works like this: 

 Interpret: When you type a prompt, Gemini adapts it to fit the running scene. 

 Plan: Gemini 3.8 Flash breaks a goal into a sequence of steps. 

 Verify: It reviews incoming frames to confirm each step succeeded. 

 Adapt: If the world shifts or you intervene, it revises the plan. 

 Between user inputs, Gemini also steers the scene so the world keeps progressing. DeepMind team frames this as an early step toward hybrid world models . In that design, a language model handles structure and narrative, while Genie renders pixels and sound. 

 What can you do inside a Genie 4 world? 

 Steer with text : You can change the weather, move the camera or add a new person or object mid-session. 

 Simulate physics and people : DeepMind cites aerodynamics and collisions. It calls human motion the biggest leap, with characters that react to their surroundings. 

 Hear the world : Every world carries ambient audio. Characters can also hold conversations that react to your inputs in real time. 

 Test robot tasks : In one research demo, Gemini 4 Argon split a checkers task into steps. Genie 4 received each step as a text caption and simulated Apptronik’s Apollo humanoid playing the game. 

 How does Genie 4 compare with other world models? 

 DeepMind released no benchmark tables for Genie 4. The comparison below uses only disclosed specs from each project’s own source. 

 Feature Genie 4 Genie 3 Runway GWM Worlds 2 Skywork Matrix-Game 3.0 Released Oct 27, 2026 Aug 5, 2025 Sep 3, 2026 Mar 27, 2026 Parameters Not disclosed Not disclosed Not disclosed 5B (plus 2x14B MoE variant) Resolution / FPS Not disclosed 720p / 24 fps 720p / 24 fps 720p / up to 40 fps Native audio Yes, incl. dialogue Not reported Yes, 48 kHz, incl. speech Not reported Mid-session text control Yes, Gemini-mediated Yes, promptable world events Yes, timestamped text actions Keyboard and mouse actions LLM planner in loop Gemini 3.8 Flash No No (optional external harness) No Consistency A few minutes; 2 min per TechCrunch A few minutes; 1 min visual memory No preset length; memory imperfect Minute-long memory Hardware Google-hosted, not disclosed Google-hosted, not disclosed Runway-hosted, not disclosed 8 GPUs for DiT plus 1 for VAE Access / license Trusted testers; AI Ultra and API soon Project Genie (AI Ultra) Research preview, contact form MIT, open weights 

&

 Who can use Genie 4, and when? 

 Genie 4 is live for trusted testers today. According to DeepMind, it is expected to be available soon to Google AI Ultra subscribers in Project Genie . Early access partners of the Gemini API and Google AI Studio come next. 

 All Genie 4 video and audio will carry SynthID watermarks. DeepMind states that it ran internal safety evaluations before the preview. 

 Testers so far span creative industries, journalism, education, gaming and engineering. 

 Reported uses include: 

 Filmmakers running multiple live ‘takes’ for pre-visualization. 

 Photojournalists turning a single archival photo into a grounded simulation. 

 Game developers testing styles and mechanics before writing engine code. 

 Enterprise partners generating zero-to-one simulation scenarios. 

 What are Genie 4’s limitations? 

 DeepMind lists several open problems on the Genie 4 model page : 

 Visual details and object permanence drift in longer sessions, after complex prompt edits, or during navigation. 

 Interaction is limited to a few minutes, not extended sessions. 

 Real-world locations are not simulated with perfect accuracy. 

 Legible text usually appears only when it is in the input description. 

 Real-time audio accuracy and multi-agent interactions remain unsolved. 

 Key Takeaways 

 Genie 4 generates world, ambient audio and dialogue together, in real time. 

 Gemini 3.8 Flash plans, checks frames and replans inside the loop. 

 No parameters, resolution, frame rate or benchmarks were disclosed. 

 Access starts with trusted testers, then AI Ultra and Gemini API partners. 

 Drift and short sessions remain the main practical limits. 

 Check out the Genie 4 announcement , the Genie 4 model page and the Project Genie waitlist . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post Meet Google DeepMind’s Genie 4: Real-Time World Model With Native Audio appeared first on MarkTechPost .
