---
id: "93c8430973d47bbf"
title: "I built an App Store screenshot skill for Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1xg4qak/i_built_an_app_store_screenshot_skill_for_claude"
link: "https://reddit.com/r/ClaudeAI/comments/1xg4qak/i_built_an_app_store_screenshot_skill_for_claude"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T18:18:07Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["quitpornio"]
language: "en"
summary: "Hey everyone, I make iOS apps, and the App Store screenshots were always the part I rushed. When I asked Claude to design them, it could make something, but it skipped the process that actually makes screenshots convert: write the headlines first, pick a clear style, then try a few directions. So I built a Claude Code skill around that. It writes the headlines first, picks from 18 styles, shows…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["products & launches"]
content_source: "post"
word_count: 254
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xg4qak/i_built_an_app_store_screenshot_skill_for_claude/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an App Store screenshot skill for Claude Code

Reddit · quitpornio · 2026-10-26

Hey everyone, I make iOS apps, and the App Store screenshots were always the part I rushed. When I asked Claude to design them, it could make something, but it skipped the process that actually makes screenshots convert: write the headlines first, pick a clear style, then try a few directions. So I built a Claude Code skill around that. It writes the headlines first, picks from 18 styles, shows three directions for the first screenshot, then builds the full set using your real app UI and exports it at exact App Store and Google Play sizes. How Claude Code helped build it: - I worked with Claude Code to write each of the 18 styles as a design system (colours, fonts, layout, decoration) plus a checklist the skill runs before export. - Claude Code wrote the scripts: a Playwright exporter that renders every screenshot at exact store size with no transparency, and helpers for AI-generated backgrounds and cut-outs. - I then had Claude Code run the skill on 7 apps to test it, fixing the skill each time something came out wrong. The video shows my subscription tracker going from its old listing to the new set, plus the other six. - The launch video is an HTML page Claude Code built and timed to the music. It's free and open source. To try it, run this in Claude Code: /plugin install aso-shots --marketplace ceorkm/aso-shots I'm still working on it, so I'd really appreciate feedback, especially on which styles to add next. https://github.com/ceorkm/aso-shots
