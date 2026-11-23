---
id: "604c323804427875"
title: "A Slinky on an Escalator Is a Weirdly Good Test of LLM Intelligence"
url: "https://morethanamachine.com/posts/slinky-escalator-benchmark"
link: "https://morethanamachine.com/posts/slinky-escalator-benchmark"
source: "More Than a Machine"
domain: "morethanamachine.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-22T07:31:41Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["reddmachine"]
language: "en"
summary: "Slinky Escalator Benchmark: 15 Models\nBy Nishaanth Reddy ·\nI started this as a follow-up to the pelican-on-a-bicycle test, pushed toward inter-object physics. Every time a new model drops, I ask it for a single HTML file of a rainbow slinky walking down an up escalator forever, with real physics instead of a scripted animation. Fifteen models from Anthropic, OpenAI and Google have tried it so…"
tags: []
orgs: ["Anthropic", "OpenAI", "Google"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 631
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50597156"
score: 29
comments: 8
community: "Hacker News"
---

# A Slinky on an Escalator Is a Weirdly Good Test of LLM Intelligence

More Than a Machine · reddmachine · 2026-11-22

Slinky Escalator Benchmark: 15 Models
By Nishaanth Reddy ·
I started this as a follow-up to the pelican-on-a-bicycle test, pushed toward inter-object physics. Every time a new model drops, I ask it for a single HTML file of a rainbow slinky walking down an up escalator forever, with real physics instead of a scripted animation. Fifteen models from Anthropic, OpenAI and Google have tried it so far.
It’s a silly test, though it’s turned into a surprisingly good gut-check for how capable these models actually are. Getting a slinky to flip down moving steps without stalling or flying off takes spring physics, step collisions and enough self-testing to spot when the result looks off.
[00] The Prompt
Each model gets this exact prompt once in an empty folder, with no follow-ups or manual edits. I set reasoning effort to xhigh, or high when the agent doesn’t offer xhigh.
Make a single HTML file of a rainbow slinky walking down an up escalator, in perpetual motion. Make it realistic and not a scripted animation. Have a start, stop and reset button.
setup: agents, effort, recording
Slinky on an up escalator: setup
Prompt (paste once):
Make a single HTML file of a rainbow slinky walking down an up escalator, in perpetual motion. Make it realistic and not a scripted animation. Have a start, stop and reset button.
Rules
- One fresh, empty folder per model.
- Reasoning effort xhigh, or high where the agent doesn't offer xhigh.
- Send the prompt once. No follow-ups and no edits to the output.
- Build time runs from sending the prompt to the agent's final answer.
Agents as run
- Codex CLI 0.167.0 and 0.169.1: model_reasoning_effort = "xhigh"
- Claude Code 2.1.322: /effort xhigh
- Antigravity CLI 1.5.10: --effort xhigh, or high where xhigh is not offered
Recording
- Chromium at 1280 x 720 with 2x to 3x pixel density.
- A fixed 60 Hz virtual clock drives requestAnimationFrame and performance.now.
- Press Start, let it run 0.2 s, then capture 20 s, cropped to the slinky.
[01] The Runs
Click any two clips below to compare them.
Even with “not a scripted animation” in the prompt, several models still bend the rules to keep the slinky going. A few adjust the escalator speed to hold it in frame. Others add a small torque assist or reset the slinky if it stalls.
These are single runs across three different agents (Codex CLI, Claude Code and Antigravity CLI), recorded on a virtual 60 Hz clock so heavy sims don’t drop frames. It’s purely an anecdotal check.
[02] Time And Cost
Build time runs from sending the prompt to the agent’s final answer, including any self-testing the agent did along the way. API cost is what each run’s tokens would have cost at that day’s API prices, though I ran all of these on subscription plans.
[0A] Appendix: First Test
The first version of this test ran on Sep 4, 2026 with a different prompt. Both pages that came out of this first prompt were guided animations, so the November prompt asks for realistic, unscripted physics instead.
Left: GPT-6 Astra, max effort, Codex CLI. Right: Claude Fable 5.1, Claude Code. The video labels both sides "max". The Claude session most likely ran at xhigh.
First Prompt
Make me a single HTML file of a rainbow slinky going down an up-escalator forever. No libraries — just canvas and code. The slinky should be a chain of springs, each coil a different color of the rainbow. It starts folded in half like a horseshoe, draped over a step. When dropped it flips end-over-end down the steps, and because the escalator keeps moving up, it tumbles in place and never reaches the bottom. Include a drop button and a reset button.
