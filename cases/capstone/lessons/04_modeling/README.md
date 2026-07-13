# Lesson 4 — Modeling

## Mentor's note

"This is where the path actually splits. Regression, classification, clustering — whichever your dataset calls for, fit a baseline first. If you can't beat a baseline, you don't have a model yet, you have a coincidence."

## Lesson goal

Split your data, fit a baseline, and fit a first real model — using whichever technique your chosen dataset actually calls for.

## Today's analytical question

Does your first model actually do better than the simplest possible baseline for your problem?

## What you're given

- The same dataset you picked in Lesson 1
- `task.py` — seven functions: `load_dataset` (new — no cleaning, replaces the old `load_clean_dataset`), `split_dataset` (works for any dataset), `impute_missing` (new — fills missing values using training-set statistics only, applied to both train and test), `scale_features` (new — standardizes features to zero mean/unit variance, needed before clustering), and one fit function per technique: `fit_regression_baseline_and_model`, `fit_classification_baseline_and_model`, `fit_clustering_model` (use only the one that matches your dataset)
- `lesson.ipynb` — the notebook where you'll fit your baseline and model

## Working in the notebook

- Load, split, and impute your dataset — `impute_missing` fills gaps using training-set statistics only.
- Run only the fit-function cell that matches your dataset's problem type. The clustering cell also scales its features first — KMeans needs comparable feature magnitudes to measure genuine similarity.
- Compare your model to the baseline.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. Starting this lesson, these checks verify structure and reasonableness (shapes, convergence, "the model beats the baseline on training data") rather than exact prediction values — there's no single correct model once you're choosing your own features.

## Homework

Two to three sentences: using the specific feature set you chose (whether the suggested one or your own), how much better is your model than the baseline, and is that difference big enough to matter for your Lesson 1 question?

## Reflection

The mentor asks: a model that fits the training data well isn't automatically a model that will work on new data. What would make you suspicious that this model is just memorizing its training set rather than learning something real?
