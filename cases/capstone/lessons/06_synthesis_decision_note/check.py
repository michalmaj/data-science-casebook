"""Self-check for Lesson 6. Run with `uv run pytest` in this directory.

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


def test_final_regression_scorecard_shape_and_values():
    reg_df = lesson.load_dataset("clinic_wait_times")
    train_df, test_df = lesson.split_dataset(reg_df)
    features = ["num_patients_ahead", "staff_on_duty", "hour_of_day", "patient_age"]
    train_df, test_df = lesson.impute_missing(train_df, test_df, features)
    target = "wait_time_minutes"
    baseline, model = lesson.fit_regression_baseline_and_model(train_df, target, features)
    scorecard = lesson.final_regression_scorecard(baseline, model, test_df, target, features)

    assert scorecard.shape == (2, 1)
    assert list(scorecard.index) == ["baseline", "model"]
    assert list(scorecard.columns) == ["mae"]
    assert abs(scorecard.loc["baseline", "mae"] - 18.567312499999996) < 1e-6
    assert abs(scorecard.loc["model", "mae"] - 10.600387466214906) < 1e-6
    assert scorecard.loc["model", "mae"] < scorecard.loc["baseline", "mae"]


def test_final_classification_scorecard_shape_and_values():
    clf_df = lesson.load_dataset("lendwell_loan_default")
    train_df, test_df = lesson.split_dataset(clf_df, stratify_column="defaulted")
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
    scorecard = lesson.final_classification_scorecard(baseline, model, test_df, target, features)

    assert scorecard.shape == (2, 3)
    assert list(scorecard.index) == ["baseline", "model"]
    assert list(scorecard.columns) == ["precision", "recall", "f1"]
    assert scorecard.loc["baseline", "precision"] == 0.0
    assert scorecard.loc["baseline", "recall"] == 0.0
    assert scorecard.loc["baseline", "f1"] == 0.0
    assert abs(scorecard.loc["model", "precision"] - 0.25) < 1e-9
    assert abs(scorecard.loc["model", "recall"] - 0.07692307692307693) < 1e-9
    assert abs(scorecard.loc["model", "f1"] - 0.11764705882352941) < 1e-9


def test_final_clustering_summary_shape_and_values():
    cluster_df = lesson.load_dataset("retail_store_segments")
    features = [
        "store_size_sqft",
        "monthly_revenue",
        "foot_traffic",
        "avg_transaction_value",
        "return_rate",
        "inventory_turnover",
    ]
    cluster_df, _ = lesson.impute_missing(cluster_df, cluster_df, features)
    scaled_df, _ = lesson.scale_features(cluster_df, features)
    model = lesson.fit_clustering_model(scaled_df, features)
    summary = lesson.final_clustering_summary(model, scaled_df, cluster_df, features)

    assert summary.shape == (3, 8)
    assert list(summary.index) == [0, 1, 2]
    assert list(summary.columns) == [*features, "size", "share"]
    assert sorted(summary["size"]) == [50, 92, 108]
    shares = sorted(summary["share"])
    assert abs(shares[0] - 0.2) < 1e-9
    assert abs(shares[1] - 0.368) < 1e-9
    assert abs(shares[2] - 0.432) < 1e-9
    store_sizes = sorted(summary["store_size_sqft"])
    assert abs(store_sizes[0] - 4104.076086956522) < 1e-6
    assert abs(store_sizes[1] - 6477.64) < 1e-6
    assert abs(store_sizes[2] - 9530.148148148148) < 1e-6
    revenues = sorted(summary["monthly_revenue"])
    assert abs(revenues[0] - 74347.41666666667) < 1e-6
    assert abs(revenues[1] - 76154.64130434782) < 1e-6
    assert abs(revenues[2] - 185517.22) < 1e-6


def test_final_clustering_summary_shares_sum_to_one():
    cluster_df = lesson.load_dataset("retail_store_segments")
    features = [
        "store_size_sqft",
        "monthly_revenue",
        "foot_traffic",
        "avg_transaction_value",
        "return_rate",
        "inventory_turnover",
    ]
    cluster_df, _ = lesson.impute_missing(cluster_df, cluster_df, features)
    scaled_df, _ = lesson.scale_features(cluster_df, features)
    model = lesson.fit_clustering_model(scaled_df, features)
    summary = lesson.final_clustering_summary(model, scaled_df, cluster_df, features)

    assert abs(summary["share"].sum() - 1.0) < 1e-9
