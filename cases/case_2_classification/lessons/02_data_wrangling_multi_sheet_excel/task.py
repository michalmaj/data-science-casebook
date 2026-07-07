"""Lesson 2 task: read both of Meridian Outlet's sheets correctly and join them.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"


def load_customers(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the "Customers" sheet and standardize its customer id column name.

    TODO: read the "Customers" sheet with pd.read_excel, then rename its
    "Customer ID" column to "customer_id" so it matches the Orders sheet's
    naming convention. Return the renamed DataFrame.
    """
    raise NotImplementedError("load_customers is not implemented yet")


def load_and_merge_orders(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the Orders sheet with its real header, then merge in customer data.

    TODO: last lesson's raw load put the title row where the header should
    be. Read the "Orders" sheet again, this time skipping the rows above
    the real header so the column names come out clean. Then call
    load_customers(path) and merge the two DataFrames on "customer_id"
    (a left join — keep every order). Return the merged DataFrame.
    """
    raise NotImplementedError("load_and_merge_orders is not implemented yet")
