# Lesson 2 — Data Quality and Cleaning

**Estimated time:** 35-45 min

## Why we're doing this

In Lesson 1 you found two columns with gaps and had to think about what to do with them. "It depends" was the right instinct — now let's make it concrete. A missing `weather` value and a missing `driver_experience_years` value are not the same kind of problem, and they don't deserve the same fix.

TransLine's data has 15 shipments with a gap somewhere. Today's question: which rows, which columns, and what should we actually do about each one?

## What you need to do

- The same `data/transport_delays.csv` from Lesson 1.
- In `task.py`, implement `load_shipments`, `rows_with_missing_data`, `drop_missing_weather`.
- In the notebook: check `rows_with_missing_data(df)` and confirm which columns are affected and how many rows. Decide — and be ready to defend — why dropping is the right call for `weather`, and why `driver_experience_years` also needs fixing but not yet. Imputing it means computing a median, and that computation isn't safe to run until you know which rows are allowed to inform it — Lesson 3 handles that.

## What to watch for

Not every cleaning decision can happen at the same point. Dropping a row is a fixed per-row rule — it doesn't depend on the rest of the data, so it's safe now. Filling with a median is a statistic computed from the data — compute it before the train/test split and information from the test set leaks into training. That's why `drop_missing_weather(df)` leaves zero missing `weather` values, but `driver_experience_years` still has gaps after this lesson — that's expected.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, write down why dropping rows for `weather` is safe before any split exists, while filling `driver_experience_years` with a median is not — yet. And: if TransLine later told you the missing `weather` values were all from the same week (a sensor outage, not random) — would that change whether dropping those rows was the right call?
