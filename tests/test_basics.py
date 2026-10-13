from datetime import datetime, timezone

from ainews.relevance import detect_orgs, detect_topics, is_ai_relevant
from ainews.schema import Article
from ainews.util import canonical_url, article_id, safe_filename, parse_date


def test_canonical_url_strips_tracking_and_www():
    a = canonical_url("https://www.example.com/story/?utm_source=x&id=2#frag")
    b = canonical_url("http://example.com/story?id=2")
    assert a == b == "https://example.com/story?id=2"
    assert article_id(a) == article_id(b)


def test_relevance():
    assert is_ai_relevant("OpenAI releases new model", "")
    assert is_ai_relevant("The AI bubble question", "")
    assert not is_ai_relevant("Said the mayor at the parade", "Local news about roads")
    assert not is_ai_relevant("New GPUs for gamers", "")  # weak-only term


def test_orgs_and_topics():
    txt = "Anthropic's Claude and OpenAI's ChatGPT face new EU AI Act regulation; regulators and lawmakers weigh a law."
    assert detect_orgs(txt)[:2] == ["Anthropic", "OpenAI"] or set(detect_orgs(txt)) >= {"Anthropic", "OpenAI", "EU"}
    assert "policy & regulation" in detect_topics(txt)


def test_frontmatter_is_flat_scalars():
    a = Article(id="abc", title='He said: "AI"', url="https://x.y/z", source="X", domain="x.y",
                source_type="tech_press", collector="rss", date="2026-10-13T08:00:00Z",
                collected_at="2026-10-13T12:00:00Z", text="body", orgs=["OpenAI"], score=None)
    fm = a.frontmatter()
    assert fm.startswith("---\nid: \"abc\"\n")
    assert 'title: "He said: \\"AI\\""' in fm
    assert "orgs: [\"OpenAI\"]" in fm
    assert "score: null" in fm
    assert "published_date: \"2026-10-13\"" in fm
    assert all(not line.startswith((" ", "-")) or line == "---" for line in fm.splitlines())


def test_safe_filename_and_dates():
    assert "/" not in safe_filename("a/b: c?")
    assert parse_date("Mon, 13 Oct 2026 08:00:00 GMT") == datetime(2026, 10, 13, 8, tzinfo=timezone.utc)
