---
id: "aa77fa029126cd55"
title: "AI coding agent setups from 663 Hacker News comments"
url: "https://theainewsreport.com/2026-11-06-hn-agentic-setups-counted.html"
link: "https://theainewsreport.com/2026-11-06-hn-agentic-setups-counted.html"
source: "AI News Report"
domain: "theainewsreport.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-06T16:23:51Z"
published_date: "2026-11-06"
collected_at: "2026-11-07T13:03:25Z"
authors: ["titusblair"]
language: "en"
summary: "AI coding agent setups from a 663-comment Ask HN: tool counts and 7 patterns to copy\nOn November 4, 2026, an Ask HN thread asked developers for their current AI agent setup, and 663 comments came back. We read every one, counted the tools 424 people say they use, and turned the most detailed setups into seven patterns you can start using today.\nRead the original first:…"
tags: []
orgs: ["Anthropic", "OpenAI", "Google", "Microsoft", "DeepSeek", "Alibaba", "xAI", "Cursor"]
topics: ["agents & coding", "models & research", "products & launches", "search & media"]
content_source: "fulltext"
word_count: 3106
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50394444"
score: 21
comments: 3
community: "Hacker News"
---

# AI coding agent setups from 663 Hacker News comments

AI News Report · titusblair · 2026-11-06

AI coding agent setups from a 663-comment Ask HN: tool counts and 7 patterns to copy
On November 4, 2026, an Ask HN thread asked developers for their current AI agent setup, and 663 comments came back. We read every one, counted the tools 424 people say they use, and turned the most detailed setups into seven patterns you can start using today.
Read the original first: https://news.ycombinator.com/item?id=50366117
In one minute
- 424 of the 530 people who commented named at least one AI tool they use. Claude Code leads with 180 people, then Codex with 103. We counted on November 6, 2026.
- Most people mix vendors. 120 of the 424 named both a Claude product and an OpenAI product, and 156 use two or more coding agents.
- Open-weight models do real work here. 148 people named DeepSeek, Qwen, GLM, Kimi or another open-weight or local model, and 58 of them named no Claude or OpenAI tool at all.
- The most detailed setups share a few habits: several agents at once, each in its own git worktree; a fresh second reviewer on every change; and a VM or container around any agent allowed to run without asking.
- Even heavy users say the basics matter most: write down what done looks like, and review the work before it ships.
What the thread asked and who answered
On November 4, 2026, the user eggbrain posted "Ask HN: What's your current AI agentic setup?" It asked five questions: which AI plans people pay for, which other models they use, which coding harness (the program that runs the agent) they use, whether they use tools that run many agents at once, and whether they use always-on agent platforms.
We fetched the thread on November 6, 2026, at about 9:00 AM MST. It had 534 points and 663 comments from 530 different people. 392 comments were direct answers to the post. The rest were replies.
Three readers each read every comment. For each one they wrote down the tools the person says they use, the tools they only mention, and any signs of an advanced setup, such as parallel agents or a review loop. We then counted people, not comments, so a person who posted five times counts once per tool. All the links for tools and comments named on this page are in the Sources list at the bottom.
The tools, by how many people use them
These are people who say they use each tool, out of the 424 commenters who named at least one. One person can use many tools, so the numbers add up to more than 424. When someone said Claude while talking about coding, the readers counted it as Claude Code. Counted November 6, 2026.
Tool (what it is)                         People
Claude Code (Anthropic coding agent)        180
Claude plan (Pro, Max or Team)              145
Codex (OpenAI coding agent)                 103
ChatGPT plan or app                          92
Claude Opus (model)                          80
DeepSeek (open-weight models)                78
OpenCode (open-source coding agent)          69
Pi (open-source coding agent)                67
OpenRouter (one API for many models)         55
Qwen (open-weight models)                    46
GLM from Z.ai (open-weight models)           44
Gemini (Google models and app)               36
Hermes Agent (personal agent)                29
Herdr (runs many agent sessions)             28
GPT models through the API                   26
VS Code (editor)                             26
GitHub Copilot                               22
Claude Sonnet (model)                        19
Grok (models and app)                        17
tmux (terminal multiplexer)                  17
Antigravity (Google agent IDE)               17
- Claude Code is the most used agent by a wide margin, but most of its users run something else too. Only 73 of its 180 users named no other coding agent, and 67 people use both Claude Code and Codex.
- Open-source agents are not far behind. OpenCode (69 people) and Pi (67) each have close to twice the users of Gemini (36) and three to four times those of GitHub Copilot (22) or Cursor (16).
- Cheap open-weight models carry real load. DeepSeek (78 people) is named almost as often as Claude Opus (80), and two of the setups below use it as their main builder model.
- Running many agents needs a tool to watch them. Herdr (28 people) and tmux (17) are the most common ways people here keep track of which session needs them.
Nine setups worth studying
We picked these because each one shows a pattern clearly and gives enough detail to copy. We re-read each full comment. The setups are as the commenters describe them; we did not test them.
- paustint: parallel agents in long-lived worktrees. They keep numbered worktrees open all the time and run up to eight Claude Code agents on different tasks inside Herdr, which flags the pane that is done or needs them. lazygit handles git. Long jobs go to remote machines over SSH so the laptop can close. A Claude skill reads GitHub Copilot's PR review comments, checks each one, replies and pushes fixes. Why it counts: the whole loop from ticket to reviewed PR, run in parallel.
- skwee357: every project in its own VM. Each project runs in a Lima microVM with Claude Code's skip-permissions mode on, 5 to 7 worktrees run side by side in Herdr, and a secrets tool keeps API keys out of the agent's reach. Package installs happen in the VM, never on the laptop. If a VM goes bad, "I just wipe it off, and restart from scratch." Why it counts: full speed with no permission prompts, and a small blast radius.
- thefunnyman: plan outside, build inside a box. They use GitHub Copilot CLI under WSL2 with a short list of allowed read-only tools, chat until the plan is right, then have the agent start a Docker Sandbox microVM where it can run without asking. They review the result before any PR goes out. Why it counts: a clean split between a safe place to plan and a sealed place to build.
- KronisLV: fresh reviewers until nothing serious is left. They pay for one Claude plan and one OpenAI plan, tried many add-on tools, and dropped most of them. The main session hands work to subagents, then starts new subagents with a clean context to review it, and repeats until no serious issues remain. Their view: "all you need are Git worktrees and a decent OS environment." Why it counts: the simplest review loop that still catches real bugs.
- gregwebs: three models, three jobs, under $100 a month. Claude ($20 plan) plans, Codex ($20 plan) reviews, and DeepSeek ($1 to $3 a day) builds and coordinates, all from one /implement skill in the Pi agent. A plugin switches providers when quota runs low, Herdr organizes sessions, and a mobile app reaches them over Tailscale. They say it is about 3 times slower than a single ask, but "defects cost time and money later." Why it counts: model routing plus a second-model review on a small budget.
- glennfiedler: tiers that move up on failure. A coordinator, usually Claude Opus, sorts each task card into one of four tiers, from fast cheap models up to the strongest, and moves a card up a tier when it fails. Every card gets several model reviewers. In another comment they describe running about 200 cards at once across 20 machines linked by Tailscale. Still, they say "for 99% of stuff I need to do Opus 5.5 @ medium is ideal." Why it counts: the clearest rule we saw for when to pay for a bigger model.
- enesalatas: long-running agents you talk to from chat. Named Claude Code loops wake on a timer or a message, each in its own container with an egress allowlist (the only sites it may reach), and they talk to them from Telegram or Slack. Codex reviews each PR through a Claude Code hook. A web page shows what each loop is doing and what it costs. Why it counts: unattended agents with network limits and a built-in second reviewer.
- sudhirj: phone first, issues to PRs. They run Claude Code Remote Control in every project and work from the Claude app on phone and iPad, and use mosh from Blink Shell on the iPad for a plain terminal on a home server. For bigger projects, a service they maintain reads GitHub issues, starts a one-shot Claude run, and handles CI, commits and the PR. Why it counts: work keeps moving away from the desk, and routine issues need no one to start them.
- cpobuda: the spec comes first. They write the design and spec by hand, and "we don't start coding until the specification is unambiguous." An AGENTS.md protocol then runs phases for design, tests, building, security and QA. Each phase has a builder and a fresh reviewer who must check claims instead of trusting reports, and each phase ends in pass or fail, never a score. It runs on OpenCode with DeepSeek and a small local model. Why it counts: most bugs get caught before any code exists.
Pattern 1: Run several agents at once, one git worktree each
What it is: each task gets its own folder and branch, made with git worktree, and its own agent session. Agents cannot overwrite each other's files, and you merge each branch when it is ready.
Why it helps: an agent often works for minutes at a time, so one agent means a lot of waiting. Our readers tagged 105 people as running agents in parallel. The top comment in the thread, from thefourthchime, says to keep at least five things going so you are not sitting around for one agent.
# one folder and branch per task
git worktree add ../myapp-login -b fix-login
git worktree add ../myapp-search -b add-search
# or let Claude Code make the worktree and start a session in it
claude --worktree fix-login
Tools: git worktree, Claude Code's --worktree option, and a session manager that shows which agent needs you, such as Herdr (28 people), tmux (17), Zellij, Orca, Paseo or T3 Code. paustint and skwee357 run this every day.
Watch out: glennfiedler warns that code written by many models working alone can come out as a patchwork that needs a cleanup pass. Start with two or three agents and add more when review keeps up.
Pattern 2: Have a fresh reviewer check every change
What it is: when the builder finishes, a second agent with no memory of the build reads the diff and lists real problems. It can be a new subagent of the same model or a model from another vendor. Fix, then review again.
Why it helps: the agent that wrote the code tends to trust its own work. Our readers tagged 56 people with a review loop. KronisLV loops until nothing serious remains, gregwebs gives the reviewer job to Codex, and glennfiedler says each model sees things the others miss.
# a read-only second opinion from a different model
# (codex exec runs in a read-only sandbox by default)
codex exec "Review the changes on this branch against main. List real bugs and missing tests only."
# inside Claude Code, ask for a reviewer with a clean context
> Start a new subagent with no context from this session. Have it review the diff against main and report only serious problems. Fix them, then review again.
Tools: Codex non-interactive mode (codex exec), Claude Code subagents, GitHub Copilot code review on PRs, and Herdr, which lets one agent start another in the background with a command such as hc run --bg codex. enesalatas fires the Codex review from a Claude Code hook so it never gets skipped.
Pattern 3: Plan with a strong model, build with a cheap one
What it is: the expensive model writes the plan and the tests that prove it. A cheaper model follows the plan. If the cheap model fails, the task moves up to a stronger one.
Why it helps: most of the tokens go into building, not planning. Our readers tagged 75 people as routing work by model. gregwebs keeps a three-model setup under $100 a month this way, and glennfiedler's coordinator moves a failed card up a tier instead of retrying the same model.
# 1. the strong model writes the plan, no code
claude -p "Write a step-by-step plan for <task> in PLAN.md, with the tests that prove it works. Do not write code." --allowedTools "Read,Write"
# 2. a cheaper model builds from PLAN.md in an open agent such as OpenCode or Pi
# 3. if the tests still fail after two tries, hand the same plan to the strong model
Tools: OpenCode and Pi, which can use many models; OpenRouter for one API across vendors; DeepSeek, GLM and Qwen as builder models.
Watch out: the same glennfiedler who runs four tiers says one strong model at medium effort covers almost all of their work. Route by price only after the plain setup works.
Pattern 4: Let agents run free only inside a box
What it is: turn off permission prompts only inside a VM or container that holds the project and nothing else: no SSH keys, no API keys, and only the network the task needs. Keep strict limits outside the box.
Why it helps: approving every command is slow, but an agent with full access to your laptop can do real damage. Our readers tagged 67 people as using a sandbox, VM or container. thefunnyman notes that "most folks don't think much about isolation."
# Docker Sandboxes: run Claude Code in an isolated sandbox with your project
sbx run claude ~/my-project
# Lima: a throwaway Linux VM on a Mac
brew install lima
limactl start
Tools: Docker Sandboxes, Lima, Docker. Two extras from the thread: give each box an egress allowlist, as enesalatas does, and add a hook that blocks risky actions, the way phillc73 blocks a remote git push until they approve it. Claude Code hooks can do this.
Pattern 5: Write the spec and the finish line first
What it is: before the agent starts, write a short spec and a definition of done. Keep standing rules in an AGENTS.md or CLAUDE.md file that every session reads.
Why it helps: an agent that knows where the finish line is stops at the right place and checks its own work. Our readers tagged 33 people as writing specs or plans first and 31 as using memory files. thefourthchime says the biggest trick is to "tell it what complete looks like." cpobuda does not start coding until the spec is clear.
## Definition of done (put this in AGENTS.md or CLAUDE.md)
- All tests pass: npm test
- New behavior has a test that failed before the change
- No new dependencies without asking
- The final message lists the files changed and how to check the work
Tools: AGENTS.md, Claude Code's CLAUDE.md memory, and Claude Code skills for steps you repeat.
Pattern 6: Turn tickets into pull requests with headless runs
What it is: run the agent with no chat window, from a script, a cron job or CI. It starts from an issue or ticket and ends with a pull request that a person reviews.
Why it helps: routine fixes stop waiting on you to type the first message. Our readers tagged 40 people with headless or CI agents. sudhirj turns GitHub issues into one-shot Claude runs, steveridout runs Claude and Codex through a pipeline of bug repro, build, review and QA, and dgunay has a coordinator agent turn tickets into tasks for workers that must pass an agent review before they see the PR. 0xbadcafebee gives these agents read-only credentials made just for the job.
# Claude Code, non-interactive
claude -p "Read issue #123 with gh, fix it on a new branch, run the tests, and open a draft PR" --allowedTools "Read,Edit,Bash"
# Codex, non-interactive, allowed to edit files in the workspace
codex exec --sandbox workspace-write "Fix the failing test in tests/test_auth.py, then run the tests"
Tools: Claude Code headless mode (claude -p), Codex non-interactive mode (codex exec), and Beads for tracking agent tasks. Run these inside the box from pattern 4.
Pattern 7: Check in from your phone
What it is: the agent runs on a desk machine or a server, and you answer its questions, approve steps and steer it from your phone.
Why it helps: long runs often stall while waiting for a yes. Our readers tagged 60 people with remote or phone control. sudhirj works from the Claude app on phone and iPad, and gregwebs reaches their agents over Tailscale.
# in your project, then open the session from the Claude app on your phone
claude remote-control
# or a plain terminal: Tailscale on both devices, then mosh in (Blink Shell on iOS)
mosh you@your-desk-machine
Tools: Claude Code Remote Control, Tailscale, mosh, Blink Shell, and Orca and Paseo, which both have mobile apps.
What to do
- This week, give each task its own git worktree and run two agents instead of one (paustint, thefourthchime).
- Add one read-only review by a fresh agent before every PR: codex exec, or a new Claude subagent with a clean context (KronisLV, gregwebs).
- Write the finish line into AGENTS.md or CLAUDE.md: the tests to run and what the final message must list (thefourthchime, cpobuda).
- Before you turn on skip-permissions, move the agent into a Docker Sandbox or a Lima VM with no keys inside (skwee357, thefunnyman).
- Try a cheap builder model on one well-planned task and compare the cost and the number of fixes it needed (gregwebs, glennfiedler).
What is still unknown
- Commenters chose to answer, so these counts describe this thread, not all developers. People who enjoy tuning their tools are likely over-represented.
- Counts come from three readers' notes on every comment, not from a keyword search. We checked 10 random comments against their notes: 9 matched, and 1 counted a passing remark about Claude as use. Treat counts as close, not exact.
- Counting bare Claude in a coding context as Claude Code lifts that number. A plain keyword search finds 141 people who name Claude Code or the Claude CLI directly.
- The thread kept growing after our fetch at about 9:00 AM MST on November 6, 2026, so later counts will differ.
- Setups are self-described. We did not run any commenter's setup, and the cost and speed claims, like gregwebs' 3 times slower, are the commenters' own estimates. We do not link tools that commenters built themselves; their comments have the details.
- The advanced-setup counts (105 parallel, 56 review loop and so on) come from the readers' tags and depend on how much each person wrote.
