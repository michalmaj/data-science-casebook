# Lesson 3 — Train/Test Split and the Sealed Envelope

**Estimated time:** 30-40 min

## Learning outcomes

- You'll be able to explain why a test set has to be carved out before any exploration, feature selection, or statistic (like a median for imputation) touches the data.
- You'll be able to split a dataset reproducibly with `train_test_split` and keep the split stable across runs.
- You'll be able to compute an imputation statistic from training data only and apply it, unchanged, to the test set.

## Mentor's note

"Before you explore anything else about this data, put the test set in a sealed envelope. Not metaphorically — actually stop looking at those rows. Every decision from here on — what correlates with what, what counts as signal, what a 'baseline' guess should be — gets made on the training rows only. You open the envelope exactly once, at the end, to find out if any of it worked."

## Lesson goal

Split the cleaned shipment data into train and test sets, and perform the one remaining cleaning step — imputing `driver_experience_years` — correctly, using training data only.

## Today's analytical question

Once we set aside data to test on honestly, what's actually left to explore and build with — and what happens if we get that boundary wrong?

## What you're given

- The data from Lesson 2 (reproduced here via `load_shipments`)
- `task.py` — three functions to implement: `load_shipments`, `split_shipments`, `impute_driver_experience`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Confirm the split adds up: 394 + 99 = 493.
4. Call `impute_driver_experience` right after splitting — notice it computes the fill value from `train_df` only, then applies that same value to both `train_df` and `test_df`.
5. Every later lesson in this case (4 onward) reuses exactly this split and this imputation — same `RANDOM_STATE`, same train/test rows.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, answer the prompt about the whole-dataset median versus the train-only median, and why a 1-year difference in an imputed value matters for honest evaluation.

## Reflection

The mentor asks: `test_df` never gets touched in this lesson beyond counting its missing values and filling them with a *train-derived* number. Why is filling test's own missing values with a train-only statistic still safe, when computing that statistic from test data itself would not be?
