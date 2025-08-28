import pandas as pd

# Load dataset
data = pd.read_csv("../sample_dataset.csv")

print("Original Data with possible missing values:\n", data.head())

# Drop rows with missing values
data_dropna = data.dropna()
print("\nAfter dropping missing values:\n", data_dropna.head())

# Fill missing values with mean (for numerical columns)
data_mean = data.fillna(data.mean(numeric_only=True))
print("\nAfter filling missing values with mean:\n", data_mean.head())

# Fill missing values with mode (for categorical columns)
for col in data.select_dtypes(include=['object']).columns:
    data_mean[col].fillna(data[col].mode()[0], inplace=True)

print("\nAfter filling categorical missing values with mode:\n", data_mean.head())
