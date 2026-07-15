# Lesson 6 — Interpreting and Naming Segments

## Mentor's note

"Lesson 5 didn't just create noise — silhouette score clearly pointed at k=2. So let's stop comparing solutions and actually interpret one. Fit it, look at what separates the two clusters, and give them names a business person would actually use."

## Lesson goal

Compute per-cluster feature profiles for the k=2 solution Lesson 5 pointed to, and translate the result into business-meaningful segment names.

## Today's analytical question

What actually separates Aurora Stream's two segments, and what would you call each one?

## What you're given

- The same `data/aurora_stream.sqlite` from Lessons 1-5
- `task.py` — two functions to implement: `load_scaled_features`, `segment_profiles`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

- Load the scaled per-subscriber table again.
- Compute `segment_profiles` for the k=2 solution.
- Compare the three viewing-intensity columns and tenure_days between the two clusters.
- Check whether plan tier or country line up with the clusters, even though the clustering never saw them.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

One sentence: one segment is small and clearly high-engagement, the other is large and clearly low-engagement, and tenure barely differs between them. What would you name these two segments, and what would you tell Aurora Stream to do differently for each one?

## Reflection

The mentor asks: this 2-cluster split is really just "engagement level" — tenure_days, plan_tier, and country played no role in separating the groups, because the clustering only ever saw the four scaled numeric features. What real-world differences between subscribers might this segmentation be completely blind to?
