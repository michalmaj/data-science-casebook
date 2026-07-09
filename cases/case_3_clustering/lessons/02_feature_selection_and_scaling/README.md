# Lesson 2 — Feature Selection and Scaling

## Mentor's note

"Session counts range from 0 to 65, minutes watched from 0 to thousands, tenure in hundreds of days. Feed that straight into a distance-based algorithm and tenure will swamp everything else. Fix that before you cluster anything."

## Lesson goal

Decide which columns actually describe viewing behavior, and scale them so no single feature dominates distance calculations.

## Today's analytical question

Which of Aurora Stream's subscriber features actually belong in a clustering model, and what happens to them once they're all on the same scale?

## What you're given

- The same `data/aurora_stream.sqlite` from Lesson 1
- `task.py` — two functions to implement: `load_subscriber_features`, `scale_features`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

- Load the per-subscriber table again.
- Scale the four behavioral features.
- Confirm the scaled columns actually have mean 0 and standard deviation 1.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

One sentence: why weren't `plan_tier` and `country` included in `scale_features`?

## Reflection

The mentor asks: `tenure_days` ranges from 35 to 895 — nearly 25x. `session_count` ranges from 0 to 65. Before scaling, which of these two features would have dominated a distance calculation, and by roughly how much?
