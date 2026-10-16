---
id: "f20361cbac8cc38a"
title: "I used Opus 5.5 to build NodeSeq, a music sequencer that runs in the browser"
url: "https://reddit.com/r/ClaudeAI/comments/1x4hxu5/i_used_opus_55_to_build_nodeseq_a_music_sequencer"
link: "https://reddit.com/r/ClaudeAI/comments/1x4hxu5/i_used_opus_55_to_build_nodeseq_a_music_sequencer"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T00:00:32Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["GuyInThe6kDollarSuit"]
language: "en"
summary: "I built NodeSeq, a music sequencer that runs in the browser, and I built it with Claude Code. It is free to use at https://nodeseq.com . The studio opens straight away with no sign-up or install. What it does Instead of a timeline or piano roll, you make a track by wiring nodes together on a canvas: Drum, synth and bass nodes make sound. Connections carry pulses between them, and each pulse…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 470
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x4hxu5/i_used_opus_55_to_build_nodeseq_a_music_sequencer/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I used Opus 5.5 to build NodeSeq, a music sequencer that runs in the browser

Reddit · GuyInThe6kDollarSuit · 2026-10-13

I built NodeSeq, a music sequencer that runs in the browser, and I built it with Claude Code. It is free to use at https://nodeseq.com . The studio opens straight away with no sign-up or install. What it does Instead of a timeline or piano roll, you make a track by wiring nodes together on a canvas: Drum, synth and bass nodes make sound. Connections carry pulses between them, and each pulse takes a set musical time to travel, so a loop of nodes becomes a rhythm. Gate nodes count pulses or follow a step pattern, which gives you fills and arrangement. Mod nodes change another node's settings (cutoff, resonance, decay, pan) every time they fire, so a line never plays quite the same twice. Nodes are grouped, and each group is a pad you can switch on and off on the bar with a number key. There are scenes, a song mode that chains scenes, and hold effects (filter, echo and reverb throws, stutter, riser) for playing live. All sound is synthesised with the Web Audio API. There are no samples. You can export a WAV, share a track as a link, or publish it to a community page where others can play it, comment, and open it in the studio to remix. How Claude was used Claude Code wrote nearly all of the code; I directed, tested by ear and decided what to keep. It started as a single HTML file. Claude later split it into modules (scheduler, sound engine, canvas, inspector, performance strip) and wrote scheduler tests so that refactors did not break timing. The scheduler and audio engine share one code path for live playback and offline WAV export, which was Claude's suggestion and removed a class of "export sounds different" bugs. The community side is a Cloudflare Worker with D1. Claude implemented passkey sign-in (WebAuthn) directly, plus the input sanitiser and text filter for published tracks. The trailer was also made by Claude. It wrote a script that drives the real app in a headless browser one video frame at a time while the audio renders offline, so picture and sound come from the same run. It performs one of the demo tracks: bringing groups in, holding effects, patching a new node. What I learned Tests on the pure-logic part (the scheduler) paid for themselves; UI work was faster to check by listening. Asking Claude to explain a timing bug before fixing it usually found the real cause faster than asking for a fix. Small, specific requests worked better than "add feature X" for anything touching audio. Try it https://nodeseq.com (free; a passkey is only needed if you want to publish a track). Load a demo from the Demos menu and press Space. Feedback welcome, especially on what is confusing in the first five minutes.
