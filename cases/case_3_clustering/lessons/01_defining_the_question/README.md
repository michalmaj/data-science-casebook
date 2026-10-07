# Lesson 1 — Defining the Question

**Estimated time:** 35-45 min

## Why we're doing this

New case, new format — SQLite this time. Two tables, no messy Excel tricks, just real SQL. Let's get the shape of the data, then build the one table we'll actually work from.

Today's question: what does a single, complete row of subscriber behavior actually look like, once Aurora Stream's raw session logs are joined and aggregated?

## What you need to do

- `data/aurora_stream.sqlite` — two tables, `subscribers` and `sessions`.
- In `task.py`, implement `list_tables`, `load_subscriber_features`.
- In the notebook: list the tables, load the joined, per-subscriber feature table. Notice which subscribers have zero sessions — decide what that means.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

One sentence: what would go wrong with an INNER JOIN instead of a LEFT JOIN here? And: two subscribers have zero sessions. Are they candidates for a "ghost" segment, or should they be excluded from the analysis entirely? There's no single right answer — just write down the reasoning.
