---
id: "9e3ea5cfb0d6a5e2"
title: "I tried to make Opus 5.5 cheaper with a cheap coding subagent, but It got worse and more expensive"
url: "https://reddit.com/r/ClaudeAI/comments/1xn0e12/i_tried_to_make_opus_55_cheaper_with_a_cheap"
link: "https://reddit.com/r/ClaudeAI/comments/1xn0e12/i_tried_to_make_opus_55_cheaper_with_a_cheap"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T18:10:04Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Fabulous_Pollution10"]
language: "en"
summary: "TL;DR: On 12 hard coding tasks, Opus alone solved 81% at $1.20/task. Opus + DeepSeek V4.1 Flash solved 67% at $1.29. I tried 7 team designs (41 setups, ~1,200 runs). None beat Opus alone, and most cost more. Why I did this. Opus is great but expensive. I was looking for one of two things: a team that beats a single model without a big jump in price, or a setup that's much cheaper than Opus and…"
tags: ["r/ClaudeAI"]
orgs: ["DeepSeek", "OpenAI"]
topics: ["jobs & society", "agents & coding", "models & research"]
content_source: "post"
word_count: 430
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xn0e12/i_tried_to_make_opus_55_cheaper_with_a_cheap/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I tried to make Opus 5.5 cheaper with a cheap coding subagent, but It got worse and more expensive

Reddit · Fabulous_Pollution10 · 2026-11-03

TL;DR: On 12 hard coding tasks, Opus alone solved 81% at $1.20/task. Opus + DeepSeek V4.1 Flash solved 67% at $1.29. I tried 7 team designs (41 setups, ~1,200 runs). None beat Opus alone, and most cost more. Why I did this. Opus is great but expensive. I was looking for one of two things: a team that beats a single model without a big jump in price, or a setup that's much cheaper than Opus and almost as good. So I had Opus plan and review while cheaper models wrote the code. The tasks. I used to build small benchmarks from my own agent sessions, but those tasks turned out too easy. This time I picked 12 hard tasks that look like my daily work, from TB4, DeepSWE, SWE-rebench, SWE-bench Pro V2 and Longtail-SWE. Hidden tests decide pass or fail, and every setup ran each task 3 times. I also went through the runs by hand: fixed broken tests or prompts in 9 tasks, and gave zero to "solutions" that just downloaded the real fix from upstream. The chart shows the main setups. The best Opus-led team got 69%. Single cheaper models beat every team: GPT-6.1 Terra got 78% and Sol 75%, both at $0.17/task. A few things stood out: A good plan doesn't save a weak worker. Most of the time the team failed, the worker couldn't solve that task on its own either. Handoffs can break things. In one task, Opus made up a rule that wasn't in the prompt, DeepSeek followed it, and Opus approved the code. The hidden test failed it, even though each model solves this task alone every time. Waiting is expensive. While the worker codes, Opus's prompt cache expires, and Opus pays to rebuild it. That alone cost more than the whole worker. How you ask matters. Telling Opus "your tokens cost 20x more than the worker's" instead of banning it from writing code gave the same score at almost half the price. Cheap models did get better with a reviewer. Having Sol review their code added 8–11 points for about $0.07/task. But it only worked one way: Sol made Opus's solutions better, while Opus reviewing Sol made things worse. It's only 12 tasks, so small differences are noise, and shorter tasks may look different. Next, I'm testing a 1-hour cache for Opus. Full table, every setup with scores, confidence intervals, cost and time per task. https://ibragim.dev/leaderboard-v2/ If you know a setup that should beat Opus alone, tell me how you'd build it. I'll run it and add it to the table.
