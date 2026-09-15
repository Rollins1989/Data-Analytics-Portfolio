# Amazon PPC Analytics

## Overview

Campaign-performance analysis focused on advertising efficiency, budget allocation, and weekly performance trends. The project combines tabular KPI analysis with an interactive dashboard.

## Business Questions

- Which campaigns generate efficient revenue relative to spend?
- Which keyword types consume budget without comparable return?
- Where should budget be scaled, reduced, or monitored?
- How do ROAS, ACOS, CTR, CPC, and CVR change over time?

## Key Findings from the Provided Dataset

- **Brand** keywords account for about **60% of revenue** while using about **39.7% of spend**.
- **Competitor** keywords use about **31.5% of spend** but contribute only about **17.3% of revenue**.
- Brand campaigns in the campaign-level dataset show ROAS around **5.9–6.1x**, while several competitor/broad campaigns are around **2.1–2.2x**.
- Strong performers should be evaluated for additional budget, while high-ACOS campaigns should be reviewed for bid and targeting efficiency.

These are descriptive observations from the supplied dataset, not causal conclusions.

## Tools

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- HTML / JavaScript
- Chart.js

## Files

- `Project 6.ipynb` — structured analysis notebook
- `ppc_analysis.py` — reusable Python analysis helpers
- `amazon_ppc_dashboard.html` — interactive dashboard
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

Run `ppc_analysis.py` or open `Project 6.ipynb` in Jupyter. The interactive HTML dashboard can be opened directly in a browser.

> **Data note:** The repository's campaign data is treated as an analysis dataset supplied for the portfolio project. No real customer-level personal data is used in the analysis.
