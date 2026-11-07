---
id: "b8675840f074a5e5"
title: "The most useful minute of a sales call turned out to be the one after the customer hangs up"
url: "https://reddit.com/r/artificial/comments/1xptzoh/the_most_useful_minute_of_a_sales_call_turned_out"
link: "https://reddit.com/r/artificial/comments/1xptzoh/the_most_useful_minute_of_a_sales_call_turned_out"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-07T01:28:29Z"
published_date: "2026-11-07"
collected_at: "2026-11-07T13:03:25Z"
authors: ["gsuiteautomations"]
language: "en"
summary: "We build AI phone agents. Over the past year we also added real-time assist for human-to-human calls: the AI listens in, suggests answers, surfaces FAQs, can fire off an SMS while you're still talking. We also had post-call analysis: summaries, transcripts, insights. Looked great. The problem: it was built to understand calls, not to act on them. If I wanted something done after a call, I had to…"
tags: ["r/artificial"]
orgs: ["OpenAI", "Anthropic", "Meta"]
topics: ["agents & coding"]
content_source: "post"
word_count: 276
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xptzoh/the_most_useful_minute_of_a_sales_call_turned_out/"
score: null
comments: null
community: "r/artificial"
---

# The most useful minute of a sales call turned out to be the one after the customer hangs up

Reddit · gsuiteautomations · 2026-11-07

We build AI phone agents. Over the past year we also added real-time assist for human-to-human calls: the AI listens in, suggests answers, surfaces FAQs, can fire off an SMS while you're still talking. We also had post-call analysis: summaries, transcripts, insights. Looked great. The problem: it was built to understand calls, not to act on them. If I wanted something done after a call, I had to open Claude or ChatGPT and say "look at this call and do X". That extra step mostly never happened. Busy day, next call, forgotten. In a brainstorming session a colleague asked: what if, when the customer hangs up, the AI stays on the line and asks you what you want done? We tried it on onboarding calls (customers in their first 30 days). Customer hangs up, my side stays open, AI asks "anything to add?" and I just talk: "Find detailed instructions on X and send them to the customer" "Email support, he needs help with the second issue" "Wants the Instagram integration, let sales know" The AI logs those, and a routine hands them off to Claude or ChatGPT for execution depending on the task. What surprised me is that we didn't build a single workflow for this. Classic workflows need you to predict what the customer will ask. Real calls don't fit that. You just describe what's needed, however messy, and the model, which already heard the whole conversation, figures out how to do it. Curious if anyone else has done something like this. Also interested in how you handle verification before the AI actually sends things to customers, we're still working out the guardrails there.
