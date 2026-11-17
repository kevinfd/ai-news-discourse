---
id: "614053f82fef9222"
title: "mcflow 0.1.0: A free workflow that makes Claude Code build, run, and visually test Minecraft plugins in-game before reporting back"
url: "https://reddit.com/r/ClaudeAI/comments/1xy64bv/mcflow_010_a_free_workflow_that_makes_claude_code"
link: "https://reddit.com/r/ClaudeAI/comments/1xy64bv/mcflow_010_a_free_workflow_that_makes_claude_code"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T00:27:43Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Accomplished_Fee9159"]
language: "en"
summary: "Claude Code is fast at writing code, but when it comes to game modding—specifically Paper plugins (server-side mods for Minecraft)—it guesses a lot. It hallucinates APIs, mixes up methods from different game versions, and confidently tells you something works without ever running it. I built mcflow , a free, open-source CLI and workflow that stops Claude Code from guessing by forcing it through…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research", "search & media"]
content_source: "post"
word_count: 399
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xy64bv/mcflow_010_a_free_workflow_that_makes_claude_code/"
score: null
comments: null
community: "r/ClaudeAI"
---

# mcflow 0.1.0: A free workflow that makes Claude Code build, run, and visually test Minecraft plugins in-game before reporting back

Reddit · Accomplished_Fee9159 · 2026-11-17

Claude Code is fast at writing code, but when it comes to game modding—specifically Paper plugins (server-side mods for Minecraft)—it guesses a lot. It hallucinates APIs, mixes up methods from different game versions, and confidently tells you something works without ever running it. I built mcflow , a free, open-source CLI and workflow that stops Claude Code from guessing by forcing it through a strict verification loop: research → build → test on a real local server → inspect it in-game → only then show you the change Even if you don't mod Minecraft, it’s a fun example of using custom skills, sub-agents, and MCP servers to make Claude verify complex, stateful software on its own. How it works: Workspace & Rules ( mcflow init ): Scaffolds a project for your target Minecraft version, complete with tailored CLAUDE.md rules, custom skills, helper agents, and AGENTS.md if you use other coding tools. Environment Checks ( mcflow doctor ): Automatically figures out which Java version your target Minecraft server needs, scans your system for existing JDKs, and tells you what’s missing. Server Control via MCP: Gives Claude an MCP server to start, stop, and cleanly restart a local Minecraft server, console commands (via RCON), and read crash logs directly. Automated Bots & Load Testing: Claude can spawn fake players to join the server, chat, and move around, plus run stress tests and performance profiling. spark ). Real In-Game Visual Checks: Uses a lightweight game client mod (Fabric) so Claude can actually boot the game and inspect what it built—like verifying a custom in-game UI menu actually rendered properly—instead of assuming the code worked. Version-Tagged Knowledge Base: Saves techniques that actually passed live tests (tagged by game version) so Claude stops making the same API mistakes twice. Fast Code Search: Bundles checksum-verified TokToken integration so Claude can quickly index and search the codebase. Install (requires Python 3.11+ and pipx ): Bash pipx install git+https://github.com/LadonON/mcflow.git@v0.1.0 It’s MIT-licensed, runs on Windows, macOS, and Linux (verified in CI by running a real server end-to-end on all three), and is at v0.1.0—so expect a few rough edges. Note that the live in-game client checks require a standard Minecraft Java Edition account. GitHub: https://github.com/LadonON/mcflow For folks building complex Claude Code workflows: how are you forcing Claude to verify its own work in environments you can't just unit-test? Would love any feedback on the setup or MCP architecture!
