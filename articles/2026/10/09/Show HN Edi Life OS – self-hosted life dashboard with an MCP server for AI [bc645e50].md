---
id: "bc645e50c62e4932"
title: "Show HN: Edi Life OS – self-hosted life dashboard with an MCP server for AI"
url: "https://github.com/edrisranjbar/lifeos"
link: "https://github.com/edrisranjbar/lifeos"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-09T00:02:19Z"
published_date: "2026-10-09"
collected_at: "2026-10-13T20:17:27Z"
authors: ["edris0077"]
language: "en"
summary: "Your habits, goals, focus, money and projects in one self-hosted dashboard that your AI assistant can use too.\nWebsite · Quick start · Tour · AI / MCP · Deploy · API · Donate · Contact · Español\nTick a habit, ask Claude to log an expense, and see it land in Finance. The expense is written through the real API with sample data.\nMost of us run our lives across a to-do app, a habit tracker, a…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1135
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50014150"
score: 41
comments: 17
community: "Hacker News"
---

# Show HN: Edi Life OS – self-hosted life dashboard with an MCP server for AI

GitHub · edris0077 · 2026-10-09

Your habits, goals, focus, money and projects in one self-hosted dashboard that your AI assistant can use too.
Website · Quick start · Tour · AI / MCP · Deploy · API · Donate · Contact · Español
Tick a habit, ask Claude to log an expense, and see it land in Finance. The expense is written through the real API with sample data.
Most of us run our lives across a to-do app, a habit tracker, a budgeting spreadsheet, a Pomodoro timer and a notes app, and none of them know about each other. Edi Life OS puts all of it in one calm, private dashboard and connects the small things you do today to the direction you want your life to take.
- Everything in one place. Ten workspaces share one design, one sign-in and one database.
- Connected, not just collected. Habits drive goal progress, Kanban cards show up in the calendar, and the Overview turns it all into one daily score.
- Yours. Runs on any PHP + MySQL host, even cheap shared hosting. No subscription, no tracking, no vendor lock-in.
- AI-ready. A built-in MCP server lets Claude and other assistants read your dashboard, plan goals, log habits and track expenses for you.
Tip
If Edi Life OS is useful to you, a ⭐ on GitHub helps other people find it.
Overview — One daily score built from focus, habits, goals and work, plus your six life dimensions at a glance.
All ten workspaces
Dates follow Asia/Tehran. The weather card shows Qeshm Island via Open-Meteo; its tide figure is a modeled estimate, not for navigation.
Edi Life OS ships with an optional MCP server that exposes 15 tools across your dashboard, goals, tasks, habits, finances and notes. Connect it to Claude Desktop, Claude Code or any MCP client and ask in plain language:
"Show me my LifeOS dashboard."
"Create a SMART goal called Build a home studio, due in three months, and add Buy acoustic panels as a task."
"Mark Reading complete for today."
"Log a 450,000 Toman food expense and show my balance."
The MCP server talks to your app only through its token-protected HTTP API. It never touches your database or credentials. Setup takes a minute — see MCP server below.
git clone https://github.com/edrisranjbar/lifeos.git && cd lifeos
cp .env.example .env    # set your sign-in and passwords
docker compose up -d
Open localhost:8080 and sign in. MySQL, the app and your attachments each live in their own volume, so docker compose up -d --build after a git pull upgrades without losing data.
Download lifeos-<version>.zip from the latest release and extract it into your hosting home directory, so public_html/ becomes your web root and the backend sits safely above it. Copy config.example.php to config.php, fill in your MySQL details, and open your site. See the deployment guide for details.
You need PHP 8.1+ (with pdo_mysql and mbstring) and MySQL 8+ (or MariaDB 10.4+).
git clone https://github.com/edrisranjbar/lifeos.git
cd lifeos
cp config.example.php config.php   # PowerShell: Copy-Item config.example.php config.php
Edit config.php with your database connection and the username and password you want to sign in with, then start the server:
php -S localhost:8000 -t public_html server.php
Open localhost:8000 and sign in. The database and tables are created on first use. Use Settings → My account to change your sign-in, or Settings → Accounts to add people with their own passwords and private workspaces. Account guide
Important
config.php and .env hold real credentials and are gitignored. Never commit them.
A private /api/v1 API covers the dashboard, goals, tasks, habits, finances and sticky notes. It uses its own bearer token, separate from your browser sign-in.
php -r "echo bin2hex(random_bytes(32));"
Set the result as api_token in config.php (or the LIFEOS_API_TOKEN environment variable), then:
curl -H "Authorization: Bearer $LIFEOS_API_TOKEN" https://your-host/api/v1/dashboard
See the API reference for endpoints, payloads and errors.
cd mcp
npm ci
cp .env.example .env   # set LIFEOS_BASE_URL and LIFEOS_API_TOKEN
npm start
The server runs over stdio; there is no hosted MCP endpoint. The MCP guide lists every tool and shows client configuration for Claude and Codex.
- Everything lives in your MySQL database. Habits use dedicated tables; other workspaces store JSON documents in app_state.
- Saves use revision checks, so a stale tab can't silently overwrite newer changes. API writes use transactions and row locks.
- Data from older browser-only versions is imported once; conflicting copies are archived as legacy_backup_* records.
- Back up the database, attachment files and your configuration together.
Moving from the old Habittify SQLite database? See migrating Habittify.
Edi Life OS supports multiple accounts with separate private data. New accounts are members, who see only their own workspace. Administrators can also add accounts, reset passwords and deactivate access; because a password reset lets them sign in as that person, make only trusted people administrators.
- The operator API token grants read and write access to supported domains for one active account (api_user_id, default 1). Per-user token issuance, token scopes and API rate limiting are not implemented, so set request limits at the hosting layer.
- Use HTTPS anywhere other than localhost, and keep tokens out of URLs, frontend code, screenshots and logs.
- Secret notes are hidden from API reads by default. The secret flag controls visibility; it is not separate encryption.
public_html/          Browser workspaces, shared assets and Apache entry points
lib/                  API domains, response helpers and state transactions
mcp/                  Optional Node.js stdio MCP server
tests/                Timer, API, MySQL and integration checks
docs/                 Guides, plus README screenshots in docs/media
config.example.php    Configuration template (no real credentials)
server.php            Development router and application routing
api.php               HTTP API entry point
Built with PHP, MySQL and vanilla JavaScript — no frontend build step, no framework.
Dockerfile, docker-compose.yml and docker/config.php run the app with configuration from environment variables.
- API reference — authentication, routes, data formats and concurrency
- MCP guide — tools, environment settings and client setup
- Deployment guide — Apache, shared hosting, backups and migration
- Development guide — local checks and disposable integration fixtures
- Growth workspace · Debts and credits
If Edi Life OS is useful to you, consider supporting its development with a donation.
Donate through Donatr — choose an available donation method on my public page.
You can also donate directly to these public receiving addresses:
Send only the listed cryptocurrency on the specified network.
For questions, feedback or collaboration, email edris.qeshm2@gmail.com.
For bugs and feature requests, please open a GitHub issue so the discussion is easy to follow.
MIT © 2026 Edris Ranjbar. Use it, fork it and build on it.
Ideas, bug reports and pull requests are welcome. Read the contributing guide to get set up, and look for good first issue if you want somewhere to start.
If Edi Life OS helps you run your days, consider giving it a ⭐ — it helps others find it.
