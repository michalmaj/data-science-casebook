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
    assert df.shape == (300, 9)
    assert list(df.columns) == [
        "subscriber_id",
        *lesson.FEATURE_COLUMNS,
        *lesson.SCALED_FEATURE_COLUMNS,
    ]


def test_final_segment_table_shape_and_columns():
    df = lesson.load_scaled_features()
    table = lesson.final_segment_table(df)
    assert table.shape == (2, 6)
    assert list(table.columns) == [*lesson.FEATURE_COLUMNS, "size", "share"]
    assert list(table.index) == [0, 1]


def test_final_segment_table_matches_known_values():
    df = lesson.load_scaled_features()
    table = lesson.final_segment_table(df)
    # Sort by session_count (itself part of what's being verified) so size
    # and share are checked in the same, now label-independent row order —
    # this keeps the correspondence a cluster actually has between columns,
    # unlike sorting each column independently.
    by_session_count = table.sort_values("session_count").reset_index(drop=True)
    assert abs(by_session_count.loc[0, "session_count"] - 13.429223744292237) < 1e-6
    assert abs(by_session_count.loc[1, "session_count"] - 46.23456790123457) < 1e-6
    assert by_session_count.loc[0, "size"] == 219
    assert by_session_count.loc[1, "size"] == 81
    assert abs(by_session_count.loc[0, "share"] - 0.73) < 1e-9
    assert abs(by_session_count.loc[1, "share"] - 0.27) < 1e-9


def test_final_segment_table_shares_sum_to_one():
    df = lesson.load_scaled_features()
    table = lesson.final_segment_table(df)
    assert abs(table["share"].sum() - 1.0) < 1e-9


def test_final_segment_table_shows_asymmetric_engagement_segments():
    df = lesson.load_scaled_features()
    table = lesson.final_segment_table(df)
    low_engagement_label = table["session_count"].idxmin()
    high_engagement_label = table["session_count"].idxmax()
    assert table.loc[high_engagement_label, "share"] < table.loc[low_engagement_label, "share"]
    viewing_columns = ["session_count", "total_minutes_watched", "avg_minutes_per_session"]
    for column in viewing_columns:
        high_value = table.loc[high_engagement_label, column]
        low_value = table.loc[low_engagement_label, column]
        assert high_value > 2 * low_value
