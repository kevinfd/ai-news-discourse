---
id: "c7d550c6bc002902"
title: "No coding background: how I built two music guessing games with Claude, starting as a game for my sister"
url: "https://reddit.com/r/artificial/comments/1x9w3jv/no_coding_background_how_i_built_two_music"
link: "https://reddit.com/r/artificial/comments/1x9w3jv/no_coding_background_how_i_built_two_music"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T12:53:39Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["roy979"]
language: "en"
summary: "Less than a year ago, my sister Shani was diagnosed with cancer. She spent almost three months in the hospital, and to give us something fun to do together during those days, I started building a music game for the two of us. She passed away on August 29th, before I finished it. I kept working on it, partly to keep my mind busy, and now it's live as Shabang, with two games: 🥁 TrackStack: every…"
tags: ["r/artificial"]
orgs: ["Anthropic"]
topics: ["agents & coding", "health & science"]
content_source: "post"
word_count: 207
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1x9w3jv/no_coding_background_how_i_built_two_music/"
score: null
comments: null
community: "r/artificial"
---

# No coding background: how I built two music guessing games with Claude, starting as a game for my sister

Reddit · roy979 · 2026-10-19

Less than a year ago, my sister Shani was diagnosed with cancer. She spent almost three months in the hospital, and to give us something fun to do together during those days, I started building a music game for the two of us. She passed away on August 29th, before I finished it. I kept working on it, partly to keep my mind busy, and now it's live as Shabang, with two games: 🥁 TrackStack: every song is split into its instruments. You start with only the drums, and each wrong guess adds a layer: bass, guitar, piano… vocals come last. ⏱️ Songuess: you hear a fifth of a second of the song, and each wrong guess plays more: half a second, 2 seconds, 4… In both, the less you need to hear, the more points you get, and each one has a daily challenge: one song a day, the same for everyone. I'm a mechanical engineer with no coding background. Claude wrote the code: the Flask backend, both games, and the pipeline that splits each song into its instruments with Demucs, an AI stem-separation model. Free, no signup, works on your phone: https://shabangmusic.com/ I'd love honest feedback, and to see your daily results in the comments.
