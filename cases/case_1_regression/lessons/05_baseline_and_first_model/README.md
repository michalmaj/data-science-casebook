# Lesson 5 — Baseline and First Model

**Estimated time:** 45-55 min

## Learning outcomes

- You'll be able to build a naive baseline, score it in-sample first to build MAE/RMSE intuition, then score it (and a real model) fairly on held-out test data.
- You'll be able to compute MAE and RMSE by hand and explain what each one penalizes differently.
- You'll be able to fit a first `LinearRegression` and show, with numbers, that it beats both a naive guess and translates into something TransLine can act on, in minutes.

## Mentor's note

"Before you build anything clever, answer this: what's the dumbest possible guess, and how wrong is it? Then — and only then — build the real thing, and prove it clears that bar on shipments it's never seen. Not against a guess on data it memorized. If you skip the split and score it on the same data it trained on, you're not measuring performance, you're measuring memorization."

## Lesson goal

Establish a fair baseline from training data, then fit a first regression model and prove — with numbers, not intuition — that it beats that baseline on held-out data.

## Today's analytical question

If TransLine had no model and just guessed the same number every time, how wrong would that be — and does a real linear regression on the four features Lesson 4 examined actually do better, on shipments it has never seen?

## What you're given

- The split and imputed data from Lesson 3 (reproduced here via `load_shipments`, `split_shipments`, `impute_driver_experience`)
- `task.py` — nine functions to implement: `load_shipments`, `split_shipments`, `impute_driver_experience`, `predict_zero_baseline`, `predict_mean_baseline`, `mean_absolute_error`, `root_mean_squared_error`, `fit_model`, `predict_delay`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Compare the two baselines' in-sample MAE on train — which naive guess is actually less wrong?
4. Notice `predict_mean_baseline` takes two arguments: call it with `(train_df, train_df)` for the in-sample check, and `(train_df, test_df)` for the fair comparison later — the mean itself always comes from `train_df`.
5. Confirm the model beats the fair mean-baseline, which beats the zero-baseline, on the held-out test set.
6. Look at the model's coefficients — do their signs match what Lesson 4's correlations suggested?

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, state by how much (in minutes of MAE) the model beats the fair baseline, and list one thing you'd try next to improve it further.

## Reflection

The mentor asks: this lesson computes the mean-baseline's value from `train_df` in both calls to `predict_mean_baseline` — even the one scored against `test_df`. Why is that still fair, when computing `correlation_with_target` on `test_df` would not be?
