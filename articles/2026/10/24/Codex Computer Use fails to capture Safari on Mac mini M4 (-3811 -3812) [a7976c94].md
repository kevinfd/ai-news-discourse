---
id: "a7976c9441a1f09c"
title: "Codex Computer Use fails to capture Safari on Mac mini M4 (-3811 / -3812)"
url: "https://reddit.com/r/OpenAI/comments/1xe5qs2/codex_computer_use_fails_to_capture_safari_on_mac"
link: "https://reddit.com/r/OpenAI/comments/1xe5qs2/codex_computer_use_fails_to_capture_safari_on_mac"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-24T11:00:40Z"
published_date: "2026-10-24"
collected_at: "2026-10-24T12:05:48Z"
authors: ["darkprinceimmortal"]
language: "en"
summary: "Anyone else getting Safari capture failures with Codex Computer Use on Apple Silicon? I’m on a Mac mini M4, macOS 27.0.1, with ChatGPT desktop app 26.1021.31345 and Computer Use build 1001631. Trying to use Safari fails with: SCStreamErrorDomain -3811: Failed to start stream due to audio/video capture failure Screen recording and device control permissions are enabled for Codex Computer Use.…"
tags: ["r/OpenAI"]
orgs: ["OpenAI", "Apple"]
topics: ["products & launches"]
content_source: "post"
word_count: 252
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/OpenAI/comments/1xe5qs2/codex_computer_use_fails_to_capture_safari_on_mac/"
score: null
comments: null
community: "r/OpenAI"
---

# Codex Computer Use fails to capture Safari on Mac mini M4 (-3811 / -3812)

Reddit · darkprinceimmortal · 2026-10-24

Anyone else getting Safari capture failures with Codex Computer Use on Apple Silicon? I’m on a Mac mini M4, macOS 27.0.1, with ChatGPT desktop app 26.1021.31345 and Computer Use build 1001631. Trying to use Safari fails with: SCStreamErrorDomain -3811: Failed to start stream due to audio/video capture failure Screen recording and device control permissions are enabled for Codex Computer Use. Restarting the apps didn’t fix it. During troubleshooting, the macOS capture log reported TCC Allow, then failed while creating the screenshot. The helper logs also showed a failed display lookup for an off-screen window. That’s what the logs showed; I don’t know the underlying cause. Restarting the Computer Use helper and bringing a normal Safari window onto the main display briefly restored control and screenshots. It was able to complete a posting task, but capture later failed again with: SCStreamErrorDomain -3812: Failed due to an invalid parameter The later log said: contentRect does not contain sourceRect. Restarting the helper and reconnecting let it continue again, so this is intermittent, not a lasting fix. Separately, the ChatGPT Mac interface sometimes freezes while voice mode keeps talking and responding. I can’t switch chats or click options when that happens. I’m not assuming that freeze and the Computer Use capture failure have the same cause. Has anyone found a stable fix for either issue? What Mac, macOS version, and app version are you using? I use these apps for work, so a reliable workaround would help. I also posted the original combined report here: https://www.reddit.com/r/ChatGPT/comments/1xe5o06/chatgpt_mac_app_freezes_but_voice_keeps_going/
