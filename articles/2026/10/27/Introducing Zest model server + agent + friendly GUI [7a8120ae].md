---
id: "7a8120aea9e5704a"
title: "Introducing Zest: model server + agent + friendly GUI"
url: "https://reddit.com/r/LocalLLaMA/comments/1xgi2cx/introducing_zest_model_server_agent_friendly_gui"
link: "https://reddit.com/r/LocalLLaMA/comments/1xgi2cx/introducing_zest_model_server_agent_friendly_gui"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-27T03:34:50Z"
published_date: "2026-10-27"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Icaruswept"]
language: "en"
summary: "Hello, everyone. A friend of mine wanted to get into running local models, and so (with the liberal use of Claude), I built them Zest. https://github.com/yudhanjaya/Zest What it is: Zest is a UI that bundles Lemonade server (which installs llama.cpp and whatever backends are needed) and the Pi agent to provide a friendly interface for people who don't want to be messing around with command-line…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding", "jobs & society"]
content_source: "post"
word_count: 439
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xgi2cx/introducing_zest_model_server_agent_friendly_gui/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Introducing Zest: model server + agent + friendly GUI

Reddit · Icaruswept · 2026-10-27

Hello, everyone. A friend of mine wanted to get into running local models, and so (with the liberal use of Claude), I built them Zest. https://github.com/yudhanjaya/Zest What it is: Zest is a UI that bundles Lemonade server (which installs llama.cpp and whatever backends are needed) and the Pi agent to provide a friendly interface for people who don't want to be messing around with command-line servers and parameters. It comes and all the functionality needed for a new user without getting in the way. Just download an appimage, go through the start tour, and you're set up and ready to go. There are sane defaults baked in (like 128k context) and model recommendations (all tried and tested on 10GB VRAM to 26GB). https://preview.redd.it/m2k2sis4hxxh1.png?width=3000&format=png&auto=webp&s=9a2da757429f9348d9e91336581bd0fbea0d8c47 It comes with helpful docs, links to places to understand more about the subject - in short, everything needed for a new user. Entirely open-source, of course. If you have anyone you want to introduce to the world of local AI, please see if this is useful. And if you have ideas, suggestions - please open an issue, send a PR, and so on. Why lemonade and Pi? Lemonade: because it does a great job of handling backends and providing a server. Pi: because it's a simple, elegant agent Both are very easy to package in something like this and bring together. And because I'm lazy: both projects are receiving steady updates, because I don't want to write yet another inference server from scratch What it isn't: It's not for advanced users. There are jobs, but no subagents, for instance: in this case the Pi philosophy really helped. In fact, I myself use Strata and Opencode, so for advanced users, it recommends those in the Help section How is this different from Unsloth desktop / Atomic chat etc? It isn't. It just tries to be a lot more lightweight and user-friendly: I decided to do this after getting said friend to download and set up llama.cpp, Unsloth Desktop, Opencode etc . . . I noticed that at some point both choice paralysis and confusion with options just took over, and there was no easy way for them as a newcomer to figure out what x thing was really for. Every setting in Zest is explained. Including what inference engines do, the works. Everything is explained at basic levels - what a model is, how it works, and so on. I've kept the lemonade + pi analogy while trying to make sure the interface was intuitive. https://preview.redd.it/1eq31ippjxxh1.png?width=2000&format=png&auto=webp&s=c7613cd847a8380d79c22c6b1ffeef5dc5a3e6bb We also have some theme support- here's a sample: https://preview.redd.it/rg4gbuq3ixxh1.png?width=2250&format=png&auto=webp&s=a82df6475c57f7a5cd5e55644b1eeca1327d46c3 https://preview.redd.it/to4s90u4ixxh1.png?width=2250&format=png&auto=webp&s=45d00e6d859547475939528f38010e9ea4038029 Have a look, let me know what you think!
