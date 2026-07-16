# Lesson 6 — Residual Interpretation

**Estimated time:** 40-50 min

## Learning outcomes

- You'll be able to compute a model's residuals and treat them as data to be studied, not just an accuracy score.
- You'll be able to group residuals by a categorical variable to spot a systematic pattern instead of random noise.
- You'll be able to connect a residual pattern back to a variable the model was never given, and state what that means for the model's blind spot.

## Mentor's note

"A model that's wrong isn't the problem — every model is wrong somewhere. The problem is not knowing *where*. If your errors are random noise, fine, that's the best you can do. If they line up with something specific, that's not noise — that's a clue you're ignoring."

## Lesson goal

Diagnose what Lesson 5's model is systematically getting wrong, and connect that back to a variable it was never given.

## Today's analytical question

Are this model's mistakes random, or do they follow a pattern — and if there's a pattern, what does it point to?

## What you're given

- The same split and model as Lesson 5, reproduced here (`load_shipments`, `split_shipments`, `impute_driver_experience`, `fit_model`)
- `task.py` — three new functions to implement on top of those: `compute_residuals`, `mean_residual_by_weather`, `residual_correlation_with_feature`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Confirm the residuals' correlation with every feature already in the model is essentially zero — then think about *why* that's guaranteed, not a sign of quality.
4. Look at the mean residual by weather — this is the check that actually tells you something, because `weather` was never given to the model.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, state in plain language what the model gets wrong and for which shipments, and propose one fix that doesn't require collecting new data.

## Reflection

The mentor asks: this lesson analyzed residuals on the *training* set, not the test set. Lesson 5 was strict about never touching test data until final scoring. Why is it still fair to look at training residuals here — what are we using them for that's different from evaluating performance?
