# Lesson 4 — Exploratory Data Analysis

**Estimated time:** 30-40 min

## Why we're doing this

The data is split now — good. Don't reach for a model yet. Look first, training rows only. Half of what you'd "discover" by modeling too early is already visible in a correlation matrix and a bar chart, and looking is a lot cheaper than fitting a model.

Today's question: of what TransLine recorded, what actually predicts a shipment's delay, and what only looks like it should — judged on the rows we're allowed to look at?

## What you need to do

- The split data from Lesson 3 (reproduced here via `load_shipments`, `split_shipments`, `impute_driver_experience`).
- In `task.py`, implement six functions: `load_shipments`, `split_shipments`, `impute_driver_experience`, `correlation_matrix`, `correlation_with_target`, `mean_delay_by_weather`.
- In the notebook: look at the histograms, the correlation matrix (which numeric column has the strongest relationship with `delay_minutes`?), and compare `num_stops`'s and `actual_duration_min`'s correlation with the target — one is a real signal, the other is misleading. Work out why.

## What to watch for

The weather bar chart never shows up in the correlation matrix, because `weather` is categorical — but it's also the one column TransLine's ops manager already flagged in Lesson 1 as unknowable before a shipment leaves the depot. Keep both of those in mind for the prompt below.

`test_df` gets created by `split_shipments`, but nothing further in this notebook uses it — that's deliberate, not an oversight.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, list which columns you'll carry into modeling next lesson and which you'll drop — one sentence of justification each. And: `actual_duration_min` is *defined* as `planned_duration_min + delay_minutes`, yet its correlation with `delay_minutes` is close to zero. If a column can be mathematically tied to the target and still show weak correlation, what does that say about trusting the correlation matrix on its own?
