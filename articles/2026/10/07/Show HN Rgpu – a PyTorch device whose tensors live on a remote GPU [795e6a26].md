---
id: "795e6a260c28f8b2"
title: "Show HN: Rgpu – a PyTorch device whose tensors live on a remote GPU"
url: "https://github.com/ymcrcat/rgpu"
link: "https://github.com/ymcrcat/rgpu"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-07T05:15:44Z"
published_date: "2026-10-07"
collected_at: "2026-10-13T20:17:27Z"
authors: ["boxstream"]
language: "en"
summary: "rGPU runs GPU work on a remote NVIDIA machine while the application stays on the client."
tags: []
orgs: ["Nvidia"]
topics: ["chips & infrastructure"]
content_source: "fulltext"
word_count: 220
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=49988516"
score: 57
comments: 4
community: "Hacker News"
---

# Show HN: Rgpu – a PyTorch device whose tensors live on a remote GPU

GitHub · boxstream · 2026-10-07

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert
Engineering records and experiments are indexed in docs/README.md.
Quick start: PyTorch device
Install rGPU with pip install rgpu, or pip install -e ./python from this
checkout, then follow the quickstart to
deploy the server. Save this as smoke.py in your workload directory:
The program selects the device; rgpu-run opens the tunnel and configures the
connection. The expected output is 8.0.
For existing Linux CUDA programs, follow the
CUDA shim guide, starting with
./scripts/build_client.sh.
Neither protocol authenticates or encrypts connections. Keep rgpu-opserver
on its default localhost bind and use SSH. The CUDA server listens on all IPv4
interfaces: restrict port 9713 with host/cloud firewall rules before starting
it, even when using an SSH tunnel. See deployment.
Development
# C++ client and fake-driver tests
./scripts/build_client.sh
# Python tests
python -m pip install -e './python[test]'
python -m pytest python/tests
# Static documentation
npm --prefix website ci
npm --prefix website run build
See scripts/README.md for the remaining build, cloud,
and hardware commands. Generated C++ is committed; its policy and regeneration
steps are in codegen/README.md.
Repository map
Historical implementation notes and experimental results are indexed in
docs/README.md.
