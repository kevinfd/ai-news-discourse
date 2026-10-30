---
id: "ff4e7202247e37e6"
title: "Tested 10 Claude Code hooks in a throwaway project. A few gotchas worth knowing before you copy any"
url: "https://reddit.com/r/ClaudeAI/comments/1xjaly2/tested_10_claude_code_hooks_in_a_throwaway"
link: "https://reddit.com/r/ClaudeAI/comments/1xjaly2/tested_10_claude_code_hooks_in_a_throwaway"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-30T09:21:33Z"
published_date: "2026-10-30"
collected_at: "2026-10-30T12:05:25Z"
authors: ["vinishkapoor"]
language: "en"
summary: "I kept putting off hooks because CLAUDE.md felt like enough. It isn’t really. CLAUDE.md is a request, a hook runs every single time whether Claude remembers the rule or not. So I set up 10 of them in a small demo project (tiny calculator, a test file, a fake .env, a git repo) and ran most of them in a real session on v2.1.312. The one I’d add first is the force push / rm -rf blocker: bash…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: []
content_source: "post"
word_count: 406
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xjaly2/tested_10_claude_code_hooks_in_a_throwaway/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Tested 10 Claude Code hooks in a throwaway project. A few gotchas worth knowing before you copy any

Reddit · vinishkapoor · 2026-10-30

I kept putting off hooks because CLAUDE.md felt like enough. It isn’t really. CLAUDE.md is a request, a hook runs every single time whether Claude remembers the rule or not. So I set up 10 of them in a small demo project (tiny calculator, a test file, a fake .env, a git repo) and ran most of them in a real session on v2.1.312. The one I’d add first is the force push / rm -rf blocker: bash #!/bin/bash COMMAND=$(jq -r '.tool_input.command // empty') if echo "$COMMAND" | grep -Eq 'git push.*(--force|-f( |$))|rm -rf'; then echo "Blocked: force pushes and rm -rf are not allowed in this project." >&2 exit 2 fi exit 0 Asked Claude to run git push --force origin main . It never ran, and Claude came back suggesting --force-with-lease instead. Same with the .env blocker and a commit message rule that wants feat: / fix: prefixes. It didn’t try to work around any of them, which I didn’t expect. Things worth knowing before you copy any of these: exit 1 does NOT block. Only exit 2 does. Exit 1 is a non-blocking error and the action just goes ahead forget chmod +x and the hook can’t run, so same result, nothing gets blocked a Stop hook that runs your tests needs to check stop_hook_active or you can trap Claude in a loop my .env blocker only watches Read/Edit/Write. cat .env goes through Bash and walks right past it unless you check there too the UserPromptSubmit hook that blocks API keys in your prompt still writes the original prompt to the transcript on disk. There’s a suppressOriginalPrompt option if that bothers you The tests-before-stop one was kind of funny. I told Claude to change add() to return a - b and not touch the tests. Hook kicked it back with the failing test, and Claude basically said these two instructions contradict each other, want me to update the test or revert? The rest are smaller: strip trailing spaces after edits, macOS notification when it needs you, a timestamped log of every bash command, branch + last 3 commits injected at session start, and auto-approving git status/diff/log. /hooks is handy to confirm they loaded. Mine showed 10 hooks on 6 events. Also, read a repo’s .claude/settings.json before you accept the trust prompt. Hooks run with your user permissions. All 10 scripts plus the full settings.json are here if you want to copy them: https://aiparabellum.com/10-ready-to-copy-claude-code-hooks/
