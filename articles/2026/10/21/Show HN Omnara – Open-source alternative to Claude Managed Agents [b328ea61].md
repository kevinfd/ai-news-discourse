---
id: "b328ea6101ebd166"
title: "Show HN: Omnara – Open-source alternative to Claude Managed Agents"
url: "https://github.com/omnara-ai/omnara"
link: "https://github.com/omnara-ai/omnara"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-21T16:44:53Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["kmansm27"]
language: "en"
summary: "Hey all, Kartik from Omnara ( https://omnara.com ) here. We're building an open-source API for running durable agents. You create an agent with an API call, and Omnara runs the agent loop, gives the agent sandboxes to run commands in, and handles secrets, permissions, and RBAC. Each agent's state is stored in Postgres, so agents survive restarts and cost nothing while idle. You can message them…"
tags: []
orgs: ["Anthropic", "OpenAI", "Amazon"]
topics: ["agents & coding", "products & launches", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 1820
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50183892"
score: 87
comments: 26
community: "Hacker News"
---

# Show HN: Omnara – Open-source alternative to Claude Managed Agents

GitHub · kmansm27 · 2026-10-21

A self-hostable alternative to Claude Managed Agents and OpenAI's Agents API.
Website · Quickstart · Docs · API · Changelog · Discord
Omnara is an open-source managed agent platform. Use the API to run AI agents on any model and any machine, with tools, secrets, permissions, and streaming built in. Self-host it for free under Apache 2.0, or use Omnara Cloud.
Sign in at app.omnara.com. Your first project comes
with a model provider (omnara-openrouter) and a pool of managed sandboxes
(default-pool), so this config runs as is. Save it as agent.yaml:
version: v1
instruction: |
  You are an engineering assistant. Use your machine to run commands.
model:
  provider_config: omnara-openrouter
  name: anthropic/claude-fable-5.1
machine_sources:
  - machine_pool_name: default-pool
Launch it with the CLI (Node.js 22 or newer). If you're not logged in, the first command opens your browser to sign in.
npx omnara agents launch --file agent.yaml \
  --name "Machine assistant" \
  --message "Report this machine's operating system and free disk space."
Chat with the agent in your terminal with npx omnara agents chat <agent-id>,
or open it in the dashboard to watch its tool calls and reply.
Launch it from your code with the TypeScript SDK
Create an API key in the dashboard and export it as OMNARA_TOKEN, install the
SDK with npm install @omnara/sdk, and use the org and project IDs that
npx omnara config prints:
import { readFile } from 'node:fs/promises'
import { bearerToken, createOmnaraClient, openAgentEventStream, sdk } from '@omnara/sdk'
const client = createOmnaraClient({ auth: bearerToken(process.env.OMNARA_TOKEN!) })
const path = { orgID: 'org_...', projectID: 'proj_...' }
const config = await sdk.createAgentConfig({
  client,
  path,
  body: { source: await readFile('agent.yaml', 'utf8'), source_format: 'yaml' },
})
const launched = await sdk.createAgent({
  client,
  path,
  body: { config: config.data.id, message: "Report this machine's free disk space." },
})
const agentID = launched.data.agent.id
for await (const event of openAgentEventStream({ client, path: { ...path, agentID } })) {
  console.log(event)
}
The quickstart shows the same flow with the REST API.
To have your coding agent do the setup, give it this prompt:
Help me set up Omnara by following https://www.omnara.com/SKILL.md
Requires Docker with Compose.
git clone https://github.com/omnara-ai/omnara.git
cd omnara
docker compose -f compose.yaml --profile app up -d
Open http://localhost:8000 and sign up. Local
development prints the verification link in docker compose logs api, so no
email provider is needed. To build from source instead of using published
images, run docker compose --profile app up -d --build.
A new instance has no models or machines yet. In the console, add a model provider and a model, connect this computer under Machines, and share both with your project. Sandboxes also work once your instance has a public URL.
Point the CLI at your instance and log in:
npx omnara config --api-url http://localhost:8000/api/v1 --issuer-url http://localhost:8000
npx omnara login
In agent.yaml, use your provider and model names, and replace the
machine_pool_name entry with machine_name: <your machine>. Then launch it
with the same command as above.
The local defaults are intentionally insecure. For a real deployment, follow the self-hosting guide and the configuration reference.
Your product talks to Omnara, and Omnara runs each agent with the model, tools, and machines in its config.
flowchart TB
    subgraph yours["Your side"]
        users(["Your users"]) --> app["Your app<br/>REST API · TypeScript SDK"]
        team["Your team<br/>CLI · dashboard<br/>Slack · Discord · GitHub"]
    end
    subgraph omnara["Omnara"]
        api["API<br/>launch · input<br/>event stream · approvals"] <--> pg[("Postgres<br/>each agent's event log")] <--> worker["Workers<br/>run the agent loop"]
    end
    subgraph plug[" "]
        models["Models<br/>OpenAI · Anthropic<br/>OpenRouter · self-hosted"]
        tools["Tools<br/>built-in · skills<br/>MCP · custom"]
        machines["Machines<br/>sandboxes or your own<br/>laptop, VM, container"]
    end
    app --> api
    team --> api
    worker --> models
    worker --> tools
    worker --> machines
    classDef side fill:none,stroke:#8b949e,stroke-width:1px
    classDef core fill:#506FCF,stroke:#3D5BB5,stroke-width:1px,color:#ffffff
    classDef store fill:#3D5BB5,stroke:#2E4794,stroke-width:1px,color:#ffffff
    classDef plugin fill:none,stroke:#85A0E6,stroke-width:1.5px
    class users,app,team side
    class api,worker core
    class pg store
    class models,tools,machines plugin
    style yours fill:none,stroke:#8b949e,stroke-dasharray:4 3
    style omnara fill:#506FCF14,stroke:#506FCF,stroke-width:1.5px
    style plug fill:none,stroke:#85A0E6,stroke-dasharray:4 3
    linkStyle default stroke:#8b949e,stroke-width:1.5px
    - API. Your app, the CLI, and the dashboard all use the same REST API to launch agents, send messages, and answer approvals. Events stream back as they happen.
- Postgres. Every step of every agent is saved here. That record is the agent's state, so any worker can pick an agent back up after a crash or restart.
- Workers. Stateless processes that build the model context, call the model, and run tools. An agent only uses a worker while it's taking a turn, so one worker can serve many agents. Add workers to handle more turns at once.
- Machines. Each machine runs the omnarad daemon, which connects out to
Omnara, so agents can run commands there without any inbound ports.
Omnara also uses Redis, blob storage for attachments and tool outputs, and a memory filesystem. The architecture docs cover the details.
- Any model. Bring your own keys for OpenAI, Anthropic, OpenRouter, Amazon Bedrock, LiteLLM, Ollama, or any compatible endpoint, including models you host yourself.
- Tools. Built-in tools for shell commands, files, web search and fetch, and asking a person a question, plus MCP servers and custom tools that run in your own systems.
- Skills. Package instructions and files once, attach them to any agent, and the agent loads them when it needs them.
- Memory. Memory stores give agents files that persist between conversations and can be shared with other agents, with read or read-write access per agent.
- Subagents. An agent can start subagents with a fresh context, check their progress, and send them new instructions. Each subagent is a full agent you can inspect.
- Machines. Machines are tools the agent uses. Install the Omnara daemon on any macOS or Linux laptop, VM, or container and your agents can run commands and edit files there, with no inbound ports or SSH keys. Or use sandboxes from eleven providers (Arker, Blaxel, boxd, CreateOS, Daytona, E2B, Freestyle, Modal, Superserve, Tenki, Unikraft). An agent can use several machines at once (for example, a set of GPU servers) and move between them. If your laptop goes offline, the agent can continue in a sandbox and sync its work back with git.
- Durable state. Every step is saved, so agents pick up where they left off after crashes, restarts, and machine disconnects.
- Schedules. Cron triggers with time zones can message an existing agent, launch a new one from a profile, or start a new Slack or Discord thread.
- Slack, Discord, and GitHub. Mention the bot in Slack or Discord to start an agent in a thread, where it replies, asks questions, and requests approvals. On GitHub, an agent can start when a pull request opens or someone mentions it, then read the diff, comment, and submit reviews. To connect another service, build a custom integration on the same public API.
- Streaming and webhooks. Stream every event as it happens or receive it as a webhook, and send new messages while the agent works.
- Permissions. Each tool can run immediately, ask a person first, or be blocked. The platform enforces the setting, and the agent waits until someone approves or denies the call.
- API, SDK, and CLI. A REST API
defined in api/openapi/openapi.yaml, a
TypeScript SDK (@omnara/sdk),
a CLI (omnara), and an MCP server.
- Role-based access control and secrets. Organization and project roles for users and API keys. Credentials for models, machines, and MCP servers are stored once and shared with each project explicitly.
- Multi-tenant. One deployment serves many organizations, each with its own members, projects, secrets, model providers, and machines. Self-hosted operators can give every new organization default models and sandboxes, as Omnara Cloud does.
- Your data. Self-hosted deployments keep every agent's history in your own Postgres, where you can query it for analytics, evals, and training datasets.
Claude Managed Agents and OpenAI's Agents API are hosted services for running agents on one company's models. Omnara does the same job as an open-source platform you can run anywhere, with any model.
Choose Claude Managed Agents or the Agents API if you use one company's models and want that company to run everything for you. Choose Omnara if you want to pick your models and machines, run the platform yourself, or keep agent data in your own database.
Each of these is an agent.yaml plus a SKILL.md in examples/,
and you can deploy any of them with one prompt to your coding agent.
- Slack coding agent fixes issues you mention in Slack, Discord, or a GitHub pull request and opens a PR.
- PR review agent reviews your GitHub pull requests against a checkout of the repository and leaves inline findings.
- SRE agent investigates production problems such as a 5xx spike.
- Browser agent works in a real browser on long-running tasks.
- PostHog analytics agent compares yesterday's product usage with the 7-day average and reports what changed.
- Reddit, X, and LinkedIn signal agents summarize the last 24 hours of posts about a topic you pick.
- Video generation agent makes short videos from a brief.
There are also code samples for a CLI chat app built on the TypeScript SDK, custom tools over webhooks, and a SharePoint filesystem mount.
MCP server. Connect Claude Code, Codex, Cursor, or any MCP client that
supports OAuth to https://app.omnara.com/mcp to launch and manage Omnara
agents. You sign in through the browser, so there are no tokens to paste. In
Claude, add it from the
connectors directory. Omnara is
also listed in the official MCP Registry as com.omnara/omnara.
claude mcp add --transport http omnara https://app.omnara.com/mcp
codex mcp add omnara --url https://app.omnara.com/mcp
Then sign in with /mcp in Claude Code or codex mcp login omnara in Codex.
See Connecting MCP clients.
CLI. omnara manages agents,
profiles, machines, model providers, secrets, skills, and cron triggers from
your terminal or your coding agent's shell. Run npx omnara --help to start.
Setup skill. skills/setup-omnara-agent,
also served at omnara.com/SKILL.md, walks a
coding agent through setting up Omnara for your project.
Docs for LLMs. docs.omnara.com/llms.txt.
What is Omnara? An open-source managed agent platform for running AI agents on any model and any machine.
How much does it cost? Nothing to self-host. Omnara Cloud has no platform fee. You can bring your own model keys and machines for free, or pay as you go for our models at provider token rates and our sandboxes by active time and retained storage. See pricing.
Can I self-host it? Yes. Run it with Docker Compose locally, then follow the self-hosting guide for production. The API, CLI, SDK, and config format are the same on Omnara Cloud and self-hosted deployments.
Which models work? Any model behind an OpenAI Responses, OpenAI Chat Completions, or Anthropic Messages compatible endpoint, including OpenAI, Anthropic, OpenRouter, Amazon Bedrock, LiteLLM, and Ollama.
Source development requires the Go version declared in go.mod,
Node.js 24 or newer with Corepack, ripgrep, and Docker with Compose. Run the
fast repository gate with make verify. See CONTRIBUTING.md
for the full test suite, generated-code workflows, and pull request
expectations.
Discord · GitHub Issues · X · Security
