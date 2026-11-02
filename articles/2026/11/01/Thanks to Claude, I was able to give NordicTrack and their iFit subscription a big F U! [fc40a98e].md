---
id: "fc40a98efc180758"
title: "Thanks to Claude, I was able to give NordicTrack and their iFit subscription a big F U!"
url: "https://reddit.com/r/ClaudeAI/comments/1xlg9nd/thanks_to_claude_i_was_able_to_give_nordictrack"
link: "https://reddit.com/r/ClaudeAI/comments/1xlg9nd/thanks_to_claude_i_was_able_to_give_nordictrack"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T22:22:22Z"
published_date: "2026-11-01"
collected_at: "2026-11-02T13:05:12Z"
authors: ["Beloved_Misanthrope"]
language: "en"
summary: "*Edit (link to repo): https://github.com/Crawler757/treadmill-home My GF bought a NordicTrack Commercial 2250 a couple of years ago, and the feature we were most excited about was the big screen that would let us watch our streaming services while working out. What we didn’t know is that everything beyond the basic workout controls is locked behind an iFit subscription, even streaming services…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 639
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlg9nd/thanks_to_claude_i_was_able_to_give_nordictrack/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Thanks to Claude, I was able to give NordicTrack and their iFit subscription a big F U!

Reddit · Beloved_Misanthrope · 2026-11-01

*Edit (link to repo): https://github.com/Crawler757/treadmill-home My GF bought a NordicTrack Commercial 2250 a couple of years ago, and the feature we were most excited about was the big screen that would let us watch our streaming services while working out. What we didn’t know is that everything beyond the basic workout controls is locked behind an iFit subscription, even streaming services you already pay for. Even for basic use you have to wait for iFit to load, and there’s no escaping its intrusive ads. It turns out that screen is just an Android 9 tablet running iFit’s software. I wanted Netflix and Crunchyroll on it without giving up the motor, so I sat down with Claude Code and a CLAUDE.md file as the project’s running memory, and over about a day and a half we got it all working. What we ended up with: A home screen app I own with big tiles for Netflix and Crunchyroll. There’s no iFit login, no ads, and no membership nags. A floating bar over whatever is playing with speed, incline, time, and distance, plus a quarter-mile track panel with laps and pace. On-screen Start, Pause, Stop, and speed and incline buttons. The physical buttons still work too. Netflix starts in about 21 seconds, down from close to a minute. How the work went: Claude did the discovery over ADB and found that iFit’s motor service runs a small server on the console that apps can talk to. It followed how the open source QZ (qdomyos-zwift) project talks to it and wrote the client from scratch in plain Java. Big shout out to the QZ folks, because none of this happens without their work. We disabled iFit’s apps one at a time with a health check on the motor service after each. Some of that went wrong: one app killed the motor service, and another attempt took half an hour to undo. Each time Claude wrote the lesson into CLAUDE.md and the next session followed it. The real fix was removing iFit’s lockdown and updater app for my user (reversible). It turned remote access off after every restart, re-enabled everything I’d disabled, and ate a big share of the CPU. Without it the treadmill boots unlocked and the tablet can finally breathe. Favorite catch: a test script helper named Rd was silently treated as PowerShell’s alias for Remove-Item. Nothing got deleted, but Claude caught it in the logs. Where Opus 5.5 refused commands: I wanted our own motor driver that talks straight to the motor board. Claude wouldn’t work out the board’s security handshake from iFit’s code, since it saw that as getting around an authentication check. I was a little disappointed, but I get it, so we stuck with iFit’s motor service. It wouldn’t start the belt remotely for testing at first. I basically had to argue that it was safer for me not to be standing on it: “I can always unplug it if something goes haywire, and in the worst case scenario of the treadmill exploding, shouldn’t it run remotely in the basement instead of me being there with it?” After that it agreed, as long as I confirmed nobody was near the treadmill. Every remote test had a speed cap, a stop command that runs even if the script fails, and a check that the speed reads zero at the end. The safety key and the console’s Stop button stayed the real way to stop. The overlay is never trusted with that. The catches: Netflix plays in SD (Widevine L3), the tablet is slow no matter what, and a factory reset could wipe it all. It’s a treadmill, I’ll live. We paid for the treadmill, the screen, and the motor, so paying monthly to use a screen we already own never sat right with me. Happy to answer questions!
