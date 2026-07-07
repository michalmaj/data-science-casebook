"""Reference solution for Lesson 1. Do not open this before attempting task.py."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.xlsx"


def list_sheet_names(path: Path = DATA_PATH) -> list[str]:
    return pd.ExcelFile(path).sheet_names


def load_raw_orders_sheet(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_excel(path, sheet_name="Orders")


def target_column_name() -> str:
    return "is_returned"
