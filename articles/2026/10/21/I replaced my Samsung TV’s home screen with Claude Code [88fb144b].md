---
id: "88fb144b82e5676f"
title: "I replaced my Samsung TV’s home screen with Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1xbzlih/i_replaced_my_samsung_tvs_home_screen_with_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xbzlih/i_replaced_my_samsung_tvs_home_screen_with_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T21:11:42Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["NelsonEU"]
language: "en"
summary: "Samsung’s home screen had turned into an ad billboard, so I asked Claude Code to build me something simpler: a clock, the apps I actually use and my consoles. The trick that made the biggest difference was faking the handful of TV APIs the launcher relies on. That let Claude and me work on the layout and remote navigation right in my laptop’s browser. Every tweak was a quick refresh instead of a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Samsung"]
topics: []
content_source: "post"
word_count: 147
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbzlih/i_replaced_my_samsung_tvs_home_screen_with_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I replaced my Samsung TV’s home screen with Claude Code

Reddit · NelsonEU · 2026-10-21

Samsung’s home screen had turned into an ad billboard, so I asked Claude Code to build me something simpler: a clock, the apps I actually use and my consoles. The trick that made the biggest difference was faking the handful of TV APIs the launcher relies on. That let Claude and me work on the layout and remote navigation right in my laptop’s browser. Every tweak was a quick refresh instead of a new install on the TV, which made iterating together really fast. Taking over the Home button was the tricky part, since Samsung offers no official way to do it. I followed the CleanFrame approach: a small helper that edits a few undocumented TV settings, saves the original values first and restores them if anything goes wrong. I’ve only tried it on my 2022 Q70B, so be careful with other models. Code: https://github.com/NelsonEU/arn0-tv Write-up: https://medium.com/@arnaudetienne/i-replaced-my-samsung-tvs-home-screen-with-claude-6f72e98c55fc
