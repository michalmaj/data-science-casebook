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


def test_load_scaled_features_shape_and_columns():
    df = lesson.load_scaled_features()
    assert df.shape == (300, 5)
    assert list(df.columns) == ["subscriber_id", *lesson.FEATURE_COLUMNS]


def test_feature_correlations_shape_and_diagonal():
    df = lesson.load_scaled_features()
    corr = lesson.feature_correlations(df)
    assert corr.shape == (4, 4)
    assert list(corr.columns) == lesson.FEATURE_COLUMNS
    assert list(corr.index) == lesson.FEATURE_COLUMNS
    for column in lesson.FEATURE_COLUMNS:
        assert abs(corr.loc[column, column] - 1.0) < 1e-9


def test_feature_correlations_matches_known_values():
    df = lesson.load_scaled_features()
    corr = lesson.feature_correlations(df)
    assert abs(corr.loc["session_count", "total_minutes_watched"] - 0.9707537640647199) < 1e-9
    assert abs(corr.loc["session_count", "tenure_days"] - (-0.09081727446380246)) < 1e-9


def test_feature_correlations_shows_viewing_features_are_redundant():
    df = lesson.load_scaled_features()
    corr = lesson.feature_correlations(df)
    viewing_pairs = [
        ("session_count", "total_minutes_watched"),
        ("session_count", "avg_minutes_per_session"),
        ("total_minutes_watched", "avg_minutes_per_session"),
    ]
    for col_a, col_b in viewing_pairs:
        assert corr.loc[col_a, col_b] > 0.9
    for column in ["session_count", "total_minutes_watched", "avg_minutes_per_session"]:
        assert abs(corr.loc[column, "tenure_days"]) < 0.15
