# Lesson 3 — Exploratory Data Analysis

## Mentor's note

"Data's clean now — good. Don't reach for a model yet. Look first. Half of what you'll 'discover' by modeling too early, you can already see in a correlation matrix and a bar chart, and it's a lot cheaper to look than to fit."

## Lesson goal

Find out which columns actually move with `delay_minutes`, using correlation and group comparisons — and notice where correlation alone is misleading.

## Today's analytical question

Of everything TransLine recorded, what actually predicts a shipment's delay, and what only looks like it should?

## What you're given

- The cleaned data from Lesson 2 (reproduced here via `load_clean_shipments`)
- `task.py` — four functions to implement: `load_clean_shipments`, `correlation_matrix`, `correlation_with_target`, `mean_delay_by_weather`
- `lesson.ipynb` — the notebook where you'll do the actual work, including your first plots

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Look at the histograms — anything skewed or surprising?
4. Look at the correlation matrix — which numeric column has the strongest relationship with `delay_minutes`?
5. Compare `num_stops` and `actual_duration_min`'s correlation with the target — one is a real signal, the other is deceptive. Figure out why.
6. Look at the weather bar chart — notice it never appeared in the correlation matrix at all.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, list the columns you'd bring into modeling next lesson, and the ones you'd leave out — with one sentence each on why.

## Reflection

The mentor asks: `actual_duration_min` is *defined* as `planned_duration_min + delay_minutes`, yet its correlation with `delay_minutes` is nearly zero. If a column can be mathematically related to your target and still show a weak correlation, what does that tell you about trusting a correlation matrix on its own?
