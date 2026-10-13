---
id: "8d61a5148a25f76f"
title: "OrcaRouter Releases OrcaCyber Zero 1.5 Cybersecurity Model With 1M Context"
url: "https://marktechpost.com/2026/10/10/orcarouter-releases-orcacyber-zero-1-5-cybersecurity-model-with-1m-context"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-11T06:20:21Z"
published_date: "2026-10-11"
collected_at: "2026-10-13T20:17:27Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "OrcaRouter has released OrcaCyber Zero 1.5 , a model for authorized vulnerability research. The model is the successor to OrcaCyber Zero 1.0 , which shipped on September 17, 2026. OrcaCyber Zero 1.5 is a post-trained Orca model for vulnerability reproduction, exploit development and penetration testing. It ships with a 1M-token context window, native function calling and structured outputs. For…"
tags: ["Agentic AI", "AI Infrastructure", "AI Shorts", "Applications", "Artificial Intelligence", "Editors Pick", "For Devs", "Language Model", "Large Language Model", "Machine Learning", "New Releases", "Security"]
orgs: ["OpenAI", "Anthropic"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "summary"
word_count: 755
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# OrcaRouter Releases OrcaCyber Zero 1.5 Cybersecurity Model With 1M Context

MarkTechPost · Asif Razzaq · 2026-10-11

OrcaRouter has released OrcaCyber Zero 1.5 , a model for authorized vulnerability research. The model is the successor to OrcaCyber Zero 1.0 , which shipped on September 17, 2026. OrcaCyber Zero 1.5 is a post-trained Orca model for vulnerability reproduction, exploit development and penetration testing. It ships with a 1M-token context window, native function calling and structured outputs. For security teams, this model brings a simple message: fewer reports, more validated and fixed vulnerabilities . 

 TL;DR 

 Size: Parameter count not disclosed. 1M-token context, 128K max output, text in and text out. 

 Runs on: Hosted API only through OrcaRouter. No weights, no quantized variants, hardware not disclosed. 

 Performance: Vendor-reported scores are near ceiling on cyber benchmarks and strong on coding. 

 Best: 100% on Cybench (39/39 tasks, unrestricted agent execution). 

 Worst: 76.5% on SWE-bench Pro V2, its lowest published score. 

 Bottom line (best): Top-tier cyber scores at $3.00 / $7.50 per 1M tokens. 

 Bottom line (worst): Every number is self-reported, and CVE-Bench used only 24 evaluable tasks. 

 What is OrcaCyber Zero 1.5? 

 OrcaCyber Zero 1.5 is a frontier cybersecurity model and the successor to Zero 1.0 . Orca team states that it has post-trained for security research and authorized security engineering. Listed uses include vulnerability reproduction, exploit development, penetration testing, security auditing and cyber reasoning. 

 The 3 design goals: 

 Find what others miss: unknown flaws like RCE, sandbox escapes, auth bypasses, privilege escalation and attack chains. 

 Go beyond detection: reason through attack paths, challenge its own hypotheses and rank flaws by demonstrable exploitability. 

 Built for autonomous agents: 1M-token context, native tool calling and extended reasoning for large codebases. 

 How does OrcaCyber Zero 1.5 perform on benchmarks? 

 The model page lists 4 vendor-reported results, last evaluated October 10, 2026: 

 Cybench: 100% (39/39, unrestricted agent execution). 

 CVE-Bench: 95.8% (23/24 evaluable tasks). 

 HumanEval+: 93.9%. 

 SWE-bench Pro V2: 76.5%. 

 Cybench contains 40 professional CTF tasks, so the 100% covers 39 of them. CVE-Bench is built on 40 critical-severity web CVEs. Orca’s 95.8% covers a 24-task evaluable subset. The SWE-bench Pro V2 score is not directly comparable with standard SWE-bench Pro results. 

&&

 How does it compare with other cyber models? 

 Feature OrcaCyber Zero 1.5 OrcaCyber Zero 1.0 Claude Mythos Preview GPT-5.5-Cyber Sakana Fugu-Cyber Developer Orca (OrcaRouter) Orca (OrcaRouter) Anthropic OpenAI Sakana AI Release Oct 10, 2026 Sep 17, 2026 Apr 7, 2026 Jun 22, 2026 (full) Jul 21, 2026 Type Post-trained model Post-trained coding model General frontier model Cyber-tuned GPT-5.5 Multi-agent orchestration Parameters Not disclosed Not disclosed Not disclosed Not disclosed Not disclosed Context 1M 1M Not disclosed Not disclosed Not disclosed CyberGym Not disclosed 98.07% (harness, pass@1) 83.1% 85.6% 86.9% Other headline score Cybench 100% Not disclosed SWE-bench Pro 77.8% Not disclosed CTI-REALM 72.1% Price (in / out per 1M) $3.00 / $7.50 $3.00 / $7.50 $25 / $125 after credits Not disclosed Not disclosed Access Gated Security Research tier Gated, closed beta Glasswing partners Vetted defenders only Application review 

 All competitor figures come from each vendor’s own announcement. None are independent replications. 

 How do developers access OrcaCyber Zero 1.5? 

 The model uses an OpenAI-compatible API . Developers set base_url to https://api.orcarouter.ai/v1 and call orca/orcacyber-zero-1.5 . 

 Access is gated to the Security Research tier. Orca lists an engagement, a passkey and accepted terms as requirements. The tier targets trusted security researchers, red teams and authorized testing. 

 Pricing is $3.00 per 1M input tokens and $7.50 per 1M output tokens. Cache reads cost $0.75 per 1M tokens. Over the past 7 days, p50 time-to-first-token was 500 ms and p95 was 2.36 s. That sample is small, at 1.3K tokens of traffic. 

 Zero 1.0 recorded a 3.43 s p50 over a much larger traffic window. The 2 latency figures are not a clean comparison. 

 Key Takeaways 

 OrcaCyber Zero 1.5 is a gated, 1M-context cybersecurity model on OrcaRouter. 

 It reports 100% on Cybench and 95.8% on a 24-task CVE-Bench subset. 

 Pricing is $3.00 / $7.50 per 1M tokens, far below Mythos Preview’s $25 / $125. 

 The 98% CyberGym claim belongs to Zero 1.0 inside Orca’s harness. 

 All results are vendor-reported, with no technical report yet. 

 Check out the model page , the launch post on X and the OrcaRouter docs . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 
 The post OrcaRouter Releases OrcaCyber Zero 1.5 Cybersecurity Model With 1M Context appeared first on MarkTechPost .
