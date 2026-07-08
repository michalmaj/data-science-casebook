# Lesson 7 — Communicating Uncertainty

## Mentor's note

"You've picked a threshold — now imagine handing Meridian Outlet a spreadsheet of raw probabilities. Nobody in ops wants to read '0.34'. Turn that number into something a human can act on."

## Lesson goal

Translate the model's predicted probabilities into a plain-language risk category, and build the report Meridian Outlet's ops team would actually use — then check whether those categories genuinely reflect risk.

## Today's analytical question

Once you sort orders into Low/Medium/High risk, do those categories actually track real return risk — or do they just look tidy?

## What you're given

- The same `data/orders.xlsx` from Lessons 1-6
- `task.py` — five functions to implement: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `risk_tier`, `risk_report`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Reproduce Lessons 5-6's exact split and model.
4. Try `risk_tier` on a few example probabilities.
5. Build the full `risk_report` for the test set.
6. Check the actual return rate within each tier — does it increase from Low to High the way you'd expect?

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: describe what you found when you checked the actual return rate by tier — did it look the way you expected? If not, what do you think explains it?

## Reflection

The mentor asks: the High tier's observed return rate (about 17.6%) is actually a bit *lower* than Medium's (about 22.7%) in this test set, even though "High" should mean riskier. With only 17 orders in that tier, is that a real problem with the risk categories, or just noise from a small sample? How would you communicate that nuance to Meridian Outlet, rather than presenting the tiers as a perfectly ordered risk scale?
