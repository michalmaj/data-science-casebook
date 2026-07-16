# Lesson 2 — Data Wrangling: Multi-Sheet Excel

**Estimated time:** 35-45 min

## Learning outcomes

- You'll be able to read a real-world Excel sheet whose title row got read as data, and recover its actual header.
- You'll be able to standardize a column name that's spelled differently across two sheets before joining on it.
- You'll be able to merge two sheets into one clean, order-level table ready for exploration.

## Mentor's note

"You noticed the raw load had two rows too many — that was the title row and the real header row both getting read as data. Today you fix that properly, and you'll meet the same kind of mess on the Customers sheet: same idea, different disguise."

## Lesson goal

Read both sheets of `orders.xlsx` with their real headers, standardize the mismatched customer-id column name, and merge them into one order-level table ready for analysis.

## Today's analytical question

Once both sheets are read correctly and joined, what does a single, complete row of Meridian Outlet's order data actually look like?

## What you're given

- The same `data/orders.xlsx` from Lesson 1
- `task.py` — two functions to implement: `load_customers`, `load_and_merge_orders`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Load the Customers sheet and confirm its id column now matches Orders' `customer_id`.
4. Load and merge the Orders sheet — check the shape and column names against what you saw in Lesson 1's raw load.
5. Confirm the merged table has zero missing values and the same ~14% return rate you'd expect from Lesson 1.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: what would have gone wrong if you'd merged the two sheets before renaming the mismatched column, and why?

## Reflection

The mentor asks: you got from 702 rows down to 700 by skipping exactly two rows above the real header. If Meridian Outlet's export tool ever added a second blank line before the title, what would silently break in your code — and how would you notice before it caused a real error?
