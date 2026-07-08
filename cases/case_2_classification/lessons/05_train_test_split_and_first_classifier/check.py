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


def test_fit_classifier_returns_fitted_logistic_regression():
    df = lesson.load_and_merge_orders()
    train_df, _ = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    assert isinstance(model, LogisticRegression)
    assert model.n_features_in_ == 3


def test_predict_return_still_misses_every_return_at_default_threshold():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    predicted = lesson.predict_return(model, test_df)
    actual = test_df["is_returned"]

    cm = confusion_matrix(actual, predicted, labels=[0, 1])
    assert cm.tolist() == [[119, 1], [20, 0]]

    acc = accuracy_score(actual, predicted)
    assert abs(acc - 0.85) < 1e-9
