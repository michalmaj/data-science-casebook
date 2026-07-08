"""Reference solution for Lesson 8. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"

RANDOM_STATE = 20260707
FEATURE_COLUMNS = ["discount_percent", "previous_returns_count", "account_age_days"]


def load_and_merge_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    orders = pd.read_excel(path, sheet_name="Orders", skiprows=2)
    customers = pd.read_excel(path, sheet_name="Customers").rename(
        columns={"Customer ID": "customer_id"}
    )
    return orders.merge(customers, on="customer_id", how="left")


def split_orders(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    train_df, test_df = train_test_split(
        df, test_size=0.2, random_state=RANDOM_STATE, stratify=df["is_returned"]
    )
    return train_df, test_df


def fit_classifier(train_df: pd.DataFrame) -> LogisticRegression:
    model = LogisticRegression()
    model.fit(train_df[FEATURE_COLUMNS], train_df["is_returned"])
    return model


def final_scorecard(
    train_df: pd.DataFrame, test_df: pd.DataFrame, model: LogisticRegression
) -> pd.DataFrame:
    majority_class = train_df["is_returned"].value_counts().idxmax()
    majority_pred = pd.Series(majority_class, index=test_df.index)

    proba = model.predict_proba(test_df[FEATURE_COLUMNS])[:, 1]
    default_pred = (proba >= 0.5).astype(int)
    chosen_pred = (proba >= 0.2).astype(int)

    actual = test_df["is_returned"]
    rows = {}
    for name, predicted in [
        ("majority_baseline", majority_pred),
        ("default_threshold_0.5", default_pred),
        ("chosen_threshold_0.2", chosen_pred),
    ]:
        rows[name] = {
            "precision": precision_score(actual, predicted, zero_division=0),
            "recall": recall_score(actual, predicted, zero_division=0),
            "f1": f1_score(actual, predicted, zero_division=0),
        }
    return pd.DataFrame(rows).T[["precision", "recall", "f1"]]
