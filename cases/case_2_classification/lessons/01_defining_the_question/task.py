"""Lesson 1 task: get your first look at Meridian Outlet's messy order export.

Fill in each TODO below. Run `uv run pytest` in this directory to check
your work.
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"


def list_sheet_names(path: Path = DATA_PATH) -> list[str]:
    """Return the names of every sheet in the Excel file at `path`.

    TODO: use pandas.ExcelFile to open the file and return its sheet_names.
    """
    raise NotImplementedError("list_sheet_names is not implemented yet")


def load_raw_orders_sheet(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the "Orders" sheet with pandas' defaults — no cleanup yet.

    TODO: read the "Orders" sheet with pd.read_excel using its defaults
    (no skiprows). Don't try to fix what you see — that's next lesson.
    """
    raise NotImplementedError("load_raw_orders_sheet is not implemented yet")


def target_column_name() -> str:
    """Return the name of the column Meridian Outlet wants to predict.

    TODO: look at what you loaded and decide which column represents the
    business question ("will this order be returned?"). Return its exact
    column name as a string.
    """
    raise NotImplementedError("target_column_name is not implemented yet")
