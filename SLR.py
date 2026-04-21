import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv("Breast_Cancer.csv")

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
