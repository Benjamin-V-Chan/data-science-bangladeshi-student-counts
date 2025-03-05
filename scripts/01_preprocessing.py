import pandas as pd
import os

# Load dataset
data_path = "data/data_resource_2018_02_05_Student_By_Age.csv"
df = pd.read_csv(data_path)

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Save cleaned dataset
output_path = "outputs/cleaned_data.csv"
os.makedirs("outputs", exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Cleaned dataset saved to {output_path}")
