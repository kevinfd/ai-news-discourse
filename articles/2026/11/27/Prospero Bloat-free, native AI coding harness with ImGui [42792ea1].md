---
id: "42792ea1ec910a69"
title: "Prospero: Bloat-free, native AI coding harness with ImGui"
url: "https://github.com/skeeto/prospero"
link: "https://github.com/skeeto/prospero"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-27T20:23:14Z"
published_date: "2026-11-27"
collected_at: "2026-11-28T13:03:39Z"
authors: ["ingve"]
language: "en"
summary: "Prospero is a native GUI application for Windows, macOS, and Linux that connects to an AI model provider, local or remote, allowing AI agents to drive your computer to develop software. It plows through intermittent errors and keeps at its task while unattended. It speaks the OpenAI Chat Completions API, used by llama.cpp, vLLM, LiteLLM, and providers with a compatible API. Also Anthropic's…"
tags: []
orgs: ["OpenAI", "Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 459
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50671275"
score: 81
comments: 34
community: "Hacker News"
---

# Prospero: Bloat-free, native AI coding harness with ImGui

GitHub · ingve · 2026-11-27

Prospero is a native GUI application for Windows, macOS, and Linux that connects to an AI model provider, local or remote, allowing AI agents to drive your computer to develop software. It plows through intermittent errors and keeps at its task while unattended. It speaks the OpenAI Chat Completions API, used by llama.cpp, vLLM, LiteLLM, and providers with a compatible API. Also Anthropic's Messages API, with extended thinking and prompt caching. No providers are configured out of the box.
The UI is highly flexible, and you can rearrange the panes as you please with dragging and docking. Save your layouts for later in View -> Layouts. Unlike conventional ImGui applications, rendering is passive and will not consume resources while idle.
It is a single executable, written in C++. In the typical case the engine runs in the same process as the window, and needs no daemon or server. The same executable can run headless, on another machine over ssh, or in the background after its window closes. The engine is lean and portable, and runs on computers and operating systems a quarter century old. Imagine a coding harness on Windows XP.
Once it's connected to a provider, you can ask Prospero for help with itself. It will read its own embedded documentation, self-configure, and navigate you to any place in its UI.
Prospero's desktop control features allow it to effectively develop, test, and debug native GUI applications. On Windows, it especially works well in w64devkit, making use of its shell and tools if available.
You can start new sessions from the command line, even if there's already an instance, by invoking Prospero with a path where the new session will be rooted. For example, to start a session here:
$ prospero .
After no arguments, this is the second most common way to run Prospero.
- Usage: running it, sessions, the GUI, attachments, modes and the command line
- Configuration: prospero.ini, endpoints,
models, roles, instructions, skills, MCP servers and web search
- Desktop control: letting the agent see and drive the screen
- Remote and background hosts: engines on other machines over ssh, and sessions that outlive the window
- Windows notes
- Building: building from source, and releases
- Development: tests, and evals for comparing models
Prospero also carries its own documentation, under Help, which an agent in it can read too.
Prospero is free and unencumbered software released into the public domain. See UNLICENSE.
Its programs include third-party code under its own licenses: Dear
ImGui (MIT), FreeType (FTL), md4c (MIT), SDL3 (zlib), cpp-httplib
(MIT), Mbed TLS (Apache-2.0), and Wuffs (Apache-2.0 or MIT, at your
option), which every program with the engine includes. The built-in
model's network, src/gemma.cpp, is derived from gemma4.c and stays
under its MIT license.
