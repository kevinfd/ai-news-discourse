---
id: "a80dd20eaec84f5f"
title: "Building a multiplayer game world with autonomous Fable-class models"
url: "https://simonwillison.net/2026/Oct/29/how-i-built-the-most-ai-pilled-company-in-the-world"
link: "https://simonwillison.net/2026/Oct/29/how-i-built-the-most-ai-pilled-company-in-the-world"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-29T17:00:26Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Simon Willison"]
language: "en"
summary: "How I Built the Most AI-Pilled Company in the World \nDon't be put off by the clickbait headline, this piece by Jacob Sansbury describing how they are building Spawn is a fascinating exploration of the bleeding edge of what's possible with agentic engineering against frontier models. \n Spawn is a massively multiplayer gaming environment where players can use prompts (to the in-game agent, Savi)…"
tags: ["game-design", "ai", "generative-ai", "llms", "claude", "coding-agents", "agentic-engineering", "claude-mythos-fable"]
orgs: ["OpenAI"]
topics: ["agents & coding", "robotics & autonomy"]
content_source: "fulltext"
word_count: 583
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Building a multiplayer game world with autonomous Fable-class models

Simon Willison · Simon Willison · 2026-10-29

29th October 2026 - Link Blog
How I Built the Most AI-Pilled Company in the World. Don't be put off by the clickbait headline, this piece by Jacob Sansbury describing how they are building Spawn is a fascinating exploration of the bleeding edge of what's possible with agentic engineering against frontier models.
Spawn is a massively multiplayer gaming environment where players can use prompts (to the in-game agent, Savi) to modify the game world.
I fired it up on my phone for a few minutes and was able to prompt a castle into existence, then a dragon, then ride the dragon to fly around that castle.
By Jacob's telling, Spawn is now being developed autonomously by a swarm of Fable-powered agents costing over $3 million in tokens per month ("we spend 30x payroll on AI tokens").
Our agents change the live code directly and ship to production hourly, so they read every error, bug report and metric themselves. About 60% of our work starts from a production error, a Savi bug report (Savi is the AI you build games with in Spawn), something odd in our logs, or a feature request.
Savi files bugs herself. When a user hits one, or Savi hits one in the product, she files it. It goes straight to an agent that decides whether it's a real bug to fix, something we won't fix, or intentional design that needs a decision. Usually it becomes a change, delivered to that user within an hour, with a message in the same chat.
This is continuous deployment turned up to 11:
A loop this tight only works if it never stops, so we treat an hour without a ship as a SEV-0, our most severe kind of incident. Unshipped changes pile up, and every problem already in production lasts longer. The feedback slows down too. An agent can only keep a few hours of work in its head, so shipping faster than that actually helps it stay coherent. [...]
We can roll back a broken change in 30 seconds, exactly where it's broken and nowhere else. When a monitor or a log alert fires, it starts or wakes an agent that owns the incident, and we break things on purpose to test that those recovery paths work.
My eyebrows raised at least a dozen times reading this. I have trouble imagining this style of development working on software with higher stakes for when something goes wrong, but for a game this appears to be working surprisingly well.
Jacob says that Fable 5 (and then 5.1) was the model that made this level of autonomy possible. Opus 5.5 doesn't quite hack it for them, and when they tried GPT-6 Astra to apply fixes from a security review everything stopped working:
Every feature had been disabled and marked to be turned on again once the security fixes were done. Astra had gone through our whole product and made the insecure things secure by turning them off.
These kinds of extreme experiments are why I'm excited about game development as a substrate for exploring the edges of what today's coding agents can do.
Recent articles
- The October inflection point for vibe game development - 28th October 2026
- Battle Drones - a vibe coded RTS with audio-based multiplayer - 20th October 2026
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
