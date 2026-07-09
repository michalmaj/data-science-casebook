"""Self-check for Lesson 2. Run with `uv run pytest` in this directory.

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


def test_load_subscriber_features_returns_300_rows():
    df = lesson.load_subscriber_features()
    assert df.shape == (300, 7)


def test_scale_features_shape_and_columns():
    df = lesson.load_subscriber_features()
    scaled = lesson.scale_features(df)
    assert scaled.shape == (300, 5)
    assert list(scaled.columns) == [
        "subscriber_id",
        "session_count",
        "total_minutes_watched",
        "avg_minutes_per_session",
        "tenure_days",
    ]


def test_scale_features_produces_standardized_columns():
    df = lesson.load_subscriber_features()
    scaled = lesson.scale_features(df)
    for column in lesson.FEATURE_COLUMNS:
        assert abs(scaled[column].mean()) < 1e-9
        assert abs(scaled[column].std(ddof=0) - 1.0) < 1e-9


def test_scale_features_matches_a_known_row():
    df = lesson.load_subscriber_features()
    scaled = lesson.scale_features(df)
    row = scaled[scaled["subscriber_id"] == "SUB-0001"].iloc[0]
    assert abs(row["session_count"] - (-0.5043062811594731)) < 1e-9
    assert abs(row["total_minutes_watched"] - (-0.542285455473438)) < 1e-9
    assert abs(row["avg_minutes_per_session"] - (-0.21945301268969813)) < 1e-9
    assert abs(row["tenure_days"] - (-0.8201558031818501)) < 1e-9
