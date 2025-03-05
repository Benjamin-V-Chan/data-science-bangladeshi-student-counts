import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset
df = pd.read_csv("outputs/feature_engineered_data.csv")

# Define features and target
X = df[["CLASS_SIX_AGE11", "CLASS_SEVEN_AGE12"]].fillna(0)
y = df["TOTAL_STUDENTS"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Save results
output_path = "outputs/model_performance.txt"
with open(output_path, "w") as f:
    f.write(f"Mean Absolute Error: {mae}\nMean Squared Error: {mse}\n")

print(f"Model performance saved to {output_path}")
