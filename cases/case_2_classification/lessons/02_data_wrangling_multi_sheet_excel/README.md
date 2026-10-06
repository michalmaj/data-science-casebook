# Lesson 2 — Data Wrangling: Multi-Sheet Excel

**Estimated time:** 35-45 min

## Why we're doing this

Lesson 1's raw load had two rows too many — that was the title row and the real header row both getting read as data. Today we fix that properly, and we'll meet the same kind of mess on the Customers sheet: same idea, different disguise.

Today's question: once both sheets are read correctly and joined, what does a single, complete row of Meridian Outlet's order data actually look like?

## What you need to do

- The same `data/orders.xlsx` from Lesson 1.
- In `task.py`, implement `load_customers`, `load_and_merge_orders`.
- In the notebook: load the Customers sheet and confirm its id column now matches Orders' `customer_id`. Load and merge the Orders sheet — check the shape and column names against Lesson 1's raw load. Confirm the merged table has zero missing values and the same ~14% return rate you'd expect from Lesson 1.

## What to watch for

Order matters: the mismatched column name needs standardizing *before* the merge, not after. Merging on columns with different names simply won't find a match.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, write what would have gone wrong if the two sheets had been merged before renaming the mismatched column. And: the row count dropped from 702 to 700 by skipping exactly two rows above the real header — if Meridian Outlet's export tool ever added a second blank line before the title, what would silently break in this code, and how would you notice before it caused a real error?
