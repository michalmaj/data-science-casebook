"""Reference solution for Lesson 5. Do not open this before attempting task.py."""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
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


def predict_return(model: LogisticRegression, df: pd.DataFrame) -> np.ndarray:
    return model.predict(df[FEATURE_COLUMNS])
