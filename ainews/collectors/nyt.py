"""New York Times Article Search API (free key; abstracts + rich keywords, no body)."""
from __future__ import annotations

import logging
import os
import time
from datetime import datetime
from typing import Iterator

from . import Candidate
from ..util import get_with_retry, parse_date, session, truncate

log = logging.getLogger("ainews.nyt")
API = "https://api.nytimes.com/svc/search/v2/articlesearch.json"


def collect_nyt(since: datetime, until: datetime) -> Iterator[Candidate]:
    key = os.environ.get("NYT_API_KEY")
    if not key:
        log.info("nyt: NYT_API_KEY not set, skipping")
        return
    sess = session()
    for page in range(0, 5):
        r = get_with_retry(sess, API, params={
            "api-key": key, "q": "artificial intelligence",
            "begin_date": since.strftime("%Y%m%d"), "end_date": until.strftime("%Y%m%d"),
            "sort": "newest", "page": page,
        }, backoff=12)
        if not r:
            break
        docs = r.json().get("response", {}).get("docs", [])
        if not docs:
            break
        for d in docs:
            head = (d.get("headline") or {}).get("main") or ""
            body = " ".join(x for x in [d.get("abstract"), d.get("lead_paragraph")] if x)
            mm = d.get("multimedia") or []
            img = None
            if isinstance(mm, list) and mm:
                img = "https://www.nytimes.com/" + mm[0].get("url", "") if mm[0].get("url") else None
            elif isinstance(mm, dict):
                img = (mm.get("default") or {}).get("url")
            yield Candidate(
                url=d.get("web_url"), title=head, source="The New York Times",
                source_type="mainstream_news", collector="nyt_api",
                published=parse_date(d.get("pub_date")),
                summary=truncate(d.get("abstract") or "", 600),
                authors=[p.get("firstname", "") + " " + p.get("lastname", "") for p in (d.get("byline") or {}).get("person", [])][:6],
                tags=[k.get("value") for k in d.get("keywords", []) if k.get("value")][:12],
                image=img, paywalled=True, body=body if body else None, content_source="api" if body else None,
            )
        time.sleep(12)  # NYT: 5 req/min on the free tier
