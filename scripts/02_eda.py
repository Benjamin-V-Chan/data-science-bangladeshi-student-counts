import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("outputs/cleaned_data.csv")

# Basic statistics
print(df.describe())

# Visualizations
plt.figure(figsize=(12,6))
sns.histplot(df["CLASS_SIX_AGE11"].dropna(), bins=20, kde=True)
plt.title("Distribution of Age 11 Students in Class Six")
plt.savefig("outputs/class_six_age11_distribution.png")

# Correlation heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.savefig("outputs/correlation_heatmap.png")

print("EDA visuals saved in 'outputs/'")
