---
id: "f433b8597cc3aa3f"
title: "Google adding official Google AI plan support to Pi coding agent"
url: "https://github.com/earendil-works/pi/pull/12614"
link: "https://github.com/earendil-works/pi/pull/12614"
source: "GitHub"
domain: "github.com"
source_type: "community"
collector: "hackernews"
date: "2026-11-28T05:42:49Z"
published_date: "2026-11-28"
collected_at: "2026-11-28T13:03:39Z"
authors: ["mtford"]
language: "en"
summary: "Repository navigation\nGoogle AI plan - #12614\nDraft\ndavidbrai wants to merge 13 commits into\nDraft\nGoogle AI plan#12614davidbrai wants to merge 13 commits into\nConversation\nNew google-ai-plan provider: sign in with Google (loopback OAuth with PKCE\nand DPoP-bound refresh tokens) and use the plan's Gemini models through the\nInteractions API (google-interactions, :createPerUserQuota endpoint).\n-…"
tags: []
orgs: ["Google"]
topics: ["agents & coding", "products & launches", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 882
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50675069"
score: 25
comments: 5
community: "Hacker News"
---

# Google adding official Google AI plan support to Pi coding agent

GitHub · mtford · 2026-11-28

Repository navigation
Google AI plan - #12614
Draft
davidbrai wants to merge 13 commits into
Draft
Google AI plan#12614davidbrai wants to merge 13 commits into
Conversation
New google-ai-plan provider: sign in with Google (loopback OAuth with PKCE
and DPoP-bound refresh tokens) and use the plan's Gemini models through the
Interactions API (google-interactions, :createPerUserQuota endpoint).
- Streaming, thinking with signed thought replay, tool calls, usage
- Plan errors: daily limit (not retried), model not on plan, sign-in,
  eligibility, kill switch
- pi-ai ships no Google client; coding-agent passes pi's own client to
  googleAiPlanProvider(), other apps must register their own
- Default model gemini-4-hydrogen
…e AI Ultra plan sign-in
        
  
    Contributor
        
    
    
  fitchmultz 
      added a commit
        to fitchmultz/pi
      that referenced
      this pull request
    
      Nov 27, 2026 
    
    
      
  
    
      …#12614 (#596)
* feat(ai): add Google AI Ultra plan sign-in
Port earendil-works/pi draft earendil-works#12614 at 628d2cc. Share the Interactions adapter while keeping the Bearer quota route separate from the API key route.
* fix(ai): enforce strict tool sampling on google-ai-plan interactions
* fix(ai): preserve classified google-ai-plan error messages
* fix(ai): honor thinkingSummaries on google-ai-plan interactions
    
  gakonst 
      pushed a commit
        to nanocodexyz/nanocode
      that referenced
      this pull request
    
      Nov 27, 2026 
    
    
      
  
    
      …PI (#1317)
Google lets third-party apps run Gemini on a user's Google AI plan quota
through the Interactions API's per-user quota endpoint
(POST /v1beta/interactions:createPerUserQuota), signed in with the app's
own Google-approved OAuth client. pi (earendil-works/pi#12614) and Hermes
Agent (NousResearch/hermes-agent#159701) already target it. This adds the
same route to the antigravity harness as --google-auth google-ai-plan, so
nanocode is ready once its own client is approved.
- Sign-in (PlanLogin, PlanAuth): Google OAuth for a Desktop app client
  with a loopback redirect on http://127.0.0.1:PORT/oauth2callback, PKCE,
  an OIDC nonce and a DPoP key (RFC 9449, ES256 over nanocode-tempo's
  P-256). The code exchange proof uses the code's hash as jti; refreshes
  retry once with Google's DPoP-Nonce and once with its Date for clock
  skew; invalid_grant and unauthorized_client ask to sign in again. The
  client comes from NANOCODE_GOOGLE_AI_PLAN_CLIENT_ID and
  NANOCODE_GOOGLE_AI_PLAN_CLIENT_SECRET and is saved with the sign-in in
  ~/.nanocode/google-ai-plan.json (PlanStore, the same locked atomic
  writer as the Antigravity subscription, now generic over the type).
- Wire: the harness's generateContent body becomes one stateless
  Interactions request (store: false): contents become user_input,
  thought, model_output, function_call and function_result steps, a
  thought signature the harness carried onto the next part goes back on
  its thought step, a call with none gets skip_thought_signature_validator,
  calls without ids get stable ones paired with their responses, and
  Gemini schemas become JSON Schema. The SSE steps come back as the same
  Parts, usage and finish reasons the other routes give. googleSearch,
  explicit caches, thinkingBudget and unknown fields are refused, not
  dropped. A daily-limit 429 fails at once with a plan hint.
- CLI: nanocode login google-ai-plan, /login google-ai-plan (and
  /login google plan), --google-auth google-ai-plan, setup google --check
  for it, and auto selects a saved plan sign-in before a saved Antigravity
  subscription.
Checked with a harness in output/plan-check against a mock Sender: login
(PKCE S256, state, loopback-only redirect, scope and ID token checks,
single use), every DPoP proof verified with graviola's independent P-256
verifier, refresh nonce and clock-skew retries, the request and replayed
steps compared field by field, streamed thoughts, text and call
arguments, usage, a cut stream, a refused googleSearch tool, a daily
limit that is not retried, and a 401 that refreshes and retries.
scripts/check: check, tidy, machines, canaries, memory and sim (63
scenarios, 163 pass jobs x 8 seeds, 460 canaries) green; check-wasm of
the touched crates green once the wasm32 target was installed.
Not yet tried against Google: nanocode has no approved client.
      
   Merged
  
      
      
  
    9 of 11 tasks
  
    
  mizorewww 
      added a commit
        to mizorewww/pi
      that referenced
      this pull request
    
      Nov 28, 2026 
    
    
      
  
    
      …-plan
feat(ai,coding-agent): add Google AI Ultra plan provider
Upstream PR: earendil-works#12614
    
  mizorewww 
      added a commit
        to mizorewww/pi
      that referenced
      this pull request
    
      Nov 28, 2026 
    
    
      
  
    
      Fork release: upstream v1.7.0 (main @ 2126569) plus upstream PR
earendil-works#12614 (Google AI Ultra plan provider), fork-specific install.sh, and
README installation instructions pointing at this fork's releases.
  This was referenced Nov 28, 2026 
    
  chunyoupeng 
      added a commit
        to chunyoupeng/pi
      that referenced
      this pull request
    
      Nov 28, 2026 
    
    
  
              
                    slmntopuz-cmd
    
              
              approved these changes
              
                  
                    Nov 28, 2026 
                  
              
              
            
This branch has not been deployed
  
    
      This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
      Learn more about bidirectional Unicode characters
    
  
  
    Sign up for free
    to join this conversation on GitHub.
    Already have an account?
    Sign in to comment
  
Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.
