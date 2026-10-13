"""Hacker News via the Algolia search API (no key, generous limits)."""
from __future__ import annotations

import logging
import time
from datetime import datetime
from typing import Iterator

from . import Candidate
from ..util import get_with_retry, parse_date, session, strip_html

log = logging.getLogger("ainews.hn")
API = "https://hn.algolia.com/api/v1/search_by_date"


def collect_hackernews(cfg: dict, since: datetime, until: datetime | None = None) -> Iterator[Candidate]:
    sess = session()
    seen: set[str] = set()
    min_points = int(cfg.get("min_points", 10))
    filters = f"created_at_i>{int(since.timestamp())},points>={min_points}"
    if until:
        filters += f",created_at_i<{int(until.timestamp())}"
    for q in cfg.get("queries", []):
        for page in range(0, 3):
            r = get_with_retry(sess, API, params={
                "query": q, "tags": "story", "numericFilters": filters,
                "hitsPerPage": 100, "page": page,
            }, backoff=3)
            if not r:
                break
            data = r.json()
            hits = data.get("hits", [])
            for h in hits:
                oid = h.get("objectID")
                if not oid or oid in seen:
                    continue
                seen.add(oid)
                hn_url = f"https://news.ycombinator.com/item?id={oid}"
                url = h.get("url") or hn_url
                story_text = strip_html(h.get("story_text") or "")
                yield Candidate(
                    url=url,
                    title=h.get("title") or "",
                    source="Hacker News" if url == hn_url else "",   # filled from domain later
                    source_type="community",
                    collector="hackernews",
                    published=parse_date(h.get("created_at_i")),
                    summary=story_text[:600],
                    authors=[h.get("author")] if h.get("author") else [],
                    body=story_text if url == hn_url and story_text else None,
                    content_source="post" if url == hn_url and story_text else None,
                    discussion_url=hn_url,
                    score=h.get("points"),
                    comments=h.get("num_comments"),
                    community="Hacker News",
                )
            if page + 1 >= data.get("nbPages", 1):
                break
            time.sleep(0.5)
        time.sleep(0.5)
    log.info("hackernews: %d unique stories across %d queries", len(seen), len(cfg.get("queries", [])))
