# Lesson 2 — Data Quality and Cleaning

**Estimated time:** 35-45 min

## Learning outcomes

- You'll be able to decide a different, justified cleaning strategy per column instead of one blanket `dropna()`.
- You'll be able to tell when dropping rows is the right call versus when imputing is, based on what a missing value in that specific column actually means.
- You'll be able to recognize which cleaning decisions are safe to make before a train/test split exists (a fixed per-row rule) versus which ones have to wait until after (a statistic learned from the data).

## Mentor's note

"Last time you found two columns with gaps and I asked what you'd do about them. 'It depends' was the right instinct — now let's make it concrete. A missing `weather` value and a missing `driver_experience_years` value are not the same kind of problem, and they don't deserve the same fix."

## Lesson goal

Decide, and justify, a specific cleaning action for each column that has missing data — not a single blanket `dropna()`.

## Today's analytical question

TransLine's data has 15 shipments with a gap somewhere. Which rows, which columns, and what should we actually do about each one?

## What you're given

- The same `data/transport_delays.csv` from Lesson 1
- `task.py` — three functions to implement: `load_shipments`, `rows_with_missing_data`, `drop_missing_weather`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Look at `rows_with_missing_data(df)` — confirm which columns are actually affected and how many rows.
4. Decide (and be ready to defend) why dropping is the right call for `weather` — and why `driver_experience_years` also needs fixing, but not yet: imputing it means computing a median, and that computation isn't safe to run until you know which rows are allowed to inform it. Lesson 3 covers that.
5. Confirm `drop_missing_weather(df)` leaves zero missing `weather` values, and that `driver_experience_years` still has gaps afterward — that's expected.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences on why dropping rows for `weather` is safe before any split exists, while filling `driver_experience_years` with a median is not — yet.

## Reflection

The mentor asks: if TransLine later tells you the missing `weather` values were all from the same week (a sensor outage, not random), does that change whether dropping those rows was the right call?
