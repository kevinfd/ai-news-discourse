---
id: "14b67dddb8073b5b"
title: "Will AI Coding Eat Video Game Engines?"
url: "https://spectrum.ieee.org/epic-games-unreal-engine-ai"
link: "https://spectrum.ieee.org/epic-games-unreal-engine-ai"
source: "IEEE Spectrum"
domain: "spectrum.ieee.org"
source_type: "tech_press"
collector: "rss"
date: "2026-11-18T12:00:03Z"
published_date: "2026-11-18"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Matthew S. Smith"]
language: "en"
summary: "When Travis McGeathy’s studio, Seeker Entertainment, ran out of funding in September, its game KinForge went down with it. KinForge was an online game built in Unreal Engine 5.7 and designed to run on servers hosted by Amazon Web Services (AWS). With no one left to pay the server bill, the game became unplayable even for those few developers, including studio co-founder McGeathy, who had the…"
tags: ["Unreal-engine", "Epic-games", "Vibe-coding", "Artificial-intelligence", "Video-games"]
orgs: ["Anthropic", "Amazon"]
topics: ["agents & coding", "models & research", "business & funding", "policy & regulation"]
content_source: "fulltext"
word_count: 1320
paywalled: false
image: "https://spectrum.ieee.org/media-library/a-game-development-software-being-used-to-generate-and-refine-images-videos-and-3d-models-of-an-1800s-saloon-setting-for-a-vi.jpg?id=68705132&width=980"
discussion_url: null
score: null
comments: null
community: null
---

# Will AI Coding Eat Video Game Engines?

IEEE Spectrum · Matthew S. Smith · 2026-11-18

When Travis McGeathy’s studio, Seeker Entertainment, ran out of funding in September, its game KinForge went down with it. KinForge was an online game built in Unreal Engine 5.7 and designed to run on servers hosted by Amazon Web Services (AWS). With no one left to pay the server bill, the game became unplayable even for those few developers, including studio co-founder McGeathy, who had the code.
Then, on a whim, McGeathy pointed Anthropic’s Claude Code at the project and asked it to make KinForge playable without AWS. After four hours of mostly hands-off work he had a build that let players host their own games. Claude added support for peer-to-peer play over both the Internet and a local area network. To McGeathy’s surprise, it also added persistent save states, a feature that lets players resume a game if they’re disconnected.
Although KinForge is still built in Unreal Engine, developments like this could give companies that create game engines cause for concern. The conversion was accomplished with an agentic AI workflow that partially bypasses the elaborate, user-friendly game engine UI that many companies, including Unreal Engine creator Epic Games, have spent decades perfecting. Anthropic’s Fable 5.2, released November 9, further upped the ante. The model is capable of generating a 3D game with a custom game engine in the style of the hit Call of Duty series.
This raises a question: can game engines evolve quickly enough to keep pace with model improvements?
“We’re definitely in a world where I can just dream up software really fast. So, if Unreal Engine was static, what’s the value at the end of next year? This is why we are pivoting hard towards velocity,” says Daniel Vogel, chief operating officer at Epic Games. “I think with any fixed set of features or functionality, it can eventually be replicated. If we’re doing our job right, we’re pushing the engine and pushing the envelope forward.”
From Code to Nodes, and Back Again
Major game engines often offer developers new visual tools and workflows that help them build games while interacting with less code. Unreal Engine’s Blueprints, a graphically based system introduced in Unreal Engine 4 that lets designers script gameplay simply by wiring boxes together, is an example. Clair Obscur: Expedition 33, an award-winning game from French studio Sandfall Interactive, leaned heavily on Blueprints for scripting gameplay encounters.
That should have been proof of the feature’s success. Instead, Epic will remove Blueprints in Unreal Engine 6 (UE6). Why? Blame LLMs. “AI doesn’t handle Blueprints very well,” says McGeathy. “It would much rather work with the code.”
Currently, LLMs interact with Unreal Engine primarily through a Model Context Protocol server. MCP is an open-source standard created by Anthropic that lets AI send commands to software. “It’s not actually moving the mouse,” says Ryan Barker, a gameplay and systems engineer who has worked on projects for Amazon Games and Sony Online Entertainment. “It’s sending signals to the editor that the editor understands.”
UE6 will lean into that reality by moving all code to Verse, a text-based programming language that will replace both Blueprints and Unreal Engine 5’s C++ gameplay framework. UE6 will also replace Unreal’s actor framework, which is based on object-oriented programming, with Scene Graph, which resembles an entity component system. “Typically, an ECS is a lot harder to code around,” says Barker, but ECS can provide superior game performance and result in less duplicate code. An LLM can help manage the complexity.
Verse debuted in Unreal Editor for Fortnite in 2023, while Scene Graph arrived in 2024. Verse was designed to let millions of creators run code side by side in Fortnite, so it’s strict. The compiler catches mistakes before code runs and limits what each function can do. And because Scene Graph is built on Verse, an AI can work with a game world through code. That’s different from Blueprints, which are stored as binary files that LLMs can’t read directly.
In addition to these changes, UE6 will make the engine more modular and expose its systems through an application programming interface “so that AI tooling can get at them without needing to fall back to slow computer use,” says Wassmer. An internal effort that Epic calls “Python All The Things” aims to make everything in the editor scriptable. UE6 will also store more game assets as text so an LLM can edit them directly. For binary assets (non-text files) that remain, Epic is building a command-line tool that allows agents to interact with the files without loading the full UE6 interface.
The traditional Unreal Engine editor isn’t going away, but Vogel expects it will change as LLM use becomes more common. “You’re not going to move stuff visually in the editor. Those times are gone,” he says. Instead, he expects game developers will more frequently use the Unreal Engine editor to visualize “the context needed to make decisions, or make the tweaks.”
Unreal Engine 5.9 offers a glimpse at what that transition will mean in practice. Released as a developer preview on 9 November, it includes a new feature called Unreal Canvas. Vogel says it’s a collaboration feature that takes inspiration from visual workspace software like Miro. “It’s a way to make sense of the project,” says Vogel.
Why Buy an Engine When You Can Build One?
Epic Games’ goal is to keep Unreal Engine relevant in a world where AI coding tools are becoming ever-more capable. The company has the benefit of approaching the problem from a position of strength: Unreal Engine is the second most commonly used engine, after Unity Technologies’ Unity engine, and ranks first if measured by the number of games sold.
Will that be enough?
McGeathy says there can be benefits to creating an engine from scratch. “If you own the engine, you’re not reliant on a third party who could yank it out from underneath you.” However, he remains skeptical that many developers will go that route, even if AI makes it less painful. “Your goal as a game developer is to make a game. It’s not to make a game engine.”
What LLMs do change, he says, is to lower the cost of switching between game engines. McGeathy, an Unreal veteran, used Claude to start building in Godot, an open-source engine he had never touched himself. “AI made transitioning from using Unreal into Godot trivial,” he says. Barker agrees. He used an LLM to build physics test scenes in both Unreal and Godot, which let him evaluate which engine was better suited to handle a game concept.
Wassmer recognizes that AI makes it “easier [for developers using Unreal Engine] to pick up a new standard, or to convert stuff,” and says that Epic won’t attempt to block this shift. On the contrary, UE6 will remove barriers where possible. “Our explicit goal is to be able to interoperate with other ecosystems and other games,” he says.
He feels confident that, even with the aid of LLMs, building an engine from scratch carries a heavy price that most developers won’t want to pay. “You still have to burn a lot of tokens to get something of scale that is optimized and that runs across all platforms,” Wassmer says. “Would you rather spend that time and energy building something from scratch? Or would you rather use something modular, like UE6, and trim out the bits you don’t need?”
- Will the Unreal Engine 5 Realize the Metaverse’s Potential? ›
- AI Coding Assistants Are Getting Worse ›
- Why AI Isn’t Ready to Be a Real Coder ›
Matthew S. Smith is a freelance consumer technology journalist with 17 years of experience and the former Lead Reviews Editor at Digital Trends. An IEEE Spectrum Contributing Editor, he covers consumer tech with a focus on display innovations, artificial intelligence, and augmented reality. A vintage computing enthusiast, Matthew covers retro computers and computer games on his YouTube channel, Computer Gaming Yesterday.
