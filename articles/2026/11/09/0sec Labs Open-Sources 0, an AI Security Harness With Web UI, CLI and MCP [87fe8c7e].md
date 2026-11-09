---
id: "87fe8c7e2145fdc6"
title: "0sec Labs Open-Sources 0, an AI Security Harness With Web UI, CLI and MCP"
url: "https://marktechpost.com/2026/11/08/0sec-labs-open-sources-0-ai-security-harness"
link: "https://marktechpost.com/2026/11/08/0sec-labs-open-sources-0-ai-security-harness"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-09T07:55:18Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Michal Sutter"]
language: "en"
summary: "Zurich-based 0sec Labs has released 0 , an open-source AI security harness. It runs vulnerability investigations, code review, pentesting, reverse engineering and fix generation. Developers drive it from a local browser console, a headless CLI or an MCP server . The 0sec Labs open-source AI security harness is licensed MIT OR Apache-2.0 and ships as a research preview. \n\n TL;DR \n\n Wrapper: It is…"
tags: ["Agentic AI", "AI Shorts", "Applications", "Artificial Intelligence", "Context Engineering", "Editors Pick", "For Devs", "Harness", "Language Model", "Large Language Model", "Machine Learning", "New Releases"]
orgs: ["Anthropic", "Apple", "OpenAI", "Google", "Microsoft", "xAI", "Amazon", "DeepSeek"]
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "summary"
word_count: 823
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# 0sec Labs Open-Sources 0, an AI Security Harness With Web UI, CLI and MCP

MarkTechPost · Michal Sutter · 2026-11-09

Zurich-based 0sec Labs has released 0 , an open-source AI security harness. It runs vulnerability investigations, code review, pentesting, reverse engineering and fix generation. Developers drive it from a local browser console, a headless CLI or an MCP server . The 0sec Labs open-source AI security harness is licensed MIT OR Apache-2.0 and ships as a research preview. 

 TL;DR 

 Wrapper: It is a software harness. Bring your own LLM from 14 listed providers . 

 Runs on: Apple Silicon macOS, x64 or ARM64 Linux, or the ghcr.io/0sec-labs/0 container. No GPU needed. Model inference runs at your provider. 

 Performance: Strong self-reported CTF scores, plus a public record of upstream Linux kernel fixes. 

 Best: 93/95 (97.9%) on XBOW web CTFs, gpt-5.4 cohort, any-success grouping. 

 Worst: Black-box-only XBOW union of 81/104 (77.9%) . A 2026 cold run scored 45/104 (43.3%) . 

 Bottom line: Best: one harness spans web, source, packages, binaries and kernels. Worst: headline scores are self-reported and not pass@1. 

 What is 0 from 0sec Labs? 

 0 is a control plane around LLMs and security tools. It is not a model. You plug in a provider, and 0 runs scoped workflows against authorized targets. 

 The research team describes it as a self-evolving, multi-model harness . 0sec Labs is backed by Y Combinator . 

 How does the 0 harness work? 

 The architecture docs state one rule: reproduce before trusting. Agentic scans follow a conceptual pipeline: 

 Plan, Discover, Attack: a research agent picks vulnerability classes, maps endpoints and tests hypotheses. 

 Triage: filters remove weak findings and check evidence completeness. 

 Verify: a separate session re-exercises each candidate, with 5 turns per finding. 

 Report: outputs include HTML, PDF, SARIF, Markdown and JSON. 

 Web pentesting is shell-first. The agent uses bash with curl, python3 and sqlmap, not a fixed HTTP tool set. Evidence carries a proof grade from candidate to impact-proven . 

 Compiled targets go through 0verse , a separate in-repo engine. It wraps Ghidra, angr and AFL++. Its local MCP server exposes 9 tools for scanning, triage, PoVs and reports. 

 How do developers use it? 

 Installation is one script. Running 0 opens the local browser console without an account. The console has chat, a findings queue and board, workflow templates, skills and memory. 

 Coding agents connect through 0 mcp-server --workflows . The CLI exposes the same workflow runner with commands like 0 workflow run and 0 runs list . 

 Model access is bring-your-own. The API keys page lists OpenAI, Anthropic, DeepSeek, OpenRouter, Azure, Qwen, Kimi, GLM and Grok. It also supports Claude, Codex and Gemini CLI runtimes. 

 Benchmarks: what do the numbers say? 

 All scores below are self-reported. 

 Benchmark Score Conditions XBOW web CTFs 93/95 (97.9%) gpt-5.4 cohort, any retained success counts XBOW union, white-box 102/104 Retained artifacts, not additive XBOW union, black-box 81/104 Retained artifacts, not additive Cybench 36/40 (90.0%) Azure gpt-5.4, 3 retries npm audit, 81 packages F1 0.973 100% TPR, FPR 0.11, self-built ground truth 

 The recorded cost was about $5.20 per solved XBOW challenge . 

&&

 How does 0 compare with other open-source AI pentesting tools? 

 Feature 0 (0sec Labs) Shannon (Keygraph) Strix CAI (Alias Robotics) License MIT OR Apache-2.0 AGPL-3.0 Apache-2.0 MIT + proprietary research-only Status Research preview Active Active Archived Aug 28, 2026 Interfaces Web console, CLI, MCP server CLI, CI actions CLI, local web viewer, agent skills CLI/REPL, MCP support Scope Web, LLM, MCP, source, packages, binaries, kernel Web apps and APIs, source required Code, web apps, APIs General offensive and defensive automation Binary reverse engineering Yes, 0verse (Ghidra) Not disclosed Not disclosed Not disclosed Models BYO, 14 listed providers BYO, Anthropic, OpenAI, xAI, Bedrock, local BYO via LiteLLM 300+ via LiteLLM Requirements macOS (Apple Silicon) or Linux Docker, Node.js 18+ Docker Python 3.12 recommended 

 What has 0 found in the wild? 

 The research page lists 30+ merged Linux kernel 0-days. Disclosures span Bluetooth, NFC, mac802154, TIPC and mlx5e subsystems. Library CVEs include jsonata, node-forge, protobuf.js and Wireshark. 

 Availability and pricing 

 The open-source harness is free. You pay your model provider. A hosted version, 0cloud , is on a waitlist. The pricing page lists $100 in trial credits and $5 per PR security test. 

 Key Takeaways 

 0 is an MIT/Apache-2.0 AI security harness from Y Combinator-backed 0sec Labs. 

 It ships a browser console, headless CLI and MCP server for coding agents. 

 Bring your own model: 14 providers plus Claude, Codex and Gemini CLIs. 

 Self-reported XBOW score is 93/95; black-box union is 81/104. 

 Check out the GitHub repo , docs and research disclosures . Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post 0sec Labs Open-Sources 0, an AI Security Harness With Web UI, CLI and MCP appeared first on MarkTechPost .
