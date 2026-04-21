# Breast Cancer Survival Prediction Project

A complete exploratory and statistical analysis project on breast cancer clinical records, with basic predictive modeling and risk scenario analysis.

This repository contains multiple Python scripts that analyze clinical factors, visualize relationships, perform hypothesis testing, and build a baseline regression model for survival months.

## 1. Project Goals

Primary goals:
- Understand the structure and quality of the breast cancer dataset.
- Explore important clinical factors that relate to patient survival.
- Visualize relationships between tumor, staging, hormone status, and outcomes.
- Perform statistical significance testing.
- Build a baseline predictive model for survival months.
- Compare manually defined high-risk and low-risk patient scenarios.

Secondary goals:
- Build a reproducible mini analytics pipeline using separate scripts.
- Prepare a foundation for future machine learning improvements.

## 2. Repository Structure

- Breast_Cancer.csv
  - Source dataset used by all scripts.
- EDA.py
  - Data inspection, summary statistics, missing/duplicate checks, skewness, and outlier counts.
- Correlation.py
  - Pearson correlation matrix and heatmap for numeric features.
- Visaulization.py
  - Clinical visual analytics (histogram, boxplot, countplot, stacked bar).
- testing.py
  - Independent t-test to compare tumor size between Alive vs Dead groups.
- SLR.py
  - Simple linear regression for survival months using positive regional nodes.
- sceniro.py
  - Rule-based high-risk vs low-risk scenario comparison.
- README.md
  - Project documentation.

## 3. Dataset Description

File: Breast_Cancer.csv

Typical columns used in this project include:
- Age
- Race
- Marital Status
- T Stage
- N Stage
- 6th Stage
- differentiate
- Grade
- A Stage
- Tumor Size
- Estrogen Status
- Progesterone Status
- Regional Node Examined
- Reginol Node Positive
- Survival Months
- Status

Important notes:
- Some column names include spaces and mixed capitalization.
- One column is spelled as Reginol Node Positive in the dataset/scripts.
- EDA.py strips extra spaces from column names during runtime.

## 4. Technical Stack

Language:
- Python 3.9+

Libraries:
- numpy
- pandas
- matplotlib
- seaborn
- scipy
- scikit-learn

## 5. Environment Setup

## 5.1 Create and Activate Virtual Environment (Windows PowerShell)

python -m venv .venv
.\.venv\Scripts\Activate.ps1

## 5.2 Install Dependencies

pip install numpy pandas matplotlib seaborn scipy scikit-learn

Optional freeze file:

pip freeze > requirements.txt

Then later:

pip install -r requirements.txt

## 6. Execution Guide

Run scripts from the project root directory so Breast_Cancer.csv can be located correctly.

Recommended order:
1. EDA.py
2. Correlation.py
3. Visaulization.py
4. testing.py
5. SLR.py
6. sceniro.py

Commands:

python EDA.py
python Correlation.py
python Visaulization.py
python testing.py
python SLR.py
python sceniro.py

## 7. Script-by-Script Deep Dive

## 7.1 EDA.py

Purpose:
- Initial data profiling and quality checks.

What it does:
- Loads the CSV into a DataFrame.
- Trims whitespace from column names.
- Prints dataset shape and dtypes.
- Prints first 5 rows.
- Prints numerical and categorical summary statistics.
- Reports missing values.
- Reports duplicate rows and drops duplicates in-memory.
- Computes skewness for key clinical features:
  - Age
  - Tumor Size
  - Regional Node Examined
  - Survival Months
- Uses IQR rule to count outliers for the same key features.

Expected output:
- Console tables and summary lines.
- No generated files by default.

## 7.2 Correlation.py

Purpose:
- Quantify linear relationships between numeric variables.

What it does:
- Selects numeric columns only.
- Computes Pearson correlation matrix.
- Prints the matrix to console.
- Draws a heatmap with annotations.

Expected output:
- Correlation matrix in terminal.
- Heatmap window shown via matplotlib.

Interpretation tips:
- Correlation close to +1 means strong positive linear relationship.
- Correlation close to -1 means strong negative linear relationship.
- Correlation near 0 means weak linear relationship.

## 7.3 Visaulization.py

Purpose:
- Provide intuitive visual interpretation of clinical patterns.

Plots generated:
- Histogram: Age distribution by survival status.
- Boxplot: Tumor size by survival status.
- Countplot: 6th Stage vs survival status.
- Stacked bar (normalized): Estrogen status vs survival percentage.

Expected output:
- Four matplotlib visual windows rendered sequentially.

## 7.4 testing.py

Purpose:
- Check whether tumor size differs between Alive and Dead groups.

Method:
- Independent two-sample t-test with unequal variance assumption (Welch test).

Hypotheses:
- H0: Mean tumor size is equal for Alive and Dead patients.
- H1: Mean tumor size is different for Alive and Dead patients.

Decision rule:
- Reject H0 if p-value < 0.05.

Expected output:
- t-statistic
- p-value
- Decision statement

## 7.5 SLR.py

Purpose:
- Build baseline linear model for survival months.

Model definition:
- Input feature X: Reginol Node Positive
- Target y: Survival Months

What it computes:
- Linear regression fit.
- Equation slope and intercept.
- R2 score.
- RMSE.
- Scatter plot with regression line.

Important limitation:
- Model is evaluated on the same dataset used for training.
- This can overestimate performance and should be improved using train/test split.

## 7.6 sceniro.py

Purpose:
- Compare manually defined high-risk and low-risk cohorts.

Current rule logic:
- High-risk:
  - Tumor Size > 35
  - Reginol Node Positive >= 4
  - Estrogen Status == Negative
- Low-risk:
  - Tumor Size <= 35
  - Reginol Node Positive < 4
  - Estrogen Status == Positive

What it reports:
- Number of high-risk patients.
- High-risk mortality rate.
- Average survival months for high-risk.
- Number of low-risk patients.
- Low-risk mortality rate.
- Average survival months for low-risk.
- Mortality percentage by cancer stage.

## 8. End-to-End Analytical Workflow

1. Data intake and sanity checks.
2. Statistical profiling and outlier summary.
3. Correlation diagnostics for numeric features.
4. Clinical visualization for key relationships.
5. Group difference statistical testing.
6. Baseline predictive modeling.
7. Scenario-driven risk interpretation.

## 9. Current Strengths

- Covers multiple analysis layers: EDA, stats, visualization, and modeling.
- Uses clinically interpretable variables.
- Includes both inferential statistics and predictive baseline.
- Provides rule-based risk segmentation for practical interpretation.

## 10. Current Limitations

- No train/validation/test split.
- No robust preprocessing pipeline for categorical encoding and scaling.
- No model comparison across algorithms.
- No saved artifacts (plots, metrics report, trained model file).
- No automated tests for script behavior.
- File naming consistency can be improved.

## 11. Recommended Improvements to Outperform

High-impact improvements:
- Convert scripts into modular pipeline folders:
  - src/data
  - src/features
  - src/models
  - src/visualization
  - src/evaluation
- Add train_test_split and cross-validation.
- Benchmark multiple models:
  - Logistic Regression (for Status)
  - Random Forest
  - Gradient Boosting
  - XGBoost or LightGBM (optional advanced)
- Add classification metrics:
  - Accuracy, Precision, Recall, F1, ROC-AUC
- Add regression metrics on holdout test set:
  - MAE, RMSE, R2
- Save figures and metrics to output folder.
- Add reproducibility controls:
  - random_state
  - fixed package versions

Advanced improvements:
- Add SHAP explainability for model interpretation.
- Add survival analysis methods (Kaplan-Meier, Cox model).
- Build a Streamlit dashboard for interactive analysis.
- Add CI checks for lint + tests.

## 12. Reproducibility Checklist

Before running:
- Confirm Python version is 3.9 or higher.
- Confirm all dependencies are installed.
- Confirm Breast_Cancer.csv exists in project root.

For stable outputs:
- Use fixed random seeds where applicable.
- Use same library versions across environments.

## 13. Troubleshooting

Issue: ModuleNotFoundError
- Cause: Missing dependency.
- Fix: Install required libraries with pip.

Issue: FileNotFoundError for Breast_Cancer.csv
- Cause: Running script from a different working directory.
- Fix: Run commands from project root.

Issue: Plot windows do not appear
- Cause: Headless environment or backend issue.
- Fix: Use local desktop Python environment with GUI backend.

Issue: Unexpected column errors
- Cause: Column naming mismatch or modified CSV schema.
- Fix: Print df.columns and validate names before analysis.

## 14. Suggested requirements.txt

numpy
pandas
matplotlib
seaborn
scipy
scikit-learn

## 15. Suggested Next Milestones

Milestone 1:
- Add requirements.txt and basic project config.

Milestone 2:
- Implement train/test split and model benchmarks.

Milestone 3:
- Add model explainability and dashboard.

Milestone 4:
- Add report notebook and publication-quality figures.

## 16. Academic Usage Note

This project is suitable for coursework demonstrating:
- Data cleaning and EDA
- Statistical testing
- Baseline machine learning
- Clinical variable interpretation

For publication-grade work, prioritize stronger validation design, feature engineering, and explainability.

## 17. Author and Versioning

Author:
- Harithar

Version:
- v1.0 (initial script-based analytical workflow)

If you continue development, update this README with:
- Changelog
- New metrics
- New models
- Final conclusions
