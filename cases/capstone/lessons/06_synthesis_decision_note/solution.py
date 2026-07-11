"""Reference solution for Lesson 6. Do not open this before attempting task.py."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    f1_score,
    mean_absolute_error,
    precision_score,
    recall_score,
    silhouette_score,
)
from sklearn.model_selection import train_test_split

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATASET_MENU = [
    "clinic_wait_times",
    "lendwell_loan_default",
    "retail_store_segments",
]
RANDOM_STATE = 42


def load_clean_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    df = pd.read_csv(data_dir / f"{name}.csv")
    cleaned = df.copy()
    for column in cleaned.columns:
        if cleaned[column].isna().any():
            if pd.api.types.is_numeric_dtype(cleaned[column]):
                cleaned[column] = cleaned[column].fillna(cleaned[column].median())
            else:
                mode_value = cleaned[column].mode().iloc[0]
                cleaned[column] = cleaned[column].fillna(mode_value)
    return cleaned


def split_dataset(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int = RANDOM_STATE
) -> tuple[pd.DataFrame, pd.DataFrame]:
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state)
    return train_df, test_df


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
    model: KMeans, df: pd.DataFrame, feature_columns: list[str]
) -> pd.DataFrame:
    labels = model.predict(df[feature_columns])
    labeled_df = df.copy()
    labeled_df["cluster"] = labels
    summary = labeled_df.groupby("cluster")[feature_columns].mean()
    summary["size"] = labeled_df.groupby("cluster").size()
    summary["share"] = summary["size"] / len(labeled_df)
    return summary
