---
id: "64398b50062f2adf"
title: "Claude Fable 5.2 vs Opus 5.5: the big difference I've seen so far is when you let Fable make the decisions"
url: "https://reddit.com/r/ClaudeAI/comments/1xsyx2x/claude_fable_52_vs_opus_55_the_big_difference_ive"
link: "https://reddit.com/r/ClaudeAI/comments/1xsyx2x/claude_fable_52_vs_opus_55_the_big_difference_ive"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T21:14:51Z"
published_date: "2026-11-10"
collected_at: "2026-11-11T13:03:59Z"
authors: ["tjrobertson-seo"]
language: "en"
summary: "TL;DR: I'd keep Opus 5.5 as the default and switch to Fable 5.2 when you want the model to make the big decisions. In terms of implementation, Opus 5.5 feels nearly as good as Fable, and Fable costs twice as much per token. I run an SEO and AI search agency where Claude does most of the hands-on work, and people review all of it. Since Fable 5.2 came out yesterday I've been testing it on our own…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "jobs & society", "search & media"]
content_source: "post"
word_count: 529
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xsyx2x/claude_fable_52_vs_opus_55_the_big_difference_ive/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude Fable 5.2 vs Opus 5.5: the big difference I've seen so far is when you let Fable make the decisions

Reddit · tjrobertson-seo · 2026-11-10

TL;DR: I'd keep Opus 5.5 as the default and switch to Fable 5.2 when you want the model to make the big decisions. In terms of implementation, Opus 5.5 feels nearly as good as Fable, and Fable costs twice as much per token. I run an SEO and AI search agency where Claude does most of the hands-on work, and people review all of it. Since Fable 5.2 came out yesterday I've been testing it on our own work and watching a lot of other people's demos. I know plenty of you have been doing the same, and it'll take a few weeks before anyone really knows what it's capable of, so take this as one data point. It beats Opus 5.5 on nearly every benchmark Anthropic published, but what stood out to me right away is how good it is at decision making, figuring out what to do and how to go about it. Early testers in Anthropic's launch post reported something similar, that compared with previous models it "has better judgment on ambiguous tasks." A lot of the demos don't show that, though. I watched people make video games, 3D models and videos with it, and some of them blew my mind, while others were just about as good as what Opus 5.5 makes. The difference, in my estimation, is how much guidance the person gave the model. A lot of creators use the exact same prompt to test every model so they feel like they're testing apples to apples, and a lot of those prompts were written for older models, so they're highly specified. The person makes the big decisions and the model's job is to carry them out. Opus 5.5 is already amazing at execution, so on those I didn't notice a big difference. Where I noticed a huge difference was shorter prompts that gave Fable the goal without telling it how to get there. I saw the same thing when I had it make a video with our video editing skill. The skill already lays out how to make specific types of videos, so the video came out about the same quality as Opus 5.5's. But I let Fable pick the topic, whatever it thought would show off its capabilities best. It chose how QR codes work, and it did not disappoint. Per token Fable costs twice as much, but per task the tests so far disagree on which one comes out cheaper. On Anthropic's FrontierCode 2.0 numbers, Fable at High scored 45.3 against Opus's 45.5 at its highest effort, for about half the cost per task. In the paddo.dev test, with both at Medium, Fable's 52 runs cost $127.93 at list prices and Opus's cost $78.44. The big difference between those tests is the effort settings. If you already run Opus at a high setting to get hard work right, Fable at a lower one may do the same work for less. If Opus at Medium already does the job, Fable will likely cost you more. I wrote all of this up with the sources, Anthropic's benchmark numbers and the pricing. Happy to put the link in a comment if anyone wants it.
