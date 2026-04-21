import numpy as np
import pandas as pd
# Load dataset
df = pd.read_csv("Breast_Cancer.csv")

# Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

# 1. Dataset structure
print("Shape of dataset:", df.shape)
print("\nData Types:\n", df.dtypes)
print("\nFirst 5 rows:\n", df.head())

# 2. Summary statistics
print("\nSummary Statistics (Numerical):\n", df.describe())
print("\nSummary Statistics (Categorical):\n", df.describe(include='object'))

# 3. Missing values & duplicates
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# 4. Distribution & skewness of key clinical features
key_features = ['Age', 'Tumor Size', 'Regional Node Examined', 'Survival Months']
print("\nSkewness of Key Features:")
for col in key_features:
    print(f"{col}: {df[col].skew():.3f}")

# 5. Outlier detection using IQR
print("\nOutlier Count (IQR method):")
for col in key_features:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    print(f"{col}: {len(outliers)} outliers")