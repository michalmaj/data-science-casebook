# Lesson 1 — Defining the Question

## Mentor's note

"New client, new format. Meridian Outlet's data doesn't come in a tidy CSV — it comes in an Excel export built for a human, not a script. Before you touch any of that, get the business question straight, the same way you did for TransLine. The mess is next lesson's problem."

## Lesson goal

Turn Meridian Outlet's complaint into a specific, measurable analytical question, and take a first, honest look at their Excel export — including its problems.

## Today's analytical question

Given what Meridian Outlet already records about an order, what exactly should we predict, and what shape is the data actually in?

## What you're given

- `data/orders.xlsx` — a two-sheet Excel export ("Orders" and "Customers")
- `task.py` — three functions to implement: `list_sheet_names`, `load_raw_orders_sheet`, `target_column_name`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. List the sheet names — note there are two, not one.
4. Load the Orders sheet with pandas' plain defaults and look closely at the column names and shape.
5. Confirm you can still name the target column despite the messy load.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences describing exactly what's wrong with the raw load — be specific about what you see in the columns and the first rows.

## Reflection

The mentor asks: the raw load has 702 rows, but Meridian Outlet says they shipped 700 orders in the quarter. Before you even open Lesson 2, what's your best guess for where the extra two rows came from?
