---
id: "b5b08cc7cfaae666"
title: "\"It runs Doom\" is more than a meme. The reason lies in its engineering"
url: "https://scientificamerican.com/article/it-runs-doom-is-more-than-a-meme-the-reason-lies-in-its-engineering"
link: "https://scientificamerican.com/article/it-runs-doom-is-more-than-a-meme-the-reason-lies-in-its-engineering"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-16T15:30:00Z"
published_date: "2026-11-16"
collected_at: "2026-11-17T13:04:11Z"
authors: ["Emma Gometz"]
language: "en"
summary: "Clever code made the classic shooter fast in 1993—it’s been easy to port and add onto ever since. Artists and scientists are still finding surprising new uses for it"
tags: []
orgs: ["Microsoft", "Intel"]
topics: ["jobs & society", "agents & coding", "health & science"]
content_source: "fulltext"
word_count: 925
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# "It runs Doom" is more than a meme. The reason lies in its engineering

Scientific American · Emma Gometz · 2026-11-16

In a building in downtown Manhattan, about 50 artists and programmers sat on the floor like kindergartners during show-and-tell, staring at a wall-sized projection of the 1993 videogame Doom. The original 1993 game is set in space and, eventually, hell and an Earth invaded by demons. The version that was seen on the wall takes place somewhere arguably scarier: an apartment in Brooklyn.
At the controls was Rae Kelly (also known as wallh4x), an artist with curly elbow-length hair and wire-frame glasses, who was walking the audience through their Doom mod, “Arlington.” Doom mods alter, or modify, the original game by changing its raw materials, such as the environmental textures or enemies, into anything the modder wants.
“There is something timeless about [Doom],” Kelly says. “It’s a really clean piece of programming that accomplishes something fundamental…, this abstract sensation of being somewhere.”
On supporting science journalism
Most 1990s video games are relics, yet Doom keeps respawning. The game’s aesthetics are iconic: a moody, rock ’n’ roll demon world that totally shreds. But much of the credit goes to that clean programming, which has allowed tinkerers to put the game on nearly any machine with a chip for more than three decades.
It was designed for the Intel 486 processor, which was state-of-the-art at the time. The developers also used a technique called binary space partitioning (BSP), which let the game sort polygons in near-to-far order from only the player’s point of view. This technique stores partially sorted polygons when rendering a frame, avoiding what would normally be repeated sorting that slows things down. Because the game’s code does that sorting in advance, when each level is rendered the game can quickly work out what to draw regardless of where the player stands. Doom was one of the first games to bring BSP to consumer hardware, and it popularized the technique for future developers.
“What made or broke a game back then was the frame rate,” says Fabien Sanglard, an independent software engineer, who wrote a book dissecting Doom’s engineering in the context of its time. “The BSP is what cracked the frame rate.”
Doom has also been easy to add to. The game’s file architecture made it so that players have been able to swap assets such as map data, sounds and characters for their own creations. That sparked a movement to build new mods of it—for gamers at home and even the U.S. Marines. In 1997 id Software, the company behind Doom, made the game’s source code open-access, so anyone could tinker with the engine itself.
And Doom will run on pretty much anything.
From the very beginning, the team designed Doom’s code to port easily to other systems, says co-creator John Romero. The developers wrote the game on Steve Jobs’s NeXTSTEP operating system, then ported it to Microsoft’s MS-DOS, which was the operating system for most personal computers at the time.
Romero and fellow cocreator John Carmack chose to write much of the game in C, a programming language that works on essentially any computer. “C is a very portable language,” Romero says. “If you’re taking damage in lava or if a switch flips and does something—all that stuff has nothing to do with the machine that’s on at all [because it’s] pure logic code.”
The only code a person needs to change when porting the game is the part that handles input and output on the new device—typically 10 percent of it, according to Sanglard. That made it easy to port and sparked the “It Runs Doom” meme, in which people show off some of the wackiest devices they’ve gotten the game to run on, such as an ATM, a flash drive, a toaster or a pregnancy test.
Scientists have joined in, designing a Doom display made of Escherichia coli in 2024 and, earlier this year, getting living human neurons—and a simulated fruit fly brain—to “play Doom.”
Georges Labrèche, an onboard machine-learning researcher for the European Space Agency’s (ESA’s) OPS-SAT Space Lab, has helped run Doom on two ESA satellites. He did it first to test machine-learning algorithms and then, this past summer, to test a new voice-command system. “It unlocked a lot of innovation,” he says.
Portability runs through Doom’s mod culture, too. Modders can choose from dozens of “source ports,” which are changed versions of the source code that fans have adapted from id’s original code.
“The source code took on a life of its own. And that was not something that id [Software] did. That was something that the community did,” Kelly says. “And the Doom community, uniquely, has been this long-standing example of how individuals can keep something alive and continue to innovate it.”
Doom’s fan base is “one of the first game communities that spread predominantly online, as opposed to in person,” Kelly adds. Whatever keeps pulling people in—the memes, the game’s design, its resurgence during the pandemic or childhood nostalgia—the community has never really logged off.
Back in Manhattan, the event was also a pop-up arcade, with several Doom mods set up on computers for attendees to try. (A nearby LaCroix station kept players hydrated.) My favorite mod had a mini art museum inside, where I viewed Pablo Picasso’s antiwar painting Guernica with a gun in my character’s hand, presumably to shoot monsters that—in this mod of the game—never came.
“Anybody can sit down and get [Doom] within, I think, the first five minutes. And then maybe they get fascinated by it,” Kelly says. “It’s as shallow as a puddle and as deep as an ocean.”
