# Exemplar Decision Note — Case 2 (Meridian Outlet)

*This is a model answer, written after completing all of Case 2. Don't read it before writing your own — the point of the exercise is to reach these conclusions yourself; this exists so you can compare your reasoning to a strong answer afterward, not so you can copy it.*

## 1. Business question

Can we identify, before or shortly after an order ships, which orders from Meridian Outlet's online store are likely to be returned — precisely enough that flagging high-risk orders for manual review catches meaningfully more returns than reviewing at random, without flooding the ops team with false alarms?

## 2. Approach

I loaded and merged Meridian's Orders and Customers sheets (`discount_percent`, `previous_returns_count`, `account_age_days` as features, `is_returned` as target), split 80/20 stratified by the target to preserve the ~14% return rate in both sets, and fit a logistic regression on the training set. I compared a majority-class baseline (always predict "not returned") against the model at three thresholds — 0.5 (default), 0.3, and 0.2 — compared on a held-out validation split, then confirmed once on the test set at the chosen threshold.

## 3. Results

| Predictor | Precision | Recall | F1 |
|---|---:|---:|---:|
| Majority baseline | 0.000 | 0.000 | 0.000 |
| Model @ 0.5 threshold | 0.000 | 0.000 | 0.000 |
| Model @ 0.2 threshold | 0.244 | 0.550 | 0.338 |

At the default 0.5 threshold the model flags only 1 of the 140 test orders — effectively never predicting "returned," functionally identical to the majority baseline. Lowering the threshold to 0.2 is what actually makes the model useful: it catches 55% of real returns, at the cost of about 3 out of 4 flagged orders turning out fine on inspection.

## 4. Threshold and metric choice

Recall matters more than precision here: a missed return costs Meridian Outlet a full refund cycle, while a false alarm just costs a few minutes of a reviewer's time checking an order that turns out fine. That's why 0.2 was chosen over 0.5 or 0.3 — it's the threshold in the set we tried that pushes recall meaningfully higher without precision collapsing to near zero.

## 5. Communicating risk

"55% recall at 24% precision" means: of every 100 orders truly headed for a return, this system catches about 55 of them for review — and for every 4 orders it flags, only 1 will actually come back. That's a real filter, not a coin flip (the majority baseline catches 0), but it is not a confident individual-order risk score — treat a flag as "worth a second look," not "this order will be returned."

## 6. Limitations

- (Resolved as of Lesson 6's validation-split fix — kept here as a reminder of what to watch for.) Earlier drafts of this lesson chose the 0.2 threshold by comparing precision/recall directly on the test set, which would have reused it for a tuning decision. Lesson 6 now compares thresholds on a held-out validation split instead, and touches the test set exactly once, for the final number reported above — so this limitation no longer applies to this analysis, but it's exactly the mistake to watch for in your own work.
- With only 98 returned orders in the full dataset (and 20 in the test set), the precision/recall estimates above have real sampling noise — a few orders going the other way would move these numbers non-trivially.

## 7. Recommendation

Deploy the model at the 0.2 threshold as a manual-review flag, not an automatic-decline system — flag the ~32% of orders it selects for review before or shortly after shipping. These numbers already reflect Lesson 6's validation-based threshold selection and a single, genuine test-set check, so they're safe to use for a resourcing decision (e.g. "we need N reviewers") as-is.

---

## Why this is a strong answer

This note earns "Exemplary" on **Modeling/evaluation correctness** by comparing thresholds on a held-out validation split and touching the test set exactly once, for the final number — exactly the discipline the rubric's Exemplary level describes, rather than reusing the test set for a tuning decision. It earns "Exemplary" on **Communication** in Section 5 by translating "55% recall, 24% precision" into a concrete "1 in 4 flagged orders is real" statement a non-technical stakeholder can act on.
