"""Self-check for Lesson 1. Run with `uv run pytest` in this directory.

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


def test_list_tables_returns_both_tables():
    assert lesson.list_tables() == ["sessions", "subscribers"]


def test_load_subscriber_features_shape_and_columns():
    df = lesson.load_subscriber_features()
    assert df.shape == (300, 7)
    assert list(df.columns) == [
        "subscriber_id",
        "plan_tier",
        "country",
        "session_count",
        "total_minutes_watched",
        "avg_minutes_per_session",
        "tenure_days",
    ]


def test_load_subscriber_features_handles_subscribers_with_no_sessions():
    df = lesson.load_subscriber_features()
    no_sessions = df[df["session_count"] == 0]
    assert len(no_sessions) == 2
    assert (no_sessions["total_minutes_watched"] == 0).all()
    assert (no_sessions["avg_minutes_per_session"] == 0.0).all()
    assert no_sessions["avg_minutes_per_session"].isna().sum() == 0


def test_load_subscriber_features_matches_a_known_row():
    df = lesson.load_subscriber_features()
    row = df[df["subscriber_id"] == "SUB-0001"].iloc[0]
    assert row["plan_tier"] == "standard"
    assert row["country"] == "Germany"
    assert row["session_count"] == 14
    assert row["total_minutes_watched"] == 641
    assert abs(row["avg_minutes_per_session"] - 45.785714285714285) < 1e-9
    assert row["tenure_days"] == 278
