# Lesson 5 — Choosing k: Comparing Solutions

**Estimated time:** 40-50 min

## Why we're doing this

Lesson 4's k=4 was a guess. Now let's actually compare solutions: fit KMeans across a range of k, look at inertia the way the elbow method wants, then look at silhouette score. There's no guarantee they'll point at the same answer.

Today's question: does inertia's elbow and silhouette score's peak point to the same number of clusters — and if not, which one should actually guide the decision?

## What you need to do

- The same `data/aurora_stream.sqlite` from Lessons 1-4.
- In `task.py`, implement `load_scaled_features`, `cluster_metrics_by_k`, `compare_feature_sets`.
- In the notebook: compute `cluster_metrics_by_k` for k from 2 to 8, compare where inertia's curve bends against which k has the highest silhouette score. Run `compare_feature_sets` at k=2 and again at k=4, using `REDUCED_FEATURE_COLUMNS` (just `total_minutes_watched` and `tenure_days`) against the full four-feature set — see whether the reported segmentation depends on which columns got handed to KMeans.

## Silhouette's peak isn't a clean runner-up list, and it isn't the only choice that matters

Silhouette score peaks sharply at k=2 — that's real, and worth taking seriously. But it isn't a ranked list you can fall back one step on if you don't trust the top result: k=3 through k=8 wobble between roughly 0.44 and 0.47 with no consistent order (k=3 beats k=4, k=4 loses to k=5 and k=6, k=6 beats k=7 and k=8) — there's no clean "second place" hiding in there. Silhouette compared the solutions actually fit, under the geometry those four features define; it didn't scan every possible number of segments and rank them.

That "geometry those four features define" part matters more than it might look. `compare_feature_sets` fits the same k on the full `FEATURE_COLUMNS` and on `REDUCED_FEATURE_COLUMNS` — one representative engagement signal (`total_minutes_watched`) plus `tenure_days`, dropping `session_count` and the exactly-derived `avg_minutes_per_session` (Lesson 3). At k=2, the two feature sets agree completely (`ari = 1.0`) — reassuring, but not because k=2 is somehow immune to feature choice. At k=4, they disagree (`ari ≈ 0.977`): a handful of subscribers land in different clusters depending on which columns were used. And the reduced set's silhouette is actually *higher* than the full set's at k=4 (0.560 vs. 0.444) — fewer, less redundant features can look cleaner by this metric. Part of that gap is a known property of silhouette itself, not just redundancy: it tends to read higher in lower-dimensional spaces, so 2-feature and 4-feature silhouette scores aren't directly comparable on an apples-to-apples scale. Either way, it's a reason not to over-trust a single silhouette number. Which features get encoded is part of defining the segmentation, same as k is — not a preliminary detail to get out of the way before the "real" decision.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

One sentence: the highest silhouette score belongs to a smaller k than Lesson 4's guess of 4. What's worth telling Aurora Stream about relying on a single metric to pick the "right" number of segments? Add a second sentence: does the feature-set comparison at k=2 and k=4 change that answer? And: inertia keeps falling smoothly across the whole k=2 to 8 range, with no single sharp elbow — on inertia alone, almost any k is defensible. Silhouette score, on the other hand, peaks clearly at one value. What does it mean for a business recommendation when two "standard" methods for choosing k don't actually agree?
