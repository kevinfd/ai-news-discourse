---
id: "3912bd240c38b37d"
title: "Show HN: Airgap-check – find what your AI app silently downloads offline"
url: "https://github.com/humanethq/airgap-check"
link: "https://github.com/humanethq/airgap-check"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T20:37:28Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["humanethq"]
language: "en"
summary: "Find out what your AI app downloads, or tries to reach, when the network goes away.\nA common assumption: point the LLM base URL at a local vLLM or Ollama instance and the app is ready for an offline network (an air-gapped VPC, a hospital or defense network, a container with no internet). In practice, many libraries fetch something on first use: tokenizer ranks, ONNX embedding weights, corpora,…"
tags: []
orgs: ["Hugging Face"]
topics: ["products & launches", "models & research"]
content_source: "fulltext"
word_count: 1743
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50431705"
score: 11
comments: 0
community: "Hacker News"
---

# Show HN: Airgap-check – find what your AI app silently downloads offline

GitHub · humanethq · 2026-11-09

Find out what your AI app downloads, or tries to reach, when the network goes away.
A common assumption: point the LLM base URL at a local vLLM or Ollama instance and the app is ready for an offline network (an air-gapped VPC, a hospital or defense network, a container with no internet). In practice, many libraries fetch something on first use: tokenizer ranks, ONNX embedding weights, corpora, price maps, or telemetry. Offline, these calls either fail at first use or hang for tens of seconds on retry backoff.
None of this is a bug in those libraries. They download once and cache. It only becomes visible when the network is gone. airgap-check tries to surface it before you deploy.
- Manifest & lockfile scan. Inspects requirements*.txt, pyproject.toml, Pipfile, package.json, Cargo.toml, go.mod, and Gemfile (skipping devDependencies, [dependency-groups], and dev/test/lint/docs groups), and follows lockfiles (uv.lock, poetry.lock, package-lock.json, pnpm-lock.yaml, yarn.lock, Cargo.lock) from production roots with explicit scope tags (prod, transitive_lockfile, optional_extra). Reads these files with a built-in minimal TOML/YAML reader (no external parser), so unusual formatting may be missed.
- Source patterns & heuristics. Flags known runtime fetch calls (nltk.download(), from_pretrained(), tiktoken.get_encoding(), whisper.load_model(), easyocr.Reader(), RapidOCR(), PaddleOCR(), FlagModel/FlagReranker, TextEmbedding(), next/font/google) while ignoring comments and local_files_only=True, plus generic asset URLs (.onnx, .safetensors, .gguf, model_prices_and_context_window.json), urlretrieve(), runtime pip install/ollama pull, and ~/.cache writes. Missing HTTP timeout= calls are reported separately as advisory robustness_hints.
- Python and Node --run. Runs your app or probe inside docker run --rm --network none with a loopback sinkhole (UDP:53 DNS, TCP:443 TLS SNI, TCP:80 HTTP Host/Path with query strings stripped, HTTP_PROXY fallback) and Python/Node socket hooks.
- --fix & custom rules. Prints Dockerfile ENV flags and pre-warming commands, and supports repo overrides via .airgap-check.json or --rules.
- .env keys. Classifies .env* key names and git ls-files status only; secret values are never read or logged.
Go standard library only. --run requires Docker.
# macOS and Linux
curl -fsSL https://raw.githubusercontent.com/humanethq/airgap-check/main/install.sh | sh
# With Go 1.22+ (also works on Windows)
go install github.com/humanethq/airgap-check/cmd/airgap-check@latest
# From source
git clone https://github.com/humanethq/airgap-check.git
cd airgap-check && make build && ./bin/airgap-check --help# static scan
airgap-check /path/to/repo
# static scan plus a Dockerfile snippet
airgap-check --fix /path/to/repo
# run in a container with no network
airgap-check --run /path/to/repo
# auto-build the repo's Dockerfile first, then run inside --network none
airgap-check --run --build --run-cmd "python3 -m pytest tests/smoke_test.py" /path/to/repo
# use your own image, NXDOMAIN DNS mode, or a custom rules file
airgap-check --run --dns-action nxdomain --image my-app:latest --run-cmd "node server.js" /path/to/repo
airgap-check --rules ./airgap.custom.json /path/to/repo
# machine-readable output (flags may appear before or after the path)
airgap-check /path/to/repo --json
Read this before applying it: if your app loads Hugging Face models, pre-warm them at build time before setting HF_HUB_OFFLINE=1 and TRANSFORMERS_OFFLINE=1. Without a warm cache the app fails at startup instead of hanging.
# --- BEGIN AIR-GAP & TELEMETRY REMEDIATION ---
ENV DO_NOT_TRACK=1 \
    NEXT_TELEMETRY_DISABLED=1 \
    ANONYMIZED_TELEMETRY=False \
    CHROMA_TELEMETRY_IMPL=none \
    SCARF_NO_ANALYTICS=true \
    HF_HUB_DISABLE_TELEMETRY=1 \
    HF_HUB_OFFLINE=1 \
    TRANSFORMERS_OFFLINE=1 \
    LANGCHAIN_TRACING_V2=false \
    LANGFUSE_ENABLED=false \
    CREWAI_DISABLE_TELEMETRY=true \
    OTEL_SDK_DISABLED=true \
    DD_TRACE_ENABLED=false \
    WANDB_MODE=offline \
    WANDB_DISABLED=true \
    GRADIO_ANALYTICS_ENABLED=False \
    LITELLM_LOCAL_MODEL_COST_MAP=True \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
    XDG_CACHE_HOME=/app/.cache \
    TIKTOKEN_CACHE_DIR=/app/.cache/tiktoken \
    HF_HOME=/app/.cache/huggingface \
    NLTK_DATA=/app/.cache/nltk_data \
    EASYOCR_MODULE_PATH=/app/.cache/easyocr \
    TORCH_HOME=/app/.cache/torch \
    PLAYWRIGHT_BROWSERS_PATH=/app/.cache/ms-playwright \
    PUPPETEER_CACHE_DIR=/app/.cache/puppeteer
RUN mkdir -p /app/.cache/tiktoken /app/.cache/huggingface /app/.cache/nltk_data /app/.cache/easyocr /app/.cache/torch /app/.cache/ms-playwright /app/.cache/puppeteer
# Pre-warm Python tiktoken encodings at build time
RUN TIKTOKEN_CACHE_DIR=/app/.cache/tiktoken python3 -c "import tiktoken; [tiktoken.get_encoding(e) for e in ('cl100k_base', 'o200k_base')]"
# Pre-warm ChromaDB's default ONNX embedding model at build time
RUN HOME=/app XDG_CACHE_HOME=/app/.cache python3 -c "from chromadb.utils.embedding_functions import ONNXMiniLM_L6_V2; ef = ONNXMiniLM_L6_V2(); ef(['airgap-warmup'])"
# --- END AIR-GAP & TELEMETRY REMEDIATION ---
--run starts a container with --network none, mounts your repository read-only, and injects an isolated loopback observer (runner.py in Python containers, or runner.js in Node-only containers; pass --build to build the repo's Dockerfile first):
- Loopback DNS sinkhole (127.0.0.1:53/udp) with /etc/resolv.conf updated inside the ephemeral container. In the default sinkhole mode (--dns-action sinkhole), A queries resolve to 127.0.0.1 so outbound connections continue to our loopback TLS/HTTP listeners rather than dying at DNS before showing their HTTP path or SNI hostname. Pass --dns-action nxdomain to fail immediately at DNS resolution.
- TLS ClientHello SNI (127.0.0.1:443) & HTTP (127.0.0.1:80) sinkholes, plus an HTTP_PROXY/HTTPS_PROXY loopback CONNECT fallback when running as a non-root container user without bind privileges on ports < 1024. Query strings are stripped from captured URLs.
- Python (sitecustomize.py) & Node (node_preload.js) socket hooks recording socket.getaddrinfo, socket.connect, dns.lookup, and net.Socket.connect.
Limits:
- Loopback sinkholes (runner.py and runner.js) were validated in real docker run --network none containers for both Python (python:3.12-slim-bookworm) and pure Node.js (node:20-bookworm-slim). Other runtimes without Python or Node fall back to shell_only error URL extraction and are not separately validated.
- Traffic to hardcoded external IP addresses (not hostnames) fails with ENETUNREACH in the kernel without hitting loopback SNI/HTTP listeners, though sitecustomize.py/node_preload.js capture literal connect targets in Python/Node. DNS-over-HTTPS traffic skips the system resolver unless SNI reveals the DoH provider.
- Non-root containers running compiled Go/Rust binaries that ignore HTTP_PROXY and cannot bind ports 53/80/443 inside the unprivileged user namespace will log ENETUNREACH rather than SNI unless run as root inside the throwaway test container.
- Only the code paths you exercise are tested. Use --run-cmd to run a smoke test that covers the paths you care about.
- The sinkhole answers immediately. In a real enclave, packets may be dropped instead, so hangs can be longer than the times below.
We evaluated airgap-check on 30 open-source Python and TypeScript AI repositories across three phases: Phase 1 (10 calibration repos), Phase 2 (10 held-out repos scored with v0.1.0 rules frozen at 8ce2f11, then re-used to design v0.2.0), and Phase 3 (10 fresh held-out repos scored strictly out-of-sample with v0.2.1 rules frozen at 47b2ddc).
These are probe-based tests: we did not start the applications themselves. A “true positive” means the flagged library fetches something when its call runs offline (or executes a runtime installer/download); it does not prove the repository reaches that call in normal operation. Telemetry findings (for example langsmith, posthog or sentry) and advisory robustness_hints (timeout= omissions) are not scored in precision/recall. Exact probe commands, upstream URLs, and commit SHAs are documented in benchmark/REPOS.md.
Timings in the table above were measured with v0.1.0 (immediate NXDOMAIN); v0.2.0+ defaults to sinkhole mode (127.0.0.1), where connections reach a local loopback TLS/HTTP listener first and hit handshake/socket errors instead of immediate DNS errors, which changes retry behaviour across HTTP clients (for example, huggingface_hub on smolagents exited in 293 ms under sinkhole vs 477 ms under --dns-action nxdomain). Browser-side telemetry, such as posthog-js in a frontend bundle, is a separate case: server environment variables do not silence it, because the requests leave from the user's browser.
At component level (v0.1.0): 35 true positives, 4 false positives, 5 false negatives. That is 89.7% precision and 87.5% recall. This is a small sample, so treat the numbers as rough. At repository level, all 9 repositories with first-use downloads were flagged, and chat-langchain was correctly flagged as clean.
False positives (all 4 in v0.1.0): pyproject.toml was scanned as plain text, so dev and test dependency groups (playwright in docling, litellm, pydantic-ai) and an optional extra named posthog triggered warnings.
False negatives (all 5 in v0.1.0): OCR weight downloaders (easyocr, rapidocr, paddleocr), FlagEmbedding, and LiteLLM's startup fetch of model_prices_and_context_window.json were not in the frozen v0.1.0 rule table.
These 10 Phase 2 repositories were used to design the v0.2.0 fixes, so re-run numbers on them are no longer out-of-sample. See the fresh Phase 3 held-out set below for out-of-sample v0.2.1 validation.
- Addresses all 4 v0.1.0 dev-group / key-name false positives (0 dev/lint/key-name false positives; optional extras such as format-html-render in docling or [extra: playwright] in pydantic_ai_harness are tagged explicitly as optional_extra rather than prod).
- Addresses the 5 v0.1.0 false negatives (FlagEmbedding, paddleocr, easyocr, rapidocr, and litellm's startup model_prices_and_context_window.json fetch — the latter caught generically by the behavioral URL scanner without requiring a package rule).
- Surfaces transitive air-gap dependencies via lockfile traversal (huggingface-hub via datasets in gpt-engineer's poetry.lock, spacy and rapidocr via uv.lock in llama_index, @huggingface/transformers via pnpm-lock.yaml in mem0, tiktoken via uv.lock in pydantic-ai).
To measure v0.2.1 strictly out-of-sample, we froze all detection rules at commit 47b2ddc before cloning 10 previously unseen AI repositories (0.02 s – 0.59 s per scan):
At finding level (v0.2.1, out-of-sample): 53 true positives, 4 false positives, 7 false negatives (93.0% precision, 88.3% recall). All 8 repositories containing runtime downloaders or optional-extra downloads were flagged (while dev-only playwright==1.63.0 inside openai-agents-python's [dependency-groups] dev produced 0 false positives), and both clean repositories (markitdown, servers) were flagged clean. Separating missing timeout= calls out of behavioral_findings into advisory robustness_hints prevented 37 HTTP-timeout hints (26 in open-webui alone) from dropping out-of-sample precision from 93.0% to 56.4%.
- False positives (4): smolagents matched a docstring example (>>> tokenizer = AutoTokenizer.from_pretrained(...) in _function_type_hints_utils.py); crewAI matched Vertex AI SDK's TextEmbeddingModel.from_pretrained(...) (genai_vertex_embedding.py), a private maintenance script (lib/devtools/src/crewai_devtools/litellm_catalog_update.py), and arxiv_paper_tool.py's user-triggered urlretrieve(pdf_url).
- False negatives (7): crawl4ai/model_loader.py has a multi-line subprocess.run(["git", "clone", ...]) call (line-by-line regex missed it) and spacy.load(); aider/models.py splits model_prices_and_context_window.json across two adjacent string literals (though litellm in requirements.txt surfaced the host); open-webui missed spacy transitively under unstructured in uv.lock and kokoro-js in package.json (kokoro.worker.ts from_pretrained() was caught); crewAI missed docling ([extra: docling] + DocumentConverter()) and spacy under optional extras. Also note: aider maps requirements-help.txt and requirements-playwright.txt via [tool.setuptools.dynamic.optional-dependencies], so the minimal TOML reader tagged those 4 extras as prod rather than optional_extra, and browser-use implements PostHog telemetry via raw stdlib urllib rather than the posthog PyPI package (unscored).
Per-repository SHAs, manifests, lockfiles, scan durations, and probe transcripts are recorded in benchmark/REPOS.md.
Drop .airgap-check.json in your repository root (or pass --rules path/to/rules.json) to add internal packages or suppress known-good components/hosts:
{
  "rules": [
    {
      "package_or_pattern": "internal-embedder",
      "component": "internal-embedder-sdk",
      "category": "runtime_model_asset",
      "severity": "CRITICAL",
      "hosts": ["models.internal.corp"],
      "impact": "Fetches internal weights at boot.",
      "mitigation": "Bake weights into /app/models during build.",
      "python_only": true
    }
  ],
  "ignore_components": ["gradio"],
  "ignore_hosts": ["api.gradio.app"]
}
- Secret values are never read, stored or logged. .env files are inspected for key names, non-empty presence, and git ls-files status.
- --run mounts your repository read-only.
airgap-check is not a security certification. It reports what it observed; a clean result does not prove that your application is safe to run in an isolated network.
Found a library that quietly phones home, or a false positive on your repo? Open an issue with the package name, the call, and the host it tries to reach, and we will add or fix the rule.
Open-sourced by Humanet, which is also building Frame, an early-stage hosting platform.
MIT
