---
id: "60c1f05da25b1be5"
title: "13 months with Claude Code: MMM, my kitchen management app, is officially launched (UPDATE POST)"
url: "https://reddit.com/r/ClaudeAI/comments/1xor1tv/13_months_with_claude_code_mmm_my_kitchen"
link: "https://reddit.com/r/ClaudeAI/comments/1xor1tv/13_months_with_claude_code_mmm_my_kitchen"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T18:58:08Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["spectrefax"]
language: "en"
summary: "https://www.mealsmealsmeals.com/ 3 months ago I shared what I was building with Claude in this thread: 10 months and counting with Claude Code to build a full kitchen management system to take the pain out of home cooking and planning. I said I couldn't wait to do it again in a few months, and now I'm back. Quick recap: I started with basically zero SaaS knowledge and used Claude Web and Claude…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 631
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xor1tv/13_months_with_claude_code_mmm_my_kitchen/"
score: null
comments: null
community: "r/ClaudeAI"
---

# 13 months with Claude Code: MMM, my kitchen management app, is officially launched (UPDATE POST)

Reddit · spectrefax · 2026-11-05

https://www.mealsmealsmeals.com/ 3 months ago I shared what I was building with Claude in this thread: 10 months and counting with Claude Code to build a full kitchen management system to take the pain out of home cooking and planning. I said I couldn't wait to do it again in a few months, and now I'm back. Quick recap: I started with basically zero SaaS knowledge and used Claude Web and Claude Code to learn as I built. MMM is a full-stack app that takes the pain out of being the main cook for a family. It helps you decide what to eat, keeps you on budget, writes your shopping list, and tracks your pantry automatically as you shop and cook. I got a bit roasted in the original thread, but was grateful for the feedback and I listened to it. Updates since last post: - Complete overhaul of UI to make it much easier to read and use. - " How It Works " page to explain how to use MMM and what it does. - Nutrition data on every card that updates automatically when you change servings or swap sides. - Allergen alerts and filters, per browsing session or account-wide. - Add to Walmart cart. - Menu sharing with a custom link and a generated preview image. - Recipe submissions, user profiles, and quite a bit more. Pricing is still US only, and shopping lists are built from Walmart products. But you can tell the shopping list you bought an item anywhere, so it works at other stores too. The app doesn't care what kind of garlic powder you bought, just that you got the amount the recipe needs. It's free to use with one menu you can reset infinitely, so please do play around with it. (Note: Walmart carts do not have a 'remove all items' option, so anything sent will need to be removed one-by-one if you send a cart without intending to use it.) Lessons I learned with Claude: I did basically all the design work myself and used Claude to translate it into code. That's partly why this took so long: the early phase was a lot of having the AI teach me what I needed to know to make design decisions (AI is probably the most advanced teaching tool humanity has ever built). Know the answer: Ambiguity is deadly for AIs. The backend of this project is pretty intricate, and I quickly learned that if I hadn't fully solved a design before handing it to Claude to code, he'd fill in the ambiguous parts with whatever he came up with. Shorter, more direct MDs win: I tried several versions of MD files to streamline the workflow with Claude, and quickly realized that once an MD gets past a certain size, he just stops bothering with it. "This is written in the MD, but I missed it and did what it says not to do anyway. My bad, haha." Commits save the day: Basically I just use commits like save states in a video game. These are highly valuable for a new coder like myself. Gate Access HARD: After seeing too many threads about AIs accidentally deleting people's whole projects, I set strict rules in my CLAUDE.md. He can read and edit the code, but deploys and anything that writes to the database need my explicit sign-off every single time. It seems tedious, but to me it's quality control and insurance more than anything. Hopefully this update thread will have more praise than roasts, but feedback of any kind is welcome, especially from anyone who's the main cook at home. Hope it helps someone, or inspires your own build. Thanks again to this community, and if you have any decent recipes, please submit them ALL! :)
