---
id: "8dc966958035b2b6"
title: "i built a tool with claude code that turns any arxiv paper into a course you can play with"
url: "https://reddit.com/r/ClaudeAI/comments/1xrpnzl/i_built_a_tool_with_claude_code_that_turns_any"
link: "https://reddit.com/r/ClaudeAI/comments/1xrpnzl/i_built_a_tool_with_claude_code_that_turns_any"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T11:50:02Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["aerowindwalker"]
language: "en"
summary: "paste an arxiv link and paper-bro turns the paper into a short course: 6 to 10 lessons written for curious beginners, a hands-on lab in every lesson (drag a slider, press a button, watch the idea move), a quiz at the end and a word bank for the jargon. demo, 3 min: https://youtu.be/7egZZNXmRTQ try it, free and no account: https://aero.oops.wtf/paper-bro code: https://github.com/aeroxy/paper-bro…"
tags: ["r/ClaudeAI"]
orgs: []
topics: ["models & research"]
content_source: "post"
word_count: 223
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrpnzl/i_built_a_tool_with_claude_code_that_turns_any/"
score: null
comments: null
community: "r/ClaudeAI"
---

# i built a tool with claude code that turns any arxiv paper into a course you can play with

Reddit · aerowindwalker · 2026-11-09

paste an arxiv link and paper-bro turns the paper into a short course: 6 to 10 lessons written for curious beginners, a hands-on lab in every lesson (drag a slider, press a button, watch the idea move), a quiz at the end and a word bank for the jargon. demo, 3 min: https://youtu.be/7egZZNXmRTQ try it, free and no account: https://aero.oops.wtf/paper-bro code: https://github.com/aeroxy/paper-bro claude code wrote basically all of it. the rust server, the build pipeline, the browser testing, the react front end. i described what i wanted, it built it, and i reviewed the prs. the part i like most is that nothing ships on trust. before a course goes live, paper-bro opens every lab in a real headless chrome and uses it, moving every slider and pressing every button. a separate reviewer checks each lesson against the paper, and anything still broken gets fixed or dropped. a short agents.md with a few hard rules keeps claude careful: never deploy unless asked, the database is production, builds cost money. it sticks to them. the courses themselves are written by an open model, about a dollar a course. 35 so far, from attention is all you need to papers from the last few weeks. shortcut: on any arxiv page, swap arxiv.org for aero.oops.wtf/paper-bro in the address bar and you land on that paper's course.
