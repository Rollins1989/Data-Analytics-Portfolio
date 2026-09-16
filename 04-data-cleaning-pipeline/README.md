# Data Cleaning Pipeline

## Business Objective

Build an auditable Python workflow that identifies, validates, standardizes, and repairs common data-quality issues before downstream analysis.

## What the Pipeline Handles

- Duplicate records
- Inconsistent categorical values and whitespace
- Missing values
- Invalid dates
- Invalid numeric values
- Salary imputation
- Phone-number normalization
- Required-column validation
- JSON audit reporting
- Before/after quality visualization

## Data Provenance

The pipeline uses **synthetic employee data generated in Python** so the data-quality problems are controlled, reproducible, and safe to demonstrate publicly. It is not presented as real company or employee data.

## Quality Results

A default run generates **5,100 rows**: 5,000 base records plus 100 exact duplicates. The cleaning stage removes those duplicates, repairs the injected invalid values, and writes an auditable report to `outputs/pipeline_run_report.json`.

The report tracks:

- Rows before and after cleaning
- Duplicate rows removed
- Invalid dates found and repaired
- Missing values before and after cleaning
- Invalid numeric values repaired

Because the pipeline is deterministic with the default seed, the same run can be reproduced locally.

## Visual

![Data Quality Output](outputs/data_quality_output.png)

## Business Interpretation

Data cleaning is not just formatting. A reliable analytics workflow should make quality problems visible, apply explicit rules, preserve an audit trail, and produce analysis-ready outputs.

## Technical Workflow

```text
Synthetic raw data
      ↓
Schema validation
      ↓
Categorical standardization
      ↓
Date validation + repair
      ↓
Numeric validation + imputation
      ↓
Phone normalization
      ↓
Duplicate removal
      ↓
Quality report + visualization
      ↓
Clean CSV
```

## Tools

**Python · Pandas · NumPy · Matplotlib · Jupyter Notebook · Regex**

## Project Structure

- `notebooks/data_cleaning_pipeline.ipynb` — interactive walkthrough
- `src/data_cleaning_pipeline.py` — reusable pipeline implementation
- `data/employees_clean.xls` — project dataset artifact
- `outputs/cleaned_data.csv` — generated clean dataset
- `outputs/pipeline_run_report.json` — generated audit report
- `outputs/data_quality_output.png` — generated quality visualization

## How to Run

From `04-data-cleaning-pipeline/`:

```bash
python src/data_cleaning_pipeline.py
```

Or open `notebooks/data_cleaning_pipeline.ipynb` in Jupyter Notebook/JupyterLab.

## Skills Demonstrated

Data profiling, schema validation, missing-value handling, duplicate detection, categorical standardization, date parsing, numeric validation, regex-based normalization, reproducible synthetic-data generation, audit reporting, and visualization.
