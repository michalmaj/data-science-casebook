# Lesson 7 — Segment Stability and the Risk of Overinterpretation

**Estimated time:** 50-60 min

## Why we're doing this

A segment you can't reproduce isn't a segment, it's noise. Before telling Aurora Stream to build a retention strategy around these clusters, let's check whether they actually survive being recomputed — on a slightly different sample of subscribers, with a different random start, and across more than just the two k values looked at so far.

Today's question: if you'd only seen 80% of these subscribers, would you have found the same segments?

## What you need to do

- The same `data/aurora_stream.sqlite` from Lessons 1-6.
- In `task.py`, implement four functions: `load_scaled_features`, `subsample_stability`, `initialization_stability`, `stability_comparison_table`.
- In the notebook: load the scaled per-subscriber table again. Run `subsample_stability` at the default k=2 and look at the agreement scores, then again at k=4. Run `initialization_stability` at k=2, 3, 4, and 5 — see whether any of them are sensitive to KMeans's random start the way they might be to resampling. Run `stability_comparison_table` for k=2, 3, 4, 5 and look at silhouette, resample-stability, and smallest-cluster-share side by side.

## Four different questions called "stability"

It's easy to say a segmentation is "stable" as if that were one fact. It isn't — here are four separate questions, and this lesson's data can only answer some of them:

1. **Resampling stability** (`subsample_stability`, above): if you'd only seen 80% of these subscribers, would KMeans find the same groups? This is what varies between seeds here — which subscribers are in the sample — while KMeans itself always runs with the same `random_state`.
2. **Initialization stability** (`initialization_stability`, new in this lesson): on the *same* full data, does KMeans's own random starting point change the answer? This is a genuinely different axis — a segmentation could be fragile to one and rock-solid to the other. For this dataset, the finding is clean and worth taking at face value: every k from 2 to 5 is perfectly stable to initialization (ARI = 1.0, every seed). That's not a dead end — it tells you that whatever disagreement shows up in silhouette or resample-stability isn't KMeans landing in different local optima; it's coming from the data and the sample, not the algorithm's randomness.
3. **Feature-choice sensitivity** (Lesson 5's `compare_feature_sets`): a third, separate axis — does the result change if you'd encoded different columns into the distance metric? Lesson 5 found k=2 robust to this, k=4 not entirely.
4. **Stability over time**, which this lesson's data genuinely cannot speak to: `aurora_stream.sqlite` is one 90-day snapshot. Nothing here tells you whether the same two segments would reappear next quarter — that would take repeated snapshots over time, which this case doesn't have. Don't let "stable under resampling" quietly turn into "stable over time" in anyone's head, including yours.

## Comparing candidates, not crowning a winner

`stability_comparison_table` puts k=2 through k=5 side by side on silhouette, worst-case resample-stability, and the smallest cluster's share of the base — so the choice rests on a set of properties, not whichever single number looks best:

| k | silhouette | resample stability (min ARI) | smallest cluster share |
|---|---:|---:|---:|
| 2 | 0.605 | 1.000 | 27.0% |
| 3 | 0.472 | 0.986 | 27.0% |
| 4 | 0.444 | 0.971 | 12.7% |
| 5 | 0.464 | 0.987 | 12.7% |

k=2 leads on silhouette and is the most resample-stable of the four — and every one of them is equally stable to initialization. That combination, plus the simplicity of a two-group story, is why k=2 is this case's working choice — not because any single row or column "announced" it. One honest caveat: the exact resample-stability numbers for k=3/4/5 are somewhat specific to `subsample_stability`'s particular way of drawing an 80% subsample — a different (equally reasonable) subsampling method could shift them a little. k=2's perfect stability is robust regardless; the finer ranking among k=3/4/5 is not something to read too much into.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

One sentence: k=2's subsample agreement is perfect on every seed; k=4's is high but not perfect, and both are perfectly stable to initialization. What does the *difference between those two kinds of stability* tell you about where k=4's extra fragility actually comes from? And: perfect stability at k=2 — under resampling *and* under initialization — doesn't mean the 2-segment story is the "true" one. It means it's the most reproducible candidate tested, on the data available, under the perturbations checked. What would you still want to check before treating "high-engagement vs. low-engagement" as a permanent fact about Aurora Stream's subscribers, rather than a snapshot of one 90-day window?
