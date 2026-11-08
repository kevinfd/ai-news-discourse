---
id: "b7d6d772858e7482"
title: "Claude Won't Clone Games Anymore. I Spent a Weekend Finding Out What It Will Do"
url: "https://pcmag.com/opinions/claude-wont-clone-games-anymore-i-spent-a-weekend-finding-out-what-it-will"
link: "https://pcmag.com/opinions/claude-wont-clone-games-anymore-i-spent-a-weekend-finding-out-what-it-will"
source: "PCMag"
domain: "pcmag.com"
source_type: "tech_press"
collector: "rss"
date: "2026-11-07T15:00:00Z"
published_date: "2026-11-07"
collected_at: "2026-11-08T13:03:58Z"
authors: ["Ruben Circelli"]
language: "en"
summary: "Anthropic's new rule on recreating games has people worried about reverse engineering, but I've found the restrictions to be narrow and easy to work around."
tags: []
orgs: ["Anthropic", "OpenAI"]
topics: ["products & launches", "policy & regulation", "models & research"]
content_source: "fulltext"
word_count: 1668
paywalled: false
image: null
discussion_url: null
score: null
comments: null
community: null
---

# Claude Won't Clone Games Anymore. I Spent a Weekend Finding Out What It Will Do

PCMag · Ruben Circelli · 2026-11-07

Since the launch of Anthropic’s Opus 5.5 model, vibe-coders have been extremely busy with software personalization projects. I made a Windows utility for multi-monitor users, but others have been more ambitious. ArtCraft’s Brandon Thomas, for example, made a full-fledged clone of Adobe Photoshop. Meanwhile, other folks are using AI to clone games and inundate Steam with AI slop.
That last group is where Anthropic is now drawing the line. The company recently updated Claude to stop it from recreating existing games, and the headlines made it sound like a crackdown on reverse engineering. So I spent a weekend decompiling games and making mods with Claude to see what's actually off-limits. Here's what changed, what still works, and why the new rule won't stop reverse engineering.
What Anthropic Actually Changed
According to Addy Osmani, a member of technical staff at Anthropic, the company recently added two sentences to the rules for Opus 5.5: “Do build original games, games in a genre, and games from the user’s own designs and assets. Don’t build a recreation of a specific existing game, even if it is renamed or called original.”
    
        This Tweet is currently unavailable. It might be loading or has been removed.
    
The idea here, said Osmani, is to “steer [Claude] away from recreating someone else's specific game because using Claude to infringe IP is against [Anthropic’s] usage policy.” However, “Original games, genre games, and games built from your own designs and assets are meant to keep working.”
Modding and Reverse Engineering Still Work
As of now, I can still use Claude (including Opus 5.5) to decompile or reverse engineer. For example, after the Claude policy change, I decompiled Valheim’s latest update and several mods to figure out how they work, in service of developing new mods, maintaining existing ones I created, and continuing work on an achievement-tracker utility that reads progress directly from decompiled game code.
You can still ask Claude for help on such projects. For example, I asked Claude whether it could help me reverse-engineer a game, and it said yes, pending some specifics. The same goes for decompiling games to port them to PC, which, again, Claude tells me it has no problem doing. Even for a demo of an unreleased game, Claude is perfectly happy to break it down into its most basic building blocks for modding or porting purposes.
This isn’t surprising, given the language of the aforementioned policy announcement. Anthropic isn’t particularly concerned if you want to use its models to breathe new life into an old game locked to a proprietary platform or create a mod, which the rule doesn’t mention. However, that’s not to say there aren’t very real restrictions on what you can do now.
Clones Are Off the Table, and So Are Some Things That Shouldn't Be
It’s one thing to use Claude as a tool to change how an existing app works, but it now refuses to make unapologetic copies of apps and games. Above, I mentioned Claude’s willingness to decompile and reverse-engineer games, including unreleased ones. However, if I ask Claude to do any of that in service of copying a game, it won't. Even if you don’t plan to reuse any of a game’s assets or code, Claude still declines to help, citing copyright issues and service agreement violations.
It treats software the same way. You can still use Claude to modify apps, but it’s no longer as willing to help you copy it. It doesn’t matter if you pitch Claude on a decompilation project in which you plan to make a new version of something with freshly generated assets and code. This is a big shift from how Claude used to work. ArtCraft’s Brandon Thomas, for example, relied on Claude during the development of PhotoCraft, his AI clone of Adobe Photoshop.
Like with the overly censorial guardrails Fable came back with after its original ban, these new restrictions are causing collateral damage. Many are reporting problems with Claude now refusing to do tasks it did before and that don’t seem to violate its new rules. For example, one user describes trying to create a digital version of a board game for personal use, which Claude refused to help with courtesy of its amended directives.
All of this is to say that you might run into issues with Claude when you try to do things it should support. With Fable, Anthropic dialed down its aggressive censorship significantly over time, so it wouldn't shock me if something similar happens with Claude. In the meantime, you can take advantage of some workarounds.
You Can Still Force Claude to Do What You Want
The simplest workaround to Claude's new restrictions is careful prompt engineering. Rather than draft a comprehensive plan with Claude to deconstruct, for example, how Adobe Photoshop works to build a better version of it, you can send smaller, more narrowly scoped tasks. You might be able to trick the AI model into doing work it wouldn’t otherwise by limiting how much information about your larger goals you share.
Alternatively, you can try more sophisticated workarounds. ArtCraft, for example, has a new app called Craft Anything, which lets you “see how any website, app or game works, then have AI build your own version,” all while still relying on Anthropic’s tech. You can use Craft Anything to make your own versions of existing software by letting an AI model look at its code first, or you can opt for a ‘clean room’ approach in which you provide only visual points of reference. Keep in mind that Craft Anything is still very much in active development, so expect bugs and limitations.
If you aren’t married to the idea of using Anthropic’s models, competitors haven't announced similar restrictions. In testing, OpenAI's GPT-6 Astra model had no problem helping me decompile, reverse engineer, and clone games, including upcoming ones with only demos available. It was even willing to dive into Adobe Acrobat’s code to help me create a brand-new PDF reader that does everything Adobe’s app does, albeit without reusing assets or code.
Other models will likely be able to do all of this soon, too. Chinese models, such as DeepSeek, currently lag behind the frontier ones in terms of performance, but they historically haven't had qualms about taking on just about any task, assuming you don’t ask them what happened at Tiananmen Square. So, although Opus 5.5 might be the model of choice right now for vibe-coders, in six months you might very well get the same level of performance from run-of-the-mill models.
Why I Think Anthropic Got This Rule Right
Although Claude’s new restrictions aren’t perfect, I appreciate what they're trying to accomplish, and I think you should, too, assuming Anthropic eventually addresses the unintended consequences.
When it comes to software (what I see as digital tools packaged as apps), however, I’m just not convinced that companies should have exclusive rights to functionality. Sure, the actual lines of code that collectively comprise Photoshop, for example, ought to belong to Adobe. But if Photoshop’s features can be recreated using different assets and code, I don’t have any moral or ethical qualms about doing so.
Games are a completely different story. Whether they're derivative or wholly unique, good or bad, video games are art. Maybe the line between artistic work and product is blurrier in video games than in a painting or another creative medium that relies less on technology. But just because it’s sometimes hard to make a distinction doesn’t mean there isn’t one.
A digital tool is, by definition, the sum of its parts. It's a collection of features sold at a certain price that work well or don’t. Video games are more than the sum of their parts. The human labor behind making each artistic decision that underpins a game’s direction is worth protecting from an unfeeling machine ingesting code and spitting back out a recreation.
And, no, this isn’t to say people shouldn’t steal ideas from other games. It's not even to say that you shouldn’t be able to use an AI model to understand how a particular system in a game was coded to try and add that system to your game. However, I'd argue that it means you shouldn’t, as Anthropic says, “build a recreation of a specific existing game, even if it is renamed or called original.”
This commandment goes beyond AI, too. I'd also argue that you shouldn’t make asset-flip games. For example, Stardew Valley might be a clone of the Harvest Moon series in the sense that it copies its gameplay loop and larger structure, but it’s a gorgeous, loving modernization of that formula. On the other hand, I wouldn’t support anybody buying a bunch of premade assets off a storefront, slapping together an exact replica of a Harvest Moon game, and trying to siphon some cash from the hard work of others. That's lame.
Most People Won't Notice a Difference
For most people, Claude's new rule won’t change much. If you're modding games, porting old ones, reverse engineering how a system works, or building your own original project, Claude is still happy to help. The real exceptions are straight-up clones and the occasional innocent project that gets caught in the crossfire, like a personal board game adaptation.
If you do want to clone a game, I'm not a cop or your parent. I think you shouldn't, but plenty of other tools and models will help you anyway. And if Anthropic's handling of Fable is any indication, Claude's overzealous refusals will likely ease up over time. Either way, using AI to build and remake software isn’t going anywhere.
About Our Expert
I’ve been writing about consumer technology and video games for over a decade at a variety of publications, including Destructoid, GamesRadar+, Lifewire, PCGamesN, Trusted Reviews, and What Hi-Fi?, among many others. At PCMag, I review AI and productivity software—everything from chatbots to to-do list apps. In my free time, I’m likely cooking something, playing a game, or tinkering with my computer.
