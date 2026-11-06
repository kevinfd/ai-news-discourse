---
id: "8e8a5a39b0d51eed"
title: "resurrect-anything: for some fun and nostalgia, bring things back to life from whatever tidbits exist about it online"
url: "https://reddit.com/r/ClaudeAI/comments/1xovqd0/resurrectanything_for_some_fun_and_nostalgia"
link: "https://reddit.com/r/ClaudeAI/comments/1xovqd0/resurrectanything_for_some_fun_and_nostalgia"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T22:03:44Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["0xcontext"]
language: "en"
summary: "https://github.com/sshah03/resurrect-anything Needed a break, and was reminiscing about the early internet, and the 90s, and my days using Geocities Pagebuilder, so I put this together. Although I have probably gone through 50 or more iterations at this point repeatedly trying some subset of close to 100 recreations (some in the demo video above), I would say this is very much still a work in…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["products & launches"]
content_source: "post"
word_count: 597
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xovqd0/resurrectanything_for_some_fun_and_nostalgia/"
score: null
comments: null
community: "r/ClaudeAI"
---

# resurrect-anything: for some fun and nostalgia, bring things back to life from whatever tidbits exist about it online

Reddit · 0xcontext · 2026-11-05

https://github.com/sshah03/resurrect-anything Needed a break, and was reminiscing about the early internet, and the 90s, and my days using Geocities Pagebuilder, so I put this together. Although I have probably gone through 50 or more iterations at this point repeatedly trying some subset of close to 100 recreations (some in the demo video above), I would say this is very much still a work in progress. I was having a lot of fun with it though, so I thought I'd throw it out there and see what people are into trying to bring back and how it does to inform my improvements. The purpose of the skill is to ask Claude Code to bring back something that's gone, and get it back working. Some examples include a lost Flash game, a shut-down app, a dead website, your old Geocities page, or a discontinued snack (this is all for fun, so I wouldn't actually trust the recipes, but it might give you some ideas). Obviously if it mostly exists intact in web archives it's easy, but it will also try to piece together as much detail as it can from pictures, videos, reviews, and discussions/comments online that are found. It digs a little bit deeper for these bits of information than Claude Code as a harness will on its own with the necessary prompts. Treat the end result as a starting point. You can use your own memory and comparison with the found material that might've been ignored to prompt it further to hone the result. This is mostly for fun, and personal use (I used it to bring back some of my old web apps from when I was 10!). The video below is from my tests, but because I am unsure of the legal ramifications of doing so, I am not posting the actual games/apps for consumption. There is a setting available to run the skill with which will remove branding and such for those wishing to produce a potentially shareable version of something that is not theirs. In the early versions I was very specific about how to do the recreations and kept adding steps, and that either worked very well, or very poorly depending on the task. It was almost akin to benchmaxxing. Settled on focusing on getting and organizing as much data as possible, and then having some broad but useful guidelines instead and. that gave me pretty consistent results over baseline. In case that's useful to anyone else having trouble getting their skills working right. Mostly tested with Opus 5.5. Would be interesting to see how Sonnet or Haiku work out for people. Have fun! Don't get too carried away, tokens are valuable! --- Quick start --- You need Claude Code and Python 3.9 or newer. The easy way: open Claude Code and paste this in Install the resurrect skill from https://github.com/sshah03/resurrect-anything. Follow the repo's AGENTS.md. Or install it yourself: /plugin marketplace add sshah03/resurrect-anything /plugin install resurrect@resurrect Start a new session, then try something like: /resurrect Close Range, The Onion's 2009 Flash game /resurrect the Subservient Chicken /resurrect Simpsonize Me, Burger King's 2007 Simpsons Movie site /resurrect Mailbox, the iPhone email app /resurrect Doom Valley, the 1982 Apple II adventure, as a native Mac app /resurrect Pizza Hut's Priazzo. I want to make it at home Put any links, notes or screenshots you have after the name. Games, apps and sites need a few extra tools (Playwright, Pillow, ffmpeg). Claude will offer to install them into the skill's own folder the first time, so nothing has to go into your own Python. ------------------
