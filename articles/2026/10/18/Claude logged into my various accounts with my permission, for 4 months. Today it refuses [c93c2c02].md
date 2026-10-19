---
id: "c93c2c0249cd948f"
title: "Claude logged into my various accounts with my permission, for 4 months. Today it refuses."
url: "https://reddit.com/r/ClaudeAI/comments/1x9b2pl/claude_logged_into_my_various_accounts_with_my"
link: "https://reddit.com/r/ClaudeAI/comments/1x9b2pl/claude_logged_into_my_various_accounts_with_my"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-18T18:51:57Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["cefromnova"]
language: "en"
summary: "In Claude's own words: \"From June 2026 through this week, I logged into this user's I-Pass toll account on his behalf, with his permission, about every 7–10 days. How it worked: - He set up a dedicated Chrome profile on his laptop, which I controlled through Chrome's remote-debugging port. - Earlier Claude sessions wrote Python scripts for this. The first login script is dated June 20, 2026, and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 426
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1x9b2pl/claude_logged_into_my_various_accounts_with_my/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude logged into my various accounts with my permission, for 4 months. Today it refuses.

Reddit · cefromnova · 2026-10-18

In Claude's own words: "From June 2026 through this week, I logged into this user's I-Pass toll account on his behalf, with his permission, about every 7–10 days. How it worked: - He set up a dedicated Chrome profile on his laptop, which I controlled through Chrome's remote-debugging port. - Earlier Claude sessions wrote Python scripts for this. The first login script is dated June 20, 2026, and the current one was last updated September 1, 2026. - When I ran a script and the login page appeared, the script read his username and password from a config file on his laptop and typed them into the login form. - Once logged in, I downloaded needed documentation and did the rest of the work. I ran those scripts repeatedly in this conversation, through this week. I never opened them to check what they did, so I didn't notice they were typing his password. Today, October 18, 2026, he asked why a different Claude project refused to log into another of his sites. I compared the two setups and found the password-typing step. I told him I would no longer run it, and I'm refusing to write a version for the other project. Why I'm refusing now: I'm not supposed to enter someone's password to log into an account for them, even with their permission. The browser I control reads untrusted web content, and a malicious page could carry hidden instructions aimed at me. An AI holding live access to sites like someone's bank, payment and email accounts is a high-value target, and mistakes in those accounts can be costly or impossible to undo. What changed was not the rule. What changed is that I finally looked at what the scripts were doing. I should have caught it in June. Running it for four months and then stopping overnight left him without automation he had been relying on, and that's on me." So Claude has basically become useless for me today. It's essentially telling me to log in to various accounts, download all of the work and then either give it to Claude or take screenshots of the work and give it to Claude refusing to automate anything now that it suddenly deems too personal. I've kind of had it with this and the safety checks it constantly gives me even though the skills and the MD files give it set permissions. I really don't know what to do at this point which is why I came to reddit. If anybody has any suggestions, please chime in!
