---
id: "7e22d86f8614a23b"
title: "Not paid attention and Haiku was shipping to the production"
url: "https://reddit.com/r/ClaudeAI/comments/1xkhbp4/not_paid_attention_and_haiku_was_shipping_to_the"
link: "https://reddit.com/r/ClaudeAI/comments/1xkhbp4/not_paid_attention_and_haiku_was_shipping_to_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-31T18:16:48Z"
published_date: "2026-10-31"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Admirable_Rip443"]
language: "en"
summary: "I thought Haiku 5.5 shipped two features for me in an hour. Git says nine commits. I use Claude Code on a side project, a Discord-style chat app with a Go backend, Postgres, a Svelte frontend, Matrix for messaging and LiveKit for calls. I'd been running Haiku 5.5 for a while without really paying attention, and I assumed I'd had one quiet hour of coding with it, two small features shipped,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "post"
word_count: 353
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xkhbp4/not_paid_attention_and_haiku_was_shipping_to_the/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Not paid attention and Haiku was shipping to the production

Reddit · Admirable_Rip443 · 2026-10-31

I thought Haiku 5.5 shipped two features for me in an hour. Git says nine commits. I use Claude Code on a side project, a Discord-style chat app with a Go backend, Postgres, a Svelte frontend, Matrix for messaging and LiveKit for calls. I'd been running Haiku 5.5 for a while without really paying attention, and I assumed I'd had one quiet hour of coding with it, two small features shipped, nothing broken. Then I asked Claude Code how many features we'd shipped with that model. Every commit it makes carries a model line, so it counted the ones signed by Haiku 5.5. There were nine, spread over two days. Roughly four were real features and five were fixes or tweaks. The features were secret notes that open once and then delete themselves, now built into the app as a bubble in the sidebar, a single add people picker for calls that works from the call bar, a voice channel menu and a person menu, including ringing people into a server voice channel, an Explore page that shows every public server instead of only listed ones, and better search results with structured data and proper icons. The fixes were call controls running off the screen on narrow layouts, a bug where a call kept ringing in every open browser tab after you answered it in one, a sitemap rule, a verification tag, and removing a side panel I decided I didn't want. As far as I can tell nothing broke in production. Things did go wrong along the way, but they were caught before reaching users. One deploy failed halfway because of a copy error and the old version simply stayed live. A test script got blocked by Cloudflare, and another sent the wrong payload to an API. It also told me plainly when something hadn't been tested, instead of claiming it worked. What surprised me wasn't that Haiku could do the work. It's that I couldn't tell the difference while I was working, and I only found out because I counted. Curious whether anyone else has checked their own history like this.
