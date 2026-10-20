---
id: "0bbe64b059dfab4a"
title: "Vite+ an excellent toolchain for AI agent development"
url: "https://janmichalek.com/blog/vite-plus-agentni-vyvoj?lang=en"
link: "https://janmichalek.com/blog/vite-plus-agentni-vyvoj?lang=en"
source: "janmichalek.com"
domain: "janmichalek.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-20T06:40:49Z"
published_date: "2026-10-20"
collected_at: "2026-10-20T12:06:23Z"
authors: ["kanbaruu"]
language: "en"
summary: "Vite+ changed how I build applications with AI agents\nOne project had 47 development dependencies, seven config files, and a Markdown file explaining to the agent how to run everything. At 2 a.m., I was debugging a difference between local checks and CI. The code was done; the tooling around it wasn't. After three weeks with Vite+ across four projects, I have a simple rule for new Vite apps: put…"
tags: []
orgs: []
topics: ["agents & coding", "products & launches"]
content_source: "fulltext"
word_count: 1292
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50162198"
score: 23
comments: 19
community: "Hacker News"
---

# Vite+ an excellent toolchain for AI agent development

janmichalek.com · kanbaruu · 2026-10-20

Vite+ changed how I build applications with AI agents
One project had 47 development dependencies, seven config files, and a Markdown file explaining to the agent how to run everything. At 2 a.m., I was debugging a difference between local checks and CI. The code was done; the tooling around it wasn't. After three weeks with Vite+ across four projects, I have a simple rule for new Vite apps: put it in the first prompt I give the AI.
The short version
- For a new Vite app, I have the agent create the project with vp create, then verify its work with vp check, vp test, and vp build.
- Speed is nice, but the bigger win for me is one clear workflow for the agent, me, and CI.
- For an existing project, I treat vp migrate as the start of a migration. I still review the diff, tests, and build behavior.
A slow linter wasn't the problem
My commands were spread across ESLint, Prettier, TypeScript, a test runner, and package.json scripts. When I let an agent into the project, its first job was figuring out which command was the right one. I wrote instructions to explain that. Now I had another file to maintain. Excellent time saver, right?
It wasn't just the number of files. Once, my local setup and CI checked a generated file differently. The agent saw one result; the pipeline saw another. Faster component generation doesn't fix that.
Vite+ brings everyday tasks under vp: Vite for development and builds, Vitest for tests, Oxlint and Oxfmt for checks, tsdown for libraries, and Vite Task for tasks. You can keep their configuration in vite.config.ts. You still have package.json, tsconfig, and, depending on the project, framework configuration. “One file for absolutely everything” would look good on a banner and bad in a real repo.
For a React app, these are the commands I need after creating the project:
The commands above assume vp is available globally. A global install is optional; you can also run Vite+ as a local dependency through a package manager. vp install uses the package manager selected for the project, so Vite+ doesn't replace npm or pnpm.
I don't let the agent guess what “done” means
The Vite+ docs include a prompt for AI assistants. It's a useful starting point, but I adapt it to the project. My goal is concrete: the agent should use Vite+ to set up the app and not quietly abandon it after generating the first page.
I don't require a global install via curl in every project. For a one-off setup, something like npx --package=vite-plus@1.3.0 vp create is enough; in an established project, the agent can run the local CLI through the selected package manager. I don't ban create-vite, either: vp create vite uses that template. What matters is that the agent follows the intended setup and keeps one consistent toolchain.
When I gave an agent free rein, I ended up with both Prettier and Oxfmt, three lockfiles, and unreliable CI. Banning a second formatter and requiring one lockfile aren't aesthetic preferences. They're two mistakes I don't want to clean up again.
One command gives me fast feedback
After changing code, I run vp check. It checks formatting and lint; it checks TypeScript when both typeAware and typeCheck are enabled in the configuration. A new project created with vp create enables them by default. In an existing project, I verify that setting instead of assuming a green result also means the types are sound.
Here's the difference from my old workflow:
vp check --fix can repair some findings automatically. After that, I read the diff and run the check again. A green lint result still doesn't tell me whether the app does the right thing. I need vp test for behavior and vp build to verify the application builds.
I also put that rule in the repo's agent instructions. When I return to a project a week later, a new agent won't remember yesterday's chat. The repo still knows its commands.
Local instructions and Git hooks help, but they can be bypassed or disabled. I run the same checks in CI. On an experiment where I let an agent work unattended, human review before merging was still my responsibility.
What I measured
In a monorepo, CI went from 4 minutes to 50 seconds after I changed the workflow. A pre-commit check dropped from 11 seconds to under 2. Those are results from my projects, not a benchmark comparing Vite+ with another toolchain under identical conditions. Part of the gain comes from what runs and which files it checks; you won't automatically get those CI times with a different configuration.
For quick checks of changed files, I use vp staged and Git hooks managed with vp hooks. When different projects behave differently, vp toolchain shows me their active versions. vp toolchain --global shows the global installation. That's more useful for debugging than my old method: “I definitely updated it.”
There are two things to distinguish in a monorepo. vp run executes a package.json script or a task defined in vite.config.ts, and it can order work according to workspace dependencies. Caching is not enabled automatically for package.json scripts. You can enable it with, for example, vp run --cache build. Tasks defined in vite.config.ts are cached by default. I won't turn my CI timing into a promise that vp run alone makes every build faster.
Where it got awkward
vp migrate ran on an older monorepo for about 4 minutes. It converted my ESLint, Prettier, and original tsup build setup, and nothing broke in my case. That doesn't mean every migration takes four minutes. You have to compare the result with the old lint, tests, hooks, and build output. Plugins and custom rules may still need manual work.
Another trap is the difference between a built-in command and a project script. vp build runs a Vite app build. vp run build runs the build script from package.json or a task with that name. In a Next.js project, the agent must not assume vp build replaces next build. The same distinction applies to vp dev and vp run dev. Vite+ can work with other templates, but that doesn't change what those commands do.
The third issue is version management. The global vp env can manage Node.js and package managers. I have three projects on three Node versions, and it made switching easier for me; if you don't want that, you can turn it off with vp env off. vp upgrade updates the global CLI, not the local vite-plus package in every project automatically. I wrote that explicitly in my agent instructions because the command name invites the opposite assumption.
Who gets Vite+ in my first prompt
Anyone starting a new Vite app with AI doing the setup. The cost of standardizing is small here: choose one toolchain, put the check commands in the repo and CI, and the agent has a clear path from a code change to verification. Across three weeks and four projects, the main benefit for me was that I stopped explaining the basic commands over and over.
I wouldn't blindly migrate a large existing app with a working build and test suite. For a framework with its own build, I'd first decide which parts of Vite+ I actually want to use. And if I already had a well documented, fast, stable stack, the promise of “one command” alone wouldn't convince me to replace it.
Next time you start a Vite project, put vp create in the first prompt and ask for the outputs of vp check, tests, and the build as part of the definition of done. A screenshot of the finished app is nice. Passing checks tell you more.
