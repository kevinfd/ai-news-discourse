---
id: "f5d4fe7db7ed68f7"
title: "Tried Anthropic’s webapp-testing skill on a tiny local app. Both checks passed, and Claude spotted a bug I hadn’t asked about"
url: "https://reddit.com/r/ClaudeAI/comments/1xpvk88/tried_anthropics_webapptesting_skill_on_a_tiny"
link: "https://reddit.com/r/ClaudeAI/comments/1xpvk88/tried_anthropics_webapptesting_skill_on_a_tiny"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T02:48:11Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["vinishkapoor"]
language: "en"
summary: "The webapp-testing skill from Anthropic’s skills repo has Claude test a local web page in a real headless browser with Playwright. I tried it on a tiny Tip Splitter page (bill, tip %, people, and a Calculate button). One prompt with exact checks: bill 80, tip 20, people 4 should show $24.00 per person an empty bill should show an error save a screenshot of each and report the browser console…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["policy & regulation", "products & launches"]
content_source: "post"
word_count: 266
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xpvk88/tried_anthropics_webapptesting_skill_on_a_tiny/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Tried Anthropic’s webapp-testing skill on a tiny local app. Both checks passed, and Claude spotted a bug I hadn’t asked about

Reddit · vinishkapoor · 2026-11-07

The webapp-testing skill from Anthropic’s skills repo has Claude test a local web page in a real headless browser with Playwright. I tried it on a tiny Tip Splitter page (bill, tip %, people, and a Calculate button). One prompt with exact checks: bill 80, tip 20, people 4 should show $24.00 per person an empty bill should show an error save a screenshot of each and report the browser console messages Results, in 13 seconds by Claude’s timer: both tests passed, and the screenshots matched the report it listed the console messages, including an “Invalid bill” error. It noted the app logs that on purpose, so it didn’t call it a bug no uncaught page errors The part I liked: without being asked, it pointed out that the app never checks the people field, so 0 or empty would give Infinity or NaN. That was true, and it was a gap I’d left in on purpose. It said it didn’t test it because I hadn’t asked. Setup notes: the skill doesn’t install Playwright. I set it up in a virtual environment with a headless Chromium download, which is the biggest wait tell Claude which Python to use if Playwright lives in .venv it asked before running its combined script and server command, so read it before you approve It suits quick checks while you build. For a suite you run on every commit, have Claude save a good script as a real test file. One small static page and two checks. I didn’t test logins, uploads or late-loading data. Screenshots and the exact prompt: https://aiparabellum.com/claude-code-webapp-testing-skill-test-local-app/
