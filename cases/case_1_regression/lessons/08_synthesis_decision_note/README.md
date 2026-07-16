# Lesson 8 — Synthesis: Decision Note

**Estimated time:** 40-50 min

## Learning outcomes

- You'll be able to assemble every prior lesson's model and baseline into one comparison table a non-technical stakeholder can actually read.
- You'll be able to write a decision note that states a recommendation, its confidence, and its limitations in plain language.
- You'll be able to decide what's genuinely actionable from seven lessons of analysis and what deliberately isn't.

## Mentor's note

"Seven lessons of code, and TransLine's ops manager will never read a line of it. What they'll read is what you write today. Everything you found — the baseline, the model, the blind spot, what's actionable and what isn't — only matters if you can say it plainly enough that someone who's never seen a p-value can act on it."

## Lesson goal

Assemble everything from Lessons 1-7 into a decision note TransLine could actually receive and act on.

## Today's analytical question

Given everything you now know, what should TransLine actually do — and how confident should they be?

## What you're given

- The same split data and model as Lessons 5-7 (reproduced here via `load_shipments`, `split_shipments`, `impute_driver_experience`, `fit_model`)
- `task.py` — one new function, `final_scorecard`, that lays out every predictor this case has built (zero-baseline, mean-baseline, model) side by side on the same held-out data
- `lesson.ipynb` — this time, most of the notebook is the decision note template itself, not code

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the code cell to generate the scorecard.
3. Fill in each of the seven decision-note sections below it, in plain language, using what you learned across Lessons 1-7.
4. There is no separate homework this lesson — the completed decision note is the deliverable for all of Case 1.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. This checks the scorecard numbers — it cannot check your decision note's writing, which is graded on communication and interpretation (see [`ASSESSMENT_RUBRIC.md`](../../../../ASSESSMENT_RUBRIC.md) and this lesson's [`exemplar_decision_note.md`](exemplar_decision_note.md) for a model answer).

## Homework

None separately — but if you want an extra exercise, try compressing your entire decision note into a 3-sentence executive summary, as if the ops manager only has thirty seconds.

## Reflection

The mentor asks: if you had to cut one section of your decision note to fit on a single slide, which one would you keep, and which would you cut — and what does that choice tell you about what actually matters to TransLine?
