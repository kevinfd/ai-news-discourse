---
id: "9db297d256fa75d3"
title: "Benchmarking Bot Detection Systems Against Modern AI Agents in 2026"
url: "https://research.poh.org/bot-benchmarking-2026"
link: "https://research.poh.org/bot-benchmarking-2026"
source: "Proof of Human Research"
domain: "research.poh.org"
source_type: "community"
collector: "hackernews"
date: "2026-10-20T17:10:31Z"
published_date: "2026-10-20"
collected_at: "2026-10-21T12:06:46Z"
authors: ["mdahardy"]
language: "en"
summary: "We revisit our bot detection benchmark with stealth browsers and modern AI agents, and find detection rates ranging from 9% to 99%.\nA year ago, we evaluated five leading bot detection systems (Proof of Human, Google reCAPTCHA v3, hCaptcha, Fingerprint Pro, and Cloudflare Turnstile) against automated browsers programmed to complete a set of predefined tasks. Detection rates varied substantially,…"
tags: []
orgs: ["Google", "xAI", "Perplexity"]
topics: ["agents & coding", "models & research", "chips & infrastructure"]
content_source: "fulltext"
word_count: 877
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50169506"
score: 47
comments: 7
community: "Hacker News"
---

# Benchmarking Bot Detection Systems Against Modern AI Agents in 2026

Proof of Human Research · mdahardy · 2026-10-20

We revisit our bot detection benchmark with stealth browsers and modern AI agents, and find detection rates ranging from 9% to 99%.
A year ago, we evaluated five leading bot detection systems (Proof of Human, Google reCAPTCHA v3, hCaptcha, Fingerprint Pro, and Cloudflare Turnstile) against automated browsers programmed to complete a set of predefined tasks. Detection rates varied substantially, ranging from 33% to 87%. Systems that incorporated behavioral signals alongside device-level signals generally outperformed those relying on device information alone.
Since then, browser automation has advanced considerably. Modern AI agents can interpret webpages, plan actions, and interact with interfaces through increasingly capable browser environments. We therefore revisited our benchmark with an expanded set of adversaries, including conventional browser automation, stealth browsers, and AI-powered browsing agents, and tested a similar set of detection systems: Proof of Human, Google reCAPTCHA v3, hCaptcha, Cloudflare Turnstile, and Cloudflare Bot Management. The results reveal similarly wide variation in detection performance.
In this post, we examine how each system performed, where it failed, and what these results suggest about the challenges of distinguishing humans from increasingly capable AI agents.
Our task used a five-question survey combining multiple-choice items with open-ended responses. Each of the five adversaries (i.e., AI agents) attempted the survey 20 times, yielding up to 100 sessions per detection system. Some detection systems failed or crashed before session completion, leaving between 89 and 100 evaluable sessions for each system.
The table below summarizes the detection systems included in the benchmark and the signals each uses to identify automated activity.
Our set of adversaries covers increasingly sophisticated forms of automation: conventional scripted browsers, stealth browsers designed to conceal automation signals, and AI agents capable of navigating webpages and completing tasks autonomously.
We found that detection performance varied substantially across systems. Aggregated across all adversaries, Proof of Human identified 99% of automated sessions, followed by reCAPTCHA v3 at 69.4%, hCaptcha at 44.3%, Cloudflare Turnstile at 42.1%, and Cloudflare Bot Management at 9.1%.
Performance differed considerably by adversary. The clearest split was between scripted browsers and AI agents. hCaptcha and Cloudflare Turnstile caught nearly every scripted Chromium and CloakBrowser session but few of the AI-agent sessions. reCAPTCHA v3 showed the opposite pattern, identifying most agent sessions but none from CloakBrowser. Cloudflare Bot Management caught few sessions from any adversary, while Proof of Human detected at least 95% of sessions overall.
As most detection systems are black-box, we cannot directly determine which signals produced each result. However, the systems' observed behavior, together with publicly available documentation, suggests several likely sources for this failure:
- reCAPTCHA v3 detected most sessions from standard Chromium and the cloud-hosted agents but did not detect CloakBrowser. CloakBrowser was the only adversary that combined a source-level modified browser fingerprint with a residential IP address. Our results cannot determine whether its browser fingerprint, residential IP, or a combination of the two was primarily responsible for its success.
- hCaptcha gave challenges to both Chromium and CloakBrowser, neither of which could reliably complete the image-based task. By contrast, the three vision-capable agents—Browser Use, Grok, and Perplexity Comet—were generally able to interpret and solve the image grid, allowing most of their sessions to pass.
- Cloudflare Turnstile detected both scripted-browser adversaries: Chromium and CloakBrowser failed to receive verification tokens, even after the full 30-second waiting period. However, it did not detect any of the three AI agents, and did not even issue challenges during these sessions.
- Cloudflare Bot Management detected relatively few sessions overall. This pattern is consistent with the stealth browser and cloud agents presenting clean browser-level signals, although the higher detection rate for Grok may reflect infrastructure-level signals Cloudflare uses, such as IP or TLS reputation.
Several limitations should be considered when interpreting these results:
- Some systems crashed or failed before completion, resulting in slightly different sample sizes across conditions.
- We evaluated the product tiers available to us rather than enterprise versions, which may incorporate additional signals or more advanced detection capabilities.
- We measured detection rates for automated sessions but did not evaluate false-positive rates among human respondents.
- Some systems, including reCAPTCHA, may become better calibrated as they observe more traffic and establish a reputation for a website. Detection rates could therefore differ in a longer-running deployment.
Our results suggest that bot detection is entering a new phase. Traditional automation signals remain effective against scripted browsers, but they are less reliable against AI agents that genuine browser environments intelligently. Interactive challenges may offer limited protection when vision-capable agents can interpret and complete them. And as browser-level indicators become easier to avoid, the way a user behaves throughout a session becomes increasingly important for distinguishing human activity from automation.
Future benchmarks should test larger volumes of traffic, include human participants to measure false-positive rates, and evaluate more complex tasks and emerging agents. At Proof of Human, we will continue tracking these changes and developing methods in this evolving threat landscape. To test Proof of Human on your own application, visit poh.org.
Milena Rmus, Mayank Agrawal, and Mathew Hardy work at Proof of Human, PBC, where they are building Proof of Human, an invisible authentication system for the web. Previously, they completed PhDs in cognitive science at the University of California, Berkeley (Milena) and Princeton University (Mayank and Matt).
