"""Self-check for Lesson 8 (optional, LendWell only). Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

import pandas as pd

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


def _fitted_model():
    df = lesson.load_dataset()
    train_df, test_df = lesson.split_dataset(df)
    train_df, test_df = lesson.impute_missing(train_df, test_df, lesson.FEATURE_COLUMNS)
    scaled_train, scaler = lesson.scale_features(train_df, lesson.FEATURE_COLUMNS)
    baseline, model = lesson.fit_classification_baseline_and_model(
        scaled_train, lesson.TARGET_COLUMN, lesson.FEATURE_COLUMNS
    )
    return model, scaler, test_df


def test_reason_codes_ranks_and_signs_bad_applicant():
    model, scaler, _ = _fitted_model()
    bad_applicant = pd.Series(
        {
            "loan_amount": 35000,
            "annual_income": 25000,
            "credit_score": 510,
            "debt_to_income_ratio": 0.55,
            "employment_years": 1,
            "previous_defaults": 2,
        }
    )
    result = lesson.reason_codes(model, scaler, bad_applicant, lesson.FEATURE_COLUMNS, top_n=3)

    assert len(result) == 3
    assert [feature for feature, _ in result] == [
        "credit_score",
        "debt_to_income_ratio",
        "employment_years",
    ]
    assert all(contribution > 0 for _, contribution in result)
    contributions = [abs(contribution) for _, contribution in result]
    assert contributions == sorted(contributions, reverse=True)


def test_reason_code_frequency_matches_known_counts():
    model, scaler, test_df = _fitted_model()
    frequency = lesson.reason_code_frequency(
        model, scaler, test_df, lesson.FEATURE_COLUMNS, top_n=3
    )

    assert sum(frequency.values()) == 21
    assert frequency["debt_to_income_ratio"] == 7
    assert "loan_amount" not in frequency
