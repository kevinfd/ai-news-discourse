---
id: "552d67f3639c6388"
title: "Scale isn’t one number: three ways a Kubernetes control plane runs out of room"
url: "https://thenewstack.io/scaling-kubernetes-control-planes"
link: "https://thenewstack.io/scaling-kubernetes-control-planes"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-18T14:00:00Z"
published_date: "2026-10-18"
collected_at: "2026-10-19T12:07:39Z"
authors: ["Joe Betz"]
language: "en"
summary: "Three clusters in trouble, and they look nothing alike. \n\n The first is a training fleet. It sat at a few thousand nodes for months, then a new run landed, and it’s at fifteen thousand. Kube-apiserver starts eating memory. Etcd starts complaining. \n\n The second never passes a few thousand nodes and is having a much worse day. It’s an agent platform, and its objects are alive: sessions created,…"
tags: ["Cloud Native Ecosystem", "Kubernetes", "Platform Engineering", "sponsor-cncf", "sponsored-post-contributed"]
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 1264
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Scale isn’t one number: three ways a Kubernetes control plane runs out of room

The New Stack · Joe Betz · 2026-10-18

Scale isn’t one number: three ways a Kubernetes control plane runs out of room
Three clusters in trouble, and they look nothing alike.
The first is a training fleet. It sat at a few thousand nodes for months, then a new run landed, and it’s at fifteen thousand. Kube-apiserver starts eating memory. Etcd starts complaining.
The second never passes a few thousand nodes and is having a much worse day. It’s an agent platform, and its objects are alive: sessions created, suspended, resumed, and destroyed thousands of times a minute, every transition a write.
The third is neither big nor fast: a platform cluster with two hundred operators installed and tens of thousands of objects that mostly just sit there, and every apiserver holds a copy of all of them.
Two of those are AI workloads, and one isn’t, which is the least interesting part. They’re running out of room in three different directions, and fixing one does nothing for the others.
KubeCon + CloudNativeCon is taking place in Salt Lake City from November 9 to 12. Register now!
Go looking for guidance, and you find… not much. There’s plenty of advice for getting to 5,000 nodes. Past that, or sideways from it, the internet shrugs.
So you add more apiservers. It’s a documented option in kOps and the standard answer you’ll get from most people. It makes your problem worse, because every apiserver you add replicates the entire watch cache. You bought request capacity and paid for it in memory you didn’t have.
None of these is a research project. Clusters well past 5,000 nodes run in production today on stock upstream components. Nobody got there with a magic fork; they got there by being deliberate about what each store holds.
The scale isn’t the hard part. The assembly instructions are missing.
Three kinds of scale
Ask how big a control plane needs to be and the answer comes back in nodes. That’s how the second and third clusters end up tuned for a problem they don’t have.
“The scale isn’t the hard part. The assembly instructions are missing.”
Node-bound. Training and RL fleets: large, homogeneous, and the pressure is every kubelet reporting in. At 100,000 nodes with a 10-second heartbeat, liveness alone generates about 10,000 writes per second, and in our measurements lease renewals were roughly 70% of write QPS. Most of what that control plane does is nodes politely saying “still here,” forever.
Churn-bound. Agent platforms: modest size, very intense day. Systems that pack many agent sessions onto a smaller pool of worker pods express each actor’s lifecycle as a custom resource, so the busiest and shortest-lived objects are CRDs, and the write rate has nothing to do with how many machines you own.
State-bound. Platform clusters: many kinds, many objects, most of them asleep. The cost isn’t writes; it’s resident bytes multiplied by every apiserver holding them. This is the axis where the add-an-apiserver reflex actively hurts.
They’re independent: you can max any one with the other two on the floor. A recipe that only knows node count will happily tune the wrong thing.
Seams and recipes
Seams are the places where you can take Kubernetes apart: a contract between two components, usually at a network boundary, and substitutable, so you can replace what’s behind it without patching upstream.
Think of them the way a tailor thinks about seams in a jacket: take it in at the waist, let out the shoulders, still the same jacket. Cut somewhere that isn’t a seam, and you’ve made a very expensive rag.
“Think of them the way a tailor thinks about seams in a jacket. Cut somewhere that isn’t a seam, and you’ve made a very expensive rag.”
Recipes are scale-tested configurations built around those seams: executable configs that pass their scale test or fail it, with CI telling you the day they stop being true.
The four seams
Seam 1: the storage contract. Which store holds which resource types. Relieves churn. Not all of your cluster state deserves the same durability guarantees. Events and node leases are ephemeral, leader-election leases are ephemeral and chatty, and none need the same durable, Raft-replicated store as your Deployments. KEP-4743 defines the storage-interface boundary, and –etcd-servers-overrides routes resource types to different backends today. etcd isn’t the problem, and none of this argues for replacing it; a general-purpose consistent store shouldn’t absorb traffic when no business is durable.
The gap: –etcd-servers-overrides only knows about built-in resources, so a churn-bound platform can’t route the very custom resources generating its write storm. Watch for an enhancement in a future release.
Seam 2: the node liveness contract. How liveness reaches the control plane. Relieves node count. Two fixes for that heartbeat load, and they compose. Absorb it: a node-facing tier in front of the control plane handles renewals and propagates only real state transitions. Make it cheaper: route renewals through etcd’s in-memory lease refresh instead of a full Raft commit. That one lands in etcd itself, so it helps every cluster, down to the three-node one.
Seam 3: the shard axis. The field that controllers, caches, and stores agree to shard on. Relieves all three. Horizontal scaling means every layer agrees on how objects are divided. Pick the wrong axis and your controller spends its life reaching for objects in someone else’s shard. KEP-5866 introduces hash-range filtering for API traffic, the foundation. Coordination, resharding, and sharding the controller manager are out of scope, and all three need work.
Seam 4: cache residency. What an apiserver actually keeps in memory. Relieves state. Remember the apiserver that replicates the whole watch cache? That’s this seam, and the state-bound cluster’s entire problem. One that only ever talks to the scheduler doesn’t need every object resident, and a two-shard prototype cuts heap by roughly half per shard. There’s a floor: with every disableable cache off, an apiserver still carries about 0.9 KB per RBAC object, because the authorizer’s informers hold them regardless.
The gap: residency doesn’t exist upstream yet. KEP-5866 filters egress, so the cache still stores everything. Prototype branches and a draft KEP update are up for review.
The recipe ladder
That last row is on the ladder on purpose: publishing the rung nobody has built is how it stays useful. The bigger gap is the index. You pick a rung by node count, the one axis of three with measurements behind it. No one, us included, has published a scale-tested recipe for a churn-bound or state-bound cluster.
None of this is a distribution: stock upstream binaries, shipped as CI-tested configuration, so a release that changes the calculus shows up as a test failure first.
Where you can push
- Per-CRD storage configuration, for Seam 1. No KEP yet so that the use cases will shape it. If your hot objects are custom resources, bring your write rates to SIG API Machinery. Numbers off a real churn-bound cluster are the most useful thing anyone could contribute.
- KEP-5866 and the residency extension, for Seams 3 and 4. Prototype branches are up for review, and the design is not settled.
- Recipes nobody has published. Above 20,000 nodes, or serious churn, or a cluster that’s simply heavy: you know something the rest of us don’t.
We’ll be at KubeCon NA. Bring your worst control-plane graph and tell us which seam we got wrong.
Training fleets, agent platforms, and the unglamorous platform cluster are running out of room in three different directions, and all three should get there with stock upstream components. Most of the pieces are already on the workbench. Let’s put them together!
