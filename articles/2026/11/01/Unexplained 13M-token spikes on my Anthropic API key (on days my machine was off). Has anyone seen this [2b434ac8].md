---
id: "2b434ac860f9c17a"
title: "Unexplained 13M-token spikes on my Anthropic API key (on days my machine was off). Has anyone seen this?"
url: "https://reddit.com/r/ClaudeAI/comments/1xl3dqt/unexplained_13mtoken_spikes_on_my_anthropic_api"
link: "https://reddit.com/r/ClaudeAI/comments/1xl3dqt/unexplained_13mtoken_spikes_on_my_anthropic_api"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T13:42:34Z"
published_date: "2026-11-01"
collected_at: "2026-11-02T13:05:12Z"
authors: ["rodnr_"]
language: "en"
summary: "My normal consume is maximum 300k tokens per day, and I got an alert that I ran out of credits which I had just recharged. Looking into the panel I found out something has consumed over 10M cache read tokens at 3AM - which I didn't have any scheduled action neither I was online on my computer. FYI I've been working with software for 10 years, so I understand structured backends to keep these…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 212
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xl3dqt/unexplained_13mtoken_spikes_on_my_anthropic_api/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Unexplained 13M-token spikes on my Anthropic API key (on days my machine was off). Has anyone seen this?

Reddit · rodnr_ · 2026-11-01

My normal consume is maximum 300k tokens per day, and I got an alert that I ran out of credits which I had just recharged. Looking into the panel I found out something has consumed over 10M cache read tokens at 3AM - which I didn't have any scheduled action neither I was online on my computer. FYI I've been working with software for 10 years, so I understand structured backends to keep these keys private and secure, What I ruled out so far: - It came from one single API Key, which is relatively new and I confirmed it is not public anywhere. - This API key is tied to 2 processes and they didn't trigger any runs on that day. - Console analytics: the Claude Code usage page shows no members or sessions. The API key page doesn’t show last-used time or request origin. - I didn't ran out of my monthly plan usage to use additional credits https://preview.redd.it/gea39ly870zh1.png?width=1124&format=png&auto=webp&s=235e50856e6cc12664790dba35b5dc64b6063f60 I already replaced this key with a new one, but, this is not the first time it has happened. 2 months ago I had to deactivate another key because it was happening exactly the same. https://preview.redd.it/kj04vdvt80zh1.png?width=1104&format=png&auto=webp&s=7b8c3256992478a091c1cf348a2471cca8f98e87 Any ideas to help me track? I've applied a budget limit to my account now
