---
id: "d1d13c9ef8d169f4"
title: "Reverse Engineering, With Receipts"
url: "https://insanely.digital/reverse-engineering-with-receipts"
link: "https://insanely.digital/reverse-engineering-with-receipts"
source: "Insanely Digital"
domain: "insanely.digital"
source_type: "community"
collector: "reddit"
date: "2026-11-04T08:30:50Z"
published_date: "2026-11-04"
collected_at: "2026-11-04T13:04:06Z"
authors: ["Insanely_Digital"]
language: "en"
summary: "In our latest blog post we discuss how we use Claude Code to reverse engineer file formats from the classic Macintosh era (1980s-2000s) without reading the source code of the applications that created them. It's a fine line to walk...."
tags: ["r/ClaudeAI"]
orgs: ["UK", "Anthropic", "Apple"]
topics: ["agents & coding", "search & media", "models & research", "products & launches"]
content_source: "fulltext"
word_count: 2895
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/ClaudeAI/comments/1xnj1l3/reverse_engineering_with_receipts/"
score: null
comments: null
community: "r/ClaudeAI"
---

# Reverse Engineering, With Receipts

Insanely Digital · Insanely_Digital · 2026-11-04

Software
Reverse Engineering, With Receipts
An open-source tool that hands disassemblers to AI agents made a big splash in October. We had agents at the controls months earlier, along with a rulebook, a ledger and a short list of things we will not read.
In October, a project called Reverse Engineer Anything had the kind of month most open-source projects only dream about. REA is an MCP server: it lets an AI coding agent drive Ghidra, Hopper, IDA and a long list of other inspection tools, so the agent can query a disassembler, follow cross-references, test a hypothesis against a binary and report back with evidence. InfoQ covered it on 17 October. At the time of writing, its README thanks people for 400,000 GitHub stars.
We read the coverage with a very particular feeling. It is the one you get when a song your band has been playing in a pub since the spring turns up on the radio.
We have been reverse engineering classic Macintosh formats since April 2026. Since July, our agents have been driving emulators and a disassembler over MCP. None of that makes us first at anything, and REA is a far broader tool than ours. But it does mean we have had several months to find out that the tooling is the easy part.
The tool is the easy part
REA’s own README is admirably clear about who carries the risk. It is for “lawful research, education, interoperability, software preservation, and analysis of software you own or are authorized to examine”. InfoQ adds that users are responsible for getting authorisation and for complying with the law. That is exactly right, and it is also where the interesting question starts. What does discharging that responsibility actually look like, day after day, with agents doing the work?
Our answer is unglamorous. It is a set of house rules that every agent reads before it touches a binary, and a ledger that records where every fact came from. This post is about both, and about the rig they govern.
A short disclaimer before the long post: we are not lawyers, and nothing here is legal advice. What follows is how we work and why. The point of writing it all down is that someone who is a lawyer can check it.
What we are for
Disk Phoenix reads classic Macintosh disk images, and the Phoenix apps around it are meant to open the files on them. The formats are almost all dead, frequently undocumented and occasionally actively mysterious. (For the full flavour, see Nobody Wrote It Down.)
So every piece of reverse engineering we do is interoperability work. We are finding out how an existing file format or wire protocol is laid out, so that a program we write ourselves can read files that already exist. Before an agent starts, it has to be able to say yes to three things:
- The object is functional facts: field offsets, bit layouts, opcodes, message grammars. We are not after a program, and we are not after anyone’s artwork, text or sounds.
- The information is not readily available. We looked, and we wrote down what we found.
- The result is independently written, and does not stand in for the original as a piece of creative work.
Those three tests aren’t decoration. They follow the shape of the law we are relying on: the US cases that made disassembly for interoperability fair use (Sega v. Accolade, Sony v. Connectix), and the UK and EU right to observe, study and test a program, and in narrow conditions to decompile it. Every one of those exceptions is drawn around interoperability. Step outside it and none of them helps.
If one of the three answers is wobbly, the work stops.
Search first
The second test has a practical consequence that is easy to skip and expensive to get wrong. Before anyone opens a disassembler, someone searches for prior art: a published specification, a Technical Note, a write-up, a permissively licensed implementation.
This is not politeness. In the UK and EU, “not readily available” is a precondition of the right to decompile. It is not a formality, and the search is also simply good engineering. We learned the hard way that the search has to be per algorithm, not per project. That story, and the two days it cost, are in Nobody Wrote It Down.
When the search succeeds, we use what we found, credit it, and ship its licence notice. When it fails, we write the negative down too. “We looked, and here is where” is evidence. “We didn’t find anything” is just a mood.
Ask the machine, not the code
The biggest difference in how we work isn’t a rule. It is the instrument we reach for first.
REA points an agent at a disassembler, which shows you what a program is. Our first move is usually to run the original software and watch what it does.
So the heart of our rig is emulation, with agents at the controls:
- Snow, a classic Macintosh emulator, behind an MCP server of our own with 68 tools. Agents boot real System software from genuine ROMs (and yes, we own a real example of every Mac we emulate), insert floppies, attach SCSI disks, type, click, take screenshots, read memory and set breakpoints on Toolbox traps by name.
- QEMU, behind a second MCP server, for Mac OS 9 on PowerPC.
- A Mac mini on macOS 10.13, kept deliberately old, because it is the last macOS that still reads standard HFS volumes and it lets us automate the GUI without per-app permission prompts. It is one of the few machines in the world whose job description includes “never update”.
- The original applications, some imaged from period disks we own (boxed retail copies, and magazine cover discs) with an Applesauce, a Greaseweazle and a plain USB floppy drive, the rest downloaded from online archives. We never crack a serial number or a registration check: where an app asks for one, we enter a licence we own.
Watching a program run gives you facts about behaviour, and facts about behaviour are what interoperability needs. For a recent example, see The Letters Apple Never Shipped. There we read Vietnamese font tables by installing 1990s fonts on an emulated Mac and writing down what it drew, byte by byte. And there is a pleasing robustness to it. The emulated Mac has no opinion about our theory. It just draws what it draws.
When we do open the binary
Sometimes watching isn’t enough, and we do disassemble. We are not purists about that. Disassembly done for interoperability, after a search has come up empty, is the kind of work the interoperability exceptions exist for.
Our favourite example is Apple’s resource compression. System 7 compressed resources with four schemes, and Apple never documented any of them. Three already had public write-ups and an MIT-licensed implementation, so we used those, with the licence notice shipped. The fourth, dcmp 3, had no public implementation at all. So we took Apple’s own 7,696-byte dcmp 3 code resource out of the System file on a Mac OS 7.6 disk and disassembled it with our own tool, classicdis.
Inside was a table of thresholds following a tidy rule, except for two that didn’t. One reads 0x66C where the pattern says 0x680. The tempting move is to tidy it. That would be a mistake, because Apple’s compressor used the same table, so every file compressed by that code depends on the anomaly. The odd value isn’t a bug in the format. It is the format.
We carried the values into our Swift code exactly as the binary has them, anomaly included, and pinned them with a test so nobody tidies them later. They are not the kind of table our rules keep out. Those are another implementation’s choices about how to express something; these numbers are the format itself, and a decompressor given any others produces the wrong bytes. All 15,756 compressed resources in our test corpus now expand.
A constant that has to be wrong in exactly Apple’s way in order to work is about as purely functional as a fact gets. We find that rather lovely.
Watching the wire
We started stricter than we ended. Our first rule was absolute: never read anyone else’s source code, full stop. We tried that on our QDesign Music decoder, and to be fair, it held. The codec was identified and one of its tables derived without anyone opening the reference decoder’s source. But it was stricter than our own standing rules, which already allowed reading other people’s code for facts as long as none of it was copied. It also ruled out something perfectly harmless: adding a few print statements to that decoder and reading the numbers.
And it had a name. The notes we wrote that July called it a “clean-room boundary”. We have since banned the phrase (more on that below). After several rounds of reverse engineering, we paused to check whether clean-room language had crept into how we describe our own work. It had. It’s an easy path to take: the phrase sounds like exactly the right thing to say. Those July notes, and a handful of other files, had drifted into that territory, borrowing the label for work that was never two-team. So we corrected course, deliberately. All of them are fixed now.
On 29 July we replaced it with something more precise. It is the most important sentence in our rulebook, and agents are told to quote it rather than paraphrase it:
Trace yes, transcribe no. A third-party implementation may be run, and may be instrumented to emit numeric traces. Those numbers are observations and may be used freely. What may not cross over is expression: its structure, its control flow, its function decomposition, its tables.
The idea came from our AppleTalk work, where we learn protocols by watching packets go by on the wire. A packet capture records what happened. It doesn’t copy the thing that made it happen. A decoder printing its intermediate values is the same act.
The rule matters most at exactly the moment REA makes easy. Decompiled pseudo-code is very readable, and an agent that has just read it will cheerfully write new code in the same shape. So our policy carries a blunt test: if the code you are writing mirrors the shape of what you just read, you have crossed the line. Stopping is a permitted outcome, and so is escalating to a human. Peeking first and asking forgiveness later is not.
Four kinds of constant
Every table that ships in our code gets a label for where it came from:
- Derived: we can regenerate it from a rule, a probe or a measurement, and the generator is recorded.
- Functionally dictated: it has to be exactly this to interoperate, like that dcmp threshold.
- Prior art under a compatible licence: taken from someone else’s published work whose licence allows it, with the obligation discharged in the same change. The MIT-licensed decompression code above is this kind, and its notice ships in the app.
- Unestablished: we don’t know where it came from or can’t yet prove it, so we say so, out loud, in the file.
That fourth label is the important one. A table with no honest origin doesn’t get to pretend it has one.
Things we will not read
Some material stays closed to us however useful it would be.
Apple released the Lisa operating system’s source through the Computer History Museum under an academic licence, and Disk Phoenix is a commercial product. That door is closed to us; Nobody Wrote It Down tells that story. Converter tables written by other projects, many of them GPL, are allowed to check our answers but never to supply them. And anything that arrives from a confidential source is an immediate stop, because no statutory exception reaches trade secrets.
The order of operations turned out to matter more than we expected. In August an agent acquired fifteen documents from a permissively licensed emulator project, to answer questions about the Lisa. Six of them turned out to be derived from the Lisa source. Five were quarantined unopened. The sixth, one of our agents had already read, cover to cover. Its brief said “stop if you encounter derived material”, and you can’t notice you’ve encountered something until you’ve read it.
We wrote that brief.
The licence on that document was perfectly permissive. Its contents were not ours to use.
So the rule now runs in a strict order. First, sweep every new document for derivation markers: source-file names, ROM listing identifiers, phrases like “per the disassembly”. Then quarantine anything that matches, with a note in the directory naming the files. Only then read what’s left.
Auditing ourselves
The rules didn’t arrive on day one, and some of our earliest code was written before them.
In August we audited every place where our source code credited one particular open-source library, a well-regarded project under a copyleft licence. We did it without opening the library, because reading it to check whether we had copied it would itself create the exposure we were auditing. The sweep found 38 matching lines across 21 files. In several of them, our own comments said the code mirrored or was based on that library.
Seven importers had been built that way, with no prior work of our own behind them. Kevin’s ruling was short: delete them and forget them. So we did. Our count of supported formats went down, and that was the point. The audit itself stays in the ledger permanently, because deleting the record would turn a disclosed and resolved problem back into an undisclosed one.
Throwing away code that worked is not a nice feeling. Keeping code you can’t account for is worse.
The register
All of this would be talk without the ledger. It is a single document, started on 29 July, that has grown to roughly 19,000 lines. Every format, codec and protocol we have reverse engineered gets an entry: 146 in the formats-and-codecs part alone. Each entry records:
- what the knowledge is and where it lives in our code;
- where it came from: a published document, a running original, a disassembly, or prior art with its licence named;
- the oracle that checked it, and what that oracle cannot see;
- the licence obligations, and whether they are discharged;
- what was refuted, kept in place and marked “⛔ REFUTED — do not re-derive”, so nobody spends a day rediscovering a wrong answer. There are 38 of those marks so far, and we treasure every one.
Each fact is recorded in three places at once. The source file carries a provenance block (187 files have one today). The ledger carries the argument. The commit that introduced it carries a Provenance: trailer, and nearly a thousand commits on our main branch have one. A fact recorded in only one place can quietly disagree with itself. A fact recorded in three gets caught.
The ledger has its own rules of evidence, too. Claims are cited by quotable text rather than line number, because line numbers rot: an audit of our own documentation found 13 of 169 such citations already broken. Every instrument has to be seen to fail on a case built to make it fail, or it counts as decoration rather than a check. And no test fixture may be generated by the code it tests.
A check that cannot fail isn’t a check. It’s a comfort.
Not “clean room”
You met that phrase earlier, in our own July notes, and it is the one we now refuse to use. “Clean room” means something specific: the two-team procedure made famous by the IBM PC BIOS clones, where one team reads the original and writes a specification, and a second team, which has never seen the original, implements from that specification alone.
We don’t do that. We are one team, and we say so. Our rulebook forbids calling our work “clean room” in code, documentation or marketing, because it invites a comparison we would lose. The accurate description is less catchy: single-team interoperability reverse engineering, independently implemented from documented behaviour. We would rather be accurate than catchy, at least in the legal sections.
What does not exist yet
To be plain about it:
- We are not lawyers, and this post is not legal advice. The ledger is written so that a lawyer can check it. That check is a lawyer’s job, not ours.
- Our rig and our ledger are not published. The emulator MCP servers, classicdis and the ledger all live in private repositories. REA is MIT-licensed and on GitHub; ours is not, today.
- The Phoenix apps are in development. None of them is available yet.
The receipts
REA has made the mechanics of reverse engineering dramatically faster, and that is genuinely good news for anyone preserving old software. An agent with a disassembler can find a structure in an afternoon that used to take a week.
But speed was never the hard part for us. The hard part is being able to answer, months later, a question nobody is asking yet: where did this number come from?
We can. It’s in the ledger, with a receipt.
