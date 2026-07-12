# Exemplar Decision Note — Case 1 (TransLine)

*This is a model answer, written after completing all of Case 1. Don't read it before writing your own — the point of the exercise is to reach these conclusions yourself; this exists so you can compare your reasoning to a strong answer afterward, not so you can copy it.*

## 1. Business question

Can we predict how many minutes a TransLine shipment will be delayed, using information available before a driver leaves — distance, number of stops, driver experience, and vehicle age — well enough to beat simply assuming "the average delay," so dispatch can flag high-risk shipments before they happen?

## 2. Approach

I used TransLine's cleaned shipment records (`distance_km`, `num_stops`, `driver_experience_years`, `vehicle_age_years` as features, `delay_minutes` as target), split 80/20 into train/test with a fixed random seed. I compared two baselines — always predicting 0 minutes of delay, and always predicting the training set's mean delay — against a linear regression fit on the four features. All three were scored on the same held-out test set.

## 3. Results

| Predictor | MAE (min) | RMSE (min) |
|---|---:|---:|
| Zero baseline | 16.80 | 20.50 |
| Mean baseline | 12.08 | 15.19 |
| Linear model | 10.21 | 12.80 |

The linear model beats the mean baseline by about 1.9 minutes of MAE — a real improvement, but not a dramatic one.

## 4. What the model misses

`weather` is not in the feature set, even though earlier exploration showed it has a real relationship with delay. The model was deliberately built without it — production dispatch systems in this exercise only have the four features above at prediction time — which means the model's residuals will systematically be larger on bad-weather days. That's not a bug in the model; it's a known, named gap between what the model can see and what actually drives delay.

## 5. What's actually actionable

A 10.21-minute average error is small enough to be useful for triage (flag shipments predicted >20 minutes late for a dispatcher's attention) but too large to promise customers a tight delivery window. The features that matter most for the model's predictions are `distance_km` and `num_stops` — both already known before a shipment leaves the depot, which is exactly when TransLine needs the estimate.

## 6. Limitations

- The model has no access to weather, which we know affects delay — so its errors will be worse on bad-weather days specifically, not just larger on average.
- The linear model assumes each feature's effect is additive and constant; if, say, extra stops matter more for already-long routes, this model won't capture that interaction.

## 7. Recommendation

Deploy the linear model as a triage flag, not a customer-facing delivery-time promise: any shipment predicted to run more than 20 minutes late gets a dispatcher's attention before it happens. Do not use it to quote delivery windows to customers until weather is added as a feature — until then, treat its estimate as a floor on likely delay, not a ceiling.

---

## Why this is a strong answer

This note earns "Exemplary" on **Modeling/evaluation correctness** because every number in the Results table comes from the same held-out test set, and the two baselines make the model's actual contribution ("1.9 minutes better than just guessing the average") legible rather than hidden behind a single impressive-sounding metric. It earns "Exemplary" on **Interpretation and limitations** because Section 4 doesn't just say "the model has limitations" — it names weather specifically, explains *why* it was excluded (feature availability at prediction time, not an oversight), and predicts *how* that gap will show up in errors (worse specifically on bad-weather days). Section 7 earns "Exemplary" on **Communication** because the recommendation is a concrete usage boundary ("triage flag, not a customer promise") rather than a restatement of the MAE number.
