"""Self-check for Lesson 6. Run with `uv run pytest` in this directory.

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


def test_train_residuals_sum_to_approximately_zero():
    df = lesson.load_clean_shipments()
    train_df, _ = lesson.split_shipments(df)
    model = lesson.fit_model(train_df)
    residuals = lesson.compute_residuals(model, train_df)
    assert abs(residuals.mean()) < 1e-6


def test_residuals_are_uncorrelated_with_every_in_model_feature():
    df = lesson.load_clean_shipments()
    train_df, _ = lesson.split_shipments(df)
    model = lesson.fit_model(train_df)
    residuals = lesson.compute_residuals(model, train_df)
    for column in lesson.FEATURE_COLUMNS:
        corr = lesson.residual_correlation_with_feature(train_df, residuals, column)
        assert abs(corr) < 1e-6


def test_mean_residual_by_weather_reveals_the_missing_predictor():
    df = lesson.load_clean_shipments()
    train_df, _ = lesson.split_shipments(df)
    model = lesson.fit_model(train_df)
    residuals = lesson.compute_residuals(model, train_df)
    means = lesson.mean_residual_by_weather(train_df, residuals)

    assert list(means.index) == ["snow", "rain", "clear"]
    assert abs(means["snow"] - 19.324425) < 1e-3
    assert abs(means["rain"] - 4.136380) < 1e-3
    assert abs(means["clear"] - (-3.656758)) < 1e-3
