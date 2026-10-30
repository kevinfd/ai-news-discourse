---
id: "467e5544f15e0df5"
title: "Failure log #1: the patch was real, the bug was different"
url: "https://reddit.com/r/artificial/comments/1xiqi8e/failure_log_1_the_patch_was_real_the_bug_was"
link: "https://reddit.com/r/artificial/comments/1xiqi8e/failure_log_1_the_patch_was_real_the_bug_was"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-29T17:31:35Z"
published_date: "2026-10-29"
collected_at: "2026-10-30T12:05:25Z"
authors: ["AIGODSEND"]
language: "en"
summary: "an agent was asked to verify a security fix. it found the patch, the tests, the advisory, and the CVE text. everything matched. it concluded the issue was resolved. the failure wasn't a hallucinated fact. it was a category error: the patch fixed a different bug than the one the researcher reported. the diff was real, the tests passed, and the original trigger still fired. the evidence supported…"
tags: ["r/artificial"]
orgs: []
topics: ["agents & coding"]
content_source: "post"
word_count: 187
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xiqi8e/failure_log_1_the_patch_was_real_the_bug_was/"
score: null
comments: null
community: "r/artificial"
---

# Failure log #1: the patch was real, the bug was different

Reddit · AIGODSEND · 2026-10-29

an agent was asked to verify a security fix. it found the patch, the tests, the advisory, and the CVE text. everything matched. it concluded the issue was resolved. the failure wasn't a hallucinated fact. it was a category error: the patch fixed a different bug than the one the researcher reported. the diff was real, the tests passed, and the original trigger still fired. the evidence supported "a patch exists," not "this bug is closed." the check that catches it: don't ask "does the patch match the advisory?" ask "does the original PoC still fire?" if the PoC is unavailable, ask the reporter for the trigger, not the fix. a patch can be real and irrelevant at the same time. this is the failure mode i care about: confident, well-sourced, and wrong about which question it answered. if you run agent reviews, the useful log is not "was the answer correct?" but "which claim did the evidence actually support?" if you have a case, put the claim and the evidence in the comments. i'll tell you which question the evidence actually answered. (composite example, details changed.)
