# Lesson 3 — Exploratory Data Analysis for Clustering

**Estimated time:** 35-45 min

## Learning outcomes

- You'll be able to check feature correlations when there's no target to validate them against.
- You'll be able to recognize when several features are carrying largely the same signal — including when one is an exact derived function of the others, not just correlated with them — and reason about what that means before clustering on all of them.

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

## One of these three isn't just correlated

Look at how `avg_minutes_per_session` is actually computed — the same SQL query every lesson uses pulls `AVG(minutes_watched)` alongside `SUM(minutes_watched)` and `COUNT(...)` from the same rows. For every subscriber who has logged at least one session, it's an exact ratio of the other two (`total_minutes_watched / session_count`), not an independently-measured signal that happens to move together with them. Clustering on all three plus `tenure_days` isn't clustering on four independent dimensions with a strong relationship between three — it's closer to two independent dimensions, with the viewing-engagement one counted roughly three times over in the Euclidean distance (confirmed by a quick PCA on the four scaled features: one component explains about 73% of the variance, with all three viewing columns loading on it almost equally).

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
