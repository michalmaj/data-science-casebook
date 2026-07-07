"""Self-check for Lesson 3. Run with `uv run pytest` in this directory.

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


def test_load_clean_shipments_returns_493_rows_no_missing():
    df = lesson.load_clean_shipments()
    assert len(df) == 493
    assert df.isna().sum().sum() == 0


def test_correlation_matrix_has_unit_diagonal():
    df = lesson.load_clean_shipments()
    corr = lesson.correlation_matrix(df)
    assert corr.shape == (7, 7)
    assert all(abs(corr.loc[col, col] - 1.0) < 1e-9 for col in corr.columns)


def test_correlation_with_target_num_stops_is_the_strongest_numeric_signal():
    df = lesson.load_clean_shipments()
    r = lesson.correlation_with_target(df, "num_stops")
    assert abs(r - 0.4926) < 1e-3


def test_correlation_with_target_actual_duration_is_deceptively_weak():
    df = lesson.load_clean_shipments()
    r = lesson.correlation_with_target(df, "actual_duration_min")
    assert abs(r - (-0.0015)) < 1e-3


def test_mean_delay_by_weather_ranks_snow_worst_and_clear_best():
    df = lesson.load_clean_shipments()
    means = lesson.mean_delay_by_weather(df)
    assert list(means.index) == ["snow", "rain", "clear"]
    assert abs(means["snow"] - 34.752) < 1e-2
    assert abs(means["clear"] - 9.5873) < 1e-3
