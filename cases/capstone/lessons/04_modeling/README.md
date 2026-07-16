# Lesson 4 — Modeling

**Estimated time:** 55-65 min

## Learning outcomes

- You'll be able to apply the same generic split/impute/(scale) sequence regardless of whether your problem turns out to be regression, classification, or clustering.
- You'll be able to fit a baseline and a first real model matching whichever technique your own chosen dataset actually calls for.
- You'll be able to state what "one generic pipeline across three techniques" buys you, and where it stops being enough for your specific problem.

## Mentor's note

"This is where the path actually splits. Regression, classification, clustering — whichever your dataset calls for, fit a baseline first. If you can't beat a baseline, you don't have a model yet, you have a coincidence."

## Lesson goal

Split your data, fit a baseline, and fit a first real model — using whichever technique your chosen dataset actually calls for.

## Today's analytical question

Does your first model actually do better than the simplest possible baseline for your problem?

## What you're given

- The same dataset you picked in Lesson 1
- `task.py` — seven functions: `load_dataset` (no cleaning, replaces the old `load_clean_dataset`), `split_dataset` (works for any dataset — takes an optional `stratify_column` to keep class balance across train/test for classification), `impute_missing` (fills missing values using training-set statistics only, in the feature columns you specify, applied to both train and test), `scale_features` (standardizes features to zero mean/unit variance, needed before clustering — also returns the fitted scaler), and one fit function per technique: `fit_regression_baseline_and_model`, `fit_classification_baseline_and_model`, `fit_clustering_model` (use only the one that matches your dataset)
- `lesson.ipynb` — the notebook where you'll fit your baseline and model

## Working in the notebook

- Set `DATASET_NAME` to match what you picked in Lesson 1 — the preview cell shows your train/test split sizes.
- Run the cell below it — it loads, splits, imputes (using training-set statistics only), and, for clustering, scales your dataset, then fits your model, all in one place.
- Compare your model to the baseline.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. Starting this lesson, these checks verify both structure/reasonableness (shapes, convergence, "the model beats the baseline on training data") and exact values for the suggested feature sets (e.g. the baseline itself, the number of model coefficients) — they confirm your generic functions behave correctly, not that your particular feature choices are the best ones. There's no single correct model once you're choosing your own features, and these checks don't grade that choice.

## Homework

Two to three sentences: using the specific feature set you chose (whether the suggested one or your own), how much better is your model than the baseline, and is that difference big enough to matter for your Lesson 1 question?

## Reflection

The mentor asks: a model that fits the training data well isn't automatically a model that will work on new data. What would make you suspicious that this model is just memorizing its training set rather than learning something real?
