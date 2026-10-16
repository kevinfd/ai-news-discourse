---
id: "6b75dae75d979d91"
title: "Talorys – A self-hosted personal AI agent on Cloudflare's free tier"
url: "https://github.com/rociiu/talorys"
link: "https://github.com/rociiu/talorys"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-10T10:52:09Z"
published_date: "2026-10-10"
collected_at: "2026-10-13T20:17:27Z"
authors: ["rociiu"]
language: "en"
summary: "Your personal AI agent. Your own cloud.\nTalorys is a free, open-source personal AI assistant that runs entirely inside your own Cloudflare account. It chats with you, remembers what matters, manages tasks, notes and projects, and runs reminders and routines on a schedule — without any server, database or account operated by the Talorys developers.\nOne person. One Cloudflare account. One command.…"
tags: []
orgs: []
topics: ["jobs & society", "agents & coding", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 1417
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50031614"
score: 328
comments: 155
community: "Hacker News"
---

# Talorys – A self-hosted personal AI agent on Cloudflare's free tier

GitHub · rociiu · 2026-10-10

Your personal AI agent. Your own cloud.
Talorys is a free, open-source personal AI assistant that runs entirely inside your own Cloudflare account. It chats with you, remembers what matters, manages tasks, notes and projects, and runs reminders and routines on a schedule — without any server, database or account operated by the Talorys developers.
One person. One Cloudflare account. One command. One personal AI agent.
npx create-talorys@latest
- A private assistant — chat with streaming responses, Markdown and tool activity indicators.
- Memory — durable personal facts and preferences you can view, edit and delete. Only the most relevant memories are sent to the model on each turn.
- Semantic recall (optional) — finds memories by meaning as well as keyword, and lists them newest first with their saved date. Off by default; turn it on with the Semantic memory recall switch near the bottom of Settings → AI (its other settings appear once it is on), or install with --semantic. See docs/semantic-recall.md.
- Memory history — facts that change over time: when you say you sold your car, the old one is kept as a past fact instead of being treated as current, and unclear conflicts wait for your review. See docs/memory-history.md.
- Tasks, notes and projects — full CRUD in the UI, and from chat ("Add a task to review my project tomorrow").
- Automations — one-time and recurring reminders, daily task digests and optional AI routines, delivered to an in-app notification center. They run on Durable Object alarms, so nothing has to stay online.
- Single-user by design — no signup, no accounts, no teams. The installer sets the owner password.
- Works without AI — tasks, notes, memories and reminders keep working if Workers AI is unavailable or your free quota is used up.
Browser ──HTTPS──▶ Cloudflare Pages (React app + /api Pages Function)
                         │  service binding (no public URL)
                         ▼
                   Private Worker (Hono router)
                         │  getAgentByName("personal-agent")
                         ▼
                   TalorysAgent — Cloudflare Agents SDK Durable Object
                     ├─ SQLite: conversations, memories, tasks, notes, projects,
                     │          automations, sessions, settings, usage
                     ├─ Workers AI: @cf/zai-org/glm-4.7-flash (streaming + tool calling)
                     └─ Alarms: reminders and recurring schedules
- The browser only ever talks to your *.pages.dev site. /api/* requests run a
Pages Function that forwards them over a service binding to the agent Worker.
- The agent Worker is deployed with workers_dev: false and preview_urls: false:
it has no public URL.
- Authentication and authorization happen in the Worker, not the frontend.
- Chat responses stream as Server-Sent Events end-to-end.
More detail: docs/architecture.md.
Talorys does not provision R2, D1, KV, Vectorize, AI Search, Workflows or any paid service.
npx create-talorys@latest
The installer:
- Checks Node.js (22+) and uses its bundled Wrangler CLI (any globally installed wrangler/cf is detected but not required).
- Verifies your Cloudflare login, or opens Cloudflare's authorization page in your browser.
- Lets you choose an account (if you have several) and an agent name.
- Asks for an owner password (hidden input, strength-checked). It is hashed locally with PBKDF2-SHA256 and stored only as a Cloudflare secret.
- Generates a 256-bit session secret and unique resource names (talorys-<id>-agent, talorys-<id>-web).
- Deploys the private Worker (creating its SQLite Durable Object), stores secrets, creates and deploys the Pages project with the service binding.
- Verifies the live deployment (frontend, auth endpoint, unauthenticated rejection, storage health) without running any AI inference.
- Prints the real https://….pages.dev URL reported by Cloudflare.
It writes a talorys/ directory containing talorys.json (installation id,
account id, resource names, URL — no secrets) and the deployable artifacts.
Keep it for updates.
Interrupted? Run the same command again in the same place. It reconciles what already exists: no duplicate resources, no password re-prompt if the password is already configured, and no data is ever deleted.
Non-interactive installs: TALORYS_OWNER_PASSWORD=... npx create-talorys@latest --yes --account-id <id>
(with CLOUDFLARE_API_TOKEN set if you are not logged in).
Browser login uses Wrangler's standard OAuth flow — no Global API Key. If you use an API token instead, it needs:
- Account › Workers Scripts › Edit
- Account › Cloudflare Pages › Edit
- Account › Workers AI › Read
- Account › Account Settings › Read
- User › User Details › Read (optional; shows your email)
See docs/deployment.md.
Open the URL the installer prints, enter your owner password, and start chatting. Sign in from any number of devices — they are all the same owner. Manage sessions under Settings → Security.
Forgot the password? From your talorys/ directory:
npx create-talorys@latest reset-password
This replaces the password secret and signs out every device.
All data is stored in a single SQLite-backed Durable Object (personal-agent)
in your Cloudflare account. Talorys has no telemetry, analytics, tracking or
advertising code and sends nothing to its developers.
Cloudflare processes your data to provide its services — including running Workers AI inference on your chat messages and the relevant memories included in each prompt. Review Cloudflare's privacy policy and Workers AI terms.
Security model and threat mitigations: docs/security.md.
Talorys is designed to fit the Cloudflare Workers Free plan and never enables paid features on its own. It is not "unlimited free", though:
- Free plans have account-level quotas (requests, Durable Object usage, a daily Workers AI Neuron allocation). Quotas are set by Cloudflare and can change.
- When the AI allocation is exhausted, chat shows a clear message and resumes after the daily reset. Everything else keeps working, and your data is untouched.
- If your account is on a paid plan, usage beyond included amounts is billed by Cloudflare under your plan.
Built-in guardrails (adjustable in Settings → AI): max output tokens, max context tokens (older history is summarized), max tool calls and reasoning steps per request, max AI requests per day (every model call counts, including each reasoning step and history summary), and max scheduled AI runs per day. Simple reminders and task digests never use AI. The Usage panel shows local estimates and links to the Cloudflare dashboard for exact Neuron usage.
Requirements: Node.js 22+.
git clone https://github.com/rociiu/talorys.git
cd talorys
npm install
npm run dev
npm run dev starts the agent Worker (wrangler dev, port 8787), the Pages
Function proxy with its service binding (wrangler pages dev, port 8788) and
the Vite UI (http://localhost:5173) in one terminal. It creates
apps/agent/.dev.vars with a local password (talorys-dev-password, override
with TALORYS_DEV_PASSWORD) and uses the deterministic mock AI provider, so no
Cloudflare login is needed. State persists in .wrangler/state.
Other scripts: npm run build, npm test, npm run test:e2e, npm run test:pack,
npm run typecheck, npm run lint. See docs/development.md.
Settings → Privacy → Download backup produces talorys-backup.json with
conversations, memories, tasks, notes, projects, settings and automations
(never sessions or credentials). Import validates the file and merges it in
one transaction; importing the same backup twice is harmless, and a memory you
edited locally after the backup was made is not overwritten. Memory history
(current vs. past facts) is included. Older backups import as before. Settings include
the effective installer defaults. If an imported timezone changes, retained
local automations are also rescheduled in that timezone. A backup file is
treated as untrusted: new automations arrive paused, existing automations are
never changed except to pause them, and the model, limits, demo mode,
auto-memory and memory history settings are kept as they are (the import
result lists any it skipped).
From your talorys/ directory:
npx create-talorys@latest update
This redeploys the latest Worker and frontend to the same resources. The
Durable Object namespace is never recreated (migrations are append-only), the
owner password and sessions are kept, and schema migrations run automatically
and transactionally on first request. Also available: status and doctor.
npx create-talorys@latest doctor checks everything automatically. More in
docs/troubleshooting.md.
apps/agent              Private Worker: Hono API, TalorysAgent, tools, SQLite repositories
apps/web                React + Vite app, Pages Function (functions/api/[[path]].ts)
packages/shared         Zod schemas, types, recurrence/DST logic, password hashing
packages/create-talorys The one-command installer (npm package)
tests/e2e               Playwright UI tests
tests/smoke             Optional real-account deployment test
docs/                   Architecture, deployment, development, security, troubleshooting
Thanks to everyone who has contributed to Talorys:
- Roc Yu (@rociiu) — creator and maintainer
- Derek (@KrunchMuffin) — Node.js 22 requirement, task deletion and cancelled-turn fixes, Windows build support
- Rudy Celekli (@rudycelekli) — automation lifecycle, deployment verification, and portable backup settings fixes
- Andrew B (@who) — opt-in semantic recall for memories
- Mendy Landa (@MendyLanda) — single-Worker deployment
- Michael Tuszynski (@michaeltuszynski) — untrusted backup import handling, daily AI budget accounting, and approvals bound to what was shown
- 김형준 (@wasuphj) — password policy, recurrence date, and vector guard fixes
