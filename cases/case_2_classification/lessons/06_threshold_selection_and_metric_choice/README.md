# Lesson 6 — Threshold Selection and Metric Choice

## Mentor's note

"You saw the model assign real probabilities, but the default threshold hid all of it. Now you get to choose the threshold yourself — and see exactly what you trade away every time you lower it."

## Lesson goal

Sweep the decision threshold down from 0.5, and see how precision, recall, and F1 trade off as you do — connecting each choice to a real business cost.

## Today's analytical question

How much precision is Meridian Outlet willing to give up to catch more actual returns — and where's a reasonable place to draw that line?

## What you're given

- The same `data/orders.xlsx` from Lessons 1-5
- `task.py` — five functions to implement: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `predict_at_threshold`, `classification_metrics`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Confirm `split_orders`/`fit_classifier` reproduce the exact same model as Lesson 5.
4. Call `predict_at_threshold` at 0.5, 0.3, and 0.2 — watch the number of flagged orders grow.
5. Call `classification_metrics` at each threshold — watch recall rise, and precision move too.
6. Connect the two kinds of mistakes to what they actually mean: a false positive wrongly flags a good order, a false negative lets a real return slip through unflagged.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: pick a threshold you'd actually recommend to Meridian Outlet, and justify it in terms of the cost of a false positive versus a false negative.

## Reflection

The mentor asks: at threshold 0.2, the model still misses 9 of 20 actual returns and wrongly flags 34 good orders for every 11 it gets right. Is precision or recall the more important number for Meridian Outlet to optimize — and does that answer depend on what happens *after* a flag (a human reviews it, versus the order gets blocked automatically)?
