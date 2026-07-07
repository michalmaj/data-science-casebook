"""Self-check for Lesson 8. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


def test_load_clean_shipments_returns_493_rows():
    df = lesson.load_clean_shipments()
    assert len(df) == 493


def test_split_shipments_produces_expected_sizes():
    df = lesson.load_clean_shipments()
    train_df, test_df = lesson.split_shipments(df)
    assert len(train_df) == 394
    assert len(test_df) == 99


def test_final_scorecard_has_expected_shape_and_index():
    df = lesson.load_clean_shipments()
    train_df, test_df = lesson.split_shipments(df)
    model = lesson.fit_model(train_df)
    scorecard = lesson.final_scorecard(train_df, test_df, model)

    assert list(scorecard.index) == ["zero_baseline", "mean_baseline", "linear_model"]
    assert list(scorecard.columns) == ["mae", "rmse"]


def test_final_scorecard_matches_expected_numbers():
    df = lesson.load_clean_shipments()
    train_df, test_df = lesson.split_shipments(df)
    model = lesson.fit_model(train_df)
    scorecard = lesson.final_scorecard(train_df, test_df, model)

    assert abs(scorecard.loc["zero_baseline", "mae"] - 16.803030) < 1e-3
    assert abs(scorecard.loc["zero_baseline", "rmse"] - 20.497186) < 1e-3
    assert abs(scorecard.loc["mean_baseline", "mae"] - 12.075106) < 1e-3
    assert abs(scorecard.loc["mean_baseline", "rmse"] - 15.186886) < 1e-3
    assert abs(scorecard.loc["linear_model", "mae"] - 10.209876) < 1e-3
    assert abs(scorecard.loc["linear_model", "rmse"] - 12.801750) < 1e-3


def test_final_scorecard_shows_monotonic_improvement():
    df = lesson.load_clean_shipments()
    train_df, test_df = lesson.split_shipments(df)
    model = lesson.fit_model(train_df)
    scorecard = lesson.final_scorecard(train_df, test_df, model)

    assert (
        scorecard.loc["zero_baseline", "mae"]
        > scorecard.loc["mean_baseline", "mae"]
        > scorecard.loc["linear_model", "mae"]
    )
    assert (
        scorecard.loc["zero_baseline", "rmse"]
        > scorecard.loc["mean_baseline", "rmse"]
        > scorecard.loc["linear_model", "rmse"]
    )
