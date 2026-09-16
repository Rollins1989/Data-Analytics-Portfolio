# Amazon PPC Analytics

## Business Objective

Analyze advertising performance to understand spend efficiency, campaign performance, keyword-type allocation, and weekly trends for better budget and targeting decisions.

## Key Questions

- Which campaigns generate efficient revenue relative to spend?
- Which keyword types consume budget without comparable return?
- Where should budget be scaled, reduced, or monitored?
- How do ROAS, ACOS, CTR, CPC, and CVR change over time?

## Key Findings

- **Brand** keywords account for about **60% of revenue** while using about **39.7% of spend**.
- **Competitor** keywords use about **31.5% of spend** but contribute only about **17.3% of revenue**.
- Brand campaigns in the campaign-level dataset show ROAS around **5.9–6.1x**, while several competitor/broad campaigns are around **2.1–2.2x**.
- High-performing campaigns can be evaluated for additional budget while high-ACOS campaigns can be reviewed for bid and targeting efficiency.

These are descriptive observations from the supplied dataset, not causal conclusions.

## Business Interpretation

The project demonstrates how advertising data can be converted into efficiency KPIs and campaign-level insights that support budget allocation, bid management, and performance monitoring.

## Tools

**Python · Pandas · Matplotlib · Jupyter Notebook · HTML · JavaScript · Chart.js**

## Files

- `amazon_ppc_analytics.ipynb` — structured analysis notebook
- `ppc_analysis.py` — reusable Python analysis helpers
- `amazon_ppc_dashboard.html` — interactive dashboard
- `amazon_ppc_analysis_output.png` — analysis output
- `campaign_performance.xls` — campaign-level metrics
- `spend_allocation.xls` — keyword-type allocation metrics
- `weekly_trends.xls` — weekly performance metrics

## KPI Definitions

- **CTR** = Clicks / Impressions
- **CPC** = Spend / Clicks
- **CVR** = Orders / Clicks
- **ACOS** = Spend / Revenue
- **ROAS** = Revenue / Spend
- **CPA** = Spend / Orders

## How to Run

Run `ppc_analysis.py` or open `amazon_ppc_analytics.ipynb` in Jupyter. Open `amazon_ppc_dashboard.html` directly in a browser for the interactive dashboard.

> **Data note:** The campaign data is treated as a portfolio analysis dataset. No real customer-level personal data is used in the analysis.
