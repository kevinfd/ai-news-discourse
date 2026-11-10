---
id: "00d30c16f5760a91"
title: "I built a 24/7 live sports channel for an invented sport, simulated in pixel art"
url: "https://reddit.com/r/ClaudeAI/comments/1xrtdwg/i_built_a_247_live_sports_channel_for_an_invented"
link: "https://reddit.com/r/ClaudeAI/comments/1xrtdwg/i_built_a_247_live_sports_channel_for_an_invented"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T14:41:30Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["spite_as_an_arrow"]
language: "en"
summary: "Scorchball TV is an always-on channel for an invented sport: eight clubs, a season a week, a live match about every 2h 40m, and the rest of the time filled the way a real channel would, with replays, a studio desk, post-match interviews, ads for made-up sponsors and an evening podcast. The league remembers: drafts, contracts, retirements, records, legends. It's best viewed in full screen in your…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 210
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrtdwg/i_built_a_247_live_sports_channel_for_an_invented/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a 24/7 live sports channel for an invented sport, simulated in pixel art

Reddit · spite_as_an_arrow · 2026-11-09

Scorchball TV is an always-on channel for an invented sport: eight clubs, a season a week, a live match about every 2h 40m, and the rest of the time filled the way a real channel would, with replays, a studio desk, post-match interviews, ads for made-up sponsors and an evening podcast. The league remembers: drafts, contracts, retirements, records, legends. It's best viewed in full screen in your browser. Also works on mobile! I directed and Claude Code wrote every line. What made it work for me: A vision doc first, then a design doc per part/phase Mock-ups before building: For anything visual, Claude built a throwaway page with looks A, B and C side by side, drawn with the real code and real data. Data, not code. Every timing, rule and commentary line lives in data files, so "make the ads run less" is a number, not a change. No game server: every browser rebuilds the same league from a snapshot and a daily key from a secret seed, so everyone sees the same match. Voices are ElevenLabs (about 11,000 clips made ahead); every sound is synthesized. Watch: https://scorchball.tv/?from=cai Write-up: https://scorchball.tv/how-it-was-built Code (MIT, CLAUDE.md and the docs included): https://github.com/savenor14/scorchball-tv Daily results (posted after all live matches are over automatically): https://bsky.app/profile/scorchball.tv
