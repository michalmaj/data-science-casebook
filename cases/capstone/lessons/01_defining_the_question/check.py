"""Self-check for Lesson 1. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

import pytest

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


def test_list_datasets_returns_the_three_menu_options():
    assert lesson.list_datasets() == [
        "clinic_wait_times",
        "lendwell_loan_default",
        "retail_store_segments",
    ]


@pytest.mark.parametrize(
    ("name", "expected_shape", "expected_columns"),
    [
        (
            "clinic_wait_times",
            (400, 8),
            [
                "visit_id",
                "department",
                "num_patients_ahead",
                "staff_on_duty",
                "is_walk_in",
                "hour_of_day",
                "patient_age",
                "wait_time_minutes",
            ],
        ),
        (
            "lendwell_loan_default",
            (400, 9),
            [
                "loan_id",
                "loan_amount",
                "annual_income",
                "credit_score",
                "debt_to_income_ratio",
                "employment_years",
                "loan_purpose",
                "previous_defaults",
                "defaulted",
            ],
        ),
        (
            "retail_store_segments",
            (250, 8),
            [
                "store_id",
                "region",
                "store_size_sqft",
                "monthly_revenue",
                "foot_traffic",
                "avg_transaction_value",
                "return_rate",
                "inventory_turnover",
            ],
        ),
    ],
)
def test_load_dataset_shape_and_columns(name, expected_shape, expected_columns):
    df = lesson.load_dataset(name)
    assert df.shape == expected_shape
    assert list(df.columns) == expected_columns


@pytest.mark.parametrize(
    ("name", "expected_missing"),
    [
        ("clinic_wait_times", {"department": 8, "staff_on_duty": 10}),
        ("lendwell_loan_default", {"employment_years": 10}),
        ("retail_store_segments", {"foot_traffic": 8}),
    ],
)
def test_missing_value_counts_matches_known_gaps(name, expected_missing):
    df = lesson.load_dataset(name)
    counts = lesson.missing_value_counts(df)
    for column, expected_count in expected_missing.items():
        assert counts[column] == expected_count


def test_lendwell_loan_default_has_the_known_class_balance():
    df = lesson.load_dataset("lendwell_loan_default")
    value_counts = df["defaulted"].value_counts().to_dict()
    assert value_counts == {0: 337, 1: 63}
