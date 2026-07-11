"""Lesson 6 task: turn your evaluated model into the one table your decision note rests on.

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
    """Load and clean the dataset called `name`, same as Lessons 1-5.

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
    """Split df into (train_df, test_df), same as Lessons 4-5.

    TODO: import train_test_split from sklearn.model_selection and call it
    with test_size=test_size and random_state=random_state. Return the
    result as (train_df, test_df), in that order.
    """
    raise NotImplementedError("split_dataset is not implemented yet")


def fit_regression_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[float, LinearRegression]:
    """Fit a mean baseline and a LinearRegression model on train_df, same as Lessons 4-5.

    TODO: compute baseline as train_df[target_column].mean(). Build a
    LinearRegression(), fit it on train_df[feature_columns] and
    train_df[target_column]. Return (baseline, fitted_model).
    """
    raise NotImplementedError("fit_regression_baseline_and_model is not implemented yet")


def fit_classification_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[int, LogisticRegression]:
    """Fit a majority-class baseline and a LogisticRegression model, same as Lessons 4-5.

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
    """Fit a KMeans model with k clusters on df[feature_columns], same as Lessons 4-5.

    TODO: build KMeans(n_clusters=k, random_state=random_state, n_init=10),
    fit it on df[feature_columns], and return the fitted model.
    """
    raise NotImplementedError("fit_clustering_model is not implemented yet")


def evaluate_regression(
    baseline: float,
    model: LinearRegression,
    test_df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> dict[str, float]:
    """Compare baseline and model MAE on held-out test_df, same as Lesson 5.

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
    """Compare baseline and model precision/recall/F1 on held-out test_df, same as Lesson 5.

    TODO: import precision_score, recall_score, f1_score from
    sklearn.metrics (use zero_division=0 in every call). Build a baseline
    prediction array the same length as test_df, filled with `baseline`.
    Compute baseline_precision/baseline_recall/baseline_f1 by comparing
    that array to test_df[target_column]. Compute model predictions via
    model.predict(test_df[feature_columns]) and compute
    model_precision/model_recall/model_f1 the same way. Return a dict
    with keys "baseline_precision", "baseline_recall", "baseline_f1",
    "model_precision", "model_recall", "model_f1".
    """
    raise NotImplementedError("evaluate_classification is not implemented yet")


def evaluate_clustering(model: KMeans, df: pd.DataFrame, feature_columns: list[str]) -> float:
    """Return the silhouette score of model's cluster assignments on df, same as Lesson 5.

    TODO: import silhouette_score from sklearn.metrics. Call
    model.predict(df[feature_columns]) to get cluster labels, then return
    silhouette_score(df[feature_columns], labels).
    """
    raise NotImplementedError("evaluate_clustering is not implemented yet")


def final_regression_scorecard(
    baseline: float,
    model: LinearRegression,
    test_df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> pd.DataFrame:
    """Turn evaluate_regression's result into a two-row decision-note table.

    TODO: call evaluate_regression(baseline, model, test_df, target_column,
    feature_columns) to get a metrics dict. Build and return a
    pandas.DataFrame with a single column "mae" containing
    [metrics["baseline_mae"], metrics["model_mae"]], indexed by
    ["baseline", "model"] in that order.
    """
    raise NotImplementedError("final_regression_scorecard is not implemented yet")


def final_classification_scorecard(
    baseline: int,
    model: LogisticRegression,
    test_df: pd.DataFrame,
    target_column: str,
    feature_columns: list[str],
) -> pd.DataFrame:
    """Turn evaluate_classification's result into a two-row decision-note table.

    TODO: call evaluate_classification(baseline, model, test_df,
    target_column, feature_columns) to get a metrics dict. Build and
    return a pandas.DataFrame with columns "precision", "recall", "f1",
    each containing [metrics["baseline_<metric>"],
    metrics["model_<metric>"]], indexed by ["baseline", "model"] in that
    order.
    """
    raise NotImplementedError("final_classification_scorecard is not implemented yet")


def final_clustering_summary(
    model: KMeans, df: pd.DataFrame, feature_columns: list[str]
) -> pd.DataFrame:
    """Build the per-cluster profile table this case's segments are described from.

    TODO: call model.predict(df[feature_columns]) to get cluster labels.
    On a copy of df, add a "cluster" column with those labels. Group by
    "cluster" and compute the mean of feature_columns per group as the
    result DataFrame. Add a "size" column with the number of rows in each
    cluster (group sizes), and a "share" column equal to "size" divided
    by len(df). Return the resulting DataFrame, indexed by cluster label,
    with columns feature_columns followed by "size" then "share".
    """
    raise NotImplementedError("final_clustering_summary is not implemented yet")
