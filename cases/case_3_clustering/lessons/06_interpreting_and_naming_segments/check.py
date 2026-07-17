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
    assert df.shape == (300, 9)
    assert list(df.columns) == [
        "subscriber_id",
        *lesson.FEATURE_COLUMNS,
        *lesson.SCALED_FEATURE_COLUMNS,
    ]


def test_segment_profiles_shape_and_columns():
    df = lesson.load_scaled_features()
    profiles = lesson.segment_profiles(df)
    assert profiles.shape == (2, 5)
    assert list(profiles.columns) == [*lesson.FEATURE_COLUMNS, "size"]
    assert list(profiles.index) == [0, 1]


def test_segment_profiles_matches_known_values():
    df = lesson.load_scaled_features()
    profiles = lesson.segment_profiles(df)
    # Sort by session_count (itself part of what's being verified) so size
    # is checked in the same, now label-independent row order — this keeps
    # the session_count/size correspondence a cluster actually has, unlike
    # sorting each column independently.
    by_session_count = profiles.sort_values("session_count").reset_index(drop=True)
    assert abs(by_session_count.loc[0, "session_count"] - 13.429223744292237) < 1e-6
    assert abs(by_session_count.loc[1, "session_count"] - 46.23456790123457) < 1e-6
    assert by_session_count.loc[0, "size"] == 219
    assert by_session_count.loc[1, "size"] == 81


def test_segment_profiles_shows_clear_engagement_split():
    df = lesson.load_scaled_features()
    profiles = lesson.segment_profiles(df)
    viewing_columns = ["session_count", "total_minutes_watched", "avg_minutes_per_session"]
    low_engagement_label = profiles["session_count"].idxmin()
    high_engagement_label = profiles["session_count"].idxmax()
    for column in viewing_columns:
        high_value = profiles.loc[high_engagement_label, column]
        low_value = profiles.loc[low_engagement_label, column]
        assert high_value > 2 * low_value


def test_segment_profiles_tenure_barely_differs_between_clusters():
    df = lesson.load_scaled_features()
    profiles = lesson.segment_profiles(df)
    # tenure_days has a population standard deviation of ~242 days; a gap
    # under ~48 days (~0.2 standard deviations) means tenure isn't what
    # separates these two clusters, unlike the viewing-engagement columns
    # above. The actual gap is ~34.6 days.
    assert abs(profiles.loc[0, "tenure_days"] - profiles.loc[1, "tenure_days"]) < 50
