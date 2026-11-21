---
id: "ba4783ec4ae64b36"
title: "Your AI agent’s “memory problem” may be something else"
url: "https://thenewstack.io/ai-agent-memory-boundaries"
link: "https://thenewstack.io/ai-agent-memory-boundaries"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-20T17:00:00Z"
published_date: "2026-11-20"
collected_at: "2026-11-21T13:03:30Z"
authors: ["Daniela Pavlenco"]
language: "en"
summary: "An agent may need additional context to continue when a user returns the next day. A workflow may resume from the wrong step, or a preference may be remembered without its scope, or a retrieval may return an outdated document.  \n\n These are often described as “memory problems,” but they have different causes. Long-running agents rely on three kinds of context: workflow state to resume execution,…"
tags: ["AI Agents", "AI Engineering", "Databases", "sponsor-oracle", "sponsored-post-contributed"]
orgs: []
topics: ["agents & coding", "models & research", "policy & regulation", "products & launches"]
content_source: "summary"
word_count: 1364
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Your AI agent’s “memory problem” may be something else

The New Stack · Daniela Pavlenco · 2026-11-20

An agent may need additional context to continue when a user returns the next day. A workflow may resume from the wrong step, or a preference may be remembered without its scope, or a retrieval may return an outdated document.  

 These are often described as “memory problems,” but they have different causes. Long-running agents rely on three kinds of context: workflow state to resume execution, durable information to carry across sessions, and external knowledge for the current request. Each needs a clear owner, lifecycle, and access boundary. 

 LangGraph and LangChain give developers useful abstractions, but the application still needs to define ownership, lifecycle, and access boundaries for each context type. Keeping those responsibilities explicit makes failures easier to diagnose and long-running agents easier to operate.  

 Three context layers in a long-running AI agent 

 Layer What it answers What changes over time Workflow state Where the current run stopped Nodes, tool results, approvals, pending work Agent memory What should be remembered for later Facts, preferences, decisions, procedures, validity RAG knowledge What external evidence supports this request Documents, chunks, embeddings, versions, access scope 

 A checkpoint can resume a workflow, but it cannot define memory 

 A workflow checkpoint answers a narrow question: Where should this run continue?   

 In LangGraph, a checkpointer can persist graph state under a thread identifier so a workflow can pause for approval, recover after a process restart, or resume after a tool failure. That state can include messages, tool results, and execution progress. It supports durable execution, but persistence alone does not determine what an agent should remember across sessions.  

 Consider a customer-support agent handling a subscription change. Its checkpoint stores the state needed to resume the workflow. If the customer expresses a preference, application rules determine whether to save it as a durable memory, and which customer or account it applies to. Retrieval supplies the current policy passage, filtered for the caller’s access. Each layer serves a different purpose and follows its own update rules. 

 “The layers can share a database without sharing a lifecycle. Make those distinctions in the data model so retaining workflow history doesn’t turn into agent memory.” 

 The layers can share a database without sharing a lifecycle. A checkpoint may expire with a run, a memory may remain until corrected or removed, and a knowledge record may change with its source. Make those distinctions in the data model so retaining workflow history doesn’t turn into agent memory.  

 Give agent memory a lifecycle 

 Durable memory is information the application selects to carry across sessions. It must be possible to retrieve, validate, update, supersede, or delete. Each record should identify its owner, scope, source, and validity.  

 A conversation can produce a candidate fact, but it becomes durable memory only after application rules or explicit user confirmation accepts it. When a fact changes, the earlier value is superseded. When deletion is requested, apply the defined scope to the source record and any derived memories or searchable data. Where retention rules permit, superseded records may remain as history but should be excluded from retrieval for current facts.  

 “Scope, retention, correction, and deletion belong in the application and data model because a prompt that assembles the next context window cannot enforce those rules on its own.” 

 The lifecycle also includes boundaries. A preference for one user is not a global instruction. A tool outcome from one tenant should not become searchable context for another. Memory extracted from an untrusted document should not silently become policy. Scope, retention, correction, and deletion belong in the application and data model because a prompt that assembles the next context window cannot enforce those rules on its own. 

 RAG supplies knowledge for the current request 

 Retrieval-augmented generation brings relevant external knowledge into the current request. That knowledge may come from product documentation, support cases, or policy records. Retrieval can use keyword search for an exact identifier, vector search for a paraphrased request, SQL for current structured facts, or a hybrid route when measurement shows that combining signals helps. 

 Vector search ranks records by the distance or similarity between query and stored embeddings. That ranking is useful, but it doesn’t prove a record is current, authoritative, complete, or permitted for the caller. The retrieval path still needs source identifiers, versions, effective dates, metadata filters, tenant scope, and lifecycle rules. A semantically similar paragraph from an expired policy is still the wrong evidence. 

 RAG should not replace agent memory. A support manual is external knowledge, a workflow decision is application state, and a user preference may be durable memory. All can be searched with vectors, but their owners, access scopes, and update rules differ.  

 Define the roles of LangGraph and LangChain 

 Frameworks make the application easier to compose, but they do not remove the need for boundaries. LangGraph is useful for representing a stateful workflow with nodes, transitions, checkpoints, and human approval points. LangChain provides abstractions for models, retrievers, tools, document processing, and application-side orchestration. Both can participate in a durable agent, but neither should be treated as the system of record for business data or as the final permission boundary. 

 “Frameworks make the application easier to compose, but they do not remove the need for boundaries. Clear ownership determines where to investigate a failure and which layer should enforce the fix.” 

 That division also makes troubleshooting more straightforward. If a workflow resumed from the wrong node, inspect the checkpoint. If the agent recalled an obsolete preference, inspect the memory lifecycle and its validity metadata. If the answer cited the wrong manual, inspect the retrieval query, source version, and filters. Frameworks provide the building blocks. Clear ownership determines where to investigate a failure and which layer should enforce the fix. 

 Design recovery alongside the primary workflow 

 An agent’s first demonstration usually follows the successful path: the model receives context, calls a tool, and returns an answer. A durable design also defines what happens when execution is interrupted, context conflicts, or evidence is missing.  

 If a tool fails after a checkpoint, can the workflow resume without repeating a non-idempotent action? 

 If a memory changes, can the application identify the older record and mark it as superseded? 

 If a document is deleted or a tenant boundary changes, will retrieval exclude it before the model sees it? 

 If the required evidence is missing, does the agent ask for clarification or state that it cannot verify the answer? 

 If the final answer is wrong, can the team tell whether the failure came from checkpoint state, memory selection, retrieval, context assembly, or generation? 

 These questions determine what to trace: workflow identifiers, selected memory and source records, versions, scopes, retrieval routes, tool calls, permissions, and responses. Evidence should show how the system produced a response.  

 Start with the boundaries, not the vector store 

 A practical starting point is small. Choose one workflow that needs to survive a restart or continue across sessions. Define the state required to resume it. Define the few facts that should become durable memory. Identify the external documents or records that belong in RAG, including their source and scope. Then test the three paths independently before combining them in the agent loop. 

 Choose retrieval methods to fit the information. Use structured queries for structured facts. Use vector or hybrid search when the question depends on meaning, wording, or related passages. Add memory promotion only when the application has a clear reason to retain something. Keep a correction and deletion path from the beginning so retained information stays accurate and useful as the system grows.  

 An operable system should make three questions easy to answer:  

 Where did the workflow stop?  

 What does the application remember?  

 Which external evidence supports this response?  

 LangGraph and LangChain can help implement the paths. A database with appropriate data access controls can store and retrieve related records, while the application manages their distinct lifecycles and access requirements.  

 To try this architecture with Oracle AI Database Free , start with one workflow and test its checkpoint, memory, and retrieval paths independently. Use the Oracle AI Developer Hub for examples to adapt and the LangGraph and LangChain integrations documentation for implementation guidance. 
 The post Your AI agent’s “memory problem” may be something else appeared first on The New Stack .
