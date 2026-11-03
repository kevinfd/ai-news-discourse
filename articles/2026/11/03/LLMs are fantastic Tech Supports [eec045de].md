---
id: "eec045de22ecf0d7"
title: "LLMs are fantastic Tech Supports"
url: "https://reddit.com/r/singularity/comments/1xmqc97/llms_are_fantastic_tech_supports"
link: "https://reddit.com/r/singularity/comments/1xmqc97/llms_are_fantastic_tech_supports"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T11:18:28Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["KrydanX"]
language: "en"
summary: "I had an issue with my MacBook Pro M4 since MacOS27 - an external monitor (connected via HDMI) that used to work all the time with previous versions of macOS suddenly had massive issues, not being recognised, not having the right settings, defaulting back to some weird settings as much as only mirroring a quarter of my built in monitor, bugging out my display settings and the whole around it. I…"
tags: ["r/singularity"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 346
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xmqc97/llms_are_fantastic_tech_supports/"
score: null
comments: null
community: "r/singularity"
---

# LLMs are fantastic Tech Supports

Reddit · KrydanX · 2026-11-03

I had an issue with my MacBook Pro M4 since MacOS27 - an external monitor (connected via HDMI) that used to work all the time with previous versions of macOS suddenly had massive issues, not being recognised, not having the right settings, defaulting back to some weird settings as much as only mirroring a quarter of my built in monitor, bugging out my display settings and the whole around it. I spend multiple hours trying to fix it. All the usual stuff, resetting this, resetting that, trying different solutions offered all around the internet, no success. I gave up, used my iPad as a second monitor and called it a day. Funny enough, on the MacBook of my wife (M3, macOS 27) it was working just fine. Even with the help of Claude, using everything the internet suggested, it didn’t work. Used BetterDisplay, went deep into deleting Color/Display profiles, nothing. Then we checked the EDID and found out, there is something broken there, the monitor is sending a buggy EDID that had 2 broken bytes in them - not me finding it out, it happened when I send Claude the Log/Screenshots. It immediately pointed out that what’s being send is broken. 10 seconds later he created a fitting EDID Bin/Profile for me, I plugged it in - worked flawless. I spend HOURS on research, debugging, problem solving - the moment I gave Claude some more informations, showed it some screenshots and let it handle it, it fixed it within seconds. I was about to give it up and just live with it, waiting for maybe the next MacOS version or just buying a new monitor. I’m pretty sure a standard hardware store or even the apple support wouldn’t help me with this and suggesting getting a new monitor or wait for an update. Claude just wrote a proper EDID profile and fixed it. TLDR; My Monitor had an EDID issue ever since, macOS 27.0 and before handled it, the new macOS was too picky and refused to work. Claude correctly found it, fixed it in seconds.
