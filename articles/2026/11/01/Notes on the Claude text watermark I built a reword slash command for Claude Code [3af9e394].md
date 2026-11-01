---
id: "3af9e394f9e5b26d"
title: "Notes on the Claude text watermark: I built a /reword slash command for Claude Code"
url: "https://reddit.com/r/ClaudeAI/comments/1xl023x/notes_on_the_claude_text_watermark_i_built_a"
link: "https://reddit.com/r/ClaudeAI/comments/1xl023x/notes_on_the_claude_text_watermark_i_built_a"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-11-01T10:47:21Z"
published_date: "2026-11-01"
collected_at: "2026-11-01T13:04:00Z"
authors: ["trigodil"]
language: "en"
summary: "The inspiration behind this is, as many of you know, the recent watermarking of Claude that Anthropic put in place, so what they did is give me a very interesting problem to work around and the weekend is the time to test what shinanigans I can come up with, ofc there are other methods like proxy routing but I find this to be the simplest - this is what I came up with What it is /reword is a…"
tags: ["r/ClaudeAI"]
orgs: ["Anthropic", "OpenAI", "DeepSeek"]
topics: ["models & research"]
content_source: "post"
word_count: 526
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xl023x/notes_on_the_claude_text_watermark_i_built_a/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Notes on the Claude text watermark: I built a /reword slash command for Claude Code

Reddit · trigodil · 2026-11-01

The inspiration behind this is, as many of you know, the recent watermarking of Claude that Anthropic put in place, so what they did is give me a very interesting problem to work around and the weekend is the time to test what shinanigans I can come up with, ofc there are other methods like proxy routing but I find this to be the simplest - this is what I came up with What it is /reword is a slash command for Claude Code plus a small Python tool behind it. You ask Claude to write something, like a paragraph, notes, a .docx or a .tex section. Instead of showing you its own draft, Claude sends the draft to another LLM API (OpenAI, DeepSeek or Anthropic) to be reworded, and hands you that version, either in chat or straight into a file. /reword one paragraph on jets /reword summary in report.docx /reword intro section in paper.tex What it does Works with plain text, Markdown, LaTeX and Word (.docx) For an existing .docx , it rewords the paragraph text in place and keeps your styles, tables, images and layout For new content, it builds a fresh .docx Safety checks: if the reworded text changes any numbers, URLs, LaTeX is thrown away and the original is kept You pick the provider or model in the request (e.g. "with deepseek-reason Reword mode stays on for the session until you say "stop" Python standard library only, nothing to pip install It is Open source MIT licensed Claude contribution Yes, Claude Code wrote all of it actually, felt that it is better to leave it to Claude because Claude knows Claude best. I had the idea and steered it, and Claude Wrote the Python tool, including the .docx handling (it edits the Word rvives) and the LaTeX/number/URL checks Wrote the /reword slash command definition and the rewrite prompt Packaged it into a repo with an install script and an empty API-key templ Debugged a bug where an old OPENAI_API_KEY in my shell was silently overriding the valid key in my config file (it kept getting 401s). It worked out the cause and fixed it so the config file wins Wrote the CLAUDE.md so you can clone the repo, open Claude Code in it, Setup The repo's CLAUDE.md is written as setup instructions for Claude. Clone it and ask it to set the tool up. It runs the installer and tests that it works. You add your own API key to ~/.claude/hooks/reword.env yourself. Chat file, and the repo only contains an empty template. Caveats It needs your own API key for at least one provider, and every reword is a paid API call. Mixed formatting inside a single Word paragraph (like one bold word) takes the style of the first run. Headers, footers and footnotes in .docx files are left alone. Fairly new and lightly tested, so expect rough edges. Why I made it It just feels inconvenient, I don't usually use AI in my code or research, at all, but the engineering was interesting enough to solve it for fun because it's a weekend. Repo: https://github.com/Trigodil/claude-reword Feedback and PRs are welcome
