---
id: "04d33513409aaa04"
title: "No model is better than another its the god damn tools templates are broken & some tools need clean filenames"
url: "https://reddit.com/r/LocalLLaMA/comments/1x6jgtq/no_model_is_better_than_another_its_the_god_damn"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T11:46:05Z"
published_date: "2026-10-15"
collected_at: "2026-10-15T12:06:50Z"
authors: ["bigorangemachine"]
language: "en"
summary: "I've been trying to figure out a few things with local models. When you talk to them they get similar answers than a lot of the top models. When I do coding and I give the same access to the files as each other... they get roughly the same answers which you would expect asking two different people. So why is it people are getting tribal about models? Well it depends what you harness you are…"
tags: ["r/LocalLLaMA"]
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 596
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x6jgtq/no_model_is_better_than_another_its_the_god_damn/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# No model is better than another its the god damn tools templates are broken & some tools need clean filenames

Reddit · bigorangemachine · 2026-10-15

I've been trying to figure out a few things with local models. When you talk to them they get similar answers than a lot of the top models. When I do coding and I give the same access to the files as each other... they get roughly the same answers which you would expect asking two different people. So why is it people are getting tribal about models? Well it depends what you harness you are running with the model. When someone was nice enough to share the hugging face qwen template fixes got me looking into modelfiles and the llama.cpp parameters. My "mission" lately is to answer the question "Why is Gemma4:27b such a bad code assistant and why". In the past I was about to "brow beat" using a preprompt in my IDE to get gemma to write solid code up until the context gets full and it just refuses to use its tools. At first I started feeding documentation links and got better results. Then for a laugh I thought I would try qwen and got... oddly similar results including broken tool calls This wasn't measurable so I decided I would hook up an MCP host and use ML-Flow. I setup modelfiles with 4 variants per model with different temperatures, paramaters and system prompts and tune to the models specific settings for programming (low temp low repeat penalty) So I started with the large parameter models (had to download qwen3) and both seemed to be getting the job done with the same system prompt & one-shot user prompt. This is where having the numbers tracked became super useful. I saw my old gemma4 model was getting huge amount of failing tool calls.... but the new model had zero tool failures. I pulled the new gemma4 in and got a 15 gig update. I ran it again and it worked! So I thought I would baseline gemma e2b... and now... the tool failures are RAMPANT. I plan to look into it more but I believe the same issue exists that the model by default is configured for another harness. But the funny thing is that the task was still delivering similar results because it would just find a way around broken tools. Then with that the qwen2.5 doesn't have the same love & care as qwen3 because the tool calls have a high level of failures. This is leading me now to see if I can get some baseline runs without tool errors so the comparisons are fair. What was also wild was due to the tool failures the one agent tried to read a transcript of some random youtube video in desperation. What also broke (some) tools was that I used brackets in the file names. For some tools & models this was a problem. So I strongly recommend that when you are setting up these testing loops that make small changes to your runners; I had only made that change and the preprompt and initially I thought the pre-prompt changed the results The biggest take away for me is that Models by default are tuned for different things Models might have broken tool templates Models might have tool templates for one harness or another out of the box This is open source so this is the experience of rolling your own vs SaaS (Frontier models) Filenames can break tools So I write this to say that when people are suggesting one open model is better than another needs a really detailed look because it might also be the harness or the task.
