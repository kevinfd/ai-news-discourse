---
id: "8ceb54c6e239950f"
title: "I built a small daily game where Claude mixes 3 GitHub repos into product ideas, and each week the community picks one we build as open source"
url: "https://reddit.com/r/ClaudeAI/comments/1x8omx2/i_built_a_small_daily_game_where_claude_mixes_3"
link: "https://reddit.com/r/ClaudeAI/comments/1x8omx2/i_built_a_small_daily_game_where_claude_mixes_3"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T23:42:57Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["aram-antonyan-hgtg42"]
language: "en"
summary: "https://preview.redd.it/8yktipgaa4wh1.png?width=2424&format=png&auto=webp&s=62119d6f1b83756a180cc845f9dff3e206eac603 If you want something semi-nerdy and semi-fun: Repo Safari is a tiny daily game for finding open-source projects. You walk a trail of categories and collect repos as stickers. The new part is the Idea Shower. Pick any 3 repos and press Mix, and Claude turns them into three product…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "jobs & society"]
content_source: "post"
word_count: 341
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x8omx2/i_built_a_small_daily_game_where_claude_mixes_3/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a small daily game where Claude mixes 3 GitHub repos into product ideas, and each week the community picks one we build as open source

Reddit · aram-antonyan-hgtg42 · 2026-10-17

https://preview.redd.it/8yktipgaa4wh1.png?width=2424&format=png&auto=webp&s=62119d6f1b83756a180cc845f9dff3e206eac603 If you want something semi-nerdy and semi-fun: Repo Safari is a tiny daily game for finding open-source projects. You walk a trail of categories and collect repos as stickers. The new part is the Idea Shower. Pick any 3 repos and press Mix, and Claude turns them into three product ideas: one useful, one unexpected and one ridiculous. If you like one, publish it to the Idea Board, where people can star the ideas they want built. Every Monday at 00:00 UTC, the idea with the most new stars that week gets built as an open-source prototype, and we share it. The first pick is Monday 26 Oct. Free; playing and generating ideas need no account Publishing and starring use GitHub sign-in (public profile only) No cookies; visits are counted anonymously https://w20labs.github.io/repo-safari/?utm_source=reddit Why I built it I kept finding great repos by accident and forgetting them. A daily trail makes discovering them a 3-minute habit. Mixing repos is the fun part: unrelated projects often suggest products nobody has built yet, and letting people vote turns that into something real every week. How it's built (mostly with Claude Code) Rooms: a weekly pipeline builds them from GitHub's own topics. Rules decide what makes the cut: active in the last 6 months, the repo is actually about the topic, at most 2 repos per owner, and a safety filter. Nobody hand-picks. Hosting: the game is one static page on GitHub Pages. Backend: the Idea Shower and the Idea Board run in a single Cloudflare Worker. Claude generates the ideas, and D1 (Cloudflare's SQLite) stores published ideas and stars. Sign-in: GitHub, with no cookies. What Claude Code did: most of the code, tests and reviews. My job was mostly deciding what to build and checking the results. The most useful habit was asking it to review its own pull requests before merging: it caught real bugs, like a moderation hold being lost when the week closed. Code (MIT): https://github.com/w20labs/repo-safari I'd love feedback on the ideas Claude comes up with, especially the ridiculous ones.
