---
id: "1d9c16e268a71913"
title: "Open sourced DaVinci Resolve in C++ with h264, h265, AAC support on Linux and miles better performance."
url: "https://reddit.com/r/ClaudeAI/comments/1xr312k/open_sourced_davinci_resolve_in_c_with_h264_h265"
link: "https://reddit.com/r/ClaudeAI/comments/1xr312k/open_sourced_davinci_resolve_in_c_with_h264_h265"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T16:54:56Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["SeniorMatthew"]
language: "en"
summary: "Hey! I’m Matthew and with a help of Claude Max I managed to make a good enough open source copy of DaVinci Resolve in C++! It’s called Kinoklip. I’m not sure whether I’m going to get hated here. Myself, I am strongly oppose AI art, but using AI as a tool in programming to free yourself from proprietary corporate software, doesn’t feel that bad to me. I’m a programmer myself, mostly C# for…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Nvidia"]
topics: ["chips & infrastructure", "agents & coding", "jobs & society", "models & research"]
content_source: "post"
word_count: 710
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xr312k/open_sourced_davinci_resolve_in_c_with_h264_h265/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Open sourced DaVinci Resolve in C++ with h264, h265, AAC support on Linux and miles better performance.

Reddit · SeniorMatthew · 2026-11-08

Hey! I’m Matthew and with a help of Claude Max I managed to make a good enough open source copy of DaVinci Resolve in C++! It’s called Kinoklip. I’m not sure whether I’m going to get hated here. Myself, I am strongly oppose AI art, but using AI as a tool in programming to free yourself from proprietary corporate software, doesn’t feel that bad to me. I’m a programmer myself, mostly C# for gamedev, but I’m sure not on a level of creating a whole video editor alone. So, why use an AI Project made by a random dude of the internet instead of somethine like Kdenlive? It is a copy of DaVinci Resolve explicitly. It is quite a lot different from Kdenlive. And to anyone who has ever used DaVinci before that is not a debate. I’m not saying that Kdenlive is bad, not at all. I think it is a really great project and the fact that it’s made by KDE team makes it even better! But for those who want something which is more familiar to DaVinci, sadly it doesn’t suite them that well. So, if you aren’t one of those people, or don’t like AI projects — feel free to downvote or just scroll past it For those who don’t care as much, I genuinely think that this project is a good replacement for DaVinci Resolve! Only after 4 days of development, my personal workflow has been fully covered! Including all the small details, and even some improvements has been made to it! DaVinci has a lot of issues on Linux , my primary reasons are: - Installation is a hell. You either use a distrobox container, like DaVinci Resolve, or install it manually, which is not easy at all. - Lack of h264, h265 and AAC codecs. Paid version only solves h264/5 and only for nvidia gpus. - Performance is bad on anything else but NVIDIA. On my personal machine performance is at least 10 times better. A lot of other users said similar things. Therefore on Windows, paid DaVinci Resolve is fine, on Linux it still isn’t. All the 7 pages of DaVinci are done. But I can only make sure that the edit tab is fully done. Even tho AI has gotten far better in the last years in terms of coding, it still is far from perfect. There were like 30 little problems with just the editing tab which I had to find manually. So this is a call for help! If you wish to try this project and use more advanced features of DaVinci, it would be incredibly helpful! Also there are a lot of things which are in the core design of this app: Performance - it should run on all the GPUs. It runs incredibly fast on my Thinkpad with Iris XE Graphics. Human readability - I would love for this project to have actual humans contributing to it one day. Extendable code - all the code should be easy to be built upon. Openness - GPL 3.0 More options - compared to something like DaVinci, for stuff like All the code is written by AI for now. Only the icons were made by me. I do not support AI art here. (And all the kittens in the preview images are real photos!) Also each change goes through 140+ different test programs, to ensure that none of them will break the functionality of a program. Claude Max was used. this text was fully written by me. And my favorite feature which I was surprised that no other video redactors have implemented yet is gotta be: One file - one project . When you drag and drop a file in to the project, it just copies and you can delete it from the place it used to be at. Now, you can easily backup one file or send it over to your friend. There's still an option to create an average project as well. https://github.com/SeniorMatt/kinoklip There are still some quirks here and there, but the whole base was build with Claude Extra High, each change goes through 170+ different test programs, to insure stability. And right now I'm waiting for the week limit reset to continue working on the project.
