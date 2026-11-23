---
id: "8cc270b184708c4b"
title: "Select Styling Specimens"
url: "https://simonwillison.net/2026/Nov/22/select-styling"
link: "https://simonwillison.net/2026/Nov/22/select-styling"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-22T19:45:06Z"
published_date: "2026-11-22"
collected_at: "2026-11-23T13:04:50Z"
authors: ["Simon Willison"]
language: "en"
summary: "Tool: Select Styling Specimens \n I got frustrated at how HTML <select> boxes default to looking different in different browsers, and are (I think) quite ugly in Chrome: \n \n So I had Claude Fable 5.2 build me this page showing all of the ways they can be styled: \n \n Build an HTML page that shows all of the ways a select box can be styled, I plan to take screenshots in every desktop and mobile…"
tags: ["tools", "css", "html"]
orgs: ["Anthropic", "Alibaba"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 197
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Select Styling Specimens

Simon Willison · Simon Willison · 2026-11-22

22nd November 2026
I got frustrated at how HTML <select> boxes default to looking different in different browsers, and are (I think) quite ugly in Chrome:
So I had Claude Fable 5.2 build me this page showing all of the ways they can be styled:
Build an HTML page that shows all of the ways a select box can be styled, I plan to take screenshots in every desktop and mobile browser
After some experimentation I've decided my favorite CSS for select boxes is this:
select {
  appearance: none;
  color: #1f2933;
  padding: 0.5em 2.25em 0.5em 0.75em;
  border: 1px solid #c4cbd3;
  border-radius: 6px;
  background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 8'%3E%3Cpath d='M1 1.5l5 5 5-5' fill='none' stroke='%23667085' stroke-width='1.5'/%3E%3C/svg%3E") no-repeat right 0.75em center / 0.75em;
}
Here's what that looks like in the three browsers:
Recent articles
- Running the full server-side Datasette Python app in the browser with service workers and Pyodide - 17th November 2026
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
