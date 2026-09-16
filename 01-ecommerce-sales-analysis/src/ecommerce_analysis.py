"""E-commerce sales analysis.

Reproducible Pandas-based analysis for the portfolio project. The included
workbook is synthetic e-commerce transaction data; results should therefore
be interpreted as an analytical demonstration rather than real company data.
"""

from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "sales_data.xls"
OUTPUT_DIR = BASE_DIR / "outputs"


def load_data(path=DATA_FILE):
    """Load transaction data and normalize the order date."""
    df = pd.read_excel(path)
    if "order_date" not in df.columns:
        raise ValueError("Expected 'order_date' column was not found.")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    return df


def build_analysis(df):
    """Build reusable revenue, customer, channel, region and discount KPIs."""
    required = {"revenue", "order_id", "is_returned", "customer_id", "category", "region", "channel", "discount"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    revenue = df["revenue"].fillna(0)
    non_zero = revenue[revenue > 0]
    summary = {
        "total_revenue": round(float(revenue.sum()), 2),
        "total_orders": int(len(df)),
        "mean_order_value": round(float(non_zero.mean()), 2),
        "median_order_value": round(float(non_zero.median()), 2),
        "return_rate_pct": round(float(df["is_returned"].mean() * 100), 2),
        "unique_customers": int(df["customer_id"].nunique()),
    }

    by_category = df.groupby("category", as_index=False).agg(revenue=("revenue", "sum"), orders=("order_id", "count")).sort_values("revenue", ascending=False)
    by_category["revenue_share_pct"] = (by_category["revenue"] / by_category["revenue"].sum() * 100).round(2)
    by_region = df.groupby("region", as_index=False).agg(revenue=("revenue", "sum"), orders=("order_id", "count")).sort_values("revenue", ascending=False)
    by_region["avg_order_value"] = (by_region["revenue"] / by_region["orders"]).round(2)
    by_channel = df.groupby("channel", as_index=False).agg(revenue=("revenue", "sum"), orders=("order_id", "count")).sort_values("revenue", ascending=False)
    monthly = df.assign(month=df["order_date"].dt.to_period("M")).groupby("month", as_index=False)["revenue"].sum()

    customer_orders = df.groupby("customer_id").size()
    customer_summary = {
        "unique_customers": int(customer_orders.size),
        "repeat_customers": int((customer_orders > 1).sum()),
        "avg_orders_per_customer": round(float(customer_orders.mean()), 2),
    }
    discount = df.assign(discount_pct=(df["discount"] * 100).round().astype(int)).groupby("discount_pct", as_index=False).agg(avg_revenue=("revenue", "mean"), orders=("order_id", "count"))
    discount["avg_revenue"] = discount["avg_revenue"].round(2)
    return {"summary": summary, "by_category": by_category, "by_region": by_region, "by_channel": by_channel, "monthly": monthly, "customer_summary": customer_summary, "discount": discount}


def save_outputs(results):
    OUTPUT_DIR.mkdir(exist_ok=True)
    for name in ("by_category", "by_region", "by_channel", "monthly", "discount"):
        results[name].to_csv(OUTPUT_DIR / f"{name}.csv", index=False)
    report = {"summary": results["summary"], "customer_summary": results["customer_summary"]}
    (OUTPUT_DIR / "analysis_summary.json").write_text(json.dumps(report, indent=2), encoding="utf-8")


def create_charts(results):
    OUTPUT_DIR.mkdir(exist_ok=True)
    results["by_category"].plot.bar(x="category", y="revenue", legend=False, title="Revenue by Category")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_by_category.png", dpi=160)
    plt.close()
    results["monthly"].plot.line(x="month", y="revenue", marker="o", legend=False, title="Monthly Revenue")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=160)
    plt.close()


def main():
    df = load_data()
    results = build_analysis(df)
    save_outputs(results)
    create_charts(results)
    summary = results["summary"]
    print(f"Total revenue: ${summary['total_revenue']:,.2f}")
    print(f"Orders: {summary['total_orders']:,}")
    print(f"Return rate: {summary['return_rate_pct']:.2f}%")
    print(f"Top category: {results['by_category'].iloc[0]['category']}")
    print(f"Top region: {results['by_region'].iloc[0]['region']}")
    print(f"Top channel: {results['by_channel'].iloc[0]['channel']}")


if __name__ == "__main__":
    main()
