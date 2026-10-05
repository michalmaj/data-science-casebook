"""Reference solution for Lesson 7. Do not open this before attempting task.py."""

import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.preprocessing import StandardScaler

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
    query = """
        SELECT
            s.subscriber_id,
            s.plan_tier,
            s.country,
            COUNT(se.session_date) AS session_count,
            COALESCE(SUM(se.minutes_watched), 0) AS total_minutes_watched,
            COALESCE(AVG(se.minutes_watched), 0) AS avg_minutes_per_session,
            CAST(julianday(?) - julianday(s.signup_date) AS INTEGER) AS tenure_days
        FROM subscribers s
        LEFT JOIN sessions se ON s.subscriber_id = se.subscriber_id
        GROUP BY s.subscriber_id
    """
    conn = sqlite3.connect(path)
    df = pd.read_sql_query(query, conn, params=(REFERENCE_DATE,))
    conn.close()

    scaler = StandardScaler()
    scaled = scaler.fit_transform(df[FEATURE_COLUMNS])
    scaled_df = pd.DataFrame(scaled, columns=FEATURE_COLUMNS)
    scaled_df.insert(0, "subscriber_id", df["subscriber_id"].values)
    return scaled_df


def subsample_stability(
    df: pd.DataFrame,
    k: int = K,
    fraction: float = FRACTION,
    seeds: list[int] = SEEDS,
    random_state: int = RANDOM_STATE,
) -> pd.DataFrame:
    baseline_model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    baseline_labels = baseline_model.fit_predict(df[FEATURE_COLUMNS])
    baseline_series = pd.Series(baseline_labels, index=df.index)

    rows = []
    for seed in seeds:
        rng = np.random.default_rng(seed)
        sample_size = int(len(df) * fraction)
        sample_idx = np.sort(rng.choice(df.index, size=sample_size, replace=False))
        sub_df = df.loc[sample_idx]
        model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
        sub_labels = model.fit_predict(sub_df[FEATURE_COLUMNS])
        sub_series = pd.Series(sub_labels, index=sample_idx)
        ari = adjusted_rand_score(baseline_series.loc[sample_idx], sub_series)
        rows.append({"seed": seed, "adjusted_rand_index": ari})
    return pd.DataFrame(rows)


def initialization_stability(
    df: pd.DataFrame, k: int = K, seeds: list[int] = SEEDS, random_state: int = RANDOM_STATE
) -> pd.DataFrame:
    baseline_model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    baseline_labels = baseline_model.fit_predict(df[FEATURE_COLUMNS])

    rows = []
    for seed in seeds:
        model = KMeans(n_clusters=k, random_state=seed, n_init=10)
        labels = model.fit_predict(df[FEATURE_COLUMNS])
        ari = adjusted_rand_score(baseline_labels, labels)
        rows.append({"seed": seed, "adjusted_rand_index": ari})
    return pd.DataFrame(rows)


def stability_comparison_table(
    df: pd.DataFrame,
    k_values: list[int] = K_VALUES,
    fraction: float = FRACTION,
    seeds: list[int] = SEEDS,
    random_state: int = RANDOM_STATE,
) -> pd.DataFrame:
    rows = []
    for k in k_values:
        model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
        labels = model.fit_predict(df[FEATURE_COLUMNS])
        sil = silhouette_score(df[FEATURE_COLUMNS], labels)
        resample = subsample_stability(
            df, k=k, fraction=fraction, seeds=seeds, random_state=random_state
        )
        min_ari = resample["adjusted_rand_index"].min()
        smallest_share = pd.Series(labels).value_counts().min() / len(labels)
        rows.append(
            {
                "k": k,
                "silhouette": sil,
                "resample_stability_min_ari": min_ari,
                "smallest_cluster_share": smallest_share,
            }
        )
    return pd.DataFrame(rows)
