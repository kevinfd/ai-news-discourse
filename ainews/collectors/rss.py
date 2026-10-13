"""RSS / Atom feed collector (feedparser)."""
from __future__ import annotations

import logging
import time
from datetime import datetime
from typing import Iterator

import feedparser

from . import Candidate
from ..util import USER_AGENT, parse_date, strip_html, truncate, uniq

log = logging.getLogger("ainews.rss")


def _entry_date(e) -> datetime | None:
    for key in ("published_parsed", "updated_parsed", "created_parsed"):
        if e.get(key):
            return parse_date(e[key])
    for key in ("published", "updated", "created", "dc_date"):
        if e.get(key):
            return parse_date(e[key])
    return None


def _entry_image(e) -> str | None:
    for mc in e.get("media_content", []) or []:
        if mc.get("url") and (mc.get("medium") == "image" or str(mc.get("type", "")).startswith("image")):
            return mc["url"]
    for mt in e.get("media_thumbnail", []) or []:
        if mt.get("url"):
            return mt["url"]
    for enc in e.get("enclosures", []) or []:
        if str(enc.get("type", "")).startswith("image") and enc.get("href"):
            return enc["href"]
    return None


def _entry_summary(e) -> str:
    raw = ""
    if e.get("content"):
        raw = e["content"][0].get("value", "") or ""
    if not raw:
        raw = e.get("summary", "") or e.get("description", "") or ""
    return strip_html(raw)


def collect_feed(feed: dict, since: datetime) -> Iterator[Candidate]:
    name, url = feed["name"], feed["url"]
    t0 = time.time()
    parsed = feedparser.parse(url, agent=USER_AGENT, request_headers={"Accept": "application/rss+xml, application/atom+xml, application/xml;q=0.9, */*;q=0.8"})
    status = getattr(parsed, "status", None)
    if parsed.bozo and not parsed.entries:
        log.warning("feed %-28s status=%s error=%s", name, status, getattr(parsed, "bozo_exception", ""))
        return
    n = 0
    for e in parsed.entries:
        link = e.get("link") or ""
        title = strip_html(e.get("title", "")) or ""
        if not link or not title:
            continue
        published = _entry_date(e)
        if published and published < since:
            continue
        summary_full = _entry_summary(e)
        authors = uniq([a.get("name", "") for a in e.get("authors", []) or []] + [e.get("author", "")])
        tags = uniq([t.get("term", "") for t in e.get("tags", []) or []])[:12]
        n += 1
        yield Candidate(
            url=link,
            title=title,
            source=name,
            source_type=feed.get("type", "tech_press"),
            collector="rss",
            published=published,
            summary=truncate(summary_full, 600),
            authors=authors[:6],
            tags=tags,
            image=_entry_image(e),
            ai_specific=bool(feed.get("ai_specific", False)),
            paywalled=bool(feed.get("paywalled", False)),
            # Feed-provided full content (Substack, some blogs) is a usable body
            # if the fetch fails; keep it around.
            body=summary_full if len(summary_full.split()) >= 250 else None,
        )
    log.info("feed %-28s status=%s entries=%d kept=%d (%.1fs)", name, status, len(parsed.entries), n, time.time() - t0)
