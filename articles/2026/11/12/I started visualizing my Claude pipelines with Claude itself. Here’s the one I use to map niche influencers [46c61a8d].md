---
id: "46c61a8d89f936be"
title: "I started visualizing my Claude pipelines with Claude itself. Here’s the one I use to map niche influencers"
url: "https://reddit.com/r/ClaudeAI/comments/1xucruc/i_started_visualizing_my_claude_pipelines_with"
link: "https://reddit.com/r/ClaudeAI/comments/1xucruc/i_started_visualizing_my_claude_pipelines_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T13:29:10Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["BogdanK_seranking"]
language: "en"
summary: "So I run a pipeline that helps me analyze niche influencers across different markets and figure out how their expertise actually shows up in public: what LLMs say about them, what Google says, and whether those two stories match. A recent post in this sub got me thinking... Someone visualized their agent workflow and I realized I had no clear picture of what my own pipelines do on the backend,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google", "OpenAI", "Perplexity"]
topics: ["agents & coding"]
content_source: "post"
word_count: 704
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xucruc/i_started_visualizing_my_claude_pipelines_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I started visualizing my Claude pipelines with Claude itself. Here’s the one I use to map niche influencers

Reddit · BogdanK_seranking · 2026-11-12

So I run a pipeline that helps me analyze niche influencers across different markets and figure out how their expertise actually shows up in public: what LLMs say about them, what Google says, and whether those two stories match. A recent post in this sub got me thinking... Someone visualized their agent workflow and I realized I had no clear picture of what my own pipelines do on the backend, or what they cost me per run. So now I ask Claude to visualize every pipeline I build with Claude. Yeah, I know... it’s Claude explaining Claude. So, here’s the animated breakdown, and below is what happens at each step and why it’s there. Step 0. Trigger (n8n) A cron schedule or webhook kicks off the run. n8n is the orchestrator for everything that follows. Why: I don’t want to remember to run it. It just runs every weekday morning and logs each execution, so when something breaks I know which run did it. Step 1. Pick a name (Notion) An n8n Notion node grabs the next row marked “Queued” from my influencer database. Name, niche, known handles. It immediately flips the status to “In progress” so a parallel run can’t grab the same person. Why: Notion is where my research queue already lives. Dedupe against past runs saves me from paying twice for the same person. Step 2. Build the prompt set (Claude) Claude turns one name plus a niche into a set of prompts: "who is X", "top experts in [niche]", comparison queries. Output is strict JSON. Why: this is the step ppl skip, and it’s the one that matters most. Asking "who is X" alone tells you almost nothing. Asking "who are the best voices on [topic]" tells you whether LLMs actually think of this person when they’re NOT named in the question. That’s the real measure of influence. Step 3. Run the name everywhere (parallel) Two branches run at the same time: SE Visible runs the prompts across ChatGPT, Perplexity, Gemini and AI Overviews and returns mentions, positions and the sources each answer cites Firecrawl searches Google and scrapes the top results: bios, interviews, podcasts, profiles n8n’s merge node waits for both. Failures go to a Slack alert instead of silently dying. Why: LLM answers and web results are two different realities. Someone can rank great on Google and be invisible in ChatGPT, or the reverse. You need both to see the gap. Step 4. Public-figure portrait (Claude) Claude merges both streams into one portrait: identity, expertise, reach, signature work, and how LLMs describe the person compared to what the web says. Contradictions get flagged, not smoothed over. Why: the flags are the interesting part. "ChatGPT thinks she’s a PPC expert, every interview is about growth hacking" is exactly the kind of thing I want to know before reaching out. Step 5. Rank niche influencers (Claude) Every other name that showed up next to our person (in LLM answers, in cited sources, in search results) gets extracted and scored by LLM mentions, Google presence and audience reach. Why: you start with one person and end with a map of the whole niche. This is honestly the most useful output. Half the names on my lists came from co-mentions I would’ve never found manually. Step 6. Card delivered (Notion + Slack) n8n writes the portrait and the ranked influencer card back into the Notion row, sets status to "Done", posts a summary in Slack and queues the next name. Why: results land where the rest of my team already works. Nobody has to open n8n. What visualizing it actually taught me The parallel step takes the longest, and grabbing LLM results are async, so polling is a real part of the runtime Claude gets called three times per run (prompts, portrait, ranking), so that’s where most of the token spend sits Cost per run: roughly [X] in Claude tokens + [Y] Firecrawl credits + [Z] SE Visible prompts. Per niche of [N] people: [total] Caveats, because there are always caveats: LLM answers change between runs, so one snapshot isn’t gospel. Co-mention scoring overrates people who are loud on a single platform. And niche markets with little English content give thinner results.
