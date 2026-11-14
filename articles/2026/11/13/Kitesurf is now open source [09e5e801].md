---
id: "09e5e80125ce2409"
title: "Kitesurf is now open source"
url: "https://blog.cloudflare.com/kitesurf-open-source"
link: "https://blog.cloudflare.com/kitesurf-open-source"
source: "Cloudflare Blog"
domain: "blog.cloudflare.com"
source_type: "company_blog"
collector: "rss"
date: "2026-11-13T20:20:21Z"
published_date: "2026-11-13"
collected_at: "2026-11-14T13:03:44Z"
authors: ["Celso Martinho", "Rui Figueira", "Bernardo Pereira", "Luís Duarte"]
language: "en"
summary: "We introduced   Kitesurf , our stateless browser for AI agents that runs entirely on top of Workers, in August and followed up  in September with WebMCP support, new APIs, and improved compatibility. On every occasion, we mentioned our commitment to open sourcing it so that developers could run their own browser engine on their own Cloudflare accounts if they want to. That promise is now real.…"
tags: ["Agents", "AI", "Browser Run", "Open Source", "Rust", "WebAssembly", "Workers"]
orgs: []
topics: ["agents & coding", "jobs & society", "models & research"]
content_source: "fulltext"
word_count: 752
paywalled: false
image: "https://blog.cloudflare.com/_emdash/api/media/file/01M7B8M53647Q1KNRABY8VM2G7.png"
discussion_url: null
score: null
comments: null
community: null
---

# Kitesurf is now open source

Cloudflare Blog · Celso Martinho, Rui Figueira, Bernardo Pereira, Luís Duarte · 2026-11-13

Kitesurf is now open source
We introduced Kitesurf, our stateless browser for AI agents that runs entirely on top of Workers, in August and followed up in September with WebMCP support, new APIs, and improved compatibility. On every occasion, we mentioned our commitment to open sourcing it so that developers could run their own browser engine on their own Cloudflare accounts if they want to.
That promise is now real. Kitesurf is open source on GitHub under the Apache 2.0 license. You can read the code, run it locally, change it, and deploy your own instance to Cloudflare Workers.
A browser built for agents
Kitesurf runs entirely on Cloudflare Workers. It parses HTML, applies CSS, executes page JavaScript, and renders screenshots without a browser container. It supports the Chrome DevTools Protocol (CDP), so you can connect clients such as Puppeteer.
Our main goal is to give AI agents a lightweight, efficient browser — one that can load websites, execute JavaScript, and interact with pages while using less CPU and memory than a full browser like Chromium, and scaling on demand across Cloudflare’s global Workers network.
Read more about why and how we built Kitesurf in our initial announcement and how to use it in Browser Run’s developer documentation.
What is inside the repository?
Kitesurf builds on Cloudflare’s Developer Platform and APIs, alongside an ecosystem of open-source Rust packages compiled to WebAssembly:
- Blitz provides HTML parsing, the DOM, layout, and painting.
- Stylo provides CSS parsing, cascading, and computed styles.
- Boa runs JavaScript inside WebAssembly (as the last resort only when we can’t run JavaScript in Dynamic Workers).
- Linebender libraries provide text layout and 2D graphics, and Krilla generates PDF output.
These projects made Kitesurf possible. They retain their respective licenses; the repository's NOTICE documents third-party notices.
Kitesurf has three main parts: the Engine manages browser sessions and client connections, PageScript runs the page and its JavaScript, and PageRenderer draws the result.
All packages, the engine, its Rust core, DOM shims, renderer, and Kitesurf CLI live separately in folders under the repository’s packages directory where you can explore how all the pieces fit together.
Run your own Kitesurf
To run Kitesurf locally, follow the repository's build requirements, then clone the repository, install dependencies, and start the engine:
git clone https://github.com/cloudflare/kitesurf.git
cd kitesurf
pnpm install --frozen-lockfile
pnpm run dev
The first build compiles the Rust core and its dependencies, so give it some time. Subsequent builds reuse the build cache. Finally wrangler starts a local development server at http://127.0.0.1:8787. Open that address to try a page in Chrome DevTools, or use it programmatically.
You can use puppeteer with a NodeJS script:
import puppeteer from "puppeteer-core";
const browser = await puppeteer.connect({
  browserWSEndpoint: "ws://127.0.0.1:8787/devtools/browser",
});
try {
  const page = await browser.newPage();
  await page.goto("https://example.com/");
  await page.screenshot({ path: "page.png" });
} finally {
  await browser.disconnect();
}
Or you can point your AI harness at the local CDP port (agents love CDP) and watch it take full control of Kitesurf.
Deploy to your Cloudflare account
When you’re done changing and testing locally, you can deploy the engine to your own account and use Kitesurf from there instead of the Browser Run managed APIs we provide. Note that a Workers Paid plan is required because Kitesurf uses Dynamic Workers to create isolated Workers for pages.
From the repository root:
pnpm run deploy
Help us make it better
As with all of our open-sourced projects, Kitesurf lives in Github and we welcome forks and contributions. However, note that Kitesurf is under heavy development and we are focusing on making the engine more compatible (check out Web Platform Test evolution), more reliable, and efficient.
Start with the contribution guidelines if you want to contribute. Open an issue with a minimal reproduction or a proposed approach, and get vouched by a maintainer before opening a pull request. Focused fixes with tests, clear evidence, and a well-defined scope are much easier to review than large rewrites or unrelated cleanup, but all contribution does not have to be code: a small page that reproduces a rendering bug, a failing automation workflow, or a clear documentation correction can help us move forward.
Stay tuned
Kitesurf is evolving quickly. Stay tuned for updates in the blog and our changelog, and keep an eye on the official landing page for the latest on standards compatibility in Web Platform Tests page and benchmarks.
And come chat with the team on Discord. We’re building a browser for agents, and we’d love your help making it better.
