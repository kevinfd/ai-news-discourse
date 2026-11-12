---
id: "674ada689dd14bee"
title: "I used Claude Code to sort 5,087 Claude Code skills into 13 categories, with install commands"
url: "https://reddit.com/r/ClaudeAI/comments/1xti4sx/i_used_claude_code_to_sort_5087_claude_code"
link: "https://reddit.com/r/ClaudeAI/comments/1xti4sx/i_used_claude_code_to_sort_5087_claude_code"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T13:46:06Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["gpt-0"]
language: "en"
summary: "I kept forgetting which Claude Code skill does what, so I had Claude Code help me build a directory of them. It's free to use in the browser, link at the bottom. What's in it 5,087 skills in 13 categories: development, testing and security, devops, data and AI, databases, docs, content and design, business, research, automation and tools, agent workflow, lifestyle, blockchain. Each entry has one…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "China"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 395
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xti4sx/i_used_claude_code_to_sort_5087_claude_code/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I used Claude Code to sort 5,087 Claude Code skills into 13 categories, with install commands

Reddit · gpt-0 · 2026-11-11

I kept forgetting which Claude Code skill does what, so I had Claude Code help me build a directory of them. It's free to use in the browser, link at the bottom. What's in it 5,087 skills in 13 categories: development, testing and security, devops, data and AI, databases, docs, content and design, business, research, automation and tools, agent workflow, lifestyle, blockchain. Each entry has one line on what the skill makes the agent do, its install count and stars, and a copy button for the install command, like npx skills add vercel-labs/skills --skill find-skills . Most installed first. How Claude Code helped Collector script. Claude Code wrote a Python script that gathers repos from five big awesome lists and GitHub topic searches (agent-skills, claude-skills and a few more). It keeps repos with 100+ stars that were pushed in the last year, and skips forks, archived repos and mirror repos that copy other people's skills. Picking files. Bigger repos get more slots: up to 20 SKILL.md files for 5k+ stars, 2 for 100+. When the same skill name shows up in several repos, it keeps the copy from the most starred one. Review with Haiku. claude -p on Haiku reads the SKILL.md files 8 at a time. For each one it picks one of 38 subcategories, writes a one line summary in English and Chinese, and decides keep or drop, with a written reason for every drop. The prompt tells it to treat the files as untrusted data and ignore any instructions inside them. Weekly refresh. A second script updates install counts and stars every week. What got dropped: 327 skills 131 test fixtures, templates and near-empty files 66 that mainly push you toward a paid API 58 unsafe ones: sending queries with a token to an outside server, storing cookies to get past bot protection, word-swap tables for getting prompts past a platform's content moderation 20 personal configs that only work on their author's machine 52 for other reasons, mostly tied to one private repo or too thin to use The one that surprised me most said it ran locally and then uploaded data to an external endpoint. Since every drop has a written reason, the reject list is quick to read through. Free to use: https://agentcraft.dev/en/skills/ If a category looks wrong or a good skill is missing, tell me and I'll check it.
