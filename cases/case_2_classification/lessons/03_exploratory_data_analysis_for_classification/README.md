# Lesson 3 — Exploratory Data Analysis for Classification

**Estimated time:** 35-45 min

## Why we're doing this

The data is merged now — the real question: which signals are actually worth building a model around, and which just look interesting? Before we touch a single classifier, let's get a feel for what predicts a return and what doesn't.

Today's question: how imbalanced are Meridian Outlet's returns, and which recorded factors — product category, discount, or a customer's own return history — actually move the needle?

## What you need to do

- The same `data/orders.xlsx` from Lessons 1-2.
- In `task.py`, implement four functions: `load_and_merge_orders`, `class_balance`, `return_rate_by_category`, `correlation_with_return`.
- In the notebook: look at `class_balance(df)` — note how rare returns actually are. Look at `return_rate_by_category(df)` — which category returns most, which returns least. Compare `correlation_with_return` for `discount_percent`, `previous_returns_count`, and `account_age_days` — which one is the strongest numeric signal.

## What to watch for

With a target this imbalanced, intuition from regression doesn't carry over directly: a high correlation or a high accuracy number can mean something quite different once one class dominates by sheer count. That's next lesson's topic — for now, just see how rare returns are.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, write: given how rare returns are, what's wrong with judging a future classifier purely on accuracy? And: if 14% of orders get returned, what accuracy would a model get by always predicting "not returned," without looking at a single feature? Would that be a good model?
