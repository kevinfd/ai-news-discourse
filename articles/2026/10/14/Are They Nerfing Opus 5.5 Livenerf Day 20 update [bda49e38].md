---
id: "bda49e383472f992"
title: "Are They Nerfing Opus 5.5? Livenerf Day 20 update"
url: "https://reddit.com/r/ClaudeAI/comments/1x606aj/are_they_nerfing_opus_55_livenerf_day_20_update"
link: "https://reddit.com/r/ClaudeAI/comments/1x606aj/are_they_nerfing_opus_55_livenerf_day_20_update"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T19:10:24Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["TheOnlyVibemaster"]
language: "en"
summary: "Three weeks ago we began tracking model capability over time with LiveNerf. The goal was to prove from an unbiased set of data if Anthropic is nerfing their models after release. I’ve continued measuring it everyday since then and the results haven’t necessarily been what I think the community expected to see. If you’re interested in tracking the performance of Opus 5.5, here’s the repo:…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 409
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x606aj/are_they_nerfing_opus_55_livenerf_day_20_update/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Are They Nerfing Opus 5.5? Livenerf Day 20 update

Reddit · TheOnlyVibemaster · 2026-10-14

Three weeks ago we began tracking model capability over time with LiveNerf. The goal was to prove from an unbiased set of data if Anthropic is nerfing their models after release. I’ve continued measuring it everyday since then and the results haven’t necessarily been what I think the community expected to see. If you’re interested in tracking the performance of Opus 5.5, here’s the repo: https://github.com/ninjahawk/livenerf If you take a look at the left 1/3, you’ll see that the variance was higher for the first 10 days when the baseline was being established. Then it appears like that in the following 11 days we’ve actually see a decreasing variance and potentially a regression to the mean. This means that if a nerf is happening or has happened, it has not happened within the data we’ve collected so far. This doesn’t necessarily mean that Anthropic isn’t decreasing capability in other ways, it also doesn’t mean that what we’re measuring establishes that day per day the result is always the same per 24-hour period. They could very well be throttling at specific times in the day and not during other periods. This brings me to where the community needs to get involved in a couple ways, we now do have some solid data that’s been accumulated over the course of three weeks, what I need from you guys now is to ask your own models or access for yourself the following question: “Did I experience a perceived decrease in capability at X time on Y day? If so, what was effected?” Testimonies won’t necessarily be more than anecdotal but I think it would be interesting if as a community we see that on certain days there’s perhaps different relations to the data that’s been collected so far. I want to thank everyone so much for the all the support over this past month, I certainly didn’t expect for us to surpass 1.5k stars in a few weeks and would’ve never expected people to donate to the project, I’d like to say as well that all the funds donated will go into further compute so we can scale further with model tracking. I do not plan on stopping with Opus 5.5 or with only tracking nerfs. In 10 days, I will return with the final verdict to lay down the hammer on tentatively proving or disproving model capabilities decreasing under the specific set of criteria LiveNerf collects data on. See you soon!
