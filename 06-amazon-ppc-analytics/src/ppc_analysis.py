"""Amazon PPC analytics helpers.

Reusable loading and summary functions for the portfolio's campaign,
spend-allocation, and weekly-trend datasets.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"


def load_data():
    """Load the three portfolio input files from the project data directory."""
    campaign = pd.read_excel(DATA_DIR / "campaign_performance.xls")
    spend = pd.read_excel(DATA_DIR / "spend_allocation.xls")
    weekly = pd.read_excel(DATA_DIR / "weekly_trends.xls")
    return campaign, spend, weekly


def numeric_summary(df):
    """Return descriptive statistics for numeric campaign fields."""
    return df.select_dtypes(include="number").describe().T


def campaign_totals(df):
    """Aggregate numeric campaign metrics by campaign name."""
    campaign_col = next((c for c in df.columns if c.lower() in {"campaign", "campaign_name"}), None)
    if campaign_col is None:
        raise ValueError("Campaign name column was not found.")
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if not numeric_cols:
        raise ValueError("No numeric campaign metrics were found.")
    return df.groupby(campaign_col, as_index=False)[numeric_cols].sum()


if __name__ == "__main__":
    campaign_df, spend_df, weekly_df = load_data()
    print("Campaign data:", campaign_df.shape)
    print("Spend allocation data:", spend_df.shape)
    print("Weekly trend data:", weekly_df.shape)
    print("\nCampaign numeric summary:")
    print(numeric_summary(campaign_df))
