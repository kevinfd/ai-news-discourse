---
id: "c18347e85914f56f"
title: "AI agents need to be replaceable – without losing your work"
url: "https://thenewstack.io/durable-ai-agent-operations"
link: "https://thenewstack.io/durable-ai-agent-operations"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-28T13:00:00Z"
published_date: "2026-10-28"
collected_at: "2026-10-29T12:05:29Z"
authors: ["Manveer Chawla"]
language: "en"
summary: "An agent receives approval to process a partial refund. It sends the request to a payment API, and the process crashes. Maybe the payment service completed the refund. Maybe the request never went through. A replacement agent spins up and finds an operation record marked dispatched with no outcome written. \n\n This kind of ambiguity isn’t unique to agents. Any distributed worker crashing…"
tags: ["AI Agents", "AI Engineering", "Backend development", "sponsor-clickhouse", "sponsored-post-contributed"]
orgs: ["Amazon"]
topics: ["agents & coding", "models & research", "jobs & society"]
content_source: "fulltext"
word_count: 1171
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# AI agents need to be replaceable – without losing your work

The New Stack · Manveer Chawla · 2026-10-28

AI agents need to be replaceable – without losing your work
An agent receives approval to process a partial refund. It sends the request to a payment API, and the process crashes. Maybe the payment service completed the refund. Maybe the request never went through. A replacement agent spins up and finds an operation record marked dispatched with no outcome written.
This kind of ambiguity isn’t unique to agents. Any distributed worker crashing mid-mutation faces the same problem. But a conventional worker resumes a predetermined workflow from the last checkpoint. An agent does something more dangerous: it reasons on its own. Given the same customer request and no outcome record, it might come up with a different plan, pick different parameters, or decide to issue a new refund instead of continuing the one already approved.
“An agent does something more dangerous: it reasons on its own.”
If the original refund went through, a second attempt refunds the customer twice. The charge still has enough remaining balance to cover another partial refund, so nothing stops it.
The replacement must inherit the original operation, not reinterpret it.
The operation must outlive the agent
An agent’s process, its in-memory variables, its transient reasoning context: all disposable. The business operation is not. The refund, its approval, its parameters, its current status. A long-running agent can preserve useful state for as long as it runs. The requirement: no essential operation should depend on the original execution surviving.
Before dispatching the refund, the application commits a durable operation record to a transactional store. That record includes the approved amount, the applicable authorization, the idempotency key the application sends to the payment provider, the application’s operation identifier in the provider’s metadata, and a status.
“An agent’s process, its in-memory variables, its transient reasoning context: all disposable. The business operation is not.”
The status moves from created to dispatched as the request leaves, and to confirmed or failed only on a provider response. If the agent crashes, the replacement retrieves this record and its correlation identifiers. A record stuck in dispatched indicates a call was attempted, but the outcome was never written.
The replacement inherits the approved operation rather than regenerating it.
When the replacement needs to verify the outcome, it can list refunds against the original charge and match the operation identifier in the returned metadata.
But the durable record isn’t just context for the replacement. The application enforces it at the tool boundary: the dispatch layer validates every outbound request against the committed record. The agent can propose a next step, but only authorized operations with their original parameters and identity reach the provider. The model can’t redefine what was approved.
ClickHouse Managed Postgres holds the business data, including the authoritative operation record that defines what the replacement is allowed to do. Native CDC replicates that data into ClickHouse. Application telemetry ships to ClickStack and agent traces to Langfuse, both configured to use the same ClickHouse service as their backend database.
Because business data, application telemetry, and agent traces land in one database, tying an operation to the agent run that dispatched it and the failed HTTP call is a single-identifier query. Not a reconciliation across three tools.
Two conditions. The application has to propagate that identifier. The operation ID must appear in the Postgres row, in the Langfuse trace attributes, and in the service’s log context, because nothing correlates it for you. And the replacement reads the record from Postgres, not from the replicated copy. CDC runs with seconds of latency. The authoritative row is the one the tool boundary enforces.
Restarting execution isn’t safely resuming work
Durable execution frameworks like LangGraph and Temporal record execution progress and resume after a failure. Both recommend making side effects idempotent, because resuming doesn’t resolve one. If the refund completed while the step was still pending, the framework can restart the agent, but it can’t tell the replacement whether the payment provider committed the original request.
The durable operation record implements that idempotency guidance for an agent whose next step isn’t predetermined.
The idempotency key from the durable record connects the replacement to the original request. If the replacement retries with the same key, the provider can recognize the same operation rather than processing an independent refund. This holds even if the original agent’s in-flight request completed after the crash, or a worker assumed dead has resumed. AWS’s Builders’ Library formalizes this pattern: a caller-provided identifier recorded atomically with the mutation.
But retrying isn’t always safe. The outcome might stay unclear. Stripe documents that a 500 response on a mutation can still produce external effects. When the outcome is unknown, the replacement needs evidence to investigate.
Langfuse can show the previous agent’s tool invocation: a refund request dispatched with the recorded idempotency key. ClickStack can fill in the operational side: an outbound HTTP request to the payment service followed by a connection failure, narrowing the failure window.
Both are available to the replacement directly. The Langfuse MCP server lets it query the previous agent’s trace by operation ID, and the ClickStack MCP server lets it search service events in the same window. Give the replacement the read tools only. It can narrow down what happened, but the tool boundary still controls what the replacement can do.
Neither trace proves the provider committed the refund. And an absent trace doesn’t prove the request was never sent, since Langfuse transmits traces asynchronously and a crash can prevent delivery. The payment provider remains the system of record for the external outcome. Execution telemetry narrows the investigation. It doesn’t replace authoritative confirmation.
Continue the work; don’t start over
The replacement has the durable record and, where the outcome was unclear, the execution evidence. Now it needs to act, but not by re-deciding what to do.
The replacement follows the recovery protocol the application defines, not its own judgment about the customer’s situation.
If the provider confirms the refund is complete, the replacement records the outcome and moves on. If the provider shows the refund is still pending or in progress, the replacement waits. Retrying would risk a duplicate. If the refund definitively failed with no external effect, the replacement revalidates preconditions before a new authorized attempt. If the outcome remains unclear, it escalates rather than guessing. A missing provider record doesn’t prove the refund was never processed. The provider may not have finalized the transaction.
“A stored approval is historical evidence, not current authority to act.”
Even after establishing the external outcome, the replacement has to verify that the world hasn’t changed. The refundable balance may have shifted. A human representative might have processed a separate refund through a different interface. The customer’s account status may have changed. Someone may have revoked the original authorization.
A stored approval is historical evidence, not current authority to act.
The real engineering question is whether a new agent can establish the work’s current objective, outstanding obligations, and uncertain effects, then continue safely without treating the predecessor’s recollections as authority.
The agent is disposable. The work isn’t.
