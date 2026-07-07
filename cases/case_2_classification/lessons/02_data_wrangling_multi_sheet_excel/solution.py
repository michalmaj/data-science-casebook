"""Reference solution for Lesson 2. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"


def load_customers(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_excel(path, sheet_name="Customers").rename(
        columns={"Customer ID": "customer_id"}
    )


def load_and_merge_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    orders = pd.read_excel(path, sheet_name="Orders", skiprows=2)
    customers = load_customers(path)
    return orders.merge(customers, on="customer_id", how="left")
