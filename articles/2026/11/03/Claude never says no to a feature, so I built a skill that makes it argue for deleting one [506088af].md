---
id: "506088afb2f58211"
title: "Claude never says no to a feature, so I built a skill that makes it argue for deleting one"
url: "https://reddit.com/r/ClaudeAI/comments/1xmw242/claude_never_says_no_to_a_feature_so_i_built_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xmw242/claude_never_says_no_to_a_feature_so_i_built_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-03T15:32:07Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["haymose"]
language: "en"
summary: "tl;dr: It's a skill that helps you safely delete features and reduce assumptions. Gist link here: https://gist.github.com/amos501/919cc1941fb668dc1781bd4cc9a34fc4 I've been building a personal finance app with Claude Code, mostly by having an idea and asking for it. That works really well. It's also how I ended up with a codebase where the same calculation or could be built four different ways…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "models & research"]
content_source: "post"
word_count: 362
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xmw242/claude_never_says_no_to_a_feature_so_i_built_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude never says no to a feature, so I built a skill that makes it argue for deleting one

Reddit · haymose · 2026-11-03

tl;dr: It's a skill that helps you safely delete features and reduce assumptions. Gist link here: https://gist.github.com/amos501/919cc1941fb668dc1781bd4cc9a34fc4 I've been building a personal finance app with Claude Code, mostly by having an idea and asking for it. That works really well. It's also how I ended up with a codebase where the same calculation or could be built four different ways in different parts of the app. What the skill does /occam takes one GitHub issue and walks Claude through a fixed set of steps. The parts that matter: Reproduce first. Write down the total number of assumptions and design the simplest model Analyze the same five options, every time: keep it delete it keep it but label where the number comes from rebuild with fewest assumptions or something creative Crude scoring. +1 for each user story the option delivers, −1 for each assumption, magic constant, special case, caveat, or alert. A second agent red-teams the pick. It stops before building See the example here https://preview.redd.it/1b6ec0n00fzh1.png?width=1616&format=png&auto=webp&s=71e9f4d566a90a556eada6f143ec44d3ec2b72da Impact I ran this on 270 issues and removed 120k lines and added 113k, new tests included, so the codebase got smaller while gaining tests. Most of the 270 issues came from a separate audit skill that walks user stories through one section of the app looking for duplicate logic, hidden assumptions, and one-off hacks, and files each finding as an issue. /occam then picks up from there. Why I think it works Claude's instinct is to add. Making "delete the feature" a row it has to score every time puts removal on the table without me having to argue for it. Designing the simple model before seeing the options keeps it from anchoring on the current code. A fixed shape and a score turn "is this good code?" made it easy for me to review 20+ issues in a single sitting. Caveats It's token heavy. I'd only run this on a subscription plan. Try it Point it at the part of your codebase you trust least. Or ask Claude to find places where the same thing is computed twice, have it file each one as an issue, and run /occam on them one at a time.
