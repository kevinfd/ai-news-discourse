---
id: "6f7370a4596df612"
title: "Achieving AI-style reasoning without an LLM"
url: "https://fleetingswallow.com/minotaur-ai-deep-dive-achieving-reasoning-without-a-language-model"
link: "https://fleetingswallow.com/minotaur-ai-deep-dive-achieving-reasoning-without-a-language-model"
source: "Fleeting Swallow"
domain: "fleetingswallow.com"
source_type: "community"
collector: "hackernews"
date: "2026-10-22T08:46:58Z"
published_date: "2026-10-22"
collected_at: "2026-10-22T12:07:09Z"
authors: ["edwardchalk"]
language: "en"
summary: "Minotaur AI Deep Dive: Achieving Reasoning Without a Language Model\nIn the last post we introduced Minotaur, an AI that reasons with no language model and no GPU. This post looks at why language models think the way people do, at what was tried before them and where each attempt stopped, and at how Minotaur’s brain does the same kinds of reasoning differently: not by imitating how people write…"
tags: []
orgs: ["UK"]
topics: ["models & research", "chips & infrastructure", "search & media", "business & funding"]
content_source: "fulltext"
word_count: 4732
paywalled: false
image: null
discussion_url: "https://news.ycombinator.com/item?id=50192868"
score: 42
comments: 24
community: "Hacker News"
---

# Achieving AI-style reasoning without an LLM

Fleeting Swallow · edwardchalk · 2026-10-22

Minotaur AI Deep Dive: Achieving Reasoning Without a Language Model
In the last post we introduced Minotaur, an AI that reasons with no language model and no GPU. This post looks at why language models think the way people do, at what was tried before them and where each attempt stopped, and at how Minotaur’s brain does the same kinds of reasoning differently: not by imitating how people write their thinking down, but by working on the structure of the system it’s reasoning about.
Introduction
In the last post we introduced Minotaur, an AI architecture built on ELC that works out its answers by measuring rather than predicting. We showed it checking real regulations against records of how they were applied: finding which organisation broke a rule, by how much and where, and telling a broken rule from a badly recorded measurement.
Checking rules against records is one kind of thinking. Today’s language models are admired for something broader: they can deduce, explain, diagnose, weigh a hypothesis, imagine what would have happened if things had been different, and change their minds when told something new. Can a machine with no language model, and no GPU, do all of that?
The answer is yes:
- Minotaur’s brain does the main kinds of reasoning usually credited to large language models: deduction, induction, abduction, diagnosis, seeing against doing, choosing the experiment that settles a question, revising a belief, and reasoning about histories in which asking a question changes the answer.
- It does all of them with one operation on one network, on one ordinary processor core, at about a quarter of a second per question on a described system.
- On blind tests written by people who never saw its code, it matched a current language model reasoning in words, on a police interview where the questions change the witness’s memory, and on learning, diagnosing and predicting systems from their data alone.
Why a Language Model Thinks Like a Person
A large language model is trained to predict the next word of a piece of text. It learns this from an enormous amount of writing, from books, papers, textbooks, forums and code, by doing it trillions of times on thousands of GPUs.
To predict the next word of a proof, you have to follow the proof. To predict the next line of a doctor’s notes, you have to follow the diagnosis. Much of the writing in the world is people thinking on paper, so a model that gets very good at continuing it ends up very good at imitating the thinking. That’s why simply asking a model to “think step by step” makes its answers better.
So a language model mirrors the way people think. It inherits our strengths: explaining, drawing analogies, using common sense, taking a question in ordinary words. Researchers have also found that it inherits our weaknesses. Like people, language models find a logical argument easier to accept when its conclusion sounds believable, and harder when it doesn’t. Their answers can shift with how a question is framed or the order things are put in. And like ours, its explanations are often written after the fact, not a record of how the answer was reached.
The model never sees the world, only our words about it.
It does mean that if you want reasoning that can be checked, replayed and certified, imitating the way people write their thinking down may not be the best place to start. Exact, checkable reasoning was what most approaches to AI before language models were trying for.
Seventy Years of Trying Something Else
People tried to build machines that reason for some sixty years before language models. Each attempt worked up to a point and then stopped, and where they stopped explains why we ended up with language models.
Search and theorem proving
In 1956 Allen Newell, Cliff Shaw and Herbert Simon built the Logic Theorist, a program that proved theorems from Whitehead and Russell’s Principia Mathematica. Their next program, the General Problem Solver, tried to do the same for any problem that could be written as a starting point, a goal and a set of moves. The idea was that reasoning is search: try the possible steps until you reach the goal.
It worked on puzzles. On real problems the number of possible steps grows so fast that no computer could search them. In 1973 the Lighthill report to the British government named this the combinatorial explosion, and funding in Britain was cut sharply.
Expert systems
The answer in the 1970s was the expert system, which gave the machine knowledge instead of search: hundreds or thousands of hand-written rules of the form if this, then that, collected from human experts. MYCIN, built at Stanford, recommended antibiotics for serious infections, and in a 1979 evaluation its advice compared well with that of specialists. XCON, at Digital Equipment Corporation, configured computer orders and saved the company a great deal of money.
They stopped for two reasons. Every rule had to be got out of an expert’s head and written down by hand, which came to be called the knowledge acquisition bottleneck. And they were brittle: just outside what the rules covered, the system had nothing sensible to say. By the end of the 1980s the market for them had collapsed.
Logic programming
Logic programming aimed to have the machine reason exactly, in a proper logic. That was the bet behind Prolog, created in Marseille in 1972, and behind Japan’s Fifth Generation Computer Systems project, which ran from 1982 to 1992 and was built around logic programming.
Logic gives exact answers, and its descendants, the solvers that check whether a set of conditions can all be true at once, are now used every day to verify computer chips. But logic only reasons about what someone has written down as logic. The world doesn’t arrive in that form, and the Fifth Generation project ended without the thinking machines it had promised.
Hand-built common sense
In 1984 Douglas Lenat started Cyc, an attempt to write down, by hand, the common sense that expert systems lacked: that water runs downhill, that people have mothers, that a thing can’t be in two places at once. Over the following decades its team entered millions of such facts.
It showed how large the common sense people take for granted is, and that writing it down by hand never comes to an end.
Probability and causal models
From the late 1980s, led above all by Judea Pearl, reasoning under uncertainty got a proper mathematical footing. A Bayesian network says which things affect which and how strongly, and lets a machine work out what an observation implies. Pearl went on to make precise the difference between seeing something and doing it: seeing a wet pavement suggests it rained, but hosing the pavement yourself tells you nothing about the weather. In the same years, Raymond Reiter, Johan de Kleer and Brian Williams turned diagnosis into a precise method for finding which component of a system has failed.
These are some of the best ideas in the field, and Minotaur reproduces them. But someone has to hand them the model first: the causal graph, or a description of every component. Given only a column of numbers, they can’t begin.
Deep learning
From 2012, neural networks trained on large amounts of data, known as deep learning, began to beat everything else at recognising images and speech. They need nothing handed to them except examples.
What they learn is a pattern, with no structure to reason on. A network that has learned how a production line behaves can predict its output. It can’t tell you that one of its inputs is a safety cut-off, or answer the question “what if that cut-off were stuck open?”, because there’s no cut-off anywhere inside it to be stuck.
And then, language models
Language models, built on the transformer design published in 2017, reached the public in 2022, and from 2024 began to be trained to reason step by step before answering. Language models won because they’re the one approach that needs nothing handed to it. You don’t write a model of your problem for it; you describe the problem in plain words, and it reads them.
The price is the one we discussed in the last post. The reasoning runs through hundreds of billions of weights on data-centre GPUs, and the answer comes with no certificate of how it was reached.
Each way of getting a machine to reason has had a price:
- The ones that reason exactly need the model handed to them.
- The ones that learn from data give you no structure to reason on.
- The one that reads the prose needs a data centre, and can’t certify its answers.
Minotaur sits in the middle. It can be given a description or learn one from data, puts it into typed roles it can reason on, and reasons exactly enough to certify each answer, on one ordinary processor core.
Minotaur’s Brain
The ideas behind ELC are set out on the MINOS page, and the last post gave the short version. Every system, whatever it’s about, is read in three roles:
- something drives it (Energy, or E);
- something constrains it (Control, or C);
- and the system has its own way of relating the two (Logic, or L).
E and C never connect directly. A drive doesn’t say what is allowed, and a limit doesn’t say which drive it answers. The relation between them always has to be supplied, and supplying it is what the system’s logic is.
Each element of a system is read as a share. Of what arrives at it, some passes and some is held back, and the two always add up to the whole. At one end everything passes, at the other everything is held, and in between there is a balance point.
This is a minimal representation of a system; MINOS stands for the minimal ordinal representation of systems. A whole boiler can be read as a single element: something drives it, something constrains it, and its logic relates the two. When more detail is needed, the same reading is applied to its parts. The boiler becomes a pump, a fan, a burner and a gas valve, each an ELC element with its own drive, constraint and logic, connected so that what one element passes on becomes the next one’s drive. The description gets finer, but it never leaves the ELC format: it’s the same three roles at every scale, just more finely divided and more interconnected.
On this representation we built Minotaur’s brain.
Two sides
A brain that reasons in general turned out to need two kinds of faculty, best kept apart, a little like the two hemispheres of a human brain.
The ELC side holds the system being reasoned about, as a network of ELC elements. It has exactly one operation, settling, described below. It can also learn a system it has never been told about, from records of what that system did. By design, it contains no counting, no exact arithmetic and no matching of text. Its results are measured: the network came to rest, or it didn’t, to within a stated tolerance.
The exact side is a calculator. It reads a description of a system, lists every case when every case has to be checked, does exact arithmetic and checks results. Its results are exact: true in every case, or here is a case where it isn’t.
The crossings
Nothing passes between the two sides except through a named, one-way crossing:
Every crossing is recorded, along with the certificate it carries. When an answer rests on several steps, it carries the weakest certificate among them.
That record is also the brain’s chain of thought. When a language model shows its reasoning, it writes a new piece of text. When Minotaur shows its reasoning, it shows the crossings it actually made, in order.
Settling
Picture the network as a set of nodes, each holding a share between “all passed” and “all held”, joined along the lines ELC allows: drives into logic, constraints into logic, logic on to logic and to constraints. Never drives straight to constraints, or back.
To ask a question, you say what each node is doing:
- some are held: these are the facts you’re given;
- some are cut: forced to a value, with their own law switched off;
- some are left free: these are the holes, the things you want to know.
The rest follow their laws. Then the network settles, a little like water finding its level:
- Every lawful node takes the value its law gives it.
- Minotaur measures the stress: how much of what was held fails to come back as it was held.
- That misfit is carried backwards, but only through the logic nodes and only to the holes, so the rule that drives and constraints never connect directly applies backwards as well as forwards.
- Each hole is pushed to commit to one end or the other: passes or holds. A hole that comes to rest at the balance point hasn’t really been answered.
- The result is read, with its stress shown.
If the stress falls to almost nothing and every fact reads back as it was held, the world closes: there’s a way for things to be that fits everything given. If no setting of the holes will close it, the stress says where the contradiction sits.
One network, many questions
Every kind of reasoning is the same settle, asked differently. What changes is only which nodes are held, which are cut and which are left free.
The ELC side has no special code for any of these kinds of reasoning. Where an answer needs every case checked, as deduction does, the exact side lists the cases and the ELC side settles each one. So deduction gets an exact certificate, because no case is left out.
Following the Brain Through
All of the systems below were written in a simple format that lists a system’s drives, constraints and laws. The first two were written by us for development. The others were written by people who never saw Minotaur’s code, and we come to how they were tested afterwards.
A diagnosis
Start with a house’s lighting. The supply comes in through a main breaker and splits into a hall circuit and a kitchen circuit, each with its own fuse, switch and bulb, and the kitchen circuit also feeds a socket and a kettle. All the switches are on. The kitchen lamp is lit and the hall lamp is dark. What has failed?
The exact side supposes, one at a time, that each part has failed, starting with the smallest possibilities. For each supposition, the ELC side settles the network and reports whether the world closes. Supposing nothing has failed, it doesn’t close, and the stress is at the hall lamp. Supposing the hall bulb has failed, it closes. The kitchen bulb doesn’t close. The hall fuse closes. Larger combinations that already contain one of those answers are skipped, because a smaller explanation is always better. None of the rest closes.
The answer is either the hall bulb or the hall fuse, which is what a good electrician would say. Asked for an experiment to tell the two apart, Minotaur says that no setting of the switches can: both faults leave the hall dark whatever you do. That is also correct.
The same lighting circuit answered 29 questions of every kind, and all 29 matched the answers of an independent checker. On 40 planted faults it found the exact set of possible explanations 40 times out of 40, with no false ones. The whole question file took about a second and a half.
Seeing is not doing
The second system is a greenhouse watering controller, with a hidden cause in it. When it rains, the beds get wet, and the rain gauge also reads wet. When the gauge reads wet, the controller stops the pump.
Ask: if we see the gauge reading wet, are the beds wet? Minotaur holds the gauge as an observed fact, with its law intact. The misfit is carried back through the gauge to its cause, rain, and the answer is yes: the gauge says it rained, so the beds are wet.
Now ask: if we force the gauge to read wet, are the beds wet? This time the gauge is held and its own law is cut, because forcing it says nothing about what caused it. Nothing is carried back through it. The pump stops, rain stays unknown, and the answer is undetermined.
This is Pearl’s distinction between seeing and doing. In Minotaur it comes from the difference between holding a node and cutting it, not from a special rule.
A boiler, from deduction to induction
The third system was written by someone outside the project, from the format alone: a home combination boiler with 30 parts, including a timer, a pump, a fan, an igniter, a flame sensor, a gas valve, and a mains supply that feeds both the fan and the pump. Here are some of the 36 questions it was asked, with Minotaur’s answers. Each one matched the independent answer key.
Saying no test exists, as in the second-to-last row, is a valid answer, and a reasoner that always proposes a test will sooner or later propose a useless one. In the last row, Minotaur doesn’t invent a single threshold; it reports the exact range the cases seen allow, and where to look next to narrow it.
When asking changes the answer
Ordinary logic assumes that facts don’t change when you look at them, but a witness’s memory can. Ask a witness a leading question, “did he have a beard?”, and you can plant the beard you asked about.
The fourth system, again written by someone outside the project, was a police interview. It has a robbery, a witness, a line-up, a detective who may or may not ask leading questions, a lawyer who may or may not be present, and a video recorder. And it has a list of what each question does to the witness’s memory: a leading question about a beard plants one, a leading question about a jacket can wipe the jacket out, and picking someone in a line-up makes the witness more confident.
Minotaur handles this by reasoning over a chain of worlds. The first world is things as they happened. Each question produces the next world: the answer is read in the world before, and then whatever the question changes is reset. The whole chain is turned into one network and answered by the same settle.
In the diagram, the witness was asked twice, with leading questions, whether the robber had a beard, and answered no and then yes. Did the robber have a beard? Minotaur answers no. The first answer was the true memory, and the first question planted the beard behind the second.
Reasoning over fixed facts can’t do this. To it, “no” and then “yes” about the same fact is a contradiction, so it calls the story impossible. On the 15 questions whose answers depend on the order of asking, fixed-fact reasoning got 0 of 15. Minotaur got 15 of 15, and all 30 questions in all, including one in which leading questions led to a wrongful charge. The whole set took seven and a half seconds.
Learning a system it was never told about
Everything so far started from a description of the system. The harder test is a system nobody has described.
So we gave Minotaur 400 rows of what a production line did. Each row had four readings, demand, feed, pressure and the ambient temperature, plus the line’s output. It got no laws, no diagram and no labels saying which column did what. Behind the scenes the line was driven by demand and feed, shut off by a safety cut-off when the pressure rose too high, and unaffected by the temperature. Then we broke the line, without saying how, and gave Minotaur 80 rows of what it did afterwards.
First Minotaur learned the line, into ELC’s typed roles. It found that demand and feed were drives, that pressure was a constraint that shut the line off above a certain level, and that the temperature was inert. When the network learns, the drive part and the constraint part can come out the wrong way round, each fitting the data equally well. ELC’s own algebra says how to put them back the right way round without changing anything the network does.
Then it supposed, one at a time, each kind of fault a system with those roles can have: the cut-off has moved, the cut-off is stuck open, it’s stuck shut, a drive has stopped counting. It fitted each supposition to the 80 new rows. One fitted far better than the rest: the pressure cut-off has moved to 0.557. We had planted it at 0.55.
Finally it went back out. The altered network predicted what the broken line would now do under new conditions, with an average error of 0.023, against 0.080 for the network before the fault was found.
On ten fresh lines, each with its own planted fault, Minotaur named the fault ten times out of ten and predicted the broken line’s behaviour every time, with errors between 0.002 and 0.023. Each line took about 10 to 15 seconds on one processor core, learning included.
The faults it could suppose, the cut-off has moved or a drive has gone dead, are faults of typed roles. A generic learner can fit the same 400 rows just as well, but it has no cut-off inside it to move and no drive to lose, so “what if the cut-off were stuck open?” isn’t a question it can be asked. The ELC neural network that does this learning is patent pending.
Carrying a conclusion into a second system
Our production line feeds a packing station, and the packing station keeps its own books, in kilograms a minute rather than shares. It was learned separately, from its own records alone.
MINOS holds that two systems framed independently can only be joined through a supplied relation between their frames, which we call a transport. So the exact side fitted one from 30 rows logged on both systems: how the line’s output shows up at the station, in the station’s units. Then Minotaur ran its conclusion about the broken line forward, through the transport, into the station: what will the station pack now?
On ten fresh pairs it predicted the station’s output ten times out of ten, with errors between 0.010 and 0.034. Leaving the transport out, and pretending the two systems speak the same units, made the predictions 2.6 to 12 times worse, every time. Asked to find a single fault that could be anywhere in either system, it found the right system and the right fault eight times out of ten.
Aristotle, recovered
Any new way of reasoning should first give back the old logic that we know is right. Physicists call this the correspondence principle: a new theory has to agree with the old one where the old one is secure.
So we read Aristotle’s four classical statements in ELC’s own terms. “S is P” becomes the share of S that passes into P, which MINOS writes as an angle. Every S is P is the end where everything passes. No S is P is the end where everything is held. Some S is P and some S is not P are everything short of one end or the other. Checked on every small case, 1,302 pairs of terms, every one came out right.
Then the syllogism, Aristotle’s two-premise argument such as every M is P, every S is M, so every S is P. We gave Minotaur none of the classical rules. It had only the angle, the fact that what passes and what is held always add up to the whole, and the MINOS rule for chaining two elements one after another. Out of the 256 possible forms it proved exactly the 24 that are valid, proved nothing false, and refused the other 232, each with a reason. It even said, for each argument that needs it, which term has to be non-empty for the argument to hold, which matches the classical account term by term.
One of the oldest mistakes in logic, the undistributed middle (every S is M, every P is M, so every S is P), is, in this reading, an attempt to chain two elements without a transport between their frames. It’s the same mistake, at the scale of a sentence, as leaving the transport out between the production line and the packing station.
How It Did Against a Language Model
How it was tested
Every result in this post was produced under the same rules:
- The pass marks were written down before each run. Nothing could be tuned afterwards to fit.
- The right answers came from someone else. Each answer was scored against a checker written separately, from the format’s rules alone, sharing no code with Minotaur.
- The tests were blind. The boiler and the police interview were written by AI agents that saw only the format. Minotaur’s code was fingerprinted and frozen before each one was opened.
- There was a competitor. A fresh language model, given the same system described in plain words, answered every question by reasoning in words, with no code allowed, and was scored by the same checker.
- The claims are made only on fresh tests. Development was done on separate data.
The results
On the police interview and the two learned systems, Minotaur matched the language model, on one ordinary processor core and with every answer certified. Where there was nothing described to start from, reasoning over fixed facts couldn’t begin.
Where ELC Earns Its Keep
Each of the older methods does one kind of reasoning well, in its own specialty, once it’s handed a description. Minotaur does every kind with one operation, typed and certified, on one processor.
And where the system isn’t described, ELC can’t be replaced. For every other approach, the question is what it would have to be handed to do what Minotaur did.
ELC supplies, from its form alone, what the others have to be handed: the roles of drive, constraint and logic, the places where a fault can be, and the frames and transports between systems. In the learned tests, ELC’s own algebra decided which learned part was the drive and which the constraint. Every diagnosis was a fault of a typed role. And leaving the transport out made the predictions up to twelve times worse.
Where This Leaves Us
A language model reasons the way people do because it learned from people writing. That has made it the best general reasoner we have, and also a reasoner that inherits our habits: confident when it shouldn’t be, swayed by framing, and unable to show what its answers rest on. The alternatives of the previous seventy years either had to be handed the model or had nothing to reason on.
Minotaur’s brain reasons in a different way. It doesn’t imitate how people write about a system; it holds the system itself in ELC’s typed roles, whether described or learned from data, and answers every kind of question with one operation: hold some things, cut some, leave some free, and settle. Every answer comes with the chain of steps it actually took and a certificate of what kind of answer it is, and gives the same result every time it’s run. Head to head on blind tests, it reached the level of a current language model, on one ordinary processor.
One network, one operation, every kind of reasoning: and the working is always shown.
The ideas behind Minotaur, from the three roles of Energy, Logic and Control to the mathematics of MINOS, are set out on the MINOS page. The mathematics itself is in the paper An Operational Representation of Systems: A Worked Construction in Lattice Gauge Theory (doi:10.5281/zenodo.23491024). The first post, Introducing Minotaur: A GPU’less AI Architecture, describes the ELC adapter and its tests on real regulations. The ELC adapter and the ELC neural network are patent pending.
