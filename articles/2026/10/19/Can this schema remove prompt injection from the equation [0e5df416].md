---
id: "0e5df416b95f951c"
title: "Can this schema remove prompt injection from the equation?"
url: "https://reddit.com/r/ArtificialInteligence/comments/1x9yrjy/can_this_schema_remove_prompt_injection_from_the"
link: "https://reddit.com/r/ArtificialInteligence/comments/1x9yrjy/can_this_schema_remove_prompt_injection_from_the"
source: "Reddit"
domain: "reddit.com"
source_type: "community"
collector: "reddit"
date: "2026-10-19T14:42:58Z"
published_date: "2026-10-19"
collected_at: "2026-10-20T12:06:23Z"
authors: ["no_awkward_Intention"]
language: "en"
summary: "I asked myself - how could we beat injections (since it's a fundamental flaw of the LLM`s architecture)? And this is my attempt Every user input goes to the mediator first (mediator is a program, not llm). The only thing it does at this step with the input is search for a matching template. Template found. The user gets a form back, not an answer. They fill it in, the mediator validates the…"
tags: ["r/ArtificialInteligence"]
orgs: []
topics: ["agents & coding", "models & research", "search & media"]
content_source: "post"
word_count: 345
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ArtificialInteligence/comments/1x9yrjy/can_this_schema_remove_prompt_injection_from_the/"
score: null
comments: null
community: "r/ArtificialInteligence"
---

# Can this schema remove prompt injection from the equation?

Reddit · no_awkward_Intention · 2026-10-19

I asked myself - how could we beat injections (since it's a fundamental flaw of the LLM`s architecture)? And this is my attempt Every user input goes to the mediator first (mediator is a program, not llm). The only thing it does at this step with the input is search for a matching template. Template found. The user gets a form back, not an answer. They fill it in, the mediator validates the fields, and only the validated filled template goes to the action agent. No template found. The input goes to the read-only agent, which has no rights to act. Its answer goes straight back to the user and never passes through the action agent. The action agent publishes the templates and variables validation rules to the mediator. The list of things the system can do is defined by the developer, not by the user’s text or by a model on the fly. Running the program is way cheaper (resource wise) that running LLM The key invariant is this: untrusted text has no path to an agent with side effects except through a typed form. It is the same idea as parameterized queries in SQL. What to do is chosen from a finite allowlist, and user input only fills in field values that are checked against a schema. The model is close to the Action-Selector and Dual LLM patterns from “Design Patterns for Securing LLM Agents against Prompt Injections” (2025). Formal model T = {t₁,…,tₙ} templates published by the action agent t = (S_t, a_t) field schema and the permitted action m(x) ∈ T ∪ {⊥} template lookup for input x if m(x) = t: the user fills in f ∈ S_t Action(x) = a_t(f) if V_t(f) = 1 Action(x) = ∅ if V_t(f) = 0 if m(x) = ⊥: y = R(x), y → User, Effects(R) = ∅ Security property, for any untrusted x: Effects(x) ⊆ { a_t(f) : t ∈ T, f ∈ S_t, V_t(f) = 1 } I wanna hear(read) your thoughts about this approach. You are welcome to comment ))
