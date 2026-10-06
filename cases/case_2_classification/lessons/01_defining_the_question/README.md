# Lesson 1 — Defining the Question

**Estimated time:** 25-35 min

## Why we're doing this

New client, new format. Meridian Outlet's data doesn't come in a tidy CSV — it comes in an Excel export built for a human, not a script. Before we touch that mess, let's get the business question straight, the same way we did for TransLine — the mess is next lesson's problem.

Today's question: given what Meridian Outlet already records about an order, what exactly should we predict, and what shape is the data actually in?

## What you need to do

- `data/orders.xlsx` — a two-sheet Excel export ("Orders" and "Customers").
- In `task.py`, implement `list_sheet_names`, `load_raw_orders_sheet`, `target_column_name`.
- In the notebook: list the sheet names (there are two, not one), load the Orders sheet with pandas' plain defaults and look closely at the column names and shape. Confirm you can still name the target column despite the messy load.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, describe exactly what's wrong with the raw load — what you see in the columns and the first rows. And: the raw load has 702 rows, but Meridian Outlet says they shipped 700 orders in the quarter — before you open Lesson 2, what's your best guess for where the extra two rows came from?
