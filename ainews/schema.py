"""The homogenised article record and its markdown serialisation."""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from typing import Optional

# Every article from every source carries exactly these frontmatter keys, in
# this order. Missing values are written as `null` so columns stay aligned.
FIELD_ORDER = [
    "id", "title", "url", "source", "domain", "source_type", "collector",
    "date", "published_date", "collected_at", "authors", "language", "summary",
    "tags", "orgs", "topics", "content_source", "word_count", "paywalled",
    "image", "discussion_url", "score", "comments", "community",
]


@dataclass
class Article:
    id: str
    title: str
    url: str                      # canonical article URL
    source: str                   # publisher display name
    domain: str
    source_type: str              # mainstream_news | tech_press | company_blog | newsletter | research | policy | community | wire
    collector: str                # rss | hackernews | reddit | gdelt | guardian_api | nyt_api
    date: Optional[str]           # ISO-8601 UTC, published time (Latent Lab reads `date`)
    collected_at: str
    text: str                     # body that gets embedded
    authors: list[str] = field(default_factory=list)
    language: str = "en"
    summary: str = ""
    tags: list[str] = field(default_factory=list)
    orgs: list[str] = field(default_factory=list)
    topics: list[str] = field(default_factory=list)
    content_source: str = "summary"   # fulltext | summary | api | post
    word_count: int = 0
    paywalled: bool = False
    image: Optional[str] = None
    discussion_url: Optional[str] = None
    score: Optional[int] = None
    comments: Optional[int] = None
    community: Optional[str] = None   # e.g. "Hacker News", "r/LocalLLaMA"

    # -- serialisation ----------------------------------------------------
    def frontmatter(self) -> str:
        d = asdict(self)
        d["published_date"] = (self.date or "")[:10] or None
        lines = ["---"]
        for key in FIELD_ORDER:
            lines.append(f"{key}: {_yaml_scalar(d.get(key))}")
        lines.append("---")
        return "\n".join(lines)

    def to_markdown(self) -> str:
        byline = " · ".join(x for x in [self.source, ", ".join(self.authors), (self.date or "")[:10]] if x)
        body = self.text.strip()
        return f"{self.frontmatter()}\n\n# {self.title.strip()}\n\n{byline}\n\n{body}\n"

    def index_row(self, path: str) -> dict:
        return {
            "id": self.id, "url": self.url, "title": self.title, "source": self.source,
            "source_type": self.source_type, "collector": self.collector, "date": self.date,
            "collected_at": self.collected_at, "content_source": self.content_source,
            "word_count": self.word_count, "path": path,
        }


def _yaml_scalar(value) -> str:
    """Emit a value as a single-line YAML scalar/flow-list (JSON is valid YAML)."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, (list, tuple)):
        return "[" + ", ".join(json.dumps(str(v), ensure_ascii=False) for v in value) + "]"
    return json.dumps(str(value), ensure_ascii=False)
