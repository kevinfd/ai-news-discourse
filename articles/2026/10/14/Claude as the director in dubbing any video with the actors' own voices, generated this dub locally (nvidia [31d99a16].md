---
id: "31d99a1650caf4b1"
title: "Claude as the director in dubbing any video with the actors' own voices, generated this dub locally (nvidia gpu required)"
url: "https://reddit.com/r/ClaudeAI/comments/1x66z85/claude_as_the_director_in_dubbing_any_video_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T23:56:52Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["_swax_"]
language: "en"
summary: "Built this dubbing tool with Claude to watch shows that have never been translated to English and it works really well. You basically checkout the repo, startup Claude Code and tell it to dub whatever video you want. Claude is the director of the process, and the repo contains all the guidance and scripts it needs to perform a successful dub - splitting out the audio with Mel-Band Roformer,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["business & funding", "chips & infrastructure"]
content_source: "post"
word_count: 120
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x66z85/claude_as_the_director_in_dubbing_any_video_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude as the director in dubbing any video with the actors' own voices, generated this dub locally (nvidia gpu required)

Reddit · _swax_ · 2026-10-14

Built this dubbing tool with Claude to watch shows that have never been translated to English and it works really well. You basically checkout the repo, startup Claude Code and tell it to dub whatever video you want. Claude is the director of the process, and the repo contains all the guidance and scripts it needs to perform a successful dub - splitting out the audio with Mel-Band Roformer, finding speech with Silero VAD, transcribing with Whisper, reading any on screen text with RapidOCR, figuring out who's speaking with pyannote/WeSpeaker, voice cloning with OmniVoice, and VoiceStudio for mixing. It even does multiple QA passes with Whisper again. I have another demo video here https://www.youtube.com/watch?v=2DsFAoTbQ8E , and repo is here https://github.com/swax/dub-anything
