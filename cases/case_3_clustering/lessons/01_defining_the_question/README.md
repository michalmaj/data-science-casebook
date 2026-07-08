# Lesson 1 — Defining the Question

## Mentor's note

"New case, new format — SQLite this time. Two tables, no messy Excel tricks, just real SQL. Get the shape of the data, then build the one table you'll actually work from."

## Lesson goal

Get your first look at Aurora Stream's subscriber data, and write the SQL that turns two normalized tables into one per-subscriber table ready for clustering.

## Today's analytical question

What does a single, complete row of subscriber behavior actually look like, once Aurora Stream's raw session logs are joined and aggregated?

## What you're given

- `data/aurora_stream.sqlite` — two tables, `subscribers` and `sessions`
- `task.py` — two functions to implement: `list_tables`, `load_subscriber_features`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

- List the tables.
- Load the joined, per-subscriber feature table.
- Notice which subscribers have zero sessions — decide what that means.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

One sentence: what would go wrong if you used an INNER JOIN instead of a LEFT JOIN here?

## Reflection

The mentor asks: two subscribers have zero sessions. Are they candidates for a "ghost" segment, or should they be excluded from the analysis entirely? There's no single right answer — just be ready to defend yours.
