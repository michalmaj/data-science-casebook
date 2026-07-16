# Lesson 7 (Optional) — Packaging Your Preprocessing as a Pipeline

**Estimated time:** 40-55 min

## Learning outcomes

- You'll be able to replace a manual impute-then-scale-then-fit sequence with one fitted `sklearn.pipeline.Pipeline`.
- You'll be able to use `ColumnTransformer` to bring in a categorical column your dataset always had but never used as a feature, and check whether it actually helps.

## Mentor's note

"This one's not graded — think of it as a bonus round. Six lessons ago you
picked a dataset with a column or two the earlier lessons never let you use.
Let's actually use one, and let's package the whole preprocessing step the
way you'd hand it to someone else, instead of three functions they'd have to
call in exactly the right order."

## Lesson goal

Replace Lessons 4-6's manual `impute_missing` -> `scale_features` -> `fit_*`
sequence with one fitted `sklearn.pipeline.Pipeline`, and use
`sklearn.compose.ColumnTransformer` to bring in a categorical column your
dataset has always had but never used as a feature.

## Today's analytical question

Does packaging your preprocessing into one object change your results — and
does actually using the categorical column your dataset offers help, hurt,
or do nothing?

## What you're given

- The same dataset you picked in Lesson 1
- `task.py` — two functions reproduced from Lessons 4-6 (`load_dataset`,
  `split_dataset`), plus seven new ones: `build_preprocessor` (the shared
  `ColumnTransformer` builder), one `build_and_fit_*_pipeline` function per
  problem type, and one `evaluate_pipeline_*` function per problem type (use
  only the ones that match your dataset)
- `lesson.ipynb` — the notebook where you'll build and evaluate your pipeline

## Working in the notebook

- Set `DATASET_NAME` to match what you picked in Lesson 1.
- Run the dispatch cell — it loads, splits (except for clustering, which
  never splits), builds a `Pipeline` combining a `ColumnTransformer` and your
  model, fits it, and evaluates it, all in one place.
- Compare the result to what you got in Lesson 6 — see the note in the
  notebook about why more than one thing might have changed at once.

## Self-check

From this lesson's folder, run:

```bash
uv run pytest
```

All tests should pass once `task.py` is complete. Like Lessons 4-6, these
checks verify exact values for the suggested feature sets — they can't tell
you whether adding your dataset's categorical column was a good analytical
choice, only that your `Pipeline`/`ColumnTransformer` code behaves correctly.

## Homework

None — this lesson is optional and ungraded. If you want the exercise: two
to three sentences on whether the categorical column you added actually
helped your model, in the "Your notes" cell.

## Reflection

The mentor asks: `ColumnTransformer` let you treat numeric and categorical
columns differently in one object. What would go wrong if you tried to fit a
`StandardScaler` directly on a categorical column instead of routing it to
`OneHotEncoder`?
