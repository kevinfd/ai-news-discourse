---
id: "b488b60277550a68"
title: "a Mac DAW where Claude can run the whole session, using Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1xmhrd7/a_mac_daw_where_claude_can_run_the_whole_session"
link: "https://reddit.com/r/ClaudeAI/comments/1xmhrd7/a_mac_daw_where_claude_can_run_the_whole_session"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T03:03:05Z"
published_date: "2026-11-03"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Xufie"]
language: "en"
summary: "I’ve been building Zammoth for most of this year, about 6 months total, mostly with Claude Code. It’s a native Mac DAW (C++/JUCE on Tracktion Engine) with an AI engineer built in. You talk to it in a side panel, and it uses the same controls you do: tracks, clips, faders, devices, routing, automation, MIDI, export. Ask it to split a song into stems, set up a drum bus, or master to -14 LUFS, and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 317
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmhrd7/a_mac_daw_where_claude_can_run_the_whole_session/"
score: null
comments: null
community: "r/ClaudeAI"
---

# a Mac DAW where Claude can run the whole session, using Claude Code

Reddit · Xufie · 2026-11-03

I’ve been building Zammoth for most of this year, about 6 months total, mostly with Claude Code. It’s a native Mac DAW (C++/JUCE on Tracktion Engine) with an AI engineer built in. You talk to it in a side panel, and it uses the same controls you do: tracks, clips, faders, devices, routing, automation, MIDI, export. Ask it to split a song into stems, set up a drum bus, or master to -14 LUFS, and you watch it do the steps. Every change can be undone, and nothing it does is hidden from you. I am looking for testers, beginners and experts of music production who would be willing to use the DAW and would receive the DAW for free, please let me know if you would like to join the discord, it is brand new. The engineer runs on Claude through your own Anthropic API key, so you pay Anthropic for what it uses. A full mix pass on the default model (Opus 5.5) has been around a dollar for me. How Claude Code helped, honestly: I’m one person, an audio engineer. Claude Code wrote most of the C++ and Python, and I made the calls on what to build and checked the results. The CLAUDE.md file is now huge. It holds every rule we learned the hard way, so each new session starts knowing them. The biggest lesson was tests that pass while measuring nothing. Claude would write a check, it would go green, and the bug was still there. Now every test has to be seen failing on the broken code before the fix goes in. That one rule caught more than anything else. Claude is confidently wrong about audio. It would tell me a limiter held the ceiling when it didn’t. I stopped trusting its reading of its own work and started checking with separate meters, plus tests that render the actual audio.
