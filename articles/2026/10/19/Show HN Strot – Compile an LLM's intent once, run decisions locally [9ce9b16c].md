---
id: "9ce9b16cd98843e7"
title: "Show HN: Strot – Compile an LLM's intent once, run decisions locally"
url: "https://github.com/strot-ai/Project-STROT"
link: "https://github.com/strot-ai/Project-STROT"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-19T04:32:07Z"
published_date: "2026-10-19"
collected_at: "2026-10-19T12:07:39Z"
authors: ["solohunter001"]
language: "en"
summary: "Compile your intent once with an LLM. Then decide on every record forever — classification, scoring, routing — as type-safe JSON with probabilities and confidence, on your own hardware, at zero marginal cost.\nWebsite · Docs · Benchmarks · PyPI\nAgents at compile time.  Never at runtime.\npip install strot-aiimport strot\nresult = strot.run(\n    tickets,\n    query=\"Triage incoming support tickets…"
tags: []
orgs: []
topics: ["models & research", "agents & coding"]
content_source: "fulltext"
word_count: 519
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50148396"
score: 23
comments: 11
community: "Hacker News"
---

# Show HN: Strot – Compile an LLM's intent once, run decisions locally

GitHub · solohunter001 · 2026-10-19

Compile your intent once with an LLM. Then decide on every record forever — classification, scoring, routing — as type-safe JSON with probabilities and confidence, on your own hardware, at zero marginal cost.
Website · Docs · Benchmarks · PyPI
Agents at compile time.  Never at runtime.
pip install strot-aiimport strot
result = strot.run(
    tickets,
    query="Triage incoming support tickets into the correct workflow.",
    action_registry={
        "billing_dispute":  "Refunds, invoice corrections, double charges",
        "technical_defect": "Crashes, bugs, broken behavior",
    },
    llm="anthropic/claude-opus-4-8",   # used once, on first compile only
)
for o in result.outcomes:
    print(o["action"], round(o["confidence"], 2))
# billing_dispute 0.97
# technical_defect 0.94
The LLM runs once, at compile time. Production is a frozen, self-contained Python artifact: a small local decision model arbitrates every record, nothing is generated, every output is bounded, and low-confidence records abstain instead of guessing.
STROT = Agentic Schema Intent + Compiler & State + Code + Execution + NLU
                      ⟹  JSON Decisions
          (classification · scoring · routing · typed answers)
            COMPILE  (once per intent + schema)
  intent + sample ─▶ synthesize ─▶ golden gate ─▶ teacher labels ─▶ calibrate
                     (labels,      (your known      (annotate         (fit the
                      projection,   answers must     a sample,         confidence
                      handlers)     pass)            once)             threshold)
                                        │
                                        ▼
                             frozen artifact  (.py)
            RUNTIME  (every record, forever)
  record ─▶ projection ─▶ decision model ─▶ confidence gate ─▶ typed JSON
            (compiled)     (144M, CPU,        (decide or         decision
                            ~60 ms)            abstain)
run() — route each record to an action and execute the compiled handler.
decide() — answer typed questions (choice / score / boolean) per record:
result = strot.decide(records, questions={
    "is_bug_report":     {"type": "boolean", "instructions": "mentions crashes/errors?"},
    "customer_sentiment":{"type": "score", "min": 1, "max": 5, "instructions": "1 angry, 5 happy"},
    "routing_bucket":    {"type": "choice", "options": ["billing", "engineering", "spam"]},
})
# → {"booleans": {...}, "scores": {...}, "choices": {...}}  with probabilities + confidence
Real model (SupersonicLabs/Julia-1, 144M, CPU), real datasets, clean Docker containers:
Reproduce everything: benchmarks/ — with the losses published too.
- Compile once, decide forever — content-addressed artifact cache; schema drift triggers exactly one recompile.
- Golden-record promotion — artifacts must pass your known answers before they serve.
- Fitted guarantees — temperature scaling + split conformal prediction, baked in: dispatched decisions are wrong ≤ α of all records (marginal); the rest abstain.
- Measured, not guessed — the compiler scores labelings, and can train a distilled head, keeping only what beats the baseline on held-out data.
- 0% structural hallucination — output is selection + computation over your registry; nothing is generated at runtime.
- Model-independent — the decision model is a slot (nlu=): local Julia-1 by default, hosted APIs, or any drop-in specialist.
pip install strot-ai            # core: pure stdlib
pip install strot-ai[local]     # + the local decision model (torch/transformers)
pip install strot-ai[hosted]    # + openai, for a hosted decision runtime
pip install strot-ai[anthropic] # + anthropic, for the synthesizer
Bake the local model into your image for offline production:
RUN pip install strot-ai[local] \
 && python -c "import strot; strot.prefetch_nlu(local_dir='/opt/julia-1', install=True)"
ENV STROT_NLU_CHECKPOINT=/opt/julia-1
(Never pip install julia — unrelated package.)
DEVELOPERS.md — architecture, compile lifecycle, calibration semantics and caveats, deployment, model swapping, full API reference.
MIT. Default decision model: Apache-2.0 (SupersonicLabs/Julia-1). Implements ideas from STROT (arXiv:2505.01636).
