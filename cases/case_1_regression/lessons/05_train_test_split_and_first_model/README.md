# Lesson 5 — Train/Test Split and First Regression Model

**Estimated time:** 35-45 min

## Learning outcomes

- You'll be able to explain why a train/test split has to happen before any statistic (like a median for imputation) is computed from the data.
- You'll be able to fit a baseline and a first `LinearRegression` model, and read the resulting MAE as "better/worse than always predicting the mean," not as an abstract number.
- You'll be able to name which of a candidate feature set's correlations with the target are strong enough to call "real signal" versus noise.

## Mentor's note

"This is the first model that has to actually earn its keep. Not against a guess on data it memorized — against Lesson 4's baseline, on shipments it's never seen. If you skip the split and score it on the same data it trained on, you're not measuring performance, you're measuring memorization."

## Lesson goal

Fit a real regression model with a proper held-out test set, and prove — with numbers, not intuition — that it beats a fair baseline.

## Today's analytical question

Does a linear regression on the four numeric features Lesson 3 examined actually predict shipment delay better than TransLine's best naive guess — even though only one of them correlated strongly on its own?

## What you're given

- The data from Lessons 2-4 (reproduced here via `load_shipments`)
- `task.py` — five functions to implement: `load_shipments`, `split_shipments`, `impute_driver_experience`, `fit_model`, `predict_delay`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Confirm the train/test split adds up: 394 + 99 = 493.
4. Call `impute_driver_experience` right after splitting — notice it computes the fill value from `train_df` only, then applies that same value to both `train_df` and `test_df`. This is the fix for a real bug this course used to have: computing the median before splitting would let a little test-set information leak into training.
5. Compare the model's MAE/RMSE on the test set against the *fair* baseline (train-mean applied to test, not Lesson 4's whole-dataset baseline).
6. Look at the model's coefficients — do their signs match what Lesson 3's correlations suggested?

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, state by how much (in minutes of MAE) the model beats the fair baseline, and list one thing you'd try next to improve it further.

## Reflection

The mentor asks: why does this lesson recompute the baseline's mean from the training set only, instead of reusing Lesson 4's mean (which was computed over the whole dataset)? What would go wrong if you used the whole-dataset mean as your "fair" baseline here?
