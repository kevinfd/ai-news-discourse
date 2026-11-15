---
id: "fa6f9a523c4f0651"
title: "Show HN: Turbo-Browser-MCP – Batch forms, DOM deltas and submit guards for MCP"
url: "https://github.com/Tthanh2k6/turbo-browser-mcp"
link: "https://github.com/Tthanh2k6/turbo-browser-mcp"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-15T04:09:11Z"
published_date: "2026-11-15"
collected_at: "2026-11-15T13:03:31Z"
authors: ["tthanh2k6"]
language: "en"
summary: "turbo-browser-mcp is a Playwright-based Model Context Protocol (MCP) server built to cut LLM token waste and multi-turn latency in browser automation. It consolidates 25-33 fine-grained browser primitives into 10 batched tools featuring delta DOM snapshots, single-turn React/Shadow DOM/iframe form prefill, direct disk file uploads (no Base64 in context), parallel tab sessions, network blocking…"
tags: []
orgs: ["OpenAI", "Google", "Meta", "Microsoft"]
topics: ["agents & coding", "models & research", "products & launches", "search & media"]
content_source: "fulltext"
word_count: 1491
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50503930"
score: 39
comments: 8
community: "Hacker News"
---

# Show HN: Turbo-Browser-MCP – Batch forms, DOM deltas and submit guards for MCP

GitHub · tthanh2k6 · 2026-11-15

turbo-browser-mcp is a Playwright-based Model Context Protocol (MCP) server built to cut LLM token waste and multi-turn latency in browser automation. It consolidates 25-33 fine-grained browser primitives into 10 batched tools featuring delta DOM snapshots, single-turn React/Shadow DOM/iframe form prefill, direct disk file uploads (no Base64 in context), parallel tab sessions, network blocking presets, and a default human-in-the-loop Submit guard.
All figures below come from benchmarks/benchmark.mjs (npm run benchmark) running headless Chromium locally with exact OpenAI o200k_base tokenization (tiktoken 0.14.0):
Note on latency vs LLM inference turns: Eliminating 10 round-trips on a 10-field form saves both 7x in browser execution (574 ms -> 82 ms) and 10 separate LLM inference round-trips (2-5s per turn in agent loops) plus ~71,800 replayed history tokens.
Standard MCP servers charge an LLM round-trip for every snapshot, field fill, <select> choice, upload, and verification check. Each turn re-sends the growing conversation history back into the model.
sequenceDiagram
    autonumber
    participant Agent as LLM Agent
    participant Std as Standard MCP (Playwright / DevTools)
    participant Turbo as turbo-browser-mcp
    Note over Agent,Std: Standard MCP (12+ LLM turns, full ARIA tree + history replay each step)
    Agent->>Std: 1. snapshot() -> full ARIA (~3,568 tok)
    loop Repeats 10+ times across fields, selects, checkboxes, upload
        Agent->>Std: fill / select_option / click
        Std-->>Agent: full ARIA or confirmation re-added to history
    end
    Agent->>Std: 12. upload inline or click chooser
    Note over Agent,Turbo: turbo-browser-mcp (2 LLM turns total, delta & inline snapshot)
    Agent->>Turbo: 1. inspect_compact(mode: "forms") -> compact refs (1,135 tok)
    Agent->>Turbo: 2. smart_fill_form(fields: [...10 fields + disk PDF...], returnSnapshot: true)
    Turbo-->>Agent: Filled 10 fields + guarded before Submit + inline snapshot (811 tok)
    - 4 connection modes (--mode auto|cdp|persistent|launch):
  - auto (default): probes --cdp http://127.0.0.1:9222 first so agents can reuse an existing signed-in browser session, then falls back to launching Chromium.
  - cdp: attach directly to a running Chromium/Chrome/Edge remote debugging port.
  - persistent: launch with a reusable --user-data-dir profile across runs.
  - launch: start a clean browser session (--headless by default, or --headed).
- Auto binary discovery (src/playwright-loader.mjs): checks playwright-core cache revisions across Windows, macOS, and Linux, system installs of Google Chrome, Microsoft Edge, Brave, and Chromium, or an explicit --executable <path>.
- Per-tab isolation (tabs_batch): open tabs inside named isolatedContext sandboxes with separate cookies and storage, batch-open up to 10 concurrent URLs (open_many), activate, reload, go back/forward, resize viewport, and emulate colorScheme, media, reducedMotion, contrast, forcedColors, or custom userAgent.
- Snapshot modes: interactive, forms, article, and all.
- Cross-boundary traversal: flattens main frame DOM, child iframes (includeFrames, frameIdx), and open Shadow DOM. Injects an init script hooking Element.prototype.attachShadow (WeakMap + WeakRef/FinalizationRegistry + window.__tbmGetShadowRoot) to keep post-init closed Shadow roots inspectable and guarded, traverses <slot> assignedNodes({ flatten: true }), and supports Form-Associated Custom Elements.
- Token controls: onlyChanged: true emits only elements added or changed since the prior snapshot; query filters by regex or substring; boxes: true adds [box=x,y,w,h] only when needed; maxChars caps payload size; savePath writes full output to disk.
Prefills an entire form in one MCP call while flushing microtasks and macrotasks between controlled inputs:
- Standard & framework inputs: text, email, password, number, date, textarea, <input type="range">, checkboxes, radio groups (check, not, overwrite). Triggers React-controlled state updates via native property setters and synthetic events.
- Selects & custom widgets: <select> and <select multiple> (option / values), ARIA comboboxes, ARIA switches, contenteditable rich editors, and Gmail compose dialogs (gmail: { to, subject, body }).
- Frame & wildcard targeting: target specific iframes via frameIdx, or set all: true to populate matching controls across frames.
- Direct disk uploads: pass file or files paths directly to Playwright setInputFiles without loading binary files or Base64 strings into LLM context.
- Atomic verification: pass returnSnapshot: true to inspect the updated form state in the same tool response.
- act_fast actions: click, dblclick, hover, focus, clear, fill, type (slowly, delayMs, submit), select, check, uncheck, drag, drop (file, files, or custom MIME dropData), press (key + modifiers: Alt, Control, ControlOrMeta, Meta, Shift), scroll (dx, dy), wait (ms, state, loadState, text, textGone, url), and upload.
- Targeting options: compact [eN] ref, CSS selector, visible text, label, or viewport (x, y) coordinates, with button (left, right, middle) and frameIdx.
- batch_actions: runs an ordered list of DOM actions and nested smart_fill_form steps in one MCP call, stopping safely if blocked by the Submit guard or optionally continuing on step errors (continueOnError).
- extract_clean_text: extracts readable plain text or compact Markdown (format: "text" | "markdown") from main/article containers and iframes, stripped of script and style noise.
- evaluate_js: runs JS expressions or (el, arg) element functions in any frame (frameIdx) with JSON-serialized results and optional savePath export.
- capture_page: full-page or element-scoped screenshots (png or jpeg with quality, css or device scale, optional returnImage) and PDF generation saved to a confined savePath.
- network_session presets: turbo, no-images, no-media, and clean (unblock all), alongside custom blockResources and blockUrls patterns.
- Session & storage management: read/write/clear browser cookies, localStorage/sessionStorage, and export or reload full Playwright storageState JSON files (saveStorageStatePath, loadStorageStatePath).
- page_diagnostics: defaults to errors-only (level: "errors", statusFilter: "errors") to surface failures cleanly without flooding context, while supporting all, includeStatic, urlFilter, deep request/response inspection (reqId + part), completed downloads, and dialog auto-handling (dialogPolicy: accept/dismiss).
Run the benchmark suite yourself with Chromium and Playwright installed:
npm run benchmark
Environment & methodology: Headless Chromium via playwright-core, counting exact OpenAI o200k_base tokens via Python tiktoken (approx-bpe fallback if tiktoken is unavailable). Cumulative workflow tokens model standard chat-history replay across $N$ sequential turns: $\sum_{i=1}^{N} (N - i + 1) \cdot T_i$, plus a one-shot baseline where the first turn captures context before acting.
Measured against installed MCP JSON schemas on disk (compact parameter schemas without annotations):
When to keep Chrome DevTools MCP alongside turbo-browser-mcp: chrome-devtools-mcp provides Lighthouse audits, performance trace analysis, CSS computed style panels, and V8 heap snapshots. turbo-browser-mcp focuses on fast multi-step UI automation, forms, and scraping with minimal token overhead.
- Human-in-the-loop Submit Guard (allowSubmit=false by default):
  - smart_fill_form (stopBeforeSubmit: true), act_fast, and batch_actions inspect matching elements, W3C AccName labels (isSafeSubmitter), implicit HTML form Enter submissions, key chords (Shift+Enter, Enter+Shift), HTMLFormElement.prototype.submit/requestSubmit, and same-origin iframe contentWindow/contentDocument proxies.
  - Final actions resembling Submit, Publish, Send, Post, Apply, Confirm, or payment triggers are blocked unless allowSubmit: true is explicitly passed or --allow-submit is enabled at startup.
  - Trade-off: pre-existing closed Shadow roots on already-open CDP tabs (attached before the init script ran) or strict cross-origin sandboxed frames fall back to Playwright frame handles, coordinate actions, and keyboard input.
- Workspace Path Confinement (TURBO_BROWSER_SAVE_ROOT):
  - File outputs (savePath, saveStorageStatePath) and state inputs (loadStorageStatePath) are strictly confined to the current working directory or TURBO_BROWSER_SAVE_ROOT.
  - Lexical checks, lstatSync/readlinkSync symlink verification, and realpathSync validation block .. traversal, UNC network paths, dangling symlinks, cyclic symlinks, and Windows junctions before reading or writing.
{
  "name": "smart_fill_form",
  "arguments": {
    "fields": [
      { "selector": "#full_name", "value": "Alex Nguyen" },
      { "selector": "#email", "value": "alex@example.com" },
      { "selector": "#country", "option": "United States" },
      { "selector": "#skills", "values": ["TypeScript", "Playwright"] },
      { "selector": "#agree_terms", "check": true },
      { "selector": "#resume_pdf", "file": "./assets/resume.pdf" }
    ],
    "stopBeforeSubmit": true,
    "returnSnapshot": true
  }
}{
  "name": "inspect_compact",
  "arguments": {
    "mode": "interactive",
    "onlyChanged": true,
    "maxChars": 3000
  }
}{
  "name": "tabs_batch",
  "arguments": {
    "operations": [
      { "action": "open", "url": "https://example.com/app", "isolatedContext": "acct-a" },
      { "action": "open_many", "urls": ["https://example.com/docs", "https://example.com/pricing"], "concurrency": 4 }
    ]
  }
}git clone https://github.com/Tthanh2k6/turbo-browser-mcp.git
cd turbo-browser-mcp
npm install
npm run doctor
If you need Playwright's bundled Chromium (or have no system Chrome/Edge/Brave installed):
npx playwright-core install chromium
Using local clone:
{
  "mcpServers": {
    "turbo-browser": {
      "command": "node",
      "args": ["/absolute/path/to/turbo-browser-mcp/src/index.mjs"],
      "env": {
        "TURBO_BROWSER_SAVE_ROOT": "/absolute/path/to/allowed/workspace"
      }
    }
  }
}
Using npx / binary entrypoint:
{
  "mcpServers": {
    "turbo-browser": {
      "command": "npx",
      "args": ["-y", "turbo-browser-mcp"]
    }
  }
}
In Chrome 136+/144+, enabling chrome://inspect/#remote-debugging on the default User Data directory exposes a WebSocket in DevToolsActivePort that displays an "Allow remote debugging?" prompt whenever a new WebSocket client connects. turbo-browser-mcp provides two built-in solutions so overnight AFK multi-agent runs never hang on a prompt:
- Automatic CDP Keep-Alive Bridge Daemon (npm run bridge / --bridge, enabled automatically on DevToolsActivePort):
  - Spawns a detached background multiplexer (src/cdp-bridge.mjs on http://127.0.0.1:9224) that holds one persistent upstream WebSocket to Chrome open indefinitely and intercepts Browser.close so downstream scripts never terminate your browser.
  - You click Allow once when starting your session; afterwards, any number of MCP servers, CLI scripts, or subagents can connect and disconnect all night with 0 additional prompts.
- Zero-Prompt Dedicated Profile Launcher (npm run launch-chrome / --launch-chrome):
  - Launches Chrome with --remote-debugging-port=9222 and a dedicated --user-data-dir (~/.turbo-browser-mcp/chrome-profile), where Chrome exposes standard HTTP/WS CDP with 0 confirmation dialogs even on the very first connection.
npm test            # 407 passing tests across 86 suites (26 test files under test/*.test.mjs)
npm run doctor      # Environment check for Node, Playwright, Chromium, and CDP
npm run bridge      # Start/verify persistent CDP Keep-Alive Bridge daemon
npm run benchmark   # Local Chromium speed & exact o200k_base token benchmark
Tested automatically on GitHub Actions (ubuntu-latest) across Node 20 and Node 22.
