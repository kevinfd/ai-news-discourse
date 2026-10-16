---
id: "1b55531ecbd82789"
title: "Opus 5.5 does not follow rules"
url: "https://reddit.com/r/ClaudeAI/comments/1x6t4sm/opus_55_does_not_follow_rules"
link: "https://reddit.com/r/ClaudeAI/comments/1x6t4sm/opus_55_does_not_follow_rules"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-15T18:13:51Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["skynet86"]
language: "en"
summary: "Full disclosure: it's probably a skill issue, and I accept it. I recently switched from OpenAI over to Anthropic, using Claude Code, and I have difficulties with Opus. It knows my rules, it reads them, accepts them and still ignores them. I also did the usual stuff: Trim the rules, fix ambiguities and loopholes etc. Opus told me itself that the rules are fine. Codex followed them stubbornly.…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: []
content_source: "post"
word_count: 424
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x6t4sm/opus_55_does_not_follow_rules/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Opus 5.5 does not follow rules

Reddit · skynet86 · 2026-10-15

Full disclosure: it's probably a skill issue, and I accept it. I recently switched from OpenAI over to Anthropic, using Claude Code, and I have difficulties with Opus. It knows my rules, it reads them, accepts them and still ignores them. I also did the usual stuff: Trim the rules, fix ambiguities and loopholes etc. Opus told me itself that the rules are fine. Codex followed them stubbornly. However, it said that if there is no mechanic that forces it to follow them, it won't. It's a little bit frustrating. How do you guys do that? Move most of the stuff to skills which is getting activated just in time? Its coming from a 20 hours long refactoring session, split up in multiple stages. When it diverged, I corrected it, but those bad habits came up again and again. It told me that those long sessions are harmful, despite the fact that CLAUDE.md gets injected on every compaction? Should I have cleared the session with /clear from time to time? I did not have the incentive to do so, because Codex works differently. New session means - start from scratch unless you have some kind of handover, and Claude always seemed to be consistent except for following the rules. Please help :( Overall I am very happy with Opus, but that issue drives me insane. EDIT: I had a very long discussion with Claude regarding this topic and I gained some insights. First of all, I underestimated how efficient Claude is Context-wise. (I limited it to 550K). At OpenAI's models, the distance between compactions is very narrow, so rules get injected much more frequently. Second, injecting the must rules at the start of each turn is the next thing that I'm going to try. Claude showed me what his summaries contained and how it works, that its attention moves from the start of the context further and further. Comparable with a soccer player - right before you score a goal (commit) you are not going back to the coach and ask "where should I score the goal again?" - the hook would be somebody from the side yelling "shoot in the upper right corner!" Third, I'm going to restructure which rules get injected at which point during development. Lastly, Claude told me that he still had information from hours ago in his summaries, without any context, just information that looked like facts. All in all, my learning is that I'm just not used to how long the context lasts. I'm tainted by OpenAIs inefficiency.
