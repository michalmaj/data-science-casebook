"""Reference solution for Lesson 6. Do not open this before attempting task.py."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    adjusted_rand_score,
    f1_score,
    mean_absolute_error,
    precision_score,
    recall_score,
    silhouette_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATASET_MENU = [
    "clinic_wait_times",
    "lendwell_loan_default",
    "retail_store_segments",
]
RANDOM_STATE = 42
CLUSTER_STABILITY_SEEDS = [0, 1, 2, 3, 4]


def load_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    return pd.read_csv(data_dir / f"{name}.csv")


def split_dataset(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = RANDOM_STATE,
    stratify_column: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    stratify = df[stratify_column] if stratify_column else None
    train_df, test_df = train_test_split(
        df, test_size=test_size, random_state=random_state, stratify=stratify
    )
    return train_df, test_df


def impute_missing(
    train_df: pd.DataFrame, test_df: pd.DataFrame, feature_columns: list[str]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    train_df = train_df.copy()
    test_df = test_df.copy()
    for column in feature_columns:
        if train_df[column].isna().any() or test_df[column].isna().any():
            if pd.api.types.is_numeric_dtype(train_df[column]):
                fill_value = train_df[column].median()
            else:
                fill_value = train_df[column].mode().iloc[0]
            train_df[column] = train_df[column].fillna(fill_value)
            test_df[column] = test_df[column].fillna(fill_value)
    return train_df, test_df


def scale_features(
    df: pd.DataFrame, feature_columns: list[str]
) -> tuple[pd.DataFrame, StandardScaler]:
    df = df.copy()
    scaler = StandardScaler()
    df[feature_columns] = scaler.fit_transform(df[feature_columns])
    return df, scaler


def fit_regression_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[float, LinearRegression]:
    baseline = train_df[target_column].mean()
    model = LinearRegression()
    model.fit(train_df[feature_columns], train_df[target_column])
    return baseline, model


def fit_classification_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[int, LogisticRegression]:
    baseline = train_df[target_column].mode().iloc[0]
    model = LogisticRegression(max_iter=1000)
    model.fit(train_df[feature_columns], train_df[target_column])
    return baseline, model


def fit_clustering_model(
    df: pd.DataFrame, feature_columns: list[str], k: int = 3, random_state: int = RANDOM_STATE
) -> KMeans:
    model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    model.fit(df[feature_columns])
    return model


def evaluate_regression(
    baseline: float,
    model: LinearRegression,
    test_df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> dict[str, float]:
    baseline_preds = np.full(len(test_df), baseline)
    model_preds = model.predict(test_df[feature_columns])
    baseline_mae = mean_absolute_error(test_df[target_column], baseline_preds)
    model_mae = mean_absolute_error(test_df[target_column], model_preds)
    return {"baseline_mae": baseline_mae, "model_mae": model_mae}


def evaluate_classification(
    baseline: int,
    model: LogisticRegression,
    test_df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> dict[str, float]:
    baseline_preds = np.full(len(test_df), baseline)
    model_preds = model.predict(test_df[feature_columns])
    y_true = test_df[target_column]
    return {
        "baseline_precision": precision_score(y_true, baseline_preds, zero_division=0),
        "baseline_recall": recall_score(y_true, baseline_preds, zero_division=0),
        "baseline_f1": f1_score(y_true, baseline_preds, zero_division=0),
        "model_precision": precision_score(y_true, model_preds, zero_division=0),
        "model_recall": recall_score(y_true, model_preds, zero_division=0),
        "model_f1": f1_score(y_true, model_preds, zero_division=0),
    }


def evaluate_clustering(model: KMeans, df: pd.DataFrame, feature_columns: list[str]) -> float:
    labels = model.predict(df[feature_columns])
    return silhouette_score(df[feature_columns], labels)


def cluster_stability(
    df: pd.DataFrame,
    feature_columns: list[str],
    k: int = 3,
    fraction: float = 0.8,
    seeds: list[int] = CLUSTER_STABILITY_SEEDS,
    random_state: int = RANDOM_STATE,
) -> pd.DataFrame:
    baseline_model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    baseline_labels = baseline_model.fit_predict(df[feature_columns])
    baseline_series = pd.Series(baseline_labels, index=df.index)

    rows = []
    for seed in seeds:
        rng = np.random.default_rng(seed)
        sample_size = int(len(df) * fraction)
        sample_idx = np.sort(rng.choice(df.index, size=sample_size, replace=False))
        sub_df = df.loc[sample_idx]
        model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
        sub_labels = model.fit_predict(sub_df[feature_columns])
        sub_series = pd.Series(sub_labels, index=sample_idx)
        ari = adjusted_rand_score(baseline_series.loc[sample_idx], sub_series)
        rows.append({"seed": seed, "adjusted_rand_index": ari})
    return pd.DataFrame(rows)


def final_regression_scorecard(
    baseline: float,
    model: LinearRegression,
    test_df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> pd.DataFrame:
    metrics = evaluate_regression(baseline, model, test_df, target_column, feature_columns)
    return pd.DataFrame(
        {"mae": [metrics["baseline_mae"], metrics["model_mae"]]},
        index=["baseline", "model"],
    )


def final_classification_scorecard(
    baseline: int,
    model: LogisticRegression,
    test_df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> pd.DataFrame:
    metrics = evaluate_classification(baseline, model, test_df, target_column, feature_columns)
    return pd.DataFrame(
        {
            "precision": [metrics["baseline_precision"], metrics["model_precision"]],
            "recall": [metrics["baseline_recall"], metrics["model_recall"]],
            "f1": [metrics["baseline_f1"], metrics["model_f1"]],
        },
        index=["baseline", "model"],
    )


def final_clustering_summary(
    model: KMeans, scaled_df: pd.DataFrame, raw_df: pd.DataFrame, feature_columns: list[str]
) -> pd.DataFrame:
    labels = model.predict(scaled_df[feature_columns])
    labeled_df = raw_df.copy()
    labeled_df["cluster"] = labels
    summary = labeled_df.groupby("cluster")[feature_columns].mean()
    summary["size"] = labeled_df.groupby("cluster").size()
    summary["share"] = summary["size"] / len(labeled_df)
    return summary
