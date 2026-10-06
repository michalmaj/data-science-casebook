# Lesson 5 — Train/Test Split and First Classifier

**Estimated time:** 35-45 min

## Why we're doing this

We built a baseline that never caught a single return. Now we fit an actual model on the three numeric signals from Lesson 3 — discount, return history, account age — and see if a real classifier does any better at the same 0.5 threshold.

Let's split Meridian Outlet's data properly, fit a real `LogisticRegression` classifier on the three numeric signals from Lesson 3, and see what the default 0.5 threshold does to it — without opening `test_df` to find out. `test_df` gets created in this lesson and then set aside; it isn't opened again until Lesson 6, after a threshold is actually chosen.

Lesson 3 also showed the strongest signal found was `product_category` — clothing returns at roughly 20% versus home_goods at 7%. It's deliberately left out of `FEATURE_COLUMNS` here: a category needs an extra encoding step before a model can use it, which this case doesn't cover. If you want to see that step, Capstone's optional Lesson 7 walks through it with `ColumnTransformer`.

Today's question: does a real classifier, trained on real features, catch more returns than the majority baseline — at least at the default threshold?

## What you need to do

- The same `data/orders.xlsx` from Lessons 1-4.
- In `task.py`, implement five functions: `load_and_merge_orders`, `split_orders`, `split_orders_by_customer`, `fit_classifier`, `predict_return`.
- In the notebook:
  1. Check `split_orders(df)` — confirm the train/test sizes, and that both sets keep roughly the same return rate. Then leave `test_df` alone — don't read its contents again for the rest of this notebook, not even to count something as simple as customers.
  2. Carve a demonstration `fit_df`/`val_df` pair out of `train_df` (using `split_orders` again, just on `train_df` this time) and check the customer overlap *there* — this tells you what a row-level split like `split_orders(df)` tends to do, without opening the real `test_df` to confirm it.
  3. Fit the model and look at its coefficients.
  4. Predict *in-sample*, on `train_df` itself — not on `test_df` — and check the confusion matrix. Compare `tp` to Lesson 4's baseline.
  5. Look at the actual predicted probabilities (still in-sample), not just the 0/1 labels.
  6. Run `split_orders_by_customer` on `train_df` and compare it to the demonstration row-level split from step 2 — confirm zero overlap for the group split versus real overlap for the row split, then compare both on their own held-out validation slice.

## "New data" means two different things here — and the test set stays closed either way

`split_orders` (step 1 above) splits `df` by row, not by customer — so what does a test set built this way actually represent? We won't find out by reading `test_df`'s own contents; that's exactly the kind of peek this lesson avoids, even for something as harmless-looking as a customer count. Instead, step 2 runs the identical splitting function on `train_df` to produce a demonstration `fit_df`/`val_df` pair, and checks the overlap there. With 264 customers and 700 orders, most customers (78%) placed more than one order, and a plain random split doesn't know that: in the demonstration split, 77 customers show up on both sides, and 84.8% of `val_df`'s rows belong to a customer `fit_df` already has on file. `test_df` was carved out by that exact same function with the exact same parameters, so the real train/test split almost certainly looks the same way — we just never need to open it up to know that. A test row built like this wouldn't be from a customer the model has never met; it would be a *new order* from a customer it already has on file.

That's a real, useful question — "does this model work on the next order from a customer we already know?" — but it's a different question from "does this model work on a customer we've never seen at all?" Both are legitimate things to ask; which one matters depends entirely on how Meridian Outlet will actually use the model. If the system scores every incoming order regardless of whether it's a repeat customer, scenario A (known customers) is the realistic one. If Meridian Outlet specifically wants to know how the model handles brand-new sign-ups, that's scenario B.

**This case's main workflow — every split from here through Lesson 8 — answers scenario A: does the model work on future orders from customers already in the training data?** That's consistent with Meridian Outlet's actual ask ("which orders are risky," not "which new customers are risky"), and it's what the plain `split_orders` already does, correctly, for that question.

So step 6 asks the scenario A/B question a different way: `split_orders_by_customer` (scenario B) is compared against the demonstration row-level split from step 2 (scenario A) — both applied to `train_df`, each producing a `fit`/`val` pair, the same shape of split Lesson 6 will use for real. **`val_df` here is a rehearsal copy of `test_df`, not `test_df` itself** — it's for trying things out (comparing splits, checking a threshold) before anything is locked in; `test_df` is for confirming a decision that's already made. Validation numbers are allowed to influence what you decide next (which split to prefer, which threshold to pick in Lesson 6); test numbers, once you look at them, are the final word — there's nothing "next" left to decide.

One concrete illustration: customer `CUST-0231` — call her Anna — has 5 orders in `train_df` (she placed 7 in total; the other 2 are wherever the main split in step 1 put them, which we don't check). Under the row-level `fit`/`val` split from step 2, 2 of her 5 land in `fit_df` and 3 in `val_df`: the model isn't meeting a stranger in `val_df`, it's being checked on more orders from someone it already partly knows. Under the group-level split, all 5 of Anna's orders land on the same side; there is no "Anna, mostly known."

| | Row split (main, scenario A) | Group split (scenario B) |
|---|---:|---:|
| `fit` rows / customers | 448 / 234 | 451 / 198 |
| `val` rows / customers | 112 / 91 | 109 / 50 |
| Customers in both `fit` and `val` | 77 | 0 |
| `val` confusion matrix @ 0.5 threshold | `[[96, 0], [16, 0]]` | `[[93, 0], [16, 0]]` |
| `val` ROC-AUC (area under the ROC curve — a threshold-free way to compare ranking quality; 0.5 is random, 1.0 is perfect) | 0.553 | 0.606 |

The two splits' results are *close*, not dramatically different, even though the group split's AUC is a bit higher here — that's not proof either split is wrong. Three reasons this comparison isn't as dramatic as it could be: these validation slices are small (112 and 109 rows, with only 16 returns each — plenty of room for a single split's numbers to wobble); the group split isn't stratified, so its own class balance drifts a little further from `train_df`'s than the row split's does; and `previous_returns_count`/`account_age_days` are fixed attributes assigned to each customer independently of their orders (check `data/generate.py` — they're drawn before any order exists), not a running tally built from the customer's own order history. If a feature were instead something like "this customer's return rate computed from their past orders so far," the row-split-vs-group-split gap would matter far more, because a row split could then let a customer's own *future* orders quietly inform a feature describing their *past*.

## Check your work

From this lesson's folder, run:

```bash
uv run pytest
```

In the "Your notes" cell, write: given the probability range you saw — is this model actually useless, or is 0.5 simply the wrong threshold for Meridian Outlet's problem? The same cell also asks why the row-split and group-split numbers came out close rather than dramatically different — answer that too. And: even in-sample, the model assigned as much as ~40% probability to some orders, yet its confusion matrix at threshold 0.5 looks almost identical to Lesson 4's baseline. If Meridian Outlet's real priority is catching returns, what happens to the confusion matrix after lowering the decision threshold from 0.5 to something like 0.3? You don't need to compute it yet — that's next lesson.
