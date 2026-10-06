# Lesson 6 — Threshold Selection and Metric Choice

**Estimated time:** 40-50 min

## Why we're doing this

We saw the model assign real probabilities, but the default threshold hid all of it. Now we choose the threshold ourselves — and see exactly what we trade away every time we lower it.

We sweep the decision threshold down from 0.5, and see how precision, recall, and F1 trade off as we do — connecting each choice to a real business cost.

Every split in this lesson (`train_df`/`test_df`, then `fit_df`/`val_df`) is the row-level split from Lesson 5, by design: this lesson is tuning for scenario A (how well the model scores future orders from customers Meridian Outlet already knows), not scenario B (brand-new customers) — see Lesson 5 for what that distinction means, if it isn't already clear.

Today's question: how much precision is Meridian Outlet willing to give up to catch more actual returns — and where's a reasonable place to draw that line?

## What you need to do

- The same `data/orders.xlsx` from Lessons 1-5.
- In `task.py`, implement six functions: `load_and_merge_orders`, `split_orders`, `split_for_validation`, `fit_classifier`, `predict_at_threshold`, `classification_metrics`.
- In the notebook:
  1. Confirm `split_orders`/`fit_classifier` reproduce the exact same model as Lesson 5.
  2. Call `split_for_validation` on `train_df` to carve out `fit_df`/`val_df` — you'll compare thresholds on `val_df`, not on `test_df`.
  3. Call `predict_at_threshold` at 0.5, 0.3, and 0.2 on `val_df` — watch the number of flagged orders grow.
  4. Call `classification_metrics` at each threshold on `val_df` — watch recall rise, and precision move too.
  5. Connect the two kinds of mistakes to what they actually mean: a false positive wrongly flags a good order, a false negative lets a real return slip through unflagged.
  6. In the last cell, retrain on the full `train_df` and check your chosen threshold on `test_df` — the one time this lesson touches it, and, in fact, the first time anywhere in this case that `test_df` is used to evaluate a model (Lesson 5 did look at `test_df` once, but only to count customer overlap with `train_df` — a fact about the split's structure, not a performance number). By this point the features, the model, and the threshold are all already fixed — nothing about `test_df`'s numbers is allowed to change any of them now.

## What to watch for

This is the first point anywhere in this case where `test_df` actually scores the model — not counting customer overlap, not checking structure, but measuring performance. It happens right at the end, once the features, model, and threshold are already locked.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, pick a threshold worth recommending to Meridian Outlet, and justify it in terms of the cost of a false positive versus a false negative. And: the validation-set numbers predicted what threshold 0.2 would do — the last cell produces the real number on `test_df`. Does it land close to what validation predicted, or does it move quite a bit? What would a big gap between the two tell you — and why is it safer to find that out *after* a threshold is chosen, rather than while still choosing one?
