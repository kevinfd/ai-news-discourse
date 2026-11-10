---
id: "6f6fff482120edaf"
title: "Quoting Prompting Claude Fable 5.2"
url: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52"
link: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-10T05:34:14Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Simon Willison"]
language: "en"
summary: "Claude Fable 5.2 responds closely to what the prompt says about who owns the code it works on. In Anthropic’s testing on small coding tasks, when a prompt said nothing about ownership or presented the code base as someone else’s, the model tended to add to the existing structure, even when that repeated existing code. [...] \n If you want the model to improve the structure as it works, say that…"
tags: ["prompt-engineering", "anthropic", "generative-ai", "ai", "llms", "claude-mythos-fable"]
orgs: ["Anthropic", "Alibaba"]
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 192
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Quoting Prompting Claude Fable 5.2

Simon Willison · Simon Willison · 2026-11-10

10th November 2026
Claude Fable 5.2 responds closely to what the prompt says about who owns the code it works on. In Anthropic’s testing on small coding tasks, when a prompt said nothing about ownership or presented the code base as someone else’s, the model tended to add to the existing structure, even when that repeated existing code. [...]
If you want the model to improve the structure as it works, say that the code is its own:
This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it.
In Anthropic’s testing on small coding tasks, the model merged repeated code in about half of the tries with this sentence, and in under a tenth of the tries without it.
— Prompting Claude Fable 5.2, Anthropic documentation
Recent articles
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
- The U.S. Census Bureau and “Super Intelligence” - 2nd November 2026
