"""Self-check for Lesson 2. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


def test_load_customers_renames_customer_id_column():
    customers = lesson.load_customers()
    assert customers.shape == (300, 3)
    assert list(customers.columns) == [
        "customer_id",
        "account_age_days",
        "previous_returns_count",
    ]
    assert customers.isna().sum().sum() == 0


def test_load_and_merge_orders_reads_the_clean_header():
    merged = lesson.load_and_merge_orders()
    assert merged.shape == (700, 9)
    assert list(merged.columns) == [
        "order_id",
        "product_category",
        "price",
        "discount_percent",
        "shipping_method",
        "customer_id",
        "is_returned",
        "account_age_days",
        "previous_returns_count",
    ]


def test_load_and_merge_orders_has_no_missing_values():
    merged = lesson.load_and_merge_orders()
    assert merged.isna().sum().sum() == 0


def test_load_and_merge_orders_preserves_return_rate():
    merged = lesson.load_and_merge_orders()
    assert merged["is_returned"].sum() == 98
    assert merged["is_returned"].mean() == 0.14


def test_load_and_merge_orders_matches_a_known_row():
    merged = lesson.load_and_merge_orders()
    row = merged[merged["order_id"] == "ORD-00001"].iloc[0]
    assert row["customer_id"] == "CUST-0156"
    assert row["account_age_days"] == 517
    assert row["previous_returns_count"] == 2
