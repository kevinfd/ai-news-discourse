---
id: "7ecf17b1a26ddf05"
title: "I asked Fable 5.2 to mash up Balatro and Diablo II. Things got out of hand."
url: "https://reddit.com/r/ClaudeAI/comments/1xwzel1/i_asked_fable_52_to_mash_up_balatro_and_diablo_ii"
link: "https://reddit.com/r/ClaudeAI/comments/1xwzel1/i_asked_fable_52_to_mash_up_balatro_and_diablo_ii"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-15T16:14:58Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["AccountlKiller"]
language: "en"
summary: "Game: DarkPattern Play it here: https://darkpattern.diamonddoge.org/ UI updated — say no to slop! The 日本語 version is now live! First of all, thanks to Anthropic for giving me three resets, all of which I managed to burn through in a single weekend working on this game. My original idea was simple: combine my two favorite games (Balatro and Diablo II) with my most hated game (Path of Exile).…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["jobs & society"]
content_source: "post"
word_count: 439
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xwzel1/i_asked_fable_52_to_mash_up_balatro_and_diablo_ii/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I asked Fable 5.2 to mash up Balatro and Diablo II. Things got out of hand.

Reddit · AccountlKiller · 2026-11-15

Game: DarkPattern Play it here: https://darkpattern.diamonddoge.org/ UI updated — say no to slop! The 日本語 version is now live! First of all, thanks to Anthropic for giving me three resets, all of which I managed to burn through in a single weekend working on this game. My original idea was simple: combine my two favorite games (Balatro and Diablo II) with my most hated game (Path of Exile). Instead of writing a detailed prompt, I had Fable interview me. It could ask up to 10 questions, then another 5, and another 3, until it had nothing left to ask. Then I handed it full control and went to bed. Our conversations went something like this: Claude Code: What kind of art style do you want? Me: Something pixel-art-ish, but not too pixel-art-ish. (Yes, I realize I sound like the world's dumbest product manager.) I also gave it an OpenRouter API key with $7 left and told it to generate images first, voiceovers second, and if it ran out of money, just draw everything itself in SVG. Then I woke up to the first version. It looked nothing like a game. It looked like a SaaS dashboard. I yelled, "THIS IS NOT A GAME! THIS IS A SAAS DASHBOARD!" Fable documented the incident in its dev log: "The user is angry. They said what I built isn't a game, but a SaaS dashboard." Starting the next day, things got a little more normal. To be fair, Fable had actually done a great job with the game engine. Most of the work was redesigning the UI and removing all the decorative stuff it loved and I hated. The real challenge was balancing. We built bots to test win rates across different card hands, and I also sent the game to three friends for feedback. Friend #1: "Way too hard. Practically impossible." Friend #2: "I'm one-shotting everything. Too easy. Boring." Friend #3: "Seems just right." So that round of human playtesting was completely useless. Naturally, I went back to running 600 bots through tens of thousands of simulated games. And that's what I'm sharing today, after another full day of testing and tweaking. I think we've pretty much achieved the original goal: Looks like Balatro, feels like Diablo II, and steals some ideas from Path of Exile. The game is called Dark Pattern , named after that famous Chris Wilson video on YouTube. But don't worry, there are no payment buttons in this game. It can't take your money. Only your time. P.S. Fable 5.2 burned all my tokens, so I had to bring in Opus 5.5 for the final code review.
