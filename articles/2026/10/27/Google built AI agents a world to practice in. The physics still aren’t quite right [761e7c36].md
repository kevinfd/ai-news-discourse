---
id: "761e7c363b046418"
title: "Google built AI agents a world to practice in. The physics still aren’t quite right."
url: "https://thenewstack.io/genie-4-world-model"
link: "https://thenewstack.io/genie-4-world-model"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-27T22:33:51Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Google DeepMind introduced Genie 4 on Tuesday , a world model that renders interactive environments in real time with simulated physics, human motion, and native audio. The photorealistic demos are seriously impressive, but arguably the real draw for anyone building AI agents is that Genie 4 gives them somewhere to run multi-step tasks before it counts. \n\n Tejas Kulkarni , a research director at…"
tags: ["AI Agents", "AI Models", "Emerging technologies"]
orgs: ["Google"]
topics: ["agents & coding", "models & research", "robotics & autonomy"]
content_source: "fulltext"
word_count: 519
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google built AI agents a world to practice in. The physics still aren’t quite right.

The New Stack · Amanda Caswell · 2026-10-27

Google built AI agents a world to practice in. The physics still aren’t quite right.
Google DeepMind introduced Genie 4 on Tuesday, a world model that renders interactive environments in real time with simulated physics, human motion, and native audio. The photorealistic demos are seriously impressive, but arguably the real draw for anyone building AI agents is that Genie 4 gives them somewhere to run multi-step tasks before it counts.
Tejas Kulkarni, a research director at Google DeepMind, describes the approach at a press briefing as a move toward “these hybrid world models,” with Gemini writing the code and text and Genie turning it into a running scene. It gives developers a way to generate test environments on demand, although how closely those simulations reflect real-world conditions remains an open question about reliability.
It gives developers a way to generate test environments on demand.
How Gemini steers Genie 4
Genie 4 uses several Gemini models to keep its simulations running. Gemini Omni helps shape the environment, while Gemini 3.8 Flash follows what’s happening, plans the next steps and adjusts when something changes.
Instead of producing a finished video, Genie 4 lets users interact with the world as it’s generated. They can move through it with a keyboard, change the camera angle or use text prompts to alter the environment without restarting the simulation.
Instead of producing a finished video, Genie 4 lets users interact with the world as it’s generated.
Rehearsing robots in simulation
Google’s clearest example puts Apptronik’s Apollo humanoid through a game of checkers, with Gemini 4 Argon planning each move and Genie 4 rendering the results as captions steer the scene.
The company is also exploring how the technology could support its Gemini Robotics research, which gives developers the ability to test agents in changing environments without having to rebuild each simulation from scratch.
Where the physics breaks down
The catch is that Genie 4 can’t always keep those environments consistent. Objects can shift position or behave unpredictably during longer sessions, and Google acknowledges that the physics isn’t always accurate.
That complicates agent evaluations, particularly when tasks involve remembering locations or returning to earlier states. A failed run could reflect a problem with the agent or the simulation itself, and Google hasn’t demonstrated that Genie 4 can replace traditional physics engines in high-stakes testing.
Game developers are using Genie 4 to explore prototypes and test game mechanics before writing engine code, while enterprise partners are looking at ways to generate their own testing scenarios.
The company hasn’t published benchmarks showing how Genie 4 performs across repeated agent tests.
The company hasn’t published benchmarks showing how Genie 4 performs across repeated agent tests. This includes whether the same prompt produces consistent results, leaving leaves developers with little to go on when deciding whether to use it in automated testing.
Who gets Genie 4 access
For now, only trusted testers have access. Google plans to expand availability to Google AI Ultra subscribers through Project Genie and select partners through the Gemini API and Google AI Studio. There’s no word yet on pricing, a wider release or performance guarantees.
