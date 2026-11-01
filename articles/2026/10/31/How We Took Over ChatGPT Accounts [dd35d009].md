---
id: "dd35d009aad680f7"
title: "How We Took Over ChatGPT Accounts"
url: "https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts"
link: "https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-10-31T23:15:22Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Simon Willison"]
language: "en"
summary: "How We Took Over ChatGPT Accounts \nParameter Labs describe an exploit they found against ChatGPT's implementation of the artifacts pattern (OpenAI used to call this \"Canvas\" but it looks like the latest revision is called HTML previews ), where interactive custom HTML apps are displayed in a sandboxed iframe. \n It's important that HTML in these stays tightly sandboxed to avoid untrusted code…"
tags: ["iframes", "javascript", "sandboxing", "security", "xss", "openai", "chatgpt", "content-security-policy"]
orgs: ["OpenAI"]
topics: ["search & media"]
content_source: "fulltext"
word_count: 364
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# How We Took Over ChatGPT Accounts

Simon Willison · Simon Willison · 2026-10-31

31st October 2026 - Link Blog
How We Took Over ChatGPT Accounts (via) Parameter Labs describe an exploit they found against ChatGPT's implementation of the artifacts pattern (OpenAI used to call this "Canvas" but it looks like the latest revision is called HTML previews), where interactive custom HTML apps are displayed in a sandboxed iframe.
It's important that HTML in these stays tightly sandboxed to avoid untrusted code interacting with OpenAI APIs and accessing private data.
Parameter found quite a complex attack chain. OpenAI use the MathLive JavaScript library as part of their graph support, and that library includes its own virtual keyboard, which can be triggered in the parent page via postMessage() from the sandboxed iframe.
That message receiving code uses innerHTML, so anything that sends a message can add custom HTML to the parent - and there was no mechanism to prevent other sandboxed frames, including HTML preview frames, from calling that method.
This meant untrusted code in an iframe could insert HTML, and while innerHTML doesn't directly execute script elements it could be used to inject a new iframe without sandbox restrictions.
OpenAI’s CSP rules blocked inline scripts entirely, and only allowed script loading from a handful of domains, but one of those was YouTube - and the YouTube oEmbed endpoint could be used to reflect JavaScript back in a way that executed it.
Once the attack had JavaScript execution on ChatGPT, it was trivial to fetch private user data from APIs and exfiltrate it via an image reference.
The end result: you could create a ChatGPT share URL which, when visited by another signed-in user, could exfiltrate their private data or take actions on their behalf.
OpenAI closed the hole and paid out a $5,000 bug bounty, which I think was a bit cheap for a vulnerability this serious.
Recent articles
- The October inflection point for vibe game development - 28th October 2026
- Battle Drones - a vibe coded RTS with audio-based multiplayer - 20th October 2026
- Hello Python 3.15, goodbye 3.10, and now I can use 3.11 - 12th October 2026
- A new feature for my blog, built using my voice - 9th October 2026
