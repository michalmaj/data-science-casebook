# Lesson 3 — Train/Test Split and the Sealed Envelope

**Estimated time:** 30-40 min

## Why we're doing this

Before you explore anything else about this data, the test set goes into a sealed envelope. Not metaphorically — actually stop looking at those rows. Every decision from here on — what correlates with what, what counts as signal, what a baseline guess should be — gets made on the training rows only. You open the envelope exactly once, at the end, to find out if any of it worked.

Today's question: once we set aside data to test on honestly, what's actually left to explore and build with — and what happens if we get that boundary wrong?

## What you need to do

- The data from Lesson 2 (reproduced here via `load_shipments`).
- In `task.py`, implement `load_shipments`, `split_shipments`, `impute_driver_experience`.
- In the notebook: confirm the split adds up (394 + 99 = 493). Call `impute_driver_experience` right after splitting and notice it computes the fill value from the training set only, then applies that same value to both the training and test sets. Every later lesson in this case reuses exactly this split and this imputation — same `RANDOM_STATE`, same rows.

## What to watch for

`test_df` in this lesson never gets touched beyond counting its missing values and filling them with a number derived from training. That distinction is what makes it safe: filling test's own gaps with a train-only statistic is fine, because the test set doesn't influence that statistic — it only receives it. Computing the same statistic from the test set itself would not be safe.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, compare the whole-dataset median to the train-only median, and write down why a 1-year difference in an imputed value matters for honest evaluation.
