---
id: "4da57e136437780b"
title: "Claude Code taught my Roborock to escape from under the stairs"
url: "https://reddit.com/r/ClaudeAI/comments/1xdnn8e/claude_code_taught_my_roborock_to_escape_from"
link: "https://reddit.com/r/ClaudeAI/comments/1xdnn8e/claude_code_taught_my_roborock_to_escape_from"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T19:30:20Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["fillyourcoffee"]
language: "en"
summary: "We've had our Roborock for a while. When we moved into a new apartment, under the stairs seemed like the perfect spot for it: out of everyone's way, and space that's otherwise wasted. Then we realised it can't get out of there on its own. The way out is only a few cm wider than the robot, so before every clean I steered it out by hand in the app. Over about one evening of actual work, I fixed…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["robotics & autonomy", "products & launches"]
content_source: "post"
word_count: 300
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xdnn8e/claude_code_taught_my_roborock_to_escape_from/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Code taught my Roborock to escape from under the stairs

Reddit · fillyourcoffee · 2026-10-23

We've had our Roborock for a while. When we moved into a new apartment, under the stairs seemed like the perfect spot for it: out of everyone's way, and space that's otherwise wasted. Then we realised it can't get out of there on its own. The way out is only a few cm wider than the robot, so before every clean I steered it out by hand in the app. Over about one evening of actual work, I fixed that with Claude Code. I was mostly the eyes ("it bumped on the left"), and Claude wrote the code, read the robot's logs and ran the tests. **Things we figured out:** - The robot has hidden remote-control commands (what the app's joystick uses), undocumented, so it was trial and error. - Moves in the first ~5 seconds of remote control are silently ignored. - After backing off the dock, the robot does a 180° turn **by itself**. For a while every turn looked like a huge overshoot. - Its map position updates live, so the script can measure after each move instead of driving blind. **Setup:** a Raspberry Pi runs Home Assistant with a bridge to Google Home. I tap "Roborock living room": it drives out of the gap and starts cleaning. If anything goes wrong, it gives up and docks. **The honest part:** the first fix was "dodge right when blocked". Then the robot steered itself straight into the stair post on the right. The robot's position reading wobbles by about as much room as it has in the gap, so there's no perfect fixed path. **What works:** when it's blocked, it backs off a few cm and tries other angles, nearest first, on both sides. Test: 10 runs in a row, out and back to the dock: **10/10 out**.
