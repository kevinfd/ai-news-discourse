---
id: "86109c7724bd26ab"
title: "Getting through the app review process & how we did it for our job search plugin."
url: "https://reddit.com/r/ChatGPT/comments/1xdmf1s/getting_through_the_app_review_process_how_we_did"
link: "https://reddit.com/r/ChatGPT/comments/1xdmf1s/getting_through_the_app_review_process_how_we_did"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T18:44:15Z"
published_date: "2026-10-23"
collected_at: "2026-10-24T12:05:48Z"
authors: ["Cojj25"]
language: "en"
summary: "Total review time: About 2 weeks Back and forth with OpenAI: 2 times We built Dreamwork, a job search plugin in the ChatGPT directory. Here are a few things that might be useful for you as you submit: 1. Have your agent read the plugin rule line by line. This week a minor update got 23 of our 69 tools blocked. To be fair, the fules exist to protect us from sketchy plugins so I'm not mad, but a…"
tags: ["r/ChatGPT"]
orgs: ["OpenAI", "Anthropic"]
topics: ["jobs & society", "products & launches", "agents & coding", "search & media"]
content_source: "post"
word_count: 579
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1xdmf1s/getting_through_the_app_review_process_how_we_did/"
score: null
comments: null
community: "r/ChatGPT"
---

# Getting through the app review process & how we did it for our job search plugin.

Reddit · Cojj25 · 2026-10-23

Total review time: About 2 weeks Back and forth with OpenAI: 2 times We built Dreamwork, a job search plugin in the ChatGPT directory. Here are a few things that might be useful for you as you submit: 1. Have your agent read the plugin rule line by line. This week a minor update got 23 of our 69 tools blocked. To be fair, the fules exist to protect us from sketchy plugins so I'm not mad, but a few rules are stricter than you'd think. Watch out for the "Destructive” flag, which applies to any action the user can't cleanly take back. Every tool in a ChatGPT plugin has to declare three things: whether it only reads, whether it reaches the open web, and whether it’s destructive. OpenAI counts deleting, overwriting, cancelling, revoking access, and any send or transaction that can’t be reversed. Only a purely additive write, one that creates something new and changes nothing else, gets to say no. Having an undo button doesn’t change the answer. Examples for us: Rewriting your cover letter is destructive, even though there’s an undo. Hiding a job you don’t want is destructive. Even saving a job is, because saving can start writing your materials in the background, and that uses part of your daily allowance. Submitting an application is the most destructive thing we do; it goes to a real employer under your name, and once it’s sent it’s sent. ChatGPT reads those labels before it calls a tool, and OpenAI requires a human yes before anything irreversible. So when you tell our agent to apply, the first call sends nothing. It comes back with a summary of what’s about to go out, and the application only leaves after you confirm. Replying to a recruiter works the same way. 2. No selling. A plugin can sell physical goods. It can’t sell subscriptions, credits or digital content, show you plans, or link you to checkout . This is different from Claude! It can tell you a feature isn’t on your plan, and that’s about it. We took checkout out of the ChatGPT version entirely, so it's all free messaging. The hard part was our error messages - encouraging upgrade to pro was sitting in refusals we never thought of as copy. In ChatGPT every one of those now says the same thing: your plan doesn’t include this or you’ve hit its limit, nothing was purchased, and nothing changed. The flip side is that a plugin can’t give ChatGPT users a worse version than its own site, or charge them more. Our ChatGPT version has every tool the Claude one has except checkout. 3. There's less data in both directions. Plugins can’t ask for your passwords, SSN, card numbers or health information (we don't want any of this, to be clear). Tools can’t request your whole chat history, only what the task needs. Our preferences tool takes the one sentence you said (“remote only, no crypto”) and not the conversation around it. Responses get trimmed too; ours strip internal IDs, contact details and screening answers before anything goes back to ChatGPT. 4. Approval isn’t a one-time thing. OpenAI rescans every update. Ours had 23 tools that we changed from destructive to not during a cleanup on our side. They actually paused our connector after the next daily scan. We eventually flipped them back and everything was live again the same day. Hopefully this is helpful to anyone else building a connector!
