# Lesson 3 — Exploratory Data Analysis for Clustering

**Estimated time:** 35-45 min

## Learning outcomes

- You'll be able to check feature correlations when there's no target to validate them against.
- You'll be able to recognize when two features are carrying largely the same signal, and reason about what that means before clustering on both.

## Mentor's note

"No target column this time — nothing to predict, nothing to check your correlations against. Just look at how these four features relate to each other before you decide what KMeans will actually be grouping."

## Lesson goal

Look for structure among Aurora Stream's four scaled features before clustering anything — starting with how correlated they are with each other.

## Today's analytical question

Do these four features actually carry four different signals, or are some of them telling the same story?

## What you're given

- The same `data/aurora_stream.sqlite` from Lessons 1-2
- `task.py` — two functions to implement: `load_scaled_features`, `feature_correlations`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

- Load the scaled per-subscriber table again.
- Compute the correlation matrix between the four features.
- Look specifically at `tenure_days` — how does it relate to the other three?

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

One sentence: three features correlate above 0.9 with each other. What does that suggest about how many genuinely different signals you actually have?

## Reflection

The mentor asks: `session_count`, `total_minutes_watched`, and `avg_minutes_per_session` all correlate above 0.94 with each other, while `tenure_days` barely correlates with any of them (all under 0.1). If you had to describe Aurora Stream's subscribers using just two numbers instead of four, which two would you pick, and why?
