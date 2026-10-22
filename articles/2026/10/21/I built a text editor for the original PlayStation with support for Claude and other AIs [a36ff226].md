---
id: "a36ff226dfe518cd"
title: "I built a text editor for the original PlayStation with support for Claude and other AIs"
url: "https://reddit.com/r/ClaudeAI/comments/1xbxsjp/i_built_a_text_editor_for_the_original"
link: "https://reddit.com/r/ClaudeAI/comments/1xbxsjp/i_built_a_text_editor_for_the_original"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-21T20:02:39Z"
published_date: "2026-10-21"
collected_at: "2026-10-22T12:07:09Z"
authors: ["nukluer_karpuz"]
language: "en"
summary: "This is a text editor for the PS1, made for writing long documents, with an AI assistant built in. A Raspberry Pi Pico 2 plugged into controller port 2 talks to the console 60 times a second. It reads a USB keyboard and saves your documents to an SD card. On the PC side, a small Python script receives your document and question from the Pico over a serial port, sends them to Claude (or a local /…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research", "agents & coding"]
content_source: "post"
word_count: 218
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xbxsjp/i_built_a_text_editor_for_the_original/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a text editor for the original PlayStation with support for Claude and other AIs

Reddit · nukluer_karpuz · 2026-10-21

This is a text editor for the PS1, made for writing long documents, with an AI assistant built in. A Raspberry Pi Pico 2 plugged into controller port 2 talks to the console 60 times a second. It reads a USB keyboard and saves your documents to an SD card. On the PC side, a small Python script receives your document and question from the Pico over a serial port, sends them to Claude (or a local / OpenAI-compatible model) and streams the answer back to the PS1. You can edit the text yourself or let Claude write the whole thing: F4 inserts the answer at the cursor, and F5 replaces the whole document with it. I built the project with Claude. Since I don’t know much about PS1 development, Claude wrote the PS1 code, and it also wrote the Python script that runs on the PC. I wrote the Pico code myself and fixed the parts of Claude’s code that caused problems when testing on real hardware. Claude is also the default AI backend inside the editor, though you can switch to a local model or any OpenAI-compatible API with your own key. The GitHub repo has the code, build steps and a full technical reference: https://github.com/alp0809/PS1-Ai-Text-editor I also made a video that explains the details: https://youtu.be/5wookCM2O7A
