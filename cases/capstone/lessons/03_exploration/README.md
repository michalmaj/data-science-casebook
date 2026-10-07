# Lesson 3 — Exploration

**Estimated time:** 45-55 min

## The decision to make

Before fitting anything, look at what's actually in the data. Explore the numeric feature relationships in the chosen dataset — with no earlier lesson pointing at the relevant columns — and form an initial, evidence-based view on which features are likely to matter for the Lesson 1 question.

## What you have to work with

- `task.py` — four functions: `load_dataset`, `split_dataset`, `impute_missing` (for the two predictive paths — explore relationships on `train_df` only, the same split and fill recipe as Lesson 2), `load_clean_dataset` (Lessons 1-2 combined, for the segmentation path, which has no split to protect), and `numeric_correlations`, used by both.
- In the notebook: for `clinic_wait_times` or `lendwell_loan_default` — split (same recipe as Lesson 2), impute, compute the correlation matrix on `train_df` only. For `retail_store_segments` — load and clean the whole dataset in one step. Sort the relationships to see which stand out, high or low.

## Before deciding

If the path has a target, the exploration — including any correlation between a feature and that target — only ever looks at `train_df`. Seeing how a feature relates to the target using rows that will later become the test set is exactly the kind of preview that made Case 1's original EDA step leak information before PR #55 fixed it.

## Justify it

From this lesson's folder, run:

```bash
uv run pytest
```

These checks verify the correlation numbers themselves, and that the two predictive paths compute them from `train_df` only — they can't tell you which relationships actually matter for the specific question at hand.

Two to three sentences: based on what you found, which feature is most convincing as a help toward the Lesson 1 question, and which is tempting to drop? What could go wrong with that judgment? And: a strong correlation between two features doesn't tell you which one (if either) is the one actually worth building your analysis around. What would be worth checking before deciding that?
