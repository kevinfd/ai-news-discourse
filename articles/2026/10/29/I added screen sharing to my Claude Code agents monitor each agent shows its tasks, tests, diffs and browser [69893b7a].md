---
id: "69893b7aadf7a136"
title: "I added screen sharing to my Claude Code agents monitor: each agent shows its tasks, tests, diffs and browser live"
url: "https://reddit.com/r/ClaudeAI/comments/1xijj1w/i_added_screen_sharing_to_my_claude_code_agents"
link: "https://reddit.com/r/ClaudeAI/comments/1xijj1w/i_added_screen_sharing_to_my_claude_code_agents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T13:09:42Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["stickygoose"]
language: "en"
summary: "I built Agent Standup , a free, open-source app that shows your Claude Code sessions as a live video call: each session and sub-agent is a drawn character with a voice. The new feature is screen sharing: each agent shows what it's working on right now. The video is episode 2 of a small mockumentary about my agents. The interviews are a joke, but every cutaway is the real app following one real…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "Mistral", "Cursor"]
topics: ["agents & coding", "products & launches", "models & research"]
content_source: "post"
word_count: 458
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xijj1w/i_added_screen_sharing_to_my_claude_code_agents/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I added screen sharing to my Claude Code agents monitor: each agent shows its tasks, tests, diffs and browser live

Reddit · stickygoose · 2026-10-29

I built Agent Standup , a free, open-source app that shows your Claude Code sessions as a live video call: each session and sub-agent is a drawn character with a voice. The new feature is screen sharing: each agent shows what it's working on right now. The video is episode 2 of a small mockumentary about my agents. The interviews are a joke, but every cutaway is the real app following one real Claude Code session: a lead and two sub-agents fixing an office coffee app. What an agent's shared screen shows, live: its task list, with each task ticked off as it's done test runs: passed/failed counts, a green or red bar, and the names of the failed tests (node, vitest, jest, pytest, mocha, go, cargo) the diff of every edit, with real line numbers the browser it drives with Claude in Chrome: the page, the pointer moving to each click, what it types the output of a command it left running in the background, streaming with a red LIVE tag The part I use every day: when a session hits a permission menu or asks a question, a character knocks on the call, and one click opens that session's tab. How I built it with Claude Claude Code wrote nearly all of it: about 300 commits in two weeks, 296 of them co-authored by Claude Code. I decide what to build and test it by hand. My workflow: I usually run several Claude Code sessions on the repo at once (backend, page, translations). Watching them was the whole reason I built the app, and I now watch them build it in the app itself. A CLAUDE.md file holds the project's traps and rules for the agents. Every time an agent made the same mistake twice, a rule went in there. Claude Code tests its own changes: it opens the page in Chrome through Claude in Chrome and checks the result. A browser test suite runs the real page. Before each release, a separate Claude reviewer tries to prove the release breaks existing users. Claude translated the app into 10 languages. Inside the app, Claude (your own claude ) is only used to translate the call. How it works: a small local server reads the session files Claude Code already writes in ~/.claude/projects . No hooks, nothing to set up in Claude Code, and nothing leaves your machine by default. It also reads Codex and Mistral Vibe sessions. MIT license. Try it (free): VS Code / Cursor / Windsurf: search "Agent Standup" in Extensions. Terminal: npx @double_geste/agent-standup@latest --open As a Claude Code plugin: /plugin install agent-standup --marketplace Atoll92/agent-standup GitHub: https://github.com/Atoll92/agent-standup Website: https://agent-standup.com/ I'm building this alone. What would you want to see on your agents' screens next?
