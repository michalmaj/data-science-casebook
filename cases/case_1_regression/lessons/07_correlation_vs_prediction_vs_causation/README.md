# Lesson 7 — Correlation vs. Prediction vs. Causation

## Mentor's note

"You've found what's correlated with delay, and you've found what improves prediction. Neither one tells you what to *change* to fix the delay. Those are three different questions, and TransLine is about to ask you the third one — because that's the one they can actually act on."

## Lesson goal

Learn a concrete way to tell whether a coefficient's story is trustworthy — by checking whether it survives adding other correlated variables to the model.

## Today's analytical question

Which of the model's coefficients can you trust enough to build a recommendation on, and which are you not entitled to interpret at all?

## What you're given

- The same split data as Lessons 5-6 (reproduced here via `load_shipments`, `split_shipments`, `impute_driver_experience`)
- `task.py` — two new functions: `fit_model_on` (fit on any feature list, not just the fixed set) and `coefficient_for` (look up one feature's coefficient)
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Compare `num_stops`'s coefficient fit alone vs. fit alongside the other features — note how little it moves.
4. Compare `distance_km`'s coefficient fit alone vs. fit alongside `planned_duration_min` — note how much it moves, and why (check their correlation).
5. Read the discussion cells and think through which factors TransLine could plausibly act on.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, pick one factor and separate out what you actually know (correlated? predictive?) from what you're only guessing at (causal? actionable?).

## Reflection

The mentor asks: `num_stops`'s coefficient was stable across feature sets, which is a good sign — but stability alone still isn't proof of causation. What's a concrete way you could imagine `num_stops` being a proxy for something else, rather than a direct cause of delay?
