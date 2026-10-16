---
id: "e2491b58b595cef2"
title: "Vercel adds always-on workers to run more of your backend"
url: "https://thenewstack.io/vercel-faces-its-daemons"
link: "https://thenewstack.io/vercel-faces-its-daemons"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-15T18:45:00Z"
published_date: "2026-10-15"
collected_at: "2026-10-16T12:06:51Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Vercel is giving developers more options for running their backends on its platform. \n\n At its Ship conference in San Francisco on Thursday, the company introduced Daemons, a new service for continuously running background workers, and made its  Python support  generally available. \n\n It also made Drives, its persistent storage for AI agents, generally available. \n\n Always-on workers, pull-based…"
tags: ["AI", "AI Agents", "AI Infrastructure"]
orgs: ["OpenAI", "Amazon"]
topics: ["agents & coding", "jobs & society", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 1142
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Vercel adds always-on workers to run more of your backend

The New Stack · Frederic Lardinois · 2026-10-15

Vercel adds always-on workers to run more of your backend
Vercel is giving developers more options for running their backends on its platform.
At its Ship conference in San Francisco on Thursday, the company introduced Daemons, a new service for continuously running background workers, and made its Python support generally available.
It also made Drives, its persistent storage for AI agents, generally available.
Always-on workers, pull-based jobs
Daemons, which is now in public beta, lets developers deploy a container and specify how many instances should run in each region. Vercel makes sure those processes keep running and restarts them if they exit or crash. At launch, it supports pull-based workloads that allow workers to fetch jobs from a queue or database and then process them as they arrive.
Vercel CTO Malte Ubl tells The New Stack that the company’s current push in terms of going further down the stack.
“Let’s look at what people are doing, and let’s make sure that a larger chunk of them could just only use Vercel as their infrastructure provider,” he says.
The company already offers queues and durable workflows, while its Services feature lets developers deploy frontends and backends together.
These features cover request-driven work, Ubl says, but not everything a sophisticated backend does. “What really doesn’t fit well into that bucket is what you do find in sophisticated backend workloads,” he says, “where you want to do essentially processing on some kind of queue,” he says.
He uses Vercel’s own deployment pipeline as an example for that kind of workload.
“When you call our API to make a deployment, we don’t do that deployment in that process that handles your request, because we can’t actually do an infinite number of concurrent deployments,” Ubl says. GitHub rate limits are one reason to back off, and Vercel’s existing compute primitives didn’t give developers “good control over the amount of concurrency” for that kind of worker.
With Daemons, “they come up, they start saying, here I am, give me work, and then they just process as it goes,” he says.
The company’s example for using Daemons combines a Next.js frontend with a Python API, as well as a containerized video processor. The container packages Python dependencies and the FFmpeg media framework, and then pulls jobs from Vercel Queues to generate playback files and thumbnails.
Transcoding is a typical case, Ubl says, with “extremely CPU-bound workloads” where “I just need computers that I want to always be 100% CPU.”
That also puts Daemons at the opposite end of the spectrum from Vercel’s sandboxes. “They’re almost the opposite of temporary,” he says of Daemons. “For temporary, you have sandboxes,” he says. Daemons stay on but aren’t invoked by requests from the internet. They reach out for work instead.
Developers can deploy through Git or the Vercel CLI. Vercel builds the container image and stores it in its Container Registry.
The company itself runs a good chunk of its control plane API on Vercel. That accounts for about a billion requests a month, Ubl says, and Vercel is now starting to move many of its asynchronous workloads onto Daemons.
Vercel didn’t invent the model, he acknowledges, “we ship it because people very much want this.”
Managed runtime or container
If you’re deep in the Vercel ecosystem, you may wonder how all of this relates to Vercel Functions.
Vercel says 5,000 teams have made 150,000 container deployments since container support entered public beta. Containers let developers package applications with their own runtimes and system libraries, expanding the range of software they can deploy.
The trade-off here is who keeps the image current, Uble argues. With a managed runtime for Node, Bun, or Python, Vercel applies a security release without the customer redeploying, Ubl says. With a container, “you do have to redeploy. It’s ultimately your responsibility,” he says. “From our point of view, it’s just bytes.”
Python support, meanwhile, is now generally available for frameworks including FastAPI, Flask, and Django. Applications run on standard CPython with PyPI dependencies, while Vercel handles framework detection, builds, and scaling. The company says 150,000 teams already run Python backends on its platform, including engineers at OpenAI, Polymarket, and Exa.
Files that survive a change of environment
Vercel Drives is a great example of how agents are changing the requirements for backend services like storage. Vercel’s Drives service separates an agent’s files from the sandbox executing its code. An agent can mount the drive in a new sandbox, change runtimes, and continue working with the files it already created.
“I wouldn’t claim it’s an industry first, but it’s certainly an instance of a new type of storage product,” Ubl says. He describes it as a hybrid of an EBS-style networked drive and object storage, something he doesn’t think AWS offers.
Writes always land on local NVMe disk and stream asynchronously to object storage, he says, and reads come from the local disk when the data is already there — or stream in block by block.
“You have a very large number of independent disks, which, because they’re just files in S3, are arbitrarily cheap to operate,” he says.
Drives versus snapshots
Many sandbox providers, Vercel included, offer snapshots, Ubl says, but he argues drives are the better model.
“The problem with snapshots is they get really big, because you ultimately snapshot all kinds of stuff that is the same every time,” he says. “In practice, what agents really do is there’s some directory, I don’t know, /home/agent. That’s where everything is. Everything else they don’t really care about.”
Mounting that one directory means every agent can boot from the same cached base image, he says. “It’s cheaper for them, it’s faster. There’s essentially no downside.”
Vercel isn’t removing snapshots, Ubl adds, but it is encouraging customers to switch.
Drives lets those agents reuse each other’s work. One can prepare a dataset while others mount read-only copies to analyze it or generate reports, saving their results separately. Agents can also fork a drive to test different approaches in independent writable workspaces. Those forks don’t merge back into the original.
In practice, Ubl says, that means telling the agent where to write. “When you use a sandbox, you always tell your agent where it should write things,” he says, typically a root directory such as /workspace. “Essentially every prompt will start with that sentence, and then that’s just what you mount into your durable drive, and that’s it.”
Drives and forking are generally available. The service is available on all Vercel plans, with default capacities of 1 TiB, or 1 GiB on Hobby, and configurations up to 16 TiB.
For a team already deploying its frontend on Vercel, running a worker or Python API there becomes an easier decision. Each additional backend service it can keep on the platform is one fewer deployment system its developers have to maintain.
