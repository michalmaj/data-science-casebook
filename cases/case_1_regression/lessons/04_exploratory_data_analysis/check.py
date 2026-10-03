"""Self-check for Lesson 4. Run with `uv run pytest` in this directory.

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


def test_split_and_impute_match_lesson_3():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    assert len(train_df) == 394
    assert len(test_df) == 99
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    assert train_df.isna().sum().sum() == 0


def test_correlation_matrix_has_unit_diagonal():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    corr = lesson.correlation_matrix(train_df)
    assert corr.shape == (7, 7)
    assert all(abs(corr.loc[col, col] - 1.0) < 1e-9 for col in corr.columns)


def test_correlation_with_target_num_stops_is_the_strongest_numeric_signal():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    r = lesson.correlation_with_target(train_df, "num_stops")
    assert abs(r - 0.4830) < 1e-3


def test_correlation_with_target_actual_duration_is_deceptively_weak():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    r = lesson.correlation_with_target(train_df, "actual_duration_min")
    assert abs(r - (-0.0102)) < 1e-3


def test_mean_delay_by_weather_ranks_snow_worst_and_clear_best():
    df = lesson.load_shipments()
    train_df, test_df = lesson.split_shipments(df)
    train_df, test_df = lesson.impute_driver_experience(train_df, test_df)
    means = lesson.mean_delay_by_weather(train_df)
    assert list(means.index) == ["snow", "rain", "clear"]
    assert abs(means["snow"] - 33.6636) < 1e-3
    assert abs(means["clear"] - 9.5714) < 1e-3


def test_train_only_correlation_differs_from_whole_dataset_value():
    # Sanity guard: 0.4926 is the old (pre-split, whole-493-row) value for
    # num_stops. The train-only value asserted above (0.4830) is close but
    # measurably different — if a solution accidentally computes EDA on
    # the whole dataset instead of train_df, it will match 0.4926 instead
    # and the test above will fail. This test pins down the margin.
    df = lesson.load_shipments()
    whole_dataset_corr = df[lesson.NUMERIC_COLUMNS].corr().loc["num_stops", "delay_minutes"]
    assert abs(whole_dataset_corr - 0.4926) < 1e-3
    assert abs(whole_dataset_corr - 0.4830) > 5e-3
