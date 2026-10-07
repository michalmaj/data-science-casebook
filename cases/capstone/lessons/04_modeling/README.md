# Lesson 4 — Modeling

**Estimated time:** 55-65 min

## The decision to make

This is where the path actually splits. Regression, classification, clustering — whichever the chosen dataset calls for, fit a baseline first. If it can't be beaten, there's no model yet — there's a coincidence.

The split below uses the same recipe as Lesson 2 (and Lesson 3, for the two predictive paths) — this lesson doesn't introduce a new split, it reuses the one the data-quality and exploration steps already relied on.

## What you have to work with

- `task.py` — seven functions: `load_dataset` (no cleaning, replaces the old `load_clean_dataset`), `split_dataset`, `impute_missing`, `scale_features` (standardizes features — decide for yourself whether the chosen technique needs this, and justify it in your notes; also returns the fitted scaler), and one fit function per technique: `fit_regression_baseline_and_model`, `fit_classification_baseline_and_model`, `fit_clustering_model` (use only the one matching the chosen dataset).
- In the notebook: set `DATASET_NAME`, run the cell that loads, splits, imputes, and (for clustering) scales, then fits a model. Compare it to the baseline.

## Justify it

From this lesson's folder, run:

```bash
uv run pytest
```

Starting this lesson, these checks verify both structure/reasonableness and exact values for the suggested feature sets — they confirm the generic functions behave correctly, not that a particular feature choice is the best one. There's no single correct model once features are chosen independently, and these checks don't grade that choice.

Two to three sentences: using the chosen feature set (suggested or independent), how much better is the model than the baseline, and is that difference big enough to matter for the Lesson 1 question? On the clustering path, add one sentence justifying the decision to scale features before fitting (or not). And: a model that fits the training data well isn't automatically a model that will work on new data. What would raise suspicion that this model is just memorizing its training set rather than learning something real?
