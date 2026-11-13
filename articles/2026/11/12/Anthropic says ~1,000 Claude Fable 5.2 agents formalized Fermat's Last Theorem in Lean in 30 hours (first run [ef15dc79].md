---
id: "ef15dc79c4a144e3"
title: "Anthropic says ~1,000 Claude Fable 5.2 agents formalized Fermat's Last Theorem in Lean in 30 hours (first run in September took 11 days)"
url: "https://reddit.com/r/ClaudeAI/comments/1xuf60h/anthropic_says_1000_claude_fable_52_agents"
link: "https://reddit.com/r/ClaudeAI/comments/1xuf60h/anthropic_says_1000_claude_fable_52_agents"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-12T15:07:42Z"
published_date: "2026-11-12"
collected_at: "2026-11-13T13:04:09Z"
authors: ["Antoine_mllt"]
language: "en"
summary: "Anthropic released Claude Fable 5.2 on Nov 9. The part of the announcement I keep coming back to isn't a benchmark, it's this: What they report - About 1,000 Fable 5.2 agents produced a complete Lean formalisation of Fermat's Last Theorem in 30 hours, with minimal human intervention. - They started from minimal prompts, with no mathematical references, and progress was scored against a list of…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "post"
word_count: 341
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xuf60h/anthropic_says_1000_claude_fable_52_agents/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Anthropic says ~1,000 Claude Fable 5.2 agents formalized Fermat's Last Theorem in Lean in 30 hours (first run in September took 11 days)

Reddit · Antoine_mllt · 2026-11-12

Anthropic released Claude Fable 5.2 on Nov 9. The part of the announcement I keep coming back to isn't a benchmark, it's this: What they report - About 1,000 Fable 5.2 agents produced a complete Lean formalisation of Fermat's Last Theorem in 30 hours, with minimal human intervention. - They started from minimal prompts, with no mathematical references, and progress was scored against a list of intermediate theorem statements. - Compared with the first formalization (September, an unreleased Claude model, 11 days), the new run used about a third of the action tokens and produced a proof roughly 7x shorter. - The same 1,000-agent setup with Opus 5.5 got to 26% in 18 hours and barely progressed after 30. Why it matters A formal proof is checked by the Lean kernel step by step, so "the agents claim they did it" and "it's correct" are not the same claim: the second one can be verified by anyone with enough compute. The September proof is public on GitHub (about 13M lines, 29,511 theorems, only Lean's three standard axioms). For context, the human-led FLT formalization project at Imperial started in 2024 and was expected to take years. To me the interesting signal is the Opus 5.5 vs Fable 5.2 gap on the same long, multi-agent job. That kind of difference doesn't show up well in single-task benchmarks. Limits - This is Anthropic's own report. The public repo is the September run; I couldn't find the 30-hour proof linked yet, and no cost figure is given. - It's not new mathematics. Wiles proved it in 1995. This is machine verification of a known proof, done much faster. - The September proof is far longer than a human-written formalization would be, which Anthropic acknowledges. Sources: Anthropic's announcement ( https://www.anthropic.com/news/claude-fable-and-mythos-5-2 ) and the September repo ( https://github.com/anthropics/fermats-last-theorem ). Not affiliated with Anthropic. Question for people who work with Lean or Mathlib: does a 30-hour, machine-generated formalization change how you think about formalizing new results, or is a proof this long mostly unusable as a library contribution?
