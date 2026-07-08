"""Self-check for Lesson 6. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

from sklearn.linear_model import LogisticRegression

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
    assert train_df["is_returned"].sum() == 78
    assert test_df["is_returned"].sum() == 20


def test_fit_classifier_returns_fitted_logistic_regression():
    df = lesson.load_and_merge_orders()
    train_df, _ = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    assert isinstance(model, LogisticRegression)
    assert model.n_features_in_ == 3


def test_predict_at_threshold_predicts_more_positives_as_threshold_drops():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)

    predicted_05 = lesson.predict_at_threshold(model, test_df, 0.5)
    predicted_03 = lesson.predict_at_threshold(model, test_df, 0.3)
    predicted_02 = lesson.predict_at_threshold(model, test_df, 0.2)

    assert predicted_05.sum() == 1
    assert predicted_03.sum() == 17
    assert predicted_02.sum() == 45
    assert predicted_02.sum() > predicted_03.sum() > predicted_05.sum()


def test_classification_metrics_show_the_precision_recall_tradeoff():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    actual = test_df["is_returned"]

    predicted_05 = lesson.predict_at_threshold(model, test_df, 0.5)
    metrics_05 = lesson.classification_metrics(actual, predicted_05)
    assert metrics_05["recall"] == 0.0
    assert metrics_05["f1"] == 0.0

    predicted_02 = lesson.predict_at_threshold(model, test_df, 0.2)
    metrics_02 = lesson.classification_metrics(actual, predicted_02)
    assert abs(metrics_02["precision"] - 0.24444444444444444) < 1e-9
    assert abs(metrics_02["recall"] - 0.55) < 1e-9
    assert abs(metrics_02["f1"] - 0.3384615384615385) < 1e-9
