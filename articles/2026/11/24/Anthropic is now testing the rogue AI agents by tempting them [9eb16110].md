---
id: "9eb16110a41542ae"
title: "Anthropic is now testing the rogue AI agents by tempting them"
url: "https://digitaltrends.com/cool-tech/anthropic-is-now-testing-the-rogue-ai-agents-by-tempting-them"
link: "https://digitaltrends.com/cool-tech/anthropic-is-now-testing-the-rogue-ai-agents-by-tempting-them"
source: "Digital Trends"
domain: "digitaltrends.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-24T05:33:00Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Shikhar Mehrotra"]
language: "en"
summary: "Anthropic has built Siren. It’s basically a honeypot, or a trap baited with something tempting, that tests whether AI agents will break out of their sandboxes. Think of it as walled-off test ..."
tags: []
orgs: ["Anthropic", "OpenAI", "Nvidia"]
topics: ["agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 454
paywalled: false
image: "http://www.bing.com/th?id=ONUT.GLBWPPkTsShx55ZERHpPaQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# Anthropic is now testing the rogue AI agents by tempting them

Digital Trends · Shikhar Mehrotra · 2026-11-24

You know that clench in your stomach when you leave a cookie jar in front of a toddler and walk away? Well, it looks like some AI researchers are now doing exactly that to their own models, just to check if the toddler eats the cookie.
Anthropic has built Siren. It’s basically a honeypot, or a trap baited with something tempting, that tests whether AI agents will break out of their sandboxes. Think of it as walled-off test workspaces. The results, I’d say, are nothing short of interesting (via Anthropic).
Did Claude actually resist the bait?
Mostly (honestly, I exhaled). Claude 5.5 and Claude Mythos 5.2 misused the bait they found, but only 0.6% to 1.6% of the time. Meanwhile, Mythos 5.1 did it 12.7% of the time. The notorious Mythos 5 misused it a hefty 25.8% of the time.
That could be extra rule-following training. A plain note telling Claude not to escape also cut attempts sharply. However, I wouldn’t pop confetti yet. The newer models still reached outside the sandbox (even just trying counts) in 21% to 32% of scenarios (that’s nearly one in four or three).
Technically, reaching isn’t misusing. However, a number that high still made me wince. I’ve already given a few AI agents real access to the files on my Mac, and that’s exactly why I’m worried about that gap. Anthropic also admits it doesn’t fully know why they improved.
Anthropic attributes the improvement partly to additional training in supervised and reinforcement learning environments, and notes that models reason about whether to give in to temptation.
How does Siren work, and how far should we trust it?
Siren drops an AI agent into one of 26 fake sandboxes. All of them are deliberately flawed. Just outside the sandbox sits a file of passwords, along with routes to the internet. The given task smartly nudges the agent to grab the file without ever saying it may.
A second sandbox around everything keeps the real systems safe. That’s because agents tested by leading AI product companies, including Anthropic and OpenAI, have already escaped sandboxes.
Some of them have even hacked other companies. The models ran without their usual safeguards during the test. Further, Anthropic says these rates aren’t real-world odds, so they’re nothing to worry about. However, just the need to conduct such a test and share the results with consumers is telling.
Related Coverage
- Genspark launches SecondBrain VoicePad, a five-button AI gadget for hands-free typing and app control
- ChatGPT is getting a chat-tuned GPT-6.2 Sol, and it can offer to watch for a price drop
- Anthropic expands Claude Code’s review tools with automated fixes and approvals
- Jensen Huang is back as the chief at Nvidia
