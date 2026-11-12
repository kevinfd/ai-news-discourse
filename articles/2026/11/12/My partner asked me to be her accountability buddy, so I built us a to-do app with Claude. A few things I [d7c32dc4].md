---
id: "d7c32dc44a166c5c"
title: "My partner asked me to be her accountability buddy, so I built us a to-do app with Claude. A few things I learnt along the way"
url: "https://reddit.com/r/ClaudeAI/comments/1xu0d4x/my_partner_asked_me_to_be_her_accountability"
link: "https://reddit.com/r/ClaudeAI/comments/1xu0d4x/my_partner_asked_me_to_be_her_accountability"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T01:58:17Z"
published_date: "2026-11-12"
collected_at: "2026-11-12T13:04:19Z"
authors: ["DjOwlz"]
language: "en"
summary: "My partner asked me to be her accountability buddy, to help her keep track of her daily tasks. We started out editing a message on Discord, which felt a bit silly given I’m a developer. So I one shot her a quick to do app with Claude, and it’s grown with whatever she’s asked for since. I make games for a living, so this was never meant to be a commercial thing, it was just for someone I care…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 504
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xu0d4x/my_partner_asked_me_to_be_her_accountability/"
score: null
comments: null
community: "r/ClaudeAI"
---

# My partner asked me to be her accountability buddy, so I built us a to-do app with Claude. A few things I learnt along the way

Reddit · DjOwlz · 2026-11-12

My partner asked me to be her accountability buddy, to help her keep track of her daily tasks. We started out editing a message on Discord, which felt a bit silly given I’m a developer. So I one shot her a quick to do app with Claude, and it’s grown with whatever she’s asked for since. I make games for a living, so this was never meant to be a commercial thing, it was just for someone I care about. It’s now a shared to do list for two people. One keeps today’s list, the other sees it change live and can send a note or an emoji. You can try both sides with made up data, no sign-up: https://www.todaytogether.co.uk/?try What I’ve learnt working with Claude on it: Keep a handover doc and make Claude maintain it. I tell Claude to write everything back to a handover.md (how the project fits together, decisions made, what’s left to do) and to keep it up to date as it goes. That way nothing lives only in one chat’s memory. I’d learnt this on other projects and have only just started doing it here, because for a long time it was just a small side project. Scope it and review it before anything gets built. I make Claude write out the plan and then review it before any code gets written. Once there’s a written scope, you can split the project into parts and hand them to different Claude instances, one to talk through the design, another to write the code. Your own judgement still matters. Claude gets things wrong, and having been a game developer since before Claude existed, I can usually tell what is and isn’t right. The same goes for feedback. Years of watching players test games helps you work out which feedback to act on and which to quietly ignore, even when the tester is your partner :) A couple of things Claude built that I liked: The demo runs on an in-memory stand-in for the Supabase client with the same API, so it’s the real app code and nothing gets sent anywhere. The promo video and screenshots are recorded from the same demo, so they can’t show features that don’t exist. Every database migration has tests against a real in-process Postgres (PGlite). They caught a bug where deleted tasks kept coming back the next day. Where it got it wrong: It fought me all the way on using PIXI.js for the garden. I knew I wanted a rich WebGL environment, that could render a lot of sprites using a texture atlas. It felt it would load too slowly, and wasn't needed. But from experience I knew it's super lightweight and would scale well with particles and lots of sprites. It's important to know when you are right, and use the experience you already have to call the shots. Happy to answer questions about the workflow. And if you try the demo, I’d love to know whether it makes sense without any explanation.
