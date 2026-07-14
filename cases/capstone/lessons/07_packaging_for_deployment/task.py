"""Lesson 7 task (optional): package your preprocessing as a Pipeline/ColumnTransformer.

This lesson is not graded — it's an extra, hands-on look at how you'd
package Lessons 4-6's manual impute -> scale -> fit sequence into one
fitted object, and a chance to actually use a categorical column your
earlier lessons only imputed. Fill in each TODO below. Run
`uv run pytest` in this directory to check your work.
"""

from pathlib import Path
from typing import TYPE_CHECKING

import pandas as pd

if TYPE_CHECKING:
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import Pipeline

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

DATASET_MENU = [
    "clinic_wait_times",
    "lendwell_loan_default",
    "retail_store_segments",
]
RANDOM_STATE = 42

NUMERIC_FEATURES = {
    "clinic_wait_times": ["num_patients_ahead", "staff_on_duty", "hour_of_day", "patient_age"],
    "lendwell_loan_default": [
        "loan_amount",
        "annual_income",
        "credit_score",
        "debt_to_income_ratio",
        "employment_years",
        "previous_defaults",
    ],
    "retail_store_segments": [
        "store_size_sqft",
        "monthly_revenue",
        "foot_traffic",
        "avg_transaction_value",
        "return_rate",
        "inventory_turnover",
    ],
}
CATEGORICAL_FEATURES = {
    "clinic_wait_times": ["department"],
    "lendwell_loan_default": ["loan_purpose"],
    "retail_store_segments": ["region"],
}


def load_dataset(name: str, data_dir: Path = DATA_DIR) -> pd.DataFrame:
    """Load the dataset called `name` — no cleaning yet, same as Lessons 4-6.

    TODO: read data_dir / f"{name}.csv" with pandas.read_csv and return it.
    """
    raise NotImplementedError("load_dataset is not implemented yet")


def split_dataset(
    df: pd.DataFrame,
    test_size: float = 0.2,
    random_state: int = RANDOM_STATE,
    stratify_column: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split df into (train_df, test_df), same as Lessons 4-6.

    TODO: import train_test_split from sklearn.model_selection. If
    stratify_column is not None, pass df[stratify_column] as the stratify
    argument; otherwise pass stratify=None. Call it with test_size=test_size
    and random_state=random_state. Return (train_df, test_df).
    """
    raise NotImplementedError("split_dataset is not implemented yet")


def build_preprocessor(
    numeric_features: list[str], categorical_features: list[str]
) -> "ColumnTransformer":
    """Build one ColumnTransformer that handles numeric and categorical columns differently.

    TODO: import ColumnTransformer from sklearn.compose, Pipeline from
    sklearn.pipeline, SimpleImputer from sklearn.impute, and
    OneHotEncoder/StandardScaler from sklearn.preprocessing. Build a
    ColumnTransformer with two named branches: "numeric" — a Pipeline of
    SimpleImputer(strategy="median") then StandardScaler(), applied to
    numeric_features; "categorical" — a Pipeline of
    SimpleImputer(strategy="most_frequent") then
    OneHotEncoder(handle_unknown="ignore"), applied to
    categorical_features. handle_unknown="ignore" matters here: without
    it, a category value the encoder never saw during fit (e.g. a new
    department opening after this model is deployed) would raise an
    error at prediction time instead of being handled gracefully. Return
    the ColumnTransformer.
    """
    raise NotImplementedError("build_preprocessor is not implemented yet")


def build_and_fit_regression_pipeline(
    train_df: pd.DataFrame,
    target_column: str,
    numeric_features: list[str],
    categorical_features: list[str],
) -> "Pipeline":
    """Build and fit one Pipeline that preprocesses and fits a LinearRegression in one call.

    TODO: call build_preprocessor(numeric_features, categorical_features)
    to get a ColumnTransformer. Wrap it in a two-step Pipeline:
    ("preprocessor", <the ColumnTransformer>), ("model", LinearRegression()).
    Fit the pipeline on train_df[numeric_features + categorical_features]
    and train_df[target_column] — one .fit() call does what Lessons 4-6
    needed impute_missing, then fit_regression_baseline_and_model to do
    across two steps. Return the fitted pipeline.
    """
    raise NotImplementedError("build_and_fit_regression_pipeline is not implemented yet")


def build_and_fit_classification_pipeline(
    train_df: pd.DataFrame,
    target_column: str,
    numeric_features: list[str],
    categorical_features: list[str],
) -> "Pipeline":
    """Build and fit one Pipeline that preprocesses and fits a LogisticRegression in one call.

    TODO: same pattern as build_and_fit_regression_pipeline, but the
    final step is ("model", LogisticRegression(max_iter=1000)) — the
    default max_iter=100 does not converge on this data's raw feature
    scales. Fit on train_df[numeric_features + categorical_features] and
    train_df[target_column]. Return the fitted pipeline.
    """
    raise NotImplementedError("build_and_fit_classification_pipeline is not implemented yet")


def build_and_fit_clustering_pipeline(
    df: pd.DataFrame,
    numeric_features: list[str],
    categorical_features: list[str],
    k: int = 3,
    random_state: int = RANDOM_STATE,
) -> "Pipeline":
    """Build and fit one Pipeline that preprocesses and fits a KMeans in one call.

    TODO: same pattern again, but the final step is
    ("model", KMeans(n_clusters=k, random_state=random_state, n_init=10)),
    and there's no target column — clustering never splits into
    train/test (same convention as Case 3 and Capstone Lessons 4-6). Fit
    on df[numeric_features + categorical_features]. Return the fitted
    pipeline.
    """
    raise NotImplementedError("build_and_fit_clustering_pipeline is not implemented yet")


def evaluate_pipeline_regression(
    pipeline: "Pipeline",
    test_df: pd.DataFrame,
    target_column: str,
    numeric_features: list[str],
    categorical_features: list[str],
) -> dict[str, float]:
    """Evaluate a fitted regression pipeline's MAE on held-out test data.

    TODO: call pipeline.predict on
    test_df[numeric_features + categorical_features] to get predictions.
    Import mean_absolute_error from sklearn.metrics and compute it
    against test_df[target_column]. Return {"mae": mae}.
    """
    raise NotImplementedError("evaluate_pipeline_regression is not implemented yet")


def evaluate_pipeline_classification(
    pipeline: "Pipeline",
    test_df: pd.DataFrame,
    target_column: str,
    numeric_features: list[str],
    categorical_features: list[str],
) -> dict[str, float]:
    """Evaluate a fitted classification pipeline's precision/recall/f1 on held-out test data.

    TODO: call pipeline.predict on
    test_df[numeric_features + categorical_features]. Import
    precision_score, recall_score, f1_score from sklearn.metrics (same
    as Lesson 5's evaluate_classification), each with zero_division=0.
    Return {"precision": ..., "recall": ..., "f1": ...}.
    """
    raise NotImplementedError("evaluate_pipeline_classification is not implemented yet")


def evaluate_pipeline_clustering(
    pipeline: "Pipeline",
    df: pd.DataFrame,
    numeric_features: list[str],
    categorical_features: list[str],
) -> float:
    """Evaluate a fitted clustering pipeline's silhouette score.

    TODO: silhouette_score needs the transformed (numeric) feature
    matrix, not the raw df with mixed types — get it via
    pipeline.named_steps["preprocessor"].transform(df[numeric_features +
    categorical_features]). Get the fitted cluster labels via
    pipeline.named_steps["model"].labels_. Import silhouette_score from
    sklearn.metrics and return silhouette_score(transformed, labels).
    """
    raise NotImplementedError("evaluate_pipeline_clustering is not implemented yet")
