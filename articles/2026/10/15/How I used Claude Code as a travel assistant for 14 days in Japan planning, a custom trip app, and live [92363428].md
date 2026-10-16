---
id: "9236342842703264"
title: "How I used Claude Code as a travel assistant for 14 days in Japan: planning, a custom trip app, and live re-planning from my phone"
url: "https://reddit.com/r/ClaudeAI/comments/1x6ng3u/how_i_used_claude_code_as_a_travel_assistant_for"
link: "https://reddit.com/r/ClaudeAI/comments/1x6ng3u/how_i_used_claude_code_as_a_travel_assistant_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T14:40:41Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["o_vieira"]
language: "en"
summary: "TL;DR: My wife and I just spent 14 days in Japan (Kyoto → Hakone → Tokyo). I used Claude Code as my travel assistant from start to finish: planning in my Obsidian vault, building a private offline trip app for our phones (inspired by another Redditor's trip web app; I cared about what ours did, not how it looked), and, during the trip, using Remote Control from my phone to re-plan days and keep…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "EU"]
topics: ["products & launches"]
content_source: "post"
word_count: 680
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x6ng3u/how_i_used_claude_code_as_a_travel_assistant_for/"
score: null
comments: null
community: "r/ClaudeAI"
---

# How I used Claude Code as a travel assistant for 14 days in Japan: planning, a custom trip app, and live re-planning from my phone

Reddit · o_vieira · 2026-10-15

TL;DR: My wife and I just spent 14 days in Japan (Kyoto → Hakone → Tokyo). I used Claude Code as my travel assistant from start to finish: planning in my Obsidian vault, building a private offline trip app for our phones (inspired by another Redditor's trip web app; I cared about what ours did, not how it looked), and, during the trip, using Remote Control from my phone to re-plan days and keep everything up to date. 1. Planning in Obsidian I already keep everything in an Obsidian vault that Claude Code works in, so the trip went there too: a hub note, itinerary, bookings, practical stuff, and a research note with every source and every option we rejected. I had Claude log friends' recommendations with who sent them, which paid off. Mid-trip I could ask "was this a friend's tip?" and get an answer. The biggest help was asking it to grill me rather than hand me a plan: one question at a time, each with a recommended option, and I make the call. Before each city I asked for a "run check", where it went through every day looking for problems. 2. The trip app The idea came from a post in r/TravelPortugal where someone shared their trip itinerary as a web app hosted on Vercel. I didn't want to juggle a travel app, Google Maps lists and screenshots, so I wanted our own version: one private page on our phones with everything we'd need on the street, in the order we'd need it. I focused on what it had to do and how it should work in practice, and left the look to Claude. Then I kept adding things as the trip showed what was missing: Day cards with times, directions, "where to board" links and opening hours Booking QR codes on the right day's card Train guides per journey (line, platform, direction, stops), grouped by city Taxi cards with the hotel address in Japanese Shopping lists with tick boxes, my sister's gift list with pictures, and progress bars for the EU customs allowance A short story and some trivia for each stop, with a photo A lot of this came during the trip itself. The stories and trivia were a mid-trip addition, and the train guides got much more detailed after we got completely lost in a station early on. It's one encrypted HTML file hosted on Vercel. It works offline, and it has an update button I could tap whenever I wanted to refresh it. Passwords and tokens stay in the macOS Keychain, so Claude can build and deploy without ever seeing them. 3. Live mode I left the Claude Code desktop session running at home with Remote Control on, plus a routine that turned Remote Control back on if it dropped, and used it from my phone: "We only caught the 10:15 train, re-time the day" → new times, app updated, calendar events moved, in a couple of minutes I asked for a calendar event per stop, so I could quickly glance at my watch to check the stops "Is there a bar our friends recommended?" → found in my notes and checked it was open "Remind me in Munich to book a ride home" → done We didn't follow the plan to the letter every day. These were holidays, not military service. But having the shape of the day a glance away really helped. 4. What went wrong One day I changed plans on the fly to fit in a store I wanted to visit, and it went into the itinerary without anyone checking it was open. It wasn't. Since then, every stop gets checked on the place's own website before it goes in. Tips if you try something like it Ask it to grill you; keep the decisions yours Make it check official sources, and say what it couldn't verify Keep one source of truth (we ended up editing the plan in two places and regretted it) Keep secrets out of the chat entirely Happy to answer questions about the setup.
