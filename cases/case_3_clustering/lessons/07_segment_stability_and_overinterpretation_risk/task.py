"""Lesson 7 task: test how well a clustering solution survives resampling.

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
K = 2
FRACTION = 0.8
SEEDS = [0, 1, 2, 3, 4]
RANDOM_STATE = 42
K_VALUES = [2, 3, 4, 5]


def load_scaled_features(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load, join, and scale Aurora Stream's subscriber features, same as Lessons 1-6.

    TODO: run the same SQL as Lesson 1 (LEFT JOIN subscribers to sessions,
    grouped by subscriber_id, using REFERENCE_DATE as a bound query
    parameter) to get subscriber_id, plan_tier, country, and the four
    FEATURE_COLUMNS. Then standardize the four FEATURE_COLUMNS with
    sklearn.preprocessing.StandardScaler, same as Lesson 2, and return a
    DataFrame with subscriber_id plus the scaled FEATURE_COLUMNS.
    """
    raise NotImplementedError("load_scaled_features is not implemented yet")


def subsample_stability(
    df: pd.DataFrame,
    k: int = K,
    fraction: float = FRACTION,
    seeds: list[int] = SEEDS,
    random_state: int = RANDOM_STATE,
) -> pd.DataFrame:
    """Measure how much KMeans(k) labels change on random subsamples of df.

    TODO: fit a baseline sklearn.cluster.KMeans(n_clusters=k,
    random_state=random_state, n_init=10) on df[FEATURE_COLUMNS] and keep
    its labels, indexed the same as df. Then, for each seed in seeds: build
    a numpy.random.default_rng(seed), use it to pick
    int(len(df) * fraction) row labels from df.index without replacement
    (sort them), take that subsample of df, fit a fresh KMeans with the
    same k/random_state/n_init=10 on just the subsample's FEATURE_COLUMNS,
    and compute sklearn.metrics.adjusted_rand_score between the baseline's
    labels restricted to the subsample's rows and the subsample model's own
    labels. Collect one row per seed into a DataFrame with columns "seed"
    and "adjusted_rand_index" and return it.
    """
    raise NotImplementedError("subsample_stability is not implemented yet")


def initialization_stability(
    df: pd.DataFrame, k: int = K, seeds: list[int] = SEEDS
) -> pd.DataFrame:
    """Measure how much KMeans(k) labels change across random initializations
    on the FULL data (no resampling) — a different question from
    subsample_stability's sampling-sensitivity check.

    TODO: fit a baseline sklearn.cluster.KMeans(n_clusters=k,
    random_state=seeds[0], n_init=10) on df[FEATURE_COLUMNS] and keep its
    labels. Then for each seed in seeds, fit a fresh KMeans with that same
    k, random_state=seed, n_init=10 on the SAME full df[FEATURE_COLUMNS]
    (no subsampling), and compute sklearn.metrics.adjusted_rand_score
    between the baseline's labels and this seed's labels. Collect one row
    per seed into a DataFrame with columns "seed" and "adjusted_rand_index"
    (the first row, seed=seeds[0], compares the baseline to itself and
    will be exactly 1.0) and return it.
    """
    raise NotImplementedError("initialization_stability is not implemented yet")


def stability_comparison_table(
    df: pd.DataFrame,
    k_values: list[int] = K_VALUES,
    fraction: float = FRACTION,
    seeds: list[int] = SEEDS,
    random_state: int = RANDOM_STATE,
) -> pd.DataFrame:
    """For each k in k_values, report silhouette, worst-case resample
    stability, and the smallest cluster's share — so k is chosen by
    comparing a set of properties, not by any single number.

    TODO: for each k in k_values: fit sklearn.cluster.KMeans(n_clusters=k,
    random_state=random_state, n_init=10) on df[FEATURE_COLUMNS] once to
    get labels, then sklearn.metrics.silhouette_score on the same
    columns/labels. Call subsample_stability(df, k=k, fraction=fraction,
    seeds=seeds, random_state=random_state) and take the minimum of its
    "adjusted_rand_index" column as "resample_stability_min_ari". Compute
    the smallest cluster's share of len(df) from the same labels as
    "smallest_cluster_share" (value_counts of the labels, take the
    smallest count, divide by len(df)). Collect one row per k into a
    DataFrame with columns "k", "silhouette", "resample_stability_min_ari",
    "smallest_cluster_share" (in that order, one row per k_values entry,
    same order as k_values) and return it.
    """
    raise NotImplementedError("stability_comparison_table is not implemented yet")
