"""Self-check for Lesson 2. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

import pandas as pd

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


def test_load_shipments_returns_expected_row_count():
    df = lesson.load_shipments()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 500


def test_rows_with_missing_data_finds_all_affected_rows():
    df = lesson.load_shipments()
    missing = lesson.rows_with_missing_data(df)
    assert len(missing) == 15


def test_drop_missing_weather_removes_exactly_seven_rows():
    df = lesson.load_shipments()
    result = lesson.drop_missing_weather(df)
    assert len(result) == 493
    assert result["weather"].isna().sum() == 0


def test_impute_missing_experience_fills_with_median_and_keeps_row_count():
    df = lesson.load_shipments()
    without_missing_weather = df.dropna(subset=["weather"])
    result = lesson.impute_missing_experience(without_missing_weather)
    assert len(result) == 493
    assert result["driver_experience_years"].isna().sum() == 0
    assert result["driver_experience_years"].median() == 13.0


def test_clean_shipments_leaves_no_missing_values():
    df = lesson.load_shipments()
    cleaned = lesson.clean_shipments(df)
    assert len(cleaned) == 493
    assert cleaned.isna().sum().sum() == 0
