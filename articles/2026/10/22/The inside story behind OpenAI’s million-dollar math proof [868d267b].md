---
id: "868d267b0e20e1e2"
title: "The inside story behind OpenAI’s million-dollar math proof"
url: "https://scientificamerican.com/article/the-inside-story-behind-openais-million-dollar-math-proof"
link: "https://scientificamerican.com/article/the-inside-story-behind-openais-million-dollar-math-proof"
source: "Scientific American"
domain: "scientificamerican.com"
source_type: "tech_press"
collector: "rss"
date: "2026-10-22T16:12:00Z"
published_date: "2026-10-22"
collected_at: "2026-10-23T12:06:21Z"
authors: ["scientificamerican"]
language: "en"
summary: "AI’s solution to the Navier-Stokes problem, and the details of how it happened, preview a chaotic future for math—and the world"
tags: ["r/artificial", "r/ArtificialInteligence"]
orgs: ["OpenAI", "Anthropic", "Google"]
topics: ["models & research", "business & funding", "products & launches", "search & media"]
content_source: "fulltext"
word_count: 2397
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/artificial/comments/1xcqows/the_inside_story_behind_openais_milliondollar/"
score: null
comments: null
community: "r/artificial"
---

# The inside story behind OpenAI’s million-dollar math proof

Scientific American · scientificamerican · 2026-10-22

Room 109 of New York University’s Warren Weaver Hall wasn’t ready for what hit it.
A half hour ahead of a special seminar scheduled for 3:30 P.M., attendees hoping to snag a seat already packed the hallway outside. When the doors opened, they all surged in, some climbing over rows of chairs to secure a good spot. Soon every inch of floor and both aisles were filled, with late-arriving onlookers trailing out the entrances. “Surely this is the most people this hall has ever seen,” I heard one bystander say. “This is no ordinary seminar. This is a rock concert,” said another.
The headliner was N.Y.U. mathematician Tristan Buckmaster. It was his first public lecture since September 8, the day OpenAI claimed to have solved one of math’s “million-dollar problems”—right after Buckmaster publicly called the company out for seeming to steal his work.
On supporting science journalism
While Buckmaster set up, I peeked at the open laptops in the row ahead of me. Each showed a chat window with a large language model (LLM), either Anthropic’s Claude Code or OpenAI’s ChatGPT Codex. The prompters were asking their LLM to help construct a mathematical proof, or rewrite part of a manuscript in progress. In other words, they were doing math in 2026.
“I hope you stay with me,” Buckmaster began. “I have been so busy these last few weeks that I literally wrote this talk last night.”
The public discord surrounding the biggest math breakthrough in decades capped off a summer of disruption that has left humanity’s oldest academic discipline forever changed. Ever since the momentous OpenAI announcement, the events behind it have appeared as messy and confusing as the proof itself. But now, as the community races to reverse-engineer the LLM’s opaque logic, a few things are becoming clear.
OpenAI’s internal model indeed found the right answer. And it did so by following a different path than anyone—including the company’s top mathematicians—initially realized.
Clearest of all, though, is that we’re entering a troubling new era. Inscrutable models are making scientific history while cloaked in proprietary secrets. Humans, with their foibles and petty jockeying, are barely keeping up. Consequently, that history has never been harder to write down.
The North Star
Buckmaster’s tale starts a year ago, with an e-mail from someone he’d never met: mathematician and Anthropic employee Levent Alpöge.
“I fear a world in which corporations are the only ones with claim to the deepest pure math work,” Alpöge wrote. “It seems to me there will be only one Millennium Problem solved in the foreseeable future,” he continued, proposing that he and Buckmaster could work together to solve it.
That problem—one of Clay Mathematics Institute’s seven “Millennium Prize Problems”—is known simply as “Navier-Stokes.” The nickname refers to the Navier-Stokes equations, which dictate how fluids swirl and flow. Mathematicians had long suspected that the equations don’t always work. That sometimes, they would predict that a fluid does the impossible—that its flow, at points, “blows up,” reaching an infinite and entirely nonsensical velocity.
Find such a flaw—using a mathematical proof—and the Clay Institute would owe you a cool $1 million. Alpöge wasn’t the only one in Silicon Valley who thought that goal was within reach.
“At that time, you have to understand that the Navier-Stokes equation became this tech bro obsession,” Buckmaster told N.Y.U. audience. Most of those tech bros didn’t even understand the equations, he said, but they’d heard mathematicians point to them as a place artificial intelligence might help. As Buckmaster put it, solving Navier-Stokes was becoming “the yardstick to say, ‘We’re better than that other AI company.’”
In fact, Buckmaster had collaborated with Google’s DeepMind team in their own pursuit of this goal—Navier-Stokes, he tells me, has always been the “North Star” of his research. So he accepted Alpöge’s overture.
They focused on a potential loophole in the Clay Institute’s posing of the problem, which said a mathematician could “stir” the fluid with a finely-tuned force. A few years ago, the Spanish mathematicians Diego Córdoba and Luis Martínez-Zoroa realized that phrasing might allow an exploit. The Spaniards sketched out a specific program—to contrive an ultraprecise, unrealistic force that pokes and prods each point in the fluid just so, massaging it into blowing up.
Alpöge and Buckmaster started by instructing their LLMs—a mix of Anthropic and OpenAI models—to carry out Córdoba and Martínez-Zoroa’s program. They first managed to blow up simpler sets of equations describing idealized fluids—easier proxies for Navier-Stokes. Buckmaster told me their collaboration was “purely personal,” without official involvement from Anthropic—although, he acknowledged in his lecture, during their work Alpöge did have access to Anthropic’s computing resources and unreleased versions of Claude.
Alpöge’s math output has been the subject of some consternation. In the last several months, he’s prodded Claude into resolving several famous open problems, often announcing them in cryptic, playful posts on social media. He’s left mathematicians unsure to what extent these explosive results represent his employer and has built a strange reputation somewhere between folk hero and Internet troll. Downplaying his affiliation, Alpöge has characterized his work with Buckmaster as “mostly me and Claude having a good time YOLO-ing random stuff in the corner.”
Contrast his approach with that of OpenAI, whose assault on mathematics has been overwhelming and deliberate. The company has strategically poached much of the field’s top young talent, arming them with lavish resources to bag the biggest mathematical game they can. They unveil their papers alongside carefully-worded press releases, substituting the impersonal, monolithic byline “OpenAI” for the traditional list of human contributors. They’ve become notorious for disregarding academic norms, and their lead scientist Sébastien Bubeck has now had to apologize repeatedly after these aggressive rollouts sparked furious backlash.
In August, after several months of slow progress, Alpöge and Buckmaster’s prompting suddenly took off. On the 15th, Alpöge informed Buckmaster that Claude had blown up the Euler equations—equivalent to Navier-Stokes without friction, a simplification seen as a crucial step toward solving the full problem. “He didn’t quite believe it himself,” Buckmaster recalled during his public talk. Looking at the document the AIs had spit out explaining their proof, Buckmaster didn’t believe it, either.
“This was the most horrible mathematics I’ve ever seen in my life,” he said to laughter as he flashed a slide showing some of the proof’s impenetrable wall of garbled text and numbers.
“Although they’re English words, it’s not English,” Buckmaster went on. “But all the different LLM models understand this complete gibberish.” As unbelievable as it seems, when LLMs team up on a math problem, they begin communicating in their own “weird slop dialect,” as one mathematician put it to me.
And on August 22 Buckmaster and Alpöge prompted their LLMs to code the whole thing in Lean—a programming language that breaks a math proof into tiny steps and confirms that each follows from those before it. “This complete and utter nonsense was Lean-verified,” Buckmaster said, meaning it was correct.
But he and Alpöge didn’t want to post a result they didn’t understand. So the pair began a sprint to rewrite the proof for human consumption, relying heavily on OpenAI’s ChatGPT Codex.
The Blowup
Here the timelines get fuzzy. The following was gleaned from public statements plus supporting documentation provided by Buckmaster. Alpöge and Bubeck both declined on-the-record interviews, but Bubeck corroborated the basic facts and direct quotes.
On August 28 OpenAI happened to begin training a new internal model that proved to be far better at math than any predecessor. Then, on August 31, Alpöge tweeted “Augustus Mirabilis”—Latin for “miraculous August.” Alarmed, Bubeck and his team at OpenAI took this and other rumors to mean Anthropic “had solved at least one Millennium Problem.” By Tuesday, September 1, they had launched a rushed counterattack, sending a squadron of copies of their new model at each open Millennium Problem, plus a few others—including the Euler equations for fluids.
The following day, Wednesday, Buckmaster and Alpöge learned through back channels about OpenAI’s frenzied efforts. Buckmaster attempted a détente on Thursday morning, e-mailing a mathematician on the company’s math team. He informed them that his collaboration with Alpöge was the subject of the rumors and clarified that their work was not an official Anthropic effort—that he’d been using OpenAI models as well, in fact. The mathematician’s response was encouraging—offering computing resources and asking for more details because “it would be useful to avoid competing here.”
But that night, a squad of 100 agents that OpenAI had set upon the Euler equations leapfrogged Bubeck and Alpöge. The agents figured out a way to remove the weird force that was the centerpiece of Córdoba and Martínez-Zoroa’s approach—that is, OpenAI’s agents managed to make the fluid blow up on its own, without stirring it at all, producing their own Euler proof.
Stunned, the team decided to redirect all its resources at Navier-Stokes. The researchers assembled a swarm of 10,000 intercommunicating agents and fed it the new Euler proof as a starting point.
On Saturday, after consuming a reported $15 million in computing resources, the 10,000-agent swarm solved Navier-Stokes. It had to reintroduce a force to do so—reopening the loophole it had managed to close for Euler.
On Sunday, Buckmaster and Bubeck finally spoke. Bubeck claimed that OpenAI’s new model had solved the Clay problem in a single go, without any input beyond the official problem statement. He then backpedaled, revealing some details of the company’s weeklong agent extravaganza. Seeing Bubeck’s story change mid-telling, Buckmaster lost confidence that OpenAI was acting in good faith. He became suspicious that the company’s internal model had somehow accessed the work he had done with their public Codex model.
From there, the conversation couldn’t be salvaged. “You are not going to be able to convince me that you did not get the key ideas from a leak,” Buckmaster told Bubeck. Bubeck offered Buckmaster lead authorship on OpenAI’s Navier-Stokes paper—but demanded that Alpöge’s name be removed because of his affiliation with OpenAI’s competitor. When Buckmaster threatened to go to the press, Bubeck asked, “Why would you risk your career?” After Buckmaster’s defiant reply, Bubeck rejoined, “if you don’t want me to be nice, then I don’t have to be nice.”
At that point, there was nothing more to say. By Tuesday morning, each team had posted their proof, along with their side of the story.
A Maze of Math
In the Sunday phone call with Buckmaster, and their blog post and press conference on Tuesday, OpenAI’s math team said that their solution to Navier-Stokes followed the same mathematical path as Buckmaster and Alpöge’s.
But it turned out they were wrong. The models had carved out their own way.
The swarm’s proof does exploit the same loophole before—it constructs a strange, perfectly calibrated force to coax the fluid into blowing up. But the way it constructs this force is distinct from the Spanish program and thus distinct from Buckmaster and Alpöge’s Euler proof.
Buckmaster himself acknowledges that OpenAI’s Navier-Stokes proof introduced new ideas. But he still believes OpenAI somehow relied on his progress. The company’s Euler proof, he said in his lecture, clearly uses the Spanish program. “That was our result,” he said plainly.
As he sees it, his work with Alpöge on the Spanish program blazed a trail to get to a specific destination—using a force to blow up the Euler equations. And he believes OpenAI’s agents followed that same trail. From there, Buckmaster thinks, the agents continued in two forking directions.
The left fork cleverly removed the force after doing all that work to construct it. OpenAI’s 100-agent squad found a way to encode that complicated stir into the fluid’s initial state, rather than applying it externally. Buckmaster says this fork only goes a tiny distance further, mathematically, than their own preexisting proof.
Mathematicians are still comparing the two Euler proofs, but at least one expert agrees with Buckmaster’s take. “As far as I can tell, OpenAI’s proof basically follows the framework of our program,” says Fan Zheng, a collaborator of Córdoba and Martínez-Zoroa at the Institute of Mathematical Sciences in Spain. “But OpenAI is able to overcome a couple of technical difficulties to remove the force.”
The right fork, according to Buckmaster, led to Navier-Stokes. He views it as an extension of the same path that added some more significant new ideas—still a fork, but a longer one. (He also says that he and Alpöge used similar ideas in an alternate AI-generated Euler proof that they never made public but that they did feed into Codex.) Other experts studying OpenAI’s Navier-Stokes proof, however, feel that the company’s swarm instead carved an entirely new path that bears only cursory similarities to the trail Buckmaster and Alpöge’s AIs had previously blazed.
OpenAI emphatically denies the allegations. “No user inputs, including anything from Dr. Buckmaster’s Codex and ChatGPT usage, after July 3, 2026, could have influenced the model or the math results it produced in any way,” a spokesperson wrote in a statement to Scientific American.
This narrative, still murky more than a month after the fact, warns of a new normal that has already arrived. LLMs are proving math results far faster than humans can make sense of them. OpenAI announced one of the most important proofs in history without anyone on staff understanding even the broad strokes of the math it contained. Bubeck himself said on X that OpenAI “collectively had no research-level expertise in fluid dynamics.”
In Buckmaster’s first e-mail to OpenAI back on September 3, he explained why he and Alpöge were taking the time to rewrite their Euler proof before posting it. “I feel strongly that the first thing anyone reads should be a mathematical argument they can follow and argue with,” he said. The company disagrees—as punctuated a few weeks later, when it dropped hundreds more nigh-impenetrable math results on the community, many without Lean verification.
In the Q&A after Buckmaster’s talk, he declined the audience’s requests to predict the future. He only knows that September 8 marks the day after which math would never be the same, and that mathematicians need to decide how to respond. But his own feelings on that question, he said, still change day to day.
Asked what should happen next, his reply received the loudest applause of the day—a clear signal of the audience’s pent-up feeling.
“What we should do right now,” he blurted out, “is get the AI companies to stop acting like children.”
