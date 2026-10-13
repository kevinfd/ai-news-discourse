"""GDELT DOC 2.0 article list API (no key). Broad mainstream/international coverage.

Unofficial limit is roughly one request per 5 s per IP; we sleep 6 s.
"""
from __future__ import annotations

import logging
import time
from datetime import datetime, timedelta
from typing import Iterator

from . import Candidate
from ..util import domain_of, get_with_retry, parse_date, session

log = logging.getLogger("ainews.gdelt")
API = "https://api.gdeltproject.org/api/v2/doc/doc"


def _windows(since: datetime, until: datetime, hours: int = 24):
    cur = since
    while cur < until:
        nxt = min(cur + timedelta(hours=hours), until)
        yield cur, nxt
        cur = nxt


def collect_gdelt(cfg: dict, since: datetime, until: datetime) -> Iterator[Candidate]:
    sess = session()
    excl = tuple(cfg.get("exclude_domains", []))
    maxrec = int(cfg.get("max_records", 250))
    seen: set[str] = set()
    first = True
    for q in cfg.get("queries", []):
        for start, end in _windows(since, until):
            if not first:
                time.sleep(6)
            first = False
            r = get_with_retry(sess, API, params={
                "query": q, "mode": "artlist", "maxrecords": maxrec, "format": "json",
                "sort": "datedesc",
                "startdatetime": start.strftime("%Y%m%d%H%M%S"),
                "enddatetime": end.strftime("%Y%m%d%H%M%S"),
            }, backoff=10, retries=4, timeout=40)
            if not r:
                log.warning("gdelt: no response for %r %s..%s", q[:40], start.date(), end.date())
                continue
            try:
                arts = r.json().get("articles", [])
            except ValueError:
                log.warning("gdelt: non-JSON response (%s)", r.text[:120])
                continue
            n = 0
            for a in arts:
                url = a.get("url") or ""
                if not url or url in seen:
                    continue
                d = domain_of(url)
                if any(d == x or d.endswith("." + x) for x in excl):
                    continue
                if (a.get("language") or "English") != "English":
                    continue
                seen.add(url)
                n += 1
                yield Candidate(
                    url=url,
                    title=a.get("title") or "",
                    source="",          # from domain / page metadata later
                    source_type="wire",
                    collector="gdelt",
                    published=parse_date(a.get("seendate")),
                    image=a.get("socialimage") or None,
                    language="en",
                    tags=[t for t in [a.get("sourcecountry")] if t],
                    ai_specific=False,
                )
            log.info("gdelt %-40s %s..%s -> %d/%d new", q[:40], start.strftime("%m-%d %H:%M"), end.strftime("%m-%d %H:%M"), n, len(arts))
