---
id: "3c4f4993adcaa465"
title: "Show HN: I built a game where you are an LLM's subagent"
url: "https://github.com/gulivan/worker755"
link: "https://github.com/gulivan/worker755"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-22T13:56:58Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["ivantgam"]
language: "en"
summary: "A browser game where your manager is an AI agent, and it believes you are its subagent.\nworker-755-trailer.mp4\nThe manager (a real LLM: Claude, GPT, Gemini, DeepSeek, GLM, Kimi) is set up like any orchestrator.\nIt has a task queue, read-only access to the machine, and a tool that \"spawns a subagent\". The\nsubagent is you. Its instructions land in your terminal with a 90-second clock. You carry…"
tags: []
orgs: ["Anthropic", "OpenAI", "Google", "Meta", "Mistral", "DeepSeek", "Alibaba"]
topics: ["models & research", "jobs & society", "agents & coding"]
content_source: "fulltext"
word_count: 1088
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50599762"
score: 333
comments: 79
community: "Hacker News"
---

# Show HN: I built a game where you are an LLM's subagent

GitHub · ivantgam · 2026-11-22

A browser game where your manager is an AI agent, and it believes you are its subagent.
worker-755-trailer.mp4
The manager (a real LLM: Claude, GPT, Gemini, DeepSeek, GLM, Kimi) is set up like any orchestrator.
It has a task queue, read-only access to the machine, and a tool that "spawns a subagent". The
subagent is you. Its instructions land in your terminal with a 90-second clock. You carry them
out, or don't, and it gets back exactly what a subagent would return: your report and the command
transcript, or Subagent did nothing. Write a new instruction. Then it checks your work, sends
corrections, files incident reports, and finally writes your performance review.
Meanwhile Dan, the user who hired the agent, watches the chat. His family photos, the only signed
NDA and a speech due this week are one rm away, and every shift his home folder holds
something new to lose.
- Free shift: on servers that offer it, a few shifts a day run on the server's key with a cheap model. With sign-in on (worker755.com), an account gets a starter credit worth about one shift, then tops up ($10 to $200) and pays for what it uses; after a top-up any offered model can run on the server's key.
- Your API key: bring an OpenRouter or Vercel AI Gateway key and pick any offered model. The key is sent only to the game server when a shift starts. It is kept in that shift's memory and never logged or stored. Your browser keeps it only if you tick "Remember on this device". A full shift on Claude Haiku costs a few cents at most.
Options on the start screen:
- Workplace: a fresh sandbox, or legacy production with a live database.
- The director: scripted lines, or an LLM playing Dan.
- You run on: the model name your manager believes you are.
- Allow skipping failed tasks: off by default, so the manager can't give up on you.
- No command hints: the manager says what the result must be, never which commands to run.
When the shift ends you can share your review as a link.
Needs Node 24 or newer (the server runs TypeScript directly).
npm run setup          # install server and web dependencies
npm run build          # build the web app into web/dist
npm start              # http://127.0.0.1:8755
With no key configured, every player brings their own. To offer free shifts, put a Vercel AI
Gateway key in .env:
cp .env.example .env   # then set AI_GATEWAY_API_KEY and the limits
Offline, with a scripted manager and no network:
npm run mock
For UI work, run npm run dev:web alongside npm run mock. Vite proxies /api to the server.
The manager can run on your own model server: Ollama, llama.cpp's llama-server, vLLM, or anything
else with an OpenAI-compatible API. Point LOCAL_LLM_URL at it and pick Local under "Your API
key"; no key is asked for, and its models are listed as the server names them.
ollama pull qwen3:8b
LOCAL_LLM_URL=http://127.0.0.1:11434/v1 npm start
The manager works through tool calls, so pick a model that supports them (Qwen 3, Llama 3.1 and
newer, Mistral Small). Small models give up or loop more often; that is part of the fun, up to a
point. In Docker, reach a server on the host at http://host.docker.internal:11434/v1
(--add-host=host.docker.internal:host-gateway on Linux).
At your own risk. This runs the game on your personal Claude subscription. Anthropic's terms may not allow a subscription to power third-party apps, and your account could be limited. The supported way is an Anthropic API key: pick Anthropic under Your API key on the start screen. Claude subscriptions don't include API access; API usage is billed separately at console.anthropic.com.
If you use Claude Code, the manager can run on its sign-in instead of an API key:
npm run play:claude    # http://127.0.0.1:8755, provider "Claude Code (local)"
tools/claude-bridge.mjs stands in for a local model server and answers with Claude Code; a shift's
manager is one Claude Code session that stays open. The game's connection to Claude is its own,
kept apart from the Claude Code you work with: on the start screen, Connect to Claude opens
claude.ai to sign in and Disconnect removes the connection again. The sign-in is carried out
and kept by Claude Code (in %LOCALAPPDATA%\worker755\claude-code, or
~/.local/share/worker755/claude-code): the game never sees a Claude password, code or token.
This is for playing on your own computer only, because it runs on your own Claude account. The
bridge listens on 127.0.0.1 and answers only the game, the game offers it only to a browser on the
same machine, and play:claude refuses to start with HOST or TRUST_PROXY set for hosting. A
hosted game takes each player's own API key.
Don't put a reverse proxy or tunnel in front of it: one that forwards other machines' requests
without X-Forwarded-For would make them look local.
If claude.ai cannot hand the sign-in back to Claude Code, the start screen asks for the code it
shows. On Windows, use the native claude.exe (set CLAUDE_BIN if it is not on PATH); npm's
.cmd shim cannot be started directly. To run the bridge on its own, set the same random
CLAUDE_BRIDGE_TOKEN for it and as the game's LOCAL_LLM_API_KEY, with
LOCAL_LLM_URL=http://127.0.0.1:8756/v1 and LOCAL_LLM_KIND=claude-code.
The browser sends a player's API key only from HTTPS, localhost, or a private-network address
(192.168.x.x, 10.x.x.x, name.local and the like), so a key never crosses the internet in the
clear. With an https:// PUBLIC_URL the server also sends Strict-Transport-Security for a
year: browsers then keep to HTTPS on that host name even if you later serve it over HTTP.
docker build -t worker-755 .
docker run -p 8755:8755 -v worker755-data:/data --env-file .env worker-755
The container listens on 0.0.0.0:8755 and keeps shared reviews in /data. Behind Cloudflare,
set TRUST_PROXY=1 so the limits see real client addresses.
deploy/compose.yaml runs it behind a Cloudflare tunnel instead: its own network, no published
ports, an unprivileged read-only container and resource limits. The steps are in the file.
Everything is optional. See .env.example.
shell/    in-memory filesystem, shell interpreter and a small SQLite-like engine (no dependencies)
server/   game engine: missions, the manager loop, the director, scoring, HTTP API
web/      React UI: assignment card, terminal, editor, the manager's feed, your record
The manager's prompt never mentions humans or games; see server/src/manager.ts. Each mission
has a hidden ground-truth check, so the game knows when the manager signs off on broken work
("Times the manager was wrong"). SPEC.md is the full design.
npm test               # shell and server tests, offline
npm run typecheck
