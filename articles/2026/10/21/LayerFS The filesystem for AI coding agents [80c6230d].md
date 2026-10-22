---
id: "80c6230d043dd75b"
title: "LayerFS: The filesystem for AI coding agents"
url: "https://layerfs.ai"
link: "https://layerfs.ai"
source: "Ephemeral AI Lab"
domain: "layerfs.ai"
source_type: "community"
collector: "hackernews"
date: "2026-10-21T12:34:46Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["l2dy"]
language: "en"
summary: "Compute exists only while a command runs.\n- Compute: Agents spend ~80% thinking, ~10% in Bash.\n- FS: Each file tool call is one atomic Store op.\n- Sandbox: Each Bash tool call mounts an ephemeral workspace, then commits.\nEphemerality: scaling multi-agent development beyond imagination\nDurable Shared History.\nLayerFS is the substrate under your agents. Each one mounts a complete, writable…"
tags: []
orgs: []
topics: ["agents & coding", "chips & infrastructure"]
content_source: "fulltext"
word_count: 531
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50179857"
score: 72
comments: 45
community: "Hacker News"
---

# LayerFS: The filesystem for AI coding agents

Ephemeral AI Lab · l2dy · 2026-10-21

Compute exists only while a command runs.
- Compute: Agents spend ~80% thinking, ~10% in Bash.
- FS: Each file tool call is one atomic Store op.
- Sandbox: Each Bash tool call mounts an ephemeral workspace, then commits.
Ephemerality: scaling multi-agent development beyond imagination
Durable Shared History.
LayerFS is the substrate under your agents. Each one mounts a complete, writable Workspace over shared committed history, does its work, commits what it changed, and goes away.
- Ephemeral workspaces
- Durable results
- Massive parallelism
Why LayerFS
six core · four supporting
Agents on different computers share one serverless Store.
- Shared storage: Every agent commits to one Store, with no DB server.
- Distributed computing: Each agent runs on its own computer.
One project, many branches. One branch, many agents.
- Commits: Every tool call is a commit on its branch.
- Conflict: A same-file clash is refused with Conflict.
- Blame: Each line names the step that wrote it.
Fork recursively any commit, at any depth.
- Zero cost: A fork is metadata and copies no files.
- Recursive: A filesystem for RSI agents and recursive exploration for RL training.
10 copies compress into 0.31.
- Dedup: Each content chunk is stored once.
- Compression: The stored chunks shrink further.
- Ratio: 10 copies → 1.05 dedup → 0.31 compression wtf???
Dependencies come with every mount. No wasting time for re-installation.
- Git / other AgentFS: Drops ignored files; reinstalls.
- LayerFS: Ignored files stay in every commit.
- Comparison: ~5 min to install vs 0.05 s to mount.
Four supporting ideas
- Auto CheckpointsEvery step an agent takes is a checkpoint to return to.Every call: Each file call is a commit; each Bash call commits when it ends.No noise: A call that changes nothing commits nothing.Rewind: Fork from any checkpoint and read any file as it was.
- Append-only ObjectsSaved objects are never rewritten. The Store only grows.Content-addressed: An object is named by the hash of its bytes.Sealed: A written pack is never updated or deleted.Safe to share: Branches share objects; readers never wait for the writer.
- Conflict Rules (.lww)Name the files that should never conflict. The newest edit wins./.lww: Gitignore-style rules at the root of the tree.Newer wins: A matched file changed on both sides takes the newer edit.For: Lockfiles, build output and caches.
- Big File, Small EditAn edit costs the size of the edit, not the size of the file.Overlay: A write keeps only the bytes it wrote.Commit: Only the edited extents and their tree path are rebuilt.Storage: The rest of the file is shared with its old version.
HISTORYmain @ L00 commits · 0 live
main is the green middle bough; each publish adds a Layer bandLayer · a band on mainCommit · a leafBranch · a boughmerge · grafts backpublish · adds a bandstopped · bare twigclick a name tag to focus its Branch
sandboxes00 workspaces mounted12 idle
no Branch yet · the orchestrator forks one from main
unassigned
store.statsmain · read-only
dedupe1.5×
compression3.32×
stored9.4 MB
file10.0 MB
logical 48.0 MB · canonical 31.2 MB · metadata 420 KB · free 180 KB · 0 commits · 1 layers
orchestratorproject · branch
