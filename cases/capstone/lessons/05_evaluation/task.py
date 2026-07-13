"""Lesson 5 task: evaluate your Lesson 4 baseline and model on held-out test data.

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
    """Load the dataset called `name` — no cleaning yet, same as Lesson 4.

    TODO: read data_dir / f"{name}.csv" with pandas.read_csv and return it.
    Missing values are handled later, after the train/test split, by
    impute_missing — not here.
    """
    raise NotImplementedError("load_dataset is not implemented yet")


def split_dataset(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int = RANDOM_STATE
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split df into (train_df, test_df), same as Lesson 4.

    TODO: import train_test_split from sklearn.model_selection and call it
    with test_size=test_size and random_state=random_state. Return the
    result as (train_df, test_df), in that order.
    """
    raise NotImplementedError("split_dataset is not implemented yet")


def impute_missing(
    train_df: pd.DataFrame, test_df: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Fill missing values in both frames using statistics from train_df only, same as Lesson 4.

    TODO: on copies of train_df and test_df, for every column where
    train_df OR test_df has any missing value: if the column is numeric
    (pandas.api.types.is_numeric_dtype), compute fill_value as
    train_df[column].median(); otherwise as
    train_df[column].mode().iloc[0]. Fill that value into both train_df
    and test_df for that column. Return (train_df, test_df).
    """
    raise NotImplementedError("impute_missing is not implemented yet")


def scale_features(df: pd.DataFrame, feature_columns: list[str]) -> pd.DataFrame:
    """Standardize feature_columns to zero mean, unit variance, same as Lesson 4.

    TODO: import StandardScaler from sklearn.preprocessing. On a copy of
    df, replace df[feature_columns] with
    StandardScaler().fit_transform(df[feature_columns]). Return the copy.
    """
    raise NotImplementedError("scale_features is not implemented yet")


def fit_regression_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[float, LinearRegression]:
    """Fit a mean baseline and a LinearRegression model on train_df, same as Lesson 4.

    TODO: compute baseline as train_df[target_column].mean(). Build a
    LinearRegression(), fit it on train_df[feature_columns] and
    train_df[target_column]. Return (baseline, fitted_model).
    """
    raise NotImplementedError("fit_regression_baseline_and_model is not implemented yet")


def fit_classification_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[int, LogisticRegression]:
    """Fit a majority-class baseline and a LogisticRegression model, same as Lesson 4.

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
    """Fit a KMeans model with k clusters on df[feature_columns], same as Lesson 4.

    TODO: build KMeans(n_clusters=k, random_state=random_state, n_init=10),
    fit it on df[feature_columns], and return the fitted model. Pass this
    function an already-scaled df when clustering.
    """
    raise NotImplementedError("fit_clustering_model is not implemented yet")


def evaluate_regression(
    baseline: float,
    model: LinearRegression,
    test_df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> dict[str, float]:
    """Compare baseline and model MAE on held-out test_df.

    TODO: import mean_absolute_error from sklearn.metrics. Build a
    baseline prediction array the same length as test_df, filled with
    `baseline` (e.g. via numpy.full). Compute baseline_mae as
    mean_absolute_error(test_df[target_column], that array). Compute
    model_mae as mean_absolute_error(test_df[target_column],
    model.predict(test_df[feature_columns])). Return
    {"baseline_mae": baseline_mae, "model_mae": model_mae}.
    """
    raise NotImplementedError("evaluate_regression is not implemented yet")


def evaluate_classification(
    baseline: int,
    model: LogisticRegression,
    test_df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> dict[str, float]:
    """Compare baseline and model precision/recall/F1 on held-out test_df.

    TODO: import precision_score, recall_score, f1_score from
    sklearn.metrics (use zero_division=0 in every call, same convention
    as Case 2). Build a baseline prediction array the same length as
    test_df, filled with `baseline`. Compute
    baseline_precision/baseline_recall/baseline_f1 by comparing that
    array to test_df[target_column]. Compute model predictions via
    model.predict(test_df[feature_columns]) and compute
    model_precision/model_recall/model_f1 the same way. Return a dict
    with keys "baseline_precision", "baseline_recall", "baseline_f1",
    "model_precision", "model_recall", "model_f1".
    """
    raise NotImplementedError("evaluate_classification is not implemented yet")


def evaluate_clustering(model: KMeans, df: pd.DataFrame, feature_columns: list[str]) -> float:
    """Return the silhouette score of model's cluster assignments on df.

    TODO: import silhouette_score from sklearn.metrics. Call
    model.predict(df[feature_columns]) to get cluster labels, then return
    silhouette_score(df[feature_columns], labels). Pass this function the
    same scaled df that fit_clustering_model was fit on.
    """
    raise NotImplementedError("evaluate_clustering is not implemented yet")
