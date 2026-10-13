"""Orchestrator: collect -> filter -> dedupe -> extract -> homogenise -> write.

Usage:
    python -m ainews.pipeline --since-hours 36 --max-fetch 600
    python -m ainews.pipeline --backfill-days 7 --max-fetch 1500
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import logging
import os
import sys
import time
from collections import Counter
from datetime import timedelta
from pathlib import Path

import yaml

from .collectors import Candidate
from .collectors.bingnews import collect_bingnews
from .collectors.gdelt import collect_gdelt
from .collectors.guardian import collect_guardian
from .collectors.hackernews import collect_hackernews
from .collectors.nyt import collect_nyt
from .collectors.reddit import collect_reddit
from .collectors.rss import collect_feed
from .extract import fetch_fulltext, is_paywalled
from .relevance import detect_orgs, detect_topics, is_ai_relevant
from .schema import Article
from .store import Store
from .util import article_id, canonical_url, domain_of, iso_utc, now_utc, parse_date, truncate, uniq

log = logging.getLogger("ainews")

# Friendly names for domains that arrive without one (GDELT, HN, Reddit links).
DOMAIN_NAMES = {
    "reuters.com": "Reuters", "apnews.com": "AP News", "cnn.com": "CNN", "bbc.com": "BBC News",
    "bbc.co.uk": "BBC News", "nytimes.com": "The New York Times", "wsj.com": "Wall Street Journal",
    "bloomberg.com": "Bloomberg", "ft.com": "Financial Times", "theguardian.com": "The Guardian",
    "washingtonpost.com": "Washington Post", "cnbc.com": "CNBC", "forbes.com": "Forbes",
    "businessinsider.com": "Business Insider", "techcrunch.com": "TechCrunch", "theverge.com": "The Verge",
    "arstechnica.com": "Ars Technica", "wired.com": "WIRED", "venturebeat.com": "VentureBeat",
    "zdnet.com": "ZDNet", "theregister.com": "The Register", "axios.com": "Axios", "politico.com": "Politico",
    "theatlantic.com": "The Atlantic", "economist.com": "The Economist", "fortune.com": "Fortune",
    "time.com": "TIME", "npr.org": "NPR", "nbcnews.com": "NBC News", "abcnews.go.com": "ABC News",
    "cbsnews.com": "CBS News", "foxnews.com": "Fox News", "usatoday.com": "USA Today", "latimes.com": "Los Angeles Times",
    "semafor.com": "Semafor", "theinformation.com": "The Information", "404media.co": "404 Media",
    "technologyreview.com": "MIT Technology Review", "engadget.com": "Engadget", "cnet.com": "CNET",
    "fastcompany.com": "Fast Company", "qz.com": "Quartz", "vox.com": "Vox", "slate.com": "Slate",
    "theinformation.com": "The Information", "nature.com": "Nature", "science.org": "Science",
    "scmp.com": "South China Morning Post", "aljazeera.com": "Al Jazeera", "dw.com": "DW",
    "france24.com": "France 24", "euronews.com": "Euronews", "independent.co.uk": "The Independent",
    "telegraph.co.uk": "The Telegraph", "thetimes.com": "The Times", "standard.co.uk": "Evening Standard",
    "news.sky.com": "Sky News", "openai.com": "OpenAI", "anthropic.com": "Anthropic", "deepmind.google": "Google DeepMind",
    "blog.google": "Google", "ai.meta.com": "Meta AI", "about.fb.com": "Meta", "microsoft.com": "Microsoft",
    "blogs.microsoft.com": "Microsoft", "nvidia.com": "NVIDIA", "blogs.nvidia.com": "NVIDIA", "huggingface.co": "Hugging Face",
    "x.ai": "xAI", "mistral.ai": "Mistral AI", "deepseek.com": "DeepSeek", "github.com": "GitHub", "github.blog": "GitHub",
    "arxiv.org": "arXiv", "simonwillison.net": "Simon Willison", "substack.com": "Substack", "medium.com": "Medium",
    "news.ycombinator.com": "Hacker News", "reddit.com": "Reddit", "redd.it": "Reddit", "i.redd.it": "Reddit", "v.redd.it": "Reddit", "youtube.com": "YouTube", "x.com": "X",
}


def friendly_source(domain: str, sitename: str | None = None) -> str:
    if domain in DOMAIN_NAMES:
        return DOMAIN_NAMES[domain]
    parts = domain.split(".")
    for i in range(len(parts) - 1):
        cand = ".".join(parts[i:])
        if cand in DOMAIN_NAMES:
            return DOMAIN_NAMES[cand]
    if sitename and 2 <= len(sitename) <= 60:
        return sitename.strip()
    stem = parts[-2] if len(parts) >= 2 else domain
    return stem.replace("-", " ").title()


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
def gather(cfg: dict, since, until, only: set[str] | None, workers: int) -> list[Candidate]:
    cands: list[Candidate] = []

    def want(name: str) -> bool:
        return only is None or name in only

    if want("rss"):
        feeds = [f for f in cfg.get("feeds", []) if f.get("enabled", True)]
        with cf.ThreadPoolExecutor(max_workers=workers) as ex:
            for result in ex.map(lambda f: _safe_list(collect_feed, f, since), feeds):
                cands.extend(result)
        log.info("rss: %d candidates from %d feeds", len(cands), len(feeds))

    if want("hackernews"):
        cands.extend(_safe_list(collect_hackernews, cfg.get("hackernews", {}), since, until))
    if want("reddit"):
        cands.extend(_safe_list(collect_reddit, cfg.get("reddit", []), since))
    if want("bingnews"):
        cands.extend(_safe_list(collect_bingnews, cfg.get("bingnews", {}), since))
    if want("gdelt") and cfg.get("gdelt", {}).get("enabled", True):
        cands.extend(_safe_list(collect_gdelt, cfg.get("gdelt", {}), since, until))
    if want("guardian"):
        cands.extend(_safe_list(collect_guardian, since, until))
    if want("nyt"):
        cands.extend(_safe_list(collect_nyt, since, until))
    return cands


def _safe_list(fn, *args) -> list:
    try:
        return list(fn(*args))
    except Exception as e:  # one broken collector must not kill the run
        log.exception("collector %s failed: %s", getattr(fn, "__name__", fn), e)
        return []


# ---------------------------------------------------------------------------
def merge(cands: list[Candidate], store: Store, stats: Counter) -> list[Candidate]:
    """Canonicalise URLs, drop known/irrelevant, merge same-URL duplicates."""
    by_id: dict[str, Candidate] = {}
    priority = {"rss": 0, "guardian_api": 0, "nyt_api": 0, "hackernews": 1, "reddit": 2, "bingnews": 3, "gdelt": 4}
    for c in sorted(cands, key=lambda c: priority.get(c.collector, 9)):
        if not c.url or not c.title:
            stats["dropped_empty"] += 1
            continue
        c.url = canonical_url(c.url)
        aid = article_id(c.url)
        if store.known(aid):
            stats["already_known"] += 1
            continue
        if aid in by_id:
            _merge_into(by_id[aid], c)
            stats["merged_duplicates"] += 1
            continue
        if not c.ai_specific and not is_ai_relevant(c.title, c.summary, (c.body or "")[:2000]):
            stats["not_ai"] += 1
            continue
        if store.title_known(c.title) and c.collector in ("gdelt", "bingnews", "hackernews", "reddit", "rss"):
            stats["title_duplicate"] += 1
            continue
        by_id[aid] = c
    return list(by_id.values())


def _merge_into(base: Candidate, other: Candidate) -> None:
    if not base.summary and other.summary:
        base.summary = other.summary
    if not base.authors and other.authors:
        base.authors = other.authors
    if not base.image and other.image:
        base.image = other.image
    if not base.published and other.published:
        base.published = other.published
    base.tags = uniq(base.tags + other.tags)[:12]
    if other.discussion_url and not base.discussion_url:
        base.discussion_url, base.score, base.comments, base.community = (
            other.discussion_url, other.score, other.comments, other.community)
    elif other.discussion_url and (other.score or 0) > (base.score or 0):
        base.discussion_url, base.score, base.comments, base.community = (
            other.discussion_url, other.score, other.comments, other.community)
    if not base.body and other.body:
        base.body, base.content_source = other.body, other.content_source
    if base.source_type == "wire" and other.source_type != "wire":
        base.source_type = other.source_type
    if not base.source and other.source:
        base.source = other.source


# ---------------------------------------------------------------------------
def build_article(c: Candidate, collected_at: str, fetch: bool) -> Article:
    extracted = None
    text, content_source = None, None
    if c.body:
        text, content_source = c.body, (c.content_source or "summary")
    if fetch and content_source not in ("post", "api") and not c.paywalled and not is_paywalled(c.url):
        extracted = fetch_fulltext(c.url)
        if extracted:
            text, content_source = extracted.text, "fulltext"
    if not text:
        text = c.summary or c.title
        content_source = content_source or "summary"
    if text.strip() and c.summary and text.strip() == c.summary.strip() and len(text.split()) < 15:
        text = f"{c.title}. {text}"

    domain = domain_of(c.url)
    source = c.source or friendly_source(domain, extracted.sitename if extracted else None)
    published = c.published or (parse_date(extracted.date) if extracted and extracted.date else None)
    authors = uniq(c.authors or (extracted.authors if extracted else []))[:6]
    language = (extracted.language if extracted and extracted.language else None) or c.language or "en"
    blob = f"{c.title}\n{c.summary}\n{text[:6000]}"
    paywalled = bool(c.paywalled or is_paywalled(c.url)) and content_source != "fulltext"

    return Article(
        id=article_id(c.url), title=c.title.strip(), url=c.url, source=source, domain=domain,
        source_type=c.source_type, collector=c.collector, date=iso_utc(published) or collected_at,
        collected_at=collected_at, text=text, authors=authors, language=language[:5],
        summary=truncate(c.summary or text, 400), tags=c.tags[:12], orgs=detect_orgs(blob),
        topics=detect_topics(blob), content_source=content_source, word_count=len(text.split()),
        paywalled=paywalled, image=c.image, discussion_url=c.discussion_url, score=c.score,
        comments=c.comments, community=c.community,
    )


# ---------------------------------------------------------------------------
def run(args) -> dict:
    root = Path(args.root)
    cfg = load_config(root / args.config)
    store = Store(root)
    until = now_utc()
    since = until - timedelta(days=args.backfill_days) if args.backfill_days else until - timedelta(hours=args.since_hours)
    only = set(args.only.split(",")) if args.only else None
    collected_at = iso_utc(until)
    stats: Counter = Counter()
    t0 = time.time()
    log.info("run: since=%s until=%s known=%d only=%s", iso_utc(since), collected_at, store.count(), only)

    cands = gather(cfg, since, until, only, args.workers)
    stats["candidates"] = len(cands)
    new = merge(cands, store, stats)
    stats["new_unique"] = len(new)
    log.info("merge: %s", dict(stats))

    # Fetch budget: prefer curated feeds and community picks over the GDELT firehose.
    order = {"rss": 0, "guardian_api": 0, "nyt_api": 0, "hackernews": 1, "reddit": 2, "bingnews": 3, "gdelt": 4}
    new.sort(key=lambda c: (order.get(c.collector, 9), -(c.score or 0)))
    fetch_flags = [i < args.max_fetch for i in range(len(new))]

    written = 0
    per_source: Counter = Counter()
    per_content: Counter = Counter()
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = [ex.submit(build_article, c, collected_at, f) for c, f in zip(new, fetch_flags)]
        for fut in cf.as_completed(futs):
            try:
                art = fut.result()
            except Exception as e:
                log.exception("build failed: %s", e)
                stats["build_errors"] += 1
                continue
            if args.dry_run:
                written += 1
                continue
            store.write(art)
            written += 1
            per_source[art.source] += 1
            per_content[art.content_source] += 1
    stats["written"] = written
    stats["seconds"] = round(time.time() - t0)
    summary = {
        "run_at": collected_at, "since": iso_utc(since), "stats": dict(stats),
        "by_content_source": dict(per_content), "top_sources": per_source.most_common(25),
        "total_articles": store.count(),
    }
    if not args.dry_run:
        (root / "data" / "last-run.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("done: wrote %d articles in %ds (total %d). content=%s", written, stats["seconds"], store.count(), dict(per_content))
    return summary


def main(argv=None):
    p = argparse.ArgumentParser(description="Collect AI news discourse into markdown articles.")
    p.add_argument("--root", default=".", help="repo root (contains config/, articles/, data/)")
    p.add_argument("--config", default="config/sources.yaml")
    p.add_argument("--since-hours", type=float, default=36, help="look-back window for a normal run")
    p.add_argument("--backfill-days", type=int, default=0, help="override look-back with N days")
    p.add_argument("--max-fetch", type=int, default=600, help="max full-text fetches this run")
    p.add_argument("--workers", type=int, default=8)
    p.add_argument("--only", default=None, help="comma list: rss,hackernews,reddit,bingnews,gdelt,guardian,nyt")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("-v", "--verbose", action="store_true")
    args = p.parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s", datefmt="%H:%M:%S",
        stream=sys.stdout,
    )
    for noisy in ("trafilatura", "urllib3", "charset_normalizer", "htmldate", "courlan"):
        logging.getLogger(noisy).setLevel(logging.WARNING)
    logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)
    summary = run(args)
    print(json.dumps(summary["stats"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
