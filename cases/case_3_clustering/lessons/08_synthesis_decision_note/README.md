# Lesson 8 — Synthesis: Decision Note

**Estimated time:** 45-60 min

## Learning outcomes

- You'll be able to assemble redundant-feature findings, metric disagreement, segment profiles, and a stability check into one decision note.
- You'll be able to recommend a segment-specific action while being explicit about what the clustering can and can't support as evidence.
- You'll be able to decide what Aurora Stream should actually do for each segment, and how confident they should be in each recommendation.

## Mentor's note

"Seven lessons of code, and Aurora Stream's retention team will never read a line of it. What they'll read is what you write today. Everything you found — the redundant features, the arbitrary first guess, the metric disagreement, the segment profiles, the stability check — only matters if you can say it plainly enough that someone who's never fit a KMeans model can act on it."

## Lesson goal

Assemble everything from Lessons 1-7 into a decision note Aurora Stream could actually receive and act on.

## Today's analytical question

Given everything you now know, what should Aurora Stream actually do for each subscriber segment — and how confident should they be?

## What you're given

- The same `data/aurora_stream.sqlite` from Lessons 1-7
- `task.py` — two functions: `load_scaled_features` (reproduced from Lessons 1-2) and one new function, `final_segment_table`, that lays out both segments' feature profiles, sizes, and shares of the subscriber base side by side
- `lesson.ipynb` — this time, most of the notebook is the decision note template itself, not code

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the code cell to generate the final segment table.
3. Fill in each of the seven decision-note sections below it, in plain language, using what you learned across Lessons 1-7.
4. There is no separate homework this lesson — the completed decision note is the deliverable for all of Case 3.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. This checks the segment table's numbers — it cannot check your decision note's writing, which is graded on communication and interpretation (see [`ASSESSMENT_RUBRIC.md`](../../../../ASSESSMENT_RUBRIC.md) and this lesson's [`exemplar_decision_note.md`](exemplar_decision_note.md) for a model answer).

## Homework

None separately — but if you want an extra exercise, try compressing your entire decision note into a 3-sentence executive summary, as if the retention team only has thirty seconds.

## Reflection

The mentor asks: if you had to cut one section of your decision note to fit on a single slide, which one would you keep, and which would you cut — and what does that choice tell you about what actually matters to Aurora Stream?
