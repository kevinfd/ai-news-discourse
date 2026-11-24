---
id: "20801fb9ef942d12"
title: "How Has Generative AI Changed the Text of Securities Reports?"
url: "https://note.com/kaki_koji/n/n5399b2ecf38a?hl=en"
link: "https://note.com/kaki_koji/n/n5399b2ecf38a?hl=en"
source: "note"
domain: "note.com"
source_type: "mainstream_news"
collector: "bingnews"
date: "2026-11-23T04:50:00Z"
published_date: "2026-11-23"
collected_at: "2026-11-24T13:04:20Z"
authors: ["柿小路"]
language: "en"
summary: "In our previous article, we conducted a survey on the actual state of how companies mention generative AI in their securities reports (yuhō) for fiscal years 2022–2025. As a follow-up, this article an ..."
tags: []
orgs: []
topics: ["models & research"]
content_source: "fulltext"
word_count: 3124
paywalled: false
image: "http://www.bing.com/th?id=ONUT.HXRwxdv0h4YXjvb1M1QJpQ&pid=News"
discussion_url: null
score: null
comments: null
community: null
---

# How Has Generative AI Changed the Text of Securities Reports?

note · 柿小路 · 2026-11-23

How Has Generative AI Changed the Text of Securities Reports?
In our previous article, we conducted a survey on the actual state of how companies mention generative AI in their securities reports (yuhō) for fiscal years 2022–2025. As a follow-up, this article analyzes whether the text in securities reports has changed for companies that have started using generative AI internally, and how such changes might affect the usefulness of information for investors.
The analysis revealed that companies reporting internal use of generative AI showed a decrease in the similarity of their Management's Discussion and Analysis (MD&A) compared to the previous year during the year of adoption, along with reduced variance in sentence length. Furthermore, one year after adoption, the tone became slightly more positive. These were all minor changes, and there was no evidence of a decrease in the proportion of numbers or proper nouns (specificity). On the other hand, the rise in tone occurred in areas that cannot be explained by business performance alone, and it is currently impossible to determine whether this represents disclosure of future prospects or a bias toward optimistic writing.
1. Hypothesis
It has been pointed out that text created by generative AI has characteristics that differ from text written by humans. de Villiers et al. (2023) note that text output by generative AI tends to be biased toward positive expressions with a lack of negative information, features simple sentences with little variation in sentence length, and lacks company-specific information while relying on clichés. However, these are observations based on case studies and have not been empirically proven. In this paper, we translate these observations into a form that can be measured in the MD&A of securities reports and have established the following five hypotheses. The hypotheses compare companies by dividing them into the following three groups (details of the classification are explained in the next section).
1. Companies using it internally: Companies that stated in their securities reports that they use generative AI internally 
2. Companies that only mentioned it as an external environment: Companies that mention generative AI but have no descriptions of its use or provision 
3. Companies with no mention: Companies where the term generative AI never appears in their securities reports
Hypothesis E is intended to distinguish whether the changes observed in (1) are due to the use of generative AI or are changes common to companies that discuss generative AI.
2. Analytical Framework
Three groups for comparison
Based on the eight major categories created in the previous survey, companies were divided into three groups based on their descriptions of generative AI in securities reports from fiscal years 2022 to 2025.
- 1. Companies using it internally (509 companies): The fiscal year in which sentences classified as "internal use/human resource development" first appeared was defined as the company's year of adoption. The breakdown of the adoption year is: 6 companies in FY2022, 86 in FY2023, 146 in FY2024, and 271 in FY2025
- 2. Companies that only mentioned it as an external environment: Companies that mention generative AI but have never used sentences related to "internal use," "providing it," "demand creation," or "research and development." These are primarily companies that describe the spread of generative AI as a change in the business environment in a few sentences
- 3. Companies with no mention: Companies where the term generative AI never appears in their securities reports from fiscal years 2022 to 2025
Groups (1) and (2) were each compared with (3). Note that AI-related terms appearing in securities reports prior to fiscal year 2021 were not used to determine the year of adoption.
Selection of comparison subjects using propensity score matching
Companies that adopt generative AI are highly likely to have different characteristics from companies in group (3), such as being larger in scale. Therefore, we estimated propensity scores based on company characteristics in fiscal year 2021, before generative AI became widespread (log of total assets, sales growth rate, debt ratio, ROA, accounting standards, and log of MD&A character count), and paired each company with one company from group (3) within the same industry (33 TSE industries) that had a similar propensity score (1-to-1, without replacement, caliper set to 0.2 times the standard deviation of the propensity score logit).
Estimation method (LP-DiD)
We compared the changes from the "year before adoption" to the "year of adoption and subsequent years" for the same company between group (1) (or (2)) and the matched group (3). Since the year of adoption differs by company, we used a method (LP-DiD; Dube et al., 2025) that performs comparisons for each adoption year and then calculates a weighted average based on the number of treated companies. We also tested whether the difference three years and two years prior to adoption was zero (pre-trend). Standard errors were calculated by clustering for each company.
Measuring with text excluding generative AI sentences
Before calculating the indicators, I removed sentences containing the words for generative AI. This ensures that I am measuring whether other parts of the text have changed rather than a mechanical change caused by the fact that "I added talk about generative AI, so the text changed."
3. Measured indicators
I created the following seven indicators for the MD&A ("Management Policy, Business Environment, and Issues to be Addressed" and "Analysis of Financial Position, Operating Results, and Cash Flows by Management").
4. Analysis results: How has the text changed?
① Companies using it internally
The estimation results for ① vs ③ are as follows (** is significant at the 5% level, * at the 10% level).
- Became less similar to the previous year in the year of adoption (-0.015): The MD&A in the year of adoption had less overlap in the words used and their frequency compared to the previous year's MD&A. Afterwards (1 year later, 2 years later), it did not move in the direction of becoming more similar to the previous year, nor did it move further away.
- Variation in sentence length decreased in the year of adoption (-0.22 words): The average sentence length did not change, meaning that the difference between long and short sentences narrowed and sentence lengths became more uniform.
- Tone became slightly more positive one year later (+0.020): The proportion of negative words also showed a downward trend.
- There were no significant changes in readability, average sentence length, or concreteness: Concreteness tended to decrease one year later, but it was not significant (p=0.11).
For all indicators, no difference from ③ was observed before adoption (3 years ago, 2 years ago). Also, the magnitude of the changes was small in all cases; the +0.020 in tone is about 0.14 times the standard deviation of tone, the -0.015 in similarity is about 0.11 times, and the -0.22 words in sentence length variation is only about 1% of the average. Even in estimations where covariates were adjusted by regression (including the level of tone in fiscal year 2021), the results were almost the same.
② Companies that only mentioned it as an external environment
In ② vs ③, no significant changes were observed in any of the seven indicators (the variation in sentence length had a p=0.04 in the pre-trend test, so it cannot be judged because there was a difference before adoption). However, ② is small with 196 pairs, and does not have enough precision to say definitively that "it did not change." For example, similarity with the previous year tended to decrease, with -0.025 (p=0.11) one year later and -0.029 (p=0.14) two years later.
5. Additional verification ①: Did it change because it was "written" with generative AI?
At least two explanations can be considered for the change in ①. One is the explanation that the text changed because generative AI was used to write the MD&A. Another is the explanation that the business or organization changed due to the introduction of generative AI, and the content written changed, or that the preceding and following text was rewritten because they started writing about generative AI anew.
Therefore, I also compared companies that stated they provide generative AI as their own product or service (the year in which the sentence in the major category "provide" first appeared is taken as the year of adoption; 297 pairs excluding companies corresponding to ①) using the same method.
- The decrease in similarity and the change in sentence length also occurred to a similar extent in companies that provide it: The decrease in similarity was of almost the same magnitude, and the variation in sentence length also decreased to a similar degree (it did not reach the significance level due to the small number of companies).
- The increase in tone was only seen in companies that use it in-house.
From this, it can be inferred that the decrease in similarity and the change in sentence length in the year of introduction are not unique to using generative AI in-house, but are changes that occur in the year when companies begin to describe generative AI for the first time. Although sentences containing the word 'generative AI' are excluded, it is thought that adding new topics also leads to the rewriting of preceding and following sentences. On the other hand, the increase in tone is a candidate for a change unique to companies that use it in-house.
6. Additional Verification (2): Can the increase in tone be explained by performance?
Even if the tone becomes more positive, if it merely reflects an improvement in performance, it cannot be said that the way of writing has changed. Therefore, we decomposed the tone into a 'part that can be explained by performance, etc.' and a 'part that cannot be explained'.
The decomposition method followed Kato and Goto (2021), which targeted MD&A in Japanese securities reports. We regressed the tone of all companies and all years on the following variables (Pooled OLS including year dummies), and defined the predicted values as the 'explainable part' and the residuals as the 'unexplainable part (adjusted tone)'.
- Explanatory variables: 10 variables: ROA, stock returns, accounting accruals, market capitalization, price-to-book ratio, ROA volatility, number of business segments, years since listing, extraordinary income/loss, and readability. From the 12 variables of Kato and Goto (2021), we excluded stock return volatility and the number of regional segments. The former requires daily/monthly stock prices, and the latter is not disclosed as a numerical value in the XBRL of securities reports, so it cannot be created from securities reports.
- Handling of stock prices: Since no free stock price database could be found, market capitalization was calculated from the PER and earnings per share stated in the securities reports. For years where the PER was not stated due to a deficit, the stock price was back-calculated from the definition of Total Shareholder Return (TSR) and dividends per share.
- Years since listing: The year of listing was read from the 'History' section of the securities reports.
As a result, for the 27,297 company-years included in the regression, the estimation results for (1) vs (3) were as follows.
The increase in tone in (1) occurred almost entirely in the part that cannot be explained by performance, etc.. In other words, the tone did not become positive because performance or stock prices improved. This result did not change even when adjusting for covariates in the regression or when decomposing by including firm fixed effects.
7. Impact on Information Usefulness
We organize the results obtained so far by applying them to the four aspects of information usefulness and comparing them with the points made by de Villiers et al. (2023).
- Novelty of information: In the year of introduction, the similarity with the previous year's MD&A decreased. There is research suggesting that the market reacts more to MD&A with larger changes from the previous year (Brown & Tucker, 2011), so if new information has been added, it is a plus for usefulness. However, similarity decreases even if the same content is just rephrased. Also, if, as de Villiers et al. (2023) point out, there are many clichés in generative AI text, then the MD&A from years written by humans were similar to each other, and only in the year of transition to generative AI did it become dissimilar to the previous year, and thereafter it is thought that it will become similar again among sentences written by generative AI. The decrease in the year of introduction is consistent with this view, but whether the similarity increases thereafter cannot be confirmed at this time, as there are only 63 companies that can be observed up to two years later.
- Understandability: Readability did not change, and the variation in sentence length decreased. de Villiers et al. (2023) point out that generative AI text has simple sentences and small fluctuations in sentence length, so the standardization of sentence length may be a sign that the sentences have become simpler. In terms of readability, it is a slight plus, but if the number of formulaic, simple sentences has increased, it means that the information has decreased.
- Concreteness: The proportion of numbers and proper nouns did not decrease significantly. The concern that using generative AI dilutes the concreteness of descriptions (de Villiers et al., 2023) was not confirmed in this analysis.
- Neutrality: The tone became positive in a way that cannot be explained by performance. This is also consistent with the point that generative AI text tends to be biased toward positive expressions (de Villiers et al., 2023). This is the biggest point of contention.
There are two diametrically opposed interpretations of the tone that cannot be explained by performance.
- Interpretation as private information regarding future outlooks: Li (2010) and Kato & Goto (2021) show that adjusted tone has a positive relationship with the following period's performance. Based on this interpretation, companies in group ① have begun to describe future outlooks more frequently, meaning the usefulness of the information has increased.
- Interpretation as impression management: Huang et al. (2014) show that a positive tone that cannot be explained by performance is linked to a future decline in performance (tone management). Based on this interpretation, the descriptions by companies in group ① have become biased toward optimism, meaning the usefulness of the information has decreased.
Which interpretation applies cannot be determined without seeing whether the increase in the adjusted tone of companies in group ① is linked to subsequent performance. Since many companies have only recently introduced it, and there are few companies at this point for which we can observe the following period's performance, this remains a task for the future.
8. Points to note
- It is unknown whether generative AI was used to create the MD&A: Group ① consists of companies that stated they are "using generative AI in-house," and it cannot be observed whether generative AI was used for the creation of the MD&A itself.
- The effect is small: Changes in tone and similarity are about 0.1 times the standard deviation, and the variation in sentence length is only about 1% of the average.
- The observation period is short: Only 63 companies can be observed up to two years after introduction, and long-term changes, such as an increase in standardized descriptions after introduction, cannot be confirmed at this time.
- Instability of classification: The sentence classification (Sent-LDA) used for the judgment of group ① includes sentences whose assignment changes when the random seed is changed (44% of sentences were assigned to the same topic across all three random seeds).
9. Summary
The results for the five hypotheses are as follows.
- A Tone: Became positive after one year (Supported)
- B Readability: Only the variation in sentence length decreased (Partially supported)
- C Similarity to the previous year: Decreased in the year of introduction, but whether it becomes similar thereafter is unconfirmed (Partially supported)
- D Concreteness: No change (Not supported)
- E Comparison target: No change in ② (Supported. However, the sample size is small)
In the MD&A of companies that stated they use generative AI in-house, similarity to the previous year decreased in the year of introduction, the variation in sentence length decreased, and the tone became slightly more positive one year later. Among these, the decrease in similarity and the change in sentence length were seen to a similar extent in companies that provide generative AI as a product or service, so these may be changes associated with newly starting to describe generative AI. What was unique to companies using it in-house was the rise in tone, which occurred in areas that could not be explained by performance or other factors.
There is no evidence that the proportion of numbers or proper nouns has decreased, and at this point, it cannot be said that the usefulness of the MD&A has decreased due to the use of generative AI. However, the evaluation of its usefulness will be diametrically opposed depending on whether the rise in tone is a disclosure of future outlooks or a bias toward optimistic writing. I would like to verify the relationship with subsequent performance once the number of years after introduction has accumulated.
References
- Basnet, A., Elias, M., Salganik-Shoshan, G., Walker, T., & Zhao, Y. (2025). Analyzing the market's reaction to AI narratives in corporate filings. International Review of Financial Analysis, 105, 104378.
- Brown, S. V., & Tucker, J. W. (2011). Large-sample evidence on firms' year-over-year MD&A modifications. Journal of Accounting Research, 49(2), 309–346.
- de Villiers, C., Dimes, R., & Molinari, M. (2023). How will AI text generation and processing impact sustainability reporting? Critical analysis, a conceptual framework and avenues for future research. Sustainability Accounting, Management and Policy Journal.
- Dube, A., Girardi, D., Jordà, Ò., & Taylor, A. M. (2025). A local projections approach to difference-in-differences. Journal of Applied Econometrics, 40(7), 741–758.
- Hope, O.-K., Hu, D., & Lu, H. (2016). The benefits of specific risk-factor disclosures. Review of Accounting Studies, 21(4), 1005–1045.
- Huang, X., Teoh, S. H., & Zhang, Y. (2014). Tone management. The Accounting Review, 89(3), 1083–1113.
- Li, F. (2010). The information content of forward-looking statements in corporate filings—A naïve Bayesian machine learning approach. Journal of Accounting Research, 48(5), 1049–1102.
- Loughran, T., & McDonald, B. (2011). When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks. The Journal of Finance, 66(1), 35–65.
- Wang, Y., Wang, D. D., & Liu, R. (2025). Impact of digital technology adoption on the similarity of sustainability reports. Sustainability, 17(8), 3728.
- Kato, D., & Goto, K. (2021). Text analysis of securities reports: Management's disclosure of future outlooks and future performance. Monetary and Economic Studies, July 2021 issue.
- Lee, J. (2016). A study on text difficulty for Japanese language education. Waseda Japanese Language Education, 21, 1–16.
