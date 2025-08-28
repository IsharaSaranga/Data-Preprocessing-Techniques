import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load dataset
data = pd.read_csv("../sample_dataset.csv")

print("Original Data:\n", data.head())

# Selecting only numeric columns for scaling
numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns

# Min-Max Normalization
scaler = MinMaxScaler()
data_minmax = data.copy()
data_minmax[numeric_cols] = scaler.fit_transform(data[numeric_cols])
print("\nAfter Min-Max Normalization:\n", data_minmax.head())

# Standardization (Z-score scaling)
scaler = StandardScaler()
data_standard = data.copy()
data_standard[numeric_cols] = scaler.fit_transform(data[numeric_cols])
print("\nAfter Standardization:\n", data_standard.head())
