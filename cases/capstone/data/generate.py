"""Generate the three synthetic capstone datasets — one per menu option.

Deterministic (fixed seed) and committed as static CSVs — every student
picks from the same menu. Re-run only if you intend to change a dataset
itself, and re-commit the resulting CSVs.
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20260710
DATA_DIR = Path(__file__).parent

DEPARTMENTS = ["General", "Pediatrics", "Urgent Care", "Cardiology"]
DEPARTMENT_PROBS = [0.4, 0.25, 0.25, 0.1]
DEPARTMENT_PENALTY = {"General": 5, "Pediatrics": 8, "Urgent Care": 15, "Cardiology": 10}


def generate_clinic_visits(rng: np.random.Generator, n_rows: int) -> pd.DataFrame:
    department = rng.choice(DEPARTMENTS, n_rows, p=DEPARTMENT_PROBS)
    num_patients_ahead = rng.integers(0, 15, n_rows)
    staff_on_duty = rng.integers(2, 8, n_rows).astype(float)
    is_walk_in = rng.choice([True, False], n_rows, p=[0.35, 0.65])
    hour_of_day = rng.integers(8, 18, n_rows)
    patient_age = rng.integers(1, 90, n_rows)

    dept_penalty = np.array([DEPARTMENT_PENALTY[d] for d in department], dtype=float)
    queue_effect = num_patients_ahead * rng.uniform(3, 6, n_rows)
    staff_relief = -staff_on_duty * rng.uniform(2, 4, n_rows)
    walkin_penalty = np.where(is_walk_in, rng.uniform(5, 15, n_rows), 0.0)
    noise = rng.normal(0, 8, n_rows)

    wait_time_minutes = (
        10 + dept_penalty + queue_effect + staff_relief + walkin_penalty + noise
    )
    wait_time_minutes = np.clip(wait_time_minutes, 2, None).round(1)

    df = pd.DataFrame(
        {
            "visit_id": [f"VISIT-{i:04d}" for i in range(1, n_rows + 1)],
            "department": department,
            "num_patients_ahead": num_patients_ahead,
            "staff_on_duty": staff_on_duty,
            "is_walk_in": is_walk_in,
            "hour_of_day": hour_of_day,
            "patient_age": patient_age,
            "wait_time_minutes": wait_time_minutes,
        }
    )

    missing_staff_idx = rng.choice(n_rows, size=10, replace=False)
    df.loc[missing_staff_idx, "staff_on_duty"] = np.nan
    remaining = np.setdiff1d(np.arange(n_rows), missing_staff_idx)
    missing_dept_idx = rng.choice(remaining, size=8, replace=False)
    df.loc[missing_dept_idx, "department"] = None

    return df


LOAN_PURPOSES = ["debt_consolidation", "home_improvement", "auto", "other"]
LOAN_PURPOSE_PROBS = [0.35, 0.25, 0.25, 0.15]
DEFAULT_OFFSET = 4.55


def generate_loans(rng: np.random.Generator, n_rows: int) -> pd.DataFrame:
    loan_amount = rng.uniform(1000, 40000, n_rows).round(0)
    annual_income = rng.uniform(20000, 150000, n_rows).round(0)
    credit_score = rng.integers(500, 820, n_rows).astype(float)
    debt_to_income_ratio = rng.uniform(0.05, 0.6, n_rows).round(3)
    employment_years = rng.integers(0, 30, n_rows).astype(float)
    loan_purpose = rng.choice(LOAN_PURPOSES, n_rows, p=LOAN_PURPOSE_PROBS)
    previous_defaults = rng.integers(0, 3, n_rows)

    risk_score = (
        -0.012 * (credit_score - 650)
        + 7 * debt_to_income_ratio
        - 0.00002 * (annual_income - 60000)
        + 0.7 * previous_defaults
        - 0.05 * employment_years
        + rng.normal(0, 1.3, n_rows)
    )
    default_prob = 1 / (1 + np.exp(-(risk_score - DEFAULT_OFFSET)))
    defaulted = (rng.uniform(0, 1, n_rows) < default_prob).astype(int)

    df = pd.DataFrame(
        {
            "loan_id": [f"LOAN-{i:04d}" for i in range(1, n_rows + 1)],
            "loan_amount": loan_amount,
            "annual_income": annual_income,
            "credit_score": credit_score,
            "debt_to_income_ratio": debt_to_income_ratio,
            "employment_years": employment_years,
            "loan_purpose": loan_purpose,
            "previous_defaults": previous_defaults,
            "defaulted": defaulted,
        }
    )

    missing_idx = rng.choice(n_rows, size=10, replace=False)
    df.loc[missing_idx, "employment_years"] = np.nan

    return df


REGIONS = ["North", "South", "East", "West"]
ARCHETYPES = ["flagship", "standard", "underperforming"]
ARCHETYPE_PROBS = [0.2, 0.55, 0.25]
REVENUE_MEAN = {"flagship": 180000, "standard": 90000, "underperforming": 40000}
TRAFFIC_MEAN = {"flagship": 12000, "standard": 6000, "underperforming": 2500}
TXN_MEAN = {"flagship": 65, "standard": 40, "underperforming": 25}


def generate_stores(rng: np.random.Generator, n_rows: int) -> pd.DataFrame:
    archetype = rng.choice(ARCHETYPES, n_rows, p=ARCHETYPE_PROBS)
    region = rng.choice(REGIONS, n_rows)
    store_size_sqft = rng.integers(1500, 12000, n_rows)

    revenue_mean = np.array([REVENUE_MEAN[a] for a in archetype], dtype=float)
    monthly_revenue = rng.normal(revenue_mean, revenue_mean * 0.15, n_rows)
    monthly_revenue = np.clip(monthly_revenue, 5000, None).round(0)

    traffic_mean = np.array([TRAFFIC_MEAN[a] for a in archetype], dtype=float)
    foot_traffic = rng.normal(traffic_mean, traffic_mean * 0.2, n_rows)
    foot_traffic = np.clip(foot_traffic, 200, None).round(0)

    txn_mean = np.array([TXN_MEAN[a] for a in archetype], dtype=float)
    avg_transaction_value = rng.normal(txn_mean, txn_mean * 0.15, n_rows)
    avg_transaction_value = np.clip(avg_transaction_value, 5, None).round(2)

    return_rate = rng.uniform(0.02, 0.12, n_rows).round(3)
    inventory_turnover = rng.uniform(2, 10, n_rows).round(2)

    df = pd.DataFrame(
        {
            "store_id": [f"STORE-{i:04d}" for i in range(1, n_rows + 1)],
            "region": region,
            "store_size_sqft": store_size_sqft,
            "monthly_revenue": monthly_revenue,
            "foot_traffic": foot_traffic,
            "avg_transaction_value": avg_transaction_value,
            "return_rate": return_rate,
            "inventory_turnover": inventory_turnover,
        }
    )

    missing_idx = rng.choice(n_rows, size=8, replace=False)
    df.loc[missing_idx, "foot_traffic"] = np.nan

    return df


def main() -> None:
    rng = np.random.default_rng(SEED)

    clinic = generate_clinic_visits(rng, 400)
    clinic.to_csv(DATA_DIR / "clinic_wait_times.csv", index=False)
    print(f"Wrote {len(clinic)} rows to {DATA_DIR / 'clinic_wait_times.csv'}")

    loans = generate_loans(rng, 400)
    loans.to_csv(DATA_DIR / "lendwell_loan_default.csv", index=False)
    print(f"Wrote {len(loans)} rows to {DATA_DIR / 'lendwell_loan_default.csv'}")

    stores = generate_stores(rng, 250)
    stores.to_csv(DATA_DIR / "retail_store_segments.csv", index=False)
    print(f"Wrote {len(stores)} rows to {DATA_DIR / 'retail_store_segments.csv'}")


if __name__ == "__main__":
    main()
