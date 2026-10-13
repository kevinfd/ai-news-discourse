"""Bing News RSS search (no key). Broad mainstream coverage; replaces GDELT's role.

Each query returns ~10 recent stories; many queries + dedupe give breadth.
The item link is a bing.com redirect whose `url` param is the real article.
"""
from __future__ import annotations

import logging
import time
from datetime import datetime
from typing import Iterator
from urllib.parse import parse_qs, urlsplit
import xml.etree.ElementTree as ET

from . import Candidate
from ..util import domain_of, get_with_retry, parse_date, session, strip_html, truncate

log = logging.getLogger("ainews.bing")
API = "https://www.bing.com/news/search"
_NS = "News"  # Bing's extension elements are namespaced by the feed URL; match on local name.


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _real_url(link: str) -> str:
    if "bing.com/news/apiclick" in link:
        qs = parse_qs(urlsplit(link).query)
        if qs.get("url"):
            return qs["url"][0]
    return link


def collect_bingnews(cfg: dict, since: datetime) -> Iterator[Candidate]:
    sess = session()
    excl = tuple(cfg.get("exclude_domains", []))
    seen: set[str] = set()
    for i, q in enumerate(cfg.get("queries", [])):
        if i:
            time.sleep(2)
        r = get_with_retry(sess, API, params={"q": q, "format": "rss", "cc": "us", "setlang": "en"}, backoff=5)
        if not r:
            log.warning("bing: no response for %r", q)
            continue
        try:
            root = ET.fromstring(r.content)
        except ET.ParseError as e:
            log.warning("bing: parse error for %r: %s", q, e)
            continue
        n = 0
        for it in root.iter("item"):
            url = _real_url(it.findtext("link") or "")
            title = strip_html(it.findtext("title") or "")
            if not url or not title or url in seen:
                continue
            d = domain_of(url)
            if any(d == x or d.endswith("." + x) for x in excl):
                continue
            published = parse_date(it.findtext("pubDate"))
            if published and published < since:
                continue
            source, image = "", None
            for ch in it:
                name = _local(ch.tag)
                if name == "Source":
                    source = (ch.text or "").strip()
                elif name == "Image":
                    image = (ch.text or "").strip() or None
            seen.add(url)
            n += 1
            yield Candidate(
                url=url, title=title, source=source, source_type="mainstream_news", collector="bingnews",
                published=published, summary=truncate(strip_html(it.findtext("description") or ""), 600),
                image=image, ai_specific=False,
            )
        log.info("bing %-36s -> %d new", q[:36], n)
    log.info("bing: %d unique stories across %d queries", len(seen), len(cfg.get("queries", [])))
