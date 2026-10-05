# Lesson 5 — Evaluation

**Estimated time:** 65-85 min

## Learning outcomes

- You'll be able to evaluate your Lesson 4 model on held-out test data, using the metric that actually matches your problem type.
- You'll be able to check a clustering solution's stability via resampling instead of a held-out split, and explain why that's the right substitute when there's no target to hold out.
- You'll be able to tell whether your model's test-set performance still beats the baseline, the way its training-set performance did.
- You'll be able to choose a classification threshold on a validation split — not on test_df, and not by default — and justify it against which mistake costs your client more.
- You'll be able to compare k values for a clustering problem using more than one metric, instead of trusting a single hardcoded default.

## Mentor's note

"Lesson 4 only told you how your model does on data it already saw. That's not evaluation, that's a rehearsal. This is where you find out if it actually learned anything."

## Lesson goal

Evaluate your Lesson 4 baseline and model on held-out test data — data the model never saw while fitting — using the metric that actually fits your problem type.

## Today's analytical question

Does your model's test-set performance still beat the baseline, the way its training-set performance did in Lesson 4?

## What you're given

- The same dataset you picked in Lesson 1
- `task.py` — the seven functions from Lesson 4, reproduced, plus six new ones: `evaluate_regression`, `evaluate_classification` (now takes an optional `threshold`), `evaluate_clustering`, `cluster_stability`, and — new this lesson — `split_for_validation` and `metrics_at_threshold` (classification only), `cluster_metrics_by_k` (clustering only). Use only the ones that match your dataset.
- `lesson.ipynb` — the notebook where you'll run your full pipeline and evaluate it

## Working in the notebook

- Run only the cell matching your dataset's problem type — it loads, splits, imputes, fits, and evaluates in one place (the clustering cell also scales features before fitting).
- Compare the test-set result to what you saw in Lesson 4.
- Decide whether the model is actually good enough to act on.

**A note on clustering evaluation:** unlike regression and classification, clustering here isn't scored on a held-out test set — `evaluate_clustering`'s silhouette score is computed on the same data the model was fit on, which is standard for cluster *quality* (matching Case 3's own approach). The clustering cell also runs `cluster_stability`, which checks something regression/classification's held-out test set already gives you for free: whether the result would hold up on a different sample. Re-fitting on repeated resamples and comparing cluster assignments via Adjusted Rand Index (ARI — 1.0 means identical, near 0 means essentially random) is what tells you whether your segments are real or an artifact of this particular dataset. This checks sensitivity to *which rows get sampled*, not to KMeans's random initialization — those are different questions, and `cluster_stability` only tests the first one (it always fits with the same `random_state`).

**A note on choosing a classification threshold:** `fit_classification_baseline_and_model` and `evaluate_classification`'s default `threshold=0.5` is a default, not a verdict. Before touching `test_df`, carve a `fit_df`/`val_df` split out of `train_df` with `split_for_validation`, fit on `fit_df`, and compare a few candidate thresholds with `metrics_at_threshold` on `val_df`. For the suggested LendWell feature set, thresholds between 0.2 and 0.6 trade precision for recall — a lower threshold catches more of the loans that actually default, at the cost of flagging more loans that wouldn't have. Which trade-off is right depends on which mistake costs your client more: approving a loan that defaults, or rejecting an applicant who would have paid it back. Pick a threshold on `val_df`, then — and only then — call `evaluate_classification(..., threshold=your_choice)` on `test_df` for your real number.

**A note on choosing k for clustering:** the suggested `k=3` in `fit_clustering_model` is a starting point, not the answer. `cluster_metrics_by_k` reports inertia and silhouette across a range of k values — look at both, plus the `cluster_stability` check above, before deciding. These metrics won't agree with each other automatically (a lower silhouette at one k doesn't make a higher-silhouette k "the" correct number of segments) — the right k also depends on whether the resulting groups are a size and shape your client could act on.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. These checks verify the evaluation numbers for the suggested feature sets — they can't tell you whether your model is good enough for your actual Lesson 1 question.

## Homework

Two to three sentences: would you actually recommend this model to your Lesson 1 client as-is, or does it need more work first? Be specific about what the evaluation number tells you. If you're on the classification path, state the threshold you chose and why; if you're on the clustering path, state the k you chose and why.

## Reflection

The mentor asks: for classification and regression, you now have both a training-set result (Lesson 4) and a test-set result (this lesson). If those two numbers told very different stories, what would that tell you about your model — and which number would you trust more, and why?
