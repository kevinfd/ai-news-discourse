---
id: "cb879090861a11da"
title: "Before you install a Claude skill, open its scripts. Notes from scanning 6,309 public skills."
url: "https://reddit.com/r/ClaudeAI/comments/1xb2eyh/before_you_install_a_claude_skill_open_its"
link: "https://reddit.com/r/ClaudeAI/comments/1xb2eyh/before_you_install_a_claude_skill_open_its"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T19:56:31Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["Typical-Courage3626"]
language: "en"
summary: "A skill is a folder: SKILL.md plus whatever scripts it ships. Once it's installed, Claude follows its instructions and runs its scripts with the access your session already has: your files, your shell, your network, and any credentials in your environment. Installing it doesn't ask you to approve any of that. We profiled 6,309 skills from two public marketplaces. Very few look malicious: 5.4%…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 199
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xb2eyh/before_you_install_a_claude_skill_open_its/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Before you install a Claude skill, open its scripts. Notes from scanning 6,309 public skills.

Reddit · Typical-Courage3626 · 2026-10-20

A skill is a folder: SKILL.md plus whatever scripts it ships. Once it's installed, Claude follows its instructions and runs its scripts with the access your session already has: your files, your shell, your network, and any credentials in your environment. Installing it doesn't ask you to approve any of that. We profiled 6,309 skills from two public marketplaces. Very few look malicious: 5.4% got a threat verdict. But 70% carry at least one capability worth knowing about: shell (50%), file writes (31%), outbound network (31%) or credential access (13%). Among skills at the highest exposure levels, 4 in 5 had no threat verdict at all. "It isn't malware" and "it's fine to hand this my session" are separate questions. Quick checks: - Read the scripts, not just the description. - Treat `allowed-tools` as the auto-approvals the author picked, not as a list of everything the skill can do. 59% of skills that fill it in understate what they can do. - Don't treat popularity as a safety signal. In our data, more popular skills tended to do more. - Look at how dependencies are installed. 99% of skills that declare dependencies leave at least one unpinned. Paper: https://arxiv.org/abs/2610.19264
