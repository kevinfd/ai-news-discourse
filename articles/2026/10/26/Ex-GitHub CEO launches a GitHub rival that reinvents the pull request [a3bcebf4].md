---
id: "a3bcebf4a3cba8e0"
title: "Ex-GitHub CEO launches a GitHub rival that reinvents the pull request"
url: "https://thenewstack.io/entire-trails-agentic-code-review"
link: "https://thenewstack.io/entire-trails-agentic-code-review"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-10-26T17:00:00Z"
published_date: "2026-10-26"
collected_at: "2026-10-27T12:07:04Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Entire, the startup founded by former GitHub CEO Thomas Dohmke , on Monday launched its GitHub alternative that replaces the traditional pull request model with a new agentic code review system called Trails. \n\n The company has been launching parts of its platform since it announced a $60 million seed round in February. Early on, Dohmke occasionally noted he wasn’t planning to compete with…"
tags: ["AI", "AI Agents", "AI Engineering", "AI Infrastructure"]
orgs: ["OpenAI", "Anthropic", "Microsoft", "Cursor"]
topics: ["agents & coding", "products & launches", "models & research", "business & funding"]
content_source: "fulltext"
word_count: 1161
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Ex-GitHub CEO launches a GitHub rival that reinvents the pull request

The New Stack · Frederic Lardinois · 2026-10-26

Ex-GitHub CEO launches a GitHub rival that reinvents the pull request
Entire, the startup founded by former GitHub CEO Thomas Dohmke, on Monday launched its GitHub alternative that replaces the traditional pull request model with a new agentic code review system called Trails.
The company has been launching parts of its platform since it announced a $60 million seed round in February. Early on, Dohmke occasionally noted he wasn’t planning to compete with GitHub.
But with Monday’s launch, Entire is launching a full GitHub alternative, with its own twist on what a modern GitHub for the agentic era should look like.
At launch, Entire supports native hosting for private repositories. Public repositories and self-hosted Git nodes are still on the roadmap.
“It’s the moment we’ve been waiting for,” Dohmke told The New Stack last week during an interview at the Linux Foundation’s AGNTCon + MCPcon in San Jose, California. “It’s exciting for us because what we set out to do a year ago is landing now — and bringing the Git hosting and the infrastructure layer together, with sites around the world, […] and the idea of continuous integration, continuous delivery, continuous memory, and then with Trails, our reinvention of the pull request.”
“It’s exciting for us because what we set out to do a year ago is landing now.”
Entire, like other devtools startups, argues that the new bottleneck for developers isn’t writing the code — agents take care of that — but code review. Unlike some other startups in this space, the company isn’t solely focused on that. Instead, the Entire is betting that solving the code review bottleneck requires an entirely new platform.
In his keynote at AGNTCon + MCPcon, Dohmke described a review queue growing in two directions: agents producing more changes, and those changes containing more code.
“I open a pull request, and I realize I have no idea what all that code does,” he says of his previous experience using coding agents.
Right now, that platform consists of Entire’s Git-compatible server, the continuous memory feature for agents that the company originally launched with, and Trails.
From pull requests to Trails
Trails is Entire’s take on the pull request model, but instead of developers reviewing code changes manually, Trails gives them a dashboard with customizable evals scored by agents. That system may assess how risky a code change is, for example, or how much intent drift has occurred over a long LLM-driven development session.
Entire says those evals run on every push, with findings available through both its web interface and its open-source CLI. Coding agents can then use that feedback to address problems and push another revision, while the developer validates the progress.
In the end, the original request, the agent’s session history, and the resulting code all become part of the review.
GitHub already offers agentic code review through Copilot. Entire’s pitch goes beyond adding an AI reviewer to a pull request: It makes the intent behind a change and the agent’s work part of the review process alongside the code.
For Entire, the idea here is that if the evals come back green, it’s ok to merge the code without a detailed human review (though few human code reviews are probably as detailed as they should be).
By default, Entire provides preset review agents, but developers can also define their own configurations in a JSON file and choose among supported Claude and OpenAI models.
“We’re redefining how the developer lifecycle works, and it’s really cool. I’ve been at home in the evenings, sitting on my couch, and texting my agents — all the while getting links from my team to their Trails on Slack and opening them.”
“We’re redefining how the developer lifecycle works, and it’s really cool,” Dohmke says. “I’ve been at home in the evenings, sitting on my couch, and texting my agents — all the while getting links from my team to their Trails on Slack and opening them. And because the user interface is designed for seeing — we’re calling it the head-up display for the pilots– so I look at my head-up display, and I see the ‘stop cop,’ one of the evals that we have internally, and if that’s green and the confidence is high, then we’re merging it.”
Entire is also partnering with Buildkite and Depot for CI. Developers can convert their existing GitHub Actions workflows using Buildkite’s bk pipeline or Depot CI, then connect the repository in Entire.
A faster, distributed Git forge
While Trails is the headline news here, Entire’s core is its Git-compatible distributed source control server, which debuted earlier this summer.
Entire says it can push up to 89x faster than GitHub and 6x faster than Cursor’s Origin.
But while a distributed system with mirrors across geographic regions helps, the key feature for many corporate users may be that Entire was built from the outset to offer private repositories in specific regions, too. Given today’s data governance landscape, that’s an increasingly important feature.
The available regions include the U.S., Europe, India, and Australia. Dohmke says customers choose a primary region and can add mirrors elsewhere, with Entire handling synchronization between them.
Memory for agents
Continuous Memory is Entire’s third pillar. It syncs AI agent sessions into a project’s repository and makes that available to the agents for future use.
For Dohmke, those sessions also preserve the approaches a developer rejected and the moments when they told an agent that working code still wasn’t what they wanted.
The company says the system combines a codebase graph that helps agents find relevant code with an “agentic brain” that turns previous sessions and prompts into memories they can query. That lets agents retrieve earlier decisions and the context behind them when they start another task.
Dohmke expects agent run costs to become the next bottleneck, with teams paying closer attention to token efficiency alongside engineering productivity. He argues that developers may find it’s cheaper to use an existing open-source project or a service like Entire than to spend tokens generating their own replacement.
The platform is free; however, Dohmke says customers pay only for the tokens the review agents consume.
But because these review agents run on LLMs, they still cost money. Right now, Dohmke says, Entire is giving all its users a $100 starter credit. Once users have run out of these credits, they will pay market rates for the model of their choosing.
The arbitrage between the discounts it can get and that market rate seems to be Entire’s current business model.
GitHub has always had very generous plans for open-source projects, and its maintainers and Dohmke hinted that the company may offer help there as well, noting that Entire is already working with some partners, including model vendors, on ideas. “More to come,” he says.
Also of note: Entire’s announcements on Monday come two days before the 2026 edition of GitHub Universe, the company’s flagship developer event in San Francisco. What timing.
