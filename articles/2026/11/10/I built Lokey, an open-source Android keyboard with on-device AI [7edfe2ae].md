---
id: "7edfe2aefb21d30b"
title: "I built Lokey, an open-source Android keyboard with on-device AI"
url: "https://reddit.com/r/LocalLLaMA/comments/1xsn0hz/i_built_lokey_an_opensource_android_keyboard_with"
link: "https://reddit.com/r/LocalLLaMA/comments/1xsn0hz/i_built_lokey_an_opensource_android_keyboard_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T13:33:36Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["Nicolodeva"]
language: "en"
summary: "I’ve been building Lokey, an open source, Android keyboard that runs word prediction, autocorrect, dictation and translation on your phone. Hold Enter to dictate, or translate text straight into the app you’re typing in. Lokey uses a fork of llama.cpp for text inference and takes advantage of its Hexagon NPU backend on supported Snapdragon phones. It can also run inference on two CPU threads. In…"
tags: ["r/LocalLLaMA"]
orgs: ["Alibaba"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 282
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsn0hz/i_built_lokey_an_opensource_android_keyboard_with/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I built Lokey, an open-source Android keyboard with on-device AI

Reddit · Nicolodeva · 2026-11-10

I’ve been building Lokey, an open source, Android keyboard that runs word prediction, autocorrect, dictation and translation on your phone. Hold Enter to dictate, or translate text straight into the app you’re typing in. Lokey uses a fork of llama.cpp for text inference and takes advantage of its Hexagon NPU backend on supported Snapdragon phones. It can also run inference on two CPU threads. In everyday use on the phones I’ve tested, the keyboard has stayed responsive and I haven’t noticed unusual battery drain with either setup. For suggestions, Lokey turns the model’s token logits into probabilities and uses them to rank up to three complete words that match what you’ve typed so far. One text model handles suggestions, autocorrect and translation. A separate speech model handles dictation. Text models · LFM 2.5 350M (~230 MB) or Qwen 3.5 0.8B (~533 MB) Speech models · Parakeet v3 0.6B or Qwen3 ASR 0.6B Typing works without any model downloads. Once you’ve downloaded the models you want, inference works offline. Typed text and mic audio stay on the device, and Lokey has no accounts or analytics SDK. I also spent time on the keyboard itself. You can use recordings of real mechanical switches as key sounds and customize haptics, layouts and colors. Swipe typing, adaptive letters and autocorrect are opt-in. It’s an early beta. I’ve tested on a OnePlus 15 and a POCO F3. If you try it, I’d love to know which phone, language and model you used, and whether suggestions can keep up with your typing. Source code (MIT) · Signed APK (Android 9+, ARM64) · 83-second demo English isn’t my first language, so I used AI to help edit this post.
