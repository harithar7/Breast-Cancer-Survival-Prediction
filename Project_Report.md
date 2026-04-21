# Breast Cancer Survival Prediction: Analytical Project Report

## Student Project Report

- Project Title: Breast Cancer Survival Analysis and Baseline Prediction
- Dataset: Breast_Cancer.csv
- Tools: Python, Pandas, NumPy, SciPy, Seaborn, Matplotlib, Scikit-learn

## Abstract

This report presents a complete statistical and analytical study of a breast cancer clinical dataset. The work addresses six tasks: exploratory data analysis (EDA), visualization, correlation analysis, hypothesis testing, simple linear regression, and scenario analysis. Results show that tumor burden, nodal positivity, stage, and hormone status are strongly associated with survival outcomes, while age has weaker influence. A baseline simple linear regression model was built to predict survival months using positive regional nodes; the model captured directionally meaningful impact but showed limited predictive power, indicating that survival is multi-factorial.

## 1. Problem Statement Coverage

This report solves the following required tasks:

1. EDA
2. Visualization
3. Correlation analysis
4. Hypothesis testing
5. Linear regression
6. Scenario analysis and high-risk strategy

## 2. Methodology

## 2.1 Data Source

- Input file: Breast_Cancer.csv
- Total observations: 4024
- Total features: 16

## 2.2 Analysis Environment

- Python virtual environment (.venv)
- Statistical significance threshold: alpha = 0.05

## 2.3 Scripts Used

- EDA.py
- Visaulization.py
- Correlation.py
- testing.py
- SLR.py
- sceniro.py

## 3. Q1. Exploratory Data Analysis (EDA)

## 3.1 Dataset Structure and Quality

- Shape: 4024 rows x 16 columns
- Missing values: 0
- Duplicate rows: 1

Interpretation:
- The dataset is complete (no missing values).
- One duplicate exists and should be dropped before final modeling.

## 3.2 Summary of Key Numerical Variables

| Variable | Mean |
|---|---:|
| Age | 53.97 |
| Tumor Size | 30.47 |
| Regional Node Examined | 14.36 |
| Reginol Node Positive | 4.16 |
| Survival Months | 71.30 |

## 3.3 Distribution and Skewness

| Variable | Skewness | Interpretation |
|---|---:|---|
| Age | -0.220 | Slight left skew, near symmetric |
| Tumor Size | 1.740 | Right skewed |
| Regional Node Examined | 0.829 | Moderately right skewed |
| Reginol Node Positive | 2.703 | Strongly right skewed |
| Survival Months | -0.590 | Moderately left skewed |

EDA Conclusion:
- Node positivity and tumor size are clearly skewed and clinically imbalanced.
- These features are likely important in survival-risk stratification.

## 4. Q2. Visualization

The following visual comparisons were created between survival groups (Alive vs Dead):

1. Age distribution histogram (with hue by Status)
2. Tumor Size boxplot by Status
3. Stage countplot (6th Stage vs Status)
4. Stacked percentage bar (Estrogen Status vs Status)

Key visual patterns:
- Dead patients generally show larger tumor size.
- Higher stages (IIIA, IIIB, IIIC) show increased mortality proportions.
- Hormone-negative groups show weaker survival outcomes.

Visualization Conclusion:
- Clinical severity markers (stage, tumor size, nodal involvement, hormone negativity) consistently align with poorer outcomes.

## 5. Q3. Correlation Analysis

## 5.1 Correlation with Survival Months

| Feature | Correlation with Survival Months |
|---|---:|
| Age | -0.009 |
| Tumor Size | -0.087 |
| Regional Node Examined | -0.022 |
| Reginol Node Positive | -0.135 |

Observation:
- Reginol Node Positive has the strongest negative association with survival months among tested numeric variables.
- Linear correlations are weak to modest, suggesting multi-factor influence.

## 5.2 Numeric Association with Death (Status coded as Dead=1)

| Feature | Correlation with Dead Status |
|---|---:|
| Age | 0.056 |
| Tumor Size | 0.134 |
| Regional Node Examined | 0.035 |
| Reginol Node Positive | 0.257 |
| Survival Months | -0.477 |

Interpretation:
- Higher positive nodal burden is most associated with mortality risk among tested clinical numeric features.

## 6. Q4. Hypothesis Testing

## 6.1 Numerical Features Across Survival Groups

Test used:
- Welch two-sample t-test

For each variable:
- H0: mean(Alive) = mean(Dead)
- H1: mean(Alive) != mean(Dead)

Results:

| Variable | Alive Mean | Dead Mean | p-value | Decision (alpha=0.05) |
|---|---:|---:|---:|---|
| Age | 53.76 | 55.15 | 0.000931 | Reject H0 |
| Tumor Size | 29.27 | 37.14 | <0.000001 | Reject H0 |
| Regional Node Examined | 14.24 | 15.02 | 0.034113 | Reject H0 |
| Reginol Node Positive | 3.60 | 7.24 | <0.000001 | Reject H0 |
| Survival Months | 75.94 | 45.61 | <0.000001 | Reject H0 |

Interpretation:
- All tested numerical variables differ significantly between Alive and Dead groups.

## 6.2 Categorical Features and Survival Association

Test used:
- Chi-square test of independence

For each variable:
- H0: Variable is independent of survival status
- H1: Variable is associated with survival status

Results:

| Variable | p-value | Decision (alpha=0.05) |
|---|---:|---|
| Estrogen Status | <0.000001 | Reject H0 |
| Progesterone Status | <0.000001 | Reject H0 |
| 6th Stage | <0.000001 | Reject H0 |
| N Stage | <0.000001 | Reject H0 |
| T Stage | <0.000001 | Reject H0 |
| Race | 0.000001 | Reject H0 |
| Marital Status | 0.000011 | Reject H0 |

Interpretation:
- Survival is significantly associated with all tested categorical variables.

## 7. Q5. Simple Linear Regression

## 7.1 Model Setup

- Target variable: Survival Months
- Predictor: Reginol Node Positive
- Train-test split: 80-20
- Model: LinearRegression

## 7.2 Model Equation

Predicted Survival Months = 73.4406 - 0.5394 x (Reginol Node Positive)

Interpretation:
- Each increase of 1 in positive regional nodes reduces predicted survival by about 0.54 months.

## 7.3 Model Evaluation

- Test R2: 0.0294
- Test RMSE: 22.7766 months

Conclusion:
- The model captures correct direction but has low explanatory power.
- A single predictor is insufficient for robust survival prediction.

## 8. Q6. Scenario Analysis and High-Risk Strategy

## 8.1 Rule-Based Cohorts

High-risk definition:
- Tumor Size > 35
- Reginol Node Positive >= 4
- Estrogen Status = Negative

Low-risk definition:
- Tumor Size <= 35
- Reginol Node Positive < 4
- Estrogen Status = Positive

## 8.2 Scenario Results

| Group | N | Mortality % | Mean Survival Months |
|---|---:|---:|---:|
| High-risk | 59 | 69.49% | 42.88 |
| Low-risk | 2063 | 8.53% | 73.81 |

Interpretation:
- The high-risk cohort has dramatically higher mortality and lower survival months.

## 8.3 Stage-Wise Mortality

| Stage | Mortality % |
|---|---:|
| IIIC | 38.35 |
| IIIB | 29.85 |
| IIIA | 17.52 |
| IIB | 11.95 |
| IIA | 7.36 |

## 8.4 Data-Driven Strategy to Identify High-Risk Patients

1. Use nodal positivity, tumor size, and estrogen status as primary screening variables.
2. Escalate risk level by stage, with IIIC and IIIB as highest-priority cohorts.
3. Prioritize early intervention follow-up for patients meeting high-risk criteria.
4. Extend to a multivariable predictive model for better individual-level risk estimation.

## 9. Final Conclusion

This project successfully addresses all required analytical tasks (Q1 to Q6). The findings are consistent across EDA, visualization, correlation, hypothesis testing, and scenario analysis:

- Advanced disease burden (stage, node positivity, tumor size) is associated with poorer survival.
- Hormone status is strongly associated with outcome differences.
- Rule-based high-risk segmentation is effective and clinically interpretable.
- The baseline simple linear regression provides directional insight but limited predictive accuracy.

Overall, the project demonstrates strong statistical reasoning and a clear clinical narrative, while leaving a clear path for performance improvements using multivariable modeling.

## 10. Submission Note

This report is ready to submit as the written analytical component for the stated problem set.
