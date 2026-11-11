---
id: "ea0174968f6dc930"
title: "I built a tiny Windows taskbar widget with Claude Code that shows your Claude 5h and weekly usage next to the clock"
url: "https://reddit.com/r/ClaudeAI/comments/1xte9be/i_built_a_tiny_windows_taskbar_widget_with_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xte9be/i_built_a_tiny_windows_taskbar_widget_with_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T10:20:10Z"
published_date: "2026-11-11"
collected_at: "2026-11-11T13:03:59Z"
authors: ["abdosarmini92"]
language: "en"
summary: "I kept checking the usage from the web, so I built a small widget that keeps them visible in the Windows taskbar (~300 KB exe, ~3 MB RAM, no installer). What it does Shows your 5-hour and weekly usage right next to the clock Turns orange at 80% and red at 95% Hover for reset times Update interval from 30 sec to 30 min, plus an option to show what's left instead of what's used Light and dark…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches"]
content_source: "post"
word_count: 359
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xte9be/i_built_a_tiny_windows_taskbar_widget_with_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a tiny Windows taskbar widget with Claude Code that shows your Claude 5h and weekly usage next to the clock

Reddit · abdosarmini92 · 2026-11-11

I kept checking the usage from the web, so I built a small widget that keeps them visible in the Windows taskbar (~300 KB exe, ~3 MB RAM, no installer). What it does Shows your 5-hour and weekly usage right next to the clock Turns orange at 80% and red at 95% Hover for reset times Update interval from 30 sec to 30 min, plus an option to show what's left instead of what's used Light and dark taskbars Tiny: one ~300 KB exe, ~3 MB RAM, no installer How Claude Code helped I built the whole thing with Claude Code (Opus): Planning: I asked for the most lightweight, native way to put text in the Windows 11 taskbar. Windows 11 removed the old official way to add things to the taskbar (deskbands). Claude Code compared the alternatives and settled on a small see-through window placed inside the taskbar, written in Rust using only built-in Windows APIs. Data: it worked out that the usage numbers come from the same endpoint Claude Code's /usage command uses, and confirmed the response format with a test call. Sharing the login: it looked at how Claude Code renews its own login, so the widget renews it the same way and uses the same lock. That way the two apps never clash. Code and testing: it wrote the Rust code, then took screenshots of my taskbar to check how it looked. From those it fixed things like the logo looking blurry at small sizes, and it tested the hover, tooltip and menu. Shipping: it set up the README, the GitHub repo and the release. My part was giving it the design, deciding features, and reviewing. Free to Use It's free and open source (MIT). Download the exe from the latest release and double-click it: https://github.com/AbdoSarmini/claude-usage-widget-for-windows-taskbar It uses your existing Claude Code login, so there's no setup. Just be signed in to Claude Code with a Pro or Max plan. Windows may show a "protected your PC" warning on first run because the exe isn't signed. Click More info → Run anyway, or build it from source. A star is appreciated. Feedback and ideas welcome!
