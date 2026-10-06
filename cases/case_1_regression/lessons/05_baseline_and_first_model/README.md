# Lesson 5 — Baseline and First Model

**Estimated time:** 45-55 min

## Why we're doing this

Before you build anything clever, answer this: what's the dumbest possible guess, and how wrong is it? Then — and only then — build the real thing, and prove it clears that bar on shipments it's never seen. Not against a guess on data it memorized: if you score a model on the same data it trained on, you're not measuring performance, you're measuring memorization.

Today's question: if TransLine had no model and just guessed the same number every time, how wrong would that be — and does a real linear regression on the four features Lesson 4 examined actually do better, on shipments it has never seen?

## What you need to do

- The split and imputed data from Lesson 3 (reproduced here via `load_shipments`, `split_shipments`, `impute_driver_experience`).
- In `task.py`, implement nine functions: `load_shipments`, `split_shipments`, `impute_driver_experience`, `predict_zero_baseline`, `predict_mean_baseline`, `mean_absolute_error`, `root_mean_squared_error`, `fit_model`, `predict_delay`.
- In the notebook: compare the two baselines' in-sample MAE on the training set — which naive guess is actually less wrong? `predict_mean_baseline` takes two arguments: call it with `(train_df, train_df)` for the in-sample check, and `(train_df, test_df)` for the fair comparison later — the mean itself always comes from `train_df`. Confirm the model beats the fair mean-baseline, which beats the zero-baseline, on the test set. Look at the model's coefficients — do their signs match what Lesson 4's correlations suggested?

## What to watch for

This lesson computes the mean-baseline's value from `train_df` in both calls to `predict_mean_baseline` — even the one scored against `test_df`. That's still fair, because the mean is only *applied* to the test set, not computed from it — the same logic as Lesson 3's imputation. Computing `correlation_with_target` on `test_df` would not be fair, because there the test set itself would be the source of the statistic, not just its recipient.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, state by how much (in minutes of MAE) the model beats the fair baseline, and note what it would take to bring `weather` — which had a real effect in Lesson 4 but isn't in `FEATURE_COLUMNS` — into the model. This is a reflection question, not a next step to actually carry out: once you've seen a model's test-set score, honestly adding a feature means re-splitting on fresh data, not quietly refitting and rescoring on the same `test_df`.
