---
id: "38d74fada3547575"
title: "PaperPilot – Zero-Cloud, Pure-Rust PDF Engine with WASM and MCP"
url: "https://github.com/KrushnaVardhanReddy/PaperPilot"
link: "https://github.com/KrushnaVardhanReddy/PaperPilot"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-26T03:29:05Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["vardhan1237"]
language: "en"
summary: "PDF tools for your AI agent — and for you. Pure Rust. Runs locally. Files never leave your machine.\nTry it in your browser → · Download · Contributing · Roadmap\nPaperPilot is a PDF and document toolkit written in Rust. The same engine runs as:\nNo Chromium, no C++ runtime, no cloud calls.\nOpen-WebUI integration (source builds): use the local gateway as a PDF-only Tika-compatible extraction…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "chips & infrastructure"]
content_source: "fulltext"
word_count: 531
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50238739"
score: 231
comments: 85
community: "Hacker News"
---

# PaperPilot – Zero-Cloud, Pure-Rust PDF Engine with WASM and MCP

GitHub · vardhan1237 · 2026-10-26

PDF tools for your AI agent — and for you. Pure Rust. Runs locally. Files never leave your machine.
Try it in your browser → · Download · Contributing · Roadmap
PaperPilot is a PDF and document toolkit written in Rust. The same engine runs as:
No Chromium, no C++ runtime, no cloud calls.
Open-WebUI integration (source builds): use the local gateway as a PDF-only Tika-compatible extraction server. See the Open-WebUI setup guide.
Codex, Claude Code, Kimi Code, and current Pi releases connect to the same local stdio server. See the coding agent setup guide for each client's configuration and verification steps. Builds from this source can also print ready-to-merge configuration:
paperpilot-mcp --client-config codex
# Also: claude-code, kimi-code, pi, claude-desktop, cursor
Download paperpilot-mcp from Releases, then add it to claude_desktop_config.json:
{
  "mcpServers": {
    "paperpilot": {
      "command": "/path/to/paperpilot-mcp"
    }
  }
}
Restart Claude and try: "Merge these two PDFs and compress the result."
# Merge
paperpilot merge --inputs doc1.pdf doc2.pdf --output merged.pdf
# Compress
paperpilot compress --input in.pdf --quality 75 --output compressed.pdf
# Rotate pages 1, 3–5 by 90°
paperpilot rotate --input in.pdf --pages 1,3-5 --angle 90 --output out.pdf
Go to usepaperpilot.com. Open your browser's Network tab while you work — you'll see no file uploads.
git clone https://github.com/KrushnaVardhanReddy/PaperPilot.git
cd PaperPilot
cargo build --release -p paperpilot-cli -p paperpilot-mcp -p paperpilot-gateway
Desktop app:
cd apps/desktop && pnpm install && pnpm tauri dev
Requires Rust 1.75+, Node.js, and pnpm.
- Organize & Layout: merge, split, rotate, delete pages, reorder pages, extract pages, booklet imposition, N-up grid, multi-sheet poster tile slicing (pdf_posterize)
- Optimize & Compress: lossy compression, stream deduplication, CMYK safety guards
- Extract & Ingest: structured text, detected Markdown tables, native Open-WebUI & Apache Tika ingestion adapter (/tika/text, /tika/json/md, /rmeta/text), pure-Rust OCR (PaddleOCR via rten)
- Security & Analysis: watermark, validate signatures, remove signatures, PII scan, deep sanitize, malformed fuzzing & panic-free error handling
- Office Data: Excel → JSON, Excel → CSV
- Private by default. Everything runs locally or in your browser tab.
- Agent-ready. MCP support is first-class, not an afterthought.
- One engine, many surfaces. CLI, MCP, REST, WASM, and desktop share the same Rust core, so behavior is consistent.
- Small and dependency-light. Pure Rust, built on lopdf, pdf_oxide, rten, and friends.
Run cargo bench --workspace to reproduce. Methodology and results: SYSTEM_BENCHMARK_REPORT.md.
Desktop (Tauri) · CLI · REST (Axum) · MCP (stdio) · WASM (browser / edge)
                              │
                       Rust core workspace
   paperpilot-core · paperpilot-pdf · paperpilot-nlp · paperpilot-gateway
   paperpilot-mcp · paperpilot-wasm · paperpilot-storage
<script src="https://cdn.usepaperpilot.com/embed.js" data-tools="merge,compress,ocr"></script>
<div id="paperpilot-widget"></div>paperpilot serve --port 7823
# Standard PDF Operations (JSON & multipart)
curl -X POST http://localhost:7823/api/v1/pdf/merge \
  -H "Content-Type: application/json" \
  -d '{"inputs": ["a.pdf", "b.pdf"], "output": "out.pdf"}'
# Open-WebUI & Tika In-Memory Ingestion (sub-5ms)
curl -X PUT http://localhost:7823/tika/text \
  -H "Content-Type: application/pdf" \
  --data-binary @sample.pdf
Interactive Swagger OpenAPI docs at http://localhost:7823/swagger-ui.
Issues and PRs are welcome. Good first contributions: bug reports with a sample PDF, new tool requests, and docs fixes.
Special thanks to all community members and contributors recognized in CONTRIBUTORS.md.
Community Edition (this repo): Apache 2.0. It includes the CLI, MCP server, REST gateway, WASM engine, and desktop app.
An Enterprise Edition (SSO, RBAC, audit logs, DLP) is developed separately.
