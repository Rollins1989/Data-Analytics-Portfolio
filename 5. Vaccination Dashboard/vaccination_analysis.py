"""Reusable analysis for the global vaccination dashboard."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_vaccination_data(seed=42):
    """Generate a synthetic country/month vaccination dataset."""
    rng = np.random.default_rng(seed)
    countries = ["India", "USA", "Brazil", "UK", "Germany", "France", "Japan", "Canada", "Australia", "Mexico"]
    months = pd.date_range("2021-01-01", periods=12, freq="MS")
    rows = []
    for country in countries:
        target = rng.uniform(55, 90)
        population = int(rng.uniform(20e6, 1.4e9))
        for i, month in enumerate(months):
            coverage = target / (1 + np.exp(-(i - 5) / 1.5)) + rng.normal(0, 2)
            rows.append({"country": country, "month": month, "vaccination_pct": round(float(np.clip(coverage, 0, target)), 2), "population": population})
    return pd.DataFrame(rows)


def country_summary(df):
    return (df.sort_values("month").groupby("country", as_index=False)
            .agg(final_vaccination_pct=("vaccination_pct", "last"), population=("population", "last"))
            .sort_values("final_vaccination_pct", ascending=False))


def monthly_global_trend(df):
    return df.groupby("month", as_index=False)["vaccination_pct"].mean()


def plot_dashboard(df, output="vaccination_dashboard.png"):
    summary = country_summary(df)
    trend = monthly_global_trend(df)
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    for country in summary.head(5)["country"]:
        part = df[df["country"] == country]
        axes[0, 0].plot(part["month"], part["vaccination_pct"], label=country)
    axes[0, 0].set_title("Vaccination Rollout — Top 5 Countries")
    axes[0, 0].set_ylabel("Vaccinated (%)")
    axes[0, 0].legend()
    axes[0, 1].bar(summary["country"], summary["final_vaccination_pct"])
    axes[0, 1].set_title("Final Vaccination Coverage")
    axes[0, 1].tick_params(axis="x", rotation=45)
    axes[0, 1].set_ylabel("Vaccinated (%)")
    axes[1, 0].scatter(summary["population"], summary["final_vaccination_pct"], s=80)
    axes[1, 0].set_title("Population vs Vaccination Coverage")
    axes[1, 0].set_xlabel("Population")
    axes[1, 0].set_ylabel("Vaccinated (%)")
    axes[1, 1].plot(trend["month"], trend["vaccination_pct"], marker="o")
    axes[1, 1].set_title("Global Average Trend")
    axes[1, 1].set_ylabel("Average Vaccinated (%)")
    fig.suptitle("Global Vaccination Analysis", fontsize=16)
    fig.tight_layout()
    fig.savefig(output, dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    data = generate_vaccination_data()
    print(country_summary(data).to_string(index=False))
    plot_dashboard(data)
    print("Saved vaccination_dashboard.png")
