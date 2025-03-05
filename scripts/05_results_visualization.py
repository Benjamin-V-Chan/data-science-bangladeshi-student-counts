import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load results
with open("outputs/model_performance.txt", "r") as f:
    performance_metrics = f.read()
print(performance_metrics)

# Load feature-engineered data
df = pd.read_csv("outputs/feature_engineered_data.csv")

# Scatter plot for predicted vs actual
plt.figure(figsize=(10,6))
plt.scatter(df["CLASS_SIX_AGE11"], df["TOTAL_STUDENTS"], label="Actual", alpha=0.5)
plt.xlabel("Class Six Age 11 Students")
plt.ylabel("Total Students")
plt.title("Class Six Age 11 vs. Total Students")
plt.legend()
plt.savefig("outputs/class_six_vs_total_students.png")

print("Visualization saved in 'outputs/'")
