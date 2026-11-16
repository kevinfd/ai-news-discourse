---
id: "3bc6cdb34c17f840"
title: "datasette 1.0a43"
url: "https://simonwillison.net/2026/Nov/15/datasette"
link: "https://simonwillison.net/2026/Nov/15/datasette"
source: "Simon Willison"
domain: "simonwillison.net"
source_type: "newsletter"
collector: "rss"
date: "2026-11-15T23:20:27Z"
published_date: "2026-11-15"
collected_at: "2026-11-16T13:13:10Z"
authors: ["Simon Willison"]
language: "en"
summary: "Release: datasette 1.0a43 \n I've been leaning hard into Claude Fable 5.2 to help knock things off the 1.0 milestone , which is now 53% complete. \n The biggest 1.0 item in this release is streaming support for output renderers - the built-in TSV and CSV export mechanisms now use this as well, and plugins can register themselves as capable of streaming every row in a table in one go via the new…"
tags: ["security", "datasette", "css", "browsers", "annotated-release-notes", "firefox", "javascript", "safari", "chrome"]
orgs: ["Anthropic", "Alibaba"]
topics: ["products & launches", "models & research"]
content_source: "fulltext"
word_count: 369
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# datasette 1.0a43

Simon Willison · Simon Willison · 2026-11-15

15th November 2026
I've been leaning hard into Claude Fable 5.2 to help knock things off the 1.0 milestone, which is now 53% complete.
The biggest 1.0 item in this release is streaming support for output renderers - the built-in TSV and CSV export mechanisms now use this as well, and plugins can register themselves as capable of streaming every row in a table in one go via the new Response.stream() method.
There are a couple of security fixes, one of which I deemed deserving of a GitHub advisory: private stored queries could be exposed, granting access to the title and SQL of the query (but not allowing that query to be executed).
There are dozens of smaller improvements. The row page JSON representation finally has a design suitable for 1.0. A new <datasette-copy-button> Web Component provides copy-schema in various places. JSON in columns on the row page can be pretty-printed. There's a new DatasetteModal.confirm() JavaScript utility method. Plus dozens of bug fixes, including contributions by Zihan Dai, Peter Olkhovets, Ilya Khalafi, and Ankita Advitot.
The feature I'm most excited about is a pretty tiny one: I've added CSS multi-page view transitions to Datasette! Here's the commit - key CSS is as follows:
/* Enable cross-document view transitions,
   for anyone without prefers-reduced-motion */
@media (prefers-reduced-motion: no-preference) {
    @view-transition {
        navigation: auto;
    }
}
/* .facet-results should morph from old position to new */
html:active-view-transition .content > .facet-results {
    view-transition-name: facet-results;
}
/* So should a .table-wrapper, provided it contains .rows-and-columns */
html:active-view-transition .table-wrapper:has(> table.rows-and-columns) {
    view-transition-name: rows-table;
}
With that in place, navigations within Datasette - still staunchly a multi-page application - feel more like an SPA. This works on Safari and Chrome at the moment and I believe supports for Firefox is due to land in Firefox 162 on December 8th 2026 (seeing as they are no longer feature-flagged in Firefox Nightly.)
Recent articles
- Locating the source of a mysterious beep with Claude - 9th November 2026
- Hide your slop PR descriptions behind <details><summary> - 9th November 2026
- Qwen 3.8 27B on my laptop can interpret model weights, too - 3rd November 2026
- The U.S. Census Bureau and “Super Intelligence” - 2nd November 2026
