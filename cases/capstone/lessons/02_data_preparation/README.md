# Lesson 2 — Data Preparation

**Estimated time:** 45-55 min

## Learning outcomes

- You'll be able to generalize a cleaning strategy that works no matter which columns in your own dataset happen to have gaps.
- You'll be able to defend a specific imputation choice as appropriate for your data, instead of applying one mechanically because it worked in an earlier case.
- You'll be able to say why, for a dataset with a target you're trying to predict, the train/test split has to happen before any fill value is computed — not after.

## Mentor's note

"Whatever you found missing in Lesson 1, don't just paper over it. Decide, deliberately, what filling those gaps assumes about the data you don't have — and be ready to defend that choice."

## Lesson goal

Assess data quality and clean the dataset you picked in Lesson 1, using a strategy that works regardless of which columns happen to have gaps.

## Today's analytical question

Which columns in your dataset have missing values, and is filling them with the median/mode actually a defensible choice here?

## What you're given

- The same dataset you picked in Lesson 1
- `task.py` — five functions: `load_dataset` and `missing_value_counts` (reproduced from Lesson 1), `clean_dataset` (whole-dataset cleaning — the right choice for the clustering path, which has no train/test split to protect), plus `split_dataset` and `impute_missing` for the other two paths. If your dataset has a target you're trying to predict, your train/test split happens *here* — before any statistic (a median, a mode) is computed from data that will later include your test set.
- `lesson.ipynb` — the notebook where you'll check quality and clean

## Working in the notebook

- Load your dataset and check missing values before cleaning — that part is the same regardless of dataset.
- If you picked `clinic_wait_times` or `lendwell_loan_default`: split into `train_df`/`test_df` first, then impute using only `train_df`'s statistics. Confirm nothing is missing in either frame afterward.
- If you picked `retail_store_segments`: there's no split to protect here — run `clean_dataset` on the whole dataset, exactly as before.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. These checks verify `clean_dataset`, `split_dataset`, and `impute_missing` do what their contracts promise (gaps actually filled, train/test actually disjoint, fill values actually computed from train only) — they can't judge whether median/mode filling, or your train/test split itself, was the *right* call for your specific dataset.

## Homework

Two to three sentences: pick one column that had missing values in your dataset. What real-world reason might explain why that value was missing — and does median/mode filling handle that reason well or badly?

## Reflection

The mentor asks: `clean_dataset`/`impute_missing` treat every missing value in a column the same way (median or mode), regardless of dataset. What's the risk of applying one generic cleaning strategy across very different kinds of data — and is there a column in your dataset where you'd justify a different approach instead?
