---
id: "661776efa62d6bdf"
title: "I made Claude sign up for my app as a brand-new user and tell me everywhere it got stuck"
url: "https://reddit.com/r/ClaudeAI/comments/1x5eblc/i_made_claude_sign_up_for_my_app_as_a_brandnew"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T01:16:20Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["New_Term_4269"]
language: "en"
summary: "I built a connector that turns Claude into a product tester. You tell it who to be, like “a busy parent signing up for the first time” or “a founder comparing us to a competitor,” and point it at your site. It signs up, tries to do real things, screenshots every step, and hands back a review ranked by what actually blocks people. It does teardowns too: homepage, pricing page, or a side-by-side…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 228
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x5eblc/i_made_claude_sign_up_for_my_app_as_a_brandnew/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made Claude sign up for my app as a brand-new user and tell me everywhere it got stuck

Reddit · New_Term_4269 · 2026-10-14

I built a connector that turns Claude into a product tester. You tell it who to be, like “a busy parent signing up for the first time” or “a founder comparing us to a competitor,” and point it at your site. It signs up, tries to do real things, screenshots every step, and hands back a review ranked by what actually blocks people. It does teardowns too: homepage, pricing page, or a side-by-side against a competitor. Those run in regular Claude chat. The sign-up tests need a browser, so Claude Code or Cowork. Here’s one it did on Claude’s own pricing page. It points out that every paid plan sells “more usage” without ever saying how much: https://cobaltcapture.com/r/wu8y66x4 How I built it: 100% with Claude Code. I designed the tools and the studies, and Claude Code wrote all of it. It’s an MCP server. The part that made it work was writing each study as a fixed playbook Claude pulls at the start, so it follows the same method every run instead of improvising. That makes a re-run after you ship a fix comparable to the last one. The other piece was letting the connector take screenshots itself, so Claude can review public pages straight from chat with no browser setup. Free to try. It’s in the connector directory: https://claude.ai/directory/cobalt-capture Drop your URL and I’ll run a few.
