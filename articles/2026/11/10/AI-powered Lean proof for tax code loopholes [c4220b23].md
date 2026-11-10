---
id: "c4220b238445b0ae"
title: "AI-powered Lean proof for tax code loopholes"
url: "https://lexifina.com/blog/searching-the-tax-code-for-loopholes"
link: "https://lexifina.com/blog/searching-the-tax-code-for-loopholes"
source: "Lexifina"
domain: "lexifina.com"
source_type: "community"
collector: "reddit"
date: "2026-11-10T00:00:54Z"
published_date: "2026-11-10"
collected_at: "2026-11-10T13:04:10Z"
authors: ["SnooPeripherals5313"]
language: "en"
summary: "extremely serious post"
tags: ["r/singularity"]
orgs: ["US government"]
topics: ["policy & regulation", "search & media", "models & research"]
content_source: "fulltext"
word_count: 1581
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xs839w/aipowered_lean_proof_for_tax_code_loopholes/"
score: null
comments: null
community: "r/singularity"
---

# AI-powered Lean proof for tax code loopholes

Lexifina · SnooPeripherals5313 · 2026-11-10

Lean proof to search for US tax loopholes
Navier stokes? That will never make money. Instead, we compiled a Lean proof to find loopholes in the US tax code.
But first, a step back. This example is part of the vulnerability monitoring work we do at global law, a CC0 repo of versioned legislation and caselaw. Our argument is that we can point AI at a versioned record of the law to find contradictions and other key logical mistakes in our system of legislation and interpretation.
Loopholes are usually found by someone who knows two provisions well and sees that together they allow what neither allows alone. Instead, we wrote the rules down with no strategy built in, let a search try every sequence of moves they permit, and had a theorem prover check the result where the answer is already known, so that the method could be judged.
The rules
A Roth IRA is taxed at the front and never again, which makes it valuable to people with a long time to save. Congress limits who may contribute to one. The amount a single filer may put in shrinks between $150,000 and $165,000 of modified adjusted gross income and is zero above that.[1],[2],[3] Since 2010, though, there has been no income limit on converting a traditional IRA into a Roth IRA, and anyone may make a non-deductible contribution to a traditional IRA whatever they earn.[4],[5],[6] Put those two together and the income limit stops nobody: contribute to a traditional IRA, convert it the next day, and the money is in a Roth. Practitioners call this the backdoor Roth. It is widely treated as a loophole: the House voted to close it in 2021,[7],[8] and the chair of the Senate Finance Committee was reported the same year to be preparing a crackdown on Roth accounts used by the wealthiest savers.[9]
There is a catch, and then a way round the catch. When money comes out of a traditional IRA, all of a person's IRAs are treated as one account, and each dollar converted is deemed to be the same mix of taxed and untaxed money as the whole.[6] Someone with $100,000 of pre-tax savings in an old IRA who adds $7,000 of after-tax money and converts $7,000 is taxed on most of it. But money rolled from an IRA into an employer's 401(k) plan can only be the pre-tax part, and is treated as coming from that part first.[6] Move the old savings into the 401(k) and what is left in the IRA is all after-tax, so the conversion costs nothing. A separate route runs through the 401(k) itself: the plan can accept after-tax contributions up to the overall limit on additions, $70,000 in 2025, and move them into its own Roth account, the route known as the mega backdoor.[10],[11],[8]
Formalising search
We wrote these provisions in Lean, a programming language whose type checker can also check mathematical proofs. An earlier post discussed how far that kind of formalisation can reach in law.[12] Here the model is small. A taxpayer has five accounts: cash, the traditional IRAs taken together, the Roth accounts, and the pre-tax and after-tax parts of a 401(k). There are seven moves between them, each written from the provision that governs it, with the 2025 limits: contribute to a Roth IRA, contribute to a traditional IRA, convert, roll IRA money into the 401(k), defer salary, make an after-tax 401(k) contribution, and roll that into the plan's Roth account.
The search starts from a single filer earning $250,000, well above the Roth limit, with $100,000 of pre-tax money in a rollover IRA and $100,000 in savings. It tries every move with every amount the position offers, six moves deep across 345,075 positions, and asks how much can go into Roth accounts without tax. The answer is $77,000 in five moves: contribute $70,000 after tax to the 401(k) and roll it into the plan's Roth account, contribute $7,000 to a traditional IRA, roll the $100,000 of pre-tax IRA money into the 401(k), then convert the $7,000. That is the backdoor and the mega backdoor, in the order the backdoor needs, found without either being described. Without the roll-in, the same $7,000 costs $6,543 in tax; at $140,000 of income, the search simply makes a Roth contribution.
What the proofs add
The search stopped at six moves; the four proofs cover sequences of any length from any starting position. The first is a conservation law: pre-tax money leaves the IRAs only by being taxed or rolled into the 401(k). The second follows from it: without the roll-in, every pre-tax dollar is taxed on its way to the Roth, however the conversions are split or ordered (the whole-dollar rounding step was proved by hand). The third is that at every income above the limits, from any starting accounts, a permitted sequence puts $7,000 into a Roth with no tax, which is exactly what section 408A's income limit is meant to prevent. The fourth is a ceiling: in a year, no plan puts more than $77,000 of new money into Roth accounts tax-free, beyond after-tax money already held, and the search's plan reaches it, so it is the best one in the model. In simplified form:
theorem roth_ceiling (income : Nat) (moves : List Move) :
    ∀ before after, run income before moves = some after →
      after.roth − before.roth ≤ 7000 + 70000 + before.iraBasis + before.planAfterTax
                                   + (after.taxed − before.taxed)
Takeaways
None of this is news to a tax adviser, which is why it was chosen. Congress has looked at these routes too. The version of the Build Back Better Act passed by the House in November 2021 would have barred converting after-tax money from 2022 and so closed both.[7],[8] The bill stalled in the Senate, and the Inflation Reduction Act that replaced it in 2022 left the provision out.[13] Nothing enacted since has revived it, and both routes remain available in 2026.[14] What is new is that the routes and their limits fall out of the rules mechanically, together with a proof that nothing in the model does better.
The more interesting places to point this are those where no one has catalogued the interactions: provisions that were amended at different times, or a bill before it passes. A drafter could write the proposed change into the same model and ask the search whether the limit they are adding can be walked around, and the proofs would say whether a fix closes every route or only the one someone thought of. The model and the search are public in global-law; see the lean-proofs folder.
Isn't a lot of this deliberate? Law is grey on purpose. Often, yes. The detectors look for mechanical mistakes, not grey areas. Whether a gap is a mistake or a choice is a legal judgement, so every review gives a verdict, and most flags turn out to be lawful, cured, intended or errors in a corpus rather than defects in the law.
The law isn't software. Why apply software-style checks? It isn't, and these checks do not try to prove a statute correct. They work like a linter: they catch the mechanical slips, and use legislation to identify dangerous interpretations and loopholes.
Who benefits, and will legislators ever adopt this? Published law is public, so anyone can run the checks. Finding these mistakes used to be much more expensive; publishing them puts pressure on legislatures to repair them.
Limits
The model applies the pro-rata rule at each conversion, while the Code uses the value of all IRAs at the end of the year,[15] which is more forgiving about order: a conversion made before the roll-in, in the same year, is also tax-free. The plan the search found works on either reading, but other orderings would come out differently, and the next version should use the year-end rule. The second route depends on the employer's plan, and after-tax contributions by higher-paid employees are often cut back by the nondiscrimination test in section 401(m).[16] The model leaves out state tax, employer contributions and investment growth, and a proof shows only that the result follows from the rules as modelled.
References
- 26 USC § 408A(c)(3) <www.law.cornell.edu/uscode/text/26/408A>
- Internal Revenue Service, Notice 2024-80, ‘2025 Limitations Adjusted as Provided in Section 415(d), etc.’ (1 November 2024) <www.irs.gov/pub/irs-drop/n-24-80.pdf>
- Internal Revenue Service, Publication 590-A, ‘Contributions to Individual Retirement Arrangements (IRAs)’ <www.irs.gov/pub/irs-pdf/p590a.pdf>
- Tax Increase Prevention and Reconciliation Act of 2005, Pub L 109-222, s 512 <www.congress.gov/109/plaws/publ222/PLAW-109publ222.pdf>
- ‘Roth IRA Conversions in 2010’ (The Tax Adviser, October 2009) <www.thetaxadviser.com/issues/2009/oct/rothiraconversionsin2010/>
- 26 USC § 408(d)(2), (d)(3)(A)(ii), (d)(3)(H) and (o) <www.law.cornell.edu/uscode/text/26/408>
- Build Back Better Act, HR 5376, 117th Congress (as passed by the House of Representatives, 19 November 2021) <www.congress.gov/bill/117th-congress/house-bill/5376>
- ‘Build Back Better Act would curb retirement plans for the wealthy’ (CNBC, 19 November 2021) <www.cnbc.com/2021/11/19/house-passes-build-back-better-act-retirement-plans-for-the-wealthy.html>
- ‘The Ultrawealthy Have Hijacked Roth IRAs. The Senate Finance Chair Is Eyeing a Crackdown.’ (ProPublica, 2021) <www.propublica.org/article/the-ultrawealthy-have-hijacked-roth-iras-the-senate-finance-chair-is-eyeing-a-crackdown>
- 26 USC §§ 402(g), 402A(c)(4) and 415(c) <www.law.cornell.edu/uscode/text/26/402A>
- Internal Revenue Service, ‘COLA increases for dollar limitations on benefits and contributions’ <www.irs.gov/retirement-plans/cola-increases-for-dollar-limitations-on-benefits-and-contributions>
- Alan Yahya, ‘The auto-formalization of mathematics versus law’ (Lexifina, 7 September 2026) <lexifina.com/blog/auto-formalisation-of-law>
- ‘Backdoor Roth 401(k) and IRA rules for the wealthy survive — for now’ (CNBC, 20 December 2021) <www.cnbc.com/2021/12/20/backdoor-roth-401k-and-ira-rules-for-the-wealthy-survive-for-now.html>
- ‘Making a backdoor or mega backdoor Roth contribution in 2026’ (Mercer Advisors, 2026) <www.merceradvisors.com/retirement/making-a-backdoor-or-mega-backdoor-roth-contribution-in-2026/>
- Internal Revenue Service, ‘Instructions for Form 8606: Nondeductible IRAs’ <www.irs.gov/instructions/i8606>
- 26 USC § 401(m) <www.law.cornell.edu/uscode/text/26/401>
