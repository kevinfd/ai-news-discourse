"""On-disk layout: articles/YYYY/MM/DD/<Title> [<id8>].md + data/index.jsonl."""
from __future__ import annotations

import json
import os
from pathlib import Path

from .schema import Article
from .util import safe_filename

ARTICLES_DIR = "articles"
INDEX_PATH = os.path.join("data", "index.jsonl")


class Store:
    def __init__(self, root: str | os.PathLike):
        self.root = Path(root)
        self.index_path = self.root / INDEX_PATH
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        self.seen_ids: set[str] = set()
        self.seen_titles: set[str] = set()
        self._load_index()

    def _load_index(self) -> None:
        if not self.index_path.exists():
            return
        with self.index_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                self.seen_ids.add(row.get("id", ""))
                self.seen_titles.add(_title_key(row.get("title", "")))

    def known(self, article_id: str) -> bool:
        return article_id in self.seen_ids

    def title_known(self, title: str) -> bool:
        return _title_key(title) in self.seen_titles

    def write(self, article: Article) -> str:
        day = (article.date or article.collected_at)[:10]
        y, m, d = day.split("-")
        rel_dir = Path(ARTICLES_DIR) / y / m / d
        (self.root / rel_dir).mkdir(parents=True, exist_ok=True)
        fname = f"{safe_filename(article.title)} [{article.id[:8]}].md"
        rel_path = rel_dir / fname
        (self.root / rel_path).write_text(article.to_markdown(), encoding="utf-8")
        with self.index_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(article.index_row(str(rel_path)), ensure_ascii=False) + "\n")
        self.seen_ids.add(article.id)
        self.seen_titles.add(_title_key(article.title))
        return str(rel_path)

    def count(self) -> int:
        return len(self.seen_ids)


def _title_key(title: str) -> str:
    import re
    t = re.sub(r"[^a-z0-9 ]+", " ", (title or "").lower())
    t = re.sub(r"\s+", " ", t).strip()
    return t
