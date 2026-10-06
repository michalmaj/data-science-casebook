# Lesson 6 — Residual Interpretation

**Estimated time:** 40-50 min

## Why we're doing this

A model that's wrong isn't the problem — every model is wrong somewhere. The problem is not knowing *where*. If the errors are random noise, fine, that's the best you can do. If they line up with something specific, that's not noise — that's a signal you're ignoring.

Today's question: are Lesson 5's model's mistakes random, or do they follow a pattern — and if there's a pattern, what does it point to?

## What you need to do

- The same split as Lesson 3, and the same model as Lesson 5, reproduced here (`load_shipments`, `split_shipments`, `impute_driver_experience`, `fit_model`).
- In `task.py`, implement three new functions: `compute_residuals`, `mean_residual_by_weather`, `residual_correlation_with_feature`.
- In the notebook: confirm the residuals' correlation with every feature already in the model is essentially zero, then look at the mean residual by weather.

## What to watch for

The residuals' correlation with every feature already in the model comes out essentially zero — think about why that's guaranteed by how linear regression fits its coefficients, rather than a sign of quality. The check that actually tells you something is the mean residual by weather, because `weather` was never given to the model.

This lesson analyzes residuals on the *training* set, not the test set — Lesson 5 was strict about never touching test data until final scoring. Why is it still fair to look at training residuals here — what are we using them for that's different from evaluating performance?

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, state in plain language what the model gets wrong and for which shipments, and propose one fix that doesn't require collecting new data.
