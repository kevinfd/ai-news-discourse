---
id: "d2ce34ed9e0dae82"
title: "Your agentic coding sessions are a treasure"
url: "https://kotrys.dev/blog/your-agent-trajectories-are-a-treasure"
link: "https://kotrys.dev/blog/your-agent-trajectories-are-a-treasure"
source: "Bartosz Kotrys"
domain: "kotrys.dev"
source_type: "community"
collector: "reddit"
date: "2026-11-02T19:10:38Z"
published_date: "2026-11-02"
collected_at: "2026-11-03T13:04:23Z"
authors: ["Bartaseth"]
language: "en"
summary: "Your agent trajectories are a treasure\nThe tests pass and the diff looks fine. That still tells you very little about why the agent needed so many attempts, which correction got it unstuck, or why the run cost more than expected. For that, you need the session history.\nI keep coding-agent transcripts so I can go back to the commands, errors, and corrections behind a change. When I hit the same…"
tags: ["r/artificial"]
orgs: ["Anthropic", "Cursor", "OpenAI"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1203
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xm6ev6/your_agentic_coding_sessions_are_a_treasure/"
score: null
comments: null
community: "r/artificial"
---

# Your agentic coding sessions are a treasure

Bartosz Kotrys · Bartaseth · 2026-11-02

Your agent trajectories are a treasure
The tests pass and the diff looks fine. That still tells you very little about why the agent needed so many attempts, which correction got it unstuck, or why the run cost more than expected. For that, you need the session history.
I keep coding-agent transcripts so I can go back to the commands, errors, and corrections behind a change. When I hit the same problem again, I want to find the fix I already worked through. When a run is unexpectedly expensive, I want to see where the work went.
That history can disappear before you need it. Claude Code’s default cleanup removes ordinary local sessions older than 30 days, including their tool results and explanations. If that was your only copy, the history is gone for good. Here is what those files contain, what you can learn from them, and how to keep a copy.
A session is more than a chat log
When you revisit a session, look at the work between the prompt and the final answer: failed commands, test output, and corrections. These show what the agent tried and what changed along the way.
Four terms help describe what gets saved: prompt, session, transcript, and trajectory.
- A prompt is what you ask the coding agent.
- A session covers the work that follows, often across several prompts: reading files, calling tools, running tests, and responding to your corrections.
- The saved transcript contains the messages, tool calls, and results.
- The trajectory is the path through that work, including failed attempts and changes of direction.
In practice, transcript and trajectory often mean the same record.
Depending on the tool, the archive also holds model and token data, saved reasoning, subagent sessions, and related memory and settings files. Not every tool saves all of this, and a transcript does not expose everything happening inside a model.
An agent saying “fixed” is not proof that the fix worked. A transcript may omit tool output, replace earlier context with a compacted summary, or lack the repository state needed to reproduce a command. You do not need to read it line by line yourself: ask your coding agent to review the saved session alongside the final diff and test results, identify repeated failures, and point you to the relevant exchanges. Check its conclusions against the code and tests.
What went wrong, and what helped
In the RTK benchmark I coauthored, one attempt passed after 339 consecutive errors and cost about 9× as much as the matching baseline attempt. The saved trajectories explained the cost: a plugin rewrote find to rtk find, which rejected a flag and advised using find directly. The retry got rewritten again. The cost comparison alone would not have explained the retry loop. This was one outlier attempt; RTK fixed the bug in 0.46.0 after the benchmark runs.
LangChain found that its coding agent sometimes stopped after rereading its code, without running tests, and repeated failed approaches. The team changed its harness, the instructions, tools, and checks around the model. It added test checks, better environment context, and reminders to reconsider repeated edits. Its Terminal Bench 2.0 pass rate rose from 52.8% to 66.5% with the same GPT-5.2-Codex model.
My memory tool was still using the old model
I use claude-mem, which lets you configure the model it uses to create memories. I had set it to Sonnet 4.6 a long time ago and forgotten about that setting, even after switching my coding work to Sonnet 5. I only noticed it in Quesma’s observability dashboard: Sonnet 4.6 was still appearing in my usage. The model-share chart below made the forgotten configuration visible.
Your transcripts also show which corrections you keep repeating. Across team-shared sessions, you can check whether instructions work consistently across models and harnesses. Use those patterns to improve AGENTS.md, skills, or DESIGN.md, then check later sessions and tests to see whether the changes helped.
Billing incidents and security audits need evidence
OpenAI acknowledged incorrect request accounting, while Anthropic confirmed that some Max users were incorrectly prompted to spend usage credits. Saved dates, model names, and token counts give you records to compare when questioning a charge, though they do not replace the provider’s billing records.
Recorded tool calls can also help investigate unexpected commands or file access. They are supporting evidence, not a complete security audit log.
Thirty days is a short life for that knowledge
Claude Code’s default cleanup removes ordinary local session records older than 30 days, including messages, tool calls, and results. The cleanup runs in the background after a session starts. Check the current documentation and the settings your organization applies.
Cursor support said in July that it did not automatically expire kept local chat history. That still leaves the history dependent on the local files. Session files can still disappear through:
- Accidental deletion, manual cleanup, or a reinstall that removes local files.
- An application update or failed migration. Cursor support has acknowledged history loss during updates.
- A lost laptop or failed disk when it holds the only copy.
In August, one Claude Code user reported 852 missing transcripts out of 1,120 conversations. Independent backups made recovery possible.
Keeping a copy
Keep a backup off the laptop and retain older versions so cleanup cannot erase the last copy. A synchronized mirror alone can copy a deletion too.
For Claude Code, "cleanupPeriodDays": 365 in your user settings.json extends retention to a year unless managed settings override it. Longer local retention helps, but you still need a backup.
macOS paths
Claude Code user settings: ~/.claude/settings.json
- Claude Code
- ~/.claude/projects/
- Codex
- ~/.codex/sessions/~/.codex/archived_sessions/~/.codex/session_index.jsonl
- Cursor
- ~/.cursor/projects/~/Library/Application Support/Cursor/User/globalStorage/
If you have changed the storage location, back up that folder instead.
Linux paths
Claude Code user settings: ~/.claude/settings.json
- Claude Code
- ~/.claude/projects/
- Codex
- ~/.codex/sessions/~/.codex/archived_sessions/~/.codex/session_index.jsonl
- Cursor
- ~/.cursor/projects/~/.config/Cursor/User/globalStorage/
Also check $XDG_CONFIG_HOME/claude/ for Claude's settings and projects. Cursor may use $XDG_CONFIG_HOME/Cursor/User/globalStorage/ or ~/.config/cursor/User/globalStorage/.
If you have changed the storage location, back up that folder instead.
Windows paths
Claude Code user settings: %USERPROFILE%\.claude\settings.json
- Claude Code
- %USERPROFILE%\.claude\projects\
- Codex
- %USERPROFILE%\.codex\sessions\%USERPROFILE%\.codex\archived_sessions\%USERPROFILE%\.codex\session_index.jsonl
- Cursor
- %USERPROFILE%\.cursor\projects\%APPDATA%\Cursor\User\globalStorage\
For tools running in WSL, use the Linux paths inside WSL.
If you have changed the storage location, back up that folder instead.
Paths vary by tool version and configuration. Close the apps before copying live databases, encrypt your backups, and check you can restore them.
Start with a session worth revisiting. Ask your agent to review it alongside the diff and test results to see what worked and what to change.
Keeping sessions across a team
I am a Founding Engineer at Quesma. We help individuals and teams preserve agent sessions, compare costs, and learn what to improve in their instructions and tools.
Our open-source Quesma Shipper collects local session files, redacts sensitive patterns, and encrypts them before upload. The architecture page explains where the data goes and who can decrypt it.
You can use Quesma as an individual; you do not need a team to get started. The product page walks you through setup on macOS, Linux, and Windows. A versioned backup is still a useful first step if you just want to keep your sessions.
