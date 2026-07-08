"""Lesson 3 task: explore Meridian Outlet's merged order data for signal.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"


def load_and_merge_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load and merge Meridian Outlet's two sheets, same as Lesson 2.

    TODO: read the "Orders" sheet skipping the two rows above the real
    header, read the "Customers" sheet and rename "Customer ID" to
    "customer_id", then left-merge the two on "customer_id". Return the
    merged DataFrame.
    """
    raise NotImplementedError("load_and_merge_orders is not implemented yet")


def class_balance(df: pd.DataFrame) -> pd.Series:
    """Return the proportion of orders with each `is_returned` value.

    TODO: use value_counts with normalize=True on the "is_returned" column,
    then sort by index so 0 (not returned) comes before 1 (returned).
    """
    raise NotImplementedError("class_balance is not implemented yet")


def return_rate_by_category(df: pd.DataFrame) -> pd.Series:
    """Return the mean `is_returned` rate for each product_category, worst first.

    TODO: group by "product_category", take the mean of "is_returned", and
    sort descending.
    """
    raise NotImplementedError("return_rate_by_category is not implemented yet")


def correlation_with_return(df: pd.DataFrame, column: str) -> float:
    """Return the correlation between `column` and `is_returned` in `df`.

    TODO: compute the Pearson correlation between df[column] and
    df["is_returned"]. This works even though is_returned is 0/1 — pandas
    treats it as a numeric column.
    """
    raise NotImplementedError("correlation_with_return is not implemented yet")
