"""Reference solution for Lesson 7. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss
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


def risk_tier(probability: float) -> str:
    if probability < 0.15:
        return "Low"
    if probability < 0.30:
        return "Medium"
    return "High"


def risk_report(model: LogisticRegression, df: pd.DataFrame) -> pd.DataFrame:
    proba = model.predict_proba(df[FEATURE_COLUMNS])[:, 1]
    tiers = [risk_tier(p) for p in proba]
    return pd.DataFrame(
        {"order_id": df["order_id"].values, "probability": proba, "risk_tier": tiers}
    )


def tier_summary(model: LogisticRegression, df: pd.DataFrame, target_column: str) -> pd.DataFrame:
    proba = model.predict_proba(df[FEATURE_COLUMNS])[:, 1]
    tiers = [risk_tier(p) for p in proba]
    combined = pd.DataFrame(
        {"probability": proba, "risk_tier": tiers, "actual": df[target_column].values}
    )
    summary = combined.groupby("risk_tier").agg(
        count=("actual", "count"),
        mean_predicted=("probability", "mean"),
        mean_observed=("actual", "mean"),
    )
    return summary.reindex(["Low", "Medium", "High"])


def brier_score(model: LogisticRegression, df: pd.DataFrame, target_column: str) -> float:
    proba = model.predict_proba(df[FEATURE_COLUMNS])[:, 1]
    return brier_score_loss(df[target_column], proba)
