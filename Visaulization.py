import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 



sns.set(style="whitegrid")
df = pd.read_csv("Breast_Cancer.csv")


# Plot 1: Histogram - Age distribution by Status

plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Age', hue='Status', kde=True, bins=25, palette='Set1')
plt.title("Age Distribution by Survival Status")
plt.xlabel("Patient Age (years)")
plt.ylabel("Number of Patients")
plt.show()

# Plot 2: Boxplot - Tumor Size by Status
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='Status', y='Tumor Size', palette='Set2')
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