"""Full-text extraction with trafilatura, with graceful fallbacks."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Optional

import trafilatura
from trafilatura.settings import use_config

from .util import domain_of

log = logging.getLogger("ainews.extract")

# Hard paywalls / aggressive bot blocking: don't waste a fetch, keep the summary.
PAYWALLED_DOMAINS = {
    "nytimes.com", "wsj.com", "bloomberg.com", "ft.com", "theinformation.com",
    "economist.com", "washingtonpost.com", "theatlantic.com", "newyorker.com",
    "nature.com", "science.org", "barrons.com", "thetimes.com", "telegraph.co.uk",
    "medium.com", "x.com", "twitter.com", "linkedin.com", "facebook.com",
}

_CFG = use_config()
_CFG.set("DEFAULT", "DOWNLOAD_TIMEOUT", "20")
_CFG.set("DEFAULT", "MAX_FILE_SIZE", "4000000")
_CFG.set("DEFAULT", "USER_AGENTS", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36")


@dataclass
class Extracted:
    text: str
    authors: list[str]
    date: Optional[str]
    image: Optional[str]
    title: Optional[str]
    language: Optional[str]
    sitename: Optional[str]


def is_paywalled(url: str) -> bool:
    d = domain_of(url)
    return any(d == p or d.endswith("." + p) for p in PAYWALLED_DOMAINS)


def fetch_fulltext(url: str, min_words: int = 60) -> Optional[Extracted]:
    """Download `url` and extract the main article text. None on failure."""
    try:
        html = trafilatura.fetch_url(url, config=_CFG)
    except Exception as e:  # network / decoding
        log.debug("fetch failed %s: %s", url, e)
        return None
    if not html:
        return None
    try:
        text = trafilatura.extract(
            html, url=url, include_comments=False, include_tables=False,
            favor_recall=True, deduplicate=True, config=_CFG,
        )
    except Exception as e:
        log.debug("extract failed %s: %s", url, e)
        return None
    if not text or len(text.split()) < min_words:
        return None
    meta = None
    try:
        meta = trafilatura.extract_metadata(html, default_url=url)
    except Exception:
        pass
    authors: list[str] = []
    if meta and meta.author:
        authors = [a.strip() for a in str(meta.author).split(";") if a.strip()]
    return Extracted(
        text=text.strip(),
        authors=authors,
        date=getattr(meta, "date", None),
        image=getattr(meta, "image", None),
        title=getattr(meta, "title", None),
        language=getattr(meta, "language", None),
        sitename=getattr(meta, "sitename", None),
    )
