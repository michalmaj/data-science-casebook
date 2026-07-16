"""Self-check for Lesson 4. Run with `uv run pytest` in this directory.

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


def test_load_scaled_features_shape_and_columns():
    df = lesson.load_scaled_features()
    assert df.shape == (300, 5)
    assert list(df.columns) == ["subscriber_id", *lesson.FEATURE_COLUMNS]


def test_fit_kmeans_returns_model_with_requested_cluster_count():
    df = lesson.load_scaled_features()
    model = lesson.fit_kmeans(df)
    assert model.n_clusters == 4
    assert sorted(set(model.labels_.tolist())) == [0, 1, 2, 3]
    assert model.cluster_centers_.shape == (4, 4)


def test_fit_kmeans_inertia_matches_known_value():
    df = lesson.load_scaled_features()
    model = lesson.fit_kmeans(df)
    assert abs(model.inertia_ - 202.9599282041436) < 1e-6


def test_fit_kmeans_cluster_sizes_match_known_value():
    df = lesson.load_scaled_features()
    model = lesson.fit_kmeans(df)
    sizes = pd.Series(model.labels_).value_counts().sort_index().to_dict()
    assert sorted(sizes.values()) == [38, 43, 106, 113]


def test_fit_kmeans_is_deterministic_across_runs():
    df = lesson.load_scaled_features()
    model_a = lesson.fit_kmeans(df)
    model_b = lesson.fit_kmeans(df)
    assert (model_a.labels_ == model_b.labels_).all()
