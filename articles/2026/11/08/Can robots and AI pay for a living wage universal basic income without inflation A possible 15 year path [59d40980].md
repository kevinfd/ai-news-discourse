---
id: "59d40980a73e3115"
title: "Can robots and AI pay for a living wage universal basic income without inflation? A possible 15 year path"
url: "https://robotubi.pages.dev"
link: "https://robotubi.pages.dev"
source: "robotubi.pages.dev"
domain: "robotubi.pages.dev"
source_type: "community"
collector: "reddit"
date: "2026-11-08T15:05:54Z"
published_date: "2026-11-08"
collected_at: "2026-11-09T13:04:29Z"
authors: ["Competitive_Travel16"]
language: "en"
summary: "Automation spreads gradually, investment responds to taxes, inflation comes from demand versus capacity, and housing has its own market. It tests whether automation, public ownership, progressive taxes, cheaper essentials and a gradual phase-in can give every adult a UBI worth 100% of a living wage without sustained excess inflation and without the public capturing all automation profits. Its…"
tags: ["r/singularity"]
orgs: []
topics: ["agents & coding", "business & funding", "policy & regulation", "models & research"]
content_source: "fulltext"
word_count: 2194
paywalled: false
image: null
discussion_url: "https://www.reddit.com/r/singularity/comments/1xr0i1r/can_robots_and_ai_pay_for_a_living_wage_universal/"
score: null
comments: null
community: "r/singularity"
---

# Can robots and AI pay for a living wage universal basic income without inflation? A possible 15 year path

robotubi.pages.dev · Competitive_Travel16 · 2026-11-08

Automation spreads gradually, investment responds to taxes, inflation comes from demand versus capacity, and housing has its own market. It tests whether automation, public ownership, progressive taxes, cheaper essentials and a gradual phase-in can give every adult a UBI worth 100% of a living wage without sustained excess inflation and without the public capturing all automation profits. Its settings are independent of the static model below. To see the possible 15-year path, pick strategy 8 under Settings.
Everything the Dynamic model computes follows from the equations and parameters below. All money values are real 2025 dollars (deflated by the factor-cost price level), so coverage is unaffected by general inflation; inflation acts on nominal debt and interest. Time t is measured in years from the start of 2026.
1. State variables (16)
2. Differential equations
Ṙ = IR − R / LR,   IR = min(M, max(0, R/LR + (R* − R)/2))
Ṁ = min(gMM, IRdes − M) if demand exceeds capacity, otherwise −0.2 (M − IRdes);   Q̇ = IR
K̇C = IC − δCKC,   IC = max(0, δCKC + (KC* − KC)/1.5), capped at 75% growth a year; δC = 0.25
K̇ = IK − δK,   IK = min(0.24Y*, max(0, δK + (K* − K)/8)); δ = 0.06
Ė = λE(E* − E),   λE = 1 / yr
Ż / Z = gZ + φZ(Iauto/Y − 0.005)
Ḟ = ωF·O + (1 − χF)F·rdiv + cFY* + e·TR − pFF
ĖP = κEsE(1 − ω)Iauto − EP·(automation depreciation / automation capital)
Ḋ = (iD − πf)D + PD,   i̇D = (i − iD)/6
π̇e = 0.5[(1 − a)π + a·π* − πe],   d ln P/dt = πf = πe + κx,   Π̇ = (Πtarget − Π)/0.5
Ḣ = IH − 0.004H,   IH = min(capH, 0.004H + γH(1 + reform)(1 + 0.5τLVT)·H·max(0, pH/cH − 1))
Ḃ = (Btarget − B)/0.5,   Btarget = min(schedule, financed amount) under the financing rule
3. Production, wages and automation rents
Work is measured in billions of human-hour equivalents. Physical (P) and cognitive (C) work combine as Cobb-Douglas with the physical share of the 2025 wage bill θ = 4.0/15.8; output adds conventional capital with share α = 1 − 15.8/30.8 = 0.487.
Λj = Hj + min(Mj, aj(t)/(1 − aj(t))·Hj),   Λ = ΛPθΛC1−θ,   Y* = Z·KαΛ1−α
wP = (1 − α)θY/ΛP,   wC = (1 − α)(1 − θ)Y/ΛC   (2026: $34/h and $68/h)
aj(t) = 0.02 + (ajmax − 0.02)·logistic((t − tj)/4), normalized to start at 0.02
Machines are paid their marginal product, so more machines in the same tasks lower the value of each machine-hour; displaced-wage values overstate rents. Robot services MP = R·hR·qR(t); AI services MC = KC(rn + δC)/(k(t)·wC,2025). Publicly owned machines produce ηpub as much.
cR = pR(rn + 1/LR)/hR + u·pR/hR + kW·$0.08 + supervision(t),   pR = max(floor, pR0(Q/0.03)−b), b = −log2(1 − LR)
Rent = wPMP + wCMC − cRR·hR − (rn + δC)KC
Machine costs already include a normal return rn on the capital, so "rent" is profit above a normal return. Adoption: a fraction f of the technical frontier is used, f = m³/(m³ + h³), where m is the cost margin 1 − cost/wage. For private owners m is reduced by taxes that reach normal returns, m·max(0, 1 − εIτadd) with τadd = τR(1 − ν) + 0.2(τtop − 0.43) (top personal rates reach only part of the marginal investment, which is also financed by pensions, retained earnings and foreign owners; Yagan 2015 found no investment response to the 2003 dividend tax cut), and raised by public support sE. Public owners use half the hurdle.
4. Allocation of automation rents (no double counting)
Rent+ = Rc + RP,   Rc = πc·Rent+ (consumers, via lower prices),   RP = retained profits
O = rnVA + RP = owner income;   O = ωFO (fund) + ωEO (public equity) + (1 − ω)O (private)
Rent tax TR = τR·(1 − ω)RP; existing capital tax 34.7% on the private remainder
Capture of retained profits κ = [ωRP + TR + 0.347((1 − ω)RP − TR)] / RP
Ownership shares use market value, which capitalizes rents (VA + 0.65·RP/0.06), so buying ownership of rents costs money. Fund and equity income is never also taxed as private profit. The consumer share lowers living-wage prices and government purchase costs and is never counted as revenue. A ceiling caps τR so that κ ≤ ceiling.
5. Demand, inflation and monetary policy
C = χ[mW·after-tax wages + mT(UBI + transfers) + mK·after-tax capital income + 0.03·private capitalized rents] / Π
Demand = C + Iauto + IK + IH + G − 0.03Y*, reduced by (3I + 0.5C)(r − r*)
i = r* + πe + 1.5(πe − π*) + 0.75x,   i ≥ 0 (zero lower bound); with rates held constant, i = r* + πe
x = (Demand − Y*)/Y*, solved jointly with the policy rate;   Y = Y*(1 + 0.3x) if x > 0, else Y*(1 + x)
Consumer inflation π = πf + Π̇/Π; only the 3-year average overshoot counts as sustained excess inflation
The UBI raises demand because recipients spend more of each dollar (0.95) than capital owners (0.35), so a fully financed UBI can still add inflation pressure. A deficit adds demand only through what households and firms spend. One-time price drops from automation appear in Π, not in πf. χ is set so the 2026 output gap is zero.
6. Labor, housing and the living wage
LF = adults × working-age share(t) × participation, participation = p0(1 − withdrawal × min(1.5, B/LW))
E* = LF(1 − 4.2%)(1 − disp × machine share) × min(1.02, Y/Y*) × (1 − reall × displacement rate)
pH = (DH/H)1/εH,   DH = 1.026·H0(N/N0)(household income / 2026)0.5,   cH = 1 − 0.45·(automated construction share)·margin
pricek = 1 − min(1, πc·pmk)[lpk·min(1, aPdepeasek)mP + lck·min(1, aCdepeasek)mC] − resk·resource decline(t)
LWadult = Σk basek(region, household mix)·pricek; housing uses pH/pH,2026
Bases are MIT after-tax expenses per adult: a mix of single adults and two-adult households, weighted by region. Child costs are half the difference between the two-adult-two-child and two-adult budgets (child care optional). The medical line can be scaled for health-coverage assumptions.
7. Government budget identities and the financing rule
Revenue = 0.30·wages + 0.347·(conventional capital income − depreciation) + existing taxes on private automation income + (1 − e)TR + progressive tax + LVT + 0.07·C + public-equity dividends
Spending = other(Y*) + G·(1 − procurement saving) + (transfers − integrated offsets) + support sE + cFY* + UBI − fund payouts
PD = Spending − Revenue,   Ḋ = (iD − πf)D + PD
The debt safeguard uses net debt, debt minus public-fund assets, so a fund financed by borrowing is a balance-sheet swap, not a loss.
Debt-stabilizing rule: PD ≤ [(g − (iD − πf))·min(d, 0.99) − 0.05·max(0, d − 0.99) + extra − 0.5·min(0, x)]·Y*
Under "pay only what is financed", the UBI rises only while the rule holds, so the UBI never worsens the debt ratio except as allowed. Once the UBI reaches its scheduled level, any further room under the rule is returned as lower wage taxes (phased in over about a year), so automation revenue does not pile up as fiscal drag. "Other spending" is set so the 2026 primary deficit is 3% of GDP. Progressive tax revenue = τtop·Z − 0.43·base, where base is the top 1%'s income above the bracket threshold (a tenth of wages plus a quarter of private capital and automation income, about $4T in 2026), Z = base·((1 − τtop)/0.57)ETI is the income still reported at the higher rate, and 43% is today's combined top rate. With ETI = 0.25, revenue peaks at τtop = 1/(1 + ETI) = 80%. Capture of automation profits is capped at 95%; the top income tax rate can go to 93%. The land value tax applies to land rents (assumed $2.0T in 2026, rising with rents and population), cannot be shifted to tenants, and raises housing supply response.
8. National-income identity, numerics, optimization and stability
wPΛP + wCΛC = (1 − α)Y (Euler), so wages + machine income + capital income = Y every year (checked)
Integration: classical fourth-order Runge-Kutta with a quarter-year step; lagged auxiliaries (last step's demand, coverage, rents and growth) are updated once per step, so those feedbacks are first-order accurate. Halving the step changes target-year coverage by about one point (checked on the Results tab).
Optimization: 40 Latin-hypercube samples of 11 policy settings, then coordinate pattern search with step halving until the step is under 2% of each range or 160 evaluations. Constraint violations get a penalty of 50 per unit. It returns a local solution and reports convergence; it does not claim a global optimum.
Equilibrium and stability: without automation the model reproduces the 2026 economy at steady growth. Employment, capital, expectations, prices and the UBI all adjust toward targets with positive speeds, which is stable when monetary policy responds more than one-for-one to inflation (the Taylor principle). With rates held constant, or at the zero bound, demand shortfalls can persist; the model then reports a slump rather than assuming it away.
9. Parameters, units, evidence and scenarios
10. Evidence audit and what changed from the static model
        - Growth. The static model treated all compounded GDP growth as additional automated work. Here baseline productivity growth (CBO projects labor productivity around 1.3–1.5% a year) is separate from automation.
- Surplus. Displaced wages overstated automation surplus. Here machines earn their marginal product and pay their full cost, including a 7% normal return.
- Physical vs. cognitive split. 41% of jobs and 28% of wages are physical (BLS OEWS occupational groupings, rough). The wage-bill split sets θ.
- Robot costs. Unitree's G1 lists near $16k and the Asimov open-source kit targets $15k, with parts bills near $10k; Morgan Stanley estimates Tesla Optimus's parts bill near $55k. The model starts a capable general-purpose humanoid at $40k and lets the learning curve take it toward a $12k floor ($6k optimistic, $20k conservative). Productivity (about half a worker today) is an analyst figure, not market data. At these prices supervision and software, not the robot itself, dominate the hourly cost. The learning rate, price floor, service life and utilization are assumptions with no adequate evidence yet.
- AI cost and electricity. The mature AI cost share and its electricity share are speculative; the 4,000 TWh comparison is observed US use.
- Investment response. Studies of bonus depreciation (Zwick and Mahon 2017) find large responses to the after-tax cost of investment; pure rent taxes (cash-flow taxes) are neutral in theory. Real designs fall in between, set by the normal-return allowance.
- Labor response. The OpenResearch $1,000-a-month trial found work fell about 4–5%; Alaska's dividend showed no employment drop. No evidence exists for a living-wage UBI; the 8% default is an assumption.
- Housing. Supply elasticities vary widely by metro (Saiz 2010); the national housing response here is an assumption calibrated to about 1.4 million completions a year.
- Fund returns. Large diversified sovereign funds have earned roughly 4–6% real over long periods; the model adds random annual shocks in the uncertainty analysis.
- Program replacement. Only cash programs that overlap with a UBI are offset, dollar for dollar up to the UBI, with top-ups kept. Health care and disability programs are never offset.
- Living-wage benchmark. MIT's figures are after-tax budgets for specific places; the "US blend" weights are a model assumption, not a national estimate.
- Land rents. The $2.0T base for land rents is an assumption (US land is valued around $40T or more; see Larson 2015).
Limitations: one aggregate good plus a living-wage basket; closed economy apart from a fixed trade deficit; no distribution of incomes within groups; no political feasibility; no migration; financial-market risk only as fund-return noise; the wealth effect and spending shares are uncertain and shape the inflation results; entrepreneurship and competition enter only through pass-through and the competition-policy setting.
11. Sources
        - Observed: MIT Living Wage Calculator (Arizona, California, Mississippi; updated February 15, 2026).
- Observed: BEA GDP and compensation of employees.
- Observed: BLS Occupational Employment and Wage Statistics.
- Projections: CBO Budget and Economic Outlook (debt, deficits, productivity, population).
- Observed: USDA ERS Food Dollar series (labor is 54 cents of the food dollar, 2024).
- Observed: Vivalt et al., NBER w32719 (OpenResearch cash-transfer study); Jones and Marinescu (2022) (Alaska Permanent Fund Dividend).
- Research: Acemoglu and Restrepo (2019), automation and new tasks; Zwick and Mahon (2017), tax policy and investment; Saez, Slemrod and Giertz (2012), elasticity of taxable income; Saiz (2010), housing supply.
- Projection: McKinsey Global Institute (2025), technical automation potential.
- Observed: LBNL data-center energy report (2024); Federal Reserve Z.1; Census housing vacancy survey; Larson (2015), value of US land.
- Observed: Norway Government Pension Fund Global returns.
- Prices: Asimov open-source humanoid kit (Hackaday, 2026); humanoid bill-of-materials estimates (Grab a Robot, 2026). Tax history: the top federal income tax rate was 92% in 1952–53 and 91% from 1954 to 1963.
Where no adequate evidence exists (mature robot productivity and prices, AI cost at maturity, labor response to a full living-wage UBI, rent-tax neutrality in practice), the parameter is tagged Spec or Asm and given a wide conservative-to-optimistic range.
