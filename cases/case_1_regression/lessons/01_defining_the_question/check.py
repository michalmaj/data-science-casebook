"""Self-check for Lesson 1. Run with `uv run pytest` in this directory.

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


def test_load_shipments_has_expected_columns():
    df = lesson.load_shipments()
    expected_columns = {
        "shipment_id",
        "distance_km",
        "planned_duration_min",
        "actual_duration_min",
        "driver_experience_years",
        "num_stops",
        "weekday",
        "weather",
        "vehicle_age_years",
        "delay_minutes",
    }
    assert expected_columns.issubset(set(df.columns))


def test_target_column_name_is_delay_minutes():
    assert lesson.target_column_name() == "delay_minutes"


def test_target_column_has_no_missing_values():
    df = lesson.load_shipments()
    counts = lesson.missing_value_counts(df)
    assert counts["delay_minutes"] == 0


def test_missing_value_counts_flags_known_gaps():
    df = lesson.load_shipments()
    counts = lesson.missing_value_counts(df)
    assert counts["driver_experience_years"] == 8
    assert counts["weather"] == 7
