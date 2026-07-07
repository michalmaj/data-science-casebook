# Lesson 2 — Data Quality and Cleaning

## Mentor's note

"Last time you found two columns with gaps and I asked what you'd do about them. 'It depends' was the right instinct — now let's make it concrete. A missing `weather` value and a missing `driver_experience_years` value are not the same kind of problem, and they don't deserve the same fix."

## Lesson goal

Decide, and justify, a specific cleaning action for each column that has missing data — not a single blanket `dropna()`.

## Today's analytical question

TransLine's data has 15 shipments with a gap somewhere. Which rows, which columns, and what should we actually do about each one?

## What you're given

- The same `data/transport_delays.csv` from Lesson 1
- `task.py` — five functions to implement: `load_shipments`, `rows_with_missing_data`, `drop_missing_weather`, `impute_missing_experience`, `clean_shipments`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Look at `rows_with_missing_data(df)` — confirm which columns are actually affected and how many rows.
4. Decide (and be ready to defend) why dropping is the right call for `weather` but imputing is the right call for `driver_experience_years`.
5. Confirm `clean_shipments(df)` leaves zero missing values anywhere.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences justifying the different treatment of the two columns, and note what would change your mind (e.g., if `weather` were missing on 30% of rows instead of ~1%).

## Reflection

The mentor asks: if TransLine later tells you the missing `weather` values were all from the same week (a sensor outage, not random), does that change whether dropping those rows was the right call?
