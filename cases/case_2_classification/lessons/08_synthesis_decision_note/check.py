"""Self-check for Lesson 8. Run with `uv run pytest` in this directory.

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


def test_final_scorecard_has_expected_shape_and_index():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    scorecard = lesson.final_scorecard(train_df, test_df, model)

    assert list(scorecard.index) == [
        "majority_baseline",
        "default_threshold_0.5",
        "chosen_threshold_0.2",
    ]
    assert list(scorecard.columns) == ["precision", "recall", "f1"]


def test_final_scorecard_matches_expected_numbers():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    scorecard = lesson.final_scorecard(train_df, test_df, model)

    assert scorecard.loc["majority_baseline", "precision"] == 0.0
    assert scorecard.loc["majority_baseline", "recall"] == 0.0
    assert scorecard.loc["majority_baseline", "f1"] == 0.0

    assert scorecard.loc["default_threshold_0.5", "precision"] == 0.0
    assert scorecard.loc["default_threshold_0.5", "recall"] == 0.0
    assert scorecard.loc["default_threshold_0.5", "f1"] == 0.0

    assert abs(scorecard.loc["chosen_threshold_0.2", "precision"] - 0.24444444444444444) < 1e-9
    assert abs(scorecard.loc["chosen_threshold_0.2", "recall"] - 0.55) < 1e-9
    assert abs(scorecard.loc["chosen_threshold_0.2", "f1"] - 0.3384615384615385) < 1e-9


def test_final_scorecard_shows_the_chosen_threshold_helps():
    df = lesson.load_and_merge_orders()
    train_df, test_df = lesson.split_orders(df)
    model = lesson.fit_classifier(train_df)
    scorecard = lesson.final_scorecard(train_df, test_df, model)

    assert (
        scorecard.loc["chosen_threshold_0.2", "recall"]
        > scorecard.loc["majority_baseline", "recall"]
    )
    assert (
        scorecard.loc["chosen_threshold_0.2", "recall"]
        > scorecard.loc["default_threshold_0.5", "recall"]
    )
    assert scorecard.loc["chosen_threshold_0.2", "f1"] > scorecard.loc["majority_baseline", "f1"]
    assert (
        scorecard.loc["chosen_threshold_0.2", "f1"] > scorecard.loc["default_threshold_0.5", "f1"]
    )
