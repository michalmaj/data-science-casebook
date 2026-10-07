# Lesson 8 — Synthesis: Decision Note

**Estimated time:** 45-60 min

## Why we're doing this

Seven lessons of code, and Aurora Stream's retention team will never read a line of it. What they'll read is what you write today. The redundant features, the arbitrary first guess, the metric disagreement, the segment profiles, the stability check — all of it only matters if you can say it plainly enough that someone who's never fit a KMeans model can act on it.

Today's question: given everything you now know, what should Aurora Stream actually do for each subscriber segment — and how confident should they be?

## What you need to do

- The same `data/aurora_stream.sqlite` from Lessons 1-7.
- In `task.py`, implement `load_scaled_features` (reproduced from Lessons 1-2) and one new function, `final_segment_table`, that lays out both segments' feature profiles, sizes, and shares of the subscriber base side by side.
- In the notebook: run the code cell to generate the final segment table, then fill in the seven decision-note sections below it, in plain language, using what you learned across Lessons 1-7. There's no separate homework — the completed decision note is the deliverable for all of Case 3. For an extra exercise: compress the whole note into a 3-sentence executive summary, as if the retention team only has thirty seconds.

## What to watch for

The note should be exactly as confident as the evidence actually supports — no more. The segmentation is a working hypothesis to test, not a discovered fact about the subscriber population; the recommendation should reflect that, not present k=2 as a definitively confirmed count of "real" groups.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

This checks the segment table's numbers — it can't check your decision note's writing, which is graded on communication and interpretation (see [`ASSESSMENT_RUBRIC.md`](../../../../ASSESSMENT_RUBRIC.md) and this lesson's [`exemplar_decision_note.md`](exemplar_decision_note.md) for a model answer).

If you had to cut one section to fit the note on a single slide, which one would you keep, and which would you cut — and what does that choice tell you about what actually matters to Aurora Stream?
