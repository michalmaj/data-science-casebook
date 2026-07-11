"""Reference solution for Lesson 4. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression, LogisticRegression
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
