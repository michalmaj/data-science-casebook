# Lesson 2 — Feature Selection and Scaling

**Estimated time:** 40-50 min

## Why we're doing this

Session counts range from 0 to 65, minutes watched from 0 to thousands, tenure in hundreds of days. Feed that straight into a distance-based algorithm and tenure will swamp everything else. That needs fixing before anything gets clustered.

Today's question: which of Aurora Stream's subscriber features actually belong in a clustering model, and what happens to them once they're all on the same scale?

## What you need to do

- The same `data/aurora_stream.sqlite` from Lesson 1.
- In `task.py`, implement `load_subscriber_features`, `scale_features`.
- In the notebook: load the per-subscriber table again, scale the four behavioral features. Confirm the scaled columns actually have mean 0 and standard deviation 1.

## What to watch for

The feature with the largest raw range wins the distance calculation, not the one with the most business meaning — unless everything's on the same scale. That's what scaling actually does: it doesn't make a feature more meaningful, it just removes an advantage that came purely from units.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

One sentence: why weren't `plan_tier` and `country` included in `scale_features`? And: `tenure_days` ranges from 35 to 895 — nearly 25x. `session_count` ranges from 0 to 65. Before scaling, which of these two features would have dominated a distance calculation, and by roughly how much?
