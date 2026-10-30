---
id: "8c0d23771daca349"
title: "A one-person studio shipped a Steam demo of a 12-chapter FPS coded by AI agents in 20 working days. Here is what the agents could and could not do."
url: "https://reddit.com/r/artificial/comments/1xikfco/a_oneperson_studio_shipped_a_steam_demo_of_a"
link: "https://reddit.com/r/artificial/comments/1xikfco/a_oneperson_studio_shipped_a_steam_demo_of_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T13:46:22Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Aware_Bell1295"]
language: "en"
summary: "I am Ekin, a one-person game studio in Turkey. On 28 October the free demo of Iron Curtain Call went live on Steam: a fast cartoon-noir FPS set in an alternate 1965 where a customer-service AI runs World War III. The code is written by Claude Code agents working from my design documents: 3,929 commits over 20 working days by 25 October, in Godot 4.7. The full game, 12 chapters, releases on 11…"
tags: ["r/artificial"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "robotics & autonomy"]
content_source: "post"
word_count: 291
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xikfco/a_oneperson_studio_shipped_a_steam_demo_of_a/"
score: null
comments: null
community: "r/artificial"
---

# A one-person studio shipped a Steam demo of a 12-chapter FPS coded by AI agents in 20 working days. Here is what the agents could and could not do.

Reddit · Aware_Bell1295 · 2026-10-29

I am Ekin, a one-person game studio in Turkey. On 28 October the free demo of Iron Curtain Call went live on Steam: a fast cartoon-noir FPS set in an alternate 1965 where a customer-service AI runs World War III. The code is written by Claude Code agents working from my design documents: 3,929 commits over 20 working days by 25 October, in Godot 4.7. The full game, 12 chapters, releases on 11 March 2027. What the agents did well: the game's systems (a Doom-style resource loop, nine weapons planned, about 49 robot types planned, bosses), the HUD, the tooling, and a headless test suite that gates every merge (zero script errors, a bot that plays the level, navigation and geometry checks). They work in parallel: one lead session, feature sessions in the cloud, one per workstream, each on its own branch. What they could not do: know what is fun. Level design that surprises took the most time of anything; the demo's level went through four versions, and a human playtest added a whole section. Every joke, the story and the cuts are mine. The agents also hit real engine bugs (a Godot audio-thread race in headless runs) and platform quirks (a minute of shader compilation on Macs) that needed measured workarounds, not prompts. Disclosure, as on the store page: voices are ElevenLabs (about 2,800 recorded lines), some art and the cinematics are Higgsfield, the score is FluidSynth plus a few ElevenLabs cues. No AI runs during play. Several subreddits for the genre ban games made with generative AI, which is its own data point about where this is heading. Demo: https://store.steampowered.com/app/5417460/Iron_Curtain_Call/ Happy to answer questions about the workflow and the limits. Drafted with the lead agent, edited by me.
