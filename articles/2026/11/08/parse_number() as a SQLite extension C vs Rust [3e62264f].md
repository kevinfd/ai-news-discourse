---
id: "3e62264ffb8eefe5"
title: "parse_number() as a SQLite extension: C vs Rust"
url: "https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust"
link: "https://simonwillison.net/2026/Nov/8/sqlite-parse-number-c-vs-rust"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-08T22:26:00Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Simon Willison"]
language: "en"
summary: "Research: parse_number() as a SQLite extension: C vs Rust \n I was out walking the dog when I got curious about how easy/difficult it would be to write a SQLite C extension that adds a parse_number() function for turning strings like -$1,234.56 or '12.5%' into numeric values that could be summed and sorted. \n I fired up regular Claude chat (Opus 5.5) and prompted : \n \n I'm thinking about a SQLite…"
tags: ["c", "research", "sqlite", "rust", "claude"]
orgs: ["Anthropic", "Alibaba"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 317
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# parse_number() as a SQLite extension: C vs Rust

Simon Willison · Simon Willison · 2026-11-08

8th November 2026
I was out walking the dog when I got curious about how easy/difficult it would be to write a SQLite C extension that adds a parse_number() function for turning strings like -$1,234.56 or '12.5%' into numeric values that could be summed and sorted.
I fired up regular Claude chat (Opus 5.5) and prompted:
I'm thinking about a SQLite custom function 'parse_number(value)' that strips ',', '$', '£' and '%', handles a leading '-', and returns 'NULL' for anything it can’t parse
Explore the difference between building this as a SQLite extension in C v.s. in Rust - I want to compare performance and code complexity and size of the resulting.so(or whatever) file
This gave me a solid starting point - the Rust extension was 321 KB (using Rusqlite) and 298 KB (using sqlite-loadable-rs), while the C extension was 14 KB. But the Rust extension was faster!
Turns out that's because the Rust equivalent of C's strtod is "twice as fast". So I prompted:
Try writing your own C function for parsing text into a decimal number that catches up to or beats the Rust implementation
And it did, using "Clinger's fast path":
Net cost per row over 2 million rows, lower is better:
Finally, I had it rewrite the prototype as a research report to match the others in simonw/research by prompting this:
Clone simonw/research from GitHub and turn your above investigation into a research report as seen in that repository - you can give me a zip file to download that contains your new folder
Here's the resulting report.
Recent articles
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
- The U.S. Census Bureau and “Super Intelligence” - 2nd November 2026
- The October inflection point for vibe game development - 28th October 2026
