import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("Breast_Cancer.csv")


# Define high-risk profile based on aggressiveness indicators
high_risk = df[(df['Tumor Size'] > 35) &
    (df['Reginol Node Positive'] >= 4) &
    (df['Estrogen Status'] == 'Negative')]

low_risk = df[(df['Tumor Size'] <= 35) &
    (df['Reginol Node Positive'] < 4) &
    (df['Estrogen Status'] == 'Positive')]

print("High-Risk Patients:", len(high_risk))
print("High-Risk Mortality Rate: {:.2f}%".format(
    (high_risk['Status']=='Dead').mean()*100))
print("Avg Survival Months (High-Risk):", round(high_risk['Survival Months'].mean(),2))

print("\nLow-Risk Patients:", len(low_risk))
print("Low-Risk Mortality Rate: {:.2f}%".format(
    (low_risk['Status']=='Dead').mean()*100))
print("Avg Survival Months (Low-Risk):", round(low_risk['Survival Months'].mean(),2))

# Stage-wise mortality
print("\nMortality % by Cancer Stage:")
print(df.groupby('6th Stage')['Status'].apply(lambda x:(x=='Dead').mean()*100).round(2))
