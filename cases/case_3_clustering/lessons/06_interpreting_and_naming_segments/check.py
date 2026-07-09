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


def test_load_scaled_features_shape_and_columns():
    df = lesson.load_scaled_features()
    assert df.shape == (300, 5)
    assert list(df.columns) == ["subscriber_id", *lesson.FEATURE_COLUMNS]


def test_segment_profiles_shape_and_columns():
    df = lesson.load_scaled_features()
    profiles = lesson.segment_profiles(df)
    assert profiles.shape == (2, 5)
    assert list(profiles.columns) == [*lesson.FEATURE_COLUMNS, "size"]
    assert list(profiles.index) == [0, 1]


def test_segment_profiles_matches_known_values():
    df = lesson.load_scaled_features()
    profiles = lesson.segment_profiles(df)
    assert abs(profiles.loc[0, "session_count"] - (-0.539042329134949)) < 1e-6
    assert abs(profiles.loc[1, "session_count"] - 1.4574107417352327) < 1e-6
    assert profiles.loc[0, "size"] == 219
    assert profiles.loc[1, "size"] == 81


def test_segment_profiles_shows_clear_engagement_split():
    df = lesson.load_scaled_features()
    profiles = lesson.segment_profiles(df)
    viewing_columns = ["session_count", "total_minutes_watched", "avg_minutes_per_session"]
    for column in viewing_columns:
        assert profiles.loc[1, column] > 1.0
        assert profiles.loc[0, column] < -0.4


def test_segment_profiles_tenure_barely_differs_between_clusters():
    df = lesson.load_scaled_features()
    profiles = lesson.segment_profiles(df)
    assert abs(profiles.loc[0, "tenure_days"] - profiles.loc[1, "tenure_days"]) < 0.2
