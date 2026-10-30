---
id: "8ec57f3006159936"
title: "My 6 year old daughter designed a fully-fledged unicorn game and Claude Sonnet built it in under a month. Every sprite, sound and map is made from scratch"
url: "https://reddit.com/r/ClaudeAI/comments/1xiks9w/my_6_year_old_daughter_designed_a_fullyfledged"
link: "https://reddit.com/r/ClaudeAI/comments/1xiks9w/my_6_year_old_daughter_designed_a_fullyfledged"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T14:00:20Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["OnyxMonolith"]
language: "en"
summary: "We built a private unicorn game for my six-year-old daughter, with Claude Sonnet 5.5 as the coding agent for all of it. I'm a quantitative engineer with 20+ years of experience but i never made a game before. My daughter designed most of the maps and the playground games, and she gave the notes that shaped the rest. The initial thing was just a small forest map and finding all the 6 unicorns.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "jobs & society", "models & research"]
content_source: "post"
word_count: 871
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xiks9w/my_6_year_old_daughter_designed_a_fullyfledged/"
score: null
comments: null
community: "r/ClaudeAI"
---

# My 6 year old daughter designed a fully-fledged unicorn game and Claude Sonnet built it in under a month. Every sprite, sound and map is made from scratch

Reddit · OnyxMonolith · 2026-10-29

We built a private unicorn game for my six-year-old daughter, with Claude Sonnet 5.5 as the coding agent for all of it. I'm a quantitative engineer with 20+ years of experience but i never made a game before. My daughter designed most of the maps and the playground games, and she gave the notes that shaped the rest. The initial thing was just a small forest map and finding all the 6 unicorns. What it is: A pixel-art sandbox that runs in a phone/tablet browser, installs to the Home Screen and plays offline. You lead a unicorn around 8 places, find 5 friends who follow in a herd, and cast 6 kinds of magic that affect certain items in the game. There are playground mini-games, and an optional spelling mode that a parent switches on. Saves stay on the device, with optional cloud backup. What Sonnet did: Claude wrote all the code: about 136k lines of TypeScript across the game, the build tools, a Cloudflare Worker and 3,000+ tests. That includes: A software 3D renderer. Unicorns, buildings and trees are small 3D models written as code. The renderer draws them at 4x size with a fixed light and ambient occlusion, then reduces them to hard-pixel sprites on atlases. No Blender, no sprite packs. A sound synthesizer. All 75 effects and 9 music loops are generated from code, with no samples. A map compiler that proves every door, spawn and friend is reachable. A game loop, pathfinding, and a herd that follows the leader. How we worked. The loop was simple. My daughter played the latest build and told me what she liked and what to change. I wrote her notes down (sometimes 25 items in one round, from "a place with a slide" to what a door should do) and gave them to Sonnet. The next day she played the result. Then again. She also learned how software gets made, because she could see her idea turn into a thing she could play and also I explained a lot about how stuff works to her. Around that loop, a few things made it work: A written plan first: We started from a tech spec, and Claude built small throwaway spikes before committing to anything. Before using Phaser it ran a seven-check test of the engine (animation, tile maps, depth sorting, pixel sampling, touch under zoom, audio unlock). It did the same for the Cloudflare backend. A style check before scale. Before rendering hundreds of frames, Claude drew one unicorn, then a forest clearing, and checked that they looked like the same world. It also dropped an idea that failed: a pure 3D face looked blank, so the eyes and mouth became hand-placed pixels. A decision log. Claude kept a row for every proactive choice with the reason and the evidence: 245 rows over 11 deploys. It also kept a handoff file so a new session could pick up exactly where the last one stopped. Tests that found real bugs: When the followers flickered between walking and standing, Claude measured it in the running game (20 flips in 103 seconds), fixed it, and measured again (none in 128 seconds). It also wrote a test that failed on the old code. When a browser test failed once, it worked out the odds of what the test assumed before blaming the machine. Checking what it couldn't see or hear: Claude couldn't watch the game or listen to it, so it screenshotted and read the pictures. It measured the sound with loudness meters and a signal analyser at the output. One thread: I always asked Claude not to use subagents, so I could follow a single conversation and audit what it did so that I always understand what is happening. Some notes: The repo has a file listing what is built, what was tested and what wasn't. It has run on two iPhones and a Mac, and we mostly play it on a Kindle Fire. When the Kindle felt choppy during spells, Claude added a low-end mode that draws fewer pixels and fewer particles, and it switches itself on for Fire tablets automatically detecting low fps. You can play it entirely for free here: https://unicorn-academy-game.github.io/ Source: https://github.com/Unicorn-Academy-Game/Unicorn-Academy-Game.github.io I will make everything fully open-source once i polish the educational engine. Overall I'm just INSANELY impressed by what Sonnet can do. I haven't felt like this since I was a teenager coding bots doing Mephisto runs in Diablo 2. I'm going to start making silly games for myself when I have the time :D And this game will probably be growing up with my daughter and develop into an open world game to help her with reading/writing/math skills. This is fan-made and inspired by characters from a book/Netflix series I don't own (Unicorn Academy). The Phaser engine and the Fredoka font are the only parts not made by Sonnet here. Well, and all the other open source libraries. But no other 3rd party graphical assets were used. I'm not a fan of image-gen. I like everything procedural. I'm here to answer any questions about prompting, planning, skills I'm using, etc. Ask me anything. Edit: look into https://github.com/cursor/plugins/tree/main/pstack . it's a game-changer, imo. there is a claude version.
