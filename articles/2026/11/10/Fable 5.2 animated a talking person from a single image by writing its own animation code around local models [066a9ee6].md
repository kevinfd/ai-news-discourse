---
id: "066a9ee62df3cddc"
title: "Fable 5.2 animated a talking person from a single image by writing its own animation code around local models"
url: "https://reddit.com/r/ClaudeAI/comments/1xszbgf/fable_52_animated_a_talking_person_from_a_single"
link: "https://reddit.com/r/ClaudeAI/comments/1xszbgf/fable_52_animated_a_talking_person_from_a_single"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T21:30:40Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Easy_Finish_2467"]
language: "en"
summary: "I ran this in one Claude Code cloud session with Fable 5.2, using about a dozen short prompts over a day. It downloaded the local models itself (SD 1.5, LivePortrait, a TTS model, Wav2Lip) and ran them on CPU in the session. Each presenter is one SD 1.5 image. LivePortrait made 65 still poses of each face, and the JS it wrote blends between them every frame. Watch the pupils and the hair while…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "chips & infrastructure"]
content_source: "post"
word_count: 118
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xszbgf/fable_52_animated_a_talking_person_from_a_single/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Fable 5.2 animated a talking person from a single image by writing its own animation code around local models

Reddit · Easy_Finish_2467 · 2026-11-10

I ran this in one Claude Code cloud session with Fable 5.2, using about a dozen short prompts over a day. It downloaded the local models itself (SD 1.5, LivePortrait, a TTS model, Wav2Lip) and ran them on CPU in the session. Each presenter is one SD 1.5 image. LivePortrait made 65 still poses of each face, and the JS it wrote blends between them every frame. Watch the pupils and the hair while they talk. The bodies move too, you can see the shoulders go up a bit every time they breathe in. It couldn't watch video, so it checked lip sync against the audio and ran optical flow on its own frames. Breakdown with pictures: https://claude.ai/artifact/J9BWy4AQMGYFciULjomtvm
