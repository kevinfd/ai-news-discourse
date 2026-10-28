---
id: "051981ed2e8cd2b8"
title: "I started from Anthropic's Slack GIF skill and ended up with a Python rig for anime punch barrages (no After Effects)"
url: "https://reddit.com/r/ClaudeAI/comments/1xh04rm/i_started_from_anthropics_slack_gif_skill_and"
link: "https://reddit.com/r/ClaudeAI/comments/1xh04rm/i_started_from_anthropics_slack_gif_skill_and"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T18:12:54Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["AnonymousClaudeuser"]
language: "en"
summary: "I draw the parts by hand. Claude rigs them in Python. No After Effects, no image generation: it only moves drawings that already exist. How it started: Anthropic ships an example skill called slack-gif-creator. I'm a nerd, so of course I opened it. Problem:I had no idea what a Slack emoji even was cause we don't use Slack where I'm from, so I just kept bending it into an animation tool. A few…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 404
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xh04rm/i_started_from_anthropics_slack_gif_skill_and/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I started from Anthropic's Slack GIF skill and ended up with a Python rig for anime punch barrages (no After Effects)

Reddit · AnonymousClaudeuser · 2026-10-27

I draw the parts by hand. Claude rigs them in Python. No After Effects, no image generation: it only moves drawings that already exist. How it started: Anthropic ships an example skill called slack-gif-creator. I'm a nerd, so of course I opened it. Problem:I had no idea what a Slack emoji even was cause we don't use Slack where I'm from, so I just kept bending it into an animation tool. A few weeks in... even Claude forgot it was ever an emoji tool. GPT was the one who found it in the code. (That's also why my early lines looked jaggy: the emoji preset quantized everything to 48 colors. A 255-color palette fixed it.) Anyway, all the GIFs in this post were made with this skill. The only thing I did in CapCut was add the subtitles. What it does now: - Parent-child rigs, with parts that detach and re-attach mid-shot - Fake-3D turns, a spinning globe, a 3D stadium folded out of a flat drawing - Punch barrages Claude writes the rigs, GPT reviews the code, and Claude re-runs everything on other drawings to make sure it's not a one-off. Things we learned the hard way: - Almost all of it is one trick: divide by depth. Turns, tapers, the globe, the floor and the punches are all the same division. - The part that moves is the parent, not the part that grabs. - Motion blur only works on the same drawing. Average two different drawings and you get a ghost, so pose swaps are hard cuts. - A punch has to end about 1.75x past the screen edge. If it stops at the edge, it reads as "arriving". - Looking at images is the expensive part. Claude diffs the frames and only looks at the spikes. My first try was in Claude Design back in early September. It never asked, kept rewriting things I didn't ask for, and ate my whole weekly limit. It asks more now. It still thinks its opinion matters more than mine. The skill is free (MIT): https://github.com/TheSingularityIsRightAroundTheCorner/animation-meme-rig If you make an anime meme with it, I want to see it. One thing I haven't solved: camera moves. Right now I paint a red box where the camera starts and a blue box where it ends. Very advanced technology. If you know a better way to block camera moves in code, tell me. Full making-of: https://www.youtube.com/watch?v=7Ok7jbB9xaE
