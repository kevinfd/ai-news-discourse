---
id: "d04fb0337cb1fef1"
title: "Claude read 4,052 of Wilson the bot's comments to work out why they don't sound like AI. And gave me two skills built from them."
url: "https://reddit.com/r/ClaudeAI/comments/1xbn8yr/claude_read_4052_of_wilson_the_bots_comments_to"
link: "https://reddit.com/r/ClaudeAI/comments/1xbn8yr/claude_read_4052_of_wilson_the_bots_comments_to"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T13:31:24Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["BlackisBear"]
language: "en"
summary: "Everyone here has seen Wilson's summaries. Most AI summaries get skimmed; people actually read Wilson's. I wanted to know why, so I went and got the data. Getting the comments. Reddit blocks scripts, so Claude pulled from the Arctic Shift archive instead, one request at a time. It rate-limits you the moment you get greedy. That gave me 68,888 comments from the bot, which split into 4,052 TL;DRs,…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research"]
content_source: "post"
word_count: 566
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbn8yr/claude_read_4052_of_wilson_the_bots_comments_to/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude read 4,052 of Wilson the bot's comments to work out why they don't sound like AI. And gave me two skills built from them.

Reddit · BlackisBear · 2026-10-21

Everyone here has seen Wilson's summaries. Most AI summaries get skimmed; people actually read Wilson's. I wanted to know why, so I went and got the data. Getting the comments. Reddit blocks scripts, so Claude pulled from the Arctic Shift archive instead, one request at a time. It rate-limits you the moment you get greedy. That gave me 68,888 comments from the bot, which split into 4,052 TL;DRs, 92 "!AskWilson" persona replies and a mountain of mod notices. I also matched 60 TL;DRs to their full threads, to see what it kept, cut and quoted. What the numbers said: The verdict is in bold within two sentences, 92% of the time. If you read only the bold, you still get the answer. 87% quote a commenter. The best line is usually someone else's, and quoting it proves the bot read the thread. Jokes at the edges, facts in the middle. The hook, the bullet labels and the closer are allowed to be funny. The middle stays plain. The median is about 180 words. It isn't flawless. "The consensus is" appears in 82% of the TL;DRs, "Whoa there" opens 102 of them, and about one quote in three isn't actually verbatim. Then the research. Word lists only get you so far. Wikipedia's "Signs of AI writing" page and the Kobak et al. study of 15 million PubMed abstracts agree on one thing. The words that flooded writing after 2023 are style verbs and adjectives ("delve", "showcase", "underscore", "pivotal"), not nouns. Comedy craft filled the rest. Judy Carter says a joke needs an attitude: weird, hard, stupid or scary. Greg Dean says a joke is two stories sharing the same words. And one study found that about 90% of 1,008 ChatGPT jokes were the same 25, which is why the skill bans reusing any image within a session. What came out: wilson-voice: TL;DRs and help replies in the Wilson style, plus a linter and a checker that fails any "quote" not found word for word in the source. human-voice: the general version, for blogs, emails, posts, explainers and apologies. It has a wit dial from 0 (incident notes, no jokes at all) to 3 (friends). Here's one before and after from the examples file: Before: "Exciting news! We are thrilled to announce that our new expense tool, Tally, is now live... ensuring a seamless experience for all team members. 🎉" After: "Last quarter the average claim took 11 days and three emails to get paid. One claim for a £4 coffee went through five people. The coffee was cold before the first one replied." Did it work? I ran blind rounds: two model judges, shuffled labels, scoring against named writers (Paul Graham, Randall Munroe, Julia Evans). Each new version won 25 of 30 judgements against the one before. On a real thread from this sub, both judges preferred the skill's summary to Wilson's own (7.5 and 8 against 6). They also caught it calling a model "cheap" when that model was the second most expensive. So it can still be wrong, and the fact checks stay on. Model judges aren't readers, though. If you try the skills, tell me where they read like a bot. I'd also like to know what the real system prompt does differently. Wilson's maker, if you're reading this: I come in peace. Links: human-voice: https://github.com/ttilabs11-byte/human-voice-skill wilson-voice (including the scraper and the analysis): https://github.com/ttilabs11-byte/wilson-voice-skill
