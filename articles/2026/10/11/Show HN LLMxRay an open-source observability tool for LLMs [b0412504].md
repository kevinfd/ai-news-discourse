---
id: "b04125043b387e8e"
title: "Show HN: LLMxRay an open-source observability tool for LLMs"
url: "https://github.com/LogneBudo/llmxray"
link: "https://github.com/LogneBudo/llmxray"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-11T21:17:45Z"
published_date: "2026-10-11"
collected_at: "2026-10-13T20:17:27Z"
authors: ["lognebudo"]
language: "en"
summary: "See what your AI is actually doing.\n  Real-time token streaming, quality analysis, performance profiling, and cost tracking\nfor local LLMs. No cloud. No API keys. No cost.\n🌐 English • Français • 中文 • العربية • Srpski\nQuick Start • Features • Screenshots • Who Is This For • Changelog\nChat Diagnostics — Watch tokens arrive one by one, coloured by speed. See where the model hesitates, and what it…"
tags: []
orgs: ["OpenAI", "Microsoft", "Anthropic", "DeepSeek", "Alibaba"]
topics: ["models & research", "chips & infrastructure", "agents & coding"]
content_source: "fulltext"
word_count: 1472
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50047905"
score: 11
comments: 0
community: "Hacker News"
---

# Show HN: LLMxRay an open-source observability tool for LLMs

GitHub · lognebudo · 2026-10-11

See what your AI is actually doing.
  Real-time token streaming, quality analysis, performance profiling, and cost tracking
for local LLMs. No cloud. No API keys. No cost.
🌐 English • Français • 中文 • العربية • Srpski
Quick Start • Features • Screenshots • Who Is This For • Changelog
Chat Diagnostics — Watch tokens arrive one by one, coloured by speed. See where the model hesitates, and what it was unsure about.
Live (new in 0.7.2) — Point VS Code Copilot, Open WebUI, Continue or your own scripts at LLMxRay instead of Ollama, and see every turn they send: prompt size, what the cache kept, where the prompt broke it, whether the model still fits on the GPU. One address to copy, nothing else to set up.
Cache Lab (new in 0.6.0) — Your system prompt is probably being recomputed from scratch every turn. Find out in 30 seconds, and measure the fix. (3.5x faster prefill in our test.)
Decision Lab — Ask a decision model (nimble, tev1, clef) typed questions about a ticket or a message, and see the probability behind every answer instead of a yes.
Compare — The same prompt against two models, or two temperatures, side by side. Stop guessing which setting was actually better.
Surgical Benchmark — Score models on real token logprobs, not on whether the answer happened to look right.
Protocol Observatory — See how the same local model replies through Ollama's native, OpenAI-compatible and Anthropic-compatible APIs, and exactly where they disagree.
Knowledge Base — Drop in PDFs and documents, chunk them, and see what RAG actually retrieves before the model ever sees it.
Plus embeddings, cost tracking, analytics, a tool builder, and a local history database. Full feature list below.
One command. 30 seconds.
npx llmxray
Or with Docker:
docker run -p 5174:5174 djovaneli/llmxray
Open http://localhost:5174 and start chatting. That's it.
Prerequisite: Ollama running locally with at least one model pulled (ollama pull llama3.2).
You run a local LLM. You chat with it. But what actually happened?
- How fast was each token? Which ones was the model confident about?
- Is the response quality degrading over long conversations?
- What would this have cost if you ran it in the cloud?
- Is the model repeating itself? Refusing? Generating gibberish?
- How does temperature 0.3 compare to 0.9 on the same prompt?
LLMxRay answers all of these, visually, in real time, for free.
Chat with any Ollama model and watch tokens arrive with confidence coloring — each token is tinted based on generation speed. Supports markdown, multi-turn conversations, file attachments, vision models, and slash commands. For reasoning models, set the thinking budget per conversation — off, model's choice, or an explicit low / medium / high / max effort.
Every response is automatically analyzed. Colored badges appear only when something is wrong:
- Repetition — excessive repeated phrases (4-gram analysis)
- Refusal — "as an AI language model" and 7 other patterns
- Gibberish — high non-ASCII ratio
- Empty — fewer than 10 words
- Truncation — hit the token limit without finishing
Up to 4 slots with independent model, temperature, and system prompt. Features include side-by-side streaming, word-level diff highlighting, metrics comparison, and one-click presets (Temperature Sweep, Deterministic Pair, Language Compare with Token Tax visualization).
- Latency percentiles (P50/P95/P99) for duration and TTFT
- Error intelligence — 7-category classifier with timeline
- Usage heatmap — 7x24 grid of your active hours
- Settings impact — temperature vs tokens/sec scatter plots
- Cold vs warm start tracking with model load history
Token usage per model/day with estimated cloud-equivalent pricing. See what you're saving by running locally.
Test model knowledge with multi-choice question suites. Uses real logprobs via OpenAI-compatible endpoint for accurate confidence measurement. Build custom suites visually or let AI generate them from a topic.
Embed text, visualize vectors, measure cosine similarity. Request a narrower output vector to see what Matryoshka truncation costs in similarity. Build a local knowledge base from PDFs, DOCX, and CSV — chunked, embedded, and searchable. All stored in IndexedDB. Zero cost.
Drag-and-drop node canvas for building tool definitions. Bidirectional code sync (edit nodes or TypeScript — both update). Probe APIs, auto-generate schemas, test with live execution.
Code completion for Qwen-Coder, CodeLlama, Codestral, DeepSeek-Coder, and StarCoder. Two textareas (prefix / suffix), the model fills the gap. Uses Ollama's suffix field on /api/generate. Stitched preview shows the result as it would appear in your editor.
LLMxRay opens a second port, 11435, that behaves exactly like Ollama and forwards everything to it. Point any other tool at http://localhost:11435 (the Ollama VS Code extension's ollama.endpoint for Copilot Chat, Open WebUI's connection URL, Continue's apiBase, n8n's Ollama credential, OLLAMA_HOST for scripts) and every turn it sends appears on the Live page: client, model, prompt tokens, how many came from the cache, prefill and generation speed, tool calls. Select a turn to see what the prompt is made of (system, tool schemas, history, your message) and the exact point where it stopped matching the previous turn, which is where the cache broke. Findings are plain sentences, each linked to the turn that proves it: a client re-reading most of its prompt every turn, a model running partly on CPU because its context no longer fits in VRAM, tool schemas that take 40% of every prompt. Only counts and timings are kept, in memory; prompt text is an opt-in that writes to a local file. Nothing leaves your machine.
Find out why your prompt misses the model’s KV cache, and measure what it costs every turn. A local model reuses its cache only while the prompt still matches from the very first token, so a single timestamp near the top forfeits everything below it. The lab finds the values that change between turns, shows the exact point where reuse dies, and then measures — sending each layout twice with a changed value, against your own daemon — what moving them to the end actually saves. Measured on a real 324-token prompt: 4 tokens reused and 64.6 ms of prefill with the timestamp at the front, 290 reused and 18.6 ms with it at the back. 3.5x faster, same words. Requires Ollama 0.33.3+.
Ollama 0.35.1 added decision models — nimble, tev1, clef, clef-flash — that answer on /v1/systemone with choices, probabilities and scores instead of text. Give the lab a state (a ticket, a message, a log line) and typed questions: a choice among named candidates, a yes/no probability, or a score on an ordered scale. Every answer comes back as the model's own probability distribution, drawn as bars with the chosen candidate highlighted. Decision models report decision as their only capability, so LLMxRay keeps them out of the chat selectors and lists them here.
Fire the same prompt through Ollama's three serving protocols — native /api/chat, OpenAI-compat /v1/chat/completions, and Anthropic-compat /v1/messages — in parallel against your local model. Side-by-side streaming, per-protocol metrics, and an envelope-diff tab that shows how each protocol frames finish reasons, token counts, and error envelopes. No cloud, no API keys — all three endpoints are local on localhost:11434.
Curate training data from your conversations. Tag, review, and export as JSONL for fine-tuning.
Every experiment (benchmarks, comparisons, chats, training pairs) is automatically archived in a queryable IndexedDB database with filters, trends, exports, and retention policies.
Full translations in English, French, Serbian (Latin + Cyrillic), Chinese, and Arabic. RTL layout support. Community scaffolds for Hebrew and Japanese.
Tested and verified against Ollama 0.40.x (verified on 0.40.3, October 2026). LLMxRay uses these Ollama endpoints:
Compatible with: Ollama 0.20 and newer (older versions work for chat/generate but lack think and JSON-schema format). Recommended: Ollama 0.33.3+ — prompt-cache reuse is reported (prompt_eval_cached_count, and usage.prompt_tokens_details.cached_tokens on the OpenAI-compatible endpoint), so prefill throughput is measured over the tokens actually evaluated. From 0.32: capabilities and context length arrive with the model listing, think accepts graded effort levels, and embeddings accept a dimensions width.
npx llmxray
npx llmxray --port 3000
npx llmxray --ollama-url http://192.168.1.50:11434docker run -p 5174:5174 djovaneli/llmxray
docker run -p 5174:5174 -e OLLAMA_URL=http://host.docker.internal:11434 djovaneli/llmxraygit clone https://github.com/LogneBudo/llmxray.git
cd llmxray
npm install
npm run dev     # http://localhost:5173
Streaming — Reads Ollama NDJSON via fetch() + ReadableStream. Tokens update the UI reactively through Pinia stores.
Token confidence — Approximated from inter-token latency (faster = more confident). Clearly labeled as approximation. Benchmarks use real logprobs via OpenAI-compatible endpoint.
Store-per-concern — Each domain has its own Pinia store: tokens, sessions, metrics, reasoning, comparison, embeddings, quality, cost, and more.
Hardware detection — Custom Vite plugin queries the OS directly (PowerShell/proc/sysctl) for accurate hardware specs.
Contributions welcome! See CONTRIBUTING.md for setup and guidelines.
Community translations especially welcome — scaffold files ready for Hebrew and Japanese.
LLMxRay is a trademark of Ivan Stankovic (LogneBudo). See TRADEMARK.md.
  If LLMxRay helps you understand your AI better, consider giving it a star.
It helps others discover the project.
