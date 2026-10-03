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


def test_load_shipments_returns_493_rows():
    df = lesson.load_shipments()
    assert len(df) == 493


def test_split_shipments_produces_expected_sizes():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    assert len(train_df) == 394
    assert len(test_df) == 99


def test_train_residuals_sum_to_approximately_zero():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    model = lesson.fit_model(train_df)
    residuals = lesson.compute_residuals(model, train_df)
    assert abs(residuals.mean()) < 1e-6


def test_residuals_are_uncorrelated_with_every_in_model_feature():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    model = lesson.fit_model(train_df)
    residuals = lesson.compute_residuals(model, train_df)
    for column in lesson.FEATURE_COLUMNS:
        corr = lesson.residual_correlation_with_feature(train_df, residuals, column)
        assert abs(corr) < 1e-6


def test_residual_diagnostics_in_this_lesson_use_train_not_test():
    # OLS guarantees residuals average ~0 (and are uncorrelated with every
    # in-model feature) only on the data the model was fit on. If this
    # lesson's residual diagnostics were ever pointed at test_df instead of
    # train_df — reopening the held-out set for a diagnosis that could feed
    # back into a modeling decision — that guarantee would no longer hold
    # and this test would catch it: the test-set mean residual is a real,
    # non-negligible number, not a numerical-precision artifact near zero.
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    model = lesson.fit_model(train_df)

    train_residuals = lesson.compute_residuals(model, train_df)
    test_residuals = lesson.compute_residuals(model, test_df)

    assert abs(train_residuals.mean()) < 1e-6
    assert abs(test_residuals.mean()) > 0.05


def test_mean_residual_by_weather_reveals_the_missing_predictor():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    model = lesson.fit_model(train_df)
    residuals = lesson.compute_residuals(model, train_df)
    means = lesson.mean_residual_by_weather(train_df, residuals)

    assert list(means.index) == ["snow", "rain", "clear"]
    assert abs(means["snow"] - 19.328648) < 1e-3
    assert abs(means["rain"] - 4.134309) < 1e-3
    assert abs(means["clear"] - (-3.656140)) < 1e-3
