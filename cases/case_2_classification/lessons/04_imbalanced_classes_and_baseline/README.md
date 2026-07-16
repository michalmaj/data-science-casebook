# Lesson 4 — Imbalanced Classes and Baseline

**Estimated time:** 35-45 min

## Learning outcomes

- You'll be able to build a majority-class baseline and see exactly why its headline accuracy number can be misleading.
- You'll be able to compute a confusion matrix and read what it reveals that a single accuracy score hides.
- You'll be able to explain why a model that's "86% accurate" but catches zero real positives isn't actually useful.

## Mentor's note

"Last lesson I asked what accuracy a model gets by always predicting 'not returned' — you probably guessed something close to 86%. Now build that baseline for real, and look at exactly which orders it gets wrong."

## Lesson goal

Build the simplest possible classifier — always predict the majority class — and see why a headline accuracy number alone can hide a model that catches zero actual returns.

## Today's analytical question

If a baseline model that ignores every feature already scores 86% accuracy, what would it actually take for a real classifier to prove it's useful to Meridian Outlet?

## What you're given

- The same `data/orders.xlsx` from Lessons 1-3
- `task.py` — four functions to implement: `load_and_merge_orders`, `predict_majority_baseline`, `accuracy`, `confusion_counts`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Look at `predict_majority_baseline(df)` — confirm it predicts the exact same value for every single order.
4. Check `accuracy(...)` — confirm it matches Lesson 3's `class_balance` almost exactly.
5. Look at `confusion_counts(...)` — notice `tp` and `fn`: the baseline never catches a single real return.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: given `tp=0` and `fn=98` in that confusion matrix, why is 86% accuracy a misleading headline number for Meridian Outlet's actual problem — catching returns before they ship?

## Reflection

The mentor asks: if Meridian Outlet's real goal is catching as many returns as possible before shipping, is a model that's 86% accurate but never predicts a single return useless, actively harmful, or something in between? What would you tell them if this were the only model you had?
