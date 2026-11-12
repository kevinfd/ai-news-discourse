---
id: "b5a98cb63ea1d74c"
title: "I built an animated watch face for my Galaxy Watch with Claude, and it turned into a little farm story with a sneaky wolf"
url: "https://reddit.com/r/ClaudeAI/comments/1xtne5p/i_built_an_animated_watch_face_for_my_galaxy"
link: "https://reddit.com/r/ClaudeAI/comments/1xtne5p/i_built_an_animated_watch_face_for_my_galaxy"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T17:10:22Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["ArTtemiishanks"]
language: "en"
summary: "So this started as me just cleaning up my Galaxy Watch4 Classic. I asked Claude (Opus, in the Claude app) to help me remove apps I don't use over ADB, and it got rid of 21 of them. Then I thought, why not make my own watch face? I've never made one before. I built it one piece at a time. I'd say what I wanted, send a photo of my watch screen, and Claude would build the next version. It drew all…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "Samsung"]
topics: ["products & launches", "jobs & society"]
content_source: "post"
word_count: 352
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xtne5p/i_built_an_animated_watch_face_for_my_galaxy/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built an animated watch face for my Galaxy Watch with Claude, and it turned into a little farm story with a sneaky wolf

Reddit · ArTtemiishanks · 2026-11-11

So this started as me just cleaning up my Galaxy Watch4 Classic. I asked Claude (Opus, in the Claude app) to help me remove apps I don't use over ADB, and it got rid of 21 of them. Then I thought, why not make my own watch face? I've never made one before. I built it one piece at a time. I'd say what I wanted, send a photo of my watch screen, and Claude would build the next version. It drew all the art with Python, wrote the watch face in Google's Watch Face Format, packaged it into an installable APK, and when the face wouldn't load at first, it read my watch's error logs and fixed the problem. The video is rendered from the same files that run on my watch. What it does (it's a 45-second day/night loop): - During the day, a boy walks out of his cabin, chops a tree, carries the logs in a sack, stacks them on the woodpile and goes back inside. The sun and clouds move across the sky. - At night you get the aurora, twinkling stars and a rocket flying past. A sheep opens the fence gate and sneaks out to eat grass... and the wolf hiding behind the bush has been waiting for exactly that. - It also shows real data: time, date, a step arc that fills up toward your daily goal, and your sleep score from Samsung Health. - Fireworks go off once you hit your step goal, and when your battery drops below 20% the chimney smoke goes thin and the cabin lights dim. - Tap a sheep and it says "Baa!", tap the cabin and the lights flicker. It's free. The APK and all the source are here: https://github.com/ArtTemiiss/aurora-farm-watchface You install it with adb (steps are in the README). I've only tested it on my Watch4 Classic, so I'm not sure about other Wear OS watches. Honestly, this was one of the most fun things I've done with Claude. Adding one silly idea at a time and watching it come alive on my wrist was great.
