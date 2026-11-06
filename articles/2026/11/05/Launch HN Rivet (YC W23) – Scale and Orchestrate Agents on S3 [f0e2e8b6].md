---
id: "f0e2e8b6917e5dbe"
title: "Launch HN: Rivet (YC W23) – Scale and Orchestrate Agents on S3"
url: "https://github.com/rivet-dev/rivet"
link: "https://github.com/rivet-dev/rivet"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-05T17:17:42Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["NathanFlurry"]
language: "en"
summary: "Hey HN, this is Nathan and Nicholas from Rivet ( https://rivet.dev ) – a fast, high-density, and scalable orchestrator for agentic workloads using the actor model. Rather than running a heavyweight sandbox per agent, each agent gets a lightweight actor backed by S3. Actors provide a long-lived process for long agent turns, in-memory state for context, a WebSocket server for multiplayer, durable…"
tags: []
orgs: ["Anthropic", "Cursor"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1725
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50381687"
score: 105
comments: 53
community: "Hacker News"
---

# Launch HN: Rivet (YC W23) – Scale and Orchestrate Agents on S3

GitHub · NathanFlurry · 2026-11-05

4.99 ms p99 cold starts, 72 KB RAM per Actor, scales to billions
Quickstart • Documentation • Blog • Discord • X
Rivet Actors are long-lived processes with in-memory state, a SQLite database, WebSockets, and scheduling. You can create one for each agent, user, session, or tenant.
- 72 KB per Actor: Actors share a node process instead of each booting a sandbox, so one server holds hundreds of thousands.
- 4.99 ms p99 cold starts: No image pull and no VM boot.
- Built for scale: All data lives in S3, so a cluster scales to billions of Actors.
- Hibernates when idle, wakes on demand: Idle Actors cost nothing and wake on the next request with nothing lost.
- SQLite backed by S3, at SSD speeds: 1.07 ms durable writes and 1.36 ms reads at p99, for about 10.4× less than replicated SSD storage.
- Durable & multiplayer AI agents: memory that survives restarts, shared live with every client
- Workflows: multi-step operations that replay instead of starting over
- AI-generated apps: run the apps and Actors your agent generates
- Collaborative editing: one Actor per document, synced to every editor
A minimal agent written from scratch. For a ready-made agent, use Pi Durable.
// server.ts
import { actor, setup } from "rivetkit";
import { db } from "rivetkit/db";
import { streamText } from "ai";
import { openai } from "@ai-sdk/openai";
// One Actor per agent, created on first use: agent.getOrCreate(["agent-123"])
export const agent = actor({
  // 1. SQLite: every agent has its own database, so history survives restarts
  db: db({
    onMigrate: async (db) => {
      await db.execute("CREATE TABLE IF NOT EXISTS messages (role TEXT, content TEXT)");
    },
  }),
  // 2. In-memory state: plain variables that live with the Actor, with no database round trip
  createVars: () => ({ online: new Map<string, string>() }),
  // 3. WebSockets: each client holds a live connection, and the Actor pushes to all of them
  onDisconnect: (c, conn) => {
    c.vars.online.delete(conn.id);
    c.broadcast("online", [...c.vars.online.values()]);
  },
  actions: {
    join: (c, user: string) => {
      c.vars.online.set(c.conn.id, user);
      c.broadcast("online", [...c.vars.online.values()]);
    },
    sendMessage: async (c, text: string) => {
      // Save the message
      await c.db.execute("INSERT INTO messages VALUES (?, ?)", "user", text);
      const messages = await c.db.execute("SELECT role, content FROM messages");
      // Stream tokens to every connected client
      const response = streamText({ model: openai("gpt-5"), messages });
      for await (const delta of response.textStream) {
        c.broadcast("token", delta);
      }
      // Save the response
      await c.db.execute("INSERT INTO messages VALUES (?, ?)", "assistant", await response.text);
    },
  },
});
export const registry = setup({ use: { agent } });// client.ts (frontend or backend)
import { createClient } from "rivetkit/client";
import type { registry } from "./server";
const client = createClient<typeof registry>();
// Open a WebSocket connection to the agent
const agent = client.agent.getOrCreate(["agent-123"]).connect();
// Listen for realtime events
agent.on("online", users => console.log("online:", users));
agent.on("token", delta => process.stdout.write(delta));
// Call actions on the Actor
await agent.join("nathan");
await agent.sendMessage("how many r's in strawberry?");
Each Actor gives the agent a long-lived process for long agent turns, in-memory state for context, a WebSocket server for multiplayer, durable SQLite storage for session transcripts and agent artifacts, and hibernation when idle.
Most of an agent's time is spent waiting on inference. When the agent loop runs inside a sandbox, you pay for a whole VM that sits mostly idle with low CPU usage.
Rivet Actors run the agent loop outside of the sandbox instead, often called "separating the head from the hands." The agent's state, memory, and context live in the Actor, and it reaches the sandbox through tools only when it needs to run code. This uses a fraction of the memory and limits the blast radius and trust boundary of the code it runs. Read more about running the harness outside of the sandbox.
Often not. An agent needs a sandbox only to run code it writes. Developers on Rivet use three patterns:
- Agents with tools: Many agents only need tool calls, MCP, and APIs, such as customer support or personal agents. No sandbox needed.
- Agents with a lightweight sandbox: agentOS provides Linux-compatible sandboxing for JS and Python using V8 and WebAssembly, with full POSIX filesystems, networking stacks, and process trees. It covers most workloads, like data analysis, file processing, evals, and code mode.
- Agents with a full sandbox: Keep your existing sandbox provider and expose its shell and filesystem to the agent as tools, such as a bash tool that runs commands in the sandbox. The Actor reattaches to it across sleeps and restarts. See the sandbox coding agent example.
Paste this prompt into Claude Code, Cursor, Codex, or any coding agent:
Run npx skills add rivet-dev/skills, then ask me what to build and run it locally.
Rivet ships libraries built on top of Actors for common use cases.
- Actors: Long-lived processes with state, realtime, and scheduling built in.
- Agents: Durable agents built on Actors, with memory that survives restarts.
- Workflows: Multi-step operations built on Actors that replay instead of starting over.
- agentOS: Run the code your agent writes, securely, with granular control over network access, filesystem access, and resource limits.
- Dynamic Apps (preview): A backend per user, deployed the moment it is generated.
Benchmark details & methodology
- Rivet numbers come from the published Rivet Actors vs Cloudflare Durable Objects benchmark, run on Rivet 3.0.3. Its repository has the raw samples and the scripts to reproduce them.
- Sandbox numbers are for E2B: 512 MiB is its default memory allocation from E2B's billing documentation as of November 4, 2026, and 1.70 s is the p99 cold start from ComputeSDK's October 30, 2026 sandbox benchmark.
- Storage cost compares S3 Standard with three Amazon EBS gp3 copies at AWS list prices.
- Sources, dates, and the full method are at rivet.dev/docs/benchmarking.
- Fault tolerance: If a node goes down, its Actors move elsewhere with their state intact.
- HTTP & WebSocket networking: Call an Actor over HTTP or hold a live WebSocket to it.
- End-to-end type safety: Typed clients for your backend and React hooks for your frontend.
- Cron & scheduling: Wake an Actor on a schedule or at a time it sets for itself.
- Actor-to-Actor calls: Actors call each other by key across the cluster.
- Scoped JWTs: Give each client a JWT scoped to the Actors it may reach.
- OpenTelemetry: Traces, metrics, and logs in OTel format.
Every option runs the same control plane, from local dev to production. Talk to an engineer →
Typed SDKs for your backend and React hooks for your frontend. Rivet runs on native Node.js and Bun with no custom runtime, so your existing packages, tooling, and tests work unchanged.
Deploy nodes on: Docker Compose • Kubernetes • VM & bare metal • Hetzner • AWS ECS • Railway • Render
Runtimes: Node.js • Bun • Rust
Tools: Vitest • OpenTelemetry • Pino • AI SDK • OpenAPI • AsyncAPI
Does Rivet have BYOC?
Yes. Rivet deploys into your own cloud account, including air-gapped environments: the control plane and storage run inside your VPC while Rivet operates them. See the BYOC docs.
Does Rivet have a cloud?
Yes. Rivet Cloud runs fully managed, dedicated clusters on AWS or GCP in any region. It can run your app's Docker image as nodes on Rivet Cloud, or you can bring your own nodes.
Can I self-host Rivet?
Yes. Rivet is fully self-hostable; see the self-hosting docs. The control plane runs anywhere a container runs, with guides for Docker Compose, Kubernetes, VMs and bare metal, Hetzner, Railway, Render, and AWS ECS. For enterprise support with a self-hosted deployment, contact us.
Do I still need Postgres, FoundationDB, or NATS?
No. An object storage bucket is the only dependency: there is no database to run and no message bus, and control plane instances find each other through the bucket. Rivet works with Amazon S3, Google Cloud Storage, Azure Blob Storage, and any S3-compatible store such as MinIO, Cloudflare R2, or Hetzner Object Storage. A local filesystem backend is available for trying Rivet on one machine.
Is Rivet open-source?
Yes. Rivet is open source under the permissive Apache 2.0 license. You're looking at it.
Are Rivet Actors only for agents?
No. Rivet is a general actor platform at its core, with nothing specific to agents. For agents, you can use the optional agent library, which runs Pi Durable on Rivet Actors, or write your own agent from scratch.
How does Rivet compare to sandboxes?
A sandbox boots a VM or container per agent, which is slow to start and sits mostly idle. A Rivet Actor runs inside a shared node process: 72 KB and 4.99 ms p99 to start, versus 512 MiB and 1.70 s for a sandbox, and it hibernates when idle. To run untrusted code your agent writes, use agentOS.
How does Rivet compare to Cloudflare Durable Objects?
Rivet is often used as an open-source alternative to Cloudflare Durable Objects that is easy to self-host and scales. It also fixes many of the constraints of Durable Objects: no 128 MB memory cap, bottomless storage instead of a 10 GB SQLite limit, Actors are not randomly evicted, and you control the runtime because Actors run on vanilla Node.js or Bun instead of a custom runtime. Rivet also adds built-in connection handling, event broadcasting, durable scheduling and cron, full Vitest support, lifecycle hooks for draining, and control over Actor upgrades. See the Cloudflare Durable Objects comparison.
Does Rivet use a custom V8 runtime?
No. Rivet runs on native Node.js and Bun, so your existing packages, tooling, and tests work unchanged.
Is Rivet like Erlang, Akka, or Orleans?
Rivet implements the virtual actor pattern, which is closest to Orleans, but focuses on what modern workloads need: SQLite persistence instead of simple JSON stores and support for modern runtimes. Erlang and Akka do not provide virtual actors out of the box, though ecosystem packages exist that offer functionality comparable to Rivet Actors.
Does Rivet require microVMs, gVisor, or nested virtualization?
No. Rivet only needs a standard process that connects to the control plane over WebSocket. That process can be Node.js, Bun, Rust, or anything else.
- Discord - Chat with the community
- X/Twitter - Follow for updates
- GitHub Discussions - Ask questions
- GitHub Issues - Report bugs
- Talk to an engineer - Discuss your use case
