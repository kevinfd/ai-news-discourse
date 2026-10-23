---
id: "0c87a516a18c859a"
title: "I made Claude act as the whole app instead of writing it: try an idea by hand in minutes (works as an artifact)"
url: "https://reddit.com/r/ClaudeAI/comments/1xd07k8/i_made_claude_act_as_the_whole_app_instead_of"
link: "https://reddit.com/r/ClaudeAI/comments/1xd07k8/i_made_claude_act_as_the_whole_app_instead_of"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-23T01:02:14Z"
published_date: "2026-10-23"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Other_Train9419"]
language: "en"
summary: "I'm a solo developer. As I worked with Claude, the direction of what I should build kept changing, and to verify whether an idea was useful, I had to spend hours repeatedly creating and revising it. Mockups weren't helpful. While the screens themselves are easy to create, what really matters is the behavior behind them. So, I reversed the order. **kuron** provides Claude with several generic…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["products & launches", "agents & coding"]
content_source: "post"
word_count: 339
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xd07k8/i_made_claude_act_as_the_whole_app_instead_of/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I made Claude act as the whole app instead of writing it: try an idea by hand in minutes (works as an artifact)

Reddit · Other_Train9419 · 2026-10-23

I'm a solo developer. As I worked with Claude, the direction of what I should build kept changing, and to verify whether an idea was useful, I had to spend hours repeatedly creating and revising it. Mockups weren't helpful. While the screens themselves are easy to create, what really matters is the behavior behind them. So, I reversed the order. **kuron** provides Claude with several generic tools (data, screens, timers, sounds, and verification functions), and no app code is generated at all. Based on an idea, Claude sets up the system and then handles all button operations on its own. If something isn't working correctly, I simply tell it, "This is how it should be," and it corrects itself. Once I know what to build, it writes specifications and a build plan based on what the system actually did. Since LLMs make everything seem possible, enabling the **"existing technology" switch** makes each action behave like a release-ready version would. In other words, it may be slow, sometimes incorrect, or even impossible to implement at this stage. **How I Built It / What I Learned** - I built this using Claude Code. My only rule was "don't put business logic in the code." If the prototype malfunctioned, the fix had to be a more appropriate instruction to the LLM, rather than an `if` statement. - Tools that check the format of each call and give verbal feedback (e.g., "Text required in the heading") let Claude correct itself. This was more effective than fine-tuning the prompt. - It runs through the `claude -p` command with the tools provided as an MCP server, or as an artifact where the page's functions serve as Claude's tools. Note: The tool schema in an artifact cannot be nested more than 8 levels deep. Recorded run (clinic using 5 devices): Setup 65 seconds / approximately $0.41, followed by 7–14 seconds per action. Not suitable for production environments or real-time applications. - Recorded run: https://kuron.pages.dev - Try it out (claude.ai login): https://claude.ai/artifact/UMMbf2FcV3ULi6d5WaW1yp - Source code (MIT): https://github.com/Ag3497120/kuron
