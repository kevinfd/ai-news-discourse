---
id: "285f83056600dcf1"
title: "Show HN: Flide: Make Jev-like decision models up to 9.5x faster"
url: "https://github.com/OmniJev/Flide"
link: "https://github.com/OmniJev/Flide"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-09T04:43:12Z"
published_date: "2026-11-09"
collected_at: "2026-11-09T13:04:29Z"
authors: ["unikcc"]
language: "en"
summary: "Decision models need their own inference engine. So we developed Flide, a high-performance and exact inference engine for Jev-like decision models. Flide achieves up to a 9.5x speedup over vLLM and SGLang. It now supports 30+ popular local Jev-like decision models. Start to make your decision immediately: pip install flide"
tags: []
orgs: ["Perplexity"]
topics: ["models & research", "products & launches", "search & media"]
content_source: "fulltext"
word_count: 581
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50421155"
score: 60
comments: 16
community: "Hacker News"
---

# Show HN: Flide: Make Jev-like decision models up to 9.5x faster

GitHub · unikcc · 2026-11-09

News · Quick start · Models · Options
Flide is fast inference infrastructure for Jev-style decision models. With exact state forking it is up to 9.5 times faster than vLLM and SGLang, and every answer is the one the model gives the question alone. It serves the Jev /v1/systemone API.
- 🔥 2026-11-09 We added Ainvest-Decision, Darwin-27B-RSI-Decision and KnowLine-31B-Gen1.5 in Flide 0.1.10, and the KnowLine family now reads images.
- 🔥 2026-11-09 We added pplx-decider-v1.1-27b and JEV-35B in Flide 0.1.9, and /v1/systemone now takes several requests in one body.
- 🔥 2026-11-08 We added two decision model families in Flide 0.1.8, including AutoTrust and Clef, and also drex-max-v1.
Earlier news
- 🔥 2026-11-02 We released our paper Flide: Accelerating Decision Inference with Exact State Forking on arXiv.
- 🔥 2026-10-29 We added three decision model families in Flide 0.1.7, including SynACK Decide, Wald and Xor, and Gemma 4 mixture-of-experts models such as KnowLine-26B-A4B.
- 🔥 2026-10-29 We added two decision model families in Flide 0.1.6, including Drex and KnowLine, and flide verify checks exact forking on your own model and requests.
- 🔥 2026-10-28 We added six decision model families in Flide 0.1.5, including Jeffan, JevAny, Kev, Lychee, pplx-decider and StartLux, and images for Lumma and mammoth.
- 🔥 2026-10-26 We added five decision model families in Flide 0.1.4, including cerno, JADE, Linne, mammoth and Sieve, and also Quyet-1.0-Large.
- 🔥 2026-10-26 We added eight decision model families in Flide 0.1.3, including AJev, Bespoke-Nimble, Darwin, jiwo, Lumma, mogan, Quyet and Senova, and LoRA adapters now serve as they are.
- 🔥 2026-10-25 We added two decision model families in Flide 0.1.2, including Intern-Decision and torchcast, and a question now takes up to 256 options.
- 🔥 2026-10-24 We released Flide 0.1.0 on PyPI, serving Qwen3.5 and Gemma 4 chat models and the OneJev and Open-Jev decision models. Welcome to have a try.
See the docs for every model, images, the API and all options.
uv venv -p 3.12 && source .venv/bin/activate
uv pip install flide torchvision
flide serve --model OmniJev/OneJev1.6-0.8B
Any model in the model table starts the same way, for example Perplexity's decision model.
flide serve --model perplexity-ai/pplx-decider-flash-v1.2
Every one of them answers this request.
curl http://localhost:8000/v1/systemone -H "Content-Type: application/json" -d '{
  "state": "Order #1182 arrived with a cracked screen. The customer asks for a refund and attached two photos.",
  "questions": {
    "action": {"type": "choice", "instructions": "What should support do next?",
               "criteria": {"refund": "refund the order", "replace": "send a replacement", "escalate": "ask a human"}},
    "urgent": {"type": "noul", "instructions": "Does this need a reply within the hour?"}
  }
}'
The last three columns say how much faster Flide answers one request than the engine its release ships, as the median latency over the requests of each workload on one H200, where DI is the Decision Index. The chat models run against the faster of vLLM and SGLang, and OneJev against qev, the engine it used before Flide. KnowLine 35B runs with --quantize fp8, as its release serves it in FP8. A value marked ~ is the average over the sizes tested.
Apache-2.0. flide/kernels/gdn.py holds a kernel derived from two kernels of
flash-linear-attention (MIT); THIRD_PARTY_NOTICES lists it with
the other code Flide builds on.
If you use Flide in your research, please cite our paper.
@article{li2026flide,
  title   = {Flide: Accelerating Decision Inference with Exact State Forking},
  author  = {Li, Bobo and Song, Jiajia and Fei, Hao and Hsu, Wynne and Lee, Mong Li},
  journal = {arXiv preprint arXiv:2610.42148},
  year    = {2026}
}
