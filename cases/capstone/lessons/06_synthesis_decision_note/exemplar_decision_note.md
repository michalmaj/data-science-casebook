# Exemplar Decision Note — Capstone (regression path)

*This is a model answer for one capstone path (regression, Riverside Community Clinic), written after completing all 6 lessons. Don't read it before writing your own — the point of the exercise is to reach these conclusions yourself; this exists so you can compare your reasoning to a strong answer afterward, not so you can copy it. If you picked a different dataset (classification or clustering), this note shows the format and depth expected — not the specific content for your dataset.*

## 1. Business question

Can Riverside Community Clinic predict how long a patient will wait, using information available at check-in — how many patients are ahead of them, how many staff are on duty, the hour of day, and the patient's age — precisely enough to give patients a more honest wait estimate than a flat clinic-wide average?

## 2. Approach

I loaded the clinic dataset, split it 80/20 into train/test, then imputed the small number of missing `staff_on_duty` values using a median computed from the training set only (applied to both train and test). `department` also has some missing values, but I didn't use it as a feature, so it was never imputed. I compared a mean-baseline (always predict the training set's average wait) against a linear regression fit on `num_patients_ahead`, `staff_on_duty`, `hour_of_day`, and `patient_age`, predicting `wait_time_minutes`.

## 3. Results

| Predictor | MAE (min) |
|---|---:|
| Baseline (mean wait) | 18.57 |
| Linear model | 10.60 |

The model's test-set error (10.60 minutes) is close to its Lesson 4 training-set error, which is a good sign — it means the model generalizes to patients it never saw during fitting, not just the ones it was trained on.

## 4. Model choice and confidence

The fact that test-set MAE (10.60) and training-set MAE from Lesson 4 land in the same range — rather than the test error being dramatically worse — is what justifies trusting this model going forward, not just the raw MAE number in isolation. A model that looks great on training data but falls apart on the test set would be memorizing, not learning; this one isn't.

## 5. Interpretation

A ~10.6 minute average error means the clinic can now give patients a personalized estimate that's typically within about 10.6 minutes of the truth — a real improvement over the current flat baseline, which always tells every patient roughly 41.5 minutes and is off by about 18.6 minutes on average. It's precise enough to be useful for setting expectations, not precise enough to promise an exact time to any individual patient.

## 6. Limitations

- (Resolved) Earlier drafts of this analysis imputed missing `staff_on_duty` values using statistics from the full dataset, before the train/test split — a small amount of test-set information technically leaked into those fill values. This has been fixed: the median fill value is now computed from the training set only and applied to both train and test.
- The model only used one train/test split with one random seed; a different split could give a somewhat different MAE, and this analysis doesn't quantify how much that number might move.

## 7. Recommendation

Use the model to give patients a personalized wait estimate at check-in instead of the current flat average — it's a real, test-set-verified improvement (18.57 → 10.60 minutes MAE). Don't treat 10.60 minutes as an exact promise to any one patient; frame it as "usually within about 10 minutes of this estimate."

---

## Why this is a strong answer

This note earns "Exemplary" on **Modeling/evaluation correctness** because Section 4 explicitly checks train-vs-test consistency as the basis for trust, rather than reporting the test MAE as if a single number were self-justifying — and because the underlying pipeline fits imputation on the training set only, never letting test-set information influence preprocessing. It earns "Exemplary" on **Interpretation and limitations** by naming a genuine, concrete constraint (a single train/test split with one random seed) and being explicit that this analysis doesn't quantify how much the reported MAE might move under a different split — a specific, checkable claim rather than a vague disclaimer.
