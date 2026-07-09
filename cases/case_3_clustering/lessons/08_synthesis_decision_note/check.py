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


def test_load_scaled_features_shape_and_columns():
    df = lesson.load_scaled_features()
    assert df.shape == (300, 5)
    assert list(df.columns) == ["subscriber_id", *lesson.FEATURE_COLUMNS]


def test_final_segment_table_shape_and_columns():
    df = lesson.load_scaled_features()
    table = lesson.final_segment_table(df)
    assert table.shape == (2, 6)
    assert list(table.columns) == [*lesson.FEATURE_COLUMNS, "size", "share"]
    assert list(table.index) == [0, 1]


def test_final_segment_table_matches_known_values():
    df = lesson.load_scaled_features()
    table = lesson.final_segment_table(df)
    assert abs(table.loc[0, "session_count"] - (-0.539042329134949)) < 1e-6
    assert abs(table.loc[1, "session_count"] - 1.4574107417352327) < 1e-6
    assert table.loc[0, "size"] == 219
    assert table.loc[1, "size"] == 81
    assert abs(table.loc[0, "share"] - 0.73) < 1e-9
    assert abs(table.loc[1, "share"] - 0.27) < 1e-9


def test_final_segment_table_shares_sum_to_one():
    df = lesson.load_scaled_features()
    table = lesson.final_segment_table(df)
    assert abs(table["share"].sum() - 1.0) < 1e-9


def test_final_segment_table_shows_asymmetric_engagement_segments():
    df = lesson.load_scaled_features()
    table = lesson.final_segment_table(df)
    assert table.loc[1, "share"] < table.loc[0, "share"]
    viewing_columns = ["session_count", "total_minutes_watched", "avg_minutes_per_session"]
    for column in viewing_columns:
        assert table.loc[1, column] > 1.0
        assert table.loc[0, column] < -0.4
