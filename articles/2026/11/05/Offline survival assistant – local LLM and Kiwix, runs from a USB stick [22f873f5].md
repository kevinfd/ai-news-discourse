---
id: "22f873f5ee58609f"
title: "Offline survival assistant – local LLM and Kiwix, runs from a USB stick"
url: "https://github.com/sdalberto/ia-da-sobrevivencia/blob/main/README.en.md"
link: "https://github.com/sdalberto/ia-da-sobrevivencia/blob/main/README.en.md"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-05T15:25:36Z"
published_date: "2026-11-05"
collected_at: "2026-11-06T13:04:08Z"
authors: ["soloyo"]
language: "en"
summary: "A survival assistant that works 100% without internet — on Windows, Linux and macOS.\n🇧🇷 Português · 🇺🇸 English · 🇪🇸 Español\nIf the internet, power and services go down, this kit keeps working on a laptop or USB drive:\n- 📚 Practical guides with cited sources (EN, PT, ES): water, fire, shelter, food, gardening and livestock, foraging/fishing/hunting, first aid and medicine, hygiene and homemade…"
tags: []
orgs: ["OpenAI", "Apple", "Alibaba"]
topics: ["models & research", "search & media", "health & science"]
content_source: "fulltext"
word_count: 636
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50380273"
score: 28
comments: 16
community: "Hacker News"
---

# Offline survival assistant – local LLM and Kiwix, runs from a USB stick

GitHub · soloyo · 2026-11-05

A survival assistant that works 100% without internet — on Windows, Linux and macOS.
🇧🇷 Português · 🇺🇸 English · 🇪🇸 Español
If the internet, power and services go down, this kit keeps working on a laptop or USB drive:
- 📚 Practical guides with cited sources (EN, PT, ES): water, fire, shelter, food, gardening and livestock, foraging/fishing/hunting, first aid and medicine, hygiene and homemade soap, alcohol (fermentation, distillation, antiseptic and fuel), solar power, radio and navigation, tools and knots, mental health and community, and checklists for 72 hours and 1 year.
- 🤖 Local AI that answers any question in natural language, citing its sources — it runs on your own computer (llama.cpp or Ollama); nothing goes to the internet.
- 🌐 Kiwix offline libraries: medical Wikipedia, post-disaster manuals, Where There Is No Doctor, wikiHow, iFixit and more — the AI searches them too.
- 📱 Web interface in your browser, shareable over the local network (other phones connect via Wi-Fi, even with no internet).
- 🔍 No-AI mode: even without a model, guide search works on any PC with Python.
⚠️ Disclaimer: educational content. It does not replace doctors, firefighters or emergency services. Health guidance follows public guidelines (WHO, Red Cross/IFRC, AHA, CDC, Hesperian…) cited in each section.
 Question ──► search kit guides (BM25) ──────┐
          └─► search Kiwix (.zim files) ──────┼─► local language model ──► answer with [1] [2] sources
                                              └─► (no model? shows the most relevant passages)
Large files are not committed to git (see .gitignore): the repository stays small and everyone builds their own kit with the preparer.
git clone https://github.com/sdalberto/ia-da-sobrevivencia.git
cd ia-da-sobrevivencia
The preparer asks for:
- AI model: leve (light, 1 GB, 4 GB RAM), padrao (default, 2 GB, 8 GB RAM — recommended), forte (strong, 4.7 GB, 16 GB RAM).
- Kiwix libraries: minimo (~3–5 GB), recomendado (~25–40 GB) or completo (100+ GB, full Wikipedia).
- Systems: this computer only, or Windows + Linux + macOS (universal USB kit).
- Portable Python: so the kit opens on computers without Python.
Non-interactive:
python sobrevivencia.py --lang en prepare --model padrao --zims recomendado --os all --python
Your browser opens http://127.0.0.1:8090. Switch language anytime with the PT/EN/ES buttons. To make English the default, create config/settings.local.json with { "language": "en" }.
Copy the whole folder to a USB drive or external disk formatted as exFAT (works on all three systems and supports files over 4 GB).
python sobrevivencia.py --lang en chat                   # terminal chat
python sobrevivencia.py --lang en ask "how do I make oral rehydration solution?"
python sobrevivencia.py --lang en search burn
python sobrevivencia.py status
python sobrevivencia.py start --host 0.0.0.0             # share on the local network
python sobrevivencia.py prepare --search survival        # find more Kiwix libraries
Ollama: if you use Ollama, run ollama pull qwen2.5:3b — it is detected automatically. Any local OpenAI-compatible server (LM Studio, llamafile, KoboldCpp, Jan) also works: set llm_url.
Kiwix Desktop: Kiwix Desktop can open the .zim files in zim/. To let the AI use its Local Kiwix Server, set { "kiwix_url": "http://127.0.0.1:<port>" } in config/settings.local.json. The Windows Kiwix Desktop package (~150 MB) exceeds GitHub's 100 MB per-file limit — publish it as a Release asset instead of committing it.
Drop .md or .txt files in knowledge/extra/ (family recipes, local maps, contacts, equipment manuals). They are indexed and cited by the AI.
- Minimum (search only): any PC with Python 3.8+.
- With AI: 4 GB RAM (light model), 8 GB recommended; x86-64 CPU with AVX2 or Apple Silicon/ARM64. No GPU needed.
- Disk: 3 GB (minimal kit) to 100+ GB (full kit).
python -m unittest discover -s tests
Code: MIT. Guides in knowledge/: CC BY-SA 4.0. Models, Kiwix, llama.cpp and ZIM files downloaded by the preparer have their own licenses. The default model (Qwen2.5 3B) uses the Qwen Research License; for commercial use choose leve or forte (Apache 2.0).
