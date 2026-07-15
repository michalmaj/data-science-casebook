# Lesson 7 — Communicating Uncertainty

## Mentor's note

"You've picked a threshold — now imagine handing Meridian Outlet a spreadsheet of raw probabilities. Nobody in ops wants to read '0.34'. Turn that number into something a human can act on."

## Lesson goal

Translate the model's predicted probabilities into a plain-language risk category, and build the report Meridian Outlet's ops team would actually use — then check whether those categories genuinely reflect risk.

## Today's analytical question

Once you sort orders into Low/Medium/High risk, do those categories actually track real return risk — or do they just look tidy?

## What you're given

- The same `data/orders.xlsx` from Lessons 1-6
- `task.py` — seven functions to implement: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `risk_tier`, `risk_report`, plus two more — `tier_summary` and `brier_score` — that check whether the tiers' predicted probabilities are actually trustworthy, not just correctly ordered
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Reproduce Lessons 5-6's exact split and model.
4. Try `risk_tier` on a few example probabilities.
5. Build the full `risk_report` for the test set.
6. Check the actual return rate within each tier — does it increase from Low to High the way you'd expect?
7. Call `tier_summary` and compare each tier's *predicted* probability to its *actual* rate — a well-calibrated model's predicted and observed numbers should be close.
8. Call `brier_score` and compare it to a baseline that always predicts the training set's base rate — is this model actually better calibrated than doing nothing, or just better at sorting orders by risk?

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: describe what you found when you checked the actual return rate by tier, and what `tier_summary`/`brier_score` told you about calibration — did the High tier's predicted probability match its observed rate? If not, would you trust an individual High-tier prediction at face value?

## Reflection

The mentor asks: the High tier's observed return rate (about 17.6%) is actually a bit *lower* than Medium's (about 22.7%) in this test set, even though "High" should mean riskier — and `tier_summary` shows why that's not just an ordering quirk: the High tier's *predicted* average is about 38.3%, more than double what actually happened. With only 17 orders in that tier, is that a real calibration problem, or just noise from a small sample? scikit-learn's `CalibratedClassifierCV` is the standard tool for correcting a gap like this — would you reach for it here, or would you want more data first? How would you communicate this nuance to Meridian Outlet, rather than presenting either the tiers or the raw probabilities as more precise than they actually are?
