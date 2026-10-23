---
id: "329f0391307c5f5b"
title: "A Developer’s Guide to OmniParseBench: Leaderboard Benchmarks and OCR Testing"
url: "https://marktechpost.com/2026/10/22/omniparsebench-document-parsing-leaderboard-guide"
link: "https://marktechpost.com/2026/10/22/omniparsebench-document-parsing-leaderboard-guide"
source: "MarkTechPost"
domain: "marktechpost.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T16:11:52Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["Asif Razzaq"]
language: "en"
summary: "In this tutorial, we implement OmniParseBench , Datalab’s open benchmark for document parsers, which grades a parser’s output with 16,288 small pass-or-fail tests across 2,937 pages, from scanned forms and handwriting to arXiv math and dense tables. Rather than trust the leaderboard, we rebuild it from the verdicts Datalab released for 27 parsers, after feeding the scorer a hand-made page to see…"
tags: ["Agentic AI", "AI Infrastructure", "Artificial Intelligence", "Computer Vision", "Editors Pick", "Embedding Model", "For Devs", "Language Model", "OCR", "Staff", "Technology", "Tutorials"]
orgs: ["Hugging Face"]
topics: ["models & research", "products & launches"]
content_source: "summary"
word_count: 5709
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# A Developer’s Guide to OmniParseBench: Leaderboard Benchmarks and OCR Testing

MarkTechPost · Asif Razzaq · 2026-10-22

In this tutorial, we implement OmniParseBench , Datalab’s open benchmark for document parsers, which grades a parser’s output with 16,288 small pass-or-fail tests across 2,937 pages, from scanned forms and handwriting to arXiv math and dense tables. Rather than trust the leaderboard, we rebuild it from the verdicts Datalab released for 27 parsers, after feeding the scorer a hand-made page to see which mistakes flip a verdict. We then measure ranking certainty, slice it by document type, test whether the two models the card names as helping build tests behave differently on tests a model corrected, and run Tesseract and Indra OCR ourselves on a 50-page sample. Along the way, we find that the top two parsers are statistically tied, the leader changes on most slices, and one launch figure doesn’t match the released files. 

 Copy Code Copied Use a different Browser import os
import re
import sys
import json
import time
import html
import shutil
import platform
import traceback
import subprocess
import collections
import urllib.request
from pathlib import Path
 
RESULTS = {} # step -> one-line result, for the summary table
CLAIMS = [] # (step, claim, held)
CURRENT = ["1"]

def banner(title):
 print("\n" + "=" * 78)
 print(title)
 print("=" * 78)

def section(name):
 def wrap(fn):
 def run(*a, **kw):
 CURRENT[0] = name.split(".")[0]
 banner(name)
 t0 = time.time()
 try:
 out = fn(*a, **kw)
 RESULTS[name] = out if isinstance(out, str) else "ok"
 return out
 except Exception as e:
 RESULTS[name] = f"SKIPPED / FAILED -> {type(e).__name__}: {e}"
 print(f"\n[!] {name} did not complete: {type(e).__name__}: {e}")
 traceback.print_exc(limit=3)
 return None
 finally:
 print(f"\n[{time.time() - t0:.1f} s]")
 return run
 return wrap

def claim(text, held):
 CLAIMS.append((CURRENT[0], text, bool(held)))
 return held

banner("1. Install omni-parse-bench 1.0.0rc1 and Tesseract, and pin the dataset revision")
SYSTEM = platform.system()
OPB_VERSION = "1.0.0rc1" # a pre-release: a bare `pip install omni-parse-bench` resolves to 0.2.0, whose API differs
REPO = "datalab-to/omni_parse_bench"
REV = "961c0f89a2da701f5ce53afbd5e80aa469b0369a" # the dataset with the published verdicts of 27 parsers
INDRA = ["indra-ocr==0.3.2", "numpy==2.5.4", "onnxruntime==1.31.0", "opencv-python-headless==5.0.0.93",
 "pypdfium2==5.14.0", "huggingface_hub==2.2.0"] # the pins of the package's own Indra server image
WORK = Path(os.environ.get("OPB_WORK") or ("/content/opb" if os.path.isdir("/content") else "opb_work")).resolve()
WORK.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, "-m", "pip", "install", "-q", f"omni-parse-bench[benchmark]=={OPB_VERSION}", "uv"], check=True)
if SYSTEM == "Linux" and shutil.which("tesseract") is None:
 scripts = ("arab armn beng cans cher cyrl deva ethi frak geor grek gujr guru hang hang-vert hans hans-vert hant "
 "hant-vert hebr jpan jpan-vert knda khmr laoo latn mlym mymr orya sinh syrc taml telu thaa thai tibt viet").split()
 subprocess.run(["apt-get", "-qq", "update"], check=True)
 subprocess.run(["apt-get", "-qq", "install", "-y", "tesseract-ocr", "tesseract-ocr-eng", "tesseract-ocr-osd"]
 + [f"tesseract-ocr-script-{s}" for s in scripts], check=True, stdout=subprocess.DEVNULL)
 
import numpy as np
import pandas as pd
import importlib.metadata as md
from huggingface_hub import snapshot_download
from omni_parse_bench import benchmark, data, harness, markdown, vocab
from omni_parse_bench.scorers import unit_tests
 
print(f"omni-parse-bench {md.version('omni-parse-bench')}, Python {platform.python_version()}, {SYSTEM} {platform.machine()}, "
 f"{os.cpu_count()} CPU cores")
if SYSTEM == "Linux":
 print("os:", open("/etc/os-release").read().split('PRETTY_NAME="')[1].split('"')[0])
tess = subprocess.run(["tesseract", "--version"], capture_output=True, text=True)
print("tesseract:", (tess.stdout or tess.stderr).splitlines()[0])
TESS_MAJOR = int((tess.stdout or tess.stderr).split()[1].split(".")[0])
print("test families:", {f: [t for t, g in vocab.FAMILIES.items() if g == f] for f in dict.fromkeys(vocab.FAMILIES.values())})
print(f"dataset {REPO} @ {REV[:7]}; work folder {WORK}")
RESULTS["1. Install omni-parse-bench 1.0.0rc1 and Tesseract, and pin the dataset revision"] = (
 f"omni-parse-bench {md.version('omni-parse-bench')}, tesseract {(tess.stdout or tess.stderr).split()[1]}, dataset @ {REV[:7]}")

 We install omni-parse-bench pinned to 1.0.0rc1, because a bare pip install still resolves to 0.2.0, an older release with a different API. The benchmark extra brings the parser adapters, the Hugging Face client, and pyarrow for the manifest, and on Colab we add Tesseract with its script models through apt. We also pin the dataset to one commit, since the repository changes as parsers are added. Printing the families shows the structure the benchmark rests on: present, order, and repeat tests form the text family; table_cell forms the tables family; and layout_kind forms the layout family. 

 Copy Code Copied Use a different Browser @section("2. How the scorer decides: one hand-built page, five test types, one change at a time")
def scorer_anatomy():
 T = lambda i, tt, out, tags, args, st=None: {"id": i, "test_type": tt, "output_type": out, "derivation": "authored",
 "tags": tags, "args": args, "settings": st or {}}
 exact = lambda s: {"text": s, "max_diffs": 0}
 gold = [
 T("title", "present", "html", ["heading"], {"content": exact("Quarterly Report")}),
 T("total", "present", "html", ["eng"], {"content": exact("Total due")}),
 T("growth", "present", "html", ["eng"], {"content": {"number": "-4.8%"}}),
 T("amount", "present", "html", ["eng"], {"content": {"number": "1,240.00"}}),
 T("eq_ratio", "present", "html", ["math"], {"content": {"latex": r"\alpha_{1} + \beta"}}),
 T("eq_half", "present", "html", ["math"], {"content": {"latex": r"\frac{1}{2} \to x"}}),
 T("order", "order", "html", ["eng"], {"before": exact("Introduction: this report covers the second quarter."),
 "after": exact("Conclusion: the plan holds.")}),
 T("repeat", "repeat", "html", ["eng"], {"content": exact("Revenue")}, {"expected_count": 2}),
 T("cell_top", "table_cell", "html", ["table"], {"cell": exact("1,240"), "top_heading": exact("2024")}),
 T("cell_left", "table_cell", "html", ["table"], {"cell": exact("1,240"), "left_heading": exact("Income")}),
 T("cell_price", "table_cell", "html", ["table"], {"cell": exact("9.50"), "top_heading": exact("Price"),
 "left": exact("Widget")}),
 T("block_title", "layout_kind", "blocks", ["heading"],
 {"content": dict(exact("Quarterly Report"), place=[[0.10, 0.04, 0.90, 0.09]])}, {"kind": "heading"}),
 T("block_total", "layout_kind", "blocks", ["eng"],
 {"content": dict(exact("Total due"), place=[[0.10, 0.12, 0.90, 0.16]])}, {"kind": "text"}),
 ]
 gold_file = WORK / "fixture" / "gold" / "demo-p1.json" # a gold file is named after its page
 gold_file.parent.mkdir(parents=True, exist_ok=True)
 gold_file.write_text(json.dumps({"tests": gold}, indent=1))
 page = data.Page(page_id="demo-p1", document="demo", suite="demo", doc_path=WORK / "fixture" / "demo-p1.pdf",
 gt_path=gold_file, outputs=("blocks", "html"))
 tests = unit_tests.gold(page)
 
 table_a = ("<table><tr><th></th><th>2023</th><th>2024</th></tr><tr><th>Income</th><td>1,000</td><td>1,240</td></tr>"
 "<tr><th>Costs</th><td>600</td><td>700</td></tr></table>")
 table_b = "<table><tr><th>Product</th><th>Price</th></tr><tr><td>Widget</td><td>9.50</td></tr></table>"
 md_table_b = "| Product | Price |\n|---|---|\n| Widget | 9.50 |"
 parts = {"title": "<h1>Quarterly Report</h1>", "total": "<p>Total due: 1,240.00 USD.</p>",
 "growth": "<p>Growth was -4.8% year on year.</p>", "ratio": r"<p>Ratio: 1+ holds.</p>",
 "half": r"<p>Half: 12x in the model.</p>",
 "intro": "<p>Introduction: this report covers the second quarter.</p>",
 "revenue": "<p>Revenue is shown in thousands. Revenue grew in the second quarter.</p>",
 "table_a": table_a, "conclusion": "<p>Conclusion: the plan holds.</p>", "table_b": table_b}
 blocks = [{"label": "heading", "bbox": [0.10, 0.04, 0.90, 0.09], "text": "Quarterly Report"},
 {"label": "text", "bbox": [0.10, 0.12, 0.90, 0.16], "text": "Total due: 1,240.00 USD."},
 {"label": "table", "bbox": [0.10, 0.40, 0.90, 0.60], "text": "Income 1,000 1,240 Costs 600 700"}]
 
 def pred(change=None, order=None, new_blocks=None):
 p = dict(parts, **(change or {}))
 return {"html": "\n".join(p[k] for k in (order or list(parts))), "blocks": blocks if new_blocks is None else new_blocks}
 
 base = {v.id: v.result for v in unit_tests.score(pred(), tests)}
 print(f"base prediction: {sum(r == 'pass' for r in base.values())} of {len(tests)} tests pass\n")
 swapped = ["title", "total", "growth", "ratio", "half", "conclusion", "intro", "revenue", "table_a", "table_b"]
 variants = [
 ("flip", "a typo: 'Total dve'", pred({"total": "<p>Total dve: 1,240.00 USD.</p>"}), ()),
 ("flip", "the minus sign dropped: 4.8%", pred({"growth": "<p>Growth was 4.8% year on year.</p>"}), ()),
 ("flip", "another symbol: alpha_2", pred({"ratio": r"<p>Ratio: 2+ holds.</p>"}), ()),
 ("flip", "conclusion before introduction", pred(order=swapped), ()),
 ("flip", "'Revenues' for the second 'Revenue'",
 pred({"revenue": "<p>Revenue is shown in thousands. Revenues grew in the second quarter.</p>"}), ()),
 ("flip", "2023 and 2024 headings swapped", pred({"table_a": table_a.replace("<th>2023</th><th>2024</th>",
 "<th>2024</th><th>2023</th>")}), ()),
 ("flip", "row label 'Margin' for 'Income'", pred({"table_a": table_a.replace("<th>Income</th>", "<th>Margin</th>")}), ()),
 ("flip", "a markdown table left in the html", pred({"table_b": md_table_b}), ()),
 ("flip", "the title's block labelled text", pred(new_blocks=[dict(blocks[0], label="text")] + blocks[1:]), ()),
 ("control", r"\dfrac12\rightarrow for \frac{1}{2}\to", pred({"half": r"<p>Half: $\dfrac12\rightarrow x$ in the model.</p>"}), ()),
 ("control", "'TOTAL DUE' and '1240.00'", pred({"total": "<p>TOTAL DUE: 1240.00 USD.</p>"}), ()),
 ("control", "markdown table through markdown.to_html", pred({"table_b": markdown.to_html(md_table_b)}), ()),
 ("unsupported", "no blocks, declared unsupported", {"html": pred()["html"]}, ("blocks",)),
 ]
 as_expected = 0
 for kind, name, p, unsupported in variants:
 changed = [v for v in unit_tests.score(p, tests, unsupported) if v.result != base[v.id]]
 if kind == "flip":
 ok = len(changed) == 1 and changed[0].result == "fail"
 elif kind == "control":
 ok = not changed
 else:
 ok = bool(changed) and all(v.result == "unsupported" for v in changed)
 as_expected += ok
 shown = "; ".join(f"{v.id} -> {v.result}" + (f" ({v.why})" if v.result == "fail" else "") for v in changed) or "no verdict changes"
 print(f"{kind:11s} {name:42s} {shown}")
 s = unit_tests.summarize(unit_tests.lines(unit_tests.score(variants[0][2], tests), tests, page))
 print(f"\nsummary of the typo variant: headline {s['headline']:.4f} = mean of "
 + ", ".join(f"{k} {v['score']:.3f} ({v['tests']} tests)" for k, v in s["families"].items()))
 claim("every one-change variant flips exactly one verdict to fail, and no control flips any", as_expected == len(variants))
 return f"{as_expected} of {len(variants)} hand-built variants behave as expected (9 flips, 3 controls, 1 unsupported)"

scorer_anatomy()

 Before trusting a score, we want to see what a verdict means, so we write a gold file by hand with thirteen tests on an invented page and grade predictions with unit_tests.score, the function the benchmark itself uses. A base prediction passes everything, and each variant changes one thing. A one-letter typo, a lost minus sign, a different symbol in an equation, swapped headings and a mislabelled block each flip exactly one test to fail, with a reason attached. The controls still pass : capitals, a dropped thousands separator and dfrac in place of frac, because text is folded and equations are compared after KaTeX renders them. 

 Copy Code Copied Use a different Browser @section("3. The dataset: 16,288 tests, what they check, and how each answer was established")
def dataset_step():
 global DATA, PAGES, TESTS, CARD_TEXT
 snapshot_download(REPO, repo_type="dataset", revision=REV, local_dir=str(WORK / "dataset"),
 allow_patterns=["manifest.parquet", "gold/*", "results.parquet", "README.md"])
 DATA, PAGES = data.read_manifest(str(WORK / "dataset"))
 rows = []
 for p in PAGES:
 for t in unit_tests.gold(p):
 rows.append(dict(test_id=t.id, page_id=p.page_id, suite=p.suite, document=p.document, test_type=t.test_type,
 derivation=t.derivation, tags=list(t.tags), pdf=p.doc_path.suffix == ".pdf"))
 TESTS = pd.DataFrame(rows)
 tags = collections.Counter(g for ts in TESTS.tags for g in ts)
 langs = {g for g in tags if re.fullmatch(r"[a-z]{3}", g)}
 scripts = {g for g in tags if re.fullmatch(r"[A-Z][a-z]{3}", g)}
 n_pdf = sum(p.doc_path.suffix == ".pdf" for p in PAGES)
 print(f"{len(TESTS):,} tests on {TESTS.page_id.nunique():,} pages from {TESTS.document.nunique():,} documents in "
 f"{TESTS.suite.nunique()} suites; {n_pdf:,} PDF pages and {len(PAGES) - n_pdf:,} images")
 print(f"tags: {len(langs)} language codes ({len(langs - {'und', 'zxx'})} without und and zxx), {len(scripts)} scripts")
 counts = lambda col: {k: int(v) for k, v in col.value_counts().items()}
 print("\ntests by type: ", counts(TESTS.test_type))
 print("tests by family: ", counts(TESTS.test_type.map(vocab.FAMILIES)))
 print("structure and role tags:", {g: n for g, n in tags.most_common() if g not in langs | scripts})
 print("\nhow each test's answer was established (derivation):")
 for d, n in TESTS.derivation.value_counts().items():
 print(f" {d:22s} {n:6,d} {', '.join(f'{k} {v}' for k, v in TESTS[TESTS.derivation == d].test_type.value_counts().items())}")
 CARD_TEXT = (DATA / "README.md").read_text()
 claim("16,288 tests on 2,937 pages from 2,343 documents in 22 suites, as the card says",
 (len(TESTS), TESTS.page_id.nunique(), TESTS.document.nunique(), TESTS.suite.nunique()) == (16288, 2937, 2343, 22))
 return f"{len(TESTS):,} tests, {TESTS.page_id.nunique():,} pages, {TESTS.document.nunique():,} documents, {len(langs - {'und', 'zxx'})} languages"

dataset_step()

 With the scorer understood, we download the manifest, the gold files, and the published verdicts at the pinned revision, skip the 1.5 GB of page images, and read every page’s tests through unit_tests.gold. The counts match the dataset card, including 92 languages once the undetermined and no-language codes are removed. Two fields deserve attention . Tags such as handwriting, rotated, or table never decide a verdict; they only let us slice results. Derivation records how each answer was established, from publisher markup and text layers to model panels and human review, which lets us test later whether test construction favored any parser. 

 Copy Code Copied Use a different Browser COLS = ["page_id", "suite", "document", "test_id", "test_type", "output_type", "derivation", "tags", "result", "why"]
STARRED = ["Gemini 3.8 Flash", "Claude Sonnet 5.5"] # the card: models "used in creating and verifying at least some tests"

@section("4. Recompute the published leaderboard from 439,776 verdicts")
def recompute_table():
 global VERDICTS, TABLE
 VERDICTS = pd.read_parquet(DATA / "results.parquet")
 VERDICTS["output_type"] = VERDICTS.test_type.map(vocab.READS)
 VERDICTS["tags"] = VERDICTS.tags.apply(list)
 VERDICTS["family"] = VERDICTS.test_type.map(vocab.FAMILIES)
 rows = []
 for system, g in VERDICTS.groupby("system", sort=False):
 s = unit_tests.summarize(g[COLS].to_dict("records"))
 fam = {k: (np.nan if v["score"] is None else 100 * v["score"]) for k, v in s["families"].items()}
 scored = g[g.result != "unsupported"]
 rows.append(dict(system=system, headline=np.nan if s["headline"] is None else 100 * s["headline"],
 text=fam.get("text"), tables=fam.get("tables"), layout=fam.get("layout"),
 pooled=100 * (scored.result == "pass").mean()))
 TABLE = pd.DataFrame(rows).set_index("system")
 card = {}
 for line in CARD_TEXT.splitlines():
 cells = [c.strip().strip("*").strip() for c in line.strip().strip("|").split("|")]
 if len(cells) == 6 and cells[1] in ("open", "closed"):
 card[cells[0]] = [None if c in ("none", "unsupported") else float(c) for c in cells[2:]]
 mismatch = []
 for name, vals in card.items():
 mine = [None if pd.isna(x) else round(x, 1) for x in TABLE.loc[name, ["headline", "text", "tables", "layout"]]]
 mismatch += [(name, a, b) for a, b in zip(mine, vals) if a != b]
 print(f"{len(VERDICTS):,} verdicts = {VERDICTS.system.nunique()} parsers x {VERDICTS.test_id.nunique():,} tests: "
 f"{ {k: int(v) for k, v in VERDICTS.result.value_counts().items()} }")
 numeric = sum(v is not None for vals in card.values() for v in vals)
 print(f"the card's table: {len(card)} parsers, {4 * len(card)} entries ({numeric} numbers, the rest none or unsupported); "
 f"recomputed with unit_tests.summarize, {len(mismatch)} differ {mismatch[:3] if mismatch else ''}\n")
 show = TABLE.sort_values("headline", ascending=False, na_position="last")
 f = lambda x: "none" if pd.isna(x) else f"{x:.2f}"
 print(f"{'parser':24s} {'headline':>9s} {'text':>7s} {'tables':>7s} {'layout':>7s} {'pooled':>7s}")
 for name, r in show.iterrows():
 if name in show.index[:8] or pd.isna(r.headline):
 print(f"{name + ('*' if name in STARRED else ''):24s} {f(r.headline):>9s} {f(r.text):>7s} {f(r.tables):>7s} "
 f"{f(r.layout):>7s} {r.pooled:7.2f}")
 a, g = TABLE.loc["Datalab accurate", "headline"], TABLE.loc["Gemini 3.8 Flash", "headline"]
 ranked = TABLE.dropna(subset=["headline"])
 print(f"\nDatalab accurate {a:.3f} vs Gemini 3.8 Flash {g:.3f}: both {a:.1f} at one decimal, {a - g:+.3f} points apart")
 print("top 3 by headline (mean of the three families):", list(ranked.headline.nlargest(3).index))
 print("top 3 by pooled pass rate over every scored test:", list(ranked.pooled.nlargest(3).index))
 claim("every number in the card's results table is reproduced from results.parquet", not mismatch)
 return f"{4 * len(card) - len(mismatch)} of {4 * len(card)} card entries reproduced; Datalab accurate {a:.2f}, Gemini {g:.2f}"

recompute_table()

 Because results.parquet holds one row per parser per test, we can rebuild the leaderboard by passing each parser’s rows to unit_tests.summarize. The headline is the mean of the text, tables and layout pass rates with unsupported tests left out, so a parser that cannot return layout blocks, such as Tesseract, gets no headline at all. All 108 entries in the card’s table match its one-decimal values. The recomputation also exposes a near tie at the top: Datalab accurate and Gemini 3.8 Flash both round to 92.9, 0.024 points apart, and pooling every test instead of averaging families puts Gemini first. 

 Copy Code Copied Use a different Browser def per_document(df, systems, groups):
 """For each system: an array (documents x groups x [passes, scored tests]); `groups` maps a name to a row mask."""
 docs = {d: i for i, d in enumerate(sorted(df.document.unique()))}
 s = df[df.result != "unsupported"]
 out = {}
 for name in systems:
 g = s[s.system == name]
 arr = np.zeros((len(docs), len(groups), 2))
 for k, mask in enumerate(groups.values()):
 sel = g[mask(g)]
 d = sel.document.map(docs).to_numpy()
 arr[:, k, 0] = np.bincount(d, weights=(sel.result == "pass").to_numpy(), minlength=len(docs))
 arr[:, k, 1] = np.bincount(d, minlength=len(docs))
 out[name] = arr
 return out, len(docs)

def resample(n_docs, B, seed):
 """B bootstrap resamples of the documents, each as a count per document."""
 rng = np.random.default_rng(seed)
 return np.stack([np.bincount(rng.integers(0, n_docs, n_docs), minlength=n_docs) for _ in range(B)]).astype(float)

@section("5. How sure is the order at the top? A document-level bootstrap")
def bootstrap_step():
 top = list(TABLE.headline.nlargest(6).index)
 families = {f: (lambda g, f=f: g.family == f) for f in ("text", "tables", "layout")}
 arrs, n_docs = per_document(VERDICTS[VERDICTS.system.isin(top)], top, families)
 W = resample(n_docs, 2000, seed=20261022)
 head = {}
 for s in top:
 tot = np.tensordot(W, arrs[s], axes=([1], [0])) # resamples x families x [passes, tests]
 head[s] = 100 * (tot[..., 0] / tot[..., 1]).mean(axis=1)
 point = {s: 100 * (arrs[s].sum(0)[:, 0] / arrs[s].sum(0)[:, 1]).mean() for s in top}
 print(f"2,000 resamples of {n_docs:,} documents; a document's tests stay together\n")
 print(f"{'parser':22s} {'headline':>9s} {'95% interval':>15s} {'gap to ' + top[0]:>26s} {'resamples where it leads':>24s}")
 leader = np.argmax(np.stack([head[x] for x in top]), axis=0)
 for s in top:
 lo, hi = np.percentile(head[s], [2.5, 97.5])
 d = head[top[0]] - head[s]
 gap = "" if s == top[0] else f"{point[top[0]] - point[s]:+.2f} [{np.percentile(d, 2.5):+.2f}, {np.percentile(d, 97.5):+.2f}]"
 print(f"{s:22s} {point[s]:9.2f} {lo:6.2f} - {hi:6.2f} {gap:>26s} {100 * np.mean(leader == top.index(s)):23.1f}%")
 d = head[top[0]] - head[top[1]]
 lo, hi = np.percentile(d, [2.5, 97.5])
 claim(f"{top[0]} and {top[1]} cannot be told apart (the 95% interval of their gap includes zero)", lo < 0 < hi)
 return f"{top[0]} vs {top[1]}: {point[top[0]] - point[top[1]]:+.2f} points, 95% interval [{lo:+.2f}, {hi:+.2f}]"

bootstrap_step()

 A gap that small raises the question of how much of the order is noise. T ests on one document tend to pass or fail together, so we resample documents rather than tests : each of 2,000 draws picks 2,343 documents with replacement and recomputes every headline from per-document pass counts with one matrix product. The gap between the top two runs ranges from about -0.9 to +0.9 points, and each leads in roughly half the draws, so the honest reading is a tie. Datalab balanced, 1.35 points behind the leader, is clearly separated from it, and so is every parser below. 

 Copy Code Copied Use a different Browser def slice_headline(df):
 """Per system: family pass rates on a slice of tests and their mean, as the benchmark's headline is built."""
 s = df[df.result != "unsupported"]
 fam = s.groupby(["system", "family"]).result.apply(lambda r: 100 * (r == "pass").mean()).unstack()
 return fam.mean(axis=1), fam

@section("6. Slices where a different parser comes first")
def slices_step():
 ranked = TABLE.dropna(subset=["headline"]).sort_values("headline", ascending=False)
 rank = {s: i + 1 for i, s in enumerate(ranked.index)}
 V = VERDICTS[VERDICTS.system.isin(ranked.index)]
 whole, _ = slice_headline(V)
 assert np.allclose(whole[ranked.index], ranked.headline), "slice_headline disagrees with unit_tests.summarize"
 print(f"{'tag':13s} {'tests':>6s} {'docs':>5s} {'first (overall rank)':34s} {'second':26s} families")
 leaders = collections.Counter()
 for tag in ("handwriting", "tiny", "rotated", "degraded", "math", "table", "form", "multi_column",
 "Grek", "Hani", "Cyrl", "Armn", "Laoo"):
 sl = V[V.tags.apply(lambda t: tag in t)]
 head, fam = slice_headline(sl)
 order = head.sort_values(ascending=False)
 (a, x), (b, y) = list(order.items())[:2]
 docs = sl.document.nunique()
 leaders[a] += 1
 note = (" (tie for first)" if x == y else "") + (" (10 or fewer documents)" if docs <= 10 else "")
 print(f"{tag:13s} {sl.test_id.nunique():6d} {docs:5d} {f'{a} {x:.1f} (#{rank[a]})':34s} {f'{b} {y:.1f}':26s} "
 f"{'+'.join(c for c in ('text', 'tables', 'layout') if c in fam.columns)}{note}")
 first = ranked.index[0]
 claim("the overall leader is not first on every slice", leaders[first] < 13)
 return f"{first} is first on {leaders[first]} of 13 slices; {len(leaders) - (first in leaders)} other parsers lead the rest"

slices_step()

 Slicing by tag shows what a single headline hides about the documents we actually have. We r ecompute the headline on handwriting, rotated pages, tables, single scripts , and other slices with the same family-mean rule, after an assertion confirms that the rule reproduces the official headlines on the full set. The overall leader comes first on only three of thirteen slices. Gemini 3.8 Flash leads on handwriting, math, and forms; Claude Sonnet 5.5 on rotated pages; and Mistral OCR on Greek. Armenian and Lao rest on six and five documents, so we treat them as hints rather than rankings. 

 Copy Code Copied Use a different Browser @section("7. Do the two models named on the card hold up better on tests a model corrected? A difference-in-differences check")
def creation_check():
 others = [s for s in TABLE.dropna(subset=["headline"]).index if s not in STARRED]
 V = VERDICTS[VERDICTS.system.isin(STARRED + others)]
 print(f"starred: {STARRED}; compared with the {len(others)} other parsers that have a headline")
 print("DiD = (starred: pass rate on the split - elsewhere) - (others: the same gap); 1,000 document resamples\n")
 print(f"{'tests established by':21s} {'tests':>6s} {'starred in / out':>17s} {'others in / out':>16s} {'DiD [95% interval]':>23s}")
 W = None
 out = {}
 for deriv, note in (("model_review", "a vision model corrected the test"),
 ("model_panel", "independent models agreed"),
 ("human_review", "placebo: a person decided")):
 groups = {"in": lambda g, d=deriv: g.derivation == d, "out": lambda g, d=deriv: g.derivation != d}
 arrs, n_docs = per_document(V, STARRED + others, groups)
 W = resample(n_docs, 1000, seed=7) if W is None else W
 
 def gaps(weights):
 r = {}
 for s, a in arrs.items():
 tot = np.tensordot(weights, a, axes=([-1], [0]))
 with np.errstate(invalid="ignore", divide="ignore"):
 r[s] = 100 * tot[..., 0] / tot[..., 1]
 did = (np.nanmean([r[s][..., 0] - r[s][..., 1] for s in STARRED], axis=0)
 - np.nanmean([r[s][..., 0] - r[s][..., 1] for s in others], axis=0))
 return r, did
 r, d = gaps(np.ones(n_docs))
 _, boot = gaps(W)
 lo, hi = np.nanpercentile(boot, [2.5, 97.5])
 si, so = np.mean([r[s][0] for s in STARRED]), np.mean([r[s][1] for s in STARRED])
 oi, oo = np.mean([r[s][0] for s in others]), np.mean([r[s][1] for s in others])
 out[deriv] = (d, lo, hi)
 print(f"{deriv:21s} {(TESTS.derivation == deriv).sum():6,d} {si:7.1f} / {so:6.1f} {oi:6.1f} / {oo:6.1f} "
 f"{d:+6.1f} [{lo:+5.1f}, {hi:+5.1f}] {note}")
 panel = TESTS[TESTS.derivation == "model_panel"]
 layout = TESTS[TESTS.test_type == "layout_kind"]
 print(f"\nmodel_panel tests are {100 * (panel.test_type == 'layout_kind').mean():.0f}% layout tests, and "
 f"{100 * (layout.derivation == 'model_panel').mean():.0f}% of layout tests are model_panel")
 review = VERDICTS[VERDICTS.derivation == "model_review"]
 rate = lambda s: 100 * (review[review.system == s].result == "pass").mean()
 print(f"pass rate on the {(TESTS.derivation == 'model_review').sum()} model_review tests: "
 + ", ".join(f"{s} {rate(s):.1f}%" for s in STARRED) + f", median of the others {np.median([rate(s) for s in others]):.1f}%")
 claim("the starred models gain more on model_review tests than on the placebo split", out["model_review"][1] > out["human_review"][2])
 claim("the placebo split shows no gap (its interval includes zero)", out["human_review"][1] < 0 < out["human_review"][2])
 return (f"DiD model_review {out['model_review'][0]:+.1f}, model_panel {out['model_panel'][0]:+.1f}, "
 f"placebo human_review {out['human_review'][0]:+.1f} points")

creation_check()

 The dataset card marks Gemini 3.8 Flash and Claude Sonnet 5.5 as used in creating and verifying some tests without saying which, so we ask a narrower question with a difference-in-differences : does a parser’s pass rate on one derivation split, relative to its rate elsewhere, change differently for the starred pair? On the 102 model_review tests, which a vision model corrected, both groups pass far less often than elsewhere, but the starred pair falls about 25 points less. The human_review placebo shows a smaller gap in the same direction and model_panel runs the other way, so we report a flag, not proof. 

 Copy Code Copied Use a different Browser def predict_pages(run, pages, alive=lambda: True):
 """Predict every page the run still lacks. A failed call is recorded, not raised, so we count failures ourselves."""
 t0, n, failed = time.time(), 0, []
 for p in pages:
 if not alive():
 raise RuntimeError(f"{run.provider}: the server stopped after {n} pages")
 if need := benchmark.needs(run, p):
 got = harness.predict(run.provider, p.doc_path, need, timeout=900, **run.options)
 benchmark.record(run, p.page_id, got)
 n += 1
 if any(c.get("failure") for c in got["calls"]):
 failed.append(f"{p.page_id}: {got['errors']}")
 if failed:
 print(f"{len(failed)} of {n} pages failed, e.g. {failed[0][:160]}")
 if 2 * len(failed) >= n:
 raise RuntimeError(f"{run.provider} failed on {len(failed)} of {n} pages")
 return n, (time.time() - t0) / max(n, 1)

@section("8. Run Tesseract ourselves on 50 pages that span all 22 suites")
def tesseract_step():
 global SAMPLE
 if TESS_MAJOR < 5:
 raise RuntimeError(f"tesseract {TESS_MAJOR}.x is installed; this tutorial was verified with tesseract 5")
 SAMPLE = data.select(PAGES, sample=50)
 snapshot_download(REPO, repo_type="dataset", revision=REV, local_dir=str(DATA),
 allow_patterns=sorted(str(p.doc_path.relative_to(DATA)) for p in SAMPLE))
 n_pdf = sum(p.doc_path.suffix == ".pdf" for p in SAMPLE)
 print(f"sample: {len(SAMPLE)} pages from {len({p.suite for p in SAMPLE})} suites, {n_pdf} PDF and {len(SAMPLE) - n_pdf} images, "
 f"{sum(p.doc_path.stat().st_size for p in SAMPLE) / 1e6:.1f} MB, {sum(len(unit_tests.gold(p)) for p in SAMPLE)} tests")
 # The adapter asks Tesseract for '-l script/<Name>'. Homebrew keeps those models in a script/ folder; Ubuntu installs
 # them flat, so on Linux we point Tesseract at a folder of symlinks with the layout it expects.
 listing = subprocess.run(["tesseract", "--list-langs"], capture_output=True, text=True)
 listing = listing.stdout + listing.stderr
 if "script/Latin" not in listing:
 src = Path(re.search(r'"(.+?)"', listing).group(1))
 dst = WORK / "tessdata"
 (dst / "script").mkdir(parents=True, exist_ok=True)
 for f in src.glob("*.traineddata"):
 for link in [dst / f.name] + ([dst / "script" / f.name] if f.name[0].isupper() else []):
 if not link.exists():
 link.symlink_to(f)
 os.environ["TESSDATA_PREFIX"] = str(dst)
 print(f"script models linked under {dst}")
 run = benchmark.Run("tesseract", {}, WORK / "runs" / "tesseract")
 benchmark.prepare(run, str(DATA), 900)
 n, per_page = predict_pages(run, SAMPLE)
 s = benchmark.grade(run, SAMPLE, say=lambda *_: None)
 fam = s["families"]
 print(f"\nTesseract: {n} pages read, {per_page:.1f} s per page")
 for k, v in fam.items():
 print(f" {k:7s} " + ("unsupported (no blocks output)" if v["score"] is None else f"{100 * v['score']:5.1f}% of {v['tests']} tests"))
 print(f" headline {'none' if s['headline'] is None else round(100 * s['headline'], 1)} (a family it cannot produce leaves no headline)")
 return f"Tesseract on 50 pages: text {100 * fam['text']['score']:.1f}%, tables {100 * fam['tables']['score']:.1f}%, {per_page:.1f} s/page"

tesseract_step()

 Rebuilding a leaderboard from published verdicts is one thing; producing verdicts ourselves is another. data.select picks a fixed 50-page sample spread over all 22 suites, and we download only those pages. The loop is the benchmark’s own: needs lists the outputs a page still lacks, harness. predict runs the parser; record saves the prediction and grades the folder, so an interrupted run can resume. On Ubuntu we also link Tesseract’s script models into the layout the adapter expects. Tesseract passes 30.4% of the sample’s text tests against 17.6% on the full set, a gap that depends on which pages were sampled. 

 Copy Code Copied Use a different Browser def agreement(folder, published):
 """Our verdicts against the published ones for the same tests, where both scored the test."""
 ours = pd.read_json(folder / "scores.jsonl", lines=True)[["test_id", "result", "why"]]
 pub = VERDICTS[VERDICTS.system == published][["test_id", "result"]]
 m = ours.merge(pub, on="test_id", suffixes=("_ours", "_pub"))
 m = m[(m.result_ours != "unsupported") & (m.result_pub != "unsupported")]
 return m, int((m.result_ours == m.result_pub).sum()), len(m)

@section("9. Indra OCR on the same pages, served on the CPU from the package's own server code")
def indra_step():
 if sys.version_info < (3, 12):
 raise RuntimeError("the Indra pins (numpy 2.5.4) need Python 3.12 or newer")
 venv = WORK / "indra-venv"
 py = venv / "bin" / "python"
 if not py.exists():
 uv = shutil.which("uv") or str(Path(sys.executable).parent / "uv")
 subprocess.run([uv, "venv", "-q", "--python", sys.executable, str(venv)], check=True)
 subprocess.run([uv, "pip", "install", "-q", "--python", str(py)] + INDRA, check=True)
 server = Path(harness.__file__).parent / "providers" / "oss" / "indra" / "server.py"
 # server.py counts cores with os.sched_getaffinity, which macOS lacks; on Linux the shim changes nothing
 launcher = WORK / "indra_launch.py"
 launcher.write_text("import os, runpy, sys\n"
 "if not hasattr(os, 'sched_getaffinity'):\n"
 " os.sched_getaffinity = lambda pid: set(range(os.cpu_count()))\n"
 "sys.argv = ['server.py', '--port', '8001', '--workers', '2']\n"
 f"runpy.run_path({str(server)!r}, run_name='__main__')\n")
 log = open(WORK / "indra_server.log", "w")
 proc = subprocess.Popen([str(py), str(launcher)], stdout=log, stderr=subprocess.STDOUT)
 t0 = time.time()
 while True:
 try:
 urllib.request.urlopen("http://127.0.0.1:8001/health", timeout=2)
 break
 except Exception:
 if proc.poll() is not None or time.time() - t0 > 600:
 proc.terminate()
 raise RuntimeError("the Indra server did not start; see " + log.name)
 time.sleep(2)
 print(f"server up in {time.time() - t0:.0f} s: {INDRA[0]}, 2 worker processes")
 try:
 run = benchmark.Run("indra-ocr", {"base_url": "http://127.0.0.1:8001"}, WORK / "runs" / "indra-ocr")
 benchmark.prepare(run, str(DATA), 900)
 n, per_page = predict_pages(run, SAMPLE, alive=lambda: proc.poll() is None)
 s = benchmark.grade(run, SAMPLE, say=lambda *_: None)
 finally:
 proc.terminate()
 fam = {k: 100 * v["score"] for k, v in s["families"].items()}
 print(f"Indra OCR: {n} pages, {per_page:.2f} s per page; text {fam['text']:.1f}%, tables {fam['tables']:.1f}%, "
 f"layout {fam['layout']:.1f}%; headline on these pages {100 * s['headline']:.1f}\n")
 ids = {p.page_id for p in SAMPLE}
 fmt = lambda x: "none" if x is None else f"{100 * x:.1f}"
 print(f"{'on the 50 pages':22s} {'headline':>9s} {'text':>6s} {'tables':>7s} {'layout':>7s}")
 for name, folder in (("Tesseract", WORK / "runs" / "tesseract"), ("Indra OCR", WORK / "runs" / "indra-ocr")):
 pub = unit_tests.summarize(VERDICTS[(VERDICTS.system == name) & VERDICTS.page_id.isin(ids)][COLS].to_dict("records"))
 ours = unit_tests.summarize(benchmark.read_scores(benchmark.Run(name, {}, folder)))
 for who, x in (("ours", ours), ("published", pub)):
 f = x["families"]
 print(f"{name + ', ' + who:22s} {fmt(x['headline']):>9s} " + " ".join(f"{fmt(f[k]['score']) if k in f else 'none':>6s}"
 for k in ("text", "tables", "layout")))
 print()
 for name, folder in (("Tesseract", WORK / "runs" / "tesseract"), ("Indra OCR", WORK / "runs" / "indra-ocr")):
 m, same, total = agreement(folder, name)
 diff = m[m.result_ours != m.result_pub]
 print(f"{name:10s} our verdicts equal the published ones on {same} of {total} tests ({100 * same / total:.1f}%); "
 f"of the {len(diff)} that differ, {(diff.result_ours == 'pass').sum()} pass only for us and "
 f"{(diff.result_ours == 'fail').sum()} only in the published run")
 if len(diff):
 by_page = diff.test_id.map(TESTS.set_index("test_id").page_id).value_counts()
 print(" differing tests by type:", {k: int(v) for k, v in diff.test_id.map(TESTS.set_index("test_id").test_type).value_counts().items()},
 f"| on {len(by_page)} pages, {by_page.iloc[0]} of them on {by_page.index[0]}")
 claim(f"{name}: our verdicts equal the published ones on at least 95% of the sample's tests", same >= 0.95 * total)
 return f"Indra OCR on 50 pages: headline {100 * s['headline']:.1f} (text {fam['text']:.1f}, tables {fam['tables']:.1f}, layout {fam['layout']:.1f}), {per_page:.2f} s/page"

indra_step()

 Indra OCR is an open CPU model, and the package ships the HTTP server its adapter talks to, so we install the versions pinned in that server’s Dockerfile into a separate environment and start it in the background. Against the published verdicts on the same pages, Tesseract agrees on every scored test, so its sample score matches the published one. Indra agrees on 203 of 221, and all of its table differences sit on one page, which accounts for the whole gap between its published tables score of 36.1 and our 69.4. One page moving a family that far is the clearest argument for resampling documents. 

 Copy Code Copied Use a different Browser @section("10. Bring your own parser: grade a PDF text-layer baseline with the same code")
def byo_step():
 import pypdfium2 as pdfium
 
 def text_layer(path):
 if path.suffix.lower() != ".pdf":
 return "" # an image has no text layer to read
 doc = pdfium.PdfDocument(str(path))
 try:
 return "<pre>" + html.escape(doc[0].get_textpage().get_text_range()) + "</pre>"
 finally:
 doc.close()
 
 out = WORK / "runs" / "text-layer"
 (out / "predictions").mkdir(parents=True, exist_ok=True)
 for p in SAMPLE:
 (out / "predictions" / f"{p.page_id}.json").write_text(json.dumps({"html": text_layer(p.doc_path)}))
 s = benchmark.grade(benchmark.Run("text-layer", {}, out), SAMPLE, say=lambda *_: None, settings={"unsupported": ["blocks"]})
 kind = {p.page_id: "PDF" if p.doc_path.suffix == ".pdf" else "image" for p in SAMPLE}
 print(f"{'parser on the same 50 pages':28s} {'text: PDF':>10s} {'images':>8s} {'all':>6s} {'tables':>8s}")
 for name in ("text-layer", "tesseract", "indra-ocr"):
 sc = pd.read_json(WORK / "runs" / name / "scores.jsonl", lines=True)
 sc = sc[sc.result.isin(["pass", "fail"])]
 txt = sc[sc.test_type.map(vocab.FAMILIES) == "text"]
 by = txt.groupby(txt.page_id.map(kind)).result.apply(lambda r: 100 * (r == "pass").mean())
 tab = sc[sc.test_type == "table_cell"]
 print(f"{name:28s} {by.get('PDF', np.nan):10.1f} {by.get('image', np.nan):8.1f} "
 f"{100 * (txt.result == 'pass').mean():6.1f} {100 * (tab.result == 'pass').mean():8.1f}")
 fam = s["families"]
 return f"text layer, no OCR: text {100 * fam['text']['score']:.1f}%, tables {100 * fam['tables']['score']:.1f}% on the 50 pages"

byo_step()

 Any parser can be graded without an adapter: we write one predictions file per page and call benchmark.grade, declaring the outputs we cannot produce as unsupported. Our parser reads a PDF’s embedded text layer with pypdfium2 and returns an empty string for images, which have none. On PDF pages it passes exactly as many text tests as Tesseract, 42.3% each, without any OCR, while on images it has nothing and Indra OCR still passes 43.1%. Plain text fails every table test, since a pass needs cell structure, so the mix of PDFs and images matters whenever two parsers are compared. 

 Copy Code Copied Use a different Browser @section("11. The launch claims, checked against the files")
def claims_step():
 a, t = TABLE.loc["Datalab accurate"], TABLE.loc["Tesseract"]
 g = TABLE.loc["Gemini 3.8 Flash", "headline"]
 c = TABLE.loc["Claude Sonnet 5.5"]
 tags = TESTS.tags
 langs = {x for ts in tags for x in ts if re.fullmatch("[a-z]{3}", x)} - {"und", "zxx"}
 pkg = Path(vocab.__file__).parent # the scorer and the modules it reads; data.py and the harness only fetch and run
 scoring = sorted(pkg.glob("scorers/**/*.py")) + [pkg / f"{m}.py" for m in ("normalize", "tables", "equations", "views", "vocab", "markdown")]
 clients = [f.name for f in scoring if re.search(r"^\s*(import|from)\s+(httpx|requests|urllib|huggingface_hub|openai|anthropic|google"
 r"|transformers|torch|omni_parse_bench\.harness)\b", f.read_text(), re.M)]
 n_eng, n_table = tags.apply(lambda x: "eng" in x).sum(), tags.apply(lambda x: "table" in x).sum()
 rows = [
 ("16,288 tests, 2,937 pages, 2,343 documents", f"{len(TESTS):,} / {TESTS.page_id.nunique():,} / {TESTS.document.nunique():,}",
 (len(TESTS), TESTS.page_id.nunique(), TESTS.document.nunique()) == (16288, 2937, 2343)),
 ("92 languages", f"{len(langs)} codes besides und and zxx", len(langs) == 92),
 ("10,089 English tests, 6,767 table tests", f"{n_eng:,} and {n_table:,}", (n_eng, n_table) == (10089, 6767)),
 ("Datalab accurate scores 92.7", f"{a.headline:.2f} in results.parquet", round(a.headline, 1) == 92.7),
 ("Datalab accurate ranks second, behind Gemini", f"{a.headline:.3f} vs {g:.3f}", a.headline < g),
 ("Claude Sonnet 5.5: text 93.1, tables 95.4, layout 77.5", f"{c.text:.1f} / {c.tables:.1f} / {c.layout:.1f}",
 [round(c[k], 1) for k in ("text", "tables", "layout")] == [93.1, 95.4, 77.5]),
 ("Tesseract: no headline, text 17.6, tables 0.0",
 f"{'none' if pd.isna(t.headline) else round(t.headline, 1)} / {t.text:.1f} / {t.tables:.1f}",
 pd.isna(t.headline) and round(t.text, 1) == 17.6 and round(t.tables, 1) == 0.0),
 ("no model judges the outputs", f"{len(clients)} of {len(scoring)} scorer modules import a model or HTTP client", not clients),
 ]
 print(f"{'claim (launch article and blog)':56s} {'what the files say':38s} verdict")
 for text, found, ok in rows:
 print(f"{text:56s} {found:38s} {'holds' if ok else 'does not hold'}")
 claim(text, ok)
 print("\nnot checkable from these files: latency, price per 1,000 pages, the other benchmarks' test counts")
 return f"{sum(bool(ok) for *_, ok in rows)} of {len(rows)} launch claims hold against the files"

claims_step()

 Instead of repeating the launch claims, we check each one against the files. The counts hold exactly, from tests and pages to languages and subsets, and the Claude and Tesseract rows match. Datalab ‘s own row does not: the launch article and blog give Datalab an accurate 92.7 and place it second behind Gemini, while the released verdicts give 92.92 against 92.89, a tie that rounds to the same figure. The no-judge claim holds for the scorer itself, whose modules import no model or HTTP client; KaTeX runs in an embedded JavaScript engine to compare equations. Latency and price cannot be checked from these files. 

 Copy Code Copied Use a different Browser banner("SUMMARY")
for name, res in RESULTS.items():
 print(f" {name:<100s} {res}")
print("\nchecks decided in this run:")
for step, text, held in CLAIMS:
 print(f" [{'held' if held else 'did not hold'}] step {step}: {text}")
failed = [k for k, v in RESULTS.items() if str(v).startswith("SKIPPED")]
print(f"\n{sum(h for *_, h in CLAIMS)} of {len(CLAIMS)} checks held; steps failed or skipped: {failed or 'none'}")
print(f"omni-parse-bench {md.version('omni-parse-bench')}, dataset @ {REV[:7]}, Python {platform.python_version()}, {SYSTEM}")
print("not run here: the hosted parsers (paid API keys), the GPU models, latency and cost, all 2,937 pages")

 The summary prints each step’s one-line result and every check the run decided, marking which held and which did not: 13 of 17 held, and the four that did not are findings rather than failures, namely the placebo gap, Indra’s reproduction and Datalab’s two launch figures. It also lists what we did not run here: the hosted parsers that need paid keys, the GPU models, latency and cost, and the full set of 2,937 pages. 

 In conclusion, OmniParseBench is a benchmark we can audit end to end: the scorer is open code that calls no model, the verdicts are released, and every entry on the card can be rebuilt from them. The top two parsers are statistically tied, pooling tests instead of families changes the order, and a different parser comes first on handwriting, rotated pages, tables and several scripts. The two models named on the card fall less far than the others on tests a model corrected, which we report as a flag rather than proof. Tesseract’s published verdicts reproduced exactly on our sample, while Indra OCR’s agreed on 92% of tests. The practical lesson is to slice the benchmark to our own documents, report intervals, and pin every version. 

 Check out the Notebook and Repo . All credit goes to the researcher of this project. Also, feel free to follow us on  Twitter  and don’t forget to join our  150k+ML SubReddit  and Subscribe to  our Newsletter . Wait! are you on telegram?  now you can join us on telegram as well. 

 Need to partner with us for promoting your GitHub Repo OR Hugging Face Page OR Product Release OR Webinar etc.?  Connect with us 
 The post A Developer’s Guide to OmniParseBench: Leaderboard Benchmarks and OCR Testing appeared first on MarkTechPost .
