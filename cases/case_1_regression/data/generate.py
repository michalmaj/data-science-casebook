"""Generate the synthetic Case 1 shipments dataset for TransLine Logistics.

Deterministic (fixed seed) and committed as a static CSV — every student
works from the same data. Re-run only if you intend to change the dataset
itself, and re-commit the resulting CSV.
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20260706
N_ROWS = 500
OUTPUT_PATH = Path(__file__).parent / "transport_delays.csv"

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
WEATHER_CONDITIONS = ["clear", "rain", "snow"]


def generate_shipments(rng: np.random.Generator, n_rows: int) -> pd.DataFrame:
    distance_km = rng.uniform(5, 500, n_rows).round(1)
    planned_duration_min = (distance_km * rng.uniform(1.1, 1.6, n_rows)).round(0)
    driver_experience_years = rng.integers(0, 25, n_rows).astype(float)
    num_stops = rng.integers(0, 8, n_rows)
    weekday = rng.choice(WEEKDAYS, n_rows)
    weather = rng.choice(WEATHER_CONDITIONS, n_rows, p=[0.7, 0.25, 0.05])
    vehicle_age_years = rng.integers(0, 15, n_rows)

    weather_penalty = np.select(
        [weather == "clear", weather == "rain", weather == "snow"],
        [0, 8, 25],
    )
    stop_penalty = num_stops * rng.uniform(2, 5, n_rows)
    experience_bonus = -driver_experience_years * rng.uniform(0.1, 0.4, n_rows)
    noise = rng.normal(0, 10, n_rows)

    delay_minutes = (weather_penalty + stop_penalty + experience_bonus + noise).round(1)
    actual_duration_min = (planned_duration_min + delay_minutes).round(0)

    df = pd.DataFrame(
        {
            "shipment_id": [f"SHP-{i:04d}" for i in range(1, n_rows + 1)],
            "distance_km": distance_km,
            "planned_duration_min": planned_duration_min,
            "actual_duration_min": actual_duration_min,
            "driver_experience_years": driver_experience_years,
            "num_stops": num_stops,
            "weekday": weekday,
            "weather": weather,
            "vehicle_age_years": vehicle_age_years,
            "delay_minutes": delay_minutes,
        }
    )

    # Deliberate, lesson-relevant defects: a few missing driver-experience
    # and weather values, so Lesson 1's data-quality check has something
    # real to find.
    missing_idx = rng.choice(n_rows, size=15, replace=False)
    df.loc[missing_idx[:8], "driver_experience_years"] = np.nan
    df.loc[missing_idx[8:], "weather"] = np.nan

    return df


def main() -> None:
    rng = np.random.default_rng(SEED)
    df = generate_shipments(rng, N_ROWS)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {len(df)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
