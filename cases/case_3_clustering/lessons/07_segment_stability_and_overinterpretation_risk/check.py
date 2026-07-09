"""Self-check for Lesson 7. Run with `uv run pytest` in this directory.

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


def test_subsample_stability_shape_and_columns():
    df = lesson.load_scaled_features()
    result = lesson.subsample_stability(df)
    assert result.shape == (5, 2)
    assert list(result.columns) == ["seed", "adjusted_rand_index"]
    assert list(result["seed"]) == [0, 1, 2, 3, 4]


def test_subsample_stability_k2_is_perfectly_stable():
    df = lesson.load_scaled_features()
    result = lesson.subsample_stability(df)
    assert (result["adjusted_rand_index"] - 1.0).abs().max() < 1e-9


def test_subsample_stability_k4_matches_known_values():
    df = lesson.load_scaled_features()
    result = lesson.subsample_stability(df, k=4).set_index("seed")
    assert abs(result.loc[0, "adjusted_rand_index"] - 0.9802378113497089) < 1e-6
    assert abs(result.loc[1, "adjusted_rand_index"] - 0.9714190847159103) < 1e-6
    assert abs(result.loc[2, "adjusted_rand_index"] - 1.0) < 1e-6


def test_subsample_stability_k2_is_more_stable_than_k4():
    df = lesson.load_scaled_features()
    result_k2 = lesson.subsample_stability(df)
    result_k4 = lesson.subsample_stability(df, k=4)
    assert result_k2["adjusted_rand_index"].min() > result_k4["adjusted_rand_index"].min()
