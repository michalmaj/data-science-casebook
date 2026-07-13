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


def load_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load the dataset called `name` — no cleaning yet.

    TODO: read data_dir / f"{name}.csv" with pandas.read_csv and return it.
    Missing values are handled later, after the train/test split, by
    impute_missing — not here. Imputing before splitting would leak
    information from the test set into the values used to fill the
    training set.
    """
    raise NotImplementedError("load_dataset is not implemented yet")


def split_dataset(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int = RANDOM_STATE
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split df into (train_df, test_df). Works the same regardless of dataset.

    TODO: import train_test_split from sklearn.model_selection and call it
    with test_size=test_size and random_state=random_state. Return the
    result as (train_df, test_df), in that order.
    """
    raise NotImplementedError("split_dataset is not implemented yet")


def impute_missing(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing values in both frames using statistics from train_df only.

    TODO: on copies of train_df and test_df, for every column where
    train_df OR test_df has any missing value: if the column is numeric
    (pandas.api.types.is_numeric_dtype), compute fill_value as
    train_df[column].median(); otherwise as
    train_df[column].mode().iloc[0]. Fill that value into both train_df
    and test_df for that column (never compute a fill value from
    test_df — only train_df). Return (train_df, test_df).
    """
    raise NotImplementedError("impute_missing is not implemented yet")


def scale_features(df: pd.DataFrame, feature_columns: list[str]) -> pd.DataFrame:
    """Standardize feature_columns to zero mean, unit variance (z-scores).

    TODO: import StandardScaler from sklearn.preprocessing. On a copy of
    df, replace df[feature_columns] with
    StandardScaler().fit_transform(df[feature_columns]). Return the
    copy. Used only by the clustering path — KMeans measures distance
    directly on feature values, so unscaled features with different
    magnitudes (e.g. monthly_revenue in the tens of thousands vs.
    return_rate as a small decimal) would dominate the distance metric
    regardless of which features actually separate the data.
    """
    raise NotImplementedError("scale_features is not implemented yet")


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
    fit it on df[feature_columns], and return the fitted model. Pass this
    function an already-scaled df (see scale_features) when clustering —
    it does not scale internally.
    """
    raise NotImplementedError("fit_clustering_model is not implemented yet")
