---
id: "739913a19f2441b7"
title: "Claude helped me unbrick my friend's Pixel 10 without losing any data (Opus 5.5, Claude Code)"
url: "https://reddit.com/r/ClaudeAI/comments/1xin15e/claude_helped_me_unbrick_my_friends_pixel_10"
link: "https://reddit.com/r/ClaudeAI/comments/1xin15e/claude_helped_me_unbrick_my_friends_pixel_10"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T15:25:24Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["Responsible_Cow2236"]
language: "en"
summary: "My friend woke up and his Pixel 10 was stuck on this screen: \"Android system can't be loaded. Your data may be corrupt.\" It only offered two options: try again, or factory reset. He didn't want to lose his data, so I sent Claude (Opus 5.5) a photo of the screen and we worked through it step by step. What we tried, in order: Pressed \"Try again.\" The phone booted, but after unlocking, the screen…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["products & launches"]
content_source: "post"
word_count: 308
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xin15e/claude_helped_me_unbrick_my_friends_pixel_10/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude helped me unbrick my friend's Pixel 10 without losing any data (Opus 5.5, Claude Code)

Reddit · Responsible_Cow2236 · 2026-10-29

My friend woke up and his Pixel 10 was stuck on this screen: "Android system can't be loaded. Your data may be corrupt." It only offered two options: try again, or factory reset. He didn't want to lose his data, so I sent Claude (Opus 5.5) a photo of the screen and we worked through it step by step. What we tried, in order: Pressed "Try again." The phone booted, but after unlocking, the screen went black, froze, and dropped back into recovery. Booted into safe mode. Same black screen and freeze. Reinstalled Android using the official update file. I used Claude Code for this part: - It set up Google's adb tool on my PC and confirmed the PC could see the phone - It found the newest official update for the Pixel 10 (Android 17, Oct 2026, CP3A.261005.005, 3.31 GB), downloaded it from Google, and verified the file's checksum - It ran the install (adb sideload). This replaces Android's system files but keeps your personal data - The install succeeded, but the phone still froze after unlocking. That proved Android itself wasn't broken He uninstalled Dragon Ball Legends. The phone has worked fine ever since. My best guess: his storage was almost full and the game was taking up a lot of it. A nearly full phone can fail exactly like this, even in safe mode. If this happens to you: - Don't factory reset first. Try the steps above - Check your storage. If it's nearly full, free up space before anything else - Reinstalling Android through adb sideload doesn't erase your data, and it tells you whether the system itself is the problem - Use a USB-C cable that supports data, not just charging, or your PC won't detect the phone - The red error lines on the sideload screen are normal. Ignore them
