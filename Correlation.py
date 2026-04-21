import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv("Breast_Cancer.csv") 

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