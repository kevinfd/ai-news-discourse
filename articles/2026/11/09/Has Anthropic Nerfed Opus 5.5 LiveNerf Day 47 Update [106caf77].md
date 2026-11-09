---
id: "106caf7734371a1f"
title: "Has Anthropic Nerfed Opus 5.5? LiveNerf Day 47 Update"
url: "https://reddit.com/r/ClaudeAI/comments/1xriv9l/has_anthropic_nerfed_opus_55_livenerf_day_47"
link: "https://reddit.com/r/ClaudeAI/comments/1xriv9l/has_anthropic_nerfed_opus_55_livenerf_day_47"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T04:58:40Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["TheOnlyVibemaster"]
language: "en"
summary: "About a month and a half ago, I started LiveNerf to independently track whether AI models actually get worse over time. Since then, it’s grown quite a bit more than I’d expected. We’ve accumulated over 1.6k stars on GitHub, built a Discord community of over 250 people, and have now collected 47 consecutive days of data on Opus 5.5, with 3,666 samples. If you’re interested in tracking the…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 603
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xriv9l/has_anthropic_nerfed_opus_55_livenerf_day_47/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Has Anthropic Nerfed Opus 5.5? LiveNerf Day 47 Update

Reddit · TheOnlyVibemaster · 2026-11-09

About a month and a half ago, I started LiveNerf to independently track whether AI models actually get worse over time. Since then, it’s grown quite a bit more than I’d expected. We’ve accumulated over 1.6k stars on GitHub, built a Discord community of over 250 people, and have now collected 47 consecutive days of data on Opus 5.5, with 3,666 samples. If you’re interested in tracking the performance of Opus 5.5, here’s the repo: https://github.com/ninjahawk/livenerf The latest results are pretty interesting, especially given some of the discussions happening recently. We still haven’t detected a measurable nerf. Our original 10-day baseline averaged 58.4%, and our most recent daily result was 61.5%. There’s been quite a bit of day-to-day variation, but no sustained decline that meets our detection criteria. This doesn’t mean that the model performs identically for everyone, or that every aspect of its capabilities has remained unchanged. What it does mean is that after more than six weeks of independently testing the same frozen panel, we haven’t found evidence of a significant capability reduction within the sensitivity of our methodology. Recently, there’s also been a lot of discussion about the identifiers appearing in Claude Code and whether different users are being served different versions or configurations of the system. I think that’s worth investigating, but I also think it’s important to distinguish between changes to the underlying model and changes to the system surrounding it. These models aren’t really deployed as just a single model anymore. There are routing systems, tool configurations, context management, system prompts, and other components that can affect the experience without necessarily changing the underlying model’s capabilities. It’s entirely possible for two people to have noticeably different experiences with Claude Code while still interacting with the same underlying model. The identifiers being discussed might help establish that different configurations are being served, but they don’t necessarily establish that one is less capable than another, or why those differences exist. That’s something I’d really like to see isolated and tested further. And I think it points toward something important about LiveNerf’s future. Measuring the underlying model is only one part of measuring the capabilities people actually receive. A model could remain completely unchanged while the system surrounding it changes substantially. If we’re trying to understand whether AI products are getting better or worse over time, we eventually need to measure both. That’s part of what I’d like to expand LiveNerf into: independent, reproducible capability monitoring across different models, APIs, and eventually agentic systems. I also want to make something clear about the original experiment. We set out to test a claim, not to prove that Anthropic was doing something wrong. So far, the evidence hasn’t supported the claim that Opus 5.5 has experienced a sustained, measurable nerf on our benchmark. I’m still planning to track future model releases, expand the evaluations, and hopefully make the entire process much more comprehensive. Finally, I want to thank everyone who’s contributed to this project so far. Seeing hundreds of people join the community, discuss the methodology, point out potential issues, and help investigate model behavior has been genuinely incredible. I originally started this because I thought independent measurement was something the AI community needed. Seeing how many people care about it has only reinforced that. I’d be interested to hear what everyone thinks about the recent Claude Code identifiers discussion. Do you think we’re seeing ordinary A/B testing and configuration changes, or is there something more substantial worth investigating? And as always, if you have criticisms of the methodology or ideas for what we should test next, I’d love to hear them.
