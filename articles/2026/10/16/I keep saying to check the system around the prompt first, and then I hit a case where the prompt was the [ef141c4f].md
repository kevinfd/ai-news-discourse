---
id: "ef141c4f8c87e836"
title: "I keep saying to check the system around the prompt first, and then I hit a case where the prompt was the problem"
url: "https://reddit.com/r/artificial/comments/1x7odac/i_keep_saying_to_check_the_system_around_the"
link: "https://reddit.com/r/artificial/comments/1x7odac/i_keep_saying_to_check_the_system_around_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-16T18:41:51Z"
published_date: "2026-10-16"
collected_at: "2026-10-17T12:05:45Z"
authors: ["ClickOk5811"]
language: "en"
summary: "I've been arguing for a while that when an AI feature starts misbehaving, the prompt is usually the last place to look. Check the input schema, check what changed upstream, check the tool descriptions, check the assembled context. The prompt is the visible layer, and visible layers attract attention they don't always deserve. Then I ran into a case where none of that applied. Same input, same…"
tags: ["r/artificial"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 263
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1x7odac/i_keep_saying_to_check_the_system_around_the/"
score: null
comments: null
community: "r/artificial"
---

# I keep saying to check the system around the prompt first, and then I hit a case where the prompt was the problem

Reddit · ClickOk5811 · 2026-10-16

I've been arguing for a while that when an AI feature starts misbehaving, the prompt is usually the last place to look. Check the input schema, check what changed upstream, check the tool descriptions, check the assembled context. The prompt is the visible layer, and visible layers attract attention they don't always deserve. Then I ran into a case where none of that applied. Same input, same tools, same context, same model version. The prompt had been written six weeks earlier and hadn't been touched. It was still the cause. Not because it degraded, but because it had never been precise about one edge case, and the edge case started showing up more often as usage grew. The prompt was always wrong. The volume just caught up to it. So the "check the surroundings first" heuristic failed here. What it gave me was a clean baseline: I could rule out the environment quickly and know the prompt was the remaining variable. That's still useful, but it's a different kind of useful than I've been describing. It's not "the environment is usually the problem." It's "checking the environment is usually cheap and tells you where the problem isn't." I don't have a tidy rule for when the prompt is the real cause versus when it's a symptom of something around it. The distinction I'm working with now is whether the failure correlates with a change (look around the prompt) or with volume (look at the prompt). It's not a clean heuristic and I'm not sure it holds outside the narrow setup I work in.
