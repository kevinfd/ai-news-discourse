---
id: "4c8ceb9354924392"
title: "ChatGPT changed its HTML structure and broke some extensions AI Memory Vault is still working"
url: "https://reddit.com/r/ChatGPT/comments/1x5k5rn/chatgpt_changed_its_html_structure_and_broke_some"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-14T06:39:36Z"
published_date: "2026-10-14"
collected_at: "2026-10-14T12:07:01Z"
authors: ["Calm_Home3943"]
language: "en"
summary: "Recently, ChatGPT changed parts of its HTML/DOM structure. Some older selectors, like data-message-author-role, are no longer available in certain versions of the interface.This can break Chrome extensions that rely on those selectors to read or extract conversations. I ran into the same issue with my extension, AI Memory Vault. I've now updated it with newer selectors and fallback mechanisms,…"
tags: ["r/ChatGPT"]
orgs: ["OpenAI"]
topics: ["products & launches"]
content_source: "post"
word_count: 125
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ChatGPT/comments/1x5k5rn/chatgpt_changed_its_html_structure_and_broke_some/"
score: null
comments: null
community: "r/ChatGPT"
---

# ChatGPT changed its HTML structure and broke some extensions AI Memory Vault is still working

Reddit · Calm_Home3943 · 2026-10-14

Recently, ChatGPT changed parts of its HTML/DOM structure. Some older selectors, like data-message-author-role, are no longer available in certain versions of the interface.This can break Chrome extensions that rely on those selectors to read or extract conversations. I ran into the same issue with my extension, AI Memory Vault. I've now updated it with newer selectors and fallback mechanisms, including support for conversation turns, article containers, and Markdown content. The Update code is in github repo https://github.com/ai-encryption-tool/ai If you're looking for a way to save and manage your ChatGPT conversations and memories, feel free to try AI Memory Vault Extension: https://ai-memory-vault.com I'm also curious: has anyone else noticed ChatGPT's recent DOM changes breaking their extensions or automation scripts? Happy to hear feedback or suggestions! https://preview.redd.it/yq2u2mwzodvh1.png?width=2262&format=png&auto=webp&s=c9c1e9befce756269ed430df41af83bc65a2af3a
