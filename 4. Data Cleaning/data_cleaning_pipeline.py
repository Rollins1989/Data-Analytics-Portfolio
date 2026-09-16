"""Reusable data-cleaning pipeline for messy tabular data."""

import re
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "outputs"


@dataclass
class CleaningReport:
    rows_before: int
    rows_after: int
    duplicate_rows_removed: int
    invalid_dates_fixed: int
    missing_values_before: int
    missing_values_after: int
    invalid_numeric_values_fixed: int


def generate_messy_data(n=5000, seed=77):
    """Create synthetic employee data containing common quality issues."""
    rng = np.random.default_rng(seed)
    dates = pd.Timestamp("2024-01-01") - pd.to_timedelta(rng.integers(0, 3650, n), unit="D")
    df = pd.DataFrame({
        "employee_id": [f"EMP{i:05d}" for i in range(n)],
        "name": [f"Employee {i}" for i in range(n)],
        "department": rng.choice(["IT", "Finance", "Marketing", "Operations", "HR", "Sales"], n),
        "age": rng.integers(20, 65, n),
        "salary": rng.uniform(30000, 200000, n).round(2),
        "hire_date": dates.strftime("%Y-%m-%d"),
        "phone": [f"+91 {rng.integers(7000000000, 9999999999)}" for _ in range(n)],
    })
    df.loc[:49, "age"] = -1
    df.loc[50:99, "salary"] = np.nan
    df.loc[100:149, "hire_date"] = "not-a-date"
    df.loc[150:199, "department"] = "  it  "
    return pd.concat([df, df.iloc[:100]], ignore_index=True)


def clean_phone(value):
    if pd.isna(value):
        return pd.NA
    digits = re.sub(r"\D", "", str(value))
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits if len(digits) == 10 else pd.NA


def clean_data(df):
    """Standardize fields, repair invalid values, remove duplicates and audit changes."""
    out = df.copy()
    rows_before = len(out)
    missing_before = int(out.isna().sum().sum())

    out["department"] = out["department"].astype("string").str.strip().str.title()
    out["hire_date"] = pd.to_datetime(out["hire_date"], errors="coerce")
    invalid_dates = int(out["hire_date"].isna().sum())
    out["hire_date"] = out["hire_date"].fillna(pd.Timestamp("2020-01-01"))

    out["age"] = pd.to_numeric(out["age"], errors="coerce")
    invalid_age = (out["age"] < 18) | (out["age"] > 80)
    invalid_numeric = int(invalid_age.sum())
    age_median = out.loc[~invalid_age, "age"].median()
    out.loc[invalid_age, "age"] = age_median

    out["salary"] = pd.to_numeric(out["salary"], errors="coerce")
    out["salary"] = out["salary"].fillna(out.groupby("department")["salary"].transform("median"))
    out["salary"] = out["salary"].fillna(out["salary"].median())
    out["phone"] = out["phone"].map(clean_phone)

    duplicates = int(out.duplicated().sum())
    out = out.drop_duplicates().reset_index(drop=True)
    missing_after = int(out.isna().sum().sum())

    report = CleaningReport(rows_before, len(out), duplicates, invalid_dates,
                            missing_before, missing_after, invalid_numeric)
    return out, report


if __name__ == "__main__":
    raw = generate_messy_data()
    cleaned, report = clean_data(raw)
    OUTPUT_DIR.mkdir(exist_ok=True)
    cleaned.to_csv(OUTPUT_DIR / "cleaned_data.csv", index=False)
    (OUTPUT_DIR / "pipeline_run_report.json").write_text(
        pd.Series(asdict(report)).to_json(indent=2)
    )
    print(pd.Series(asdict(report)))
