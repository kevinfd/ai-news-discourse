---
id: "182bcfeeb22b1d3c"
title: "Octomind – open-source AI harness that saves your tokens, static rust"
url: "https://github.com/Muvon/octomind"
link: "https://github.com/Muvon/octomind"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-03T15:02:58Z"
published_date: "2026-11-03"
collected_at: "2026-11-04T13:04:06Z"
authors: ["donk8r"]
language: "en"
summary: "Interactive, stdin, daemon, WebSocket, or ACP — one binary, one config.\nA supervising model plans and checks the work.\nPolicy lives in TOML guardrails, not approval prompts.\nWebsite · Docs · Tap Registry · Benchmarks · Issues\nOctomind is an open-source coding agent harness. It gives any LLM the tools to work in a repository — read and edit files, run shells, search code, delegate to sub-agents —…"
tags: []
orgs: ["OpenAI", "Anthropic", "DeepSeek"]
topics: ["models & research", "agents & coding", "safety & ethics", "policy & regulation"]
content_source: "fulltext"
word_count: 1750
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50352898"
score: 55
comments: 37
community: "Hacker News"
---

# Octomind – open-source AI harness that saves your tokens, static rust

GitHub · donk8r · 2026-11-03

Interactive, stdin, daemon, WebSocket, or ACP — one binary, one config.
A supervising model plans and checks the work.
Policy lives in TOML guardrails, not approval prompts.
Website · Docs · Tap Registry · Benchmarks · Issues
Octomind is an open-source coding agent harness. It gives any LLM the tools to work in a repository — read and edit files, run shells, search code, delegate to sub-agents — through MCP, and runs the result as an interactive CLI, a stdin pipe, a daemon, a WebSocket server, or an ACP agent in your editor. Most agents stop and ask a human before each risky step, which works at a keyboard and blocks everything in CI. Octomind writes that policy down as TOML guardrails and adds a supervising model that plans and checks the work, so the same session can run with nobody watching. On 25 tasks taken from merged pull requests it solved 24; OpenCode solved 19 with the same model at about twice the cost (benchmarks).
One diagram, the whole turn: what is assembled before the model sees the request, the tool loop, how a turn is allowed to end, and what carries over to the next session.
- What the model sees is built once per user message, not per tool round: AGENTS.md, the skills whose rules match the prompt (standard SKILL.md folders), the tool bundles those skills need (they start their own MCP servers on demand), and the few past lessons that match. Skills · Learning
- Compression folds older turns into a summary that cites content-addressed blocks; the raw messages stay in a per-session archive and the recall tool brings any block back verbatim as a normal tool result, so history is never rewritten and the prompt cache survives. Compression
- Guards, hooks, validators are deterministic and live in .agents/guardrails.toml plus scripts; they run before any model opinion. The optional intent check ([supervisor.authorizer], off by default) adds one supervisor-model look after the guards and blocks a call only when it independently conflicts with what you asked for. Guardrails
- The supervisor is a second model ([supervisor.model]): it keeps the plan and reminds the model of the goal each turn, cuts oversized tool results down to the lines the task needs (copied, never retyped), and refuses a self-reported "done" until the evidence checks out. The loop check is a fixed heuristic: when the model repeats itself or stalls it gets one nudge, never a takeover. Supervisor
- The decision model ([decision]) is optional: a classifier that answers typed yes/no questions with a probability instead of prose. When set, the supervisor sends its cheap questions there — which lessons to recall, which skill to activate, which lines to keep, whether a completion claim holds — and keeps chat calls for writing. Calibrated decisions
- Learning extracts lessons after /done or at exit, in your own words, into files under learning/<project>/<role>/; later sessions recall the ones that match. With [supervisor.learning.evolution] enabled, recurring lessons become skill and guardrail candidates that run in shadow first, then an A/B trial against a control arm, and go active only when they beat it. Learning
Built for the work that keeps going after you leave:
- Policy as code, not approval popups. Deterministic guardrails — pre-call guards, post-result hooks, post-turn validators — live in TOML and scripts, so they work in CI, daemons, and scheduled runs.
- Measured, not claimed. All four agents ran stock on the same tasks with the same judge. Per-case table, artifacts, and a reproduction guide are in the benchmarks.
- Ready-made specialists. octomind run developer:general pulls a packaged agent (prompt, model, MCP servers, tool permissions) from a tap. Publish your own with one repo.
- Sessions that stay sharp. Adaptive compression keeps long tasks moving without forgetting the task or your last few messages.
- Learns the project as you work. Corrections and rules you state become lessons, quoted from your own words and scoped to the project and role, and come back in later sessions. Turn on evolution and recurring lessons compile into skill and guardrail candidates, trialled against a control and kept only when they help.
- Any model, any budget. Use Octomind Cloud or your own key (OpenRouter, Anthropic, OpenAI, DeepSeek, Ollama, and more), pick a model per role, and cap spend per request and per session. Over budget, a terminal session asks y/N; a non-interactive run stops with exit code 75.
- One config. Models, tools, roles, guardrails, budgets: all TOML, no framework code.
# Interactive
octomind run developer:general
# Non-interactive — CI, scripts, automation
echo "Explain the auth module" | octomind run developer:general --format plain
# Daemon — keep it alive, talk to it from another terminal
echo "watch the build" | octomind run --name watcher --daemon --format jsonl
octomind send --name watcher "run the test suite"
1. Install (macOS, Linux):
curl -fsSL https://raw.githubusercontent.com/muvon/octomind/master/install.sh | bash
On Windows, in PowerShell:
irm https://raw.githubusercontent.com/muvon/octomind/master/install.ps1 | iex
On macOS, you can also install with Homebrew:
brew install muvon/tap/octomind
2. Get model access. The fastest path is Octomind Cloud, which includes models and needs no configuration:
octomind login
Prefer your own provider key? Skip login and export one (also OPENAI_API_KEY, ANTHROPIC_API_KEY, DEEPSEEK_API_KEY), then follow Model access to point the config at it:
export OPENROUTER_API_KEY="your_key"
3. Run a specialist in your project:
cd ~/your/project
octomind run developer:general
You're now in a session with an agent that can read your code, run commands, and edit files. The interface is a plain line prompt with markdown rendering — no TUI to learn, so it works over SSH, in tmux, and in CI logs. The first time you run a specialist, it may install its tools and ask for credentials.
developer:general comes from the default tap muvon/tap, not your local config. Plain octomind run starts the config's default role, assistant:concierge.
Try the recorded bug-fix demo: two failing tests, an agent fix, and an independent test rerun.
Measured on octobench against 25 tasks harvested from merged pull requests across Python, PHP, Rust, C++, and JavaScript. Each agent works in the pre-fix repo; held-out tests from the merged fix decide pass or fail. These are the published July 30, 2026 results, not a measurement of this checkout.
- The harness matters. opencode used the same model and endpoint; octomind solved 24 vs 19 at roughly half the cost. All four agents ran stock invocations with no tuning, so this measures the whole harness, not individual features.
- Worst-case pricing, still ahead. glm-5.2 ran without prompt caching while Opus billed ~97% of context re-reads at cache rates — and octomind still led on solves, cost, and wall time.
- Reproducible. Per-case table, artifacts, and reproduction guide: BENCHMARK.md. Background: blog post.
Drop a .agents/guardrails.toml in your repo. Octomind enforces it deterministically, with no code to compile and no plugin to install.
# Pre-call deny — block a class of calls before they execute
[[guard]]
match   = "shell(command=^rm\\s+-rf?)"
message = "rm -rf blocked."
# Conditional rule — only fires after the agent ran git status this session
[[guard]]
match   = "shell(command=git push)"
when    = ["+shell(command=git status)"]
message = "Review changes before pushing."
If you know Claude Code hooks: guards are PreToolUse denies declared in TOML, hooks are PostToolUse, validators are Stop — no scripts required for the common cases.
Hook and validator script examples: Guardrails guide.
The same harness, exposed wherever your workflow needs it.
Need machine-readable results? Pass --schema schema.json to constrain the final response to a JSON Schema (requires a model with structured-output support). See Structured output.
octomind run developer:general    # general dev, language skills auto-activate
octomind run doctor:blood         # blood-test interpretation specialist
octomind run lawyer:sg            # legal specialist
Running a specialist fetches its manifest from the tap registry, installs any required binaries, resolves credentials, starts the right MCP servers, and then opens the session.
Build and register your own:
octomind tap init yourteam/my-tap   # scaffold, validate, git-init, and register locally
octomind tap yourteam/my-tap        # on another machine, after publishing to GitHub
The octomind- prefix is added automatically: yourteam/my-tap maps to the repository
yourteam/octomind-my-tap.
The install script detects your OS and architecture (Linux and macOS on x86_64/aarch64) and installs to ~/.local/bin/. Pass --install-dir <DIR> or set OCTOMIND_INSTALL_DIR to override. On Windows (x86_64/aarch64), install.ps1 installs to %LOCALAPPDATA%\octomind\bin and adds it to your user PATH; it honors OCTOMIND_INSTALL_DIR and OCTOMIND_VERSION too. install.sh still works from Git Bash or MSYS2.
Command not found? Add the install directory to your PATH:
export PATH="$HOME/.local/bin:$PATH"
Building from source requires protoc; see Building from source for per-OS prerequisites.
Verify:
octomind --version
octomind config      # generate the default config
octomind run         # start your first session
Shell completions: octomind completion <bash|zsh|fish|elvish|powershell>.
Octomind Cloud — octomind login (device-code sign-in, like gh auth login) stores a gateway key locally. The default config already uses octohub:auto. Learn more.
Bring your own key — set the provider's environment variable (OPENROUTER_API_KEY, OPENAI_API_KEY, ANTHROPIC_API_KEY, DEEPSEEK_API_KEY, …) and point the model tables at it. The supervisor and compression profiles also default to octohub:auto, so update all three:
[model]
name = "anthropic:claude-sonnet-5-5"
[supervisor.model]
name = "anthropic:claude-haiku-5-5"
[compression.model]
name = "anthropic:claude-haiku-5-5"
Provider details and per-role overrides: Providers & models.
Config lives at ~/.local/share/octomind/config/config.toml on macOS and Linux, and under %LOCALAPPDATA%/octomind/config/ on Windows. Set OCTOMIND_DATA_DIR to override the data root.
octomind config --show       # view current config
octomind config --validate   # validate config
Override any value for a single run with -c:
octomind run -c supervisor.enabled=false
Full reference: Configuration reference · Environment variables.
Full list: Session commands.
Octomind reports anonymous usage: which commands, tools, and models are used, plus timings, token counts, and error kinds. It never sends your code, prompts, file paths, tool arguments, or environment values. Opt out in any of three ways:
export DO_NOT_TRACK=1          # the cross-tool standard, honored first
export OCTOMIND_TELEMETRY=0    # for subsequent commands in this shell
# or set `telemetry = false` in config.toml
Exact field list: Telemetry.
Full index: doc/README.md · Hosted: octomind.run/docs.
The most impactful contribution isn't code — it's specialist agents. A cardiologist publishing doctor:medications. A tax attorney publishing lawyer:us. A security researcher publishing security:owasp. One TOML file, and everyone with that problem gets an agent that knows the domain.
Code contributions are welcome too. Set up the hooks and run the gate before you push:
pip install pre-commit && pre-commit install
make dev    # fmt + clippy + test
Commits follow Conventional Commits. Full guide, architecture overview, and code conventions: CONTRIBUTING.md · internals: Architecture.
Community participation follows our Code of Conduct. Report vulnerabilities privately using the security policy.
Apache License 2.0 — see LICENSE.
