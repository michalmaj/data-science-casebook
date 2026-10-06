# Lesson 7 — Communicating Uncertainty

**Estimated time:** 45-55 min

## Why we're doing this

The threshold is chosen — now imagine handing Meridian Outlet a spreadsheet of raw probabilities. Nobody in ops wants to read "0.34." That number needs to become something a human can act on.

Today's question: once orders are sorted into Low/Medium/High risk, do those categories track real return risk — or do they just look tidy?

## What you need to do

- The same `data/orders.xlsx` from Lessons 1-6.
- In `task.py`, implement seven functions: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `risk_tier`, `risk_report`, plus two more — `tier_summary` and `brier_score` — that check whether the tiers' predicted probabilities are actually trustworthy, not just correctly ordered.
- In the notebook: reproduce Lessons 5-6's exact split and model. Try `risk_tier` on a few example probabilities. Build the full `risk_report` for the test set. Check the actual return rate within each tier — does it increase from Low to High the way you'd expect? Call `tier_summary` and compare each tier's *predicted* probability to its *actual* rate — a well-calibrated model's predicted and observed numbers should be close. Call `brier_score` and compare it to a baseline that always predicts the training set's base rate.

## What to watch for

Sorting well by risk and being well calibrated are two different things. A model can correctly rank orders from least to most risky while its predicted probabilities still miss the actual return rate within a given tier — `tier_summary` and `brier_score` check the second thing, not the first.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, describe what you find when checking the actual return rate by tier, and what `tier_summary`/`brier_score` say about calibration — did the High tier's predicted probability match its observed rate? If not, is an individual High-tier prediction worth trusting at face value? And: the High tier's observed return rate (about 17.6%) is actually a bit *lower* than Medium's (about 22.7%) in this test set, even though "High" should mean riskier — and `tier_summary` shows why that's not just an ordering quirk: the High tier's *predicted* average is about 38.3%, more than double what actually happened. With only 17 orders in that tier, is that a real calibration problem, or just noise from a small sample? scikit-learn's `CalibratedClassifierCV` is the standard tool for correcting a gap like this — worth reaching for here, or better to get more data first? How would this nuance get communicated to Meridian Outlet, rather than presenting either the tiers or the raw probabilities as more precise than they actually are?
