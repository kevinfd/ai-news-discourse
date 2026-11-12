---
id: "c3e3902cde69e8a2"
title: "I built a free MCP connector with Claude so it draws organic chemistry correctly: ~10× fewer output characters, 0 drawing errors in a blind test"
url: "https://reddit.com/r/ClaudeAI/comments/1xtt75f/i_built_a_free_mcp_connector_with_claude_so_it"
link: "https://reddit.com/r/ClaudeAI/comments/1xtt75f/i_built_a_free_mcp_connector_with_claude_so_it"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-11T20:47:39Z"
published_date: "2026-11-11"
collected_at: "2026-11-12T13:04:19Z"
authors: ["sodiumbromo"]
language: "en"
summary: "I built ChemView, a free MCP connector that lets Claude draw organic chemistry correctly. I built it with Claude (mostly Opus 5.5 in the Claude app), and it's made for Claude, though it also works in ChatGPT, Claude Code and Codex. The problem: ask Claude to draw the Favorskii rearrangement and you get floating atoms, a cyclopropanone with no C=O and a product with no ester (left of the video).…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI"]
topics: ["models & research", "agents & coding", "products & launches"]
content_source: "post"
word_count: 479
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xtt75f/i_built_a_free_mcp_connector_with_claude_so_it/"
score: null
comments: null
community: "r/ClaudeAI"
---

# I built a free MCP connector with Claude so it draws organic chemistry correctly: ~10× fewer output characters, 0 drawing errors in a blind test

Reddit · sodiumbromo · 2026-11-11

I built ChemView, a free MCP connector that lets Claude draw organic chemistry correctly. I built it with Claude (mostly Opus 5.5 in the Claude app), and it's made for Claude, though it also works in ChatGPT, Claude Code and Codex. The problem: ask Claude to draw the Favorskii rearrangement and you get floating atoms, a cyclopropanone with no C=O and a product with no ester (left of the video). Same request with ChemView on the right. What it does: the model only writes the molecule as SMILES; ChemView draws it, with curly arrows, lone pairs, and chairs, Newman, Fischer, Haworth and bridged cages computed from the molecule's stereo, so the picture can't contradict the structure. How I built it with Claude Design: Claude and I picked a remote MCP connector over a skill, so the model sends a short SMILES call instead of hundreds of lines of SVG. Server: Claude wrote it as one JavaScript file on Cloudflare Workers. Drawing happens in your browser with RDKit, shown inline in Claude as an MCP App. Fixable errors: bad SMILES used to fail silently in the viewer, so we added server-side checks (rings, valence, atom numbers) that return an error the model can fix and retry. Getting Claude to use it: in v1 Claude answered in text and asked whether to draw. We rewrote the tool instructions so it draws first, without making them token-heavy. Testing: Claude ran the blind test below with fresh agents and graded it with RDKit, including 3D checks for endo/exo. The test 5 hard figures, 20 fresh agents with no memory. Sonnet and Opus each drew every figure by hand-writing SVG and again through ChemView. Hand SVG ChemView Sonnet: characters written 26,213 Opus: characters written 32,776 Sonnet: median time per figure 144 s Opus: median time per figure 186 s Fewer output characters means less of your usage limit per figure. Figure Sonnet SVG Sonnet + CV Opus SVG Opus + CV Cholesterol, 8 stereocentres ✅ ✅ ✅ ✅ β-D-glucose, Haworth + chair ❌ ✅ ❌ ✅ E2 Newman, meso-stilbene dibromide ✅ ⚠️ ✅ ✅ Endo Diels–Alder, 3D cage ❌ ⚠️ 🟡 ✅ Pinacol mechanism ✅ ✅ ✅ ✅ Drawing errors 2 0 2 0 🟡 partly right · ⚠️ model slip: drawing matched the SMILES, but the model chose the wrong isomer ChemView rendered all 10 figures faithfully to what the model asked for. Full results, including where ChemView lost, are linked in the comments. Try it (free) No account, no API key. In Claude: Settings → Connectors → Add custom connector → paste the connector URL from the first comment, no authentication. Steps for ChatGPT, Claude Code and Codex are on the setup page linked there. ChemView doesn't save your molecules or chats. If you try it, post what it drew, good or bad. Mechanisms it gets wrong are the most useful feedback.
