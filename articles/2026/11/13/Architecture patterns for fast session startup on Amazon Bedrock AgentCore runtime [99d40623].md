---
id: "99d40623cf51112d"
title: "Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime"
url: "https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime"
link: "https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime"
source: "AWS Machine Learning Blog"
domain: "aws.amazon.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-13T22:02:39Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Evandro Franco"]
language: "en"
summary: "Agents today review code, process claims, and run unattended for hours. Many also sit behind interactive experiences where a person waits for the first response. Amazon Bedrock AgentCore runtime gives these agents a fully managed, serverless environment: each session runs in its own isolated microVM, the platform scales to zero when there’s no work, and you only pay for the resources your…"
tags: ["Amazon Bedrock AgentCore", "Best Practices", "Expert (400)"]
orgs: ["Amazon"]
topics: ["agents & coding", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 2360
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime

AWS Machine Learning Blog · Evandro Franco · 2026-11-13

Artificial Intelligence
Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime
Agents today review code, process claims, and run unattended for hours. Many also sit behind interactive experiences where a person waits for the first response. Amazon Bedrock AgentCore runtime gives these agents a fully managed, serverless environment: each session runs in its own isolated microVM, the platform scales to zero when there’s no work, and you only pay for the resources your sessions consume.
AgentCore runtime with platformVersion set to “V2” changes how sessions start. Instead of initializing your container for every session, it prepares your environment once, snapshots it, and restores that snapshot for each new session. Session start times are faster and more consistent. V2 also reclaims memory your sessions don’t use, so your bill tracks what your agent uses.
For most agents, switching to V2 is all it takes. Some agents need restructuring to get the full benefit, and for chat and voice experiences even 2 seconds is too slow. This post explains how V2 starts a session, how to measure session start time, and how to keep work off the first request, including build hooks, which AgentCore runtime now supports. We cover four patterns, from changes to your agent’s code to starting sessions before users need them.
Which pattern do you need?
How V2 starts a session
AgentCore runtime runs each session in a new microVM. On V1, AgentCore pulls your container image from Amazon Elastic Container Registry (Amazon ECR), starts the container, and runs your initialization code before it can process the first request. The image pull dominates, so cold start grows with image size.
V2 does that work once. When you create or update a runtime, AgentCore runtime starts your container in a fresh microVM and waits for the first healthy ping (GET /ping), which must arrive within 120 seconds. It then clears the operating system’s file cache, to keep the snapshot small, freezes the microVM, and stores its memory and disk as a snapshot.
This is a change from V1: Every create or update now takes a few minutes while the snapshot is built.
In this post, init means everything your agent does before /ping reports healthy. With the AgentCore Python SDK, that’s everything before app.run(). If you run your own HTTP server, in Node.js or another language, report healthy only after your initialization finishes.
When a new session arrives, AgentCore restores the snapshot into a new microVM. Your process resumes exactly where it was frozen, with its imports, objects, and clients in place. Files from your image are loaded lazily: each block is fetched the first time a session reads it.
Three facts follow from these flows, and the rest of this post builds on them:
- Memory comes back whole. Anything your process held at snapshot time, and anything in a RAM-backed file system such as /dev/shm, is available at memory speed from the first access.
- File reads don’t carry over. The file cache is cleared before the freeze, so reading a file during init doesn’t make it fast in a restored session.
- Image files are fetched on first read. The first read of a block comes from snapshot storage and is then cached closer to the host.
The following table shows what that means for the work a typical agent does, depending on where it does it:
If you know AWS Lambda SnapStart, this will feel familiar. Marc Brooker’s post on how SnapStart loads snapshots and the SnapStart priming strategies post are useful background.
Everything in the table assumes your agent can keep what it needs in its own process. That isn’t always possible. A CLI that runs as a separate process and exits, or a browser binary, is read during init and then gone, so a restored session fetches it from the image again. For these cases, you can add a build hook, covered in “Working with hooks.” Figure 3 shows where it runs.
Measure before you optimize
Latency in an agentic application isn’t one number. A request spends time in AgentCore runtime getting a session ready to run your code, then in your code: model calls, tool calls, sub-agents, and streaming the response back. You fix these in different ways, so start by finding out which one dominates.
AgentCore runtime publishes both as Amazon CloudWatch metrics in the AWS/Bedrock-AgentCore namespace. Latency is the time to first byte. OverheadLatency is the part that belongs to the platform, such as starting the microVM and restoring the snapshot on a new session.
Init doesn’t appear in these metrics because on V2 it runs once, while the snapshot is built, and not in each session. It adds to how long a create or update takes to reach READY, not to request latency. To see how long it takes, log it once before app.run(). The line appears in your runtime’s build logs:
How to read the split:
- High OverheadLatency on new sessions: the time is in session start. Use the patterns later in this post to start sessions before users need them.
- Your code’s time is much higher on the first request than on the second in the same session: work that belongs in init is running in your handler. Add custom spans in AgentCore Observability (a capability of Amazon Bedrock AgentCore) around tool setup, file loads, and late imports to find it, then move it into init.
Report percentiles such as P90 and P99, or trimmed means such as TM90, which averages the fastest 90% of requests and drops the slowest tail. A plain average hides the slow requests. OverheadLatency covers requests to running sessions as well as new ones, so its distribution depends on how many of your requests start a new session. Compare runs with a similar mix.
Test at the rate of new sessions you expect in production, not with a handful of sessions after a deploy.
To include network time from your client, measure on the client as well. Time the invoke call, have your handler return how long it ran, and subtract. Both timestamps come from the same machine, so clock differences between the client and the microVM don’t matter. If you stream, very small events can be held back until a few hundred bytes of output build up, so time to first event can read higher than session start.
Keep work off the first request
The usual cold start advice is to import lazily and keep initialization small. On V2, do the opposite: init runs once, when the snapshot is built, and work deferred to the handler is paid by every new session. This applies to static work: imports, clients, and data from your image. Dynamic data can’t be snapshotted. The next section covers it.
The agents that notice most are the ones that read large files from their image at request time: weights for a small local model, embeddings, datasets, large libraries, a browser binary for automation, or a CLI toolchain that a coding agent runs as subprocesses. Reading many small files, as compiling a TypeScript project does, has the same effect. An agent that imports a few libraries and calls a hosted model mostly needs to get its imports and clients right.
How to restructure your agent
Create objects during init, not only imports. Creating an object loads the modules it depends on and keeps them in active memory. Initialize local tools that use external libraries during init too, not when the agent first calls them.
Create your clients during init. Endpoint resolution, credential resolution, and the client’s modules all come back with the snapshot. Sockets don’t, but boto3 clients reconnect cleanly on the first call. Some other network clients first try the stale socket, which adds hundreds of milliseconds, so close their connections before the snapshot.
Keep static data in memory, such as prompts, skill front matter, configuration, and small indexes. Hold the data in an object, not only a read of it:
Keep tools running instead of starting them per request. A subprocess launched in the handler reads its binary and libraries from the image in every new session. A long-running helper started during init, such as a language server or a worker process with its imports done, comes back as part of process memory. Talk to it over a pipe or socket.
Copy files you can’t hold in memory to a RAM-backed disk. Toolchains like tsc run as separate programs that read their own files. Copy them to /dev/shm or a ramfs mount during init so their reads come from memory.
Ship compiled bytecode. uv pip install doesn’t compile by default, so late imports also compile from source. Set UV_COMPILE_BYTECODE=1 or use pip install --compile.
The example below builds the agent, its model, and its clients during init, so every session inherits them:
The trade-off: time to first byte on a new session is the time to start the microVM and restore the snapshot, plus the time your handler takes. Moving work into init shortens the handler, but anything you hold in memory makes the snapshot larger. You also pay for that held memory in every session. Measure end-to-end session start before and after the change, so you know you’ve reduced latency and not only moved it from the handler to the restore.
Reference card
Working with hooks
A build hook builds on init and doesn’t replace it. Do what you can in init and use the hook for what init can’t cover. You expose an HTTP endpoint in your container, and AgentCore runtime sends it a POST request twice while it builds your runtime:
- Before the snapshot. On the build microVM, after your agent reports healthy and before the freeze. Anything your agent loads here and keeps in memory is part of the snapshot, so every session starts with it.
- After a test restore. On a separate microVM that restores the snapshot to check it. Nothing from this call is snapshotted. Use it to read the files your sessions will need, which shapes what restored sessions fetch first.
The X-Amzn-Bedrock-AgentCore-Runtime-Warmup-Type header tells your agent which call it’s handling: memory for the first, disk for the second. The two calls share 120 seconds, so the disk call gets whatever time the memory call leaves. Return a 2xx response only after the work is done. Any other response, a failed connection, or running out of time fails the create or update, and AgentCore runtime doesn’t retry. The build-logs- streams in your runtime’s log group show which call failed and why.
Hooks are available on V2 runtimes. Configure them with hooksConfiguration when you create or update the runtime:
The port is optional and defaults to your agent’s serving port. If you set it, use a port from 8000 to 12000 that isn’t reserved by the platform. The path can’t match a route AgentCore runtime already uses on that port, such as POST /invocations or GET /ping. UpdateAgentRuntime replaces the whole hook configuration, so include hooksConfiguration in every update where you want to keep the hook.
In the agent, handle both call types on the same endpoint:
For the full configuration reference, see Configure lifecycle hooks for AgentCore runtime. For a complete code example, see the sample code.
Snapshot pitfalls: What must stay in the handler
Everything created during init is frozen into the snapshot until your next deploy, and every session starts with the same copy. For most objects that’s the point. For the values below, it’s a bug, and for random values, a security issue.
Load dynamic data in the handler, once per session. Tool catalogs from AgentCore Gateway (a capability of Amazon Bedrock AgentCore), feature flags, and price lists change after you deploy. Load them in the handler and cache them at module level, so each session fetches them once. Sessions can last up to 8 hours, so give the cache an expiry:
Call get_tools() from the handler and pass the result to the agent you created during init.
Create per-session values in the handler.
Know the limits. A session ends when its idle timeout expires (idleRuntimeSessionTimeout: 15 minutes by default, from 60 seconds up to 8 hours), when it reaches its maximum lifetime (maxLifetime: 8 hours by default and at most), or when you stop it.
Sub-second: Start the session before the user needs it
Suppose your new session takes about 2 seconds to start, including all the timing breakdown covered in the preceding sections. A session that’s already running answers in about 200 ms. For a chat or voice experience, the way to sub-second is to make sure the session has started before the user’s first request arrives. There are two ways to do that.
Pre-warm on user engagement
Most interactive applications get a signal before the first prompt: the user opens the app, a chat window, or a support page. Use it. Generate a session ID, send the agent a warm-up request in the background, and keep the session ID with the conversation. By the time the user has typed their first message, the session is running.
This pattern needs no extra infrastructure and fully hides session start whenever users take more than about 2 seconds to send their first message. It costs a session for each user who engages but never sends a prompt. A short idle timeout keeps that small.
Conclusion
On V2, AgentCore runtime moves most of the work of starting a session to deployment time. Your container starts once, and every new session restores the result: memory comes back whole, and files are fetched on first read.
To keep session startup time near 2 seconds, do your static work during init, hold the data the first request needs in memory, and keep dynamic and per-session values in the handler. For files your process can’t hold, add a build hook. To get under a second, start the session before the user needs it: on user engagement when you get a signal.
To get started, set platformVersion to V2 when you create or update a runtime, then review Optimize your agent for AgentCore runtime V2. For questions about your workload, reach out to your AWS account team.
