"""Self-check for Lesson 5. Run with `uv run pytest` in this directory.

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


def test_evaluate_regression_beats_baseline_on_held_out_test_data():
    df = lesson.load_clean_dataset("clinic_wait_times")
    train_df, test_df = lesson.split_dataset(df)
    features = ["num_patients_ahead", "staff_on_duty", "hour_of_day", "patient_age"]
    target = "wait_time_minutes"

    baseline, model = lesson.fit_regression_baseline_and_model(train_df, target, features)
    result = lesson.evaluate_regression(baseline, model, test_df, target, features)

    assert abs(result["baseline_mae"] - 18.567312499999996) < 1e-9
    assert abs(result["model_mae"] - 10.600387466214906) < 1e-9
    assert result["model_mae"] < result["baseline_mae"]


def test_evaluate_classification_matches_known_values():
    df = lesson.load_clean_dataset("lendwell_loan_default")
    train_df, test_df = lesson.split_dataset(df)
    features = [
        "loan_amount",
        "annual_income",
        "credit_score",
        "debt_to_income_ratio",
        "employment_years",
        "previous_defaults",
    ]
    target = "defaulted"

    baseline, model = lesson.fit_classification_baseline_and_model(train_df, target, features)
    result = lesson.evaluate_classification(baseline, model, test_df, target, features)

    assert result["baseline_precision"] == 0.0
    assert result["baseline_recall"] == 0.0
    assert result["baseline_f1"] == 0.0
    assert abs(result["model_precision"] - 0.5) < 1e-9
    assert abs(result["model_recall"] - 0.07692307692307693) < 1e-9
    assert abs(result["model_f1"] - 0.13333333333333333) < 1e-9


def test_evaluate_clustering_matches_known_value():
    df = lesson.load_clean_dataset("retail_store_segments")
    features = [
        "store_size_sqft",
        "monthly_revenue",
        "foot_traffic",
        "avg_transaction_value",
        "return_rate",
        "inventory_turnover",
    ]

    model = lesson.fit_clustering_model(df, features)
    score = lesson.evaluate_clustering(model, df, features)

    assert abs(score - 0.6939991062993562) < 1e-9
