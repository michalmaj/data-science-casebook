"""Reference solution for Lesson 4. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"


def load_and_merge_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    orders = pd.read_excel(path, sheet_name="Orders", skiprows=2)
    customers = pd.read_excel(path, sheet_name="Customers").rename(
        columns={"Customer ID": "customer_id"}
    )
    return orders.merge(customers, on="customer_id", how="left")


def predict_majority_baseline(df: pd.DataFrame) -> pd.Series:
    majority_class = df["is_returned"].value_counts().idxmax()
    return pd.Series(majority_class, index=df.index)


def accuracy(actual: pd.Series, predicted: pd.Series) -> float:
    return (actual == predicted).mean()


def confusion_counts(actual: pd.Series, predicted: pd.Series) -> dict[str, int]:
    tp = int(((actual == 1) & (predicted == 1)).sum())
    fp = int(((actual == 0) & (predicted == 1)).sum())
    tn = int(((actual == 0) & (predicted == 0)).sum())
    fn = int(((actual == 1) & (predicted == 0)).sum())
    return {"tp": tp, "fp": fp, "tn": tn, "fn": fn}
