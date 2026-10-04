"""Self-check for Lesson 5. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


def test_load_and_merge_orders_returns_700_rows():
    df = lesson.load_and_merge_orders()
    assert df.shape == (700, 9)


def test_split_orders_produces_expected_sizes_and_preserves_balance():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    assert len(train_df) == 560
    assert len(test_df) == 140
    assert len(train_df) + len(test_df) == len(df)
    assert train_df["is_returned"].sum() == 78
    assert test_df["is_returned"].sum() == 20


def test_split_orders_by_customer_has_no_customer_overlap_within_train():
    # The row-vs-group comparison in this lesson is a validation-level
    # experiment: it splits train_df further, it does not touch test_df.
    df = lesson.load_and_merge_orders()
    train_df, _test_df = lesson.split_orders(df)
    fit_df, val_df = lesson.split_orders_by_customer(train_df)
    assert set(fit_df["customer_id"]).isdisjoint(set(val_df["customer_id"]))


def test_split_orders_by_customer_produces_expected_sizes_within_train():
    df = lesson.load_and_merge_orders()
    train_df, _test_df = lesson.split_orders(df)
    fit_df, val_df = lesson.split_orders_by_customer(train_df)
    assert len(fit_df) == 451
    assert len(val_df) == 109
    assert len(fit_df) + len(val_df) == len(train_df)
    assert fit_df["customer_id"].nunique() == 198
    assert val_df["customer_id"].nunique() == 50


def test_split_orders_row_level_does_not_guarantee_disjoint_customers_within_train():
    # Contrast case: the row-level split this case uses as its main workflow
    # does NOT give disjoint customers — that's expected and fine for the
    # "future orders from known customers" scenario this case teaches, but
    # a test should say so explicitly rather than leaving it to be
    # discovered by accident. Still a validation-level split of train_df,
    # not the final test_df.
    df = lesson.load_and_merge_orders()
    train_df, _test_df = lesson.split_orders(df)
    fit_df, val_df = lesson.split_orders(train_df)
    overlap = set(fit_df["customer_id"]) & set(val_df["customer_id"])
    assert not set(fit_df["customer_id"]).isdisjoint(set(val_df["customer_id"]))
    assert len(overlap) == 77


def test_validation_splits_never_touch_the_final_test_set():
    # The core methodological property this lesson must not violate: every
    # demonstration here — the customer-overlap check, the threshold-0.5
    # catch-rate check, and the row-vs-group comparison — reads only
    # train_df or a further split of train_df, never test_df's own rows.
    # This can't catch a notebook that reads test_df directly (pytest only
    # sees task.py/solution.py, not lesson.ipynb) — see the lesson's README
    # for why the notebook itself is written to never do that. What this
    # test CAN pin down is that splits built this way from train_df never
    # share a row with test_df — i.e. any demonstration following this
    # lesson's pattern (customer overlap included) cannot accidentally
    # read from, or be scored against, the final holdout.
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    row_fit_df, row_val_df = lesson.split_orders(train_df)
    grp_fit_df, grp_val_df = lesson.split_orders_by_customer(train_df)
    test_indices = set(test_df.index)
    for sub_df in (row_fit_df, row_val_df, grp_fit_df, grp_val_df):
        assert set(sub_df.index).isdisjoint(test_indices)


def test_fit_classifier_returns_fitted_logistic_regression():
    df = lesson.load_and_merge_orders()
    train_df, _ = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    assert isinstance(model, LogisticRegression)
    assert model.n_features_in_ == 3


def test_predict_return_in_sample_still_misses_every_return_at_default_threshold():
    # Deliberately in-sample (train -> train), not train -> test: this
    # lesson shows the threshold-0.5 problem WITHOUT opening the final test
    # set. If the model can't even catch a return on the data it was fit
    # on, that's a threshold problem, not something only visible out of
    # sample — and it makes the point without spending the holdout early.
    df = lesson.load_and_merge_orders()
    train_df, _test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    predicted = lesson.predict_return(model, train_df)
    actual = train_df["is_returned"]

    cm = confusion_matrix(actual, predicted, labels=[0, 1])
    assert cm.tolist() == [[482, 0], [78, 0]]

    acc = accuracy_score(actual, predicted)
    assert abs(acc - 0.8607142857142858) < 1e-9
