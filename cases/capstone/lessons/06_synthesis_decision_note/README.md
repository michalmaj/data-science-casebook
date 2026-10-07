# Lesson 6 — Synthesis: Decision Note

**Estimated time:** 60-75 min

## The decision to make

Five lessons of code, and the client will never read a line of it. What they'll read is what gets written today. The baseline, the model, how well it generalized to data it never saw — all of it only matters if it can be said plainly enough that someone who's never fit a model can act on it.

Given everything now known: what should the client actually do — and how confident should they be?

## What you have to work with

- `task.py` — the eleven functions from Lessons 4-5, reproduced (`evaluate_classification` now takes an optional `threshold`), plus three new ones: `final_regression_scorecard`, `final_classification_scorecard` (also takes `threshold` — pass whatever was locked in during Lesson 5), `final_clustering_summary`.
- In the notebook: generate the scorecard or segment summary (for the LendWell path, set `CHOSEN_THRESHOLD` to whatever was locked in during Lesson 5, not 0.5 by default), then fill in the seven decision-note sections, using what was learned across Lessons 1-5. There's no separate homework — the completed decision note is the deliverable for the whole capstone.

## Justify it

From this lesson's folder, run:

```bash
uv run pytest
```

This checks the scorecard and segment-summary numbers — it can't check the decision note's writing, which is graded on communication and interpretation (see [`ASSESSMENT_RUBRIC.md`](../../../../ASSESSMENT_RUBRIC.md) and this lesson's [`exemplar_decision_note.md`](exemplar_decision_note.md) for a model answer).

For an extra exercise: compress the whole decision note into a 3-sentence executive summary, as if the client only has thirty seconds. And: which section of the note would be worth keeping, and which cutting, to fit it on a single slide — and what does that choice say about what actually matters to the client?
