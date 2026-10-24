---
id: "a4a882a5ce5a30df"
title: "Using OpenAI Realtime API with a Robot"
url: "https://reddit.com/r/OpenAI/comments/1xddpuh/using_openai_realtime_api_with_a_robot"
link: "https://reddit.com/r/OpenAI/comments/1xddpuh/using_openai_realtime_api_with_a_robot"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T13:14:41Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Tarun122"]
language: "en"
summary: "I hooked up the OpenAI Realtime API (gpt-realtime-2.1 over WebRTC) to a small robot arm I built, so I can just talk to it. In the video it plays tic-tac-toe with me, puts a cube in a bowl, picks its favourite toy car and hands a cube back to me. How it works: The voice model gets only a handful of tools: look, reach, grab, drop, gripper, park and stop. Reach and grab aren't hand-coded moves.…"
tags: ["r/OpenAI"]
orgs: ["OpenAI"]
topics: ["models & research", "robotics & autonomy"]
content_source: "post"
word_count: 157
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1xddpuh/using_openai_realtime_api_with_a_robot/"
score: null
comments: null
community: "r/OpenAI"
---

# Using OpenAI Realtime API with a Robot

Reddit · Tarun122 · 2026-10-23

I hooked up the OpenAI Realtime API (gpt-realtime-2.1 over WebRTC) to a small robot arm I built, so I can just talk to it. In the video it plays tic-tac-toe with me, puts a cube in a bowl, picks its favourite toy car and hands a cube back to me. How it works: The voice model gets only a handful of tools: look, reach, grab, drop, gripper, park and stop. Reach and grab aren't hand-coded moves. They're policies I trained in simulation, so the model decides what to do and the trained skills decide how . Fresh images from both cameras (top view and wrist) go into the conversation with every user turn, so it always sees the current board. It reads the tic-tac-toe grid itself from the images. To pick a target, a vision model puts a point on the object in the top camera image, and the reach or grab policy goes to that point.
