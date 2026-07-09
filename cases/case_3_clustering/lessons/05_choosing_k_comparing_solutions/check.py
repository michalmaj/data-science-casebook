"""Self-check for Lesson 5. Run with `uv run pytest` in this directory.

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


def test_cluster_metrics_by_k_shape_and_columns():
    df = lesson.load_scaled_features()
    metrics = lesson.cluster_metrics_by_k(df)
    assert metrics.shape == (7, 3)
    assert list(metrics.columns) == ["k", "inertia", "silhouette"]
    assert list(metrics["k"]) == [2, 3, 4, 5, 6, 7, 8]


def test_cluster_metrics_by_k_matches_known_values():
    df = lesson.load_scaled_features()
    metrics = lesson.cluster_metrics_by_k(df).set_index("k")
    assert abs(metrics.loc[2, "inertia"] - 430.1938819385636) < 1e-6
    assert abs(metrics.loc[2, "silhouette"] - 0.6048203554783642) < 1e-6
    assert abs(metrics.loc[4, "inertia"] - 202.9599282041436) < 1e-6
    assert abs(metrics.loc[4, "silhouette"] - 0.4441873734011112) < 1e-6


def test_cluster_metrics_by_k_inertia_decreases_monotonically():
    df = lesson.load_scaled_features()
    metrics = lesson.cluster_metrics_by_k(df)
    diffs = metrics["inertia"].diff().dropna()
    assert (diffs < 0).all()


def test_cluster_metrics_by_k_best_silhouette_is_k_2():
    df = lesson.load_scaled_features()
    metrics = lesson.cluster_metrics_by_k(df)
    best_row = metrics.loc[metrics["silhouette"].idxmax()]
    assert int(best_row["k"]) == 2
