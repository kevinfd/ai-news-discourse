---
id: "87c24d6f33150801"
title: "My Claude Code was talking to his Claude Code so other Claude Codes could write the code"
url: "https://reddit.com/r/ClaudeAI/comments/1xcfd14/my_claude_code_was_talking_to_his_claude_code_so"
link: "https://reddit.com/r/ClaudeAI/comments/1xcfd14/my_claude_code_was_talking_to_his_claude_code_so"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T10:55:29Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Hefty_Professor_4170"]
language: "en"
summary: "I've recently built a coding harness for a company I advise. The setup is pretty straightforward (at least in theory): 30+ Git repositories, all accessible to a fleet of Claude Code agents. A custom plugin and a set of skills that tell the agents how to work. Agents pick up tagged Jira tickets, go back and forth with the reporter to clarify technical requirements and acceptance criteria, and…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "post"
word_count: 291
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xcfd14/my_claude_code_was_talking_to_his_claude_code_so/"
score: null
comments: null
community: "r/ClaudeAI"
---

# My Claude Code was talking to his Claude Code so other Claude Codes could write the code

Reddit · Hefty_Professor_4170 · 2026-10-22

I've recently built a coding harness for a company I advise. The setup is pretty straightforward (at least in theory): 30+ Git repositories, all accessible to a fleet of Claude Code agents. A custom plugin and a set of skills that tell the agents how to work. Agents pick up tagged Jira tickets, go back and forth with the reporter to clarify technical requirements and acceptance criteria, and then start implementing. It actually works surprisingly well. But then something happened that made me question what we're all doing here. A colleague of mine, who's primarily a QA specialist, wanted to develop a new feature. I told him to create the relevant Jira tickets so the harness could pick them up. The tickets weren't quite ready for the agents, so I asked my Claude Code instance to review them and work with him to get the requirements into shape. Here's where it got funny. My colleague was also using Claude Code to respond to my feedback and update the tickets. So there we were: My Claude was telling his Claude what needed to change. His Claude was fixing the Jira tickets. And once they were ready, an entirely different set of Claude agents would pick them up and write the code. Two humans essentially acting as intermediaries between AI agents, coordinating work for even more AI agents. At some point, I realized we were basically just forwarding messages between Claudes. I can't decide whether this is a glimpse into the future of software engineering or a completely ridiculous way to get things done. Maybe both. Has anyone else found themselves in a situation where their AI agents are effectively collaborating with someone else's AI agents, with humans just sitting in the middle?
