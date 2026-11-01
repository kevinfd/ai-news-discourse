---
id: "6899180bc665f115"
title: "[Discussion] WiCi: Connecting a GPU over the WiFi"
url: "https://reddit.com/r/LocalLLaMA/comments/1xkaqk0/discussion_wici_connecting_a_gpu_over_the_wifi"
link: "https://reddit.com/r/LocalLLaMA/comments/1xkaqk0/discussion_wici_connecting_a_gpu_over_the_wifi"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T13:50:04Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["shubham0204_dev"]
language: "en"
summary: "I'm an on-device ML enthusiast, not affiliated with WiCi I follow the NetworkChuck YT channel and he (Chuck Keith) posted a video on WiCi, a wireless GPU that connects to the host computer over WiFi. The host computer sees the wireless GPU as a native GPU connected to the computer and also shows up in the Windows Task Manager. Video: https://youtu.be/cFdoXn6yvE4?si=gUCzg3UbzkCGXQYo WiCi:…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 305
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xkaqk0/discussion_wici_connecting_a_gpu_over_the_wifi/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# [Discussion] WiCi: Connecting a GPU over the WiFi

Reddit · shubham0204_dev · 2026-10-31

I'm an on-device ML enthusiast, not affiliated with WiCi I follow the NetworkChuck YT channel and he (Chuck Keith) posted a video on WiCi, a wireless GPU that connects to the host computer over WiFi. The host computer sees the wireless GPU as a native GPU connected to the computer and also shows up in the Windows Task Manager. Video: https://youtu.be/cFdoXn6yvE4?si=gUCzg3UbzkCGXQYo WiCi: https://wici.ai The video also demonstrates running DeepSeek and some graphics-intensive games. The GPU being shared over WiFi in the video is a RTX 5090. I wanted to dig deep into how WiFi as a protocol can be used for communicating with the GPU. In a normal situation, the GPU will communicate via PCIe with the CPU of the host computer, ensuring high-bandwidth data transfers. I found the following lines in a blog that WiCi has shared: So WiCi keeps the local-GPU contract while shrinking what actually crosses the link: cache stable facts, deduplicate repeated payloads, compress or stream large transfers, pipeline independent work, keep expensive state resident, and preserve true dependencies exactly. What I feel is that, WiCi, has introduced an intermediate layer between the host and the GPU that facilitates communication. The commands intended for the GPU, are first encoded in some intermediate language, passed through the network and decoded back within the WiCi remote GPU (the silver box holding the 5090) into commands that the CUDA driver understands. WiCi does not seem to replace the physical PCIe protocol with IEEE 802.11 (WiFi) protocol over the physical medium. This is my assumption and I am not sure about it. But if this product proves what it claims, then this would be a huge deal in my opinion. A shared GPU that the different devices can use would be great for local LLMs. Let me know what you all think about this tech!
