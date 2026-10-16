---
id: "ae304a8adfa9df05"
title: "What it takes to trust AI with real-world fixes"
url: "https://commandline.microsoft.com/ai-agent-copilot-autopilot-layered-model-production-network-incidents-on-call-engineers"
link: "https://commandline.microsoft.com/ai-agent-copilot-autopilot-layered-model-production-network-incidents-on-call-engineers"
source: "Microsoft Source"
domain: "commandline.microsoft.com"
source_type: "company_blog"
collector: "rss"
date: "2026-10-13T17:58:47Z"
published_date: "2026-10-13"
collected_at: "2026-10-14T12:07:01Z"
authors: ["sbaynes"]
language: "en"
summary: "Tags: \n\n AI Security \n\n The post What it takes to trust AI with real-world fixes appeared first on Source ."
tags: ["Company News", "AI", "Security"]
orgs: []
topics: ["agents & coding", "models & research", "safety & ethics"]
content_source: "fulltext"
word_count: 1887
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# What it takes to trust AI with real-world fixes

Microsoft Source · sbaynes · 2026-10-13

It’s 2:00 am. A pager goes off. A link somewhere in a datacenter has started flapping, a handful of alarms have correlated into one incident, and the on-call engineer is now doing what on-call engineers have always done: opening five tabs, one per system, and reconstructing what happened from fragments.
We built an AI agent to do that reconstruction. It works. It pulls the device state, reads the telemetry, correlates the recent changes, classifies the failure, and writes a clean summary into the incident before the human has finished logging in. It also knows the fix.
And that is where the demo stops being a demo.
Because the agent “knows the fix,” the question is whether the system should allow it to shut a BGP session on a device that’s carrying live customer traffic. A “read” is something you can double-check. A “write” is an action that already happened. The moment an agent can change production, every property you were relaxed about at the read stage becomes a potential source of customer impact and risk.
This post is about what we learned building an agent that’s trusted to take that action, as well as the uncomfortable conclusion we kept arriving at: There is no single thing you can build that makes an agent safe to run in production. Not a smarter model, not a stricter prompt, not a clever guardrail. Safe autonomy requires a stack.
What do we even mean by “agent”?
Ask 10 builders for a definition, and you’ll get 10 answers—and most of them are really examples (“You know, like a coding agent”) rather than definitions. That’s fine; we’re still in the relatively early days of agentic AI. But the fuzziness hides what matters here.
An agent is not the model. The model is the brilliant, non-deterministic part in the middle. The agent is the deterministic software wrapped around it—the part that decides what the model is asked, what it may do with the answer, which tools it can reach, and what happens when it is wrong. The model supplies intelligence. The agent supplies judgment about how far to trust that intelligence and what to let it touch.
Seen that way, the interesting engineering in an agentic system is usually the wrapper. And the whole safety question reframes with that distinction: Making an agent safe is less about a smarter model in the middle and more about a better deterministic shell around it.
Concretely, the harness we wrap around the model during execution is a mostly-deterministic workflow with a few narrow, schema-checked model steps inside it. It is what turns “the model worked something out once” into “these steps run the same way every time.” You don’t need its full mechanics yet—that’s another layer. For now, just hold the picture: a deterministic workflow with the model kept on a short leash inside it.
Harness, agent, orchestrator, playbook, call it what you like. The load-bearing idea is the same: deterministic software putting a non-deterministic model to work, on purpose, within limits.
Authorization over intelligence
The “holy grail” of agentic development is an agent that can investigate a problem, work out a fix, and carry it out without a human directing every step. But getting there in production means building safety into each step. More autonomy should not mean fewer controls.
Imagine giving that agent a service account with broad access, a shell that can run anything, and a stern system prompt listing everything it must never do. It might have everything it needs to fix the problem. But what actually prevents it from taking an action it shouldn’t take?
A broadly privileged service account can give the agent more access than the person who invoked it. An unrestricted shell can put anything that account and machine can reach within the impact radius. A system prompt helps guide behavior, but it can’t enforce permissions. The model can misinterpret an instruction or be influenced by malicious text in a log or tool response. Production safety can’t depend on instructions to the model alone.
The hard part of autonomy is authorization, not intelligence. Modern models are frighteningly good at figuring out the fix. The real question is: “What is this thing allowed to do, under whose identity, through what interface, and with whose sign off?” It’s boring, it’s deterministic, and it’s the whole game.
The mental model: Four boundaries, layered
Once we started stacking boundaries, the architecture fell into four layers. Each answers a different question. None of them are sufficient alone, and that’s the point.
Read bottom to top, it’s defense in depth across identity, tool, mutation, and time. Read as a sentence: The agent acts only as the human who summoned it (identity), reaches production only through a controlled interface (tool), can read freely but must pause before it changes anything (mutation), and gets less reliant on live reasoning the more it runs (time). Two of these are security controls in the literal sense: identity and tool access are where an attacker or a hallucination does its damage, so that’s where the hardest walls go.
Layer 1: The agent never has more access than you
The agent doesn’t get its own powerful account. It acts on behalf of the human who invoked it, bounded by that person’s real permissions. Where a service identity is unavoidable, it gets the narrower of the two. Identity is compound: the human plus the agent, and the stricter one wins. Access policies are owned by the teams that own each tool, defined per tool, and changed through a normal pull request (PR) with the tool team as a required reviewer. Merging a PR grants access; reverting it revokes access.
Layer 2: One tool interface, not a bare shell
The agent never gets a bare shell. Every capability it has sits behind a single typed tool interface, each tool is individually authorized, and each call is structured and logged. Note the careful wording: The enemy is not the command line; it is the unbounded one. A raw shell cannot be governed, because you cannot put a permission boundary, a schema, or a clean audit trail around bash. But a command line invoked as one narrow, declared tool, behind the interface, is fine.
This is why the framing of “MCP vs. CLI” is a false dichotomy. You want both, chosen by trust level. Put everything behind the tool interface, then pick the implementation per call: a plain function or a sandboxed CLI for low-risk local work inside the trust boundary, and MCP for anything that crosses it, because MCP gives you least privilege, credential isolation, structured audit, human approval hooks, and rate limiting for free. You can secure a CLI, too, but only by paying for per-user sandboxes with tightly limited access, and even then, you can’t match per-tool granularity.
Layer 3: Read freely, pause before you write
Diagnostics run on their own. Anything that mutates production stops and waits for a human. This sounds obvious and is surprisingly hard to enforce, because the temptation is to let “safe-looking” writes through. We do not. The gate is code in the execution engine, not a line in a prompt, and trust to skip it is earned per procedure and per action type—never granted to a model because the model is smart.
Layer 4: The agent that learns to stop being an agent
The first time we see an incident, the agent reasons through it end to end, which is expensive and non-deterministic. But most incidents aren’t novel. When the same reasoning path succeeds enough times, we crystallize it into a deterministic playbook that runs with zero model calls. The agent becomes a discovery mechanism for new problems, not a permanent tax on old ones. Less live reasoning means lower cost, higher reproducibility, and a smaller surface for both hallucination and attack, all at once.
Why one layer is never enough
Let me make this concrete with the incident from the top, because it shows where a single control would have failed.
The agent gets show interface status back from a device. That output is unstructured text, and this is the kind of work a language model is good at, so we let it parse. But we don’t let it decide. The output of the model is constrained to a schema, validated, and only then handed to ordinary deterministic code that chooses the action:
# errdisabled- recovery.yaml  (excerpt) 
steps: 
  - id: parse-status 
    type: ai-extract          # LLM parses unstructured CLI output into typed JSON 
    prompt: "Extract interface, status, vlan from the CLI output." 
    schema: 
      interface: string 
      status: enum[connected, errdisabled, notconnect] 
      vlan: int 
 
  - id: validate 
    type: assert              # deterministic: reject anything off-schema 
    rule: "status in [connected, errdisabled, notconnect]" 
 
  - id: decide 
    type: condition           # deterministic: no model in the decision 
    when: "status == 'errdisabled'" 
    then: recover-interface   # a WRITE step -> pauses for human approval 
    else: no-action 
This is the pattern we call deterministic skeleton, probabilistic filling. The language model is the semantic parser. It is never the decision-maker, and it never holds the credential that executes the change.
Now watch what happens on a harder request. Ask the same system to generate a BGP configuration for a new device, and it will produce something that looks completely correct. It will also, often enough to matter, invent an ASN, reference a route policy that doesn’t exist, or quietly miss a datacenter-specific convention that no amount of prompting reliably teaches. Config generation is novel synthesis, which is the least reliable thing a model does, and it’s also the most risky, because the output goes near production.
So, walk the counterfactual, one layer at a time.
- Remove identity and the agent runs with “god-mode” credentials. The hallucinated config gets pushed with authority no human on that call actually had.
- Remove the tool interface and give it a bare shell, and there is no way to even name “pushing a BGP config” as a distinct, authorizable, auditable action. It’s just another command, with nowhere to attach RBAC or an approval gate.
- Remove the mutation gate and the invented ASN reaches the device, because the config looked fine and nothing stopped to ask.
- Remove time / crystallization and you pay full, non-deterministic reasoning cost on every routine incident forever, which means you’re running the riskiest execution mode even for problems you solved months ago.
Each removal breaks the system, and each one breaks it differently. There’s no single point you can harden to cover all four. That is what defense in depth actually means, and it’s why the product is the stack and not any one layer.
There’s a growing consensus in this space that policy is something the runtime must enforce, rather than something you ask a model to honor. We pointed that instinct at physical infrastructure. The difference here is that when our runtime is wrong, the impact radius isn’t a bad pull request. It’s customer traffic, and that is unacceptable.
The takeaway
If you’re trying to move a team from copilot to autopilot, the most useful thing I can tell you is to stop looking for the safeguard. There isn’t one. Pick the four boundaries, or your own equivalent set, and build them as separate, deterministic layers that each fail closed. Then let the model be brilliant inside them.
The stack is the autopilot.
