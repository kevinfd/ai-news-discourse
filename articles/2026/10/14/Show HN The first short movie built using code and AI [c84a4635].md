---
id: "c84a4635b7697ec3"
title: "Show HN: The first short movie built using code and AI"
url: "https://fframes.studio/the-why"
source: "Fframes"
domain: "fframes.studio"
source_type: "community"
collector: "hackernews"
date: "2026-10-14T15:23:13Z"
published_date: "2026-10-14"
collected_at: "2026-10-15T12:06:50Z"
authors: ["neogoose"]
language: "en"
summary: "frames rendered in 94 seconds\nA 98-second film at 60 fps, rendered with fframes.\nOur first short film made with code and AI\nWhat’s worth building?\nwith fframes.\nThe entire film is a Rust program.\nfframes renders the 3D worlds, titles and sound.\n// Give the machines a reason.\nlet scene = Scene::new()\n    .environment(Environment::studio());\nlet camera = Camera::perspective(35.0);\n// And let there…"
tags: []
orgs: []
topics: []
content_source: "fulltext"
word_count: 119
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50089045"
score: 14
comments: 5
community: "Hacker News"
---

# Show HN: The first short movie built using code and AI

Fframes · neogoose · 2026-10-14

frames rendered in 94 seconds
A 98-second film at 60 fps, rendered with fframes.
Our first short film made with code and AI
What’s worth building?
with fframes.
The entire film is a Rust program.
fframes renders the 3D worlds, titles and sound.
// Give the machines a reason.
let scene = Scene::new()
    .environment(Environment::studio());
let camera = Camera::perspective(35.0);
// And let there be light.
let image = renderer.render(
    &scene, &camera
);
The billboards play Made of Motion, a fframes adaptation of Jordan Watkins’ original film.
Cold blue for the machines. Warm light for human intent.
Real roofs, walls and streets from NYC’s open city model.
Real motion-capture datasets record how people walk, kneel and shift their weight.
is yours.
