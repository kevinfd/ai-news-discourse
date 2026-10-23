---
id: "d5590e9d18825ecb"
title: "Anthropic appears to sneak in a legal loophole in Claude Code to train on \"feedback\" even with training off as in Claude Code's source theres a legal term that counts every \"Allow edit\" you press as feedback."
url: "https://reddit.com/r/ClaudeAI/comments/1xd5ruf/anthropic_appears_to_sneak_in_a_legal_loophole_in"
link: "https://reddit.com/r/ClaudeAI/comments/1xd5ruf/anthropic_appears_to_sneak_in_a_legal_loophole_in"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T05:51:20Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["HearMeOut-13"]
language: "en"
summary: "I'm on a Max plan with \"help improve Claude\" turned off. Every Claude Code binary I have installed (2.1.283 to 2.1.309) starts with this comment: // Claude Code is a Beta product per Anthropic's Commercial Terms of Service. // By using Claude Code, you agree that all code acceptance or rejection decisions you make, // and the associated conversations in context, constitute Feedback under…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research"]
content_source: "post"
word_count: 166
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xd5ruf/anthropic_appears_to_sneak_in_a_legal_loophole_in/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Anthropic appears to sneak in a legal loophole in Claude Code to train on "feedback" even with training off as in Claude Code's source theres a legal term that counts every "Allow edit" you press as feedback.

Reddit · HearMeOut-13 · 2026-10-23

I'm on a Max plan with "help improve Claude" turned off. Every Claude Code binary I have installed (2.1.283 to 2.1.309) starts with this comment: // Claude Code is a Beta product per Anthropic's Commercial Terms of Service. // By using Claude Code, you agree that all code acceptance or rejection decisions you make, // and the associated conversations in context, constitute Feedback under Anthropic's Commercial Terms, // and may be used to improve Anthropic's products, including training models. Accepting or rejecting an edit is usually just pressing Enter at a permission prompt. Read literally, that makes a normal session "Feedback" that can be trained on, whatever your privacy setting says. To verify it yourself: strings ~/.local/share/claude/versions/$(claude --version | cut -d' ' -f1) | grep -A3 "constitute Feedback" Does this clause override the consumer training opt-out or not? I contacted Anthropic support about this on 2 September and have had no answer in over a month. Has anyone had a clear answer from Anthropic on this?
