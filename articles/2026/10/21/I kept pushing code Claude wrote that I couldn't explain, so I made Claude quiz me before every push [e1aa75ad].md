---
id: "e1aa75ad63a8b620"
title: "I kept pushing code Claude wrote that I couldn't explain, so I made Claude quiz me before every push"
url: "https://reddit.com/r/ClaudeAI/comments/1xbjn2x/i_kept_pushing_code_claude_wrote_that_i_couldnt"
link: "https://reddit.com/r/ClaudeAI/comments/1xbjn2x/i_kept_pushing_code_claude_wrote_that_i_couldnt"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T10:36:09Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["NthOfHisName"]
language: "en"
summary: "After a few months of Claude Code doing most of my typing, I noticed something uncomfortable: my PRs looked fine, but if a teammate asked me \"why this approach?\" I had to go read my own code first. So I built grip, a git pre-push hook. It reads your diff, asks five questions about it, and grades your answers. Below the pass mark, the push waits. ​The Claude part: It uses your existing Claude…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 183
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbjn2x/i_kept_pushing_code_claude_wrote_that_i_couldnt/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I kept pushing code Claude wrote that I couldn't explain, so I made Claude quiz me before every push

Reddit · NthOfHisName · 2026-10-21

After a few months of Claude Code doing most of my typing, I noticed something uncomfortable: my PRs looked fine, but if a teammate asked me "why this approach?" I had to go read my own code first. So I built grip, a git pre-push hook. It reads your diff, asks five questions about it, and grades your answers. Below the pass mark, the push waits. ​The Claude part: It uses your existing Claude Code install as the model, so no API key needed. There's a /grip skill: Claude asks you the questions in chat, and it's told to never answer them for you. There's a gate that stops Claude itself from running git push until you've passed. The newest mode draws your change as a whiteboard in the browser and pins the questions on it, inspired by Mitchell Hashimoto's "whiteboard defense" post. Free, open source, Python: github.com/guilyx/grip Try it offline first if you're curious: pipx install grip-hook, then grip quiz --provider fake in a test repo. Curious if anyone else has a ritual for this, or if you just trust the tests.
