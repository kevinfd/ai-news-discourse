---
id: "4c864a00e7b387e7"
title: "Built with Claude Code: an AI that runs on my Apple Watch, with its own hearing and voice running on the Watch"
url: "https://reddit.com/r/ClaudeAI/comments/1xrazjr/built_with_claude_code_an_ai_that_runs_on_my"
link: "https://reddit.com/r/ClaudeAI/comments/1xrazjr/built_with_claude_code_an_ai_that_runs_on_my"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-08T22:26:43Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["breagz"]
language: "en"
summary: "Dooder is an AI that lives on the Apple Watch, and I built it with Claude Code as the lead developer. In the video it finds my next free weekend from my calendar, searches flights and Airbnbs for those dates, then saves the plan to Notion. It asks before changing anything. Hearing and a voice, on the Watch No phone and no server needed once it's set up, so both run on the Watch itself: -…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Apple", "Nvidia", "OpenAI"]
topics: ["models & research", "agents & coding", "chips & infrastructure"]
content_source: "post"
word_count: 282
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xrazjr/built_with_claude_code_an_ai_that_runs_on_my/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Built with Claude Code: an AI that runs on my Apple Watch, with its own hearing and voice running on the Watch

Reddit · breagz · 2026-11-08

Dooder is an AI that lives on the Apple Watch, and I built it with Claude Code as the lead developer. In the video it finds my next free weekend from my calendar, searches flights and Airbnbs for those dates, then saves the plan to Notion. It asks before changing anything. Hearing and a voice, on the Watch No phone and no server needed once it's set up, so both run on the Watch itself: - Hearing: NVIDIA's Parakeet speech recognition model (110M) runs on the Watch - Voice: an 8M-parameter neural voice (Paradee, a Kokoro relative) speaks every reply on the Watch - Pronunciation: a 150,000-word dictionary compiled on the iPhone into a compact file the Watch reads in place, plus a small model that works out words it's never seen - The whole voice is about 25 MB. The iPhone downloads it and hands it to the Watch Claude in the app - Add your own Claude API key and Dooder uses it straight from the Watch, over cellular. No Dooder server in between (ChatGPT sign-in works too) - Connects to apps through MCP, from the official registry or by URL What worked well building it with Claude Code - Design first, agree it, then build - Real tester screenshots as bug reports. Most fixes went out in a TestFlight build the same day - Evals against real models caught tool-choice regressions before testers did Free on TestFlight (just opened 100 more spots): https://testflight.apple.com/join/c42uMmzU More at dooder.ai Full disclosure: I trimmed the bits where Dooder is thinking to keep the video short. Nothing's sped up and responses usually take 5-10 secs. It's still early days, so feedback is very appreciated.
