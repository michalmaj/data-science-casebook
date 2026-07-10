"""Self-check for Lesson 3. Run with `uv run pytest` in this directory.

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


@pytest.mark.parametrize(
    ("name", "expected_shape"),
    [
        ("clinic_wait_times", (400, 8)),
        ("lendwell_loan_default", (400, 9)),
        ("retail_store_segments", (250, 8)),
    ],
)
def test_load_clean_dataset_shape_and_no_missing(name, expected_shape):
    df = lesson.load_clean_dataset(name)
    assert df.shape == expected_shape
    assert df.isna().sum().sum() == 0


@pytest.mark.parametrize(
    ("name", "expected_shape", "expected_columns"),
    [
        (
            "clinic_wait_times",
            (5, 5),
            [
                "num_patients_ahead",
                "staff_on_duty",
                "hour_of_day",
                "patient_age",
                "wait_time_minutes",
            ],
        ),
        (
            "lendwell_loan_default",
            (7, 7),
            [
                "loan_amount",
                "annual_income",
                "credit_score",
                "debt_to_income_ratio",
                "employment_years",
                "previous_defaults",
                "defaulted",
            ],
        ),
        (
            "retail_store_segments",
            (6, 6),
            [
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
def test_numeric_correlations_shape_columns_and_diagonal(name, expected_shape, expected_columns):
    df = lesson.load_clean_dataset(name)
    corr = lesson.numeric_correlations(df)
    assert corr.shape == expected_shape
    assert list(corr.columns) == expected_columns
    assert list(corr.index) == expected_columns
    for column in expected_columns:
        assert abs(corr.loc[column, column] - 1.0) < 1e-9


@pytest.mark.parametrize(
    ("name", "col_a", "col_b", "expected_value"),
    [
        ("clinic_wait_times", "num_patients_ahead", "wait_time_minutes", 0.8212027396179216),
        ("lendwell_loan_default", "credit_score", "defaulted", -0.2802107743801826),
        ("lendwell_loan_default", "debt_to_income_ratio", "defaulted", 0.24167306839178965),
        ("retail_store_segments", "monthly_revenue", "foot_traffic", 0.8418692750767021),
        ("retail_store_segments", "monthly_revenue", "avg_transaction_value", 0.8440744982364937),
    ],
)
def test_numeric_correlations_matches_known_values(name, col_a, col_b, expected_value):
    df = lesson.load_clean_dataset(name)
    corr = lesson.numeric_correlations(df)
    assert abs(corr.loc[col_a, col_b] - expected_value) < 1e-9


def test_retail_store_segments_shows_some_features_matter_more_than_others():
    df = lesson.load_clean_dataset("retail_store_segments")
    corr = lesson.numeric_correlations(df)
    assert corr.loc["monthly_revenue", "foot_traffic"] > 0.8
    for column in ["store_size_sqft", "return_rate", "inventory_turnover"]:
        max_abs_corr = corr[column].drop(column).abs().max()
        assert max_abs_corr < 0.15
