---
id: "f87b0ccd6d28bd1c"
title: "When a deadline is missed, how do you rebuild the closing timeline"
url: "https://reddit.com/r/artificial/comments/1xtvnd2/when_a_deadline_is_missed_how_do_you_rebuild_the"
link: "https://reddit.com/r/artificial/comments/1xtvnd2/when_a_deadline_is_missed_how_do_you_rebuild_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T22:25:50Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["daverinderknecht"]
language: "en"
summary: "Every closing carries a dozen-plus deadlines (inspection, financing, appraisal, earnest money, closing itself), and a lot of files get tracked in a spreadsheet that gets updated after showings. That system works right up until an addendum moves a date or a contingency gets extended, and then the spreadsheet and the executed contract disagree without anyone noticing. So I'm curious how people…"
tags: ["r/artificial"]
orgs: []
topics: []
content_source: "post"
word_count: 212
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xtvnd2/when_a_deadline_is_missed_how_do_you_rebuild_the/"
score: null
comments: null
community: "r/artificial"
---

# When a deadline is missed, how do you rebuild the closing timeline

Reddit · daverinderknecht · 2026-11-11

Every closing carries a dozen-plus deadlines (inspection, financing, appraisal, earnest money, closing itself), and a lot of files get tracked in a spreadsheet that gets updated after showings. That system works right up until an addendum moves a date or a contingency gets extended, and then the spreadsheet and the executed contract disagree without anyone noticing. So I'm curious how people actually rebuild the timeline after a miss. Do you go back to the contract plus every addendum and re-derive each date from scratch, or is there a saner triage order: which dates are hard legal deadlines vs. negotiable, what has to be re-papered vs. just re-communicated to the lender and title? The AI side is what I keep chewing on. Pulling dates out of a clean purchase agreement PDF is one problem. Addenda and state-specific forms are a different one, because the amendment silently supersedes earlier terms, and a naive extraction pass will happily hand you a timeline that's already stale. I think that supersession problem is where most document-extraction demos quietly stop being useful, and I haven't seen a clean answer for it. Has anyone here dealt with the reconciliation step, human or automated? Specifically, how do you decide which document wins when three of them touch the same date?
