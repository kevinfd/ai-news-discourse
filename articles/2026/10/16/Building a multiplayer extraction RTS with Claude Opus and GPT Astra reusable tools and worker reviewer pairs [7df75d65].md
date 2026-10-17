---
id: "7df75d65609507d7"
title: "Building a multiplayer extraction RTS with Claude Opus and GPT Astra: reusable tools and worker/reviewer pairs"
url: "https://reddit.com/r/ClaudeAI/comments/1x7jiai/building_a_multiplayer_extraction_rts_with_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1x7jiai/building_a_multiplayer_extraction_rts_with_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T15:38:02Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["idlerunner00"]
language: "en"
summary: "I've been building Out of Pixkrieg with massive help from Claude Opus 5.5, with some GPT Astra involved too. It's a multiplayer extraction RTS in the browser: take your units into a raid, find loot and new people, and try to bring them home. Survivors stay with you for the next run. I wanted to share how I've been working with the agents, because the workflow and the development tools are a big…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "jobs & society", "models & research"]
content_source: "post"
word_count: 514
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7jiai/building_a_multiplayer_extraction_rts_with_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Building a multiplayer extraction RTS with Claude Opus and GPT Astra: reusable tools and worker/reviewer pairs

Reddit · idlerunner00 · 2026-10-16

I've been building Out of Pixkrieg with massive help from Claude Opus 5.5, with some GPT Astra involved too. It's a multiplayer extraction RTS in the browser: take your units into a raid, find loot and new people, and try to bring them home. Survivors stay with you for the next run. I wanted to share how I've been working with the agents, because the workflow and the development tools are a big part of how this came together. Claude has been the main model involved in development, including the procedural code and the game around it. The stack is Rust on the client and servers, WebAssembly in the browser, wgpu rendering and a thin TypeScript shell. I have agents work in tandems: I define a task and the quality threshold I want it to meet. A worker implements the task. A reviewer evaluates the result and identifies improvements. Those findings go back to the worker, which makes the changes. Review and revision repeat until that threshold is reached. The target comes from me, and the review findings become work for the next iteration. The repository also holds the project's rules, design, architecture and progress notes, so the agents have written context alongside the code. Before building out the game, I made procedural generators for units, structures and terrain its core. Two earlier tools are available under MIT: Procedural Pixel Creatures , including generated bodies, rigs and animation. Procedural terrain generator and painter . Both posts link to the source. The generators here build on those learnings. With that foundation already in place, the game reached this first testable prototype over a few weeks. A goal for me is to build development tools that remain useful for future projects. I'm a sucker for procedural generation, and becoming more of one. Improving a generator can improve many outputs, and having the asset work handled by those systems leaves more attention for gameplay and experimentation. For a concrete design example, unit identity is separate from equipment. The seed determines the character's appearance and name; the loadout changes what it wears and carries. The same character can return from a raid with new gear and remain recognisable. That gives a specific behaviour to check when changing the generator: equipment changes should preserve identity. The fast iteration is also great for wild brainstorming. I can try an idea, see what comes out and discard it if it doesn't work for me. I throw a lot away. I want the tools and what I learn from those attempts to carry forward, even when the experiment itself doesn't. It's still rough. The review loop gives me a process for improving the implementation, and now I need players to find out how the whole thing feels. Try the browser playtest for free from October 16 at 16:00 CEST until October 18 at 10:00 CEST . If you're using a similar setup with Claude, how do you decide when to keep iterating on an experiment and when to drop it? Feedback on the game is welcome here or on my Discord .
