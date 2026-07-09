"""Lesson 5 task: compare KMeans solutions across a range of k values.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "aurora_stream.sqlite"

REFERENCE_DATE = "2026-04-01"
FEATURE_COLUMNS = [
    "session_count",
    "total_minutes_watched",
    "avg_minutes_per_session",
    "tenure_days",
]
K_VALUES = list(range(2, 9))
RANDOM_STATE = 42


def load_scaled_features(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load, join, and scale Aurora Stream's subscriber features, same as Lessons 1-4.

    TODO: run the same SQL as Lesson 1 (LEFT JOIN subscribers to sessions,
    grouped by subscriber_id, using REFERENCE_DATE as a bound query
    parameter) to get subscriber_id, plan_tier, country, and the four
    FEATURE_COLUMNS. Then standardize the four FEATURE_COLUMNS with
    sklearn.preprocessing.StandardScaler, same as Lesson 2, and return a
    DataFrame with subscriber_id plus the scaled FEATURE_COLUMNS.
    """
    raise NotImplementedError("load_scaled_features is not implemented yet")


def cluster_metrics_by_k(
    df: pd.DataFrame, k_values: list[int] = K_VALUES, random_state: int = RANDOM_STATE
) -> pd.DataFrame:
    """Fit KMeans once per k in k_values and record inertia and silhouette score.

    TODO: for each k in k_values, build sklearn.cluster.KMeans(n_clusters=k,
    random_state=random_state, n_init=10), fit_predict it on
    df[FEATURE_COLUMNS], then compute sklearn.metrics.silhouette_score on
    df[FEATURE_COLUMNS] and the resulting labels. Collect the results into
    a DataFrame with columns "k", "inertia", "silhouette" (one row per k,
    in the same order as k_values) and return it.
    """
    raise NotImplementedError("cluster_metrics_by_k is not implemented yet")
