---
id: "71dec3d3a2e59a08"
title: "Why Claude Code can cost you 2x to 10x of usage limits"
url: "https://github.com/inevolin/claude-code-usage-analysis"
link: "https://github.com/inevolin/claude-code-usage-analysis"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-11-17T11:30:39Z"
published_date: "2026-11-17"
collected_at: "2026-11-17T13:04:11Z"
authors: ["ilya47"]
language: "en"
summary: "I spent time investigating and optimising my Claude Code token usage, here’s the most important anti-patterns avoid and best-practices to follow. Enjoy!"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["models & research", "products & launches", "agents & coding"]
content_source: "fulltext"
word_count: 3832
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xyi3xo/why_claude_code_can_cost_you_2x_to_10x_of_usage/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Why Claude Code can cost you 2x to 10x of usage limits

GitHub · ilya47 · 2026-11-17

Claude Code usage is driven by cache misses, not by how much you type. The expensive habits are ways of throwing that cache away.
Everyone uses Claude Code differently. The best settings for you depend on your own logs. Paste the text below into Claude Code to check your habits once:
Everyone uses Claude Code differently. Recommend settings that fit MY logs, not general advice.
1. Clone https://github.com/inevolin/claude-code-usage-analysis into a temp folder, then run:
   python3 -m pip install -e .
   OUT=$(mktemp -d)
   python3 -m cc_usage_study.analyze ~/.claude/projects --summary --sessions --calls -o "$OUT/report.json"
   Keep that report file outside any git repo. Use only that file: summary numbers, timestamps, token counts, entrypoints, and compact_boundary fields. Do not read, paste, or upload the raw text of my chats. Do not report money amounts. Use % and multipliers.
2. Score my habits with my own numbers:
   - Continuing a session after the cache expired: use cache_rebuilds_main.ttl_expired_rebuild (a gap over 5 minutes if cache_creation_5m_tokens are most of the writes, or over 1 hour if cache_creation_1h_tokens are).
   - /compact after a break, or before: compare boundary_rows timestamps and trigger with gaps in call_rows.
   - Many short sessions close together (a rough sign of /clear between related work) instead of one continued session.
   - sdk-cli (claude -p) sessions continued across gaps, instead of a new session each run.
   - Which app I used, from by_entrypoint: cli = Claude Code CLI, sdk-cli = claude -p, t3-code = T3 Code, claude-desktop-3p = Desktop Code tab. Prefer the CLI, or T3 Code. Desktop's Code tab used at least 1.80 times the CLI in this study. The Claude chat app was not measured.
   - Sessions where one request reaches 300,000 tokens: use one call's prompt_tokens or compact pre_tokens. Do not use the session-sum of prompt_tokens.
3. Write a short report:
   (a) the 3 habits costing me the most, with my % or multipliers;
   (b) changes that fit my pattern, only from this list: /compact before breaks, /clear plus a 3-line reminder when I am already back, a new `claude -p` session each scheduled run, prefer the CLI or T3 Code over Desktop's Code tab. Mention `--autocompact` only as an unproven idea, and only if my sessions actually get that large;
   (c) what you could not tell. If a field is missing, compute it from timestamps and compact_boundary metadata only, or say you cannot tell.
This runs on your computer, on the files in ~/.claude/projects. The prompt tells Claude to use summary numbers and timestamps, not the raw text of your chats. The only thing that leaves your machine is the normal Claude Code conversation. That conversation will include those summary numbers.
Or install the skill, then type /claude-code-usage-check in a new session:
mkdir -p ~/.claude/skills
cp -R skills/claude-code-usage-check ~/.claude/skills/
To run only the analyzer yourself: python3 -m cc_usage_study.analyze ~/.claude/projects --summary --sessions --calls -o ./local-out/report.json. Keep the report file outside git. The tool never copies the text of your prompts.
- Our calculation says --autocompact 180000 uses about 43% less. In a live test on a 270,000-token session, it only tied the default. We ran that test once, with no long pauses. (details)
- We do not yet know the best compact settings for very long sessions. Our calculation failed when we checked it against the live tests. (details)
- Editing CLAUDE.md, adding an MCP server, or changing effort between turns did not break the cache. The next turn used about the same as a normal turn (0.95x to 1.08x on average). (3 runs each, Claude Code 2.1.325) (details)
- Fewer raw tokens is not the same as less usage. One setting sent 63% fewer raw tokens than the default, and used 25.2% more. (details)
A "break" means you were away longer than the prompt cache. That cache lasts 5 minutes if you use an API key or usage credits, and 1 hour if you use a subscription within its usage limits. We measured pauses of 2 to 13 minutes on the 5-minute cache. (does this apply to you?)
Three habits that avoid paying for a cache rebuild. Paste them into your terminal or Claude Code prompt and edit the details.
- Scheduled runs (cron, CI): start a fresh claude -p session every run and pass state in through a notes file, instead of resuming an old session.
- Before a break: run /compact and tell it what to keep, so the session is small when you return.
- Back from a break on a new task: run /clear, then give a 3-line reminder (Goal, Done, Next).
# Cron and CI: start a new session every run, and keep notes in a file
claude -p "$(cat .agent/handoff.md) Continue the nightly triage." --output-format json# Before a break
/compact Keep: the open issue, files touched, test command
# Back after a break, new task
/clear
Goal: fix the currency rounding in invoices.
Done: tests in tests/test_invoice.py reproduce it.
Next: patch money.py, run the suite.
Careful with CLAUDE_AUTOCOMPACT_PCT_OVERRIDE. On a 1M-context model, 25 fires at about 245,000 tokens, which is reasonable. On a 200k-context model it fires at 45,000, below what a summary leaves behind, and the session thrashes (+239% in our model). In T3 Code it stacks with "Auto-compact after", so set only one of the two. (details)
T3 Code can compact before a break for you. Its idle-thread setting has three modes: "When you return" (the default, onReturn), "Before the cache expires" (beta, beforeCacheExpires), and "Never". "When you return" compacts after the cache has already expired, so you pay the rebuild anyway. "Before the cache expires" compacts an idle thread while the cache is still warm, which is the automatic version of /compact before a break. Not measured in this study yet.
This is the data behind the rules above. You do not need to read it to use the rules.
Methods in brief. All live runs used Claude Opus 5.5, effort medium, Claude Code 2.1.325, and the default 5-minute prompt cache, on a dedicated API key. "Usage" is cache-weighted units (1 / 1.25 / 2 / 0.05 / 5): input 1, 5-minute write 1.25, 1-hour write 2, read 0.05, output 5. That is list price divided by the Opus 5.5 input price. We report the mean and the min-to-max range. Findings with n under 3 are marked preliminary. The analyzer never copies prompt text.
The chart below is the main result. Usage of the same class of small fix, on a session of about 97,000 tokens of history, stays near 1.5 times a new session while the cache is warm. After the 5-minute cache expires, it jumps to about 10 times. The jump is a cache miss: the first request after a long pause writes the history again, instead of reading it cheaply.
All 5 continues inside the window used 1.49x to 1.52x (mean 1.51x). All 5 continues after expiry used 9.76x to 9.92x (mean 9.83x).
Each later continue is scored against a new session that ran the same fix (median, slice, or currency rounding). Those new sessions used 12,396 to 12,843 units (mean 12,571, n=3). The first request after a pause tells the same story in a different way: inside the window, it read 96,000 or more tokens from the cache and wrote only a few hundred. After the window, it wrote 86,000 or more and read only a short prefix.
Two runs with almost the same raw token count (about 294,000) differed 6.5x in usage. The warm continue mostly read the history. The stale continue had to write it again.
The multiplier scales with history size. At 97,000 tokens it is about 10x for a small next fix. A smaller session would jump less; a larger one would jump more. A 1-hour subscription cache would move the cliff, not remove it. (does this apply to you?)
Scheduled claude -p jobs that use --resume across a gap longer than the cache are the same mechanism. The estimate is about 3x compared with a new session each run. That estimate was not tested live.
/compact only helps if it runs while the cache is still warm. Then the summary is written cheaply, and the history you carry across the break is short.
Baseline: the same three new-session fixes (mean 12,571 units). Compact after a break does not beat just continuing the stale session (9.87x, n=3).
Yes, if you use an API key or usage credits: the cache lasts 5 minutes, which is what we measured.
If you use a Pro, Max, or Ultra subscription, and you stay within the five-hour and weekly limits, the cache lasts 1 hour. The same miss is more expensive per token (a 1-hour cache write costs 2 times a plain input, not 1.25 times). You have more time before it happens. We did not measure the 1-hour cache live. At the 97,000-token history we used, the adjusted calculation says a miss past the hour is 11.0 times a new session (the 5-minute miss was 9.8 times).
claude -p and a sleeping laptop do not keep a process alive, so idle compact (which can summarize a large session before a 1-hour cache expires) does not run. A normal interactive session can, if the window stays open and idle compact is on.
This section checks our calculations against the live tests.
The estimated rules (scheduled jobs, pause traps, long-session compact settings) come from the simulator. python3 -m cc_usage_study.validate scores it against every live run, with no API calls, in two versions. The original numbers are the ones used in this README. The adjusted version learns the task shape (calls per task, tokens per call, and the starting instructions already saved from earlier sessions) from the 3 new /clear sessions only.
Each run has a role. The new sessions are used to tune the adjusted calculation. The warm and stale continues are held-out checks: the adjusted calculation sees only the new sessions and the history size. The /compact runs are not held-out checks. They use each run's own summary size and post-compact prompt.
- The cache math matches the continues. All 4 continue runs in this check land within 3% with the adjusted shape. With the original numbers, none of the 4 were close (all were off by more than a quarter). This is still a weak test: 4 runs from one 97,000-token session. A stale continue is mostly one rewrite of the cold history, which any sound cache model gets right. The six later dose-response continues were not part of this check. They used the same new-session baselines and landed in the same two bands (1.49x to 1.52x inside the window, 9.76x to 9.92x after it).
- The original task shape is the problem. The original numbers put a new session at 4.5 times the measured cost. Most of that is the task shape: 5 calls with 2,000-token tails and 600 output tokens each, where the live fix took 3 calls with far smaller turns (fixing that alone leaves 2.1 times). The starting instructions already saved from earlier sessions (about 11,400 tokens) are the smaller part (fixing that alone leaves 3.4 times).
- What that changes (estimate; only 97,000 tokens was measured). The break-even point barely moves, but estimated continue penalties above it look too low. At 30,000 tokens of history, a stale continue costs +96% compared with /clear plus 2 exploration calls, not the original +41%. At 60,000 tokens, it is +245%, not +102%. The break-even history barely moves (10,100 to 10,800 on the 5-minute cache, 8,300 to 8,700 on the 1-hour cache).
- /compact after a break sent the cold history as plain input (1 times), not as a cache write (1.25 times), which is what the simulator assumes. That was read from these same runs.
- The long-session compact calculation fails when we checked it against the live tests. We replayed the migration task from the default setting's measured path. The calculation gets the direction right on 2 of 4 trigger settings, and lands within 5 points on 1. It predicts -0.9% for --autocompact 140000, where the live run measured +18.1%. It predicts +51.7% with 14 compacts for the stacked setting, where the live run measured +13.6% with 6. It prices a summary call at 21,600 units, against a measured 36,600 per compact. Real context growth is uneven (1 to 14 calls between compacts in one setting), so even growth places compacts in the wrong spots. Fitting summary size and extra calls on the same settings made it worse. Treat the settings section below as an idea to test, not as a result.
Full scores per run: outputs/validation.json.
Shrinking history mid-session is not always cheaper, and some of the usage is hidden.
Every setting ran the same task: a 24-module migration over 4 --resume phases. Opus 5.5, effort medium, 5-minute cache, no long pauses, n=1 per setting, preliminary. Slate is what the log shows. Orange is summary traffic that only appears in Claude Code's own cost_state total.
- Fewer tokens is not less usage. The 100,000 setting sent 63% fewer raw tokens (2.27 million compared with 6.12 million) and used 25.2% more. Most of the default's tokens were cheap cache reads.
- Part of the usage is invisible. Summary calls were 11.8% to 25.5% of each compacting setting, about 36,600 units per compact on average.
- The ranking depends on the read weight. At 0.1x reads, the 180,000 setting comes out 13.6% under the default. The tie also assumes no pauses. One pause past the cache, at about 260,000 tokens of history, would add roughly 39% to the default setting (estimate).
- Quality held everywhere: all 5 settings passed the tests and the functional checker, and reported 12 of 12 planted anomalies.
Per-setting table
The order is not a smooth line at n=1 (57,500 beat 107,000 and 67,000). So "a lower trigger pays past a break-even length" is a claim from the calculation, not from this table.
For a few quick, related fixes, staying in the session used less than starting over each time.
Three quick fixes, one after another, n=1, preliminary. Three new sessions compared with one session continued inside the cache time limit. The continued session read 7.0% more raw tokens but rebuilt 53% fewer, so it used 27.7% less (21.1% to 32.0% by model). Context peaked at 20,265 tokens. This only holds while history is small.
The same fix in the Claude Code CLI, T3 Code, and Claude Desktop's Code tab.
Same Opus 5.5, effort medium, identical 3-line CLAUDE.md, no user MCP servers, n=1 per client, preliminary. All three fixed all 3 planted bugs.
T3 Code runs Claude Code through the Agent SDK and adds 67 deferred tools plus a longer system prompt. Desktop's Code tab carries a whole app (35 inline tools, 3.5 times the system prompt) and writes no cost_state row, so its number is at least 1.80 times the CLI. We did not measure the Claude chat app. Full table: benchmarks/client_comparison.md.
The number you type is not the point where compact actually runs.
Read from the Claude Code v2.1.325 binary. The number you type is not where it fires: subtract 33,000, and never stack two knobs. The first live compact fired 0.3% to 55.5% past the formula's threshold. The check runs between requests, and one large tool result can carry the context well past it.
effective_window = window - min(maxOutputTokens, 20000)
threshold        = effective_window - 13000                                    # no override
threshold        = min(floor(effective_window * pct / 100), effective_window - 13000)   # with CLAUDE_AUTOCOMPACT_PCT_OVERRIDE
Idle compact summarizes a big session at about 90% of the cache time limit, before the cache expires. It only runs when all of these hold: idleCompaction is on (default since v2.1.299), the session is on the 1-hour cache (never on API keys), the process is still alive (not a sleeping laptop or a finished claude -p), and context is at least CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS (200,000 by default, 100,000 at the lowest). --autocompact 180000 keeps you under 200,000, so pair it with CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS=100000 if you take long breaks with the terminal open.
This section is a set of ideas to test, not a result. The compact calculation failed when we checked it against the live tests (see the check above), so do not treat these as savings.
The main idea: for a long session headed past 300,000 tokens, claude --autocompact 180000 is estimated at about 43% less. Live, it tied the default on a 270,000-token session (n=1, no pauses). If you try it and take long breaks with the terminal open, pair it with CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS=100000.
Workflow and pause-trap tables (estimate, original numbers)
A long test log costs you after Claude has read it, because it stays in the chat.
A new session runs a failing test suite once and reports the result in one line. Then it answers 5 short questions with no tools, a few seconds apart, so the cache stays warm. Only the test output changes: a 1-line summary (48 tokens), a normal failing pytest log (803 tokens), or a long log with tracebacks and captured logs (8,602 tokens). Claude Code cut the long log to about 10,000 characters before it went into the chat. Opus 5.5, n=2 per arm, preliminary, about 17,000 tokens of context. Every run named the same 3 failing tests.
The log is written to the cache once, then read again on every later turn. Part of the gap in the next 5 turns is longer answers after a long log. Without output tokens the gap is 1.08x and 1.29x. These sessions were small, so the log is a large share of each turn. In a bigger session the share is smaller, but the extra tokens per turn stay the same. After a break the cache expires, and the log is written to the cache again with the rest of the chat.
This section checks whether changing settings between turns throws the cache away.
Switching models: from Anthropic's docs, not measured. The Claude Code docs say each model has its own cache. After /model, the next request reads the whole chat with no cache hits. Our live runs use only Opus 5.5, so we did not test it.
The closest test on Opus 5.5: turning off one tool. We turned off one built-in tool (--disallowedTools Edit) between turns. That changes the tool list at the very start of the prompt, so nothing after it matches the cache. This is the same effect the docs describe for a model switch. The next turn read 0% from the cache, wrote about 43,700 tokens again, and used 22x a normal turn (21.8x to 22.2x, n=2, preliminary).
Changing effort did not break the cache. Medium to high: 0.98x of a normal turn. High back to medium: 0.95x. 99.7% or more was read from the cache (n=3). The docs say Opus 5.5 keeps the cache when effort changes. On many older models it does not.
Each session read 2 log files (about 44,000 tokens of context), then answered one short question per turn with no tools. Each turn was a new claude -p --resume run a few seconds after the last one. One thing changed before each test turn. Control turns changed nothing. Each change is compared with the average of the control turns in the same session.
Claude Code 2.1.325 did not change the start of the prompt for a CLAUDE.md edit or a new MCP server. It added the new CLAUDE.md at the end of the chat as a note that the instructions changed. It listed the new MCP tool at the end as a deferred tool (tool search). So the rest of the chat still matched the cache. An edit to CLAUDE.md only reaches Claude after a restart, /clear, or /compact (docs). We tested the restart case: --resume in a new process. The docs say that with tool search turned off, adding an MCP server does break the cache. We did not test that. n=3 per change, one session size, Opus 5.5.
This section lists what this study cannot claim.
- Small n. The cache-expiry curve is the best-supported result, and even there each pause length has only a few runs. Many other settings were tested once (n=1). Findings with n under 3 are marked preliminary. We report min-to-max ranges, not confidence intervals, except where n is large enough to say otherwise.
- Small sessions for some tests. The tool-output and between-turn tests used about 17,000 and 44,000 tokens of context, with a warm cache.
- One model, small tasks, one cache time limit. All live runs used Opus 5.5 on the 5-minute cache. 1-hour cache numbers are estimates.
- The cache-expiry runs used claude -p --resume, not an interactive terminal. The cache rule is the same. An open terminal can also run idle compact on a 1-hour cache, which these runs do not.
- Ratios compared with a small fix look larger. The 10 times figure is compared with a 3-call fix. The extra cost per carried token is the number that still holds for a bigger next task.
- These units are not your subscription bill. Units follow API list prices. Subscription limits use weights Anthropic does not publish.
- The compact calculation failed when checked against the live tests. See the check above.
- The short-task check is narrow. 4 held-out checks from one session, one history size, and one model. It shows the cache math is right. It does not show that every estimated number is right.
- Two of the five compact settings fail the repo's own validity check.
More on method and open questions: FINDINGS.md.
These commands rebuild the study on your machine.
python3 -m pip install -e ".[dev]"
python3 -m cc_usage_study.pipeline        # analyze, check, simulate, figures, validate, verify; one command
python3 -m pytest -q
Run the analyzer on your own logs, and keep the output outside git:
python3 -m cc_usage_study.pipeline --projects ~/.claude/projects --split-date YYYY-MM-DD --out ./local-out
The analyzer copies summary numbers only, never prompt text. Read preTokens on your first compact_boundary. If it does not match the table in where compaction actually fires, your setting is not the one you think.
Setup and what's inside
- Clients: Claude CLI v2.1.325, T3 Code v0.1.9 (Agent SDK wrapping Claude Code v2.1.325), Claude Desktop v5.1231.2 (Code tab, bundled Claude Code v2.1.321).
- Model claude-opus-5-5, effort medium, 1M context, maxOutputTokens 128,000.
- Cache-weighted units are the logged list-price cost divided by the Opus 5.5 input price. Pricing snapshot 13 November 2026, pricing page.
- "Hidden" usage is cost_state.totalCostUSD minus the deduplicated assistant rows in the same transcript.
- Prompt caching in Claude Code: which requests get the 5-minute or 1-hour cache, and how to choose it
- Prompt caching on the API: cache lifetime, 1-hour cache, write and read multipliers (pricing)
- Manage costs in Claude Code and context window
- Commands: /compact, /clear, /usage
- Claude Code with a Pro, Max or Ultra plan (five-hour and weekly limits) and usage limit best practices
- API rate limits
Live experiments ran on Claude Opus 5.5. Writing and analysis were AI-assisted, and then edited.
MIT. See LICENSE.
