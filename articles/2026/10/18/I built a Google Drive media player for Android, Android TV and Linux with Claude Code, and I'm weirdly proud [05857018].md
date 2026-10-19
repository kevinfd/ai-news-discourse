---
id: "0585701880cb954b"
title: "I built a Google Drive media player for Android, Android TV and Linux with Claude Code, and I'm weirdly proud of it 😅"
url: "https://reddit.com/r/ClaudeAI/comments/1x9a05m/i_built_a_google_drive_media_player_for_android"
link: "https://reddit.com/r/ClaudeAI/comments/1x9a05m/i_built_a_google_drive_media_player_for_android"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T18:09:09Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Anything-Greedy"]
language: "en"
summary: "Hey everyone! I'm a third-year Computer Science student, and over the past week or so I've been working on a project called DriveCinema. 🎯 The problem I know about solutions like Jellyfin, and a friend of mine runs a home media server. But whenever I want something added, I have to ask him to do it for me. It's not a huge deal, but I don't want to keep bothering him every time I want to watch…"
tags: ["r/ClaudeAI"]
orgs: ["Google", "Anthropic", "Samsung"]
topics: ["search & media", "products & launches", "agents & coding", "models & research"]
content_source: "post"
word_count: 833
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9a05m/i_built_a_google_drive_media_player_for_android/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a Google Drive media player for Android, Android TV and Linux with Claude Code, and I'm weirdly proud of it 😅

Reddit · Anything-Greedy · 2026-10-18

Hey everyone! I'm a third-year Computer Science student, and over the past week or so I've been working on a project called DriveCinema. 🎯 The problem I know about solutions like Jellyfin, and a friend of mine runs a home media server. But whenever I want something added, I have to ask him to do it for me. It's not a huge deal, but I don't want to keep bothering him every time I want to watch something new. Setting up my own media server would solve that, but then I'd need a machine to run it, maintain it and keep it available. So I started thinking: what if I could use the Google Drive storage I already have instead? 🎬 What DriveCinema does DriveCinema is a media player for videos stored in your own Google Drive. You sign in with Google, point it at a folder, and it builds a library with posters and details, Continue Watching, and series with seasons and a Next Episode button. No server to run or maintain. • Platforms: Android phone, Android TV (remote-friendly UI, sign in by pairing with your phone) and Linux desktop (.deb) • Read-only Drive access: the app can't change or delete anything in your Drive • Not supported (yet): iOS, Windows packaging is still in progress, and Samsung/LG TVs need a Google TV stick 🤖 Being honest about the AI part I want to be upfront: this project is largely vibe-coded with Claude Code. I'm not going to pretend I wrote the codebase myself or that I fully understand every part of it. But I've been actively involved the whole time: shaping what the app should be, testing every build on real devices (phone, TV, laptop), troubleshooting issues, configuring Google OAuth and release signing, and getting the Linux package built and working. Since I didn't want to blindly trust AI-written code, I also had it run a robustness audit on its own code. It found 18 issues, including a real security bug where the Google sign-in token was sent along on redirects. Each one got fixed with a regression test and checked on real devices, and testing on the TV turned up a few more small ones that I fixed too. And honestly, it turned out way better than I imagined. I feel genuinely proud of it, which is kind of embarrassing considering how much of the actual coding the AI did. 😅 But I've grown pretty attached to this little project. 🙋 A bit about me I'm still a beginner. I'm currently learning PHP and Laravel at uni (I've built things like a URL shortener and a magic-link password reset), and some days I feel like I'm nowhere near being a "proper" software developer. I'm not always sure I'm heading in the right direction, so seeing an AI build something like this in a week was exciting and a little discouraging at the same time. My plan now is to learn Kotlin properly by fixing and extending this codebase myself, using the AI as a reviewer instead of the author. 🌱 Why open source and not a product At one point, I even considered turning DriveCinema into a more serious project that could make some money. But since almost all of the code was generated with AI, I'm not confident enough in my understanding of every part to treat it as a commercial product. I'm also not convinced it's polished or convenient enough yet that people would want to pay for it. So I decided to make it public and see if it can grow into a nice little open-source project. Honestly, I don't feel like I have much to lose. Worst case, nobody checks it out and things stay as they are. Best case, I get valuable feedback, learn from more experienced developers, and maybe other people find it useful or even want to contribute. Knowing that something I helped bring to life is actually useful to someone would be a pretty great feeling. ⚠️ One important limitation Google treats Drive access as a "restricted" permission, and making the sign-in public needs Google's verification (including a paid security assessment). So for now, you need your own free Google Cloud OAuth client to use it. There's a step-by-step setup guide in the README. 💬 I'd love to hear your thoughts • Would you actually use something like this? • What features would make it more useful? • If you're an experienced developer, is there anything about the architecture or implementation you'd approach differently? • If you've gone through a similar AI-assisted journey, what did you learn from it? And how did you keep learning yourself along the way? Feel free to explore the code, report bugs, suggest features or even contribute. It's GPLv3. GitHub: https://github.com/MONHuN23/DriveCinema-app I'm not expecting this to become the next big thing. I just wanted to build something useful, learn along the way, and see what happens when I share it with the world. Thanks for reading! ❤️
