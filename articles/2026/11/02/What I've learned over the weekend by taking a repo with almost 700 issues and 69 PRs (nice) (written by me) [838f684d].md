---
id: "838f684d426c3cac"
title: "What I've learned over the weekend by taking a repo with almost 700 issues and 69 PRs (nice) (written by me)"
url: "https://reddit.com/r/ClaudeAI/comments/1xlmoie/what_ive_learned_over_the_weekend_by_taking_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xlmoie/what_ive_learned_over_the_weekend_by_taking_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-02T03:28:12Z"
published_date: "2026-11-02"
collected_at: "2026-11-02T13:05:12Z"
authors: ["InadequateUsername"]
language: "en"
summary: "Users don't know what the fuck they actually want or what they're asking for. If you fork someone's repo and tell Claude just \"fix the bugs\" and \"implement the asks with a bounty\". You will waste time and tokens with scope creep and debugging ancient parts of the code base. Deciding when to say \"no\" is really important. And if you're a maintainer, curating your issues list is important, saying…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Amazon"]
topics: ["search & media"]
content_source: "post"
word_count: 335
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xlmoie/what_ive_learned_over_the_weekend_by_taking_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# What I've learned over the weekend by taking a repo with almost 700 issues and 69 PRs (nice) (written by me)

Reddit · InadequateUsername · 2026-11-02

Users don't know what the fuck they actually want or what they're asking for. If you fork someone's repo and tell Claude just "fix the bugs" and "implement the asks with a bounty". You will waste time and tokens with scope creep and debugging ancient parts of the code base. Deciding when to say "no" is really important. And if you're a maintainer, curating your issues list is important, saying "yeah I'll get to this" then leaving it opened for 4 years isn't really doing any favors. No, local AI will not be implemented within the project to accomplish a singular task, instead run it external from the project and import the output. If you need postgresql because SQLite isn't performative enough for your local use since your media collection has become that large and caching isn't the answer, you might have a problem. No, native support for AWS will not be added, it comes with a Docker container, that's already half the work done for you. Why does a Plex equivalent need support for written stories? Use Calibre or another equivalent. The point of a cover image, is that it's a single image that largely represents the media's content, does it really need more than a 1:1 ratio? Having your media library support images in a .zip archive is dumb with little benefit, pictures don't compress well at all. And then supporting a method of exporting your current media library to .zip format? Running CI on a private repo adds up fast, and it's really easy for Claude to say "yeah just add another $10 bro" after blowing away the GitHub pro minutes in a day, and $10 USD is like $15 cad. Anyways my work is 2x Claude Pro accounts, Opus Medium, and Codex Sol 6.1. One Claude assigns work to Codex and the other Claude session, while working on its own stuff. Every PR undergoes a code review by a different session and the outcome documented as a comment on the pr.
