---
id: "bf42968ff81ca20c"
title: "I used Codex to revive Pro Pinball - The Web (1995)"
url: "https://reddit.com/r/ChatGPT/comments/1xpoi08/i_used_codex_to_revive_pro_pinball_the_web_1995"
link: "https://reddit.com/r/ChatGPT/comments/1xpoi08/i_used_codex_to_revive_pro_pinball_the_web_1995"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-06T21:19:34Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["rnatau"]
language: "en"
summary: "Inspired by posts about AI being used to reverse engineer this and re-implement that I decided to take on a real love project of mine - transporting the pinball classic \"Pro Pinball - The Web\" (1995) into the present. A game I spent so many hours on back then, I even tried recreating that feeling by setting up a retro PC with Windows 98. However it would just never run right, neither on that…"
tags: ["r/ChatGPT"]
orgs: []
topics: []
content_source: "post"
word_count: 572
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1xpoi08/i_used_codex_to_revive_pro_pinball_the_web_1995/"
score: null
comments: null
community: "r/ChatGPT"
---

# I used Codex to revive Pro Pinball - The Web (1995)

Reddit · rnatau · 2026-11-06

Inspired by posts about AI being used to reverse engineer this and re-implement that I decided to take on a real love project of mine - transporting the pinball classic "Pro Pinball - The Web" (1995) into the present. A game I spent so many hours on back then, I even tried recreating that feeling by setting up a retro PC with Windows 98. However it would just never run right, neither on that Win98 machine nor in DosBox. So yeah, I used Codex (Sol 6.1 High) to reverse engineer the game in the hopes of reviving one of "my" greatest games. The process was quite straight forward - in relatively small steps I'd ask Codex to analyze and recreate parts. Physics first, then animations, towards the first playable demo... I spent quite a lot of time playtesting to make sure everything had been gotten right. The first playable version was fixed to 1024x768, that was just too small on a modern PC, so "we" implemented scaled full screen, which made the dot matrix display look like ***. Codex had the great idea to not scale that one but redraw it, so now it looks crisp and awesome. I was impressed the most by the methodology Codex used - disassemble, create unit tests out of parts running in an emulator, and most importantly, run extensive gameplay simulations and compare them frame by frame with the same sequences from the original game. After the game had reached a fully faithful state I decided to make an enhanced version where some kinks were ironed out, e.g. that missions could not be interrupted by other events, the game would not silently restart when pressing start during a running game... But most importantly we modified the engine so that the 60 Hz game loop with 17 microsteps (i.e. a 1020 Hz physics engine, in 1995!!!) would use frame sync and just draw the current state whenever needed. And really, 175 Hz gameplay in this game is just something else entirely and makes the whole thing so worth it! There were only few issues - sometimes Codex would play a bit dumb, e.g. with the frame sync I had to explain it that it should be able to calculate the microsteps just up until that time where we are at, that it does not necessarily have to calculate all 17 of them at the same time - i.e. that we *can* effectively increase the FPS. Also the DMD menu flow in the enhanced edition is still a bit bumpy because I did not take the time to specify it myself, so those parts are feeling a bit viby still. I also realized why it never ran nicely on Win98 - even the first playable demo I got had the same issue, as apparently the window timer has too much jitter. Codex however identified and fixed the issue quickly after my protests, just as it did with the weird every-second-stutter I observed after adding gamepad support. The result is free and open source, and there are ready-to-run Windows and Linux binaries. You'll need the original game's data files, though - those you can get from archive.org. Source and binaries here: https://github.com/rnatau/theweb If anyone remembers playing The Web back in the day, I'd love to hear what you think. And if you give it a try, feedback is very welcome! It'll forever be work in progress, I guess ;-)
