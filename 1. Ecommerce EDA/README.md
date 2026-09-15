# E-commerce Sales Analysis

## Overview

A reproducible e-commerce exploratory analysis covering revenue, customer behavior, sales channels, regional performance, returns, and discount impact.

**Data note:** the transaction dataset is synthetic and is used to demonstrate an end-to-end analytics workflow. The results should not be presented as real company performance.

## Business Questions

- Which product categories contribute the most revenue?
- How does revenue vary over time and across regions?
- Which sales channels perform best?
- What is the return rate?
- How does discount level relate to average order revenue?
- How frequently do customers purchase?

## Key Results

- **10,000 orders** analyzed
- **$4.51M total revenue** in the supplied analysis output
- **8.23% return rate**
- **3,678 unique customers**
- **2.72 average orders per customer**
- Electronics represented **53.3% of revenue**
- Mobile was the highest-revenue channel
- West was the highest-revenue region

## Technical Workflow

1. Load and validate transaction data with Pandas
2. Parse order dates and prepare analytical fields
3. Calculate revenue and order KPIs
4. Analyze category, region, channel, customer, and discount segments
5. Export summary tables and charts

## Tools

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Files

- `Project 1.ipynb` — original exploratory notebook
- `ecommerce_analysis.py` — reproducible Pandas analysis script
- `sales_data.xls` — source dataset
- `sales_report.json` — generated summary metrics
- `Project 1_output*.png` — existing analysis outputs
- `outputs/` — generated tables and charts when the script is run

## How to Run

Install the repository dependencies, then run:

```bash
python ecommerce_analysis.py
```

Or open `Project 1.ipynb` in Jupyter Notebook/JupyterLab.

## Skills Demonstrated

Exploratory data analysis, data preparation, KPI analysis, segmentation, trend analysis, customer analysis, return analysis, visualization, and reproducible reporting.
