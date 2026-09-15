"""Amazon PPC analytics helpers.

This module provides a small, reusable analysis layer for the campaign,
spend-allocation, and weekly-trend datasets used by the dashboard.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent


def load_data():
    """Load the three portfolio input files."""
    campaign = pd.read_excel(BASE_DIR / "campaign_performance.xls")
    spend = pd.read_excel(BASE_DIR / "spend_allocation.xls")
    weekly = pd.read_excel(BASE_DIR / "weekly_trends.xls")
    return campaign, spend, weekly


def numeric_summary(df):
    """Return descriptive statistics for numeric campaign fields."""
    return df.select_dtypes(include="number").describe().T


def campaign_totals(df):
    """Aggregate numeric campaign metrics by campaign when available."""
    campaign_col = next(
        (c for c in df.columns if c.lower() in {"campaign", "campaign_name"}),
        None,
    )
    if campaign_col is None:
        raise ValueError("Campaign name column was not found.")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        raise ValueError("No numeric campaign metrics were found.")

    return df.groupby(campaign_col, as_index=False)[numeric_cols].sum()


if __name__ == "__main__":
    campaign_df, spend_df, weekly_df = load_data()
    print("Campaign data:", campaign_df.shape)
    print("Spend data:", spend_df.shape)
    print("Weekly data:", weekly_df.shape)
    print("\nCampaign numeric summary:")
    print(numeric_summary(campaign_df))
