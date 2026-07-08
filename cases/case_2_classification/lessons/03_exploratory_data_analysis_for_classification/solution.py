"""Reference solution for Lesson 3. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"


def load_and_merge_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    orders = pd.read_excel(path, sheet_name="Orders", skiprows=2)
    customers = pd.read_excel(path, sheet_name="Customers").rename(
        columns={"Customer ID": "customer_id"}
    )
    return orders.merge(customers, on="customer_id", how="left")


def class_balance(df: pd.DataFrame) -> pd.Series:
    return df["is_returned"].value_counts(normalize=True).sort_index()


def return_rate_by_category(df: pd.DataFrame) -> pd.Series:
    return df.groupby("product_category")["is_returned"].mean().sort_values(ascending=False)


def correlation_with_return(df: pd.DataFrame, column: str) -> float:
    return df[column].corr(df["is_returned"])
