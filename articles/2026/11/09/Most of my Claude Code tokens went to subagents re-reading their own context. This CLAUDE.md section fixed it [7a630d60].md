---
id: "7a630d6038a49085"
title: "Most of my Claude Code tokens went to subagents re-reading their own context. This CLAUDE.md section fixed it"
url: "https://reddit.com/r/ClaudeAI/comments/1xs1d5y/most_of_my_claude_code_tokens_went_to_subagents"
link: "https://reddit.com/r/ClaudeAI/comments/1xs1d5y/most_of_my_claude_code_tokens_went_to_subagents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-09T19:35:41Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Altruistic_Bag9820"]
language: "en"
summary: "Hey guys, I use Claude a lot, and at first I kept hitting usage limits. I normally run Opus on high effort as my main session and work on several projects at once, and I was using up my whole allowance in 36 hours or less. After some troubleshooting I found that most of my tokens were going into sharing context with the subagents Claude starts. Claude was also using Opus for well-defined tasks…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding"]
content_source: "post"
word_count: 409
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xs1d5y/most_of_my_claude_code_tokens_went_to_subagents/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Most of my Claude Code tokens went to subagents re-reading their own context. This CLAUDE.md section fixed it

Reddit · Altruistic_Bag9820 · 2026-11-09

Hey guys, I use Claude a lot, and at first I kept hitting usage limits. I normally run Opus on high effort as my main session and work on several projects at once, and I was using up my whole allowance in 36 hours or less. After some troubleshooting I found that most of my tokens were going into sharing context with the subagents Claude starts. Claude was also using Opus for well-defined tasks that Sonnet or Haiku could handle perfectly well. I added a delegation section to my CLAUDE.md , plus three custom subagents. Since then I've gotten at least 3x more usage without losing any quality. Sharing it in case anyone wants to give it a try. **Full CLAUDE.md section and the three agent files: https://gist.github.com/eugertjani-lab/5a7c441555aa819404f65c0bc9d887cc\*\* Here's the short version of how it works: - The main Opus session investigates, plans, makes the decisions and checks the results. As soon as a step is fully specified, it hands the execution to a cheaper subagent. - The three custom agents live in `~/.claude/agents/`: `implementer` (Sonnet, high effort) for multi-file work that follows a written plan, `mechanic` (Haiku, xhigh) for renames, repeated edits, format conversion and running scripts, and `scout` (Haiku, xhigh, read-only) for finding files, symbols and call sites. - Subagents never make decisions. When they hit an open choice, a contradiction with the brief, or anything destructive, they stop and return a `DECISION NEEDED` block. Opus makes the call and continues the same agent. - The brief carries the context: the goal, exact paths, decisions already made, steps, what's out of scope and an acceptance check. Excerpts go in as `file:line` ranges, never whole files. - Agents stay short. At around 150 tool calls (100 for mechanic) an agent stops with a `HANDOFF` block and Opus starts a fresh one from it. Finished agents never get resumed for small follow-ups, because a resume re-reads the whole context on every call. - The built-in `general-purpose` and `Explore` agents are avoided for delegated work, since they may inherit Opus and erase the savings. The biggest surprise for me was the re-reads. Every tool call resends the whole conversation, so a subagent that has read a lot gets more expensive with every step it takes. In my longer runs, nearly all the spent tokens were agents re-reading contexts that had grown toward a million tokens. If you've found other ways to keep subagent context small, I'd love to hear them.
