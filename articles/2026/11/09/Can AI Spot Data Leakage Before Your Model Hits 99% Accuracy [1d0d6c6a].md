---
id: "1d0d6c6a5f33d866"
title: "Can AI Spot Data Leakage Before Your Model Hits 99% Accuracy?"
url: "https://kdnuggets.com/can-ai-spot-data-leakage-before-your-model-hits-99-accuracy"
link: "https://kdnuggets.com/can-ai-spot-data-leakage-before-your-model-hits-99-accuracy"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-09T15:00:00Z"
published_date: "2026-11-09"
collected_at: "2026-11-10T13:04:10Z"
authors: ["Nate Rosidi"]
language: "en"
summary: "4 classic leaks, planted in real data, tested cold on 4 models."
tags: []
orgs: ["Anthropic", "Amazon"]
topics: ["models & research"]
content_source: "fulltext"
word_count: 1846
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/Rosidi-Can-AI-Spot-Data-Leakage-1.png"
discussion_url: null
score: null
comments: null
community: null
---

# Can AI Spot Data Leakage Before Your Model Hits 99% Accuracy?

KDnuggets · Nate Rosidi · 2026-11-09

Can AI Spot Data Leakage Before Your Model Hits 99% Accuracy?
4 classic leaks, planted in real data, tested cold on 4 models.
Every data scientist knows the feeling: a model comes back with 99% accuracy, and instead of celebrating, we get suspicious. Nine times out of ten, the cause is leakage: some piece of information in the training data that would not actually be available at prediction time.
We wanted two real numbers. First, how dramatic is that accuracy jump on real data, not a toy example? Second, if we describe the pipeline to an AI model before anyone runs it, with no hint that anything is wrong, does it catch the leak, and does the answer change depending on which model we ask?
So we took four real data projects, planted a different, well-known leakage pattern into each one, trained a real model with and without the leak, and recorded the actual numbers.
Then, separately, we described each pipeline in plain terms and asked four Claude models, from fastest to strongest, what they would flag before trusting the result.
Setting Up the Experiment
Each leak takes a different route into the pipeline: a feature that mechanically defines the label, a feature built with future information, a split that ignores relational structure, and a preprocessing step done in the wrong order.
For the AI side, we tested Claude Haiku 4.5, Claude Sonnet 5, Claude Opus 5, and Claude Fable 5.1, across the speed and capability range we have access to.
We are naming exactly which models we tested and not implying a cross-vendor comparison, since that is not what we ran. Each model got a fresh session with zero memory of the others, a closed-book description of the pipeline, features, or code, and no ability to run anything. None were told a leak existed.
Case 1: The Feature That Already Knows the Answer
For this case, we are using datasets from the project Prediction of Stock Price Direction.
The task: predict whether Amazon's closing price lands higher than that same day's opening price. Here, Label equals 1 if Close is greater than Open, 0 otherwise.
Here is a sample of one of the datasets, in this case AMZN_train.csv:
Comparing Leakage and Non-Leakage Performance
Feed the model that same day's Close and Adj Close alongside Open, High, Low, and Volume, and validation accuracy hits 97.0%, with an area under the curve (AUC) of 0.999.
Restrict it to only the prior day's open, high, low, close, and volume, nothing from the day being predicted, and accuracy falls to 51.6%, AUC 0.476: a coin flip. That difference, 97% versus 52%, is the whole article in one number.
Checking What AI Caught
All four models caught it instantly, for the right reason: Close defines the label.
Haiku called it "circular."
Sonnet said the model "can reconstruct the label with a single comparison."
Opus went further, unprompted: "if High equals Open, the day never traded above the open, so the label must be 0." It also set the honest expectation itself, that a fair model should land "in the low 50s for accuracy," almost exactly what our clean run produced.
Case 2: The Dataset That Already Told You Where the Line Is
For this case, we are using datasets from the project Delivery Duration Prediction. We are using a subset of its dataset, historical_data.csv.
The task: predict duration_sec, the seconds between an order being placed and delivered, computed as actual_delivery_time minus created_at.
DoorDash's historical_data.csv holds 197,428 orders, one row each, 16 columns. The target is duration_sec: actual_delivery_time minus created_at, the seconds from when the order was placed to when it arrived.
The columns the model actually saw:
We left out market_id, store_primary_category, and order_protocol: region, restaurant category, and order channel. Not because they're useless, just because encoding 74 different restaurant categories had nothing to do with the leak we were testing.
We added one engineered feature, a store's average delivery duration, computed in two ways:
# leaked: uses every row, including the ones about to be scored
store_avg = df.groupby("store_id")["duration_sec"].transform("mean")
df_shuffled = df.sample(frac=1.0)  # random split on timestamped data
# clean: only training-period orders, then a chronological split
store_avg = train.groupby("store_id")["duration_sec"].mean()
train["store_avg"] = train["store_id"].map(store_avg)
test["store_avg"] = test["store_id"].map(store_avg)
That one engineered feature carries two separate leaks.
First: store_avg is built by grouping the whole table, train and test rows together, by store_id and averaging duration_sec, the exact thing we're predicting, then copying that average onto every row.
For a store with only a handful of orders, the average sits close to that row's own duration_sec, so the model is reading a smoothed copy of the answer.
Second: created_at is a timestamp, so this table is inherently ordered in time, and shuffling it before the 80/20 split lets training rows fall chronologically after test rows. A real production model only ever sees orders placed before the one it is asked to predict.
Comparing Leakage and Non-Leakage Performance
We scored both versions with root mean squared error (RMSE), in seconds, the same unit as duration_sec. It answers "how far off is a typical prediction," with large misses counted more heavily. For scale, the average order here takes about 47 minutes to deliver (median 44), so an RMSE of 14 to 16 minutes means the honest model's typical miss is close to a third of an average delivery.
The leaked version reports an RMSE of 862.7 seconds against 949.9 seconds for the honest version, an apparent 9% improvement that comes entirely from the leak, not from the model learning anything real.
Checking What AI Caught
Every model caught the store-average leak. Only three of four caught the second problem: shuffling a timestamped table instead of splitting it chronologically. Sonnet, Opus, and Fable all raised it unprompted. Fable's phrasing was the clearest: "the training set can contain orders that occurred after some of the test-set orders."
Haiku stopped after fixing the store-average feature and never mentioned the split. Opus alone added that DoorDash's own data already contains a baseline worth beating, estimated_order_place_duration plus estimated_store_to_consumer_driving_duration, and that RMSE without that comparison proves little. Readers can reproduce this one themselves.
Case 3: The Leak You Can't See in a Single Column
For this case, we are using datasets from the project Fraudsters Detection (Revolut).
The task: predict IS_FRAUDSTER for each user from their profile and transaction history.
Revolut's schema is naturally one-to-many: one users table with a label, IS_FRAUDSTER, and one transactions table with many rows per user. After joining them, one user can therefore appear across many transaction rows, all carrying the same fraud label.
The prediction problem is really about identifying fraudulent users, even though the model is trained on transaction-level rows.
Transactions table:
Users table:
Split the joined transaction rows at random, and 1,950 of 2,246 users end up with transactions on both sides of the split.
That means the test set often contains a different transaction from a user the model already saw during training.
Comparing Leakage and Non-Leakage Performance
A model trained this way scored AUC 0.960, where a higher AUC means better separation between fraudsters and non-fraudsters. Split by user instead, so nobody's transactions cross the line, and the honest AUC is 0.898: a solid model, just not the one that was reported.
Checking What AI Caught
All four models named the exact mechanism unprompted: the label lives at the user level, so a row-level split lets the model partly recognize a user it has already seen rather than detect fraud in a new one.
Opus's answer was the most complete, pointing out that the real sample size here is the number of users, not transactions, and that any field populated only after a fraud investigation closes is its own separate leak regardless of the split.
We ran into that ourselves while building this experiment: Revolut's account-status field is ACTIVE for every non-fraudster and LOCKED for every single fraudster in the data, a feature so leaky we removed it before touching anything else.
Case 4: The Leak That Is Not in the Data at All
For this case, we are using datasets from the project Flagging Loans (Chime).
The task: predict bad_flag, whether a loan goes bad, from columns like dpd_30_cnt, past_billings_cnt, and two credit scores.
Chime's loan data is imbalanced: about 10% of loans are flagged bad_flag = 1, with columns like dpd_30_cnt, past_billings_cnt, and two credit scores. To compensate for that imbalance, the pipeline duplicates minority-class rows before training.
We tested one short snippet, no data, no metrics attached, just code…
X_bal, y_bal = oversample(X, y)  # duplicates minority rows first
X_train, X_test, y_train, y_test = train_test_split(
    X_bal,
    y_bal,
    stratify=y_bal
)
…against the same steps reordered, split first and oversample only the training half.
Comparing Leakage and Non-Leakage Performance
Oversample-then-split reported AUC 0.986. Split-then-oversample, evaluated on a test set that was never touched, reported 0.637: a real but modest model.
The problem is that duplicating rows before the split lets identical copies of the same loan land in both halves, so the model is partly graded on examples it has effectively already seen.
Checking What AI Caught
All four models flagged it cold, from the snippet alone, with no accuracy number to tip them off. Opus went furthest again, noting that stratifying on already-balanced labels "is harmless but meaningless," that neither step sets a random seed, and asking whether oversampling was the right call at all versus weighting the classifier or reporting recall at a fixed review budget instead of ROC AUC.
Conclusion: What Every Model Caught
Every model we tested, including the fastest and cheapest one, caught the specific leak we planted in every case, when asked directly to review the pipeline before trusting it.
That is worth stating plainly: these four patterns are not exotic, and a model asked the right question catches them.
The difference between models showed up in what came bundled with the primary catch.
Haiku answered correctly and briefly, and in Case 2 that brevity cost it a second real leak sitting next to the one it found.
Sonnet and Fable caught both problems whenever there were two.
Opus was the only model that, across all four cases, added something beyond the leak itself: an honest accuracy expectation, a baseline worth comparing against, a leak we had not even asked about, and a challenge to whether the fix we described was the right fix.
Asking a model to review a pipeline before trusting its numbers is cheap, fast, and caught four real, planted leaks every time in this experiment. Whether it also catches the second problem sitting next to the first one depends on which model you ask, and on how much of the pipeline any reviewer, human or AI, gets to see.
 
Nate Rosidi is a data scientist and in product strategy. He's also an adjunct professor teaching analytics, and is the founder of StrataScratch, a platform helping data scientists prepare for their interviews with real interview questions from top companies. Nate writes on the latest trends in the career market, gives interview advice, shares data science projects, and covers everything SQL.
