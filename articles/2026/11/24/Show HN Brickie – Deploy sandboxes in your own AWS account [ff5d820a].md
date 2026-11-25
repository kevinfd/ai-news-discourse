---
id: "ff5d820a02c7229c"
title: "Show HN: Brickie – Deploy sandboxes in your own AWS account"
url: "https://github.com/hatchet-dev/brickie"
link: "https://github.com/hatchet-dev/brickie"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-24T15:48:34Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["abelanger"]
language: "en"
summary: "Hey HN, this is Alexander from Hatchet ( https://github.com/hatchet-dev/hatchet ). We’re releasing a new open-source project today called Brickie. Brickie lets you run sandboxes in your own cloud account, primarily targeting EKS on AWS. Sandboxes are an incredibly useful primitive for agentic applications. They serve two main functions: (1) a way for the agent to safely execute untrusted code,…"
tags: []
orgs: ["Amazon", "Microsoft"]
topics: ["agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 654
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50629936"
score: 31
comments: 8
community: "Hacker News"
---

# Show HN: Brickie – Deploy sandboxes in your own AWS account

GitHub · abelanger · 2026-11-24

Brickie lets you run durable sandboxes in your own cloud / k8s cluster.
Brickie sandboxes are built on top of agent-sandbox with custom snapshot/restore implemented on top of object storage. They are designed to be called from @hatchet-dev/sandbox and support the ability to take a coordinated snapshot of agent state. This means that every sandbox call is a retryable and observable Hatchet task.
Each sandbox session is a container with a shell and a workspace and runs in your Kubernetes cluster with flexible runtime support, including Kata, gVisor and AWS Nitro. Every call that changes the workspace produces a snapshot, which can be used to fork a new sandbox or resume an existing session.
Head over to the quickstart guide to get up and running your own Brickie sandboxes with a local Hatchet instance.
Brickie is in beta. Flags, chart values and the wire contract may change before 1.0. See the changelog.
Docs: here
- Hatchet-guaranteed safe retries: Hatchet's durable execution guarantees mean no wasted compute on retries of succesful sandbox operations.
- Immutable and forkable snapshots: Every call that changes files in your sandbox workspace are saved and stored in object storage. They are immutable and forkable from other sandbox processes.
- Fast starts: A warm pool of pods maintained by the provider means small cold start times for new sandbox pods.
- Custom images: Any image with sh and tar can be used to run a sandbox.
- mTLS for all sandboxes: The provider and each sandbox talk to each other over mutual TLS with strict guarantees around certificate issuance, rotation, and usage.
- Resource limits: Each sandbox is backed by a pre-set network and resource limit to cap usage and to protect nodes from starvation.
- Any object storage: Metadata and snapshots can be stored in any S3-compatible store as well as in GCS and Azure.
- FIPS support: By default, the provider runs all of its workloads in FIPS 140-3 mode with signed and SBOM attested container images.
- Extensible interface: Backed by drivers, the provider can be extended to support more backends apart from Docker and Kubernetes.
pnpm add @hatchet-dev/sandbox @hatchet-dev/typescript-sdkimport "@hatchet-dev/sandbox";
const session = hatchet.durableTask({
  name: "agent-session",
  fn: async (input) => {
    const sandbox = await hatchet.sandbox.create({
      id: input.conversationId,
      template: "alpine:3",
    });
    await sandbox.files.write("haiku.txt", "an old silent pond");
    const haiku = await sandbox.exec("cat haiku.txt");
    await sandbox.kill();
    return { haiku: haiku.stdout };
  },
});
// run the session for a conversation; its ID becomes the sandbox ID
const { haiku } = await session.run({ conversationId: "conv-42" });
// later, from anywhere with a Hatchet client
const again = await hatchet.sandbox.connect("conv-42");
Under the hood, brickie uses the agent-sandbox controller and warm pools to run sandbox pods. On top of this, the Brickie provider does a few different things:
- Every brickie sandbox turn produces an immutable snapshot in your object store, keyed by sandbox and Hatchet run ID. These snapshots can be forked into new sandboxes, or used to resume an existing session. On agent-sandbox, state is persisted through a PVC per sandbox, which forces a cold start, while the only point-in-time snapshot is GKE-specific.
- Every call is a Hatchet task, so it is retried, observable, and replayed from its own snapshot. A retried call finds the snapshot it already stored and does not run the command twice.
- The same code path runs on a Docker engine, so the Kubernetes cluster is not needed for development locally.
- Architecture, how turns, snapshots and the store fit together
- Security, trust boundaries, isolation and image verification
- Drivers and extending Brickie with your own
- Wire contract, what the SDK sends and gets back
- Hatchet docs, the task engine underneath
- Contributing and AGENTS.md, the working rules
Pull requests are welcome from vouched contributors, and the first ones should be small. CONTRIBUTING.md explains how to get vouched, what to work on first and how AI use is disclosed.
