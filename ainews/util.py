"""Shared helpers: HTTP session, URL canonicalisation, dates, slugs."""
from __future__ import annotations

import hashlib
import logging
import re
import time
from datetime import datetime, timezone
from typing import Iterable, Optional
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import requests
from dateutil import parser as dateparser

log = logging.getLogger("ainews")

USER_AGENT = (
    "Mozilla/5.0 (compatible; ai-news-discourse/0.1; "
    "+https://github.com/kevinfd/ai-news-discourse; research crawler)"
)


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
    return s


def get_with_retry(
    sess: requests.Session,
    url: str,
    *,
    params: Optional[dict] = None,
    timeout: int = 25,
    retries: int = 3,
    backoff: float = 6.0,
    headers: Optional[dict] = None,
) -> Optional[requests.Response]:
    """GET with simple backoff on 429/5xx. Returns None on final failure."""
    for attempt in range(retries):
        try:
            r = sess.get(url, params=params, timeout=timeout, headers=headers)
        except requests.RequestException as e:
            log.debug("GET %s failed (%s), attempt %d", url, e, attempt + 1)
            time.sleep(backoff * (attempt + 1))
            continue
        if r.status_code == 200:
            return r
        if r.status_code in (429, 500, 502, 503, 504):
            wait = backoff * (attempt + 1)
            ra = r.headers.get("Retry-After")
            if ra and ra.isdigit():
                wait = max(wait, float(ra))
            log.debug("GET %s -> %s, sleeping %.0fs", url, r.status_code, wait)
            time.sleep(wait)
            continue
        log.debug("GET %s -> %s", url, r.status_code)
        return None
    return None


# ---------------------------------------------------------------------------
# URLs
# ---------------------------------------------------------------------------
_TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "utm_id",
    "fbclid", "gclid", "mc_cid", "mc_eid", "ref", "ref_src", "s", "smid", "ocid",
    "cmpid", "guccounter", "guce_referrer", "guce_referrer_sig", "__twitter_impression",
    "ncid", "sh", "src", "source", "ICID", "taid", "rss", "feedType", "feedName",
}


def canonical_url(url: str) -> str:
    """Normalise a URL so the same article from two feeds dedupes."""
    url = (url or "").strip()
    if not url:
        return ""
    parts = urlsplit(url)
    scheme = "https" if parts.scheme in ("http", "https", "") else parts.scheme
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    if host.startswith("amp."):
        host = host[4:]
    path = re.sub(r"/+$", "", parts.path or "")
    path = re.sub(r"/amp$", "", path)
    if path.endswith("/index.html"):
        path = path[: -len("/index.html")]
    q = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=False)
         if k not in _TRACKING_PARAMS and not k.lower().startswith("utm_")]
    query = urlencode(sorted(q))
    return urlunsplit((scheme, host, path, query, ""))


def domain_of(url: str) -> str:
    host = (urlsplit(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def article_id(url: str) -> str:
    return hashlib.sha1(canonical_url(url).encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# Dates
# ---------------------------------------------------------------------------
def parse_date(value) -> Optional[datetime]:
    """Parse anything date-like into an aware UTC datetime (or None)."""
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        dt = value
    elif isinstance(value, (int, float)):
        dt = datetime.fromtimestamp(value, tz=timezone.utc)
    elif hasattr(value, "tm_year"):  # time.struct_time from feedparser
        dt = datetime(*value[:6], tzinfo=timezone.utc)
    else:
        try:
            dt = dateparser.parse(str(value))
        except (ValueError, TypeError, OverflowError):
            return None
        if dt is None:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def iso_utc(dt: Optional[datetime]) -> Optional[str]:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ") if dt else None


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


# ---------------------------------------------------------------------------
# Text
# ---------------------------------------------------------------------------
_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"[ \t\r\f\v]+")


def strip_html(text: str) -> str:
    import html as _html
    if not text:
        return ""
    text = _TAG_RE.sub(" ", text)
    text = _html.unescape(text)
    text = _WS_RE.sub(" ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return text.strip()


def truncate(text: str, n: int) -> str:
    text = text or ""
    if len(text) <= n:
        return text
    cut = text[: n - 1]
    if " " in cut:
        cut = cut[: cut.rfind(" ")]
    return cut + "…"


_SAFE_FILENAME_RE = re.compile(r'[\\/:*?"<>|\x00-\x1f]+')


def safe_filename(title: str, max_len: int = 110) -> str:
    """Make a readable, filesystem-safe filename stem out of a title."""
    t = _SAFE_FILENAME_RE.sub(" ", title or "untitled")
    t = re.sub(r"\s+", " ", t).strip(" .")
    if len(t) > max_len:
        t = t[:max_len].rsplit(" ", 1)[0].rstrip(" .")
    return t or "untitled"


def uniq(items: Iterable[str]) -> list[str]:
    seen, out = set(), []
    for it in items:
        it = (it or "").strip()
        if it and it.lower() not in seen:
            seen.add(it.lower())
            out.append(it)
    return out
