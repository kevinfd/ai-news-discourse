---
id: "93f4a072693cc074"
title: "PSA: The free banked reset expires TODAY/Oct 22 at 16:00 UTC, not midnight."
url: "https://reddit.com/r/ClaudeAI/comments/1xbo16i/psa_the_free_banked_reset_expires_todayoct_22_at"
link: "https://reddit.com/r/ClaudeAI/comments/1xbo16i/psa_the_free_banked_reset_expires_todayoct_22_at"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T14:03:16Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Da_Funk0104"]
language: "en"
summary: "Here's the exact timestamp Everyone's been saying \"expires Oct 22,\" but nobody had an exact time, and Anthropic's help page only says it expires \"on the day and time listed on the offer.\" So I dug into the network responses on the usage page. The offer object contains: \"starts_at\":\"2026-09-22T16:00:00+00:00\", \"ends_at\":\"2026-10-22T16:00:00+00:00\", \"clears\":[\"five_hour\",\"seven_day\"] So it's…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["search & media"]
content_source: "post"
word_count: 182
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbo16i/psa_the_free_banked_reset_expires_todayoct_22_at/"
score: null
comments: null
community: "r/ClaudeAI"
---

# PSA: The free banked reset expires TODAY/Oct 22 at 16:00 UTC, not midnight.

Reddit · Da_Funk0104 · 2026-10-21

Here's the exact timestamp Everyone's been saying "expires Oct 22," but nobody had an exact time, and Anthropic's help page only says it expires "on the day and time listed on the offer." So I dug into the network responses on the usage page. The offer object contains: "starts_at":"2026-09-22T16:00:00+00:00", "ends_at":"2026-10-22T16:00:00+00:00", "clears":["five_hour","seven_day"] So it's exactly 30 days, from 9 AM Pacific to 9 AM Pacific. It expires Oct 22 at 16:00 UTC: Time zone Expires US West Coast (PDT) 9:00 AM US East Coast (EDT) 12:00 PM (noon) London (BST) 5:00 PM Central Europe (CEST) 6:00 PM Japan (JST) 1:00 AM Oct 23 That also explains why some people in Asia see "Expires Oct 23": the UI shows the date in your local time zone. Verify it yourself (Firefox/Chrome): Go to claude.ai → Settings → Usage Open DevTools (F12) → Network tab, then reload Use the search in responses (magnifier icon in Firefox, Ctrl+Shift+F in Chrome) and search for ends_at or 2026-10-22 If you're in the US, don't wait until the evening. Use it before your Thursday morning or lunch break is over.
