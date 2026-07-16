# Lesson 7 — Segment Stability and the Risk of Overinterpretation

**Estimated time:** 50-60 min

## Learning outcomes

- You'll be able to test a clustering solution's stability by refitting it on repeated random subsamples and comparing labels with an adjusted Rand index.
- You'll be able to state precisely what a subsample-stability check does and doesn't tell you — sampling sensitivity, not K-means initialization sensitivity.
- You'll be able to decide, with a stability number in hand, whether a segment is solid enough to build a retention strategy around.

## Mentor's note

"A segment you can't reproduce isn't a segment, it's noise. Before you tell Aurora Stream to build a retention strategy around these clusters, check whether they actually survive being recomputed on a slightly different sample of subscribers."

## Lesson goal

Test how much the k=2 clustering solution's labels change when refit on repeated 80% random subsamples, and compare that stability to k=4.

## Today's analytical question

If you'd only seen 80% of these subscribers, would you have found the same segments?

## What you're given

- The same `data/aurora_stream.sqlite` from Lessons 1-6
- `task.py` — two functions to implement: `load_scaled_features`, `subsample_stability`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

- Load the scaled per-subscriber table again.
- Run `subsample_stability` at the default k=2 and look at the agreement scores.
- Run it again at k=4 and compare.

**A note on what this measures:** `subsample_stability` only varies which subscribers get sampled — it always fits KMeans with the same `random_state`, so it doesn't separately test sensitivity to the algorithm's random centroid initialization. That's a real, different question worth asking. For this dataset, it turns out not to matter: refitting the full k=2 solution at five different `random_state` values gives ARI = 1.0 against each other every time — this segmentation is not an artifact of which random start KMeans happened to pick.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

One sentence: k=2's subsample agreement is perfect on every seed; k=4's is high but not perfect. What does that difference tell you about how much confidence to put in a finer-grained segmentation versus a coarser one?

## Reflection

The mentor asks: perfect stability at k=2 doesn't mean the 2-segment story is the "true" one — it just means it's the most reproducible one you tested. What would you still want to check before treating "high-engagement vs. low-engagement" as a permanent fact about Aurora Stream's subscribers, rather than a snapshot of one 90-day window?
