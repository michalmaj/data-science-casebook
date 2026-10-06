# Lesson 4 — Imbalanced Classes and Baseline

**Estimated time:** 35-45 min

## Why we're doing this

Last lesson asked what accuracy a model gets by always predicting "not returned" — probably something close to 86%. Now let's build that baseline for real and look at exactly which orders it gets wrong.

Today's question: if a baseline model that ignores every feature already scores 86% accuracy, what would it actually take for a real classifier to prove it's useful to Meridian Outlet?

## What you need to do

- The same `data/orders.xlsx` from Lessons 1-3.
- In `task.py`, implement four functions: `load_and_merge_orders`, `predict_majority_baseline`, `accuracy`, `confusion_counts`.
- In the notebook: look at `predict_majority_baseline(df)` — confirm it predicts the exact same value for every single order. Check `accuracy(...)` — confirm it matches Lesson 3's `class_balance` exactly (a majority-class baseline's accuracy is the majority class's share, by definition). Look at `confusion_counts(...)` — notice `tp` and `fn`: the baseline never catches a single real return.

## What to watch for

The confusion matrix shows something a single accuracy number hides: `tp=0` and `fn=98` mean this baseline never — not once — predicts a return, despite 86% "accuracy."

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, write: given `tp=0` and `fn=98`, why is 86% accuracy a misleading headline number for Meridian Outlet's actual problem — catching returns before they ship? And: if Meridian Outlet's real goal is catching as many returns as possible before shipping, is a model that's 86% accurate but never predicts a single return useless, actively harmful, or something in between? What would be worth telling them if this were the only model available?
