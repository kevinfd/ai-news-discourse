---
id: "22ba58ecade23d40"
title: "VectorDash update: now written in Rust, with full clipboard management, LOCAL reverse image search, web search, and AI chat (with computer and browser use), (mostly) powered by EmbeddingGemma 2!"
url: "https://reddit.com/r/LocalLLaMA/comments/1xb41jt/vectordash_update_now_written_in_rust_with_full"
link: "https://reddit.com/r/LocalLLaMA/comments/1xb41jt/vectordash_update_now_written_in_rust_with_full"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-20T21:00:09Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["andy2na"]
language: "en"
summary: "Thanks to everyone who tried VectorDash and shared feedback. A recurring request was to move from Python to Rust and build something that could replace more of what people use Everything and Windows search for. I wasn't going to post an update, but I think its even more relevant to LocalLlama more than ever with all the new, local-first features! VectorDash is now written in Rust , and it has…"
tags: ["r/LocalLLaMA"]
orgs: ["OpenAI"]
topics: ["search & media", "products & launches", "models & research", "agents & coding"]
content_source: "post"
word_count: 703
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1xb41jt/vectordash_update_now_written_in_rust_with_full/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# VectorDash update: now written in Rust, with full clipboard management, LOCAL reverse image search, web search, and AI chat (with computer and browser use), (mostly) powered by EmbeddingGemma 2!

Reddit · andy2na · 2026-10-20

Thanks to everyone who tried VectorDash and shared feedback. A recurring request was to move from Python to Rust and build something that could replace more of what people use Everything and Windows search for. I wasn't going to post an update, but I think its even more relevant to LocalLlama more than ever with all the new, local-first features! VectorDash is now written in Rust , and it has grown into a universal search tool for Windows: files, clipboard history, web search, and AI chat in one place. Feel like all of this is scope creep? All features (clipboard, web search, AI Chat) are optional , you can keep it just as a simple searcher or enable content search and the other tools you want. On my system, when VectorDash isnt indexing or models loaded, it uses less than 100mb of system memory. https://github.com/ampersandru/VectorDash What’s new since my original post : Smarter index updates: optional NTFS USN journaling tracks changes so VectorDash can update affected files and folders instead of repeatedly scanning entire drives. Recovery scans are still needed in some situations. Option to disable indexing (and unload all models) when full-screen or game is playing. A full, searchable clipboard manager: searchable text, links, and images; configurable retention and storage limits; permanently saved items; separate pinned items; tags, editing, and app exclusions. EmbeddingGemma 2 can find copied images by what they show, just like regular search. Search your clipboard history for specific images, text, or links Local Reverse image search: paste in an image into Search or Clipboard to find visually similar indexed images on your computer using EmbeddingGemma 2. EmbeddingGemma 2 will quickly index the pasted image before finding same or similar indexed images. Our savior, or our downfall? Quick Launch in any Folder: Double pressing Ctrl in any folder in explorer and open the quick search only that folder Web search: connect your own SearXNG or Degoog instance, or use a Brave Search API. AI chat: connect a local or remote OpenAI-compatible LLM, attach screenshots or pasted images, ask follow-up questions, and optionally let it search the web (if web search is configured). AI Local File Search: lets your chat model search VectorDash’s indexed file names and content snippets directly. Optional MCP server is also available to connect your other agents. Read-only access, for now... Computer and Browser Use ( in Beta release ): Option to have your LLM control a browser of your choice or control Windows ("turn on bluetooth for me", "use my browser to setup a hermes discord bot"). Highly YMMV and beta. Experience depends on how fast and capable your model is. Quick area screenshot to AI: similar to Android phones, you can set a shortcut to select an area of your screen and paste it into AI chat and quickly ask things like "what is this?" or "fact check this". enable web-search tool to allow your LLM to access updated information. Quickly fact check or ask about anything on your screen Voice input STT and playback TTS: local Parakeet or remote dictation, plus optional TTS with playback controls using your own TTS server. More customization: reorder search modes, assign shortcuts for individual tools, and adjust colors, transparency, gradients, and activity indicators. Interface localization in 13 languages: Beta. Windows 10 and camera RAW support: Beta - I only have access to Win11, need Win10 users to try it out. Quick vs. Full indexing still works the same way: Quick: file and folder names across entire drives. No embedding model needed. This is extremely fast. Full: supported document contents, photos, screenshots, audio, and video, searchable by exact words or meaning with EmbeddingGemma 2. This can be slow the first time you index the files. You can mix them: Quick-index your drives, then Full-index the document and media folders whose contents you want to search. Your index stays on your PC. Local processing is available; optional remote services receive the queries, images, or snippets needed for the features you enable. Yep, still vibed this. There’s now a larger automated test suite, but different hardware and real-world collections keep finding things I miss. I’d especially appreciate feedback on Windows 10, RAW files, translations, and the new image search. Thanks!
