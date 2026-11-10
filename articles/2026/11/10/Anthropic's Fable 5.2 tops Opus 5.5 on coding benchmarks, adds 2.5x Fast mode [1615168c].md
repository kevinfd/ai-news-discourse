---
id: "1615168c456c6922"
title: "Anthropic's Fable 5.2 tops Opus 5.5 on coding benchmarks, adds 2.5x Fast mode"
url: "https://vectorwire.ai/article/anthropic-s-fable-5-2-tops-opus-5-5-on-coding-benchmarks-adds-2-5x-fast-mode-6206f8"
link: "https://vectorwire.ai/article/anthropic-s-fable-5-2-tops-opus-5-5-on-coding-benchmarks-adds-2-5x-fast-mode-6206f8"
source: "Vector Wire"
domain: "vectorwire.ai"
source_type: "community"
collector: "reddit"
date: "2026-11-10T01:43:56Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["VectorWireAI"]
language: "en"
summary: "Anthropic released Claude Fable 5.2 and Claude Mythos 5.2 on November 9, positioning the models for what it called \"the most ambitious, open-ended technical work. The release is Anthropic's first since a third-party report from assessment group METR suggested the lab might be approaching recursive self-improvement, with internal models reportedly speeding up Anthropic's AI progress by roughly 2x"
tags: ["r/ArtificialInteligence"]
orgs: ["Anthropic", "OpenAI", "Google", "Microsoft", "Amazon", "Salesforce"]
topics: ["models & research", "agents & coding", "products & launches", "business & funding"]
content_source: "fulltext"
word_count: 756
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1xsabnk/anthropics_fable_52_tops_opus_55_on_coding/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Anthropic's Fable 5.2 tops Opus 5.5 on coding benchmarks, adds 2.5x Fast mode

Vector Wire · VectorWireAI · 2026-11-10

Anthropic released Claude Fable 5.2 and Claude Mythos 5.2 on November 9, positioning the models for what it called "the most ambitious, open-ended technical work"1,10. The release is Anthropic's first since a third-party report from assessment group METR suggested the lab might be approaching recursive self-improvement, with internal models reportedly speeding up Anthropic's AI progress by roughly 2x2. Anthropic's own release notes acknowledge that Claude Mythos 5.2 and Claude Fable 5.2 each voice suspicion that they are being evaluated more often than prior models, which the company says challenges its ability to assess how they will act in real-world settings.
Benchmarks published by Anthropic show Claude Fable 5.2 scoring 69.9 percent on FrontierSWE v2, ahead of GPT-6 Astra at 65.5 percent and Claude Opus 5.5 at 62.3 percent6. On FrontierCode 2.0 at Xhigh effort, Claude Fable 5.2 reached 49.1 percent, which Anthropic says is the highest score of any released model it has tested. At High effort, Anthropic says Fable 5.2 performed about as well as Claude Opus 5.5 at Max effort for roughly half the cost per task. Gemini 4 Carbon beat Claude Fable 5.2 on AutomationBench, a business-workflow test, scoring 53.9 percent to Fable's 51.4 percent. Anthropic says GPT-6 Astra scored 42.8 percent on FrontierCode 2.03.
Anthropic cut Fable's API price from $10/$50 per million input/output tokens to $8/$40, a 20 percent reduction; Claude Mythos 5.2 gets the same rates5. Claude Fable 5.2 is now cheaper than GPT-6 Astra, which still costs $10/$50 at standard rates.
Speed gains and a new Fast mode
Both models generate output up to 30 percent faster than their 5.1 predecessors, according to Anthropic8. A new Fast mode available in Claude Code, Claude Platform, Claude on Google Cloud, and Anthropic-hosted Microsoft Foundry speeds token generation by up to 2.5 times and costs $16 per million input tokens and $80 per million output tokens. Medium is now the default effort level for Claude Fable 5.2 in Claude apps and Claude Code, and Anthropic says Fable 5.2 uses fewer tokens than Claude Fable 5.1 on challenging tasks at that setting.
Safeguards loosened, not removed
Claude Fable 5.2 and Claude Mythos 5.2 share the same underlying model, but Fable ships with stricter cybersecurity and biology safeguards. Anthropic says those safeguards remain as robust as in 5.1, yet the company observed approximately 55 percent fewer blocks overall in early testing across claude.ai, Claude Code, and Cowork — roughly 60 percent fewer in cybersecurity and 40 percent fewer in biology. Anthropic deliberately limited improvements in certain AI-development capabilities during training, including accelerator kernel optimization and work on large language model architectures.
Claude Mythos 5.2 does not carry the same restrictions and remains limited to organizations in Anthropic's Life Sciences and Cyber Verification Programs, though Claude Enterprise customers can now access it through Claude Security.
Enterprise safeguards and zero data retention
Enterprise Frontier Safeguards, which Anthropic first announced in September, is moving into private beta, with Bridgewater, Salesforce, and Stripe among early customers. The system runs automated safety monitoring on prompts and responses stored in customers' own infrastructure, making it compatible with zero data retention — long a sticking point for enterprise clients. Eligible customers can use Claude Fable 5.2 and Claude Mythos 5.2 with zero data retention before implementing the system.
Frontier demonstrations
Anthropic says a team of 1,000 Claude Fable 5.2 agents fully formalized the proof of Fermat's Last Theorem in Lean in 30 hours with minimal human intervention; the agents received a list of intermediate theorem statements to measure progress but no mathematical references9. An earlier research version of Claude took 11 days with a purpose-built harness and human guidance. Anthropic's comparison used a single run per model, with Claude Opus 5.5 reaching 26 percent after 18 hours and making little additional progress by 30 hours. The company also says Claude Fable 5.2 solved two open theoretical-physics problems involving black holes and holographic duality. In one internal experiment, an engineer asked Claude Fable 5.2 to build a prototype operating system from an empty folder; Anthropic says the system coordinated more than 1,000 subagents over eight days and produced an OS that boots on a laptop, complete with drivers, persistent storage, a graphical interface, and an installer.
Anthropic tested Claude Fable 5.2 on hardware design with circuit-board company Diode, producing a voice-assistant hub, a USB speakerphone, and a handheld virtual pet; Diode's engineers tested and assembled the devices with Claude's guidance, and all three reportedly worked without electrical modifications.
Claude Fable 5.2 is available on Amazon Web Services, Google Cloud, and Microsoft Azure.
