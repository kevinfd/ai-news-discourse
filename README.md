# AI news discourse — a living dataset

A daily-updated corpus of English-language public discourse about artificial
intelligence: mainstream news, tech press, company and lab blogs, newsletters,
research-institution news, policy announcements, and community discussion
(Hacker News, Reddit). Every item is one markdown file whose YAML frontmatter
carries the same homogenised metadata regardless of where it came from, and
whose body is the article's full text when it could be fetched.

The repository is the dataset. A GitHub Actions workflow runs every morning at
08:00 America/New_York, collects the last 36 hours, de-duplicates against
`data/index.jsonl`, writes new files under `articles/YYYY/MM/DD/`, and pushes.
Latent Lab follows the repository as a git live source and embeds every new
file incrementally, so the map grows day by day without reprocessing history.

## Layout

```
articles/YYYY/MM/DD/<Title> [<id8>].md   one article per file (ingested by Latent Lab)
data/index.jsonl                          id, url, title, source, date, path — the dedupe ledger
data/last-run.json                        stats from the most recent run
config/sources.yaml                       feed registry + collector settings
ainews/                                   the collector package
.github/workflows/collect.yml             the 08:00 schedule
```

## Sources (free, no paid access)

| Collector | What | Key? | Full text? |
|---|---|---|---|
| `rss` | ~100 publisher feeds (see `config/sources.yaml`) | no | fetched with trafilatura; feed summary when paywalled |
| `hackernews` | Algolia HN search, stories ≥ 10 points matching AI queries | no | linked article fetched; Ask HN text kept as post |
| `reddit` | public `.rss` of r/artificial, r/MachineLearning, r/LocalLLaMA, r/singularity, r/OpenAI, r/ClaudeAI, r/ArtificialInteligence, r/ChatGPT | no | linked article fetched; self posts kept as post |
| `bingnews` | Bing News RSS search, ~23 AI queries (mainstream breadth) | no | fetched |
| `gdelt` | GDELT DOC 2.0 (disabled by default: shared-IP rate limit makes it unusable from GitHub runners) | no | fetched |
| `guardian_api` | Guardian Open Platform search | `GUARDIAN_API_KEY` (free) | API body text |
| `nyt_api` | NYT Article Search | `NYT_API_KEY` (free) | abstract + lead only |

Feeds that are not AI-specific pass through a keyword relevance filter
(`ainews/relevance.py`). Hard-paywalled domains (NYT, WSJ, Bloomberg, FT, The
Information, The Economist, …) are never fetched; their records keep the feed
summary and are flagged `paywalled: true`.

## The homogenised record

```yaml
---
id: "1950a6eafc69d45a"            # sha1(canonical url)[:16]
title: "…"
url: "https://…"                  # canonical (tracking params stripped)
source: "Ars Technica"            # publisher display name
domain: "arstechnica.com"
source_type: "tech_press"         # mainstream_news | tech_press | company_blog | newsletter | research | policy | community | wire
collector: "rss"                  # rss | hackernews | reddit | bingnews | gdelt | guardian_api | nyt_api
date: "2026-10-12T20:59:50Z"      # published (UTC) — Latent Lab's timeline reads this key
published_date: "2026-10-12"
collected_at: "2026-10-13T12:03:44Z"
authors: ["Kyle Orland"]
language: "en"
summary: "…"                      # ≤ 400 chars
tags: ["AI", "Gaming"]            # publisher categories / subreddit / GDELT country
orgs: ["Anthropic", "Google"]     # organisations mentioned (regex, ordered by count)
topics: ["agents & coding"]       # coarse keyword topics for filtering
content_source: "fulltext"        # fulltext | summary | api | post
word_count: 246
paywalled: false
image: "https://…"
discussion_url: null              # HN / Reddit thread when the item came via a community
score: null                       # HN points / Reddit score
comments: null
community: null                   # "Hacker News", "r/LocalLLaMA", …
---
```

## Running locally

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m ainews.pipeline --since-hours 36 --max-fetch 600      # a normal daily run
python -m ainews.pipeline --backfill-days 7 --max-fetch 1500    # seed history
python -m ainews.pipeline --only rss,hackernews --dry-run -v    # debug one collector
python -m pytest tests
```

Optional environment variables: `GUARDIAN_API_KEY`, `NYT_API_KEY` (both free
developer keys). In GitHub Actions these are repository secrets, as are the
optional `LATENTLAB_WEBHOOK_URL` / `LATENTLAB_WEBHOOK_SECRET` that make Latent
Lab sync immediately after each push instead of waiting for its poll interval.

## Latent Lab

The dataset is registered as a git live source with
`exclude_extensions: [.json, .jsonl, .yaml, .yml, .py, .txt, .toml, .cfg, .lock]`
so only the article markdown is embedded. `date_frontmatter_key` is left on
`auto`, which reads the `date:` key above for the timeline.

Note on metadata: Latent Lab's folder/git ingest currently reads only the date
from frontmatter; the other keys are embedded with the text but are not yet
exposed as filterable metadata columns. The frontmatter is deliberately flat
(top-level scalars and flow lists only) so that a small extension of the
ingest — surfacing `frontmatter_scalars()` as item metadata — makes every
field above a column with no change to this repository.

## Copyright

Full article text is stored for research use by the MIT Media Lab. The
repository is private; do not redistribute article bodies.
