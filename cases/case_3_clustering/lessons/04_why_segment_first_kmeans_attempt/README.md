# Lesson 4 — Why Segment? First KMeans Attempt

## Mentor's note

"Aurora Stream doesn't want a model for its own sake — they want to know if 'treat every subscriber the same' is actually the wrong call. Let's find out. Fit a KMeans model, pick some round number of clusters for now, and see what falls out. Don't worry yet about whether it's the *right* number — that's next lesson's problem."

## Lesson goal

Make the business case for segmentation, then fit a first `KMeans` model on Aurora Stream's four scaled features at an arbitrary `k`.

## Today's analytical question

If you split subscribers into a handful of groups using nothing but their viewing behavior, do you get groups that look meaningfully different in size — and does that alone tell you anything worth acting on?

## What you're given

- The same `data/aurora_stream.sqlite` from Lessons 1-3
- `task.py` — two functions to implement: `load_scaled_features`, `fit_kmeans`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

- Load the scaled per-subscriber table again.
- Fit `fit_kmeans` with its default `k=4` and check the resulting inertia.
- Look at how many subscribers landed in each of the four clusters.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

One sentence: one of the four clusters is much smaller than the rest. What would you want to check before recommending Aurora Stream build a retention offer around it?

## Reflection

The mentor asks: right now `k=4` was picked with no real justification — it's just a round number. What does it mean for a business recommendation if the "segments" you're about to describe depend on a number nobody has defended yet?
