# Lesson 3 — Exploratory Data Analysis for Classification

**Estimated time:** 35-45 min

## Learning outcomes

- You'll be able to measure how imbalanced a binary target actually is before building any model around it.
- You'll be able to compute a rate-by-category breakdown to find which factors are genuinely associated with the outcome.
- You'll be able to tell a factor that merely "looks interesting" apart from one with a real, measurable relationship to the target.

## Mentor's note

"Merged data in hand — now the real question: which of these signals are actually worth building a model around, and which just look interesting? Before you touch a single classifier, get a feel for what predicts a return and what doesn't."

## Lesson goal

Explore Meridian Outlet's merged order data to find which factors are actually associated with a return, and get an honest read on how rare returns are in the first place.

## Today's analytical question

How imbalanced are Meridian Outlet's returns, and which recorded factors — product category, discount, or a customer's own return history — actually move the needle?

## What you're given

- The same `data/orders.xlsx` from Lessons 1-2
- `task.py` — four functions to implement: `load_and_merge_orders`, `class_balance`, `return_rate_by_category`, `correlation_with_return`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Look at `class_balance(df)` — note how rare returns actually are.
4. Look at `return_rate_by_category(df)` — which category returns most, which returns least?
5. Compare `correlation_with_return` for `discount_percent`, `previous_returns_count`, and `account_age_days` — which one is the strongest numeric signal?

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: given how rare returns are, what's wrong with judging a future classifier purely on accuracy?

## Reflection

The mentor asks: if 14% of orders get returned, what accuracy would a model get by always predicting "not returned," without looking at a single feature? Would you call that a good model?
