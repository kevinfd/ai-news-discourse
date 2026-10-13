"""The Guardian Open Platform (free developer key; full article body)."""
from __future__ import annotations

import logging
import os
from datetime import datetime
from typing import Iterator

from . import Candidate
from ..util import get_with_retry, parse_date, session, strip_html, truncate

log = logging.getLogger("ainews.guardian")
API = "https://content.guardianapis.com/search"


def collect_guardian(since: datetime, until: datetime) -> Iterator[Candidate]:
    key = os.environ.get("GUARDIAN_API_KEY")
    if not key:
        log.info("guardian: GUARDIAN_API_KEY not set, skipping")
        return
    sess = session()
    page = 1
    while page <= 5:
        r = get_with_retry(sess, API, params={
            "api-key": key, "q": '"artificial intelligence" OR AI OR OpenAI OR chatbot OR "machine learning"',
            "from-date": since.strftime("%Y-%m-%d"), "to-date": until.strftime("%Y-%m-%d"),
            "order-by": "newest", "page-size": 50, "page": page,
            "show-fields": "bodyText,byline,trailText,thumbnail,wordcount,lang",
            "show-tags": "keyword",
        })
        if not r:
            break
        resp = r.json().get("response", {})
        for it in resp.get("results", []):
            f = it.get("fields", {})
            body = f.get("bodyText") or ""
            yield Candidate(
                url=it.get("webUrl"), title=it.get("webTitle") or "",
                source="The Guardian", source_type="mainstream_news", collector="guardian_api",
                published=parse_date(it.get("webPublicationDate")),
                summary=truncate(strip_html(f.get("trailText") or ""), 600),
                authors=[a.strip() for a in (f.get("byline") or "").split(" and ") if a.strip()][:6],
                tags=[t.get("webTitle") for t in it.get("tags", []) if t.get("webTitle")][:12],
                image=f.get("thumbnail"), language=(f.get("lang") or "en"),
                body=body if body else None, content_source="api" if body else None,
                ai_specific=False,
            )
        if page >= int(resp.get("pages", 1)):
            break
        page += 1
    log.info("guardian: fetched %d page(s)", page)
