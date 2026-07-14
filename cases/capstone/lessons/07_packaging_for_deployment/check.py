"""Self-check for Lesson 7 (optional). Run with `uv run pytest` in this directory.

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


def test_build_preprocessor_clinic_shape():
    df = lesson.load_dataset("clinic_wait_times")
    train_df, _ = lesson.split_dataset(df)
    numeric = lesson.NUMERIC_FEATURES["clinic_wait_times"]
    categorical = lesson.CATEGORICAL_FEATURES["clinic_wait_times"]
    preprocessor = lesson.build_preprocessor(numeric, categorical)
    transformed = preprocessor.fit_transform(train_df[numeric + categorical])
    assert transformed.shape == (320, 8)


def test_build_preprocessor_loans_shape():
    df = lesson.load_dataset("lendwell_loan_default")
    train_df, _ = lesson.split_dataset(df, stratify_column="defaulted")
    numeric = lesson.NUMERIC_FEATURES["lendwell_loan_default"]
    categorical = lesson.CATEGORICAL_FEATURES["lendwell_loan_default"]
    preprocessor = lesson.build_preprocessor(numeric, categorical)
    transformed = preprocessor.fit_transform(train_df[numeric + categorical])
    assert transformed.shape == (320, 10)


def test_build_preprocessor_retail_shape():
    df = lesson.load_dataset("retail_store_segments")
    numeric = lesson.NUMERIC_FEATURES["retail_store_segments"]
    categorical = lesson.CATEGORICAL_FEATURES["retail_store_segments"]
    preprocessor = lesson.build_preprocessor(numeric, categorical)
    transformed = preprocessor.fit_transform(df[numeric + categorical])
    assert transformed.shape == (250, 10)


def test_regression_pipeline_matches_known_mae():
    df = lesson.load_dataset("clinic_wait_times")
    train_df, test_df = lesson.split_dataset(df)
    numeric = lesson.NUMERIC_FEATURES["clinic_wait_times"]
    categorical = lesson.CATEGORICAL_FEATURES["clinic_wait_times"]
    pipeline = lesson.build_and_fit_regression_pipeline(
        train_df, "wait_time_minutes", numeric, categorical
    )
    metrics = lesson.evaluate_pipeline_regression(
        pipeline, test_df, "wait_time_minutes", numeric, categorical
    )
    assert abs(metrics["mae"] - 10.315792872775276) < 1e-6


def test_classification_pipeline_matches_known_metrics():
    df = lesson.load_dataset("lendwell_loan_default")
    train_df, test_df = lesson.split_dataset(df, stratify_column="defaulted")
    numeric = lesson.NUMERIC_FEATURES["lendwell_loan_default"]
    categorical = lesson.CATEGORICAL_FEATURES["lendwell_loan_default"]
    pipeline = lesson.build_and_fit_classification_pipeline(
        train_df, "defaulted", numeric, categorical
    )
    metrics = lesson.evaluate_pipeline_classification(
        pipeline, test_df, "defaulted", numeric, categorical
    )
    assert abs(metrics["precision"] - 0.2857142857142857) < 1e-6
    assert abs(metrics["recall"] - 0.15384615384615385) < 1e-6
    assert abs(metrics["f1"] - 0.2) < 1e-6


def test_clustering_pipeline_matches_known_silhouette_and_sizes():
    df = lesson.load_dataset("retail_store_segments")
    numeric = lesson.NUMERIC_FEATURES["retail_store_segments"]
    categorical = lesson.CATEGORICAL_FEATURES["retail_store_segments"]
    pipeline = lesson.build_and_fit_clustering_pipeline(df, numeric, categorical)
    sil = lesson.evaluate_pipeline_clustering(pipeline, df, numeric, categorical)
    assert abs(sil - 0.18963882095516987) < 1e-6
    labels = pipeline.named_steps["model"].labels_
    sizes = [int((labels == i).sum()) for i in range(3)]
    assert sizes == [90, 50, 110]
