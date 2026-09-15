# Data Cleaning Pipeline

## Overview

A structured data-cleaning workflow focused on identifying and correcting common data-quality problems before analysis.

## Data Quality Checks

The pipeline addresses:

- Duplicate records
- Inconsistent strings and categorical values
- Missing values
- Date parsing problems
- Salary formatting and imputation
- Invalid phone numbers
- Numeric inconsistencies
- Email validation

## Output

The cleaned dataset contains **4,800 rows and 14 columns** after duplicate removal and transformation steps.

The generated report records the issues detected and the fixes applied at each stage, making the cleaning process auditable rather than treating cleaning as an undocumented preprocessing step.

## Tools

- Python
- Pandas
- Jupyter Notebook

## Files

- `Project 4.ipynb` — cleaning workflow
- `employees_clean.xls` — cleaned dataset
- `cleaning_report.json` — data-quality report
- `Project 4_output*.png` — output visualization

## Skills Demonstrated

Data profiling, missing-value analysis, duplicate handling, categorical standardization, validation, imputation, transformation, and quality reporting.

## How to Run

Open `Project 4.ipynb` in Jupyter Notebook or JupyterLab and run the cells from top to bottom.
