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
