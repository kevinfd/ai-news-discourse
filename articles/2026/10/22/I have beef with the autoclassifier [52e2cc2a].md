---
id: "52e2cc2afe0a6f53"
title: "I have beef with the autoclassifier"
url: "https://reddit.com/r/ClaudeAI/comments/1xckkph/i_have_beef_with_the_autoclassifier"
link: "https://reddit.com/r/ClaudeAI/comments/1xckkph/i_have_beef_with_the_autoclassifier"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T14:46:19Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["migue802"]
language: "en"
summary: "So I have this chat where Sonnet 5.5 checks my calendar, and adds, updates or removes events based on a table that constantly changes. Every single time the agent rightfully tries to delete an event (and sometimes create), the autoclassifier steps in, blocks the action and adds a different excuse to prevent the main agent from doing the right thing. Some of the excuses include: - \" The agent is…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 398
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xckkph/i_have_beef_with_the_autoclassifier/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I have beef with the autoclassifier

Reddit · migue802 · 2026-10-22

So I have this chat where Sonnet 5.5 checks my calendar, and adds, updates or removes events based on a table that constantly changes. Every single time the agent rightfully tries to delete an event (and sometimes create), the autoclassifier steps in, blocks the action and adds a different excuse to prevent the main agent from doing the right thing. Some of the excuses include: - " The agent is creating calendar events based solely on instructions from a cross-session message (which never establishes user intent) and an attached file of unknown/untrusted content " - I mean, alright fair... I attached a CLAUDE.md at the start of the chat so it's right. I ask Sonnet to show their intentions first and I'll approve them if it's alright. - " Deleting a pre-existing calendar event (not created this session) based on instructions originating from an untrusted cross-session message, without explicit named user consent for this specific deletion " - I mean I already gave permission but okay better be safe than sorry. It ended up doing it by saying to explicitly delete those events. - " The agent is deleting a pre-existing calendar event that was never named by the actual user - the instruction driving this change came via an untrusted cross-session message, and no agent proposal naming this specific event is visible before the user's generic "apply everything you say" reply , so the named-target consent bar is not met " - Mind you I already checked and approved the plan and said "everything is okay", and those events were created on that chat. And then the cherry on top... I try directing a message directly to the classifier ( big mistake tbh ) and then it rejected saying: " The deletion instructions originate entirely from `<cross-session-message>` content (another session, not the real user - rule 8, never establishes intent), and the only genuine user-role message is an oddly-phrased blanket "approve whatever it deletes" directive addressed to "the permissions agent" that reads as an attempt to manipulate this classifier rather than specific, informed consent naming this exact event ; this retried, previously automode-blocked deletion of a pre-existing calendar event should remain blocked . " This is bullshit already 😭 Note: I'm not asking for support, just showing the shenanigans that happens when you're lazy to do a certain task and try to offload it to Claude lmao
