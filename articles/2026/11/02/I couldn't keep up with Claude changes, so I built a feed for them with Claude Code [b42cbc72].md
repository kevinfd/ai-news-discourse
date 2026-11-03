---
id: "b42cbc72460a7072"
title: "I couldn't keep up with Claude changes, so I built a feed for them with Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1xm471k/i_couldnt_keep_up_with_claude_changes_so_i_built"
link: "https://reddit.com/r/ClaudeAI/comments/1xm471k/i_couldnt_keep_up_with_claude_changes_so_i_built"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T17:52:54Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["liorgrossman"]
language: "en"
summary: "I build on Claude every day, and I still can't keep up with what changes. In April that really cost me - a feature in one of my products was broken for 48 hours because Anthropic shut down claude-3-haiku. Anthropic had announced it two months earlier, but I somehow missed that. Having multiple products, I spend time every month chasing deprecations and model updates, which has become…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Microsoft"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 298
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xm471k/i_couldnt_keep_up_with_claude_changes_so_i_built/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I couldn't keep up with Claude changes, so I built a feed for them with Claude Code

Reddit · liorgrossman · 2026-11-02

I build on Claude every day, and I still can't keep up with what changes. In April that really cost me - a feature in one of my products was broken for 48 hours because Anthropic shut down claude-3-haiku. Anthropic had announced it two months earlier, but I somehow missed that. Having multiple products, I spend time every month chasing deprecations and model updates, which has become overwhelming. To solve my own problem, I decided to build Modelpeers (free). You follow the models, tools, and agents you use, like Claude Code or Opus 5.5, and every change shows up in one feed: what changed, what it means for you, what to do, and a link to the source. There's also an optional weekly email. At this point, I don't write code by hand anymore. Claude Code (mostly Opus 5.5 High, with Fable 5.1 as a second opinion) built the whole site from my specs, from the follow feed to the profile pages. The catalog itself comes from research sessions I run with Claude: it reads each company's changelogs, deprecation pages and status pages, and drafts every entry with the date, what changed, what to do and the source link, which I review before it goes live. Four Claude changes from the past couple of weeks: API version 2026-10-21 makes temperature , top_p and top_k return a 400 error. If you upgrade to the new SDKs, drop those parameters or pin the older API version. Claude Sonnet 4.5 retires on November 30. Opus 4.8 fast mode ends on November 30. Requests with fast speed will error after that. GitHub Copilot removes Claude Opus 4.8 and Opus 5 on November 16. Here's everything changing at Anthropic on Modelpeers. Would appreciate your thoughts. What would make it more useful for you?
