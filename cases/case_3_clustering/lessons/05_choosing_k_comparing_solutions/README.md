# Lesson 5 — Choosing k: Comparing Solutions

**Estimated time:** 40-50 min

## Learning outcomes

- You'll be able to compare `KMeans` solutions across a range of k using both inertia (elbow method) and silhouette score.
- You'll be able to handle the case where two standard model-selection metrics disagree, and decide which one should actually drive the choice.

## Mentor's note

"Lesson 4's k=4 was a guess, and I told you so at the time. Now let's actually compare solutions. Fit KMeans across a range of k, look at inertia the way the elbow method wants you to, then look at silhouette score. Don't be surprised if they don't point at the same answer."

## Lesson goal

Compare `KMeans` solutions across a range of k values using two metrics — inertia (elbow method) and silhouette score — and see whether they agree on a "best" k.

## Today's analytical question

Does inertia's elbow and silhouette score's peak point to the same number of clusters — and if not, which one should actually guide the decision?

## What you're given

- The same `data/aurora_stream.sqlite` from Lessons 1-4
- `task.py` — two functions to implement: `load_scaled_features`, `cluster_metrics_by_k`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

- Load the scaled per-subscriber table again.
- Compute `cluster_metrics_by_k` for k from 2 to 8.
- Compare where inertia's curve bends against which k has the highest silhouette score.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

One sentence: the highest silhouette score belongs to a smaller k than Lesson 4's guess of 4. What would you tell Aurora Stream about relying on a single metric to pick the "right" number of segments?

## Reflection

The mentor asks: inertia keeps falling smoothly across the whole k=2 to 8 range, with no single sharp elbow — on inertia alone, almost any k is defensible. Silhouette score, on the other hand, peaks clearly at one value. What does it mean for a business recommendation when two "standard" methods for choosing k don't actually agree?
