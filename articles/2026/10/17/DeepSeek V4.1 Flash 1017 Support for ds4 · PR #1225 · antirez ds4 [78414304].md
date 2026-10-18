---
id: "7841430455379003"
title: "DeepSeek V4.1 Flash 1017 Support for ds4 · PR #1225 · antirez/ds4"
url: "https://github.com/antirez/ds4/pull/1225"
link: "https://github.com/antirez/ds4/pull/1225"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "reddit"
date: "2026-10-17T20:42:23Z"
published_date: "2026-10-17"
collected_at: "2026-10-18T12:05:49Z"
authors: ["returnity"]
language: "en"
summary: "Just pushed a PR for dwarfstar that adds support for Deepseek-v4.1-Flash-1017 with its new engrams and updated vision tower. The PR basically just adds compatibility for the file revisions and checks to make sure the vision+language model file combination matches, raising on mixed pairings. Any files quantized with the ds4 quantization suite will load without any special changes, and it…"
tags: ["r/LocalLLaMA"]
orgs: ["DeepSeek"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 387
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/LocalLLaMA/comments/1x8koix/deepseek_v41_flash_1017_support_for_ds4_pr_1225/"
score: null
comments: null
community: "r/LocalLLaMA"
---

# DeepSeek V4.1 Flash 1017 Support for ds4 · PR #1225 · antirez/ds4

GitHub · returnity · 2026-10-17

Repository navigation
Support DeepSeek V4.1 Flash 1017 by matching the vision GGUF to its language model - #1225
Open
nazeshinjite wants to merge 1 commit into
Open
nazeshinjite wants to merge 1 commit into
Conversation
DeepSeek released a second V4.1 Flash checkpoint (DeepSeek-V4.1-Flash-1017,
revision 1bae0e10) with the same architecture, tokenizer and Engram layout but
retrained weights, including the vision tower. The runtime pinned V4.1 vision
sidecars to the first checkpoint's revision, so a correctly built 1017 sidecar
was rejected while a September sidecar loaded next to a 1017 language model.
The engine now requires the sidecar's source revision to equal the language
GGUF's. The converters take name and source URL from a table of released
checkpoints instead of literals, and refuse unknown revisions rather than
stamping them with the first checkpoint's URL. Output for the original
checkpoint is byte-identical to before.
    
  ivanfioravanti 
      added a commit
        to ivanfioravanti/ds4-metal
      that referenced
      this pull request
    
      Oct 18, 2026 
    
    
      
  
    
      Brings in nazeshinjite's change from antirez#1225,
with the commit unchanged: ds4 pairs a V4.1 vision GGUF with its language GGUF
by general.source.revision instead of one fixed revision, so encoders built
from DeepSeek-V4.1-Flash-1017 load. The converters take --source-revision and
record the 1017 repo name and URL.
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
