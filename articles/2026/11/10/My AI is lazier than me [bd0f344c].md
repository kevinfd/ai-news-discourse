---
id: "bd0f344c7532f9b6"
title: "My AI is lazier than me"
url: "https://reddit.com/r/LocalLLaMA/comments/1xsytlk/my_ai_is_lazier_than_me"
link: "https://reddit.com/r/LocalLLaMA/comments/1xsytlk/my_ai_is_lazier_than_me"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T21:11:05Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["cerchez07"]
language: "en"
summary: "Let's start with my setup: I have 2 Sparks running glm 5.3 flash, and the harness is hermes agent running on a MacBook Air. While trying to justify all the money I spent (around 6500 euro for both machines, a long time ago when prices were just high instead of outrageous), I decided to hop on the decompilation wagon. As I know my fable at home is not \"THAT\" smart, I decided to start with…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["agents & coding"]
content_source: "post"
word_count: 472
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xsytlk/my_ai_is_lazier_than_me/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# My AI is lazier than me

Reddit · cerchez07 · 2026-11-10

Let's start with my setup: I have 2 Sparks running glm 5.3 flash, and the harness is hermes agent running on a MacBook Air. While trying to justify all the money I spent (around 6500 euro for both machines, a long time ago when prices were just high instead of outrageous), I decided to hop on the decompilation wagon. As I know my fable at home is not "THAT" smart, I decided to start with something small: I asked it to decompile and recompile the original Need for Speed Special Edition for MS-DOS, using the famous rea repo from GitHub. Its first reaction was "I know a better way, we will use DOSBox and run the game" — and it already started installing a DOS emulator on my Mac :). I stopped it and told it I want actual decompilation and recompilation. The second answer was, in other words, "It's a lot of work and it will take a long time. Think about it — do you really want this?" I insisted. It started the decompilation process, and after some breakthroughs it even became enthusiastic. At some point, decompilation was "DONE". We started the next phase: recompile for Android. I did not pay much attention to what it did, but it said that it could use some GitHub repo as a base and started working. After the initial APK, we had to iterate a few times on some crashes and controller issues, which it solved. During gameplay I noticed that some AI cars started the race going in reverse, the car did not slide no matter the speed, and other stuff. It definitely did not feel like the NFS I remember. I told it about it, and it started checking the code and making tweaks to the physics. I stopped it and challenged it: this means we will not preserve the original feel if we go down this path. To my surprise, we never did. It never used the decompiled code. It found an engine on GitHub which was using the original assets to mimic the original game. When I asked why, it said it was a lot faster than rewriting all the old code into current instructions… So I asked it to go back and do the job properly — and to no surprise, it found a recompiled NFS2 repo on GitHub and decided it's better to start from there rather than from scratch. I don't know how this will go, but I wanted to share this story, as I find it quite interesting the lengths it's willing to go to reach its goal as fast as possible even if this means ignoring previous instructions. P.S. This post was proofread by said AI, as English is not my own language — but the words are still my own, I double checked
