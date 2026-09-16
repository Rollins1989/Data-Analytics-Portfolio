# Data Cleaning Pipeline

## Business Objective

Build an auditable data-cleaning workflow that identifies, validates, and corrects common data-quality issues before analysis.

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

The generated report records detected issues and applied fixes, making the preprocessing workflow auditable rather than treating cleaning as an undocumented step.

## Business Interpretation

Reliable analytics depends on reliable inputs. This project demonstrates a repeatable approach to profiling, validating, cleaning, and documenting messy operational data before downstream analysis.

## Tools

**Python · Pandas · Jupyter Notebook**

## Files

- `data_cleaning_pipeline.ipynb` — cleaning workflow
- `data_cleaning_pipeline.py` — reusable cleaning script
- `employees_clean.xls` — cleaned dataset
- `cleaning_report.json` — data-quality report
- `data_quality_output.png` — output visualization

## How to Run

From the project directory:

```bash
python data_cleaning_pipeline.py
```

Or open `data_cleaning_pipeline.ipynb` in Jupyter Notebook/JupyterLab.

## Skills Demonstrated

Data profiling, missing-value analysis, duplicate handling, categorical standardization, validation, imputation, transformation, and quality reporting.
