---
id: "b74fe227b114b0dd"
title: "I built an Android TV app with Claude Code: a night-and-day globe and walls of live webcams. What it had to measure on the TV instead of guessing"
url: "https://reddit.com/r/ClaudeAI/comments/1xgr28v/i_built_an_android_tv_app_with_claude_code_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xgr28v/i_built_an_android_tv_app_with_claude_code_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T12:22:43Z"
published_date: "2026-10-27"
collected_at: "2026-10-28T12:05:24Z"
authors: ["cyberdinn"]
language: "en"
summary: "Lukarne is a free, open-source (MIT) Android TV app. You spin a night-and-day globe with the remote, dive into a region, and a 3×3 wall of live webcams fills up: California and Delaware road cams, Finnish weather cams, 24/7 YouTube live cams. Free to try: it's a sideload, no account, no ads. How Claude helped. Claude Code wrote the code (Kotlin and Compose, an OpenGL ES globe, a Python catalogue…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["search & media", "products & launches", "models & research", "jobs & society"]
content_source: "post"
word_count: 395
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xgr28v/i_built_an_android_tv_app_with_claude_code_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an Android TV app with Claude Code: a night-and-day globe and walls of live webcams. What it had to measure on the TV instead of guessing

Reddit · cyberdinn · 2026-10-27

Lukarne is a free, open-source (MIT) Android TV app. You spin a night-and-day globe with the remote, dive into a region, and a 3×3 wall of live webcams fills up: California and Delaware road cams, Finnish weather cams, 24/7 YouTube live cams. Free to try: it's a sideload, no account, no ads. How Claude helped. Claude Code wrote the code (Kotlin and Compose, an OpenGL ES globe, a Python catalogue pipeline, a GitHub Actions job that rebuilds the catalogue every day) and the scripts that build, install and measure on the device. What worked best was making it measure instead of guess. Four examples from the decision log: The globe. The first version was drawn with Compose Canvas: on the Shield's Tegra X1 the land dots alone took 28 ms a frame. It moved the globe to OpenGL ES on its own thread (dots and coastlines in VBOs, the projection in the vertex shader, 4 draw calls): about 3 ms a frame, 60 fps. How many live tiles. The decoder declares no instance limit, so it measured: 9 H.264 streams at once worked, first frames in 2.3 to 3.6 s. The app plays up to 8. Measuring at all. adb shell input starts a Java VM for every key press, which skews the very frame you want to measure, so it built an autopilot that presses keys from inside the app. It also found debug builds about 10× slower per frame, so every number comes from the release build. A frozen YouTube cam I couldn't reproduce on demand. It logged every player state and found the cause: the video was loaded while its WebView was briefly detached from the window. After the fix it checked 12 switches, 8 quick double switches and 2 minutes of demo mode: every cam started. What didn't work. Grabbing fresh YouTube frames on GitHub's runners: YouTube answers "Sign in to confirm you're not a bot". Frames grabbed on the TV worked, but storing YouTube frames goes against YouTube's terms, so they were removed before release; only the road cams keep them. Windy's webcams were dropped too: its API terms forbid redistribution. Limits. Tested only on a Shield (Android 11), needs Android TV 9 or later, and one YouTube cam plays at a time. Every decision, with its measurements and the options we dropped, is in the repo's decision log: https://github.com/storagebits/lukarne
