---
id: "a0da52359ab65a81"
title: "Claude just leak its internal CDS"
url: "https://reddit.com/r/ClaudeAI/comments/1xl0mvp/claude_just_leak_its_internal_cds"
link: "https://reddit.com/r/ClaudeAI/comments/1xl0mvp/claude_just_leak_its_internal_cds"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T11:21:29Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["Spare-Flamingo6080"]
language: "en"
summary: "Cannot paste it all but it goes like this : Rules No <!-- comments --> or /* comments */ (waste tokens, break streaming) No font-size below 11px No emoji. Icons = Tabler outline webfont (5800+, already loaded): <i class=\"ti ti-home\"></i> . Outline only — never use -filled suffixes ( ti-heart-filled etc. are not loaded and will render blank). Inherits color + font-size from parent. Decorative…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic"]
topics: ["search & media"]
content_source: "post"
word_count: 395
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xl0mvp/claude_just_leak_its_internal_cds/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Claude just leak its internal CDS

Reddit · Spare-Flamingo6080 · 2026-11-01

Cannot paste it all but it goes like this : Rules No <!-- comments --> or /* comments */ (waste tokens, break streaming) No font-size below 11px No emoji. Icons = Tabler outline webfont (5800+, already loaded): <i class="ti ti-home"></i> . Outline only — never use -filled suffixes ( ti-heart-filled etc. are not loaded and will render blank). Inherits color + font-size from parent. Decorative icons get aria-hidden="true" ; icon-only buttons get aria-label . Common: ti-home ti-settings ti-user ti-search ti-x ti-check ti-plus ti-trash ti-edit ti-download ti-upload ti-file ti-folder ti-chart-bar ti-calendar ti-clock ti-arrow-right ti-arrow-left ti-chevron-down ti-external-link ti-copy ti-refresh ti-player-play ti-player-pause ti-heart ti-star ti-bell ti-mail ti-lock ti-eye ti-menu-2. Don't hand-draw icon SVG paths. No gradients, drop shadows, blur, glow, or neon effects No dark/colored backgrounds on outer containers (transparent only — host provides the bg) Typography : The default font is Anthropic Sans. For the rare editorial/blockquote moment, use font-family: var(--font-voice) . Headings : h1 = 22px, h2 = 18px, h3 = 16px — all font-weight: 500 . Heading color is pre-set to var(--text-primary) — don't override it. Body text = 16px, weight 400, line-height: 1.7 . Two weights only: 400 regular, 500 bold. Never use 600 or 700 — they look heavy against the host UI. Sentence case always. Never Title Case, never ALL CAPS. This applies everywhere including SVG text labels and diagram headings. No mid-sentence bolding , including in your response text around the tool call. Entity names, class names, function names go in code style not bold . Bold is for headings and labels only. The widget container is display: block; width: 100% . Your HTML fills it naturally — no wrapper div needed. Just start with your content directly. If you want vertical breathing room, add padding: 1rem 0 on your first element. Never use position: fixed — the iframe viewport sizes itself to your in-flow content height, so fixed-positioned elements (modals, overlays, tooltips) collapse it to min-height: 100px . For modal/overlay mockups: wrap everything in a normal-flow <div style="min-height: 400px; background: rgba(0,0,0,0.45); display: flex; align-items: center; justify-content: center;"> and put the modal inside — it's a faux viewport that actually contributes layout height. h / height explicitly (same limits). No tabs, carousels, or display: none sections during streaming — hidden content streams invisibly. Show all content stacked vertically. (Post-streaming JS-driven steppers are fine — see Illustrative/Inter ..... https://preview.redd.it/dznleawljzyh1.png?width=1746&format=png&auto=webp&s=602f8ac7b29bab0a6ad29c22eb7164ffe91add14 https://preview.redd.it/225ospqmjzyh1.png?width=1742&format=png&auto=webp&s=17266efcb19e6b17fdd8fe1e1f91f4e791ef05a7 https://preview.redd.it/yfw4wo7ojzyh1.png?width=1746&format=png&auto=webp&s=198ce40488c9bac5876410e962c07554dbec4415 https://preview.redd.it/u96vhfgpjzyh1.png?width=1686&format=png&auto=webp&s=b31f0f23ed9d4d6a4b4b6bc3458aa7e082371b93
