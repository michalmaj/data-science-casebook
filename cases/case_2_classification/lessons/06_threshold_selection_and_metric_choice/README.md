# Lesson 6 — Threshold Selection and Metric Choice

## Mentor's note

"You saw the model assign real probabilities, but the default threshold hid all of it. Now you get to choose the threshold yourself — and see exactly what you trade away every time you lower it."

## Lesson goal

Sweep the decision threshold down from 0.5, and see how precision, recall, and F1 trade off as you do — connecting each choice to a real business cost.

## Today's analytical question

How much precision is Meridian Outlet willing to give up to catch more actual returns — and where's a reasonable place to draw that line?

## What you're given

- The same `data/orders.xlsx` from Lessons 1-5
- `task.py` — six functions to implement: `load_and_merge_orders`, `split_orders`, `split_for_validation`, `fit_classifier`, `predict_at_threshold`, `classification_metrics`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Confirm `split_orders`/`fit_classifier` reproduce the exact same model as Lesson 5.
4. Call `split_for_validation` on `train_df` to carve out `fit_df`/`val_df` — you'll compare thresholds on `val_df`, not on `test_df`.
5. Call `predict_at_threshold` at 0.5, 0.3, and 0.2 on `val_df` — watch the number of flagged orders grow.
6. Call `classification_metrics` at each threshold on `val_df` — watch recall rise, and precision move too.
7. Connect the two kinds of mistakes to what they actually mean: a false positive wrongly flags a good order, a false negative lets a real return slip through unflagged.
8. In the last cell, retrain on the full `train_df` and check your chosen threshold on `test_df` — the one time this lesson touches it.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: pick a threshold you'd actually recommend to Meridian Outlet, and justify it in terms of the cost of a false positive versus a false negative.

## Reflection

The mentor asks: your validation-set numbers predicted what threshold 0.2 would do. When you finally looked at `test_df` in the last cell, did the real numbers land close to what validation predicted, or did they move quite a bit? What would a big gap between the two have told you — and why is it safer to find that out *after* you've already committed to a threshold, rather than while you're still choosing one?
