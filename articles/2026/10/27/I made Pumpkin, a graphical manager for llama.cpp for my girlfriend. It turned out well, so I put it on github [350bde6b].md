---
id: "350bde6b5d329523"
title: "I made Pumpkin, a graphical manager for llama.cpp for my girlfriend. It turned out well, so I put it on github"
url: "https://reddit.com/r/LocalLLaMA/comments/1xgnhw5/i_made_pumpkin_a_graphical_manager_for_llamacpp"
link: "https://reddit.com/r/LocalLLaMA/comments/1xgnhw5/i_made_pumpkin_a_graphical_manager_for_llamacpp"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T09:05:13Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["gbolgurov"]
language: "en"
summary: "As the title says, my girlfriend needed a local model for privacy reasons, but her terminal skills are... nonexistent, so I made an all-in-one graphical manager for llama.cpp that gets you up and running in around 5 minutes. In my humble opinion, it turned out rather well, so I put it on GitHub, and I think it will help some of you who are either just staring out and haven't touched a terminal…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 299
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xgnhw5/i_made_pumpkin_a_graphical_manager_for_llamacpp/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# I made Pumpkin, a graphical manager for llama.cpp for my girlfriend. It turned out well, so I put it on github

Reddit · gbolgurov · 2026-10-27

As the title says, my girlfriend needed a local model for privacy reasons, but her terminal skills are... nonexistent, so I made an all-in-one graphical manager for llama.cpp that gets you up and running in around 5 minutes. In my humble opinion, it turned out rather well, so I put it on GitHub, and I think it will help some of you who are either just staring out and haven't touched a terminal before or want an all-in-one manager for all your models with extra capabilities. Pumpkin looks at your hardware, downloads the right llama.cpp build and picks a quant that fits your GPU and RAM, so you go from install to a running model in a few clicks. It finds models you already have from LM Studio and Ollama, and gives you a chat with web search, tools, MCP servers, Claude-style skills and connectors for GitHub, Notion, Git, Postgres and more. Pumpkin Code is a coding agent that works in a folder you point it to and can ask before changing files or running commands. You can ask questions about your own documents, and attach pictures even to models that can't see (a small vision model describes them first). It also makes pictures and short videos through stable-diffusion.cpp (extra install), and works from your phone. It's a very early release and most of my testing is on Ubuntu and Mac. Windows and Android work, but I haven't tried them properly because I lack the hardware, so that's where I expect the rough edges. I'd really like to hear what breaks. You can find the project here: GitHub: https://github.com/geobellingham/pumpkin Disclamer: It’s open source and I am not trying to make money off of this. Posting this because I truly believe this will be useful so some of you :).
