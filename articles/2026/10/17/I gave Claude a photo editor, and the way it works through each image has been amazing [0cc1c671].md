---
id: "0cc1c67182e05bf8"
title: "I gave Claude a photo editor, and the way it works through each image has been amazing"
url: "https://reddit.com/r/ClaudeAI/comments/1x89ggt/i_gave_claude_a_photo_editor_and_the_way_it_works"
link: "https://reddit.com/r/ClaudeAI/comments/1x89ggt/i_gave_claude_a_photo_editor_and_the_way_it_works"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T12:49:40Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["fcf41"]
language: "en"
summary: "I built Editmamei Connect , a remote MCP server that lets Claude edit photos the traditional way, with layers, masks and curves, instead of regenerating them. You add it as a custom connector and edit from any Claude app, including your phone, with nothing to install. You send Claude a photo and describe the edit the way you'd brief an editor. Claude picks the tools, checks a preview between…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Meta"]
topics: ["agents & coding", "products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 456
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x89ggt/i_gave_claude_a_photo_editor_and_the_way_it_works/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I gave Claude a photo editor, and the way it works through each image has been amazing

Reddit · fcf41 · 2026-10-17

I built Editmamei Connect , a remote MCP server that lets Claude edit photos the traditional way, with layers, masks and curves, instead of regenerating them. You add it as a custom connector and edit from any Claude app, including your phone, with nothing to install. You send Claude a photo and describe the edit the way you'd brief an editor. Claude picks the tools, checks a preview between steps, and hands back a JPEG or a layered PSD you can keep working on. It can also lay out Instagram stories and carousels, and put product shots on a clean background for listings. The video is one real edit. The fun part was watching Claude catch its own mistake: it darkened the sky by pulling down the blues, checked a preview, saw it had turned the grey lava field into blotchy bands, put it all back, and masked the sky with an AI selection instead. I built this with Claude Code, building off my local desktop version. I wanted to move it into the cloud so I could edit anywhere, not just at my desktop. I was able to port over a lot of the same tools from the local side, but faced a whole new challenge in figuring out how to actually put a photo editor in the cloud as a remote MCP server. Over the past few weeks I worked through hosting all of it on Cloudflare, with an architecture that uses everything from Durable Objects to R2 object storage to the containers that run the editor itself, plus building sign-in, accounts and a whole ecosystem around the core job of editing photos. I wanted to make sure it could scale, so every user gets their own dedicated container that spins up for their edit. Multiple people can edit at the same time without competing for the same resources, and each person's edits run in their own container. Since Opus 5.5 came out, it's also been building my videos, like the one attached here. It uses the photo editor I gave it to make all the edits, makes the stills and frames, and merges them with HTML into the animated video. That's been an awesome way to share the work and show people how to set it up and get going. The AI selection tools still need refinement to match Adobe quality. Fine edges and complex subjects, like a bouquet of flowers, don't always come out clean, and that's what I'm working on next. It's free to try. New accounts get free credits that top up every month, and there are paid packs if you want more. To try it out, add this as a custom connector in Claude: https://connect.editmamei.com/mcp More about it: editmamei.com/connect
