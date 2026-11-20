---
id: "4ba1303d2ee21d77"
title: "PostgreSQL 19 Released"
url: "https://simonwillison.net/2026/Nov/19/postgresql-19"
link: "https://simonwillison.net/2026/Nov/19/postgresql-19"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-19T20:43:57Z"
published_date: "2026-11-19"
collected_at: "2026-11-20T13:03:52Z"
authors: ["Simon Willison"]
language: "en"
summary: "PostgreSQL 19 Released \nMost years PostgreSQL ships a new release in September, but this year's release came two months later thanks mainly to the flurry of issues that the PostgreSQL team needed to address as part of the ongoing AI-reported vulnerability apocalypse. \n This release was definitely worth the wait. My favorite new feature is this one: \n \n For applications that send reads to…"
tags: ["mysql", "postgresql", "replication", "scaling", "wikipedia", "ai-security-research"]
orgs: ["Anthropic", "Alibaba"]
topics: ["products & launches", "models & research"]
content_source: "fulltext"
word_count: 386
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# PostgreSQL 19 Released

Simon Willison · Simon Willison · 2026-11-19

19th November 2026 - Link Blog
PostgreSQL 19 Released (via) Most years PostgreSQL ships a new release in September, but this year's release came two months later thanks mainly to the flurry of issues that the PostgreSQL team needed to address as part of the ongoing AI-reported vulnerability apocalypse.
This release was definitely worth the wait. My favorite new feature is this one:
For applications that send reads to standbys, PostgreSQL 19 adds "read-your-writes" consistency with the new WAIT FOR LSN command. A session on a standby can use WAIT FOR LSN to wait until the standby has replayed the write-ahead log (WAL) up to a specific log sequence number (LSN) before running a query, so the application can read data it just wrote on the primary.
In practice, that looks like this:
UPDATE movie SET genre = 'Dramatic' WHERE genre = 'Drama';
SELECT pg_current_wal_insert_lsn();
That returns a value like 0/0306EE20. Store that somewhere (a signed cookie would work) such that on a subsequent request your application can do:
WAIT FOR LSN '0/0306EE20' WITH (TIMEOUT '0.1s');
SELECT * FROM movie WHERE genre = 'Drama';
The timeout is optional - if you provide one you'll get an error if the replica you are talking to doesn't catch up within the specified time.
I first encountered this pattern in Wikipedia, which has a hand-rolled version of this built against MySQL replication:
In addition to this, MediaWiki attempts to ensure that the user sees events occurring on the wiki in chronological order. A few seconds of lag can be tolerated, as long as the user sees a consistent picture from subsequent requests. This is done by saving the primary binlog position in the session, and then at the start of each request, waiting for the replica to catch up to that position before doing any reads from it.
Here's the relevant MediaWiki code, which these days uses MySQL's WAIT_FOR_EXECUTED_GTID_SET() function and falls back to SOURCE_POS_WAIT().
Recent articles
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
