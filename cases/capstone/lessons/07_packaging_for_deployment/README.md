# Lesson 7 (Optional) — Packaging Your Preprocessing as a Pipeline

**Estimated time:** 40-55 min

## The decision to make

This one's not graded — think of it as a bonus round. Six lessons ago a dataset was picked with a column or two the earlier lessons never allowed using. Let's actually use one, and package the whole preprocessing step the way it would get handed to someone else, instead of three functions that need calling in exactly the right order.

## What you have to work with

- `task.py` — two functions reproduced from Lessons 4-6 (`load_dataset`, `split_dataset`), plus seven new ones: `build_preprocessor` (the shared `ColumnTransformer` builder), one `build_and_fit_*_pipeline` function per problem type, and one `evaluate_pipeline_*` function per problem type.
- In the notebook: set `DATASET_NAME`, run the dispatch cell — it loads, splits, builds a `Pipeline` combining a `ColumnTransformer` and the model, fits it, and evaluates it. Compare the result to Lesson 6 — see the note in the notebook about why more than one thing might have changed at once.

## Justify it

From this lesson's folder, run:

```bash
uv run pytest
```

Like Lessons 4-6, these checks verify exact values for the suggested feature sets — they can't tell you whether adding the categorical column was a good analytical choice, only that the `Pipeline`/`ColumnTransformer` code behaves correctly.

None — this lesson is optional and ungraded. For the exercise: two to three sentences on whether the added categorical column actually helped the model, in the "Your notes" cell. And: `ColumnTransformer` allowed treating numeric and categorical columns differently in one object. What would go wrong trying to fit a `StandardScaler` directly on a categorical column instead of routing it to `OneHotEncoder`?
