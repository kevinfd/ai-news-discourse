---
id: "ed5596a5e7c02ac9"
title: "Show HN: Linkit – AI bookmark manager, 100% free and open source"
url: "https://github.com/blue-idea/linkit"
link: "https://github.com/blue-idea/linkit"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-21T09:51:41Z"
published_date: "2026-10-21"
collected_at: "2026-10-21T12:06:46Z"
authors: ["manbudezhu"]
language: "en"
summary: "English | 简体中文\nLinkit is a desktop bookmark manager built for knowledge workers. AI summaries, semantic search, and a knowledge graph turn saved links into real assets. Collections let you group ideas across categories; link health checks and duplicate detection keep your library clean; one-click import from Chrome, Firefox, Raindrop and more gets you started in seconds. Twelve beautiful themes,…"
tags: []
orgs: ["OpenAI", "DeepSeek", "Apple"]
topics: ["models & research", "search & media", "products & launches", "chips & infrastructure"]
content_source: "fulltext"
word_count: 985
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50178218"
score: 10
comments: 4
community: "Hacker News"
---

# Show HN: Linkit – AI bookmark manager, 100% free and open source

GitHub · manbudezhu · 2026-10-21

English | 简体中文
Linkit is a desktop bookmark manager built for knowledge workers. AI summaries, semantic search, and a knowledge graph turn saved links into real assets. Collections let you group ideas across categories; link health checks and duplicate detection keep your library clean; one-click import from Chrome, Firefox, Raindrop and more gets you started in seconds. Twelve beautiful themes, dual-track local-first storage and cloud sync — completely free with no paywalls, your data is always yours. Connect any OpenAI-compatible API or a local model (Ollama, etc.) for full AI features. Available on macOS, Windows, and Linux.
brew install blue-idea/tap/linkitbrew update && brew upgrade linkit
Linkit is currently distributed without Apple notarization. The Cask automatically clears the Gatekeeper com.apple.quarantine attribute on install — no sudo required.
Windows, macOS (DMG), and Linux (AppImage / DEB) binaries are on the GitHub Releases page.
macOS DMG: If Gatekeeper blocks the app, drag Linkit.app to /Applications, then run Fix Gatekeeper.command inside the DMG to clear the quarantine flag automatically.
- Zero setup, no account required: All bookmarks are stored in a local SQLite database on your machine by default. Works seamlessly offline with lightning-fast sub-millisecond lookups.
- Uncapped library size: No limits on how many bookmarks, tags, or collections you can store. No hidden caps, trial periods, or functional paywalls.
- 100% data sovereignty: Your data stays on your machine. No telemetry, no ads, and zero third-party data sharing.
- Real-time multi-device sync: Sign in anytime to keep bookmarks, collections, categories, and tags synchronized across all your devices.
- Enterprise-grade Row-Level Security (RLS): Powered by Supabase (PostgreSQL), each record is cryptographically bound to your auth.uid(). Nobody else (not even the developers) can access your bookmarks.
- Conflict resolution & draft protection: Built-in revision tracking and automatic merging prevent multi-device race conditions; dirty draft caching ensures zero data loss during network disruptions.
- Completely free, forever: Unlike competing tools that gate cross-device sync, full-text search, or backups behind monthly subscriptions, Linkit's cloud sync is 100% free with zero paywalls.
Migrate your existing bookmarks in seconds:
- Browser HTML export — Chrome, Firefox, Safari, Edge
- Raindrop.io CSV/JSON export
- Clipboard URL — paste any link directly via Spotlight (Cmd/Ctrl + K)
Every bookmark is a rich knowledge card: custom tags, star ratings, pinning, personal notes, and reading status (unread → reading → read → archived). Stop losing links you meant to revisit.
Build a stable category tree with drag-and-drop. Then create Collections — cross-category themed spaces with custom emojis and colors — for projects, research, or inspiration boards. Organize items manually or let AI structure them around your curation goals.
Break free from rigid hierarchies. Provide a natural language prompt (e.g., "Collect modern frontend tooling and design resources"), and the built-in AI will match relevant bookmarks across your library, generate a collection title and description, and recommend contextual tags. Inside any collection, a dynamic recommendation banner continuously surfaces relevant bookmarks based on content and tag similarity for one-click addition. All suggestions remain editable previews until you explicitly confirm.
Note: Linkit does not provide built-in LLM services or API keys by default; users need to configure their own model.
Connect any OpenAI / DeepSeek-compatible API or a local LLM (Ollama, etc.) and unlock:
- Auto page fetch, summarization, and key takeaways
- Smart tag and category recommendations
- AI-curated collections from natural language prompts
- Semantic search across your entire library
- Duplicate detection and merge suggestions
Instant full-text and semantic vector search across titles, notes, tags, and AI-generated content. Also doubles as a quick-capture bar — paste a URL and save it without leaving your current tab.
Linkit periodically generates an Insights Report summarizing your curation habits: most-used tags, reading progress, content patterns, and AI-surfaced highlights from your unread pile. Turn your bookmark graveyard into an active knowledge base.
Automatically surface exact-URL duplicates and AI-detected near-duplicates (same content, different URLs). Review and merge with one click to keep your library clean.
Background scans detect broken links (404) and silently changed pages. Filter, review, and clean up stale bookmarks before they pile up.
Visualize your entire library as an interactive network. Nodes connect via shared tags, collections, and AI semantic similarity. Click any node to jump directly to that bookmark.
Three-column layout with collapsible sidebars, six view modes (grid, list, waterfall, timeline, tag-cluster, collections), and a rich detail panel.
Instant multi-attribute and semantic search, or paste a URL to capture and analyze it on the spot.
One-click page analysis: core takeaways, auto-tags, and a concise summary — all generated locally or via your chosen API.
Generate curated collections from natural language goals, with real-time similarity-based bookmark suggestions inside each collection view.
Drag-and-drop or clipboard detection. AI fetches metadata and suggests tags in real time.
Seamlessly choose between an account-free, offline local-first mode or a free cloud account with multi-device synchronization.
Note: Linkit does not provide built-in LLM services or API keys by default; users need to configure their own model.
Connect any OpenAI / DeepSeek-compatible cloud API or local LLM (such as Ollama, LocalAI, vLLM). API keys are encrypted in your local OS keychain (macOS Keychain / Windows Credential Manager) and never uploaded.
Scan for broken or changed links and filter results by status.
Twelve elegant themes (Midnight, Ocean, Graphite, Sunset, Obsidian, Aurora, Daylight, Paper, Cupertino, Cappuccino, Provence, Monet) and full English / 简体中文 localization.
- Desktop Framework: Wails (Go)
- Frontend: React + Vite + TypeScript
- UI: Tailwind CSS + Glassmorphism design system
- Local DB: SQLite (via GORM)
- Cloud Sync: Supabase (PostgreSQL + RLS)
- AI: OpenAI / DeepSeek-compatible APIs or local LLMs (Ollama)
- Local by default: No account, no telemetry, no cloud dependency to get started.
- RLS-enforced sync: Cloud data is row-level secured — only you can access your records.
- Keychain-stored credentials: AI API keys are stored in your OS keystore (go-keyring → macOS Keychain / Windows Credential Manager). Never hardcoded, never uploaded.
