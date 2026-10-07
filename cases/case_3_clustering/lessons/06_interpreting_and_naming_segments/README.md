# Lesson 6 — Interpreting and Naming Segments

**Estimated time:** 45-60 min

## Why we're doing this

Lesson 5 didn't just create noise — among the solutions compared, k=2 came out as a strong candidate: the best silhouette score, and a robust one, since it held up even when the redundant engagement features got swapped out. That's enough reason to stop comparing and actually interpret one solution. Let's fit it, see what separates the two clusters, and give them names a business person would actually use.

Today's question: what actually separates Aurora Stream's two segments, and what would you call each one?

## What you need to do

- The same `data/aurora_stream.sqlite` from Lessons 1-5.
- In `task.py`, implement `load_scaled_features`, `segment_profiles`.
- In the notebook: load the scaled per-subscriber table again, compute `segment_profiles` for the k=2 solution (a strong candidate among the solutions Lesson 5 compared). Compare the three viewing-intensity columns and `tenure_days` between the two clusters. Check whether plan tier or country line up with the clusters, even though the clustering never saw them.

## What to watch for

Any agreement with plan tier or country is suggestive, not confirmation — the clustering never saw those columns, so lining up with them says something about what the segments might represent, but doesn't prove the segments are "real" in some deeper sense.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

One sentence: one segment is small and clearly high-engagement, the other is large and clearly low-engagement, and tenure barely differs between them. What names would you give these two segments, and what would you tell Aurora Stream to do differently for each one? And: this 2-cluster split is really just "engagement level" — `tenure_days`, `plan_tier`, and `country` played no role in separating the groups, because the clustering only ever saw the four scaled numeric features. What real-world differences between subscribers might this segmentation be completely blind to?
