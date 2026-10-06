# Lesson 7 — Correlation vs. Prediction vs. Causation

**Estimated time:** 35-45 min

## Why we're doing this

You already know what's correlated with delay and what improves prediction. Neither one tells you what to *change* to fix the delay. Those are three different questions, and TransLine is about to ask you the third one — because that's the one they can actually act on.

Today's question: which of the model's coefficients can you trust enough to build a recommendation on, and which are you not entitled to interpret at all?

## What you need to do

- The same split data as Lesson 3, and the same model-fitting approach as Lesson 5 (reproduced here via `load_shipments`, `split_shipments`, `impute_driver_experience`).
- In `task.py`, implement two new functions: `fit_model_on` (fit on any feature list, not just the fixed set) and `coefficient_for` (look up one feature's coefficient).
- In the notebook: compare `num_stops`'s coefficient fit alone vs. fit alongside the other features — note how little it moves. Compare `distance_km`'s coefficient fit alone vs. fit alongside `planned_duration_min` — note how much it moves, and check their correlation to see why.

## What to watch for

A concrete way to tell whether a coefficient's story is trustworthy: check whether it survives adding other correlated variables to the model. A coefficient that doesn't move deserves more trust than one that jumps around depending on what else is in the model — but a stable coefficient still isn't proof of causation, only a reason to keep investigating it.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, pick one factor and separate out what you know for sure (correlated? predictive?) from what you're only guessing at (causal? actionable?). And: `num_stops`'s coefficient was stable across feature sets, which is a good sign — what's a concrete way `num_stops` could be a proxy for something else, rather than a direct cause of delay?
