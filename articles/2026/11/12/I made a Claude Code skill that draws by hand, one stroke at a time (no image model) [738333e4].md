---
id: "738333e4e922c7e6"
title: "I made a Claude Code skill that draws by hand, one stroke at a time (no image model)"
url: "https://reddit.com/r/ClaudeAI/comments/1xuqprd/i_made_a_claude_code_skill_that_draws_by_hand_one"
link: "https://reddit.com/r/ClaudeAI/comments/1xuqprd/i_made_a_claude_code_skill_that_draws_by_hand_one"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T22:26:08Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["jchapuis"]
language: "en"
summary: "This is drawing , a Claude Code skill. You put a picture in a folder as subject.png and ask Claude to draw it. No image model is involved. Claude types every stroke as coordinates in a Python script, and a headless tldraw canvas renders them. The video replays the ~350 strokes it typed for this house, in order. It works the way a drawing class teaches: a few loose lines first, then straight…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 303
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xuqprd/i_made_a_claude_code_skill_that_draws_by_hand_one/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made a Claude Code skill that draws by hand, one stroke at a time (no image model)

Reddit · jchapuis · 2026-11-12

This is drawing , a Claude Code skill. You put a picture in a folder as subject.png and ask Claude to draw it. No image model is involved. Claude types every stroke as coordinates in a Python script, and a headless tldraw canvas renders them. The video replays the ~350 strokes it typed for this house, in order. It works the way a drawing class teaches: a few loose lines first, then straight lines to get the proportions right, then colour, ink, and a finish (watercolour here). After each stage it compares its render with the subject before going on. One of the checks is a second Claude that never sees the subject and only describes what the drawing shows. If that description doesn't match the subject's, it's back to work. How Claude helped build it: I built the skill with Claude Code as well. I ran it on subject after subject (a rooster, a dog, a portrait, a bicycle, this house), and each time a drawing went wrong, we turned the failure into a rule or a check. Keeping it honest took the longest. Left alone, Claude will happily write a loop or trace the photo and call that a drawing. So the pen now refuses any script whose strokes come from a loop, another file or mostly computed numbers. Every point is typed out. Caveats: It's slow and hungry: roughly 350-450k tokens for one object, a few million for a full scene. A busy scene gets split across several agents, one per object, which is where the millions come from. It needs Python (numpy, scipy, pillow, opencv) and Node for the canvas. It's free and open source (MIT). Install: /plugin marketplace add jchapuis/drawing-skill /plugin install drawing@drawing-skill Repo, gallery and how it works: https://github.com/jchapuis/drawing-skill Feedback welcome, maybe you find this experiment interesting.
