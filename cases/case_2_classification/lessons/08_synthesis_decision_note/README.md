# Lesson 8 — Synthesis: Decision Note

**Estimated time:** 40-50 min

## Why we're doing this

Seven lessons of code, and Meridian Outlet's ops manager will never read a line of it. What they'll read is what you write today. The baseline, the model, the threshold trade-off, how confident to be in the risk tiers — all of it only matters if you can say it plainly enough that someone who's never seen a p-value can act on it.

Today's question: given everything you now know, what should Meridian Outlet actually do — and how confident should they be?

## What you need to do

- The same cleaned, split data and model as Lessons 5-7 (reproduced here via `load_and_merge_orders`, `split_orders`, `fit_classifier`).
- In `task.py`, implement one new function, `final_scorecard` — it lays out every predictor this case has built (majority baseline, default-threshold model, chosen-threshold model) side by side on the same held-out data.
- In the notebook: run the code cell to generate the scorecard, then fill in the seven decision-note sections below it, in plain language, using what you learned across Lessons 1-7. There's no separate homework — the completed decision note is the deliverable for all of Case 2. For an extra exercise: compress the whole note into a 3-sentence executive summary, as if the ops manager only has thirty seconds.

## What to watch for

The note should be exactly as confident as the evidence actually supports — no more. A probability-based tool isn't a certificate; the recommendation should give one concrete action, not restate the accuracy or F1 number.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

This checks the scorecard numbers — it can't check your decision note's writing, which is graded on communication and interpretation (see [`ASSESSMENT_RUBRIC.md`](../../../../ASSESSMENT_RUBRIC.md) and this lesson's [`exemplar_decision_note.md`](exemplar_decision_note.md) for a model answer).

If you had to cut one section to fit the note on a single slide, which one would you keep, and which would you cut — and what does that choice tell you about what actually matters to Meridian Outlet?
