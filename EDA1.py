import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


#EDA
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
print("\nSummary Statistics (Categorical):\n", df.describe(include=['object', 'string']))

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


 

#Visualization

sns.set(style="whitegrid")


# Plot 1: Histogram - Age distribution by Status

plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Age', hue='Status', kde=True, bins=25, palette='Set1')
plt.title("Age Distribution by Survival Status")
plt.xlabel("Patient Age (years)")
plt.ylabel("Number of Patients")
plt.show()

# Plot 2: Boxplot - Tumor Size by Status
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='Status', y='Tumor Size', hue='Status', palette='Set2', legend=False)
plt.title("Tumor Size by Survival Status")
plt.xlabel("Survival Status")
plt.ylabel("Tumor Size")
plt.show()

# Plot 3: Bar Chart - Mortality by Cancer Stage
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='6th Stage', hue='Status', palette='coolwarm')
plt.title("Cancer Stage vs Survival Status")
plt.xticks(rotation=30)
plt.xlabel("Cancer Stage")
plt.ylabel("Number of Patients")
plt.show()

# Plot 4: Stacked Bar - Estrogen Status vs Survival
ct = pd.crosstab(df['Estrogen Status'], df['Status'], normalize='index') * 100
ct.plot(kind='bar', stacked=True, figsize=(7,5), color=['#2ecc71','#e74c3c'])
plt.title("Estrogen Status vs Survival (%)")
plt.ylabel("Percentage")
plt.show()



#Correlation 

# Pearson correlation matrix
num_df = df.select_dtypes(include=np.number)
corr = num_df.corr(method='pearson')
print("Correlation Matrix:\n", corr)

# Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Pearson Correlation Heatmap")
plt.xlabel("Clinical Features")
plt.ylabel("Clinical Features")
plt.show()



#Statistical Hypothesis Testing

# ---- Test 1: Independent t-test (Tumor Size: Alive vs Dead) ----
alive = df[df['Status']=='Alive']['Tumor Size']
dead  = df[df['Status']=='Dead']['Tumor Size']

t_stat, p_val = stats.ttest_ind(alive, dead, equal_var=False)
print("=== Independent t-test: Tumor Size vs Status ===")
print("H0: Mean Tumor Size is equal for Alive and Dead patients")
print("H1: Mean Tumor Size differs between Alive and Dead")
print(f"t-statistic: {t_stat:.3f}, p-value: {p_val:.5f}")
alpha=0.05
if p_val<alpha:
    print("\nResult: Reject the null Hypothesis")
    print("There IS a statistically significant difference in Tumor Size between Alive and Dead patients.")
else:
    print("\nResult: Fail to Reject the null Hypothesis")
    print("There is NO statistically significant difference in Tumor Size between Alive and Dead patients.")




#Simple Linear Regression

X = df[['Reginol Node Positive']]   
y = df['Survival Months']           

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

m = model.coef_[0]
c = model.intercept_
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mean_squared_error(y, y_pred))

print(f"Regression Equation: Survival Months = {m:.3f} * (Regional Node Positive) + {c:.3f}")
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.3f}")

# Regression line plot
plt.figure(figsize=(8,5))
sns.scatterplot(x=X['Reginol Node Positive'], y=y, alpha=0.4)
plt.plot(X, y_pred, color='red', linewidth=2)
plt.title("Regression: Regional Node Positive vs Survival Months")
plt.xlabel("Regional Node Positive")
plt.ylabel("Survival Months")
plt.show()





#Case Study / Scenario-Based Analysis


# Define high-risk profile based on aggressiveness indicators
high_risk = df[(df['Tumor Size'] > 35) &
    (df['Reginol Node Positive'] >= 4) &
    (df['Estrogen Status'] == 'Negative')]

low_risk = df[(df['Tumor Size'] <= 35) &
    (df['Reginol Node Positive'] < 4) &
    (df['Estrogen Status'] == 'Positive')]

print("High-Risk Patients:", len(high_risk))
print("High-Risk Mortality Rate: {:.2f}%".format((high_risk['Status']=='Dead').mean()*100))
print("Avg Survival Months (High-Risk):", round(high_risk['Survival Months'].mean(),2))

print("\nLow-Risk Patients:", len(low_risk))
print("Low-Risk Mortality Rate: {:.2f}%".format((low_risk['Status']=='Dead').mean()*100))
print("Avg Survival Months (Low-Risk):", round(low_risk['Survival Months'].mean(),2))

# Stage-wise mortality
print("\nMortality % by Cancer Stage:")
print(df.groupby('6th Stage')['Status'].apply(lambda x:(x=='Dead').mean()*100).round(2))

 
