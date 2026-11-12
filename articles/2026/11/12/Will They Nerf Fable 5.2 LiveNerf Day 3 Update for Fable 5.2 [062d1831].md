---
id: "062d18315c328fb7"
title: "Will They Nerf Fable 5.2? LiveNerf Day 3 Update for Fable 5.2"
url: "https://reddit.com/r/ClaudeAI/comments/1xu01lm/will_they_nerf_fable_52_livenerf_day_3_update_for"
link: "https://reddit.com/r/ClaudeAI/comments/1xu01lm/will_they_nerf_fable_52_livenerf_day_3_update_for"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T01:42:34Z"
published_date: "2026-11-12"
collected_at: "2026-11-12T13:04:19Z"
authors: ["TheOnlyVibemaster"]
language: "en"
summary: "I’ve been running LiveNerf since Opus 5.5 launched on September 24. The idea is pretty simple: run the same questions every day and see if Claude actually gets worse over time. If you’re interested in tracking performance of Opus 5.5 and Fable 5.2, here’s the repo: https://github.com/ninjahawk/livenerf Every day, Opus answers the same frozen set of 78 questions from GPQA Diamond, MMLU-Pro,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "post"
word_count: 610
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xu01lm/will_they_nerf_fable_52_livenerf_day_3_update_for/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Will They Nerf Fable 5.2? LiveNerf Day 3 Update for Fable 5.2

Reddit · TheOnlyVibemaster · 2026-11-12

I’ve been running LiveNerf since Opus 5.5 launched on September 24. The idea is pretty simple: run the same questions every day and see if Claude actually gets worse over time. If you’re interested in tracking performance of Opus 5.5 and Fable 5.2, here’s the repo: https://github.com/ninjahawk/livenerf Every day, Opus answers the same frozen set of 78 questions from GPQA Diamond, MMLU-Pro, competition math, and AIME. Everything runs through headless Claude Code on one Max subscription. The study is pre-registered, results are append-only, and grading is exact. The Opus results so far: Launch baseline (first 10 days): 58.4% Today’s score: 60.3% Nerf detected: Not a statistically meaningful general one within the pre-registered parameters. There’s been plenty of daily variation, but nothing that meets the pre-registered threshold for a sustained decline. I’ve also added Fable 5.2 tracking. Some people in the Discord wanted the new model included, so I started running Fable on its launch day, November 9, using the same 78 questions, prompts, and graders. Results so far: Nov 9: 63/78 (80.8%) Nov 10: 69/78 (88.5%) Nov 11: 66/78 (84.6%) Every answer was served by Fable 5.2, with zero errors. That’s roughly 25 percentage points above Opus on this panel. Fable is the orange line on the graph. Nothing about the original Opus study has changed. One important qualification: these questions were originally selected to be difficult for Opus, so Fable scores pretty close to the ceiling. Also, Fable requires a newer Claude Code version (2.1.319 vs. 2.1.280). The difference between the lines isn’t a clean model-only comparison. A couple of other things I’ve added: Claude Code assigns experiments and feature flags to accounts. LiveNerf now records a SHA-256 fingerprint of those assignments before and after each run. Only the hash is published, not the actual settings. In my personal harness, I’ve detected 18 experiments running on my account. I’ll probably share those at some point when I’ve figured out what each does. This means if performance changes, I can check whether the experiment assignments changed around the same time. So far they’ve been stable across every Fable run. I’m also tracking output and thinking tokens per question, since changes in effort might show up before changes in accuracy and it’s been shown that some of the experiments do affect effort and token count. As for detecting a Fable nerf: The baseline is its first 10 days, ending November 18. The decision rule requires two consecutive 10-day windows showing a decline at 99% confidence, with a minimum 3-point drop. The first possible verdict is December 8. Based on the validation work, the study should be able to detect a sustained decline of around 7 points. Before launch, I tested the setup with identical runs, lower-effort settings, and a blind substitution of Opus for Fable. Identical runs were statistically consistent, reducing effort cut output tokens by 42% and was detectable, and the model substitution was clearly detected. Refusals, errors, and reroutes are also reported both excluded and counted as incorrect. Obviously, this is still one account’s experience, not a measurement of every Claude user. And three days isn’t enough to say anything about Fable’s long-term stability. But that’s why I’m collecting the data instead of trying to draw conclusions from individual bad responses. There’s also a Sponsor button on the repo if anyone wants to help cover the subscription and API costs of keeping this running. I’m very grateful for the community we’ve built around this, I never would’ve expected us to be at nearly 2,000 stars after only a few months and have a discord community of over 250 members. Thankful to you all. See you on the next update.
