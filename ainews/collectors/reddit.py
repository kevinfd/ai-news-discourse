"""Reddit via public .rss endpoints (no API key). Polite: 1 request / 6 s."""
from __future__ import annotations

import logging
import re
import time
from datetime import datetime
from typing import Iterator

import feedparser

from . import Candidate
from ..util import get_with_retry, parse_date, session, strip_html, truncate

log = logging.getLogger("ainews.reddit")

_LINK_RE = re.compile(r'<a href="([^"]+)">\[link\]</a>')
_REDDIT_HOST = re.compile(r"^https?://(www\.|old\.|new\.)?reddit\.com/")


def collect_reddit(subs: list[str], since: datetime, listing: str = "top", t: str = "day") -> Iterator[Candidate]:
    sess = session()
    sess.headers["User-Agent"] = "macos:ai-news-discourse:0.1 (research crawler; by u/latentlab)"
    for i, sub in enumerate(subs):
        if i:
            time.sleep(6)
        url = f"https://www.reddit.com/r/{sub}/{listing}/.rss?t={t}&limit=50"
        r = get_with_retry(sess, url, backoff=15, retries=3)
        if not r:
            log.warning("reddit r/%s unavailable", sub)
            continue
        parsed = feedparser.parse(r.content)
        n = 0
        for e in parsed.entries:
            permalink = e.get("link") or ""
            title = strip_html(e.get("title", ""))
            if not permalink or not title:
                continue
            published = parse_date(e.get("updated_parsed") or e.get("published_parsed"))
            if published and published < since:
                continue
            content_html = (e.get("content") or [{}])[0].get("value", "") or e.get("summary", "")
            m = _LINK_RE.search(content_html)
            external = m.group(1) if m else None
            text = strip_html(re.sub(r"<a href=\"[^\"]+\">\[(link|comments)\]</a>", "", content_html))
            text = re.sub(r"submitted by\s+/u/\S+\s*", "", text).strip()
            is_self = not external or _REDDIT_HOST.match(external) is not None
            author = (e.get("author") or "").lstrip("/u/").replace("u/", "")
            n += 1
            yield Candidate(
                url=permalink if is_self else external,
                title=title,
                source="Reddit" if is_self else "",
                source_type="community",
                collector="reddit",
                published=published,
                summary=truncate(text, 600),
                authors=[author] if author else [],
                body=text if is_self and len(text.split()) >= 20 else None,
                content_source="post" if is_self else None,
                discussion_url=permalink,
                community=f"r/{sub}",
                tags=[f"r/{sub}"],
            )
        log.info("reddit r/%-22s entries=%d kept=%d", sub, len(parsed.entries), n)
