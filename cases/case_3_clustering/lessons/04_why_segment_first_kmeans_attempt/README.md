# Lesson 4 — Why Segment? First KMeans Attempt

**Estimated time:** 40-50 min

## Why we're doing this

Aurora Stream doesn't want a model for its own sake — they want to know if "treat every subscriber the same" is actually the wrong call. Let's find out: fit a KMeans model, pick some round number of clusters for now, and see what falls out. Whether it's the *right* number is next lesson's problem.

Today's question: if we split subscribers into a handful of groups using nothing but their viewing behavior, do we get groups that look meaningfully different in size — and does that alone tell us anything worth acting on?

## What you need to do

- The same `data/aurora_stream.sqlite` from Lessons 1-3.
- In `task.py`, implement `load_scaled_features`, `fit_kmeans`.
- In the notebook: load the scaled per-subscriber table again, fit `fit_kmeans` with its default `k=4` and check the resulting inertia. Look at how many subscribers landed in each of the four clusters.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

One sentence: two of the four clusters are noticeably smaller than the other two. What would you want to check before recommending Aurora Stream build a retention offer around one of the smaller ones? And: `k=4` was picked with no real justification — it's just a round number. What does it mean for a business recommendation if the "segments" you're about to describe depend on a number nobody has defended yet?
