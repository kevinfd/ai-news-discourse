---
id: "05955360494a2b50"
title: "Stretchtext for Claude Code: a 1967 idea that got more useful as text became generative"
url: "https://reddit.com/r/ClaudeAI/comments/1x66prd/stretchtext_for_claude_code_a_1967_idea_that_got"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T23:43:49Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["pro-vi"]
language: "en"
summary: "cc-stretch is a free (MIT) Claude Code plugin. Replies arrive short. Click a linked phrase and it grows in place; click « and it shrinks back. The plugin tells Claude which parts you opened, so it doesn't assume you read the rest. Why now In 1967 Ted Nelson described stretchtext: text that grows where you want more and shrinks back where you don't. It stayed a quaint idea because writing every…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 224
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x66prd/stretchtext_for_claude_code_a_1967_idea_that_got/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Stretchtext for Claude Code: a 1967 idea that got more useful as text became generative

Reddit · pro-vi · 2026-10-14

cc-stretch is a free (MIT) Claude Code plugin. Replies arrive short. Click a linked phrase and it grows in place; click « and it shrinks back. The plugin tells Claude which parts you opened, so it doesn't assume you read the rest. Why now In 1967 Ted Nelson described stretchtext: text that grows where you want more and shrinks back where you don't. It stayed a quaint idea because writing every level of fidelity by hand is just tediously hard. Text is generative now, so Claude can just write it for us, for basically free. Also because Anthropic released Claude Mods. How Claude helped Claude Code wrote most of the code. At runtime Claude writes each reply with {{short|long}} markup, and the plugin only draws it. What I learned Across 69 real replies from four of my projects, the folded version was 17% of the words Claude wrote without the plugin, and kept about two of every three most important points. It saved enough reading, that I'd name it "progressive attention". Limits Clicks only work in Claude Code's fullscreen renderer ( /tui fullscreen ). Everywhere else, including the desktop app, every stretch shows open. It is built on an early-access plugin API, so it may break between releases. Install (free), in a Claude Code session: /plugin install cc-stretch --marketplace pro-vi/cc-stretch /tui fullscreen Repo: https://github.com/pro-vi/cc-stretch
