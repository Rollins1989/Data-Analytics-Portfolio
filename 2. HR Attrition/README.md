# HR Employee Attrition Analysis

## Overview

An HR analytics project examining employee turnover patterns, workforce segmentation, and relationships between employee characteristics and attrition.

**Data note:** the analysis uses synthetic HR data generated for portfolio practice. It is not a real company's employee dataset.

## Business Questions

- What is the overall attrition rate?
- Which departments show higher turnover?
- How does attrition vary by workforce segment?
- Which numeric factors have the strongest relationship with attrition?
- How should correlation results be interpreted without overstating causation?

## Reference Results from the Original Analysis

- **5,000 employees** analyzed
- **21.52% overall attrition**
- The original analysis identified a higher-risk segment with **647 employees** and a **30.8% attrition rate**
- Job satisfaction, engagement, and work-life balance showed negative relationships with attrition in the original analysis

## Technical Workflow

1. Generate and validate the synthetic workforce dataset
2. Calculate workforce KPIs
3. Compare attrition across departments
4. Calculate correlations for numeric workforce variables
5. Visualize the strongest relationships
6. Interpret the findings with an explicit correlation-vs-causation caveat

## Tools

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Files

- `hr_attrition_analysis.ipynb` — cleaned, portfolio-ready analysis notebook
- `Project 2.ipynb` — removed legacy notebook; it contained unsupported resume-style claims
- `hr_cleaned.xls` — existing cleaned dataset
- `hr_summary.json` — existing summary metrics
- `Project 2_output*.png` — existing analysis output

## Skills Demonstrated

Data preparation, KPI analysis, groupby analysis, correlation analysis, workforce segmentation, visualization, and responsible interpretation of analytical results.

## How to Run

Open `hr_attrition_analysis.ipynb` in Jupyter Notebook or JupyterLab and run the cells from top to bottom.
