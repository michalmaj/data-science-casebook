# Lesson 5 — Evaluation

**Estimated time:** 65-85 min

## The decision to make

Lesson 4 only showed how the model does on data it already saw. That's not evaluation, that's a rehearsal. Now it's time to find out if the model actually learned anything — and decide whether the result is good enough to act on.

## What you have to work with

- `task.py` — the seven functions from Lesson 4, reproduced, plus six new ones: `evaluate_regression`, `evaluate_classification` (now takes an optional `threshold`), `evaluate_clustering`, `cluster_stability`, and — new this lesson — `split_for_validation` and `metrics_at_threshold` (classification only), `cluster_metrics_by_k` (clustering only).
- In the notebook: run the cell matching the dataset's problem type — it loads, splits, imputes, fits, and evaluates in one place. Compare the test-set result to Lesson 4, and decide whether the model is actually good enough to act on.

## Before deciding

**On clustering evaluation:** unlike regression and classification, clustering here isn't scored on a held-out test set — `evaluate_clustering`'s silhouette score is computed on the same data the model was fit on, which is standard for cluster *quality* (matching Case 3's own approach). The clustering cell also runs `cluster_stability`, which checks something regression/classification's held-out test set already gives for free: whether the result would hold up on a different sample. Re-fitting on repeated resamples and comparing cluster assignments via Adjusted Rand Index (ARI — 1.0 means identical, near 0 means essentially random) is what tells you whether the segments are real or an artifact of this particular dataset. This checks sensitivity to *which rows get sampled*, not to KMeans's random initialization — those are different questions, and `cluster_stability` only tests the first one.

**On choosing a decision threshold:** `fit_classification_baseline_and_model` and `evaluate_classification`'s default `threshold=0.5` is a default, not a verdict. Before touching `test_df`, carve a `fit_df`/`val_df` split out of `train_df` with `split_for_validation`, fit on `fit_df`, and compare a few candidate thresholds with `metrics_at_threshold` on `val_df`. For the suggested LendWell feature set, thresholds between 0.2 and 0.6 trade precision for recall — a lower threshold catches more of the loans that actually default, at the cost of flagging more loans that wouldn't have. Which trade-off is right depends on which mistake costs the client more: approving a loan that defaults, or rejecting an applicant who would have paid it back. Pick a threshold on `val_df`, then — and only then — call `evaluate_classification(..., threshold=your_choice)` on `test_df` for the real number.

**On choosing k for clustering:** the suggested `k=3` in `fit_clustering_model` is a starting point, not the answer. `cluster_metrics_by_k` reports inertia and silhouette across a range of k values — look at both, plus the `cluster_stability` check above, before deciding. These metrics won't agree with each other automatically (a lower silhouette at one k doesn't make a higher-silhouette k "the" correct number of segments) — the right k also depends on whether the resulting groups are a size and shape the client could act on.

## Justify it

From this lesson's folder, run:

```bash
uv run pytest
```

These checks verify the evaluation numbers for the suggested feature sets — they can't tell you whether the model is good enough for the actual Lesson 1 question.

Two to three sentences: is this model worth recommending to the Lesson 1 client as-is, or does it need more work first? Be specific about what the evaluation number says. On the classification path, state the chosen threshold and why; on the clustering path, state the chosen k and why. And: for classification and regression, there are now two results — a training-set one (Lesson 4) and a test-set one (this lesson). If those two numbers told very different stories, what would that say about the model — and which number would be worth trusting more, and why?
