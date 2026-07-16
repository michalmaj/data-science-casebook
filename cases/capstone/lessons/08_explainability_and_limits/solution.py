"""Reference solution for Lesson 8 (optional, LendWell only). Do not open before task.py."""

from collections import Counter
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
RANDOM_STATE = 42
FEATURE_COLUMNS = [
    "loan_amount",
    "annual_income",
    "credit_score",
    "debt_to_income_ratio",
    "employment_years",
    "previous_defaults",
]
TARGET_COLUMN = "defaulted"


def load_dataset(data_dir: Path = DATA_DIR) -> pd.DataFrame:
    return pd.read_csv(data_dir / "lendwell_loan_default.csv")


def split_dataset(
    df: pd.DataFrame, test_size: float = 0.2, random_state: int = RANDOM_STATE
) -> tuple[pd.DataFrame, pd.DataFrame]:
    train_df, test_df = train_test_split(
        df, test_size=test_size, random_state=random_state, stratify=df[TARGET_COLUMN]
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


def fit_classification_baseline_and_model(
    train_df: pd.DataFrame, target_column: str, feature_columns: list[str]
) -> tuple[int, LogisticRegression]:
    baseline = train_df[target_column].mode().iloc[0]
    model = LogisticRegression(max_iter=1000)
    model.fit(train_df[feature_columns], train_df[target_column])
    return baseline, model


def reason_codes(
    model: LogisticRegression,
    scaler: StandardScaler,
    applicant: pd.Series,
    feature_columns: list[str],
    top_n: int = 3,
) -> list[tuple[str, float]]:
    """Top-N features driving this applicant's prediction, ranked by |contribution|.

    contribution = coefficient (scaled-feature space) x this applicant's scaled
    value. Positive pushes the prediction toward "defaulted"; negative pushes
    toward "repaid". model and scaler must both come from a scaled fit (see
    fit_classification_baseline_and_model called on a scale_features output) —
    mixing a raw-fit model with this function produces meaningless numbers.
    """
    scaled_row = scaler.transform(applicant[feature_columns].to_frame().T)[0]
    contributions = model.coef_[0] * scaled_row
    ranked = sorted(
        zip(feature_columns, contributions, strict=True), key=lambda pair: -abs(pair[1])
    )
    return ranked[:top_n]


def reason_code_frequency(
    model: LogisticRegression,
    scaler: StandardScaler,
    test_df: pd.DataFrame,
    feature_columns: list[str],
    top_n: int = 3,
) -> dict[str, int]:
    """How often each feature appears in the top-N reasons across every applicant
    in test_df the model predicts as a default. Answers: is one feature
    dominating every denial?
    """
    scaled_test_df = test_df.copy()
    scaled_test_df[feature_columns] = scaler.transform(test_df[feature_columns])
    predictions = model.predict(scaled_test_df[feature_columns])
    frequency: Counter[str] = Counter()
    for is_denied, (_, row) in zip(predictions, test_df.iterrows(), strict=True):
        if not is_denied:
            continue
        for feature, _ in reason_codes(model, scaler, row, feature_columns, top_n=top_n):
            frequency[feature] += 1
    return dict(frequency)
