"""Generate the synthetic Case 2 Meridian Outlet orders dataset (two-sheet Excel).

Deterministic (fixed seed) and committed as a static file — every student
works from the same data. Re-run only if you intend to change the dataset
itself, and re-commit the resulting file.
"""

from pathlib import Path

import numpy as np
import openpyxl
import pandas as pd

SEED = 20260707
N_CUSTOMERS = 300
N_ORDERS = 700
OUTPUT_PATH = Path(__file__).parent / "orders.xlsx"

CATEGORIES = ["clothing", "electronics", "home_goods", "books"]
CATEGORY_PROBS = [0.4, 0.25, 0.2, 0.15]
CATEGORY_PRICE_RANGE = {
    "clothing": (15, 80),
    "electronics": (50, 500),
    "home_goods": (20, 150),
    "books": (8, 30),
}


def generate_customers(rng: np.random.Generator) -> pd.DataFrame:
    account_age_days = rng.integers(1, 1000, N_CUSTOMERS)
    previous_returns_count = rng.poisson(1.5, N_CUSTOMERS)
    customer_ids = [f"CUST-{i:04d}" for i in range(1, N_CUSTOMERS + 1)]
    return pd.DataFrame(
        {
            "Customer ID": customer_ids,
            "account_age_days": account_age_days,
            "previous_returns_count": previous_returns_count,
        }
    )


def generate_orders(rng: np.random.Generator, customers_df: pd.DataFrame) -> pd.DataFrame:
    n_customers = len(customers_df)
    order_customer_idx = rng.integers(0, n_customers, N_ORDERS)
    customer_ids = customers_df["Customer ID"].to_numpy()
    account_age_days = customers_df["account_age_days"].to_numpy()
    previous_returns_count = customers_df["previous_returns_count"].to_numpy()

    product_category = rng.choice(CATEGORIES, N_ORDERS, p=CATEGORY_PROBS)
    price = np.array(
        [rng.uniform(*CATEGORY_PRICE_RANGE[c]) for c in product_category]
    ).round(2)
    discount_percent = rng.uniform(0, 50, N_ORDERS).round(1)
    shipping_method = rng.choice(["standard", "express"], N_ORDERS, p=[0.8, 0.2])

    prev_returns_for_order = previous_returns_count[order_customer_idx]
    account_age_for_order = account_age_days[order_customer_idx]

    logit = (
        -2.4
        + 0.9 * (product_category == "clothing")
        + 0.02 * discount_percent
        + 0.25 * prev_returns_for_order
        - 0.0015 * account_age_for_order
    )
    prob = 1 / (1 + np.exp(-logit))
    is_returned = (rng.uniform(0, 1, N_ORDERS) < prob).astype(int)

    order_ids = [f"ORD-{i:05d}" for i in range(1, N_ORDERS + 1)]
    order_customer_ids = customer_ids[order_customer_idx]

    return pd.DataFrame(
        {
            "order_id": order_ids,
            "product_category": product_category,
            "price": price,
            "discount_percent": discount_percent,
            "shipping_method": shipping_method,
            "customer_id": order_customer_ids,
            "is_returned": is_returned,
        }
    )


def main() -> None:
    rng = np.random.default_rng(SEED)
    customers_df = generate_customers(rng)
    orders_df = generate_orders(rng, customers_df)

    with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
        orders_df.to_excel(writer, sheet_name="Orders", index=False, startrow=2)
        customers_df.to_excel(writer, sheet_name="Customers", index=False)

    workbook = openpyxl.load_workbook(OUTPUT_PATH)
    orders_sheet = workbook["Orders"]
    orders_sheet["A1"] = "Q1 2026 Order Export"
    orders_sheet.merge_cells(
        start_row=1, start_column=1, end_row=1, end_column=len(orders_df.columns)
    )
    workbook.save(OUTPUT_PATH)

    print(f"Wrote {len(orders_df)} orders and {len(customers_df)} customers to {OUTPUT_PATH}")
    print(f"Return rate: {orders_df['is_returned'].mean():.4f}")


if __name__ == "__main__":
    main()
