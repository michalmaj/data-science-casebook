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
    df = lesson.load_dataset("clinic_wait_times")
    train_df, test_df = lesson.split_dataset(df)
    features = ["num_patients_ahead", "staff_on_duty", "hour_of_day", "patient_age"]
    train_df, test_df = lesson.impute_missing(train_df, test_df, features)
    target = "wait_time_minutes"

    baseline, model = lesson.fit_regression_baseline_and_model(train_df, target, features)
    result = lesson.evaluate_regression(baseline, model, test_df, target, features)

    assert abs(result["baseline_mae"] - 18.567312499999996) < 1e-9
    assert abs(result["model_mae"] - 10.600387466214906) < 1e-9
    assert result["model_mae"] < result["baseline_mae"]


def test_evaluate_classification_matches_known_values():
    df = lesson.load_dataset("lendwell_loan_default")
    train_df, test_df = lesson.split_dataset(df, stratify_column="defaulted")
    features = [
        "loan_amount",
        "annual_income",
        "credit_score",
        "debt_to_income_ratio",
        "employment_years",
        "previous_defaults",
    ]
    train_df, test_df = lesson.impute_missing(train_df, test_df, features)
    target = "defaulted"

    baseline, model = lesson.fit_classification_baseline_and_model(train_df, target, features)
    result = lesson.evaluate_classification(baseline, model, test_df, target, features)

    assert result["baseline_precision"] == 0.0
    assert result["baseline_recall"] == 0.0
    assert result["baseline_f1"] == 0.0
    assert abs(result["model_precision"] - 0.25) < 1e-9
    assert abs(result["model_recall"] - 0.07692307692307693) < 1e-9
    assert abs(result["model_f1"] - 0.11764705882352941) < 1e-9


def test_evaluate_clustering_matches_known_value():
    df = lesson.load_dataset("retail_store_segments")
    features = [
        "store_size_sqft",
        "monthly_revenue",
        "foot_traffic",
        "avg_transaction_value",
        "return_rate",
        "inventory_turnover",
    ]
    df, _ = lesson.impute_missing(df, df, features)
    scaled_df, _ = lesson.scale_features(df, features)

    model = lesson.fit_clustering_model(scaled_df, features)
    score = lesson.evaluate_clustering(model, scaled_df, features)

    assert abs(score - 0.22231830884063178) < 1e-9


def test_cluster_stability_matches_known_values():
    df = lesson.load_dataset("retail_store_segments")
    features = [
        "store_size_sqft",
        "monthly_revenue",
        "foot_traffic",
        "avg_transaction_value",
        "return_rate",
        "inventory_turnover",
    ]
    df, _ = lesson.impute_missing(df, df, features)
    scaled_df, _ = lesson.scale_features(df, features)

    stability = lesson.cluster_stability(scaled_df, features)

    assert stability.shape == (5, 2)
    assert list(stability.columns) == ["seed", "adjusted_rand_index"]
    assert list(stability["seed"]) == [0, 1, 2, 3, 4]
    expected_ari = [
        1.0,
        0.298486552621068,
        0.3099899620816333,
        0.9000942897023166,
        0.949562686665437,
    ]
    for actual, expected in zip(stability["adjusted_rand_index"], expected_ari, strict=True):
        assert abs(actual - expected) < 1e-9
