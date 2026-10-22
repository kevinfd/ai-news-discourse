---
id: "766b28ce0c10f383"
title: "Berth v0.3.4: hand your GPU to a Windows VM and get it back (VFIO)"
url: "https://reddit.com/r/LocalLLaMA/comments/1xc4u2o/berth_v034_hand_your_gpu_to_a_windows_vm_and_get"
link: "https://reddit.com/r/LocalLLaMA/comments/1xc4u2o/berth_v034_hand_your_gpu_to_a_windows_vm_and_get"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-22T01:02:19Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["Distinct-Pie2389"]
language: "en"
summary: "GPU passthrough to a VM (experimental, Linux). berth vfio run -- your VM script drains your engines at a safe point, checks that nothing still holds the card, then runs your script. The script does the sudo and the driver switch; Berth never touches drivers or passwords. The card goes back to your engines only once it is on the NVIDIA driver again, and while the VM has it, berth status and the…"
tags: ["r/LocalLLaMA"]
orgs: ["Nvidia"]
topics: ["chips & infrastructure"]
content_source: "post"
word_count: 220
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xc4u2o/berth_v034_hand_your_gpu_to_a_windows_vm_and_get/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# Berth v0.3.4: hand your GPU to a Windows VM and get it back (VFIO)

Reddit · Distinct-Pie2389 · 2026-10-22

GPU passthrough to a VM (experimental, Linux). berth vfio run -- your VM script drains your engines at a safe point, checks that nothing still holds the card, then runs your script. The script does the sudo and the driver switch; Berth never touches drivers or passwords. The card goes back to your engines only once it is on the NVIDIA driver again, and while the VM has it, berth status and the web UI say so. On my 4090 it is one keybind: a password prompt, Windows on the monitor, and llama-swap back when Windows shuts down. Example launcher and libvirt config are in contrib/vfio. Also New Gateway fallback: During a slow cold start, a request can go to a CPU engine instead of waiting. Minimum turn per engine: Prevents the card from constantly flipping between models. Escaped child processes: Child processes that escape their engine stay on its lease via systemd scopes. API key security: The gateway no longer passes your node's API key on to engines. Windows fixes (from testers): Per-process VRAM counts only Berth's card. Processes like dwm.exe have proper names. Epic's tray app no longer grabs the card. Links & Resources Docs with search: t-crypt.github.io/berth GitHub Repo: T-Crypt/berth Proxmox Users: If you run Proxmox, check out issue #128 to share how you use your GPUs
