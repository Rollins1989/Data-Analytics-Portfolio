"""Reusable, auditable data-cleaning pipeline for messy tabular data."""

import re
from dataclasses import asdict, dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "outputs"


@dataclass
class CleaningReport:
    """Summary of the transformations applied during a cleaning run."""

    rows_before: int
    rows_after: int
    duplicate_rows_removed: int
    invalid_dates_found: int
    missing_values_before: int
    missing_values_after: int
    invalid_numeric_values_fixed: int


def generate_messy_data(n: int = 5000, seed: int = 77) -> pd.DataFrame:
    """Create synthetic employee data containing representative quality issues."""
    if n < 100:
        raise ValueError("n must be at least 100 so the demo issues can be injected")

    rng = np.random.default_rng(seed)
    dates = pd.Timestamp("2024-01-01") - pd.to_timedelta(
        rng.integers(0, 3650, n), unit="D"
    )
    df = pd.DataFrame(
        {
            "employee_id": [f"EMP{i:05d}" for i in range(n)],
            "name": [f"Employee {i}" for i in range(n)],
            "department": rng.choice(
                ["IT", "Finance", "Marketing", "Operations", "HR", "Sales"], n
            ),
            "age": rng.integers(20, 65, n),
            "salary": rng.uniform(30000, 200000, n).round(2),
            "hire_date": dates.strftime("%Y-%m-%d"),
            "phone": [
                f"+91 {rng.integers(7000000000, 9999999999)}" for _ in range(n)
            ],
        }
    )

    # Inject common data-quality problems.
    df.loc[:49, "age"] = -1
    df.loc[50:99, "salary"] = np.nan
    df.loc[100:149, "hire_date"] = "not-a-date"
    df.loc[150:199, "department"] = "  it  "

    # Add 100 exact duplicate rows to make duplicate detection measurable.
    return pd.concat([df, df.iloc[:100]], ignore_index=True)


def clean_phone(value):
    """Normalize Indian phone numbers to ten digits where possible."""
    if pd.isna(value):
        return pd.NA
    digits = re.sub(r"\D", "", str(value))
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits if len(digits) == 10 else pd.NA


def clean_data(df: pd.DataFrame):
    """Standardize fields, repair invalid values, remove duplicates and audit changes."""
    required = {"employee_id", "name", "department", "age", "salary", "hire_date", "phone"}
    missing_columns = required.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

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
    out["salary"] = out["salary"].fillna(
        out.groupby("department")["salary"].transform("median")
    )
    out["salary"] = out["salary"].fillna(out["salary"].median())
    out["phone"] = out["phone"].map(clean_phone)

    duplicates = int(out.duplicated().sum())
    out = out.drop_duplicates().reset_index(drop=True)
    missing_after = int(out.isna().sum().sum())

    report = CleaningReport(
        rows_before=rows_before,
        rows_after=len(out),
        duplicate_rows_removed=duplicates,
        invalid_dates_found=invalid_dates,
        missing_values_before=missing_before,
        missing_values_after=missing_after,
        invalid_numeric_values_fixed=invalid_numeric,
    )
    return out, report


def save_quality_visualization(report: CleaningReport) -> None:
    """Save a compact before/after quality summary for the project README."""
    labels = ["Rows", "Missing values"]
    before = [report.rows_before, report.missing_values_before]
    after = [report.rows_after, report.missing_values_after]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].bar(["Before", "After"], [before[0], after[0]])
    axes[0].set_title("Dataset size")
    axes[0].set_ylabel("Count")

    axes[1].bar(["Before", "After"], [before[1], after[1]])
    axes[1].set_title("Missing values")
    axes[1].set_ylabel("Count")

    fig.suptitle("Data Cleaning Quality Summary")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "data_quality_output.png", dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    raw = generate_messy_data()
    cleaned, report = clean_data(raw)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(OUTPUT_DIR / "cleaned_data.csv", index=False)
    (OUTPUT_DIR / "pipeline_run_report.json").write_text(
        pd.Series(asdict(report)).to_json(indent=2), encoding="utf-8"
    )
    save_quality_visualization(report)

    print("Data cleaning pipeline completed successfully.")
    print(pd.Series(asdict(report)))
