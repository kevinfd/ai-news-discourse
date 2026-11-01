---
id: "f820f39f7fbc9ac3"
title: "We built a 3D MMO that runs in the browser, mostly with Claude."
url: "https://reddit.com/r/ClaudeAI/comments/1xksx0n/we_built_a_3d_mmo_that_runs_in_the_browser_mostly"
link: "https://reddit.com/r/ClaudeAI/comments/1xksx0n/we_built_a_3d_mmo_that_runs_in_the_browser_mostly"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T03:24:20Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["eagleman234"]
language: "en"
summary: "We're the devs of Todroth, a 3D sandbox MMO that runs in a desktop browser. We just launched the beta. It's free at https://todroth.com What's in it: real-time combat (directional melee, bows, aimed spells that can miss), open PvP with wanted status and a prison, ships, houses and farms, and about 140 voiced quests. Guilds fight over four forts in weekly sieges, holding one makes your guild…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 335
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xksx0n/we_built_a_3d_mmo_that_runs_in_the_browser_mostly/"
score: null
comments: null
community: "r/ClaudeAI"
---

# We built a 3D MMO that runs in the browser, mostly with Claude.

Reddit · eagleman234 · 2026-11-01

We're the devs of Todroth, a 3D sandbox MMO that runs in a desktop browser. We just launched the beta. It's free at https://todroth.com What's in it: real-time combat (directional melee, bows, aimed spells that can miss), open PvP with wanted status and a prison, ships, houses and farms, and about 140 voiced quests. Guilds fight over four forts in weekly sieges, holding one makes your guild leader a lord, and each month the lords choose a King. The King then changes the game for everyone: scrap the taxes, open the toll roads, build or tear down a bridge, burn a forest, set lions loose on a region's roads, or bring us their own idea, which we build if we approve it thanks to the ridiculously fast build times with Claude. It stays until a later King undoes it, so who sits on the throne is worth fighting over. Outside of that you're free to play how you like: trader, pirate, farmer, fisher, builder, an outlaw etc How we worked: - We say what we want, usually with a screenshot, and Claude plans it, builds it and tests it. For visual stuff it often makes two versions and we pick one. - Each feature gets its own Claude Code session in its own git worktree, with several running at once. The day before launch, three agents built referrals, account email and the new player prologue in parallel. - Claude writes headless Playwright runs that sign up, play the prologue and take quests. CI runs them, the test server deploys itself, we test it, then it goes live. Other tools: ElevenLabs for voices (1,700+ lines), Codex on a couple of branches, Blender was used as well. Things we learnt the hard way: - It overbuilds. Ask for a dungeon and you get 40 new items. We cap it at about 10 per zone. - It struggles to see 3D bugs like T-poses and floating props. Please give it a go and tell us what you think!
