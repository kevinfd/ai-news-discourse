"""Collectors. Each yields `Candidate` records; the pipeline homogenises them."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Candidate:
    url: str
    title: str
    source: str
    source_type: str
    collector: str
    published: Optional[datetime] = None
    summary: str = ""
    authors: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    image: Optional[str] = None
    language: str = "en"
    ai_specific: bool = False       # True -> skip relevance filter
    paywalled: bool = False         # True -> don't fetch full text
    body: Optional[str] = None      # pre-fetched body (API bodyText, self-post text)
    content_source: Optional[str] = None
    discussion_url: Optional[str] = None
    score: Optional[int] = None
    comments: Optional[int] = None
    community: Optional[str] = None
