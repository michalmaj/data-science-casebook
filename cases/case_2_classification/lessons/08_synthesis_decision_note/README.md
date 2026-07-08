# Lesson 8 — Synthesis: Decision Note

## Mentor's note

"Seven lessons of code, and Meridian Outlet's ops manager will never read a line of it. What they'll read is what you write today. Everything you found — the baseline, the model, the threshold trade-off, how confident to be in the risk tiers — only matters if you can say it plainly enough that someone who's never seen a p-value can act on it."

## Lesson goal

Assemble everything from Lessons 1-7 into a decision note Meridian Outlet could actually receive and act on.

## Today's analytical question

Given everything you now know, what should Meridian Outlet actually do — and how confident should they be?

## What you're given

- The same cleaned, split data and model as Lessons 5-7 (reproduced here via `load_and_merge_orders`, `split_orders`, `fit_classifier`)
- `task.py` — one new function, `final_scorecard`, that lays out every predictor this case has built (majority baseline, default-threshold model, chosen-threshold model) side by side on the same held-out data
- `lesson.ipynb` — this time, most of the notebook is the decision note template itself, not code

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the code cell to generate the scorecard.
3. Fill in each of the seven decision-note sections below it, in plain language, using what you learned across Lessons 1-7.
4. There is no separate homework this lesson — the completed decision note is the deliverable for all of Case 2.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. This checks the scorecard numbers — it cannot check your decision note's writing, which is graded on communication and interpretation (see the rubric in `do_poczytania.txt`).

## Homework

None separately — but if you want an extra exercise, try compressing your entire decision note into a 3-sentence executive summary, as if the ops manager only has thirty seconds.

## Reflection

The mentor asks: if you had to cut one section of your decision note to fit on a single slide, which one would you keep, and which would you cut — and what does that choice tell you about what actually matters to Meridian Outlet?
