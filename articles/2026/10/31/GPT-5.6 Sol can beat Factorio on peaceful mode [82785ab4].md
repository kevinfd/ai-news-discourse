---
id: "82785ab4f152db3e"
title: "GPT-5.6 Sol can beat Factorio on peaceful mode"
url: "https://ryanmadden.net/gpt-56-beats-factorio"
link: "https://ryanmadden.net/gpt-56-beats-factorio"
source: "Ryan Madden"
domain: "ryanmadden.net"
source_type: "community"
collector: "hackernews"
date: "2026-10-31T18:50:34Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["ryanmadden"]
language: "en"
summary: "GPT-5.6 Sol can beat Factorio\nEdit: Woah, this took off! If you want more details you can subscribe at the bottom of the post or on YouTube. I’m working on a more detailed highlights/commentary post and video.\nPreviously: We got Claude Code playing Factorio, Towards beating Factorio autonomously, and Faketorio: an agent testbed\nI got GPT-5.6 Sol, running in Codex with low thinking level, to…"
tags: []
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "health & science", "agents & coding", "search & media"]
content_source: "fulltext"
word_count: 390
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50318871"
score: 173
comments: 184
community: "Hacker News"
---

# GPT-5.6 Sol can beat Factorio on peaceful mode

Ryan Madden · ryanmadden · 2026-10-31

GPT-5.6 Sol can beat Factorio
Edit: Woah, this took off! If you want more details you can subscribe at the bottom of the post or on YouTube. I’m working on a more detailed highlights/commentary post and video.
Previously: We got Claude Code playing Factorio, Towards beating Factorio autonomously, and Faketorio: an agent testbed
I got GPT-5.6 Sol, running in Codex with low thinking level, to complete a peaceful (i.e. no biters) Factorio run in 13.5 hours of game time:
A timelapse of the full run is available on YouTube.
Similar to my previous post, this run used a game manager to allow Sol/Codex to interact with the game via a small library (though in this run it was Python rather than Bash). The library allows the model to play the game programmatically while enforcing the same restrictions that human players face when using the GUI (e.g. reach of the player, fog of war).
Observing the run was fascinating: Sol exceeded my expectations in some areas while also showing clear weaknesses in others. I have the entire run recorded and am working on a commentary video, but in the meantime here’s a small timelapsed segment showing some parts of the factory:
Besides the screencast, my run manager also captured production statistics throughout the game. Here’s a chart of total resource production, annotated with science research milestones:
I had planned to terminate the run after blue science research, but Sol’s surprising effectiveness convinced me to keep it going. Unfortunately, the scaling issues I thought would occur in the blue science stage appeared later and slowed Sol’s relative progress significantly.
The rocket launch was only achieved through significant ‘manual’ effort on Sol’s part as it papered over its late-game failures to connect certain production systems by repeatedly ferrying supplies between areas of the factory.
Still, I was pleased with the improvement over previous attempts with GPT-5.5 which suffered from the model’s failures to use transport belts at all.
I’m optimistic about autonomous Factorio play as a medium for building intuition about the nature of model capabilities. In many ways playing Factorio is analogous to programming but with the benefit of being much more legible to casual observers, making it convenient for grounding discussion of model behaviors.
I look forward to testing other models and thinking levels, as well as non-peaceful runs. Stay tuned!
