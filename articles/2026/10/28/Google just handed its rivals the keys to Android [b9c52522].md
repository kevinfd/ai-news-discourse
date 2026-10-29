---
id: "b9c525222015c967"
title: "Google just handed its rivals the keys to Android"
url: "https://thenewstack.io/android-agents-build-debug"
link: "https://thenewstack.io/android-agents-build-debug"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T17:43:09Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Amanda Caswell"]
language: "en"
summary: "Google is giving coding agents like Anthropic’s Claude Code and OpenAI’s Codex deeper access to its Android development tools, including devices, performance profilers and production crash reports; now, agents can now investigate bugs, test changes, and verify their own fixes. \n\n The push spans Android Studio and the terminal-based Android CLI, with Google opening both to third-party agents…"
tags: ["AI"]
orgs: ["Google", "Anthropic", "OpenAI"]
topics: ["agents & coding", "models & research", "robotics & autonomy", "products & launches"]
content_source: "fulltext"
word_count: 742
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Google just handed its rivals the keys to Android

The New Stack · Amanda Caswell · 2026-10-28

Google just handed its rivals the keys to Android
Google is giving coding agents like Anthropic’s Claude Code and OpenAI’s Codex deeper access to its Android development tools, including devices, performance profilers and production crash reports; now, agents can now investigate bugs, test changes, and verify their own fixes.
The push spans Android Studio and the terminal-based Android CLI, with Google opening both to third-party agents rather than steering developers toward Gemini. Matthew McCullough, vice president of product for Android, has emphasized giving developers the freedom to choose their own models and coding agents.
In a Wednesday post, Adarsh Fernando, senior product manager for Android developer tools, describes the goal as giving developers and their agents “the tools and knowledge to build high-quality Android apps faster.” The updates were announced Wednesday at Android Dev Summit.
Bring your own agent
The company’s Bring Your Own Agent feature now supports more than 40 coding agents that speak the open Agent Client Protocol, among them Anthropic’s Claude Agent, OpenAI’s Codex, and Google’s own Antigravity, and Google says the feature is now stable in Wednesday’s release of Android Studio Rabbit 2.
A developer can install several and switch between them without leaving the IDE, and connected agents inherit the IDE’s own read on a project — its structure, build configuration, symbols, and tools such as Compose Preview, the emulator, and Logcat — context they would otherwise have to rebuild through code searches and terminal guesswork.
Alongside it, a new Change Review feature scans an agent’s pending changes for common issues and can walk a developer through a large set of modifications before anything is applied, and Google is pushing the same reach beyond the IDE with official Android CLI plugins for Claude Code, and Codex that cover project creation, emulator management, UI inspection, and its Android documentation.
Compose previews from the terminal
Another announcement includes the new android preview command that lets coding agents render Jetpack Compose previews directly in the terminal without launching an IDE or emulator.
The company says agents using it completed UI tasks 77% faster while using up to three times fewer tokens, though it shared little about how it measured those results. The CLI also adds android device remote, giving agents access to physical devices in Google’s lab for testing.
agents using it completed UI tasks 77% faster while using up to three times fewer tokens, though it shared little about how it measured those results.
Finding memory leaks with Claude
Google is also giving agents more ways to investigate problems after an app is built, including performance issues, production crashes and memory leaks. In one demo, Claude Code worked with LeakCanary, an open source leak-detection library, to check critical user journeys for memory leaks using a single instruction from the developer.
Claude Code ran the journeys across multiple devices in parallel, analyzed heap dumps through the CLI’s LeakCanary integration, and traced the leaks back to the offending code. It then made the fixes and reran the tests to confirm they worked. Google says the tooling helped capable models complete these investigations nearly twice as fast while using up to 25% fewer tokens.
autonomous bug-finding can outrun autonomous bug-fixing — an Anthropic scanner flagged some 29,000 possible vulnerabilities in open-source code while only a few hundred were ever fixed.
The demo is very impressive, and it also runs against a record that counsels patience, since autonomous bug-finding can outrun autonomous bug-fixing — an Anthropic scanner flagged some 29,000 possible vulnerabilities in open-source code while only a few hundred were ever fixed.
A companion android signals command now pipes Android vitals and Firebase Crashlytics data into the same terminal workflow, which gives agents a direct line to production crashes, ANRs, and memory problems, but none of this retires the human in the loop, as developers who watched Claude Code land a Linux kernel fix only for reviewers to catch a race condition can attest.
A companion android signals command now pipes Android vitals and Firebase Crashlytics data into the same terminal workflow
Benchmarking agents with Android Bench
Google is also introducing Android Bench 2.0 to evaluate how models and agent harnesses perform on more complex Android development tasks. It tests whether completed apps actually run with assignments ranging from building an app from mockups to migrating an existing interface. Some tasks are modeled on work that would take an Android engineer several days, and the benchmark also measures completion time and cost.
