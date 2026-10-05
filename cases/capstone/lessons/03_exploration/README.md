# Lesson 3 — Exploration

**Estimated time:** 45-55 min

## Learning outcomes

- You'll be able to explore numeric feature relationships in a dataset you chose yourself, without an earlier lesson pointing you at the relevant columns.
- You'll be able to form an initial, evidence-based view on which of your dataset's features are likely to matter for your own Lesson 1 question.
- You'll be able to explain why, for a dataset with a target, exploring a feature's relationship to that target only tells you something honest if it's computed on `train_df` alone.

## Mentor's note

"Before you fit anything, look at what's actually in the data. Some features will turn out to matter a lot for your question, some barely at all — and you want to know which is which before you build a model around the wrong ones."

## Lesson goal

Explore how the numeric features in your chosen dataset relate to each other, and start forming a view on which ones are likely to matter for your Lesson 1 question.

## Today's analytical question

Which of your dataset's numeric features look most related to each other — and to whatever you're trying to predict or understand?

## What you're given

- The same dataset you picked in Lesson 1
- `task.py` — four functions: `load_dataset`, `split_dataset`, `impute_missing` (for the two predictive paths — explore relationships on `train_df` only, the same split and fill recipe as Lesson 2), `load_clean_dataset` (Lessons 1-2 combined, for the segmentation path, which has no split to protect), and `numeric_correlations`, used by both
- `lesson.ipynb` — the notebook where you'll explore

If your path has a target you're trying to predict, this lesson's exploration — including any correlation between a feature and that target — only ever looks at `train_df`. Seeing how a feature relates to the target using rows that will later become your test set is exactly the kind of preview that made Case 1's original EDA step leak information before PR #55 fixed it; this lesson doesn't repeat that mistake.

## Working in the notebook

- If you picked `clinic_wait_times` or `lendwell_loan_default`: split first (same recipe as Lesson 2), impute `train_df`/`test_df`, then compute the correlation matrix on `train_df` only.
- If you picked `retail_store_segments`: load and clean the whole dataset in one step, exactly as before — there's no split to protect for a segmentation problem.
- Sort the relationships to see which stand out, high or low.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. These checks verify the correlation numbers themselves, and that the two predictive paths compute them from `train_df` only — they can't tell you which relationships actually matter for your specific question.

## Homework

Two to three sentences: based on what you found, which feature are you most confident will help answer your Lesson 1 question, and which are you tempted to drop? What could go wrong with that judgment?

## Reflection

The mentor asks: a strong correlation between two features doesn't tell you which one (if either) is the one actually worth building your analysis around. What would you need to check before deciding that?
