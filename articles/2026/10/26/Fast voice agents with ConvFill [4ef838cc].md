---
id: "4ef838cc73364d47"
title: "Fast voice agents with ConvFill"
url: "https://reddit.com/r/LocalLLaMA/comments/1xfzdqu/fast_voice_agents_with_convfill"
link: "https://reddit.com/r/LocalLLaMA/comments/1xfzdqu/fast_voice_agents_with_convfill"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-26T15:06:08Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["futterneid"]
language: "en"
summary: "Voice agents are either fast or smart. ConvFill proposes a way to bridge that gap by training a smol talker model (0.6B!) to talk with cheat notes from a large reasoner model. The way it works is this: after the user's speech is transcribed, the talker replies quickly to buy itself time while the reasoner thinks. The reasoner then generates an appropriate response, which the talker reads to…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "agents & coding", "health & science"]
content_source: "post"
word_count: 214
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xfzdqu/fast_voice_agents_with_convfill/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Fast voice agents with ConvFill

Reddit · futterneid · 2026-10-26

Voice agents are either fast or smart. ConvFill proposes a way to bridge that gap by training a smol talker model (0.6B!) to talk with cheat notes from a large reasoner model. The way it works is this: after the user's speech is transcribed, the talker replies quickly to buy itself time while the reasoner thinks. The reasoner then generates an appropriate response, which the talker reads to continue the conversation. It's a bit like if you went on a panel with rocket scientists and had a little earbud with your own expert that could tell you what to say. You just reply quickly so as not to blow your cover, and then you begin saying what the expert in your earbud is telling you. Playing with the model, I think the main idea is there and this could be a great direction to go, but the talker model should be a bit smarter for it to work like magic. Still, really cool direction! ConvFill was developed by students from the University of Washington UbiComp Lab. I found it cool, so I reached out to them so we could build a really good demo for it together. They are presenting their paper at EMNLP this week. Go try it out in our demo: https://huggingface.co/spaces/smolagents/convfill-speech-demo
