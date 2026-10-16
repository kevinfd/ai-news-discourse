---
id: "eb72dd5c230337ed"
title: "Don't just build output, build tooling"
url: "https://reddit.com/r/ClaudeAI/comments/1x4s8zh/dont_just_build_output_build_tooling"
link: "https://reddit.com/r/ClaudeAI/comments/1x4s8zh/dont_just_build_output_build_tooling"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T09:40:09Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["CobaltThunder"]
language: "en"
summary: "I've been seeing some of the examples of how good Opus 5.5 is at doing programmatic content generation, and built myself a little tool for custom invites / flyers. How I architected it: - Asked Claude code to build me a simple web app with rich text editing and text box positioning, as well as PDF / PNG exports - Have the graphics of each invite be generated as SVGs and laid out on a HTML…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "jobs & society"]
content_source: "post"
word_count: 245
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x4s8zh/dont_just_build_output_build_tooling/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Don't just build output, build tooling

Reddit · CobaltThunder · 2026-10-13

I've been seeing some of the examples of how good Opus 5.5 is at doing programmatic content generation, and built myself a little tool for custom invites / flyers. How I architected it: - Asked Claude code to build me a simple web app with rich text editing and text box positioning, as well as PDF / PNG exports - Have the graphics of each invite be generated as SVGs and laid out on a HTML canvas, keeping claude in a loop to 'view' the generated output with playwright and iterate until it thinks its done a good job. Further iteration of the graphics is done via prompting rather than in the web app - The web app tooling for text editing / positioning allows me to avoid some of the pitfalls of prompting AI image models with large quantities of text and iterating, as well as giving me more human level control over what I need it to say and make quick edits without burning more tokens. I'm super happy with the results I'm getting (tried it with a few different invite formats now, the web app basically saves them all as templates i can reuse if needed) - the invites are very high quality and the SVG graphics mean I can export losslessly. Biggest lesson for me is to think about prompting for tooling, not just for output, so that you can make useful edits in ways you can predict without more tokens.
