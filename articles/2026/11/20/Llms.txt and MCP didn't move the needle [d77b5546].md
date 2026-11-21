---
id: "d77b5546421e2909"
title: "Llms.txt and MCP didn't move the needle"
url: "https://backpackforlaravel.com/articles/opinions/llms-txt-and-mcp-didn-t-move-the-needle-for-us-here-s-what-did"
link: "https://backpackforlaravel.com/articles/opinions/llms-txt-and-mcp-didn-t-move-the-needle-for-us-here-s-what-did"
source: "Backpack for Laravel"
domain: "backpackforlaravel.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-20T14:00:23Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["moebrowne"]
language: "en"
summary: "Two years ago, an admin panel for a simple website took me a day, maybe two - and I was proud of how fast I was. Now it takes me about...\n    \n    \n      Share:\n    \n    \n    \n  \nTwo years ago, an admin panel for a simple website took me a day, maybe two - and I was proud of how fast I was. Now it takes me about an hour or two.\nThe old day went like this. Install the package, generate the CRUDs,…"
tags: []
orgs: ["Anthropic"]
topics: ["agents & coding", "models & research"]
content_source: "fulltext"
word_count: 1626
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50574772"
score: 31
comments: 21
community: "Hacker News"
---

# Llms.txt and MCP didn't move the needle

Backpack for Laravel · moebrowne · 2026-11-20

Two years ago, an admin panel for a simple website took me a day, maybe two - and I was proud of how fast I was. Now it takes me about...
    
    
      Share:
    
    
    
  
Two years ago, an admin panel for a simple website took me a day, maybe two - and I was proud of how fast I was. Now it takes me about an hour or two.
The old day went like this. Install the package, generate the CRUDs, configure every field and column, wire up the relationships, click through everything to check it works. Thirty to sixty minutes per CRUD, easily. Now I describe what I want, the agent runs our generators, writes the configuration, writes the tests, and I review. A day of work fits in an hour. A week-long feature fits in a day.
I'm not the only one seeing this. In February 2026, a customer from New Zealand gave us a 10 out of 10 in our feedback form. The whole review was one line:
"Straightforward to use (particularly with Claude looking over my shoulder!)"
That's the new normal. The developer isn't alone with the docs anymore. There's an agent next to them that already knows the package.
I maintain Backpack for Laravel, an admin panel package that's been around for 10 years. We did a bunch of things to make the AI agents better at writing admin panels with Backpack - it's a quick-moving niche. But when I looked at why AI agents are so good at it, the answer surprised me. Most of it isn't the AI-specific stuff we built. Two of the things everyone tells you to add, llms.txt and an MCP server, barely helped us at all.
Here's what did help, so you can do the same for your package.
Let's get these out of the way first, because most "make your package AI-ready" advice starts with them.
llms.txt. We shipped one. I don't think it does much. Agents rarely go looking for it. When they do, they find a table of contents for docs they could already read. Thinking of removing it, tbh.
An MCP server. We built one so agents could query our docs. The results were mixed at best. The agent has to decide to call it, and it usually doesn't. Then the queries some of the AIs make are... laughable. Of course our MCP doesn't return anything useful, your AI just typed two words - absurd! So no, I don't think our MCP is helpul any more - thinking of removing it too, tbh. An MCP server is a great fit for live data the agent can't get any other way - or tool use. Static documentation isn't that.
The lesson: anything the agent has to remember to go fetch is weak. What works is what's already in front of it, or already in its head.
Our biggest wins came from decisions we made years before anyone used AI to write code.
Backpack's core API has barely changed in the last four years. Even v8, which we're working on right now, started with maintenance: bumping and removing dependencies, fixing inconsistencies. The way you define a field or a column stays the same. We did that to make upgrades painless for old projects. The side effect: years of Backpack code ended up in model training data, and all of it is still correct.
When an agent writes CRUD::column('name'), it isn't searching or guessing. It already knows. Every rename you ship splits what the model learned into "old way" and "new way", and it will keep suggesting the old one for years.
There is a downside. Models sometimes write patterns from much older versions. We fix that with in-project instructions (more on that below), not by hoping the model catches up.
For your package: deprecate instead of rename. Keep old signatures working. Treat every breaking change as costing you twice: once for your users, once for every agent that learned the old API.
Our core, backpack/crud, is open source. That means ten years of GitHub issues, pull requests, tutorials, Stack Overflow answers and blog posts. All of it is training data. All of it is searchable when an agent does go looking.
You can't buy that. But if you're deciding between open source and closed, this is a new argument for open.
This is the one I think matters most for commercial packages. Composer installs everything into vendor/, including our paid add-ons. No obfuscation, no remote API. An agent can open the actual source of any feature, free or paid, and see exactly how it works.
We've always kept that code simple, commented and predictably organized, for humans. It turns out that's exactly what agents need too. In practice, reading vendor/ is how agents answer most of their own questions about Backpack. They do it without being told.
For your package: if you sell code, ship it readable. Obfuscated or SaaS-only features are invisible to the agent writing your customer's code.
Backpack has always been loose on purpose. You can override almost anything with a closure or a small tweak, without creating classes, registering providers or extending five things.
That turns out to be ideal for agents. Need a computed column? One line:
CRUD::column('full_name')->value(fn ($entry) => $entry->first_name.' '.$entry->last_name);
No custom column class, no view, no binding. Small changes stay in one file. That means less context for the agent to load, and fewer places for it to get things wrong. A strict, heavily abstracted architecture forces the agent to understand a lot before it can change a little.
For your package: for every extension point, ask how many files it takes to customize. If the answer is more than one, add a shortcut.
We added a Laravel Boost plugin for Backpack. Run php artisan boost:install, tick backpack/crud, and your agent gets our guidelines and skills straight in its context: which features exist, how to use them properly, which version-specific patterns to follow. The skill is split by topic (fields, columns, filters, operations, testing and so on), so the agent loads only the part it needs. We wrote about it when v7.1 shipped.
This worked where MCP didn't, for one reason: the agent doesn't have to decide to fetch it. It's already in context when the work starts. It also fixes the training-data downside above, because the instructions match the version actually installed.
For your package: if you're in the Laravel ecosystem, ship Boost guidelines. If you're not, ship the equivalent: a short, version-matched instructions file your users can drop into their agent's context.
php artisan backpack:crud Product creates the model, request, controller, route and menu item in one go. Then php artisan backpack:tests (from our backpack/test-generators add-on) writes a feature test for every CrudController, in PHPUnit or Pest, and backpack:tests:status shows which controllers still have no coverage. There are smaller ones too: backpack:field, backpack:column, backpack:filter, backpack:button, backpack:crud-operation.
This matters more with agents than without. A command gives the same correct result every time. Boilerplate the agent writes by hand is a fresh chance to make a small mistake in every file. The agent's time is better spent on what's actually specific to the project.
For your package: if users repeatedly write the same scaffolding, turn it into a command. Agents use CLI tools happily and reliably.
When names follow a pattern, agents guess right. A text field has a text column. A select2 field has a select2_multiple sibling, so select2_from_ajax has a select2_from_ajax_multiple one too. A date_picker field pairs with a date_picker column. The agent has seen one, so it correctly guesses the rest, without opening a single file.
Every inconsistency is a spot where the agent guesses wrong and you pay for it in review.
For your package: make things guessable. Same name for the same concept everywhere, same argument order, same patterns.
Our docs sit behind Cloudflare, and we turned on the feature that serves Markdown instead of HTML when an agent asks for it. Agents read our docs faster and with less noise. It's a small win, and a free one if you're already on Cloudflare.
In rough order of impact:
- Put instructions in the project, not behind a tool call. Boost guidelines or an equivalent file, matched to the installed version.
- Stop renaming things. Deprecate, alias, keep old signatures alive.
- Ship readable source, including the paid parts. Comment it for the next reader, human or not.
- Turn repeated scaffolding into commands. Generators for code, generators for tests.
- Cut ceremony. One-file customizations. Closures over classes where you can.
- Make names guessable. Same concept, same name, everywhere.
- Serve Markdown docs if your host makes it easy.
- Skip llms.txt and docs-only MCP unless you have a specific reason. Spend the time on the list above instead.
None of our biggest wins were clever. Stability, open code, simple architecture and good generators were all things we did for human developers. They just happen to be what AI agents need most too. The AI-specific additions only helped when they put the right information in front of the agent, without it having to ask.
One more thing, on the user side: use the best model you can get. The gap between today's frontier models and the ones on top six months ago is huge. It shows most on exactly this kind of work.
If you use Backpack with AI: how much faster are you building admin panels now? One hour instead of ten? A day instead of a week? Tell me in the comments. I'd love real numbers to compare against mine.
Subscribe to our "Article Digest". We'll send you a list of the new articles, every week, month or quarter - your choice.
What do you think about this?
