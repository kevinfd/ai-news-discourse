---
id: "703f41c5d0806de4"
title: "How to Calibrate Your Classifier’s Probabilities in Scikit-learn"
url: "https://kdnuggets.com/how-to-calibrate-your-classifiers-probabilities-in-scikit-learn"
link: "https://kdnuggets.com/how-to-calibrate-your-classifiers-probabilities-in-scikit-learn"
source: "KDnuggets"
domain: "kdnuggets.com"
source_type: "newsletter"
collector: "rss"
date: "2026-11-17T15:00:00Z"
published_date: "2026-11-17"
collected_at: "2026-11-18T13:04:14Z"
authors: ["Shittu Olumide"]
language: "en"
summary: "In this tutorial, you will train two scikit-learn classifiers on a real dataset, expose their miscalibration with a reliability diagram and a Brier score, and fix it with Platt scaling and isotonic regression"
tags: []
orgs: []
topics: ["models & research"]
content_source: "fulltext"
word_count: 2194
paywalled: false
image: "https://www.kdnuggets.com/wp-content/uploads/KDN-Shittu-How-to-Calibrate-Your-Classifiers-Probabilities-in-Scikit-learn-scaled.png"
discussion_url: null
score: null
comments: null
community: null
---

# How to Calibrate Your Classifier’s Probabilities in Scikit-learn

KDnuggets · Shittu Olumide · 2026-11-17

How to Calibrate Your Classifier’s Probabilities in Scikit-learn
In this tutorial, you will train two scikit-learn classifiers on a real dataset, expose their miscalibration with a reliability diagram and a Brier score, and fix it with Platt scaling and isotonic regression
Your model says 0.9. You treat it as a 90% chance, set a threshold, and build a decision on top of it. Then you check the predictions the model scored near 0.9 and find that noticeably fewer of them were right. Nothing is broken. The model ranks cases well, and it is still a poor judge of how sure it should be.
That gap between a score and a real probability is what calibration closes. In this tutorial, you will train two scikit-learn classifiers on a real dataset, expose their miscalibration with a reliability diagram and a Brier score, and fix it with Platt scaling and isotonic regression. By the end, you will know how to calibrate classifier probabilities in scikit-learn and how to pick the right method for your data.
What Calibration Means
A well-calibrated classifier lets you read predict_proba as a confidence level. In the words of the scikit-learn user guide, among the samples that get a score close to 0.8, about 80% should actually belong to the positive class.
Accuracy and the area under the receiver operating characteristic curve (ROC-AUC) cannot tell you whether that holds. Both look at labels or rankings, not at whether 0.8 means 80%. A model can score well on both and still be wildly over- or under-confident.
Some models are more prone to this than others. The guide notes that logistic regression tends to be well calibrated by itself. Gaussian naive Bayes pushes probabilities toward 0 and 1, random forests tend to avoid the extremes, and maximum-margin methods like support vector machines (SVMs) produce a sigmoid-shaped distortion. You will see two of these behaviors yourself below.
Setup and Data
Install the libraries and check your version:
pip install -U scikit-learn matplotlib numpy
python -c "import sklearn; print(sklearn.__version__)"
You need scikit-learn 1.6 or later. That is the release that introduced FrozenEstimator, which replaced the old cv="prefit" option, per the 1.6 changelog. Many older tutorials still use cv="prefit", so keep that in mind if you borrow their code.
The data is the Covertype dataset: 581,012 patches of forest with 54 features each, collected for predicting the dominant tree species. It is multiclass, so you will turn it into a binary problem: Spruce/Fir (class 1) against everything else.
Create calibrate.py and start with this:
import numpy as np
import matplotlib.pyplot as plt
from sklearn.calibration import CalibratedClassifierCV, CalibrationDisplay
from sklearn.datasets import fetch_covtype
from sklearn.ensemble import RandomForestClassifier
from sklearn.frozen import FrozenEstimator
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
RANDOM_STATE = 42
# ---- Step 1: data -------------------------------------------------------
X, y = fetch_covtype(return_X_y=True)
y = (y == 1).astype(int)  # 1 = Spruce/Fir, everything else = 0
# Work with a 100,000-row sample so everything runs quickly
rng = np.random.default_rng(RANDOM_STATE)
subset = rng.choice(len(X), size=100_000, replace=False)
X, y = X[subset], y[subset]
print("Rows:", X.shape[0], "| Share of positives:", round(y.mean(), 3))
# Split 50% train, 20% calibration, 30% test
X_train, X_rest, y_train, y_rest = train_test_split(
    X, y, train_size=0.5, stratify=y, random_state=RANDOM_STATE
)
X_cal, X_test, y_cal, y_test = train_test_split(
    X_rest, y_rest, train_size=0.4, stratify=y_rest, random_state=RANDOM_STATE
)
print("Train / calibration / test:", len(X_train), len(X_cal), len(X_test))
fetch_covtype downloads the data on the first call and caches it in a scikit_learn_data folder in your home directory. The target holds the values 1 to 7, so y == 1 turns it into a 0/1 label. Sampling 100,000 rows keeps the random forest fast without changing the lesson.
The part that matters most is the three-way split. The user guide explains that a calibrator should be fit on data independent of what trained the classifier, because a model is more confident on its own training data. Fit the calibrator on the training data, and it learns probabilities that are too close to 0 and 1. So you get a training set, a calibration set, and a test set that nothing touches until the final check. stratify keeps the class share the same in every split.
Showing the Problem
Now train two models that are known to misbehave in opposite ways. Add this to the same file:
# ---- Step 2: train two models -------------------------------------------
models = {
    "Naive Bayes": GaussianNB(),
    "Random forest": RandomForestClassifier(
        n_estimators=200, n_jobs=-1, random_state=RANDOM_STATE
    ),
}
for model in models.values():
    model.fit(X_train, y_train)
# Predicted probability of the positive class on the untouched test set
raw = {name: m.predict_proba(X_test)[:, 1] for name, m in models.items()}
Both models fit on the training set only. predict_proba(X_test)[:, 1] keeps the probability of the positive class, which is all you need for a binary problem.
Next come three small helpers you will reuse for every comparison:
# ---- helpers ------------------------------------------------------------
def ninety_test(name, p, y_true, low=0.85, high=0.95):
    """How often are samples scored in [low, high) actually positive?"""
    mask = (p >= low) & (p < high)
    if mask.sum() == 0:
        print(f"{name}: no test samples scored in [{low}, {high})")
        return
    print(
        f"{name}: {mask.sum()} samples scored in [{low}, {high}) "
        f"-> {y_true[mask].mean():.1%} are actually positive"
    )
def print_scores(y_true, probas):
    print(f"{'Model':<32}{'Brier':>8}{'Log loss':>10}{'ROC-AUC':>9}")
    for name, p in probas.items():
        print(
            f"{name:<32}{brier_score_loss(y_true, p):>8.4f}"
            f"{log_loss(y_true, p):>10.4f}{roc_auc_score(y_true, p):>9.4f}"
        )
def reliability_plot(y_true, probas, title):
    fig, (ax_curve, ax_hist) = plt.subplots(
        2, 1, figsize=(7, 9), gridspec_kw={"height_ratios": [3, 1]}, sharex=True
    )
    for i, (name, p) in enumerate(probas.items()):
        CalibrationDisplay.from_predictions(
            y_true, p, n_bins=10, name=name, ax=ax_curve, ref_line=(i == 0)
        )
        ax_hist.hist(p, bins=10, range=(0, 1), histtype="step", label=name)
    ax_curve.set_title(title)
    ax_curve.set_xlabel("")
    ax_hist.set_xlabel("Mean predicted probability")
    ax_hist.set_ylabel("Count")
    ax_hist.legend(loc="upper center")
    plt.tight_layout()
    plt.show()
ninety_test is the "does 0.9 mean 90%?" check in plain code. It takes every test sample scored between 0.85 and 0.95 and reports how many were truly positive.
print_scores reports three numbers. The Brier score is the mean squared gap between probability and outcome, and lower is better. Log loss punishes confident mistakes harder. ROC-AUC measures ranking and will help you show that calibration leaves it intact.
reliability_plot draws a calibration curve, also called a reliability diagram. The samples are grouped into 10 bins by predicted probability. The x-axis is the average prediction in each bin and the y-axis is the share of real positives in it. A perfect model sits on the diagonal. The histogram underneath shows how many predictions land in each bin, so you know which curve points rest on plenty of data and which on very little. ref_line=(i == 0) draws the diagonal only once.
Now run the diagnosis:
# ---- Step 3: show the problem -------------------------------------------
for name, p in raw.items():
    ninety_test(name, p, y_test)
print()
print_scores(y_test, raw)
reliability_plot(y_test, raw, "Reliability diagram: uncalibrated models")
Run python calibrate.py. Your exact numbers will differ from mine, since they depend on the sample and scikit-learn version, but the shape should be consistent.
Read the diagram like this. A curve below the diagonal means the model is overconfident: it said 0.9 and reality was lower. A curve above the diagonal means it is underconfident. Naive Bayes should sit below the line at the high end, with a histogram crowded at 0 and 1. The random forest should draw an S-curve, under the line on the low end and above it on the high end, with fewer predictions at the extremes. That matches the explanation in the docs of how averaging many trees keeps predictions away from 0 and 1.
The ninety test makes it concrete. Compare the "actually positive" percentage for each model against the 90% it implied.
One caution about the Brier score. The user guide notes that it mixes calibration with discriminative power, so a lower Brier score does not always mean better calibration. That is why the diagram sits next to the numbers instead of being replaced by them.
Fix 1: Platt Scaling
Platt scaling fits a small logistic curve on top of the model's output. The user guide gives the formula, p = 1 / (1 + exp(A·f + B)), where f is the model's raw score and A and B are two numbers learned by maximum likelihood. It goes back to Platt's 1999 paper on SVM outputs, which the user guide cites.
Because it learns only two parameters, it is hard to overfit. The guide notes that it assumes the calibration curve can be corrected by a sigmoid function, so it suits distortions with that S shape. It is also monotonic, so it keeps the ranking of your predictions. And with a small calibration set, it is the safer choice, since the API reference warns against isotonic there.
In scikit-learn, this is method="sigmoid" on CalibratedClassifierCV:
calibrator = CalibratedClassifierCV(FrozenEstimator(models["Naive Bayes"]), method="sigmoid")
calibrator.fit(X_cal, y_cal)
p_platt = calibrator.predict_proba(X_test)[:, 1]
FrozenEstimator wraps a model that is already fitted so that calling fit on it does nothing. Without it, CalibratedClassifierCV would refit your model. As the API reference explains, all the data you pass to fit is then used for calibration, and keeping it separate from the training data is up to you. You did that with the calibration split.
Fix 2: Isotonic Regression
Isotonic regression does not assume a shape. It fits a step-wise function that never goes down as the score goes up. That makes it more flexible than Platt scaling: it can correct any monotonic distortion, not only S-curves.
The flexibility has a price. The guide warns that isotonic regression is more prone to overfitting, especially on small datasets, and that it tends to match or beat the sigmoid only when you have enough data, roughly more than 1,000 samples. The API reference is blunter, calling isotonic calibration not recommended when the calibration set is far below that. Your calibration set has 20,000 samples, so you are safe.
There is one more side effect. Isotonic regression produces ties in the predictions, so ROC-AUC can shift slightly after calibration. If you must keep the ranking exactly as it is, use the sigmoid.
The call is identical, with one word changed. Here is the full loop that calibrates both models with both methods:
# ---- Step 4 + 5: Platt scaling and isotonic regression ------------------
calibrated = {}
for name, model in models.items():
    for method in ("sigmoid", "isotonic"):
        calibrator = CalibratedClassifierCV(FrozenEstimator(model), method=method)
        calibrator.fit(X_cal, y_cal)
        calibrated[(name, method)] = calibrator.predict_proba(X_test)[:, 1]
Each calibrator learns its mapping from the 20,000 calibration samples only. The dictionary keeps the test-set probabilities for all four model and method combinations, ready to compare.
Comparing and Choosing
Add the comparison at the end of the script:
# ---- Step 6: compare ----------------------------------------------------
all_probas = {}
for name in models:
    group = {
        f"{name} (raw)": raw[name],
        f"{name} + Platt": calibrated[(name, "sigmoid")],
        f"{name} + isotonic": calibrated[(name, "isotonic")],
    }
    all_probas.update(group)
    reliability_plot(y_test, group, f"{name}: before and after calibration")
print()
print_scores(y_test, all_probas)
print()
for label, p in all_probas.items():
    ninety_test(label, p, y_test)
You get one before-and-after diagram per model, then a score table, then the ninety test for every variant.
What to look for:
- The curves: The calibrated lines should hug the diagonal much more closely than the raw ones.
- Brier score and log loss: Both should drop after calibration, with the biggest gain on the model that was furthest off.
- ROC-AUC: The Platt rows should match the raw rows exactly. The isotonic rows can differ in the last digits, because of the ties mentioned above.
- The ninety test: The "actually positive" share for the 0.85 to 0.95 bin should move toward the range the bin implies. If a variant has no samples in that bin, the helper says so, which can happen when a method compresses scores.
Which method should you use?
If you have no spare data for a calibration set, let scikit-learn cross-validate for you:
cv_calibrated = CalibratedClassifierCV(GaussianNB(), method="sigmoid", cv=5)
cv_calibrated.fit(X_train, y_train)
p_cv = cv_calibrated.predict_proba(X_test)[:, 1]
Here you pass an unfitted model. For each of the 5 folds, CalibratedClassifierCV trains a copy on part of the data and fits the calibrator on the rest. At prediction time it averages the five results, so the calibrator never sees the data its own classifier trained on.
Three habits will save you from the usual traps:
- Never fit the calibrator on training data
- Keep the test set untouched until the final check, so your before-and-after scores are honest
- Recalibrate when the model changes
Wrapping Up
You started with a model whose 0.9 did not mean 90%. You split real data three ways, trained a naive Bayes model and a random forest, and used a reliability diagram, a Brier score, and a simple ninety test to measure the problem. Then you fixed it with Platt scaling and isotonic regression through CalibratedClassifierCV and FrozenEstimator, confirmed the result, and picked a method based on how much calibration data you have.
Now try it on your own model. Replace the two classifiers in models with the one you ship, keep the three-way split, and run the diagrams. If you want to go further, scikit-learn's calibration comparison example lines up more models, and Venn-ABERS predictors give you probability intervals instead of single values.
 
Shittu Olumide is a software engineer and technical writer passionate about leveraging cutting-edge technologies to craft compelling narratives, with a keen eye for detail and a knack for simplifying complex concepts. You can also find Shittu on Twitter.
