---
id: "abc9750b7fe9f819"
title: "inferencekit: open-source plugin to optimize any model on any hardware using coding agents"
url: "https://reddit.com/r/LocalLLaMA/comments/1xut6z0/inferencekit_opensource_plugin_to_optimize_any"
link: "https://reddit.com/r/LocalLLaMA/comments/1xut6z0/inferencekit_opensource_plugin_to_optimize_any"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-13T00:14:11Z"
published_date: "2026-11-13"
collected_at: "2026-11-13T13:04:09Z"
authors: ["ElectricalBar7464"]
language: "en"
summary: "KittenML just released inferencekit , a free opensource plugin to turn coding agents(Claude Code, Codex, OpenCode) into inference engineers for your hardware. Most models ship with inference tuned for whatever hardware the authors used, which is usually not what you have locally. The fastest path on a 3070 might be different from the fastest path on a Mac or a Radeon. inferencekit allows you to…"
tags: ["r/LocalLLaMA"]
orgs: ["Anthropic"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 152
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xut6z0/inferencekit_opensource_plugin_to_optimize_any/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# inferencekit: open-source plugin to optimize any model on any hardware using coding agents

Reddit · ElectricalBar7464 · 2026-11-13

KittenML just released inferencekit , a free opensource plugin to turn coding agents(Claude Code, Codex, OpenCode) into inference engineers for your hardware. Most models ship with inference tuned for whatever hardware the authors used, which is usually not what you have locally. The fastest path on a 3070 might be different from the fastest path on a Mac or a Radeon. inferencekit allows you to find that path for your setup. This was used to get streaming TTFB of Kitten-TTS-2 down to ~10ms on RTX Pro 6000. other results are shown in the image attached. Once you've optimized a model on your hardware, please make a PR to the inferencekit-engine repo linked below, so anyone running the same model on the same hardware, can just reuse it. The idea is to crowdsource the best inference engine for every model + hardware setup Plugin's Github: https://github.com/KittenML/inferencekit Inference Engine's Github: https://github.com/KittenML/inferencekit-engines KittenML Discord: https://discord.com/invite/VJ86W4SURW
