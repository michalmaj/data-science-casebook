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


def test_cluster_metrics_by_k_silhouette_peaks_at_k_2_for_this_dataset():
    # A dataset-specific, tested fact — not a claim that k=2 is the
    # universally "correct" number of segments. Silhouette only ranks the
    # k values actually tried, under this data's current geometry.
    df = lesson.load_scaled_features()
    metrics = lesson.cluster_metrics_by_k(df)
    best_row = metrics.loc[metrics["silhouette"].idxmax()]
    assert int(best_row["k"]) == 2


def test_cluster_metrics_by_k_silhouette_is_noisy_not_monotonic_after_its_peak():
    # Silhouette doesn't decay cleanly after k=2 — there's no clear
    # "second place." This rules out "just take the next-highest
    # silhouette if you don't trust the top one."
    df = lesson.load_scaled_features()
    metrics = lesson.cluster_metrics_by_k(df).set_index("k")
    sil = metrics["silhouette"]
    assert sil[3] > sil[4]
    assert sil[5] > sil[4]
    assert sil[6] > sil[5]
    assert sil[7] < sil[6]
    assert sil[8] < sil[7]


def test_compare_feature_sets_at_k2_shows_robust_coarse_split():
    df = lesson.load_scaled_features()
    result = lesson.compare_feature_sets(df, k=2)
    assert abs(result["ari"] - 1.0) < 1e-9
    assert abs(result["silhouette_full"] - 0.6048203554783642) < 1e-6
    assert abs(result["silhouette_reduced"] - 0.5140387549879696) < 1e-6


def test_compare_feature_sets_at_k4_shows_real_sensitivity():
    # Unlike k=2, the finer k=4 split is NOT identical between feature
    # sets — the "see it in practice" demonstration that feature choice
    # is part of the segmentation, not a detail to get out of the way.
    df = lesson.load_scaled_features()
    result = lesson.compare_feature_sets(df, k=4)
    assert abs(result["ari"] - 0.9769982544982871) < 1e-6
    assert result["ari"] < 1.0
    assert abs(result["silhouette_full"] - 0.4441873734011112) < 1e-6
    assert abs(result["silhouette_reduced"] - 0.5604884334099374) < 1e-6
