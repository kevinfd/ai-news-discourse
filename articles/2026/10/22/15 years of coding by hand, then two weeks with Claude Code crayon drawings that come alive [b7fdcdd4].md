---
id: "b7fdcdd40daabd47"
title: "15 years of coding by hand, then two weeks with Claude Code: crayon drawings that come alive"
url: "https://reddit.com/r/ClaudeAI/comments/1xcl7r1/15_years_of_coding_by_hand_then_two_weeks_with"
link: "https://reddit.com/r/ClaudeAI/comments/1xcl7r1/15_years_of_coding_by_hand_then_two_weeks_with"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T15:10:37Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["lombarovic"]
language: "en"
summary: "I've been a developer for 15 years, mostly .NET. I built my drawing game Drawize (10M+ players) by hand, the old-school way, with hardly any libraries besides jQuery. For my new project I didn't write the code. Claude Code did, often several agents in parallel, and I acted as the product owner. The first fully working version took two weeks and launched on 12 October. You color a page in the…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "jobs & society"]
content_source: "post"
word_count: 306
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xcl7r1/15_years_of_coding_by_hand_then_two_weeks_with/"
score: null
comments: null
community: "r/ClaudeAI"
---

# 15 years of coding by hand, then two weeks with Claude Code: crayon drawings that come alive

Reddit · lombarovic · 2026-10-22

I've been a developer for 15 years, mostly .NET. I built my drawing game Drawize (10M+ players) by hand, the old-school way, with hardly any libraries besides jQuery. For my new project I didn't write the code. Claude Code did, often several agents in parallel, and I acted as the product owner. The first fully working version took two weeks and launched on 12 October. You color a page in the browser, or print it, color it with real crayons and take one photo, and the drawing comes alive in your colors and walks into a shared world with everyone else's drawings. The photo is my real crayon rooster next to the iPad. What actually made it work: - CLAUDE.md as a constitution. No shortcuts, tests with every change, and ask me only about product, money and taste. Everything technical was theirs to decide and write down. - A decision log. Agents forget between sessions; the repo doesn't. It's now 279 decisions long. - Me reviewing everything by eye. The agents measured motion very well, but most "this looks wrong" moments still came from me watching it move (sliding feet, legs detaching like wooden puppets). - Fixing the input, not the code. When an animal walked badly, we redrew it instead of patching the rig. Numbers after 25 days: 2,515 commits, about 280k lines, about 2,400 tests, 119 animated creatures in 7 worlds, 12 languages. What went wrong: a sign error made every four-legged animal shuffle diagonally. About 2,000 tests missed that real fingers wobble, so a Pixel phone could barely color. And leftover worktrees filled 400 GB of my disk. Full write-up, with how the rigs are generated from flat drawings and how crayon colors are read from a phone photo: https://www.livecoloringbook.com/how-it-was-built Try it (free, no account): https://www.livecoloringbook.com Happy to answer questions about the workflow.
