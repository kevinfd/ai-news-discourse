---
id: "52b929606619a140"
title: "Made the history podcast I wanted to exist: ask it anything, interrupt it, quiz yourself at the end"
url: "https://reddit.com/r/ClaudeAI/comments/1xoivyb/made_the_history_podcast_i_wanted_to_exist_ask_it"
link: "https://reddit.com/r/ClaudeAI/comments/1xoivyb/made_the_history_podcast_i_wanted_to_exist_ask_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-05T13:39:39Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["Goldenchild123"]
language: "en"
summary: "History is something I’m quite passionate about and at work I have experience with software development and LLMs. So I thought how can I bring these things together and built something that I would actually use. This is the results of many months of hard work! You type any topic, moment or person. About a minute later, two hosts are telling you the story with artwork that follows along. You can…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Google"]
topics: ["models & research", "jobs & society"]
content_source: "post"
word_count: 388
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xoivyb/made_the_history_podcast_i_wanted_to_exist_ask_it/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Made the history podcast I wanted to exist: ask it anything, interrupt it, quiz yourself at the end

Reddit · Goldenchild123 · 2026-11-05

History is something I’m quite passionate about and at work I have experience with software development and LLMs. So I thought how can I bring these things together and built something that I would actually use. This is the results of many months of hard work! You type any topic, moment or person. About a minute later, two hosts are telling you the story with artwork that follows along. You can interrupt mid-episode with a question; they answer and pick the story back up. They also remember what you’ve listened to in the past and can refer to it. At the end there’s also a optional quiz to test what you learned! Quite a lot of emphasis was put into the research part. It searches the web and gathers notes on the topic, prioritizing reference-grade sources (encyclopedias, museums, archives, academic pages) over blogs and also searches in the language of the place or person, so a story about Japan or Peru isn’t told only from English sources. When the sources disagree, which in history is constantly, the hosts say so instead of quietly picking a side. Every episode links the pages it used and tags the subtitles. Under the hood it’s not one model. A single episode is about a dozen calls, each pinned to the model that won its bake-off: research, writing, artwork, voices, sources, quiz, etc... Finding the right balance between quality, speed and cost was where a lot of the work went. The Claude part: Claude Code did roughly 80% of the development, the front end came out of Claude Design. I steer the idea and the design, it codes, I review, and we go back and forth even on small features. Review is where the time goes For the models inside the app, I ran bake-offs across GPT, Claude and Gemini for each job, and a few things surprised me: Opus 4.8 was the clear winner as the writer. Better dialogue, better pacing, and it handled “the sources disagree here” honestly instead of picking a side. Opus 5.5, oddly, wrote more generic scripts in my tests, which surprised me For smaller tasks I found Gemini was the best quality/speed/cost model. Mainly looking for feedback on the idea and how to make it better! Happy to answer any questions! You can try it here: historai.ca
