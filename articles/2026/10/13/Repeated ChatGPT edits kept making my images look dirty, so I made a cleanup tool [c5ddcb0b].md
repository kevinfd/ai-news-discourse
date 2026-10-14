---
id: "c5ddcb0b337084a8"
title: "Repeated ChatGPT edits kept making my images look dirty, so I made a cleanup tool"
url: "https://reddit.com/r/ChatGPT/comments/1x5aktu/repeated_chatgpt_edits_kept_making_my_images_look"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-13T22:21:48Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Kiko_Production"]
language: "en"
summary: "I’m working on a game and kept running into this with the art: after several rounds of edits in ChatGPT, images would pick up grain, blotches, and weird light or dark fringes around outlines. I’d finally get the design how I wanted it, but the image itself would look increasingly messy. So I made a small tool called AI Image Rehab to help clean that up. It runs locally on your computer with a…"
tags: ["r/ChatGPT"]
orgs: ["OpenAI"]
topics: ["jobs & society", "products & launches", "chips & infrastructure"]
content_source: "post"
word_count: 249
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1x5aktu/repeated_chatgpt_edits_kept_making_my_images_look/"
score: null
comments: null
community: "r/ChatGPT"
---

# Repeated ChatGPT edits kept making my images look dirty, so I made a cleanup tool

Reddit · Kiko_Production · 2026-10-13

I’m working on a game and kept running into this with the art: after several rounds of edits in ChatGPT, images would pick up grain, blotches, and weird light or dark fringes around outlines. I’d finally get the design how I wanted it, but the image itself would look increasingly messy. So I made a small tool called AI Image Rehab to help clean that up. It runs locally on your computer with a browser interface. You’ll need Python to launch it, but the basic automatic cleanup doesn’t need a GPU, and your images aren’t uploaded anywhere. For me, the best order is automatic cleanup first, then upscaling, then fixing individual spots manually inside the tool. After that, ideally, an artist would do a final touch-up pass. There’s still work to do afterward. It helps with the grain and fringes, but won’t automatically fix bad anatomy, inconsistent details, or something the generator drew wrong. Those problems still need attention. Also, watch out for over-smoothing. Detailed backgrounds and clothing can lose small patterns, fabric texture, stitching, or intentional grain during cleanup. Compare the result with the original at full size, because some of what gets removed might be detail you actually wanted. I’ve mainly tuned it on anime-style character art so far. If you try it on your own images, I’d be interested to hear where it helps and where it makes things worse. It’s free, and the code, setup instructions, and before/after examples are here: GitHub: AI Image Rehab
