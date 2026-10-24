---
id: "97b1a2b6b2d54565"
title: "Opus 5.5 animated this music video frame by frame: 4,320 frames, every jump locked to the beat"
url: "https://reddit.com/r/ClaudeAI/comments/1xdnfqe/opus_55_animated_this_music_video_frame_by_frame"
link: "https://reddit.com/r/ClaudeAI/comments/1xdnfqe/opus_55_animated_this_music_video_frame_by_frame"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T19:22:21Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["chrisBhappy"]
language: "en"
summary: "No video editor, no animator. Suno made the song. Opus 5.5 wrote a 22,000-line Python engine in about a week, and that engine placed every single frame. How it works: First it takes the song apart. AI stem splitting pulls out vocals, drums and bass. A beat tracker maps all 175 BPM, and forced alignment timestamps every one of the 337 sung words. The whole film runs on that clock. The…"
tags: ["r/ClaudeAI"]
orgs: []
topics: ["safety & ethics"]
content_source: "post"
word_count: 248
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xdnfqe/opus_55_animated_this_music_video_frame_by_frame/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Opus 5.5 animated this music video frame by frame: 4,320 frames, every jump locked to the beat

Reddit · chrisBhappy · 2026-10-23

No video editor, no animator. Suno made the song. Opus 5.5 wrote a 22,000-line Python engine in about a week, and that engine placed every single frame. How it works: First it takes the song apart. AI stem splitting pulls out vocals, drums and bass. A beat tracker maps all 175 BPM, and forced alignment timestamps every one of the 337 sung words. The whole film runs on that clock. The choreography is code, not keyframes. Every move is pinned to an exact moment: “take off on bar 42”, “land on the snare at 58.37 s”. A physics solver with real gravity and stride lengths fills in the runs and jumps between those points. The runner is 1,933 hand-picked drawings. Wan image-to-video clips of him painted on a white wall get sliced into single poses. The engine picks one, holds it for a 16th note (about 2 frames), then swaps to the next. That’s where the stop-motion feel comes from. Video models can’t keep a beat. I tested Seedance with the actual song as input: it landed 1.25 to 2 seconds late every time, and the full film would have cost about $480. The code-timed version hit every beat exactly, for $0.30 on the same test clip. One continuous shot, zero cuts. Spring camera, dripping wet paint, rain, and at 0:57 he leaps in total silence and lands right on the drop. Total AI generation cost for the whole film: about $187. 12 full renders before this one.
