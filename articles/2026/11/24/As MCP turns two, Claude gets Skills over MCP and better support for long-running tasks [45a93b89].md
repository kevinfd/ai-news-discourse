---
id: "45a93b8955dba9cd"
title: "As MCP turns two, Claude gets Skills over MCP and better support for long-running tasks"
url: "https://thenewstack.io/mcp-skills-tasks-claude"
link: "https://thenewstack.io/mcp-skills-tasks-claude"
source: "The New Stack"
domain: "thenewstack.io"
source_type: "tech_press"
collector: "rss"
date: "2026-11-24T18:08:34Z"
published_date: "2026-11-24"
collected_at: "2026-11-25T13:04:01Z"
authors: ["Frederic Lardinois"]
language: "en"
summary: "Anthropic on Tuesday marked the second anniversary of the Model Context Protocol (MCP) by bringing support for skills, long-running tasks, and file uploads over MCP to Claude. \n\n Skills over MCP , which lets MCP servers publish skills alongside their tools, is now available in public beta, while Tasks, which  first landed in Claude Code  as a beta in October, and Elicitation are now generally…"
tags: ["AI", "AI Agents", "Model Context Protocol (MCP)"]
orgs: ["Anthropic"]
topics: ["agents & coding", "products & launches", "models & research", "business & funding"]
content_source: "summary"
word_count: 2219
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# As MCP turns two, Claude gets Skills over MCP and better support for long-running tasks

The New Stack · Frederic Lardinois · 2026-11-24

Anthropic on Tuesday marked the second anniversary of the Model Context Protocol (MCP) by bringing support for skills, long-running tasks, and file uploads over MCP to Claude. 

 Skills over MCP , which lets MCP servers publish skills alongside their tools, is now available in public beta, while Tasks, which  first landed in Claude Code  as a beta in October, and Elicitation are now generally available. File uploads will roll out soon. 

 All three are meant to help agents work more autonomously and for longer stretches of time, which, according to the protocol’s maintainers, is also where the project focused much of its second year. In its announcement, Anthropic says these features let Claude treat an MCP server more like another agent that it can learn from and delegate work to. 

 Den Delimarsky, a lead maintainer of MCP at Anthropic, tells The New Stack, “You have long-running tasks, you have events, you have file uploads and downloads, you have skills over MCP, and all of them working together now enable a completely different spectrum of scenarios.” 

 Credit: MCP project. 

 From early adoption to agents 

 When Anthropic  first launched MCP  in November 2024, it wasn’t clear whether the protocol would pan out, says David Soria Parra, who co-created MCP at Anthropic and remains one of its lead maintainers. That first year was mostly about adoption, he says. 

 Anthropic says the MCP SDKs now see more than 700 million downloads per month (up from the  400 million it reported in July ) and that there are now more than 10,000 MCP connectors for Claude.  claude 

 It’s no secret that MCP saw an impressive adoption curve, and by its first birthday, it had become clear that there was a need for an open protocol, but also that it still had a lot of pain points, especially for companies that deployed it in production at scale. 

 In reaction to this, the MCP team released the  2026-07-28 version of the spec  earlier this year, which  removed sessions from the protocol  and made it stateless — and with that, a lot easier to run behind a standard load balancer, for example. 

 At the same time, Claude Code also kept getting more popular, and it became clear that the industry wanted agents, Soria Parra says. MCP, though, had launched without any primitives built specifically for agents. But as Soria Parra notes, that is part of the development philosophy behind MCP. 

 “MCP never tries to predict where the future goes, but tries to pick up people where they currently are, which is why we did not have agentic primitives from the very beginning, but just tools and resources,” Soria Parra tells The New Stack. 

 Anthropic’s David Soria Parra at AGNTCon+MCPCon Europe 2026. Credit: AAIF. 

 Building for autonomous agents 

 Now, however, agents are everywhere and the MCP community is reacting to that. 

 “We’ve seen in the past year the world shift from the expectation that somebody’s always in front of the keyboard to a world where agents are now autonomously doing things,” Delimarsky says. 

 When MCP first launched, for example, its authorization flow still assumed that a user would be there to always click a consent button. That’s not the case now that agents have become widely used. With the  Enterprise-Managed Authorization extension , which the MCP team worked on with Okta and others, admins can now authorize an MCP server once for all of their users. 

 The team is now also working on the Workload Authorization Grant (WAG), Delimarsky says, a standard for agents that need to access third-party services on their own. 

 Like most of the recent additions to MCP, this work didn’t start with the maintainers deciding what they wanted to build, he says: “It actually comes from real industry needs that we see shifting.” 

 Long-running tasks and Elicitation 

 Among the MCP features that are now generally available in Claude are  Tasks  and  Elicitation . Tasks allow an MCP server to start a long-running job in the background and then report back when it’s done, while Elicitation lets the server pause and ask the user for input. 

 Developers have been asking for a way to handle these long-running operations for quite a while, Soria Parra says. “People effectively use MCP servers not just to provide tools that are singular actions, but effectively expose full-on agents.” 

 Credit: Anthropic. 

 This means a developer in Claude Code could, for example, ask an MCP server to investigate a failing CI run. The agent on the other side might then work on this for a few hours, and once it’s done, the chat session pops back open with the answer. 

 That’s also closer to how people tend to work with each other, Soria Parra argues, since they usually kick something off and then wait for the work to get done “rather than just always sitting there and interacting with something.” 

 Quite a few companies already use Tasks internally, where they control their own harnesses, he says, and he expects that usage will pick up now that Claude supports the feature. ZoomInfo, for example, uses Tasks for account and contact research jobs that previously took users several prompts, Anthropic says. 

 Servers will mostly use Elicitation to get a user’s approval, through a form or a link, before they do something that costs money or can’t easily be undone. Supabase, for example, now confirms the cost with the user before it creates a paid project, while GitHub asks users to type in a repository’s name before an agent can delete it. 

 Both features are now generally available in Claude and Claude Code for users on Anthropic’s Pro, Max, and Ultra plans and are still rolling out to Team and Enterprise users. 

 Skills over MCP 

 Skills over MCP, which became an official MCP extension in September, brings the  Agent Skills format  to MCP servers. A server can now provide not only its tools but also the instructions for how to best use them. 

 Since these skills live on the server, developers can update them whenever they update their tools, and users don’t have to install anything. Claude also only loads a skill into its context when it actually needs it. 

 Soria Parra believes this is one of the most exciting features to come to MCP in a long time. 

 “If you are a Figma MCP server, you could — and I don’t know if they do it, but you could hypothetically support a skill for designers and a skill for engineers,” he says. 

 Since many MCP servers already require users to log in, they can now also serve skills that are highly personalized for a specific user or organization. That’s something a plugin can’t do, Soria Parra says. 

 “You can totally imagine an MCP server that just generates a skill that’s only for you,” he says. 

 Credit: Anthropic. 

 Shopify, HubSpot, and Atlassian are among the first companies to offer skills through their MCP servers. Shopify’s skills, for example, walk Claude through building and updating a merchant’s online store. 

 Adding skills to an MCP server is quite easy, Soria Parra notes, but supporting them in a client like Claude Code is a bit harder. 

 “Skills are text that steers the model, and that comes with security and approval implications, and those are the difficult part,” Soria Parra says. “Reading a file over MCP and giving it to a context is the easy part. Making sure that it’s done safely and securely is a much harder piece.” 

 Skills over MCP is now available in Claude and Claude Code and turned on by default for users on the Pro, Max, and Ultra plans. Admins on the Team plan have to enable it first, and support for Enterprise plans is coming soon. 

 It’s worth noting that Anthropic isn’t the only company working on this, though. The extension is also already available in preview in Microsoft’s Foundry. 

 File uploads are coming soon 

 File uploads remain the most experimental of these new features. 

 In Claude and Claude Code, they’ll roll out soon to users on the Pro, Max, and Ultra plans (and eligible Team and Enterprise plans), and at first, they’ll only work with the MCP servers from Intuit and Dropbox. 

 The MCP extension itself is also still a draft that Delimarsky and Google’s Wil St. Charles  first published earlier this month . 

 It was already possible to send files to an MCP server before, Delimarsky says, but that was “a little hacky” because it involved encoding the file in base64 and embedding it in a tool call. That doesn’t work for the large audio and video files that some of his favorite MCP servers handle. 

 “I can’t rely on base64 and loading a 1.2 gigabyte file,” he says. 

 With the new extension, the file never passes through the model’s context. Instead, the server provides an upload target (typically a pre-signed URL) and the client then sends the file there directly over HTTPS. 

 The team built this on top of existing HTTP conventions because it’s “trying not to reinvent the wheel unless we absolutely have to,” Delimarsky says. The protocol also doesn’t set any limits on file sizes (though servers can set their own). 

 “We inherently did not bake any limits because we don’t know,” he says. 

 Extensions as a testing ground 

 All three of these features are extensions to MCP and not part of the core protocol. That also means they aren’t specific to Claude, and Anthropic notes that a server that supports them will work in any other compatible client, too. 

 That’s very much by design, Delimarsky says and he credits Soria Parra with the idea that “adding things is easy, removing them is very hard.” With so many MCP clients and servers now in production, removing a feature from the core protocol and breaking those servers is “just not acceptable anymore,” he says. 

 Extensions give the team a way to try new ideas with partners first. Some of them could later become part of the core protocol, but others, like  MCP Apps , will always remain extensions because not every client can support them. 

 “You need an HTML rendering interface, so terminals are out,” Soria Parra says. 

 The team has some experience with features that didn’t take off. Soria Parra says he was a big proponent of sampling, for example, which allowed MCP servers to use the client’s model for inference. 

 “It turns out people really don’t want that for a variety of reasons,” he says. 

 The July spec  deprecated sampling  (though it will keep working for at least another 12 months), and Soria Parra notes that prompts, another early MCP feature, have mostly fallen out of use as well. 

 MCP’s popularity also means that the maintainers now get a lot of proposals for new features. “Everybody wants to fit their tiny little use case in and comes with proposals exactly perfect for that, and it’s a selection choice,” Soria Parra says. 

 The  core maintainers , who work at Anthropic, Microsoft, Google, OpenAI, and Amazon, have been good at picking the features that the major harnesses then adopt, he belives. He does acknowledge, though, that the group has been “a bit slow” to finalize the  Events extension , for example, which lets MCP servers notify an agent when something happens. 

 Both Delimarsky and Soria Parra stressed that all of this work happens in public working groups. The file uploads group, for example, was led by Delimarsky and two Google engineers, with others from Microsoft and Dropbox (which will be one of the launch partners for the feature in Claude) also participating. 

 Anthropic  donated MCP  to the Linux Foundation’s Agentic AI Foundation (AAIF) last December. Soria Parra says little has changed in how the project is steered since then, but that the neutral governance has helped with adoption. 

 Angie Jones, the foundation’s vice president, says in a statement that she has “watched independent developers and engineers from competing companies bring real problems back to the project and solve them together.” 

 What’s next for MCP 

 As for what’s next, Soria Parra stresses that the team isn’t trying to predict where things are going. Streaming is on the list, as are voice and other modalities, but the general idea is to keep “carefully observing what the industry is doing” and then standardize that. 

 The team will likely also add better support for what Anthropic calls programmatic tool calling (and what others often call “code mode”), where an agent writes code that calls its tools and doesn’t have to call them one at a time. That idea has been around for more than a year and a half, Soria Parra notes, but it’s only now becoming widely known. 

 “Things are moving fast, but they are also at the same time slower than you expect,” he says. 

 Delimarsky expects that real-world usage will shape the new extensions, too. Events, for example, supports push, poll, and webhook delivery. “We don’t know which one of these three would be the most popular,” he says. 

 Soria Parra notes that while the major harnesses continue to invest in MCP, they’re picky about which features they support. It remains to be seen how quickly clients beyond Claude will pick up these new extensions. 
 The post As MCP turns two, Claude gets Skills over MCP and better support for long-running tasks appeared first on The New Stack .
