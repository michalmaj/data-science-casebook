# Lesson 5 — Train/Test Split and First Classifier

## Mentor's note

"You built a baseline that never caught a single return. Now fit an actual model on the signals you found in Lesson 3 — discount, return history, account age — and see if a real classifier does any better at the same 0.5 threshold."

## Lesson goal

Split Meridian Outlet's data properly, fit a real `LogisticRegression` classifier on the signals you found in Lesson 3, and evaluate its predictions at the default 0.5 threshold.

## Today's analytical question

Does a real classifier, trained on real features, actually catch more returns than the majority baseline — at least at the default threshold?

## What you're given

- The same `data/orders.xlsx` from Lessons 1-4
- `task.py` — four functions to implement: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `predict_return`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Check `split_orders(df)` — confirm the train/test sizes, and that both sets keep roughly the same return rate.
4. Fit the model and look at its coefficients.
5. Predict on the test set and check the confusion matrix — compare `tp` to Lesson 4's baseline.
6. Look at the actual predicted probabilities, not just the 0/1 labels.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: given the probability range you saw, is this model actually useless, or is 0.5 simply the wrong threshold for Meridian Outlet's problem?

## Reflection

The mentor asks: the model assigned as much as ~54% probability to some orders, yet its confusion matrix at threshold 0.5 looks almost identical to Lesson 4's baseline. If Meridian Outlet's real priority is catching returns, what do you think happens to the confusion matrix if you lower the decision threshold from 0.5 to something like 0.3? You don't need to compute it yet — that's next lesson.
