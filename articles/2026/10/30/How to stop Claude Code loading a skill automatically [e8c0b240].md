---
id: "e8c0b24067a6d293"
title: "How to stop Claude Code loading a skill automatically"
url: "https://reddit.com/r/ClaudeAI/comments/1xj49xc/how_to_stop_claude_code_loading_a_skill"
link: "https://reddit.com/r/ClaudeAI/comments/1xj49xc/how_to_stop_claude_code_loading_a_skill"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T03:02:19Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["shoumikgoswami"]
language: "en"
summary: "You might want a changelog or weekly-report skill available as a command, without Claude choosing to load it during other work. Claude Code has a SKILL.md frontmatter field for that: --- name: changelog description: Format unreleased changes as a changelog entry disable-model-invocation: true --- Format the unreleased changes as a changelog entry: List the changes since the last release. Group…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches"]
content_source: "post"
word_count: 178
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xj49xc/how_to_stop_claude_code_loading_a_skill/"
score: null
comments: null
community: "r/ClaudeAI"
---

# How to stop Claude Code loading a skill automatically

Reddit · shoumikgoswami · 2026-10-30

You might want a changelog or weekly-report skill available as a command, without Claude choosing to load it during other work. Claude Code has a SKILL.md frontmatter field for that: --- name: changelog description: Format unreleased changes as a changelog entry disable-model-invocation: true --- Format the unreleased changes as a changelog entry: List the changes since the last release. Group them under Added, Changed and Fixed. Keep each line to one sentence. Save that as the skill's SKILL.md, then invoke it with /changelog. The field is from the Claude Code docs; the changelog example above is an illustration, not a reported test result. The docs describe disable-model-invocation as preventing Claude from automatically loading the skill, while keeping it available for manual invocation. Important distinction: this controls loading this particular skill. Don't treat it as a safety boundary that prevents Claude doing similar work through other instructions or tools. Invoking a skill doesn't grant extra permissions either. Useful when a workflow should be available on demand, rather than another thing Claude decides to bring into the task. Source: https://code.claude.com/docs/en/skills
