---
id: "a7a3c2f2747d9424"
title: "I built a 90s cable TV guide for Plex, Jellyfin and Emby with Claude. Started in May, 1400+ Apple TV downloads later, now porting it to Roku"
url: "https://reddit.com/r/ClaudeAI/comments/1xgts0i/i_built_a_90s_cable_tv_guide_for_plex_jellyfin"
link: "https://reddit.com/r/ClaudeAI/comments/1xgts0i/i_built_a_90s_cable_tv_guide_for_plex_jellyfin"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T14:18:02Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["chadMueller"]
language: "en"
summary: "Hi, since May I've been building Nostalgex with Claude doing most of the coding. It turns your Plex, Jellyfin or Emby library into live cable channels with a real channel guide. You turn it on and something's already playing, mid movie, like 1996. Why you might want it: 130+ channels built from your own library, like Saturday morning cartoons, sitcoms and 80s action seasonal blocks: SCREAM for…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 450
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgts0i/i_built_a_90s_cable_tv_guide_for_plex_jellyfin/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a 90s cable TV guide for Plex, Jellyfin and Emby with Claude. Started in May, 1400+ Apple TV downloads later, now porting it to Roku

Reddit · chadMueller · 2026-10-27

Hi, since May I've been building Nostalgex with Claude doing most of the coding. It turns your Plex, Jellyfin or Emby library into live cable channels with a real channel guide. You turn it on and something's already playing, mid movie, like 1996. Why you might want it: 130+ channels built from your own library, like Saturday morning cartoons, sitcoms and 80s action seasonal blocks: SCREAM for October, and a holiday lineup with Christmas specials and a Turkey Day channel a real scrolling guide with ratings and posters, plus a retro mode with scanlines works with Plex, Jellyfin and Emby, and blends all your servers into one lineup no setup beyond signing in. Pick your libraries and it builds the channels Apple TV app on the App Store, plus a web tuner and Docker if you'd rather self host free and open source (MIT), with an optional tip jar that unlocks nothing Where it's at: 1,400+ Apple TV downloads, 776 people watching in the last month (about 260 hours of TV in one week), 735 commits, 65 merged PRs, 7 contributors and 132 GitHub stars. Most of that came from people on Discord finding bugs I never would have. How I built it: Why: I missed channel surfing. Streaming apps make you pick, and I wanted my own library to just be on Start with a spec, not code. I wrote down how real cable felt (guide grid, tuning in mid show, channels with a vibe) and had Claude turn that into a plan before writing anything Keep rules in data, not code. All 130+ channels live in one JSON file of rules (genres, keywords, decades), so adding a channel is an edit, not a rebuild Use real data to fill gaps. Claude wrote small one off scripts that pull from TMDB (a public movie database) to build lists like the stand up channel Test on the real device, every time. The simulator lied constantly. Apple TV remote focus only got right through back and forth on an actual TV Let users drive the backlog. Discord testers found the bugs that mattered, and I'd paste their reports straight into Claude with the logs Port with a reference. For Roku, Claude used the Apple TV app as the spec, so the two behave the same What's next: Roku. We're porting it now. The beta filled all 20 tester spots, version 1.0.5 just went out, and the goal is the public Roku Channel Store. If you want to hear when it's live or help test, the Discord is where updates land first. Happy to answer anything about the build or the Claude workflow. Site: https://nostalgex.app/?utm_source=reddit&utm_medium=social&utm_campaign=launch_oct26_r_claudeai Apple TV: https://apps.apple.com/app/apple-store/id6762563534?pt=128802261&ct=r_claudeai&mt=8 Discord: https://discord.gg/FgnZcr5bDT Code: https://github.com/chadMueller/Nostalgex
