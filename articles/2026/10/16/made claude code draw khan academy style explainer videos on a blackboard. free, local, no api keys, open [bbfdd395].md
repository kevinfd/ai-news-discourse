---
id: "bbfdd3955347f4c3"
title: "made claude code draw khan academy style explainer videos on a blackboard. free, local, no api keys, open source"
url: "https://reddit.com/r/ClaudeAI/comments/1x7lhrq/made_claude_code_draw_khan_academy_style"
link: "https://reddit.com/r/ClaudeAI/comments/1x7lhrq/made_claude_code_draw_khan_academy_style"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T16:52:47Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["_haiderfarooq"]
language: "en"
summary: "you type a prompt, claude code writes a scene file, and one command renders an mp4 where a pen draws on a blackboard while a voice explains it. i open-sourced the skill: https://github.com/haiderfarooq3/khan-explainer Here's a 65-second video the skill drew about itself: https://youtu.be/JD9OirRC3YE What it makes: Blackboard or whiteboard lessons, drawn stroke by stroke Draw-over-UI tutorials:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["search & media"]
content_source: "post"
word_count: 276
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x7lhrq/made_claude_code_draw_khan_academy_style/"
score: null
comments: null
community: "r/ClaudeAI"
---

# made claude code draw khan academy style explainer videos on a blackboard. free, local, no api keys, open source

Reddit · _haiderfarooq · 2026-10-16

you type a prompt, claude code writes a scene file, and one command renders an mp4 where a pen draws on a blackboard while a voice explains it. i open-sourced the skill: https://github.com/haiderfarooq3/khan-explainer Here's a 65-second video the skill drew about itself: https://youtu.be/JD9OirRC3YE What it makes: Blackboard or whiteboard lessons, drawn stroke by stroke Draw-over-UI tutorials: arrows, circles and numbered steps over your own product screenshots "Khanify" a YouTube video: it keeps the speaker's real voice and draws the board to their words. One 20-minute talk gave me 22 vertical clips. How Claude is used: the skill is a SKILL.md plus a renderer (HTML canvas, Playwright, ffmpeg, the Mac's built-in say voice). Claude reads the rules, writes the beats (one spoken clause + the drawing for it), renders, then reads a contact sheet of every beat and fixes overlaps or text off the board before it shows you anything. A render takes seconds so it iterates 3-4 times on its own. The thing that makes it work: the voice drives the clock. Each line is spoken and measured first, then the pen gets exactly that long to draw it. Nobody types timestamps, so the drawing can't run ahead of the words. Free to try, MIT, no accounts or keys. macOS only right now (the free voice is say ). Optional ElevenLabs voice if you want it to sound human. Not affiliated with Khan Academy, the name describes the look. I wrote up the tricks that transfer to any content skill (self-grading output, caching the expensive step, measuring instead of eyeballing coordinates) here: https://haiderfarooq.dev/blog/claude-code-skills-for-content Happy to answer questions about how the timing or the capture recipe works.
