# Lesson 2 — Data Preparation

**Estimated time:** 45-55 min

## The decision to make

Whatever was missing in Lesson 1, don't paper over it mechanically. Decide deliberately what filling those gaps assumes about the data you don't have, and justify that choice — instead of applying median/mode because it worked in an earlier case.

## What you have to work with

- The same dataset picked in Lesson 1.
- `task.py` — five functions: `load_dataset` and `missing_value_counts` (reproduced from Lesson 1), `clean_dataset` (whole-dataset cleaning — the right choice for the clustering path, which has no train/test split to protect), plus `split_dataset` and `impute_missing` for the other two paths.
- In the notebook: load the dataset and check missing values before cleaning. If `clinic_wait_times` or `lendwell_loan_default` was picked: split into `train_df`/`test_df`, then impute using only `train_df`'s statistics. If `retail_store_segments` was picked: there's no split to protect here — run `clean_dataset` on the whole dataset.

## Before deciding

If the dataset has a target being predicted, the train/test split has to happen before any fill-value statistic is computed — not after. For a dataset with no target (clustering), this problem doesn't exist at all.

## Justify it

From this lesson's folder, run:

```bash
uv run pytest
```

These checks verify that `clean_dataset`, `split_dataset`, and `impute_missing` do what they promise — they can't judge whether median/mode filling, or the train/test split itself, was the *right* call for this particular dataset.

Two to three sentences: pick one column that had missing values. What real-world reason might explain that gap — and does median/mode filling handle that reason well or badly? And: `clean_dataset`/`impute_missing` treat every missing value in a column the same way, regardless of dataset. What's the risk of applying one generic cleaning strategy across very different kinds of data — and is there a column worth justifying a different approach for?
