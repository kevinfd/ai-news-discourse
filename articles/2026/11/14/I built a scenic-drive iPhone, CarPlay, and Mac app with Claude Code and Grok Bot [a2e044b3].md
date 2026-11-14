---
id: "a2e044b30787d329"
title: "I built a scenic-drive iPhone, CarPlay, and Mac app with Claude Code and Grok Bot"
url: "https://reddit.com/r/ClaudeAI/comments/1xvtuzg/i_built_a_scenicdrive_iphone_carplay_and_mac_app"
link: "https://reddit.com/r/ClaudeAI/comments/1xvtuzg/i_built_a_scenicdrive_iphone_carplay_and_mac_app"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-14T05:04:07Z"
published_date: "2026-11-14"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Capable_Advisor_6667"]
language: "en"
summary: "My wife Jordan and I do long Florida-to-Ohio drives with our kids, and we kept wanting to know what parks, historic sites, and covered bridges were coming up — and how many minutes a stop would add — before we'd already passed the exit. That's WanderWay. It's an iPhone and CarPlay navigation app that finds places along your drive, can tell you a short story as you pass, and will navigate you…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple", "xAI"]
topics: ["products & launches", "search & media"]
content_source: "post"
word_count: 584
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xvtuzg/i_built_a_scenicdrive_iphone_carplay_and_mac_app/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a scenic-drive iPhone, CarPlay, and Mac app with Claude Code and Grok Bot

Reddit · Capable_Advisor_6667 · 2026-11-14

My wife Jordan and I do long Florida-to-Ohio drives with our kids, and we kept wanting to know what parks, historic sites, and covered bridges were coming up — and how many minutes a stop would add — before we'd already passed the exit. That's WanderWay. It's an iPhone and CarPlay navigation app that finds places along your drive, can tell you a short story as you pass, and will navigate you there. There's a Mac app now too (macOS 26, Apple silicon): you can search a town from the Mac, or pair an iPhone and follow the drive live. On iPhone, maps and routing are 100% Apple MapKit. I didn't build this alone. I built it with Claude Code and Grok Bot, and I still decide what ships. How Claude Code helped (two examples from the last two days, both still on local branches with tests behind them, not shipped yet) Kids Mode screening for everything read aloud. Kids Mode only screened stories in Story mode, so at Brief or Detailed length a place description mentioning a battle, a death or a bar could be read to a car full of kids. Claude Code mapped the code and found four more gaps, like a story that wasn't ready in time falling back to the raw description, and "What did I just pass?" naming places Kids Mode hides. It routed every spoken path (drive narration, Siri, CarPlay, walking tours and more) through one screening function. A description that fails now becomes the name and kind of place, or a kid-friendly line that already existed in all 13 languages. 3,067 tests pass, 31 of them new, and 22 of those fail if the change is taken out, so they really test it. With Kids Mode off, tests prove every path reads exactly what it read before. Cutting the app's processor use. The app re-read place files from disk on every search, redrew CarPlay two or three times per GPS fix and re-wrote the Lock Screen text every second. Claude Code made 11 fixes over 19 commits: tiles cached in memory, one CarPlay redraw per fix, text only re-worded when it changes, and the parked search resting when nothing moves. Each fix was reviewed from three sides, and one was deliberately taken back because it would have made a story you ask for while muted start late. Two fixes that touch turn-by-turn are held until a real test drive. It's not timed on a phone yet, so no speed numbers until it is. What I like about working this way: I describe the problem and the rule, it maps the code and writes the tests that prove the change, and I decide what ships and what waits for a real drive. What Grok Bot handles Reads incorrect-info reports sent from the app and helps me fix or close them. Drafts support-email replies for me to approve. Runs tests, installs builds on a real iPhone, and helps prep App Store pages and translations. Builds test and TestFlight versions I try on actual drives. It's free to try: every feature is open for 14 days, then a one-time $7.99 unlock covers both iPhone and Mac. No subscription. We've passed 2,000+ first-time downloads. On iPhone 2.6.1, Natural voices keep speaking with the phone locked and in CarPlay. There's no account, and no location history or routes on a server. wanderwayapp.com apps.apple.com/app/wanderway-navigation Happy to answer questions about the Claude Code / Grok Bot workflow, or about shipping a CarPlay app.
