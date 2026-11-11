---
id: "bf7c4a0c59ded287"
title: "I built a webcam X-ray mirror with Claude Fable 5.2"
url: "https://reddit.com/r/ClaudeAI/comments/1xstews/i_built_a_webcam_xray_mirror_with_claude_fable_52"
link: "https://reddit.com/r/ClaudeAI/comments/1xstews/i_built_a_webcam_xray_mirror_with_claude_fable_52"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T17:44:48Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Sourcecode12"]
language: "en"
summary: "I built a web page that works like an X-ray mirror. You point a webcam at your face and see a skull, brain and facial muscles pinned to your head and following it as you move. The jaw opens when you open your mouth, and if you hold up a hand you see its bones follow your fingers. What it does Skull, brain, muscles and eyes as separate layers, in an X-ray look or a solid look Mixed reality views:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["health & science"]
content_source: "post"
word_count: 373
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xstews/i_built_a_webcam_xray_mirror_with_claude_fable_52/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a webcam X-ray mirror with Claude Fable 5.2

Reddit · Sourcecode12 · 2026-11-10

I built a web page that works like an X-ray mirror. You point a webcam at your face and see a skull, brain and facial muscles pinned to your head and following it as you move. The jaw opens when you open your mouth, and if you hold up a hand you see its bones follow your fingers. What it does Skull, brain, muscles and eyes as separate layers, in an X-ray look or a solid look Mixed reality views: half real face and half interior, or an X-ray “lens” that follows your fingertip Optional labels for bones, brain regions and muscles Sliders to fit the skull to your own head, and to soften the edges Why I built it I wanted to test two things: whether a webcam and a browser are enough to make anatomy something you can explore on your own body, for educational use, and how far the Fable 5.2 model’s capabilities go on a project with real 3D data and live tracking. How Claude helped I built it with Claude Fable 5.2 in one chat. I described what I wanted and Claude wrote all the code. It also found an open anatomy dataset (BodyParts3D), simplified the 3D models, and aligned them to the face tracker’s reference face so the skull sits in the right place. I tested each version on my own webcam and asked for changes: manual fit sliders, labels and edge feathering all came from follow-up requests. The first working version took under an hour. How it works It’s a single HTML file. MediaPipe does the face and hand tracking in the browser and three.js draws the 3D. The video is processed on your own computer and never uploaded. Free to try It’s free, with no account. You can download the tool here and try it on your browser. Try the tool on Github . One caveat: the anatomy is a real dataset of one adult scaled to your head, so it shows where things typically sit. It isn’t a scan of you and it isn’t a medical tool. Anatomy models: BodyParts3D, © The Database Center for Life Science, CC BY-SA 2.1 Japan. Feedback welcome, especially on how well the skull lines up on different faces.
