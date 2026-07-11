"""Self-check for Lesson 4. Run with `uv run pytest` in this directory.

Set LESSON_MODULE=solution to check the reference solution instead of
task.py (used by CI, not by students).
"""

import importlib.util
import os
from pathlib import Path

import numpy as np
import pytest
from sklearn.metrics import mean_absolute_error

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)


@pytest.mark.parametrize(
    ("name", "expected_total", "expected_train", "expected_test"),
    [
        ("clinic_wait_times", 400, 320, 80),
        ("lendwell_loan_default", 400, 320, 80),
        ("retail_store_segments", 250, 200, 50),
    ],
)
def test_split_dataset_produces_known_sizes_with_no_overlap(
    name, expected_total, expected_train, expected_test
):
    df = lesson.load_clean_dataset(name)
    train_df, test_df = lesson.split_dataset(df)
    assert len(df) == expected_total
    assert len(train_df) == expected_train
    assert len(test_df) == expected_test
    assert len(train_df) + len(test_df) == len(df)
    assert set(train_df.index).isdisjoint(set(test_df.index))


def test_fit_regression_baseline_and_model_learns_something():
    df = lesson.load_clean_dataset("clinic_wait_times")
    train_df, _ = lesson.split_dataset(df)
    features = ["num_patients_ahead", "staff_on_duty", "hour_of_day", "patient_age"]
    target = "wait_time_minutes"

    baseline, model = lesson.fit_regression_baseline_and_model(train_df, target, features)

    assert abs(baseline - 41.521249999999995) < 1e-9
    assert len(model.coef_) == 4
    assert model.n_features_in_ == 4

    baseline_preds = np.full(len(train_df), baseline)
    model_preds = model.predict(train_df[features])
    baseline_mae = mean_absolute_error(train_df[target], baseline_preds)
    model_mae = mean_absolute_error(train_df[target], model_preds)
    assert model_mae < baseline_mae


def test_fit_classification_baseline_and_model_learns_something():
    df = lesson.load_clean_dataset("lendwell_loan_default")
    train_df, _ = lesson.split_dataset(df)
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

    assert baseline == 0
    assert list(model.classes_) == [0, 1]
    assert model.n_features_in_ == 6

    train_preds = model.predict(train_df[features])
    assert set(train_preds.tolist()) == {0, 1}


def test_fit_clustering_model_returns_expected_shape():
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

    assert model.n_clusters == 3
    assert model.cluster_centers_.shape == (3, 6)
    assert len(model.labels_) == 250
    assert sorted(set(model.labels_.tolist())) == [0, 1, 2]

    model2 = lesson.fit_clustering_model(df, features)
    assert (model.labels_ == model2.labels_).all()
