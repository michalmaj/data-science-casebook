# Lesson 5 — Train/Test Split and First Classifier

**Estimated time:** 35-45 min

## Learning outcomes

- You'll be able to split classification data properly while preserving class balance between train and test.
- You'll be able to fit a `LogisticRegression` classifier and evaluate its predictions at the default 0.5 threshold.
- You'll be able to compare a real classifier's catch rate against the majority-class baseline, not just its raw accuracy.
- You'll be able to tell apart two different "does this generalize?" questions — to known customers' future orders versus to entirely new customers — and pick the one that matches the business scenario.

## Mentor's note

"You built a baseline that never caught a single return. Now fit an actual model on the three numeric signals from Lesson 3 — discount, return history, account age — and see if a real classifier does any better at the same 0.5 threshold."

## Lesson goal

Split Meridian Outlet's data properly, fit a real `LogisticRegression` classifier on the three numeric signals from Lesson 3, and evaluate its predictions at the default 0.5 threshold.

Lesson 3 also showed `product_category` was the strongest signal you found — clothing returns at roughly 20% versus home_goods at 7%. It's deliberately left out of `FEATURE_COLUMNS` here: a category needs an extra encoding step before a model can use it, which this case doesn't cover. If you want to see that step, Capstone's optional Lesson 7 walks through it with `ColumnTransformer`.

## Today's analytical question

Does a real classifier, trained on real features, actually catch more returns than the majority baseline — at least at the default threshold?

## What you're given

- The same `data/orders.xlsx` from Lessons 1-4
- `task.py` — five functions to implement: `load_and_merge_orders`, `split_orders`, `split_orders_by_customer`, `fit_classifier`, `predict_return`
- `lesson.ipynb` — the notebook where you'll do the actual work

## Working in the notebook

1. Open `lesson.ipynb`.
2. Once `task.py` is filled in, run the notebook top to bottom.
3. Check `split_orders(df)` — confirm the train/test sizes, and that both sets keep roughly the same return rate.
4. Run `split_orders_by_customer` and compare its customer-overlap numbers against `split_orders` — confirm zero overlap for the group split versus the 90-customer overlap for the row split.
5. Fit the model and look at its coefficients.
6. Predict on the test set and check the confusion matrix — compare `tp` to Lesson 4's baseline.
7. Look at the actual predicted probabilities, not just the 0/1 labels.

## "New data" means two different things here

`split_orders` (step 3 above) carves out a test set — but *what* is it testing generalization to? With 264 customers and 700 orders, most customers (78%) placed more than one order, and a plain random split doesn't know that: it's entirely possible (and, as step 4 showed you, actually happens) for customer X's first order to land in `train_df` and their second order to land in `test_df`. That test row isn't from a customer the model has never met — it's a *new order* from a customer it already has on file.

That's a real, useful question — "does this model work on the next order from a customer we already know?" — but it's a different question from "does this model work on a customer we've never seen at all?" Both are legitimate things to ask; which one matters depends entirely on how Meridian Outlet will actually use the model. If the system scores every incoming order regardless of whether it's a repeat customer, scenario A (known customers) is the realistic one. If Meridian Outlet specifically wants to know how the model handles brand-new sign-ups, that's scenario B.

**This case's main workflow — every split from here through Lesson 8 — answers scenario A: does the model work on future orders from customers already in the training data?** That's consistent with Meridian Outlet's actual ask ("which orders are risky," not "which new customers are risky"), and it's what the plain `split_orders` already does, correctly, for that question.

`split_orders_by_customer` (step 4 above) answers scenario B instead: it groups by customer, so no customer appears on both sides.

One concrete illustration: customer `CUST-0231` — call her Anna — placed 7 orders. Under the row-level split, 5 of those land in `train_df` and 2 in `test_df`: the model isn't meeting a stranger in `test_df`, it's being checked on two more orders from someone it already partly knows, the same way you'd check whether a loyal customer with a long order history gets her next couple of orders scored sensibly. Under the group-level split, Anna lands entirely on one side or the other; there is no "Anna, mostly known."

| | Row split (main, scenario A) | Group split (scenario B) |
|---|---:|---:|
| Train rows / customers | 560 / 248 | 577 / 211 |
| Test rows / customers | 140 / 106 | 123 / 53 |
| Customers in both train and test | 90 | 0 |
| % of test rows whose customer is also in train | 86.4% | 0% |
| Test confusion matrix @ 0.5 threshold | `[[119, 1], [20, 0]]` | `[[108, 0], [15, 0]]` |
| Test ROC-AUC (area under the ROC curve — a threshold-free way to compare ranking quality; 0.5 is random, 1.0 is perfect) | 0.643 | 0.672 |

Notice the two splits' results are *close*, not dramatically different, and the group split's AUC is actually slightly higher here — the opposite of what you might expect if group splits were simply "harder." Don't read that as proof either split is wrong. Three reasons this comparison isn't as dramatic as it could be: the test sets are small (140 and 123 rows, with only 20 and 15 returns respectively — plenty of room for a single split's numbers to wobble); the group split isn't stratified, so its train/test return rates (14.38% / 12.20%) drift a bit further apart than the row split's (13.93% / 14.29%); and `previous_returns_count`/`account_age_days` are fixed attributes assigned to each customer independently of their orders (check `data/generate.py` — they're drawn before any order exists), not a running tally built from the customer's own order history. If a feature were instead something like "this customer's return rate computed from their past orders so far," the row-split-vs-group-split gap would matter far more, because a row split could then let a customer's own *future* orders quietly inform a feature describing their *past*.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete.

## Homework

In `lesson.ipynb`'s "Your notes" cell, write two to three sentences: given the probability range you saw, is this model actually useless, or is 0.5 simply the wrong threshold for Meridian Outlet's problem? The same cell also asks why the row-split and group-split numbers came out close rather than dramatically different — answer that too.

## Reflection

The mentor asks: the model assigned as much as ~54% probability to some orders, yet its confusion matrix at threshold 0.5 looks almost identical to Lesson 4's baseline. If Meridian Outlet's real priority is catching returns, what do you think happens to the confusion matrix if you lower the decision threshold from 0.5 to something like 0.3? You don't need to compute it yet — that's next lesson.
