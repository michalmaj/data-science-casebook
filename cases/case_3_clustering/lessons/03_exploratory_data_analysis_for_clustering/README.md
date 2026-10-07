# Lesson 3 — Exploratory Data Analysis for Clustering

**Estimated time:** 35-45 min

## Why we're doing this

No target column this time — nothing to predict, nothing to check correlations against. Let's see how these four features relate to each other before deciding what KMeans will actually be grouping.

Today's question: do these four features actually carry four different signals, or are some of them telling the same story?

## What you need to do

- The same `data/aurora_stream.sqlite` from Lessons 1-2.
- In `task.py`, implement `load_scaled_features`, `feature_correlations`.
- In the notebook: load the scaled per-subscriber table again, compute the correlation matrix between the four features. Look specifically at `tenure_days` — how does it relate to the other three?

## One of these three isn't just correlated

Look at how `avg_minutes_per_session` is actually computed — the same SQL query every lesson uses pulls `AVG(minutes_watched)` alongside `SUM(minutes_watched)` and `COUNT(...)` from the same rows. For every subscriber who has logged at least one session, it's an exact ratio of the other two (`total_minutes_watched / session_count`), not an independently-measured signal that happens to move together with them. Clustering on all three plus `tenure_days` isn't clustering on four independent dimensions with a strong relationship between three — it's closer to two independent dimensions, with the viewing-engagement one counted roughly three times over in the Euclidean distance (confirmed by a quick PCA on the four scaled features: one component explains about 73% of the variance, with all three viewing columns loading on it almost equally).

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

One sentence: three features correlate above 0.9 with each other. What does that suggest about how many genuinely different signals you actually have? And: `session_count`, `total_minutes_watched`, and `avg_minutes_per_session` all correlate above 0.94 with each other, while `tenure_days` barely correlates with any of them (all under 0.1). If you had to describe Aurora Stream's subscribers using just two numbers instead of four, which two would you pick, and why?
