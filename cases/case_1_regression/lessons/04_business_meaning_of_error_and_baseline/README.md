# Lesson 4 — Business Meaning of Error and Baseline Model

## Mentor's note

"Before you build anything clever, answer this: what's the dumbest possible guess, and how wrong is it? If you skip this, you'll have no way to tell whether next lesson's model is actually good — 'better than nothing' isn't the same as 'good enough to ship.'"

## Lesson goal

Establish a baseline TransLine can already act on today, and measure exactly how wrong it is — in minutes, not abstract error scores.

## Today's analytical question

If TransLine had no model at all and just guessed the same number every time, what should that number be, and how far off would it typically land?

## What you're given

- The cleaned data from Lessons 2-3 (reproduced here via `load_clean_shipments`)
- `task.py` — five functions to implement: `load_clean_shipments`, `predict_mean_baseline`, `predict_zero_baseline`, `mean_absolute_error`, `root_mean_squared_error`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Compare the two baselines' MAE — which naive guess is actually less wrong on average?
4. Compare MAE and RMSE for the same baseline — why are they different numbers for the same predictions?

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write the one-sentence answer to the ops manager's question, plus a note on what MAE number any future model of yours needs to beat to be worth deploying.

## Reflection

The mentor asks: RMSE for the mean-baseline turns out to equal the standard deviation of `delay_minutes`. Why would that be true, and what does it tell you about what RMSE actually measures?
