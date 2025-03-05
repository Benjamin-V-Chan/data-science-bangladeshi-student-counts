import pandas as pd
import os

# Load data
df = pd.read_csv("outputs/cleaned_data.csv")

# Aggregate total students per school
df["TOTAL_STUDENTS"] = df.iloc[:, 5:].sum(axis=1)

# Create percentage of students within standard age range
df["CLASS_SIX_STANDARD_AGE"] = df["CLASS_SIX_AGE11"] / df["TOTAL_STUDENTS"]

# Save feature-engineered dataset
output_path = "outputs/feature_engineered_data.csv"
os.makedirs("outputs", exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Feature-engineered dataset saved to {output_path}")
