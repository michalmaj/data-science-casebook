"""Reference solution for Lesson 7. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    f1_score,
    mean_absolute_error,
    precision_score,
    recall_score,
    silhouette_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

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


def build_preprocessor(
    numeric_features: list[str], categorical_features: list[str]
) -> ColumnTransformer:
    numeric_pipeline = Pipeline(
        [("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )
    return ColumnTransformer(
        [
            (
                "numeric",
                numeric_pipeline,
                numeric_features,
            ),
            (
                "categorical",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("encoder", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                categorical_features,
            ),
        ]
    )


def build_and_fit_regression_pipeline(
    train_df: pd.DataFrame,
    target_column: str,
    numeric_features: list[str],
    categorical_features: list[str],
) -> Pipeline:
    preprocessor = build_preprocessor(numeric_features, categorical_features)
    pipeline = Pipeline([("preprocessor", preprocessor), ("model", LinearRegression())])
    pipeline.fit(train_df[numeric_features + categorical_features], train_df[target_column])
    return pipeline


def build_and_fit_classification_pipeline(
    train_df: pd.DataFrame,
    target_column: str,
    numeric_features: list[str],
    categorical_features: list[str],
) -> Pipeline:
    preprocessor = build_preprocessor(numeric_features, categorical_features)
    model = LogisticRegression(max_iter=1000)
    pipeline = Pipeline([("preprocessor", preprocessor), ("model", model)])
    pipeline.fit(train_df[numeric_features + categorical_features], train_df[target_column])
    return pipeline


def build_and_fit_clustering_pipeline(
    df: pd.DataFrame,
    numeric_features: list[str],
    categorical_features: list[str],
    k: int = 3,
    random_state: int = RANDOM_STATE,
) -> Pipeline:
    preprocessor = build_preprocessor(numeric_features, categorical_features)
    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("model", KMeans(n_clusters=k, random_state=random_state, n_init=10)),
        ]
    )
    pipeline.fit(df[numeric_features + categorical_features])
    return pipeline


def evaluate_pipeline_regression(
    pipeline: Pipeline,
    test_df: pd.DataFrame,
    target_column: str,
    numeric_features: list[str],
    categorical_features: list[str],
) -> dict[str, float]:
    preds = pipeline.predict(test_df[numeric_features + categorical_features])
    return {"mae": mean_absolute_error(test_df[target_column], preds)}


def evaluate_pipeline_classification(
    pipeline: Pipeline,
    test_df: pd.DataFrame,
    target_column: str,
    numeric_features: list[str],
    categorical_features: list[str],
) -> dict[str, float]:
    preds = pipeline.predict(test_df[numeric_features + categorical_features])
    y_true = test_df[target_column]
    return {
        "precision": precision_score(y_true, preds, zero_division=0),
        "recall": recall_score(y_true, preds, zero_division=0),
        "f1": f1_score(y_true, preds, zero_division=0),
    }


def evaluate_pipeline_clustering(
    pipeline: Pipeline,
    df: pd.DataFrame,
    numeric_features: list[str],
    categorical_features: list[str],
) -> float:
    columns = numeric_features + categorical_features
    transformed = pipeline.named_steps["preprocessor"].transform(df[columns])
    labels = pipeline.named_steps["model"].labels_
    return silhouette_score(transformed, labels)
