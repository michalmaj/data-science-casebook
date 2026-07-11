"""Lesson 4 task: fit a baseline and a first model for your chosen dataset.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression, LogisticRegression

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATASET_MENU = [
    "clinic_wait_times",
    "lendwell_loan_default",
    "retail_store_segments",
]
RANDOM_STATE = 42


def load_clean_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load and clean the dataset called `name`, same as Lessons 1-3.

    TODO: read data_dir / f"{name}.csv" with pandas.read_csv. Then, on a
    copy of that DataFrame, for every column with any missing values: if
    the column is numeric (pandas.api.types.is_numeric_dtype), fill it
    with the column's median; otherwise fill it with the column's most
    frequent value (column.mode().iloc[0]). Return the cleaned DataFrame.
    """
    raise NotImplementedError("load_clean_dataset is not implemented yet")


def split_dataset(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int = RANDOM_STATE
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split df into (train_df, test_df). Works the same regardless of dataset.

    TODO: import train_test_split from sklearn.model_selection and call it
    with test_size=test_size and random_state=random_state. Return the
    result as (train_df, test_df), in that order.
    """
    raise NotImplementedError("split_dataset is not implemented yet")


def fit_regression_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[float, LinearRegression]:
    """Fit a mean baseline and a LinearRegression model on train_df.

    TODO: compute baseline as train_df[target_column].mean(). Build a
    LinearRegression(), fit it on train_df[feature_columns] and
    train_df[target_column]. Return (baseline, fitted_model).
    """
    raise NotImplementedError("fit_regression_baseline_and_model is not implemented yet")


def fit_classification_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[int, LogisticRegression]:
    """Fit a majority-class baseline and a LogisticRegression model on train_df.

    TODO: compute baseline as train_df[target_column].mode().iloc[0]. Build
    a LogisticRegression(max_iter=1000) — the default max_iter=100 does not
    converge on this data's raw feature scales — fit it on
    train_df[feature_columns] and train_df[target_column]. Return
    (baseline, fitted_model).
    """
    raise NotImplementedError("fit_classification_baseline_and_model is not implemented yet")


def fit_clustering_model(
    df: pd.DataFrame, feature_columns: list[str], k: int = 3, random_state: int = RANDOM_STATE
) -> KMeans:
    """Fit a KMeans model with k clusters on df[feature_columns].

    TODO: build KMeans(n_clusters=k, random_state=random_state, n_init=10),
    fit it on df[feature_columns], and return the fitted model.
    """
    raise NotImplementedError("fit_clustering_model is not implemented yet")
