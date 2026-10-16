---
id: "54e0547a940cb779"
title: "Show HN: Deslop – Oxlint rules for AI-generated TypeScript"
url: "https://github.com/maharshi365/deslop"
link: "https://github.com/maharshi365/deslop"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-13T17:52:57Z"
published_date: "2026-10-13"
collected_at: "2026-10-13T20:17:27Z"
authors: ["maharshi365"]
language: "en"
summary: "Catches unsafe types, duplicate code, and low-value tests."
tags: []
orgs: []
topics: []
content_source: "fulltext"
word_count: 116
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50075809"
score: 10
comments: 2
community: "Hacker News"
---

# Show HN: Deslop – Oxlint rules for AI-generated TypeScript

GitHub · maharshi365 · 2026-10-13

Opinionated Oxlint rules that reject low-evidence, low-signal, AI-slop code patterns.
Rules are vendored from dmmulroy/anti-slop (generic rules) alongside additional deslop rules, all renamed under the deslop/* namespace. The vendored source is MIT licensed; see Credits below.
npm install --save-dev ai-deslop
# @oxlint/plugins comes along as a runtime dependency — keep it in sync with your oxlint version
Ships compiled JavaScript — works with any oxlint JS-plugin runtime (Bun, Deno, or Node.js).
import { defineConfig } from "oxlint";
import { configs as deslopConfigs } from "ai-deslop";
export default defineConfig({
  jsPlugins: ["ai-deslop"],
  options: deslopConfigs.recommended.options,
  rules: deslopConfigs.recommended.rules
});
Standard rules enabled by the recommended config
- Generic rules vendored verbatim from dmmulroy/anti-slop (MIT, © Dillon Mulroy), including src/shared/*.
MIT
