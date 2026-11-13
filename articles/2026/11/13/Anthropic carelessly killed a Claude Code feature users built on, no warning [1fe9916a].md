---
id: "1fe9916aaf7114fb"
title: "Anthropic carelessly killed a Claude Code feature users built on, no warning"
url: "https://github.com/anthropics/claude-code/issues/109446"
link: "https://github.com/anthropics/claude-code/issues/109446"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-13T03:13:43Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["rezzminator"]
language: "en"
summary: "Repository navigation\nDescription\nRegression: 2.1.323 silently removed subagentStatusLine, with no reason, no replacement and no migration path\nWhat happened\nThe 2.1.323 changelog says:\nRemoved the subagentStatusLine setting: subagent rows always use the default look, and settings files that still hold the key load as before\nThe settings schema now describes the key as \"Deprecated: no longer has…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 1054
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50477704"
score: 25
comments: 6
community: "Hacker News"
---

# Anthropic carelessly killed a Claude Code feature users built on, no warning

GitHub · rezzminator · 2026-11-13

Repository navigation
Description
Regression: 2.1.323 silently removed subagentStatusLine, with no reason, no replacement and no migration path
What happened
The 2.1.323 changelog says:
Removed the subagentStatusLine setting: subagent rows always use the default look, and settings files that still hold the key load as before
The settings schema now describes the key as "Deprecated: no longer has any effect. Subagent rows always use the default look." Nothing warns at startup. A configured command simply stops running, and users find out when their agent panel goes blank.
2.1.322 still runs the command. 2.1.323 never calls it.
Why this hurts
subagentStatusLine was the only place in Claude Code where a user could see, per running subagent, at a glance:
- its live context use against its own window
- what it has spent so far (tokens and dollars)
- its model and its reasoning effort
- its status, its age and its prompt-cache state
Without it, a session that runs several background agents is flying blind. Nothing in the default row shows which agent is burning context, which one is about to hit its window, which one went to the expensive model, or which one is silently re-paying for an expired cache.
This is the row as it rendered on 2.1.322, boxed in red:
The same row as text:
○ ▱▱▱▱▱▱▱ 8% 82.6K/1.0M Σ$2.06/2.9M/28.5K/40 │flights:foreman│opus·▰▰ medium│running 5m:40s│1 error│💾5m✓4m:54s 98%
After 2.1.323 the same row reads only flights:foreman  Running grep.
This contradicts your own recent direction
The changelog kept investing in this setting right up to the removal:
- "Added reasoning effort to the subagentStatusLine payload, so custom agent rows can render model and effort"
- "Added agentType to the subagentStatusLine payload, so scripts can tell custom subagent types apart"
- "Fixed ${CLAUDE_PLUGIN_ROOT} not being substituted in a plugin-provided subagentStatusLine command"
People built on those additions. The docs still present the setting as live today: https://code.claude.com/docs/en/statusline (section on subagentStatusLine) and https://code.claude.com/docs/en/settings.
Mods do not replace it
The ui.render sites in 2.1.323 are AskUserQuestion, UserMessage, AssistantMessage, ToolUse, ToolResult, ToolGroup, ToolProgress, CommandOutput, Spinner, TurnDuration, InfoNotice, SessionMode, PromptHint, AbovePrompt, Pane and Placed. None of them is an agent-panel row, so no mod can draw what this setting drew. #105919 asked for exactly that render site on 2026-10-29 and has had no answer.
Related open requests that all assume this setting exists: #102183, #102890, #96895, #97634 (the last one notes that no other place in the UI shows a subagent's model).
What we ask
- Restore subagentStatusLine in the next release, with the same payload as 2.1.322 (including effort, agentType, contextWindowSize and tokenCount).
- If the default agent panel is being redesigned, ship the replacement before removing the old hook: a ui.render site for each agent-panel row ([FEATURE] Mods: render sites for statusLine and subagentStatusLine rows #105919), whose props carry the same payload.
- Do not remove a documented, configurable surface without a deprecation release that warns at startup and a changelog line that says why.
Environment
- Claude Code 2.1.323 (regression); 2.1.322 works
- Linux and macOS, terminal UI
- The subagentStatusLine command is set through --settings and in user settings; both are ignored on 2.1.323
Activity
- addedbugSomething isn't workingSomething isn't workingplatform:linuxIssue specifically occurs on LinuxIssue specifically occurs on Linuxplatform:macosIssue specifically occurs on macOSIssue specifically occurs on macOSon Nov 13, 2026
- You've removed a functionality that I've built my real-time observability on it, with NO reason/replacement/explanation!!
This is unacceptable!
@dhollman Can you please have a look into this!? Reacted by hagsonz
- Same regression here. Our subagentStatusLine script showed, per running agent: model + effort, input/output/cache tokens, ≈$ cost, its share of the 5h/7d limits, the nested-agent tree, and which external CLI the agent was driving. After 2.1.323 none of it is visible.
What we tried on 2.1.323: 
  - color: in the agent frontmatter does not reach the agent panel rows.
  - A mod cannot render those rows either: there is no ui.render site for them (only Pane, AbovePrompt, ToolUse, …). An AbovePrompt band fed by $.agent.list() and agent.spawn works, but it lists every agent a second time above the prompt while the native rows below stay plain, and the native panel cannot be hidden.
  - The only real workaround is pinning 2.1.322 with DISABLE_AUTOUPDATER=1, which gives up every later fix.
Please either restore subagentStatusLine, or ship a replacement that renders into the native rows, for example a mod render site for agent-panel rows (#105919) that receives the row's agent id, model and effort.
- what? why? we need it back Reacted by a6m1n
- Same regression on macOS, 2.1.322 → 2.1.323. Before (2.1.322): After (2.1.323): What the custom row gave me, per running subagent, at a glance and live:
sonnet-5-5·medium · Reading the settings module · 2m · ▁▃█▂▁ · ↓ 85.5k/1M 9%
Why it matters: I assign a model and an effort level to each subagent on purpose
(cheaper model for mechanical work, stronger one for review). The row was the only
place that showed what each agent actually got, and how close it was to its context
window, without opening the agents one by one. On 2.1.323 the same row reads
general-purpose  Reading the settings module.
What I checked on 2.1.323 before giving up: 
  - No setting or env var changes the row; the schema says "Deprecated: no longer has any effect".
  - Mods: no render site for the agent panel rows, and AgentInfo from $.agent.list()
has no model, effort or token fields, so a band above the prompt would need to rebuild
them from transcript files, and it lists every agent a second time.
  - /tasks names the model and effort, but not context use, and it is not visible while working.
  - Rebuilding the rows inside the main statusLine works, but it duplicates the panel,
a row cannot open its agent, and it refreshes only onrefreshInterval.
Workaround for anyone who needs the rows today: pin 2.1.322. A symlink at
~/.local/bin/claude pointing into versions/ is re-pointed by auto-update; a small
wrapper script there (exec ~/.local/share/claude/versions/2.1.322 "$@") is left alone,
and claude doctor confirms it. The cost is every fix after 2.1.322.
Ask: restore subagentStatusLine with the 2.1.322 payload, or ship a render site for
the panel rows (#105919, #102058) whose props carry model, effort, token count and
context window size, before the old hook goes away.
- "AI doesn't care about users" Silly humans
