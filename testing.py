import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("Breast_Cancer.csv") 

# ---- Test 1: Independent t-test (Tumor Size: Alive vs Dead) ----
alive = df[df['Status']=='Alive']['Tumor Size']
dead  = df[df['Status']=='Dead']['Tumor Size']

t_stat, p_val = stats.ttest_ind(alive, dead, equal_var=False)
print("=== Independent t-test: Tumor Size vs Status ===")
print("H0: Mean Tumor Size is equal for Alive and Dead patients")
print("H1: Mean Tumor Size differs between Alive and Dead")
print(f"t-statistic: {t_stat:.3f}, p-value: {p_val:.5f}")
print("Decision:", "Reject H0" if p_val < 0.05 else "Fail to Reject H0")


